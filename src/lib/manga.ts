import fs from "fs";
import path from "path";

export interface MangaPostSummary {
  id: string;
  hinban?: string;
  title: string;
  review: string;
  image: string;
  sample_images?: string[];
  affiliate_url: string;
  tachiyomi_url?: string;
  genres: string[];
  author: string[];
  publisher?: string;
  date: string;
  labels: string[];
}

let cachedMangaList: MangaPostSummary[] | null = null;
const mangaDetailCache = new Map<string, MangaPostSummary>();

/**
 * 全漫画データを取得（インメモリキャッシュ付き）
 */
export function getAllManga(): MangaPostSummary[] {
  if (cachedMangaList) {
    return cachedMangaList;
  }

  const mangaJsonPath = path.join(process.cwd(), "public", "data", "manga.json");
  if (fs.existsSync(mangaJsonPath)) {
    try {
      const content = fs.readFileSync(mangaJsonPath, "utf-8");
      cachedMangaList = JSON.parse(content) as MangaPostSummary[];
      return cachedMangaList;
    } catch (e) {
      console.error("Failed to parse public/data/manga.json:", e);
    }
  }

  const mangaDir = path.join(process.cwd(), "src", "data", "manga");
  if (!fs.existsSync(mangaDir)) {
    cachedMangaList = [];
    return [];
  }

  try {
    const files = fs.readdirSync(mangaDir).filter(f => f.endsWith(".json"));
    const list: MangaPostSummary[] = [];
    for (const file of files) {
      try {
        const item = JSON.parse(fs.readFileSync(path.join(mangaDir, file), "utf-8")) as MangaPostSummary;
        list.push(item);
      } catch {}
    }
    list.sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
    cachedMangaList = list;
    return cachedMangaList;
  } catch {
    cachedMangaList = [];
    return [];
  }
}

/**
 * 単体漫画データを取得
 */
export function getMangaById(id: string): MangaPostSummary | null {
  if (mangaDetailCache.has(id)) {
    return mangaDetailCache.get(id) || null;
  }

  const filePath = path.join(process.cwd(), "src", "data", "manga", `${id}.json`);
  if (!fs.existsSync(filePath)) return null;

  try {
    const post = JSON.parse(fs.readFileSync(filePath, "utf-8")) as MangaPostSummary;
    mangaDetailCache.set(id, post);
    return post;
  } catch {
    return null;
  }
}

/**
 * 類似・関連する漫画作品を高精度スコアリングで取得
 */
export function getSimilarManga(
  currentManga: { id: string; author?: string[]; genres?: string[]; publisher?: string },
  limit: number = 4
): { manga: MangaPostSummary; matchReason: string; score: number }[] {
  const allManga = getAllManga();
  const currentAuthors = currentManga.author || [];
  const currentGenres = currentManga.genres || [];

  const scored: { manga: MangaPostSummary; matchReason: string; score: number }[] = [];

  for (const m of allManga) {
    if (m.id === currentManga.id) continue;

    let score = 0;
    const reasons: string[] = [];

    // 1. 同一作者 (最優先 +15点)
    if (currentAuthors.length > 0 && m.author) {
      const commonAuthor = currentAuthors.filter(a => m.author.includes(a));
      if (commonAuthor.length > 0) {
        score += 15;
        reasons.push(`同作者「${commonAuthor[0]}」の他作品`);
      }
    }

    // 2. 共通ジャンル数 (+3点/個)
    if (currentGenres.length > 0 && m.genres) {
      const commonGenres = currentGenres.filter(g => m.genres.includes(g));
      if (commonGenres.length > 0) {
        score += commonGenres.length * 3;
        if (reasons.length === 0) {
          reasons.push(`同ジャンル「${commonGenres[0]}」`);
        }
      }
    }

    // 3. 同一レーベル/出版社 (+2点)
    if (currentManga.publisher && m.publisher && currentManga.publisher === m.publisher) {
      score += 2;
      if (reasons.length === 0) {
        reasons.push(`${currentManga.publisher} レーベル作`);
      }
    }

    if (score > 0) {
      scored.push({
        manga: m,
        score,
        matchReason: reasons[0] || "おすすめ人気漫画"
      });
    }
  }

  scored.sort((a, b) => b.score - a.score);

  // 足りない場合は最新の人気漫画で補完
  if (scored.length < limit) {
    for (const m of allManga) {
      if (m.id === currentManga.id || scored.some(s => s.manga.id === m.id)) continue;
      scored.push({
        manga: m,
        score: 1,
        matchReason: "注目の人気コミック"
      });
      if (scored.length >= limit) break;
    }
  }

  return scored.slice(0, limit);
}
