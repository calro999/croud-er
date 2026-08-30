import fs from "fs";
import path from "path";

export interface PostSummary {
  id: string;
  hinban?: string;
  title: string;
  review: string;
  image: string;
  sample_images?: string[];
  sample_movie_url?: string;
  affiliate_url: string;
  genres: string[];
  actresses: string[];
  maker: string;
  directors?: string[];
  price?: string;
  date: string;
  labels: string[];
}

export interface PostDetail extends PostSummary {
  sample_images?: string[];
  sample_movie_url?: string;
}

// プロセス内メモリキャッシュ
let cachedSummaryPosts: PostSummary[] | null = null;
const postDetailCache = new Map<string, PostDetail>();

/**
 * 全記事のサマリー一覧を取得（インメモリキャッシュ付き）
 */
export function getAllSummaryPosts(): PostSummary[] {
  if (cachedSummaryPosts) {
    return cachedSummaryPosts;
  }

  const postsJsonPath = path.join(process.cwd(), "public", "data", "posts.json");
  if (fs.existsSync(postsJsonPath)) {
    try {
      const content = fs.readFileSync(postsJsonPath, "utf-8");
      cachedSummaryPosts = JSON.parse(content) as PostSummary[];
      return cachedSummaryPosts;
    } catch (e) {
      console.error("Failed to parse public/data/posts.json:", e);
    }
  }

  // フォールバック: src/data/posts から一度だけ構築
  const postsDir = path.join(process.cwd(), "src", "data", "posts");
  if (!fs.existsSync(postsDir)) {
    cachedSummaryPosts = [];
    return [];
  }

  try {
    const files = fs.readdirSync(postsDir).filter((f) => f.endsWith(".json"));
    const now = Date.now();
    const posts: PostSummary[] = [];

    for (const file of files) {
      try {
        const filePath = path.join(postsDir, file);
        const post = JSON.parse(fs.readFileSync(filePath, "utf-8")) as PostDetail;
        if (post.date && new Date(post.date).getTime() > now) {
          continue;
        }

        let shortReview = "";
        if (post.review) {
          shortReview = post.review.replace(/<[^>]*>?/gm, "").trim().slice(0, 120);
          if (post.review.length > 120) shortReview += "...";
        }

        posts.push({
          id: post.id,
          hinban: post.hinban || "",
          title: post.title || "",
          review: shortReview,
          image: post.image || "",
          affiliate_url: post.affiliate_url || "",
          genres: post.genres || [],
          actresses: post.actresses || [],
          maker: post.maker || "",
          directors: post.directors || [],
          price: post.price || "300~",
          date: post.date || "",
          labels: post.labels || [],
        });
      } catch {
        // skip parse error
      }
    }

    posts.sort((a, b) => new Date(b.date || 0).getTime() - new Date(a.date || 0).getTime());
    cachedSummaryPosts = posts;
    return cachedSummaryPosts;
  } catch (e) {
    console.error("Failed to load posts directory:", e);
    cachedSummaryPosts = [];
    return [];
  }
}

/**
 * 個別記事の詳細データを取得（キャッシュ付き）
 */
export function getPostById(id: string): PostDetail | null {
  if (postDetailCache.has(id)) {
    return postDetailCache.get(id)!;
  }

  const filePath = path.join(process.cwd(), "src", "data", "posts", `${id}.json`);
  if (!fs.existsSync(filePath)) {
    return null;
  }

  try {
    const post = JSON.parse(fs.readFileSync(filePath, "utf-8")) as PostDetail;
    postDetailCache.set(id, post);
    return post;
  } catch (e) {
    console.error(`Failed to read post detail for ${id}:`, e);
    return null;
  }
}

/**
 * 類似作品を取得（「この作品が好きなら次はこれ」）
 * 同一女優、同ジャンル、同監督、同メーカーの作品を関連度順にレコメンド
 */
export function getSimilarPosts(currentPost: { id: string; actresses?: string[]; genres?: string[]; maker?: string; directors?: string[] }, limit = 4): { post: PostSummary; matchReason: string }[] {
  const allPosts = getAllSummaryPosts();
  const scored: { post: PostSummary; score: number; matchReason: string }[] = [];

  const currentActresses = currentPost.actresses || [];
  const currentGenres = currentPost.genres || [];

  for (const post of allPosts) {
    if (post.id === currentPost.id) continue;

    let score = 0;
    let reasons: string[] = [];

    // 1. 同一女優 (最優先)
    if (currentActresses.length > 0 && post.actresses) {
      const commonAct = currentActresses.filter(a => post.actresses.includes(a));
      if (commonAct.length > 0) {
        score += 10;
        reasons.push(`${commonAct[0]} 出演作`);
      }
    }

    // 2. 共通ジャンル数
    if (currentGenres.length > 0 && post.genres) {
      const commonGenres = currentGenres.filter(g => post.genres.includes(g));
      if (commonGenres.length > 0) {
        score += commonGenres.length * 2;
        if (reasons.length === 0) {
          reasons.push(`同ジャンル「${commonGenres[0]}」`);
        }
      }
    }

    // 3. 同一メーカー
    if (currentPost.maker && post.maker && currentPost.maker === post.maker) {
      score += 3;
      if (reasons.length === 0) {
        reasons.push(`${currentPost.maker} 人気作`);
      }
    }

    if (score > 0) {
      scored.push({
        post,
        score,
        matchReason: reasons[0] || "おすすめ類似作品"
      });
    }
  }

  scored.sort((a, b) => b.score - a.score);

  if (scored.length < limit) {
    for (const post of allPosts) {
      if (post.id === currentPost.id || scored.some(s => s.post.id === post.id)) continue;
      scored.push({
        post,
        score: 1,
        matchReason: "話題の注目作"
      });
      if (scored.length >= limit) break;
    }
  }

  return scored.slice(0, limit);
}

/**
 * 関連作品を取得（後方互換）
 */
export function getRelatedPosts(currentPost: { id: string; actresses?: string[]; genres?: string[]; maker?: string }): PostSummary[] {
  return getSimilarPosts(currentPost, 3).map(s => s.post);
}

/**
 * 全記事のIDリストを取得（静的パス生成用）
 */
export function getAllPostIds(): string[] {
  const posts = getAllSummaryPosts();
  return posts.map((p) => p.id);
}
