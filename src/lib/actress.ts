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
 * 類似女優を取得（同系統のカップサイズ、共通監督、メーカー、ジャンル傾向から詳細なおすすめ理由を生成）
 */
export function getSimilarActresses(currentName: string, limit = 4): { name: string; image?: string; cup?: string; reason: string }[] {
  const current = getActressWikiData(currentName);
  const allNames = getAllActressNames();
  const candidates: { name: string; image?: string; cup?: string; score: number; reason: string }[] = [];

  // 現在の女優の主要出演ジャンル
  const currentGenres = new Set<string>();
  if (current?.works) {
    for (const w of current.works) {
      for (const g of w.genres || []) {
        if (!["ハイビジョン", "4K", "単体作品", "完全版", "独占配信", "大容量"].includes(g)) {
          currentGenres.add(g);
        }
      }
    }
  }

  for (const name of allNames) {
    if (name === currentName) continue;
    const other = getActressWikiData(name);
    if (!other) continue;

    let score = 0;
    const reasons: string[] = [];

    // 1. カップサイズの一致
    if (current?.cup && other.cup && current.cup === other.cup) {
      score += 4;
      reasons.push(`${current.cup}カップの迫力ボディ`);
    }

    // 2. 共通監督の存在
    if (current?.directors && other.directors) {
      const commonDirectors = current.directors.filter(d => other.directors.includes(d));
      if (commonDirectors.length > 0) {
        score += 3;
        reasons.push(`名匠『${commonDirectors[0]}監督』作品で魅せる迫真の演技力`);
      }
    }

    // 3. 共通ジャンル傾向
    if (other.works) {
      const otherGenres = new Set<string>();
      for (const w of other.works) {
        for (const g of w.genres || []) otherGenres.add(g);
      }
      const sharedGenres = [...currentGenres].filter(g => otherGenres.has(g));
      if (sharedGenres.length > 0) {
        score += 2;
        reasons.push(`『${sharedGenres.slice(0, 2).join('・')}』での濃厚な絡み`);
      }
    }

    // 4. スタイル・雰囲気の魅力フォールバック
    let finalReason = reasons.length > 0 ? reasons.join(' ＆ ') : "同系統の圧倒的プロポーションと演技力";
    if (other.cup && !finalReason.includes("カップ")) {
      finalReason = `【${other.cup}カップ】${finalReason}`;
    }

    candidates.push({
      name: other.name,
      image: other.image_large || other.image_small,
      cup: other.cup || undefined,
      score,
      reason: finalReason
    });
  }

  candidates.sort((a, b) => b.score - a.score);
  return candidates.slice(0, limit);
}
