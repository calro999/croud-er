import fs from "fs";
import path from "path";
import Link from "next/link";
import { Metadata } from "next";

interface Post {
  id: string;
  hinban?: string;
  title: string;
  review: string;
  image: string;
  affiliate_url: string;
  genres: string[];
  actresses: string[];
  maker: string;
  date: string;
  labels: string[];
}

export const metadata: Metadata = {
  title: "FANZA人気AV作品ランキング2026【厳選レビュー】",
  description: "FANZAで今話題のAV作品を厳選したランキング。2026年最新の人気女優・ジャンル別おすすめ作品を徹底レビュー。品番検索・感想・評価も掲載。",
  keywords: [
    "FANZA ランキング 2026",
    "AV 人気ランキング",
    "アダルト動画 おすすめ",
    "AV女優 人気 2026",
    "FANZA おすすめ作品",
    "AV ランキング",
    "アダルトビデオ 人気"
  ].join(","),
  alternates: { canonical: "https://haitoku.pages.dev/ranking" },
  openGraph: {
    title: "FANZA人気AV作品ランキング2026【厳選レビュー】",
    description: "FANZAで今話題のAV作品を厳選したランキング。2026年最新の人気女優・ジャンル別おすすめ作品を徹底レビュー。",
    url: "https://haitoku.pages.dev/ranking",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "FANZA人気AV作品ランキング2026【厳選レビュー】",
    description: "FANZAで今話題のAV作品を厳選したランキング。2026年最新の人気女優を紹介。",
  },
};

function getAllPosts(): Post[] {
  const postsDir = path.join(process.cwd(), "src", "data", "posts");
  if (!fs.existsSync(postsDir)) return [];
  try {
    return fs.readdirSync(postsDir)
      .filter(f => f.endsWith(".json"))
      .map(file => {
        try {
          return JSON.parse(fs.readFileSync(path.join(postsDir, file), "utf-8")) as Post;
        } catch { return null; }
      })
      .filter(Boolean) as Post[];
  } catch { return []; }
}

