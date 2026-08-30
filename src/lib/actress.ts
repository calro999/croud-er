import fs from "fs";
import path from "path";

export interface ActressWork {
  id: string;
  title: string;
  date: string;
  image: string;
  affiliate_url: string;
  directors: string[];
  maker: string;
  genres: string[];
  price: string;
}

export interface ActressWikiData {
  name: string;
  ruby?: string;
  fanza_id?: string | null;
  bust?: string | null;
  cup?: string | null;
  waist?: string | null;
  hip?: string | null;
  height?: string | null;
  birthday?: string | null;
  blood_type?: string | null;
  hobby?: string | null;
  prefectures?: string | null;
  image_large?: string;
  image_small?: string;
  affiliate_url: string;
  directors: string[];
  works_count: number;
  works: ActressWork[];
  updated_at?: string;
}

const ACTRESS_DATA_DIR = path.join(process.cwd(), "src", "data", "actresses");
const actressCache = new Map<string, ActressWikiData>();

/**
 * 女優のWikipedia風詳細データを取得
 */
export function getActressWikiData(actressName: string): ActressWikiData | null {
  if (actressCache.has(actressName)) {
    return actressCache.get(actressName)!;
  }

  const filePath = path.join(ACTRESS_DATA_DIR, `${actressName}.json`);
  if (!fs.existsSync(filePath)) {
    return null;
  }

  try {
    const content = fs.readFileSync(filePath, "utf-8");
    const data = JSON.parse(content) as ActressWikiData;
    actressCache.set(actressName, data);
    return data;
  } catch (e) {
    console.error(`Failed to load actress wiki data for ${actressName}:`, e);
    return null;
  }
}

/**
 * 全女優名の一覧を取得
 */
export function getAllActressNames(): string[] {
  if (!fs.existsSync(ACTRESS_DATA_DIR)) {
    return [];
  }

  try {
    const files = fs.readdirSync(ACTRESS_DATA_DIR).filter((f) => f.endsWith(".json"));
    return files.map((f) => f.replace(/\.json$/, ""));
  } catch {
    return [];
  }
}

/**
 * 類似女優を取得（同系統のカップサイズや出演ジャンル傾向から類似を抽出）
 */
export function getSimilarActresses(currentName: string, limit = 4): { name: string; image?: string; cup?: string; reason: string }[] {
  const current = getActressWikiData(currentName);
  const allNames = getAllActressNames();
  const candidates: { name: string; image?: string; cup?: string; score: number; reason: string }[] = [];

  for (const name of allNames) {
    if (name === currentName) continue;
    const other = getActressWikiData(name);
    if (!other) continue;

    let score = 0;
    let reason = "同系統の注目人気女優";

    if (current?.cup && other.cup && current.cup === other.cup) {
      score += 3;
      reason = `${current.cup}カップの極上ボディ`;
    }

    if (current?.directors && other.directors) {
      const commonDirectors = current.directors.filter(d => other.directors.includes(d));
      if (commonDirectors.length > 0) {
        score += 2;
        reason = `${commonDirectors[0]}監督作品で活躍`;
      }
    }

    candidates.push({
      name: other.name,
      image: other.image_large || other.image_small,
      cup: other.cup || undefined,
      score,
      reason
    });
  }

  candidates.sort((a, b) => b.score - a.score);
  return candidates.slice(0, limit);
}
