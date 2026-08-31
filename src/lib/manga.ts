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

// 汎用すぎて類似度判定に向かないタグ
const GENERIC_GENRES = new Set([
  "無料作品", "単行本", "単話", "フルカラー", "EROTOON", "独占販売", "先行販売",
  "デジタル特装版", "合冊版", "分冊版"
]);

/**
 * 類似・関連する漫画作品を高精度スコアリングで取得（IDF重み付け & キャッチコピー風レコメンド）
 */
export function getSimilarManga(
  currentManga: { id: string; title: string; author?: string[]; genres?: string[]; publisher?: string },
  limit: number = 4
): { manga: MangaPostSummary; matchReason: string; score: number }[] {
  const allManga = getAllManga();
  const currentAuthors = (currentManga.author || []).map(a => a.trim()).filter(Boolean);
  const currentGenres = (currentManga.genres || []).filter(g => !GENERIC_GENRES.has(g));

  // ジャンル出現頻度のマップ（IDF用）
  const genreFreqMap: Record<string, number> = {};
  allManga.forEach(m => {
    (m.genres || []).forEach(g => {
      genreFreqMap[g] = (genreFreqMap[g] || 0) + 1;
    });
  });

  const scored: { manga: MangaPostSummary; matchReason: string; score: number }[] = [];

  for (const m of allManga) {
    if (m.id === currentManga.id) continue;

    let score = 0;
    const reasons: { priority: number; idf?: number; text: string }[] = [];

    // 1. 同一作者 (最優先 +60点)
    if (currentAuthors.length > 0 && m.author) {
      const commonAuthor = currentAuthors.filter(a => m.author.includes(a));
      if (commonAuthor.length > 0) {
        score += 60;
        reasons.push({ priority: 1, text: `✍️ 【${commonAuthor[0]}】先生が贈るもう一つの傑作！` });
      }
    }

    // 2. 特徴的ジャンルの一致（出現頻度が低いジャンルほど高加点）
    if (currentGenres.length > 0 && m.genres) {
      const targetGenres = (m.genres || []).filter(g => !GENERIC_GENRES.has(g));
      const commonGenres = currentGenres.filter(g => targetGenres.includes(g));

      for (const g of commonGenres) {
        const freq = genreFreqMap[g] || 1;
        // 希少なジャンルほどスコアを大きく（5回出現なら+25点、50回なら+5点）
        const idf = Math.max(4, Math.round(100 / (Math.sqrt(freq) + 2)));
        score += idf;
        reasons.push({
          priority: 2,
          idf,
          text: `💥 『${g}』好き悶絶！快楽に堕ちていく背徳の傑作`
        });
      }
    }

    // 3. タイトルキーワードの一致
    const cleanCurrentTitle = (currentManga.title || "").replace(/[【】\[\]（）\(\)\s]/g, "");
    const cleanMTitle = (m.title || "").replace(/[【】\[\]（）\(\)\s]/g, "");
    for (const kw of ["不倫", "人妻", "義母", "百合", "レズ", "NTR", "寝取", "催眠", "調教", "幼なじみ", "女教師", "ギャル", "妹", "姉", "後輩", "先輩", "巨乳"]) {
      if (cleanCurrentTitle.includes(kw) && cleanMTitle.includes(kw)) {
        score += 15;
        reasons.push({
          priority: 3,
          text: `🔥 『${kw}』シチュエーションが最高に刺さる注目作！`
        });
      }
    }

    // 4. 同一レーベル/出版社 (+5点)
    if (currentManga.publisher && m.publisher && currentManga.publisher === m.publisher) {
      score += 5;
      reasons.push({
        priority: 4,
        text: `🏢 レーベル【${currentManga.publisher}】が誇るハイクオリティ話題作`
      });
    }

    if (score > 0) {
      reasons.sort((a, b) => (a.priority - b.priority) || ((b.idf || 0) - (a.idf || 0)));
      scored.push({
        manga: m,
        score,
        matchReason: reasons[0]?.text || "⭐ 読者満足度トップクラスの人気コミック！"
      });
    }
  }

  // スコア順にソート
  scored.sort((a, b) => b.score - a.score);

  const finalResults: { manga: MangaPostSummary; matchReason: string; score: number }[] = [];
  const pickedIds = new Set<string>();

  for (const item of scored) {
    if (pickedIds.has(item.manga.id)) continue;
    finalResults.push(item);
    pickedIds.add(item.manga.id);
    if (finalResults.length >= limit) break;
  }

  // 足りない場合は作品一覧から補完
  if (finalResults.length < limit) {
    for (let i = 0; i < allManga.length; i++) {
      const m = allManga[i];
      if (m.id === currentManga.id || pickedIds.has(m.id)) continue;
      finalResults.push({
        manga: m,
        score: 1,
        matchReason: "⭐ FANZA屈指の高評価！一度読んだら止まらない話題作"
      });
      pickedIds.add(m.id);
      if (finalResults.length >= limit) break;
    }
  }

  return finalResults.slice(0, limit);
}