export default function RankingPage() {
  const allPosts = getAllPosts();

  // 最新20件をランキングとして表示
  const rankedPosts = [...allPosts]
    .sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime())
    .slice(0, 20);

  // ジャンル別集計（人気ジャンルトップ10）
  const genreCount: Record<string, number> = {};
  allPosts.forEach(p => (p.genres || []).forEach(g => { genreCount[g] = (genreCount[g] || 0) + 1; }));
  const topGenres = Object.entries(genreCount).sort((a, b) => b[1] - a[1]).slice(0, 10);

  // 女優別集計（出演数トップ10）
  const actressCount: Record<string, number> = {};
  allPosts.forEach(p => (p.actresses || []).forEach(a => { actressCount[a] = (actressCount[a] || 0) + 1; }));
  const topActresses = Object.entries(actressCount).sort((a, b) => b[1] - a[1]).slice(0, 10);

  const breadcrumbSchema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "ホーム", "item": "https://haitoku.pages.dev" },
      { "@type": "ListItem", "position": 2, "name": "人気ランキング", "item": "https://haitoku.pages.dev/ranking" }
    ]
  };

  const faqSchema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "FANZAで今人気のAV作品は？",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": `現在当サイトで注目度の高い作品は「${rankedPosts[0]?.title || ""}」「${rankedPosts[1]?.title || ""}」「${rankedPosts[2]?.title || ""}」などです。ランキング詳細は本ページをご確認ください。`
        }
      },
      {
        "@type": "Question",
        "name": "FANZAの人気AV女優は誰ですか？",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": `当サイトのレビューで登場する人気女優は「${topActresses.slice(0, 5).map(([name]) => name).join("・")}」などです。各女優ページでレビューをご確認いただけます。`
        }
      },
      {
        "@type": "Question",
        "name": "FANZAで人気のAVジャンルは？",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": `当サイトで多く取り上げているジャンルは「${topGenres.slice(0, 5).map(([g]) => g).join("・")}」などです。ジャンル別ページでまとめてレビューをご確認いただけます。`
        }
      }
    ]
  };

  const itemListSchema = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "FANZA人気AV作品ランキング2026",
    "description": "FANZAで今話題のAV作品を厳選したランキング",
    "numberOfItems": rankedPosts.length,
    "itemListElement": rankedPosts.map((post, idx) => ({
      "@type": "ListItem",
      "position": idx + 1,
      "url": `https://haitoku.pages.dev/posts/${post.id}`,
      "name": post.title,
    }))
  };

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(itemListSchema) }} />

      <div className="space-y-10 max-w-5xl mx-auto">
        <nav className="flex items-center gap-1.5 text-xs font-medium text-slate-500" aria-label="パンくずリスト">
          <Link href="/" className="hover:text-rose-600 transition-colors">ホーム</Link>
          <span className="text-slate-300">›</span>
          <span className="text-slate-700 font-bold">人気ランキング</span>
        </nav>

        {/* ヒーロー */}
        <section className="rounded-2xl bg-gradient-to-br from-slate-800 to-slate-950 p-8 md:p-12 border border-slate-700/30 shadow-sm">
          <div className="space-y-4">
            <span className="inline-flex text-[9px] font-bold tracking-widest text-rose-400 bg-rose-500/10 border border-rose-500/20 px-3 py-1 rounded">
              2026 BEST RANKING
            </span>
            <h1 className="text-3xl md:text-4xl font-black text-white tracking-tight leading-snug">
              FANZA 人気AV作品<br />
              <span className="bg-gradient-to-r from-rose-400 to-pink-300 bg-clip-text text-transparent">
                ランキング 2026
              </span>
            </h1>
            <p className="text-slate-400 text-sm leading-relaxed max-w-lg">
              FANZAで今話題の人気AV作品を厳選してランキング形式でご紹介。最新作から定番まで徹底レビュー。
            </p>
            <div className="flex flex-wrap gap-4 pt-2">
              <div className="text-center bg-white/5 border border-white/10 rounded-xl px-5 py-3">
                <span className="block text-2xl font-black text-rose-500">{allPosts.length}</span>
                <span className="text-[9px] font-bold text-slate-400 uppercase tracking-widest">Total Reviews</span>
              </div>
              <div className="text-center bg-white/5 border border-white/10 rounded-xl px-5 py-3">
                <span className="block text-2xl font-black text-slate-300">{topActresses.length}+</span>
                <span className="text-[9px] font-bold text-slate-400 uppercase tracking-widest">Actresses</span>
              </div>
              <div className="text-center bg-white/5 border border-white/10 rounded-xl px-5 py-3">
                <span className="block text-2xl font-black text-slate-300">{topGenres.length}+</span>
                <span className="text-[9px] font-bold text-slate-400 uppercase tracking-widest">Genres</span>
              </div>
            </div>
          </div>
        </section>

        {/* TOP20ランキング */}
        <section className="space-y-4">
          <h2 className="text-xl font-extrabold text-slate-800">🏆 注目作品 TOP {rankedPosts.length}</h2>
          <div className="space-y-3">
            {rankedPosts.map((post, idx) => (
              <article key={post.id} className="flex items-center gap-4 bg-white border border-slate-200 rounded-2xl p-4 shadow-sm card-hover-effect">
                <div className={`flex-shrink-0 w-10 h-10 rounded-xl flex items-center justify-center font-black text-lg ${idx < 3 ? "bg-rose-500 text-white shadow-md" : "bg-slate-100 text-slate-500"}`}>
                  {idx + 1}
                </div>
                <div className="flex-shrink-0 w-16 h-11 rounded-lg overflow-hidden bg-slate-100">
                  {post.image ? (
                    <img src={post.image} alt={post.title} referrerPolicy="no-referrer" className="w-full h-full object-cover" loading="lazy" />
                  ) : (
                    <div className="w-full h-full bg-slate-200" />
                  )}
                </div>
                <div className="flex-grow min-w-0">
                  <div className="flex flex-wrap items-center gap-1.5 text-[9px] font-bold text-slate-400 mb-1">
                    <span className="text-rose-600">{post.hinban}</span>
                    <span>•</span>
                    <span>{(post.actresses || []).slice(0, 2).join("・")}</span>
                  </div>
                  <h3 className="text-sm font-extrabold text-slate-800 leading-snug line-clamp-1">{post.title}</h3>
                  <div className="flex flex-wrap gap-1 mt-1">
                    {(post.genres || []).slice(0, 2).map(g => (
                      <span key={g} className="text-[9px] text-slate-500 bg-slate-100 border border-slate-200 px-1.5 py-0.5 rounded">{g}</span>
                    ))}
                  </div>
                </div>
                <div className="flex-shrink-0 flex gap-2">
                  <Link href={`/posts/${post.id}`} className="text-xs font-bold text-slate-700 bg-white border border-slate-300 hover:bg-slate-50 px-3 py-2 rounded-lg transition whitespace-nowrap">
                    レビュー
                  </Link>
                  <a href={post.affiliate_url} target="_blank" rel="noopener noreferrer"
                    className="text-xs font-bold text-white bg-gradient-to-r from-rose-500 to-rose-600 hover:from-rose-400 hover:to-rose-500 px-3 py-2 rounded-lg shadow transition whitespace-nowrap">
                    視聴
                  </a>
                </div>
              </article>
            ))}
          </div>
        </section>

        {/* 人気ジャンル */}
        <section className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm space-y-4">
          <h2 className="text-lg font-extrabold text-slate-800">🎭 人気ジャンルランキング</h2>
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-3">
            {topGenres.map(([genre, count], idx) => (
              <Link key={genre} href={`/genre/${encodeURIComponent(genre)}`}
                className="flex flex-col items-center text-center p-3 rounded-xl bg-slate-50 hover:bg-rose-50 border border-slate-200 hover:border-rose-200 transition-colors duration-200 group">
                <span className={`text-lg font-black mb-1 ${idx < 3 ? "text-rose-500" : "text-slate-400"}`}>
                  {idx + 1}
                </span>
                <span className="text-xs font-bold text-slate-700 group-hover:text-rose-600 transition-colors leading-snug">{genre}</span>
                <span className="text-[9px] text-slate-400 mt-0.5">{count}件</span>
              </Link>
            ))}
          </div>
        </section>

        {/* 人気女優 */}
        <section className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm space-y-4">
          <h2 className="text-lg font-extrabold text-slate-800">💫 人気女優ランキング</h2>
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-3">
            {topActresses.map(([actress, count], idx) => (
              <Link key={actress} href={`/actress/${encodeURIComponent(actress)}`}
                className="flex flex-col items-center text-center p-3 rounded-xl bg-slate-50 hover:bg-rose-50 border border-slate-200 hover:border-rose-200 transition-colors duration-200 group">
                <span className={`text-lg font-black mb-1 ${idx < 3 ? "text-rose-500" : "text-slate-400"}`}>
                  {idx + 1}
                </span>
                <span className="text-xs font-bold text-slate-700 group-hover:text-rose-600 transition-colors leading-snug">{actress}</span>
                <span className="text-[9px] text-slate-400 mt-0.5">{count}作品</span>
              </Link>
            ))}
          </div>
        </section>

        {/* FAQ */}
        <section className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm space-y-4">
          <h2 className="text-sm font-extrabold text-slate-800">よくある質問</h2>
          <div className="space-y-4 divide-y divide-slate-100">
            <div className="pt-4 first:pt-0 space-y-1.5">
              <p className="text-sm font-bold text-slate-700">Q. FANZAで今人気のAV作品は？</p>
              <p className="text-xs text-slate-500 leading-relaxed">A. 「{rankedPosts[0]?.title || ""}」「{rankedPosts[1]?.title || ""}」などが注目されています。上記ランキングで詳細をご確認ください。</p>
            </div>
            <div className="pt-4 space-y-1.5">
              <p className="text-sm font-bold text-slate-700">Q. FANZAで人気のAVジャンルは？</p>
              <p className="text-xs text-slate-500 leading-relaxed">A. {topGenres.slice(0, 5).map(([g]) => g).join("・")}などが人気ジャンルです。</p>
            </div>
            <div className="pt-4 space-y-1.5">
              <p className="text-sm font-bold text-slate-700">Q. FANZAの人気AV女優は誰ですか？</p>
              <p className="text-xs text-slate-500 leading-relaxed">A. {topActresses.slice(0, 5).map(([name]) => name).join("・")}などが人気女優です。各女優ページでレビューをご確認いただけます。</p>
            </div>
          </div>
        </section>
      </div>
    </>
  );
}
