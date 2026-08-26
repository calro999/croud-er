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
 * public/data/posts.json があればそれを1度だけロード、無ければ個別JSONから構築
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
 * 関連作品を取得（インメモリキャッシュから探索）
 */
export function getRelatedPosts(currentPost: { id: string; actresses?: string[] }): PostSummary[] {
  const allPosts = getAllSummaryPosts();
  const related: PostSummary[] = [];
  const others: PostSummary[] = [];

  const currentActresses = currentPost.actresses || [];

  for (const post of allPosts) {
    if (post.id === currentPost.id) continue;

    const hasCommonActress =
      currentActresses.length > 0 &&
      post.actresses &&
      post.actresses.some((act) => currentActresses.includes(act));

    if (hasCommonActress) {
      related.push(post);
    } else {
      others.push(post);
    }
  }

  if (related.length < 3) {
    related.push(...others.slice(0, 3 - related.length));
  }

  return related.slice(0, 3);
}

/**
 * 全記事のIDリストを取得（静的パス生成用）
 */
export function getAllPostIds(): string[] {
  const posts = getAllSummaryPosts();
  return posts.map((p) => p.id);
}
