import fs from "fs";
import path from "path";
import Link from "next/link";
import { Metadata } from "next";
import PostListContainer from "./components/PostListContainer";

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

export const metadata: Metadata = {
  alternates: {
    canonical: "/",
  },
};

function getPosts(): Post[] {
  try {
    const postsPath = path.join(process.cwd(), "public", "data", "posts.json");
    if (fs.existsSync(postsPath)) {
      const postsData = fs.readFileSync(postsPath, "utf8");
      return JSON.parse(postsData);
    }
  } catch (error) {
    console.error("Error reading posts.json in page.tsx:", error);
  }
  return [];
}

export default function Home() {
  const posts = getPosts();

  // JSON-LD 構造化データ
  // 1. WebSite 構造化データ
  const websiteSchema = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "背徳の深夜書斎",
    "alternateName": ["背徳の深夜書斎 - AV・アダルト動画レビュー・感想まとめ【FANZA厳選】"],
    "url": "https://haitoku.pages.dev",
    "potentialAction": {
      "@type": "SearchAction",
      "target": "https://haitoku.pages.dev/?q={search_term_string}",
      "query-input": "required name=search_term_string"
    }
  };

  // 2. ItemList 構造化データ
  const itemListSchema = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "FANZA AV作品レビュー一覧",
    "numberOfItems": posts.length,
    "itemListElement": posts.slice(0, 30).map((post, idx) => ({
      "@type": "ListItem",
      "position": idx + 1,
      "url": `https://haitoku.pages.dev/posts/${post.id}`,
      "name": post.title,
    })),
  };

  // 3. FAQPage 構造化データ（リッチリザルト狙い）
  const allGenres = Array.from(new Set(posts.flatMap(p => p.genres || []))).slice(0, 5);
  const allActresses = Array.from(new Set(posts.flatMap(p => p.actresses || []))).slice(0, 3);

  const faqSchema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "背徳の深夜書斎とはどんなサイトですか？",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": `FANZA（DMM）の人気AV作品を厳選レビューするサイトです。現在${posts.length}作品のレビューを掲載しており、品番検索・女優別・ジャンル別にもまとめています。`
        }
      },
      {
        "@type": "Question",
        "name": "FANZAで人気のAVジャンルは？",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": `当サイトで多く取り上げているジャンルは「${allGenres.join("・")}」などです。各ジャンルページでまとめてレビューをご確認いただけます。`
        }
      },
      {
        "@type": "Question",
        "name": "FANZAで人気のAV女優は？",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": `当サイトのレビューに登場する人気女優は「${allActresses.join("・")}」などです。各女優ページで全出演作品をまとめてご確認いただけます。`
        }
      },
      {
        "@type": "Question",
        "name": "AVの品番から作品を検索できますか？",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "はい、当サイトの検索ボックスに品番（例: SSIS-648、ABW-123など）を入力すると該当作品を検索できます。"
        }
      }
    ]
  };

  const actressCount = new Set(posts.flatMap((p) => p.actresses || [])).size;

  return (
    <>
      {/* 構造化データの埋め込み */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(websiteSchema) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(itemListSchema) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema) }}
      />

      <div className="space-y-8 md:space-y-12">
        {/* ヒーローセクション - アダルト感を極限まで薄めたモダンで上品なマガジン風 */}
        <section className="relative rounded-2xl overflow-hidden bg-gradient-to-br from-slate-800 to-slate-950 p-8 md:p-12 border border-slate-700/30 shadow-sm flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
          <div className="absolute top-0 right-0 w-[400px] h-[400px] bg-rose-500/[0.01] rounded-full filter blur-3xl pointer-events-none" />
          
          <div className="relative max-w-xl space-y-4">
            <span className="inline-flex text-[9px] font-bold tracking-widest text-rose-500 bg-rose-500/10 border border-rose-500/10 px-3 py-1 rounded">
              FANZA OFFICIAL REVIEW SITE
            </span>
            <h1 className="text-2xl md:text-4xl font-extrabold tracking-tight leading-snug text-white">
              FANZA人気AVレビュー・感想まとめ、<br />
              <span className="bg-gradient-to-r from-slate-100 via-rose-200 to-slate-200 bg-clip-text text-transparent">
                女優別・ジャンル別厳選レビュー
              </span>
            </h1>
            <p className="text-slate-300 leading-relaxed text-xs md:text-sm max-w-md">
              FANZA（DMM）の人気AV作品を厳選レビュー。女優別・品番検索・ジャンル別からお気に入りの作品を簡単検索。
            </p>
            {/* ナビゲーションリンク */}
            <div className="flex flex-wrap gap-2 pt-1">
              <Link href="/ranking" className="text-xs font-bold text-rose-300 bg-rose-500/10 hover:bg-rose-500/20 border border-rose-500/20 px-3 py-1.5 rounded-lg transition">
                🏆 ランキング
              </Link>
              <span className="text-[10px] text-slate-400 self-center">ジャンル別:</span>
              {allGenres.slice(0, 3).map(g => (
                <Link key={g} href={`/genre/${encodeURIComponent(g)}`}
                  className="text-[10px] font-bold text-slate-400 hover:text-rose-300 hover:bg-white/10 px-2 py-1 rounded transition">
                  {g}
                </Link>
              ))}
            </div>
          </div>

          {/* スタッツカウンター */}
          <div className="w-full md:w-auto grid grid-cols-2 gap-4 bg-white/5 border border-white/10 p-5 rounded-xl md:min-w-[200px] backdrop-blur-sm">
            <div className="text-center space-y-1">
              <span className="block text-2xl font-black text-rose-500 tracking-tight">{posts.length}</span>
              <span className="text-[9px] font-bold text-slate-400 uppercase tracking-widest block">Articles</span>
            </div>
            <div className="text-center space-y-1 border-l border-white/10">
              <span className="block text-2xl font-black text-slate-300 tracking-tight">{actressCount}</span>
              <span className="text-[9px] font-bold text-slate-400 uppercase tracking-widest block">Actresses</span>
            </div>
          </div>
        </section>

        {/* フィルタおよび記事一覧 (クライアント側) */}
        <PostListContainer initialPosts={posts} />

        {/* FAQセクション（リッチリザルト・内部リンク強化） */}
        <section className="bg-white border border-slate-200 rounded-2xl p-6 md:p-8 shadow-sm space-y-5" aria-label="よくある質問">
          <h2 className="text-lg font-extrabold text-slate-800">よくある質問（FAQ）</h2>
          <div className="space-y-5 divide-y divide-slate-100">
            <div className="pt-5 first:pt-0 space-y-2">
              <p className="text-sm font-bold text-slate-700">Q. 背徳の深夜書斎とはどんなサイトですか？</p>
              <p className="text-xs text-slate-500 leading-relaxed">A. FANZA（DMM）の人気AV作品を厳選レビューするサイトです。現在{posts.length}作品のレビューを掲載しており、品番検索・女優別・ジャンル別にもまとめています。</p>
            </div>
            <div className="pt-5 space-y-2">
              <p className="text-sm font-bold text-slate-700">Q. AVの品番から作品を検索できますか？</p>
              <p className="text-xs text-slate-500 leading-relaxed">A. はい、上部の検索ボックスに品番（例: SSIS-648、ABW-123など）を入力すると該当作品を検索できます。</p>
            </div>
            <div className="pt-5 space-y-2">
              <p className="text-sm font-bold text-slate-700">Q. FANZAで人気のAVジャンルは？</p>
              <p className="text-xs text-slate-500 leading-relaxed">A. 当サイトで多く取り上げているジャンルは「{allGenres.join("・")}」などです。<Link href="/ranking" className="text-rose-600 hover:underline font-bold">ランキングページ</Link>でまとめてご確認いただけます。</p>
            </div>
            <div className="pt-5 space-y-2">
              <p className="text-sm font-bold text-slate-700">Q. FANZAの人気AV女優は誰ですか？</p>
              <p className="text-xs text-slate-500 leading-relaxed">A. 当サイトのレビューに登場する人気女優は「{allActresses.join("・")}」などです。各女優ページで全出演作品をまとめてご確認いただけます。</p>
            </div>
          </div>
        </section>
      </div>
    </>
  );
}
