import fs from "fs";
import path from "path";
import Link from "next/link";
import { notFound } from "next/navigation";

interface Post {
  id: string;
  title: string;
  review: string;
  image: string;
  sample_images: string[];
  affiliate_url: string;
  genres: string[];
  actresses: string[];
  maker: string;
  date: string;
  labels: string[];
}

// 静的プリレンダリング外のIDもオンデマンドで動的生成可能にする
export const dynamicParams = true;

// 静的ルート生成用のパラメータ一覧を取得
export async function generateStaticParams() {
  const jsonPath = path.join(process.cwd(), "public", "data", "posts.json");
  if (!fs.existsSync(jsonPath)) {
    return [];
  }
  try {
    const fileContent = fs.readFileSync(jsonPath, "utf-8");
    const posts: Post[] = JSON.parse(fileContent);
    return posts.map((post) => ({
      id: post.id,
    }));
  } catch (e) {
    console.error("Failed to read posts.json for static params:", e);
    return [];
  }
}

// 個別の詳細記事ページコンポーネント
export default async function PostPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const jsonPath = path.join(process.cwd(), "public", "data", "posts.json");

  if (!fs.existsSync(jsonPath)) {
    notFound();
  }

  let post: Post | undefined;
  try {
    const fileContent = fs.readFileSync(jsonPath, "utf-8");
    const posts: Post[] = JSON.parse(fileContent);
    post = posts.find((p) => p.id === id);
  } catch (e) {
    console.error("Failed to parse posts.json in page:", e);
  }

  if (!post) {
    notFound();
  }

  return (
    <div className="space-y-8 max-w-4xl mx-auto">
      {/* 戻るリンク */}
      <Link
        href="/"
        className="inline-flex items-center gap-2 text-xs font-bold text-gray-400 hover:text-pink-500 transition"
      >
        ← 書庫一覧に戻る
      </Link>

      {/* メインセクション */}
      <div className="border border-[#2d123a] bg-[#120718]/30 rounded-2xl p-6 md:p-10 shadow-2xl space-y-8">
        
        {/* タイトルとメタデータ */}
        <div className="space-y-4">
          <div className="flex flex-wrap items-center gap-3 text-xs text-gray-400">
            <span>{post.date}</span>
            <span>•</span>
            <span className="text-pink-400 font-bold">{post.maker || "単体作品"}</span>
          </div>
          <h1 className="text-2xl md:text-4xl font-black leading-tight text-white">
            {post.title}
          </h1>
          <div className="flex flex-wrap gap-2 pt-2">
            {post.labels?.map((lbl) => (
              <span key={lbl} className="bg-pink-900/20 text-pink-400 border border-pink-900/50 text-[10px] font-bold px-2.5 py-0.5 rounded">
                #{lbl}
              </span>
            ))}
          </div>
        </div>

        {/* ジャケット画像（中央配置） */}
        <div className="flex justify-center bg-black/40 rounded-xl p-4 border border-[#2d123a]">
          <a href={post.affiliate_url} target="_blank" rel="noopener noreferrer" className="block relative group">
            <img
              src={post.image}
              alt={post.title}
              className="max-h-[500px] object-contain rounded-lg shadow-lg group-hover:opacity-90 transition"
            />
            {/* ホバーガイダンス */}
            <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition flex items-center justify-center rounded-lg">
              <span className="text-sm font-bold text-white bg-pink-600 px-4 py-2 rounded-lg shadow-lg">
                大画像で詳細を見る
              </span>
            </div>
          </a>
        </div>

        {/* 女優・ジャンル情報 */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 p-4 rounded-xl bg-[#1b0a23]/50 border border-[#371947]/50 text-xs">
          <div>
            <span className="text-gray-400 font-bold block mb-1">出演女優</span>
            <span className="text-gray-200 font-bold">
              {post.actresses?.join("、 ") || "紹介制・単体女優"}
            </span>
          </div>
          <div>
            <span className="text-gray-400 font-bold block mb-1">作品属性</span>
            <span className="text-gray-200">
              {post.genres?.join("、 ") || "人妻、不倫、ネトラレ"}
            </span>
          </div>
        </div>

        {/* LLM生成された濃厚レビュー文 */}
        <div className="prose prose-invert max-w-none text-gray-300 space-y-6 leading-relaxed">
          <div
            className="review-content-html"
            dangerouslySetInnerHTML={{ __html: post.review }}
          />
        </div>

        {/* サンプル画像スライドショー (あれば表示) */}
        {post.sample_images && post.sample_images.length > 0 && (
          <div className="space-y-4">
            <h3 className="text-sm font-black text-gray-300 tracking-wider">▼ 現場の瞬間（サンプル写真）</h3>
            <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-3">
              {post.sample_images.map((imgUrl, idx) => (
                <a
                  key={idx}
                  href={post.affiliate_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="block aspect-video relative overflow-hidden rounded border border-[#2d123a] bg-black hover:border-pink-500 transition duration-300"
                >
                  <img
                    src={imgUrl}
                    alt={`Sample ${idx}`}
                    className="w-full h-full object-cover opacity-80 hover:opacity-100 transition"
                    loading="lazy"
                  />
                </a>
              ))}
            </div>
          </div>
        )}

        {/* 巨大CTAアフィリエイトボタン */}
        <div className="pt-8 border-t border-[#2d123a]/50 text-center">
          <a
            href={post.affiliate_url}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-block px-8 py-5 text-xl font-black text-white bg-gradient-to-r from-pink-600 to-purple-600 hover:from-pink-500 hover:to-purple-500 rounded-full shadow-2xl hover:shadow-pink-600/40 transition duration-300 transform hover:-translate-y-1 cursor-pointer"
          >
            🔥 この作品の全貌を視聴する！
          </a>
          <p className="text-[10px] text-gray-500 mt-3">
            ※クリックするとFANZA（18禁商品特設サイト）へ遷移します
          </p>
        </div>

      </div>
    </div>
  );
}
