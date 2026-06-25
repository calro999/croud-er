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

export const dynamicParams = false;

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
    <div className="space-y-10 max-w-4xl mx-auto">
      {/* 戻るナビゲーション */}
      <Link
        href="/"
        className="inline-flex items-center gap-2.5 text-xs font-bold text-slate-400 hover:text-rose-400 transition-colors duration-300"
      >
        <span>←</span> <span>書庫一覧に戻る</span>
      </Link>

      {/* メイン詳細パネル - プレミアムデザイン */}
      <div className="border border-white/[0.03] bg-gradient-to-b from-[#0c0512]/40 to-[#020004]/60 rounded-3xl p-6 md:p-12 shadow-2xl space-y-10">
        
        {/* ヘッダー情報 */}
        <div className="space-y-4">
          <div className="flex flex-wrap items-center gap-2 text-[10px] font-bold text-slate-400 uppercase tracking-widest">
            <span>{post.date}</span>
            <span>•</span>
            <span className="text-rose-400">{post.maker || "単体作品"}</span>
          </div>
          <h1 className="text-2xl md:text-4xl font-extrabold leading-tight text-slate-100">
            {post.title}
          </h1>
          <div className="flex flex-wrap gap-1.5 pt-2">
            {post.labels?.map((lbl) => (
              <span key={lbl} className="bg-rose-500/5 text-rose-400 border border-rose-500/10 text-[9px] font-bold px-2.5 py-0.5 rounded-full">
                #{lbl}
              </span>
            ))}
          </div>
        </div>

        {/* 巨大アートジャケット画像 */}
        <div className="flex justify-center bg-black/40 rounded-2xl p-4 border border-white/[0.03] overflow-hidden">
          <a href={post.affiliate_url} target="_blank" rel="noopener noreferrer" className="block relative group max-w-full">
            <img
              src={post.image}
              alt={post.title}
              className="max-h-[550px] w-auto object-contain rounded-xl shadow-2xl group-hover:opacity-90 transition duration-500"
            />
            {/* ホバーガイダンス */}
            <div className="absolute inset-0 bg-[#030005]/60 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center rounded-xl">
              <span className="text-xs font-bold text-white bg-rose-500/90 border border-rose-400/20 px-5 py-3 rounded-xl shadow-2xl backdrop-blur-sm">
                公式サイトで詳細を視聴
              </span>
            </div>
          </a>
        </div>

        {/* メタ情報テーブル */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 p-6 rounded-2xl bg-white/[0.01] border border-white/[0.04] text-xs">
          <div className="space-y-1.5">
            <span className="text-slate-500 font-bold uppercase tracking-wider block text-[9px]">出演女優</span>
            <span className="text-slate-200 font-bold text-sm">
              {post.actresses?.join("、 ") || "紹介制・単体女優"}
            </span>
          </div>
          <div className="space-y-1.5">
            <span className="text-slate-500 font-bold uppercase tracking-wider block text-[9px]">作品属性</span>
            <span className="text-slate-200 font-medium">
              {post.genres?.join("、 ") || "人妻、不倫、ネトラレ"}
            </span>
          </div>
        </div>

        {/* 濃厚レビューテキスト */}
        <div className="prose prose-invert max-w-none text-slate-300 space-y-6 leading-relaxed text-sm md:text-base font-medium">
          <div
            className="review-content-html"
            dangerouslySetInnerHTML={{ __html: post.review }}
          />
        </div>

        {/* サンプル写真スライド */}
        {post.sample_images && post.sample_images.length > 0 && (
          <div className="space-y-4 pt-4 border-t border-white/[0.03]">
            <h3 className="text-xs font-bold text-slate-400 uppercase tracking-widest">
              ▼ 現場の瞬間（サンプル写真）
            </h3>
            <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-3.5">
              {post.sample_images.map((imgUrl, idx) => (
                <a
                  key={idx}
                  href={post.affiliate_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="block aspect-video relative overflow-hidden rounded-xl border border-white/[0.04] bg-black hover:border-rose-500/50 transition-colors duration-300"
                >
                  <img
                    src={imgUrl}
                    alt={`Sample ${idx}`}
                    className="w-full h-full object-cover opacity-80 hover:opacity-100 transition duration-300"
                    loading="lazy"
                  />
                </a>
              ))}
            </div>
          </div>
        )}

        {/* 極上のプレミアムCTAボタン */}
        <div className="pt-8 border-t border-white/[0.03] text-center space-y-4">
          <a
            href={post.affiliate_url}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-block px-10 py-5 text-lg font-extrabold text-white bg-gradient-to-r from-rose-500 via-rose-600 to-pink-600 hover:from-rose-400 hover:to-rose-500 rounded-2xl shadow-xl transition-all duration-300 transform hover:-translate-y-0.5 cursor-pointer"
          >
            🔥 この作品の全貌を視聴する！
          </a>
          <p className="text-[10px] text-slate-500">
            ※クリックするとFANZA（18禁公式サイト）へ直接遷移します
          </p>
        </div>

      </div>
    </div>
  );
}
