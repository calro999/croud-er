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
 * キャッチコピー風の推薦理由テンプレート
 */
const CATCHCOPY_PATTERNS = {
  author: [
    (author: string) => `✍️ ${author}先生の真骨頂！美麗作画とフェチズムの結晶`,
    (author: string) => `🔥 ${author}ファン必読！筆致が冴え渡る極上シチュエーション`,
    (author: string) => `✨ ${author}先生が描く、息をのむほど濃密な官能美`
  ],
  genre: [
    (genre: string) => `💥 『${genre}』好き悶絶！快楽に堕ちていく背徳の傑作`,
    (genre: string) => `💖 ${genre}ファン必見！感情と欲望が交錯する最高傑作`,
    (genre: string) => `🔞 濃密な『${genre}』の悦びを極限まで引き出した注目作`,
    (genre: string) => `⚡ 理性が溶ける…！『${genre}』の決定版コミック`
  ],
  publisher: [
    (pub: string) => `🏢 レーベル【${pub}】が誇るハイクオリティ話題作`,
    (pub: string) => `🏆 【${pub}】発！読者の五感を刺激するおすすめ作`
  ],
  general: [
    () => `⭐ FANZA屈指の高評価！一度読んだら止まらない傑作`,
    () => `🔥 美麗作画と濃厚エロの極致！読者満足度トップクラス`,
    () => `📖 試し読みで即堕ち者続出！今一番読まれている話題作`,
    () => `💫 興奮のツボを的確に刺激する、至福のフルカラー体験`
  ]
};

/**
 * 類似・関連する漫画作品を高精度スコアリングで取得（キャッチコピー風レコメンド）
 */
export function getSimilarManga(
  currentManga: { id: string; author?: string[]; genres?: string[]; publisher?: string },
  limit: number = 4
): { manga: MangaPostSummary; matchReason: string; score: number }[] {
  const allManga = getAllManga();
  const currentAuthors = (currentManga.author || []).map(a => a.trim()).filter(Boolean);
  const currentGenres = currentManga.genres || [];

  const scored: { manga: MangaPostSummary; matchReason: string; score: number }[] = [];

  for (const m of allManga) {
    if (m.id === currentManga.id) continue;

    let score = 0;
    let matchReason = "";

    // 決定論的乱数シード（作品ペアごとに固定）
    const seed = (currentManga.id + m.id).split("").reduce((acc, char) => acc + char.charCodeAt(0), 0);

    // 1. 同一作者 (最優先 +20点)
    if (currentAuthors.length > 0 && m.author) {
      const commonAuthor = currentAuthors.filter(a => m.author.includes(a));
      if (commonAuthor.length > 0) {
        score += 20;
        const authorName = commonAuthor[0];
        const fn = CATCHCOPY_PATTERNS.author[seed % CATCHCOPY_PATTERNS.author.length];
        matchReason = fn(authorName);
      }
    }

    // 2. 共通ジャンル数 (+4点/個)
    if (currentGenres.length > 0 && m.genres) {
      const commonGenres = currentGenres.filter(g => m.genres.includes(g));
      if (commonGenres.length > 0) {
        score += commonGenres.length * 4;
        if (!matchReason) {
          const selectedGenre = commonGenres[seed % commonGenres.length];
          const fn = CATCHCOPY_PATTERNS.genre[seed % CATCHCOPY_PATTERNS.genre.length];
          matchReason = fn(selectedGenre);
        }
      }
    }

    // 3. 同一レーベル/出版社 (+3点)
    if (currentManga.publisher && m.publisher && currentManga.publisher === m.publisher) {
      score += 3;
      if (!matchReason) {
        const fn = CATCHCOPY_PATTERNS.publisher[seed % CATCHCOPY_PATTERNS.publisher.length];
        matchReason = fn(currentManga.publisher);
      }
    }

    if (score > 0) {
      scored.push({
        manga: m,
        score,
        matchReason
      });
    }
  }

  // スコア順かつ多様性を保つためソート
  scored.sort((a, b) => b.score - a.score);

  const finalResults: { manga: MangaPostSummary; matchReason: string; score: number }[] = [];
  const pickedIds = new Set<string>();

  for (const item of scored) {
    if (pickedIds.has(item.manga.id)) continue;
    finalResults.push(item);
    pickedIds.add(item.manga.id);
    if (finalResults.length >= limit) break;
  }

  // 足りない場合は全体の漫画からバリエーション豊かに補完
  if (finalResults.length < limit) {
    for (let i = 0; i < allManga.length; i++) {
      const m = allManga[i];
      if (m.id === currentManga.id || pickedIds.has(m.id)) continue;
      const seed = (currentManga.id + m.id).split("").reduce((acc, char) => acc + char.charCodeAt(0), 0);
      const fn = CATCHCOPY_PATTERNS.general[seed % CATCHCOPY_PATTERNS.general.length];
      finalResults.push({
        manga: m,
        score: 1,
        matchReason: fn()
      });
      pickedIds.add(m.id);
      if (finalResults.length >= limit) break;
    }
  }

  return finalResults.slice(0, limit);
}
