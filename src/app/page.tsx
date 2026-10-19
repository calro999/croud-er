import Link from "next/link";
import { Metadata } from "next";
import PostListContainer from "./components/PostListContainer";
import { getActressSlug, getGenreSlug } from "@/lib/slugs";
import { getAllSummaryPosts } from "@/lib/posts";

export const metadata: Metadata = {
  alternates: {
    canonical: "/",
  },
};

// Build trigger: 2026-08-31 16:50
export default function Home() {
  const posts = getAllSummaryPosts();

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
                <Link key={g} href={`/genre/${getGenreSlug(g)}`}
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

        {/* 特選PICKUP: FANZA見放題ch＆お得セール特設バナー */}
        <section className="relative overflow-hidden rounded-2xl bg-gradient-to-br from-slate-900 via-rose-950 to-slate-900 p-6 md:p-8 border border-rose-500/40 shadow-xl text-white space-y-4">
          <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6">
            <div className="space-y-2 max-w-2xl">
              <div className="flex items-center gap-2">
                <span className="bg-gradient-to-r from-amber-400 to-amber-600 text-slate-950 text-[10px] font-black px-2.5 py-0.5 rounded tracking-wide shadow">
                  👑 コスパ最強
                </span>
                <span className="text-rose-300 text-xs font-bold bg-rose-500/20 border border-rose-500/30 px-2 py-0.5 rounded">
                  15万本見放題・大型セール開催中
                </span>
              </div>
              <h2 className="text-lg md:text-2xl font-black text-white leading-snug">
                単品買いで損していませんか？定額で抜ける「FANZA見放題ch」＆100円〜公式セール特集
              </h2>
              <p className="text-xs md:text-sm text-slate-300 leading-relaxed">
                1本2,500円〜の都度買いから月額定額へ！人気単体女優・大手レーベル・VRまで15万本以上が見放題。さらに過去の名作が100円から手に入る公式セールも随時実施中。
              </p>
              <div className="pt-1 flex flex-wrap items-center gap-3 text-[11px] text-slate-400">
                <span className="text-emerald-400 font-bold">🔒 クレカ明細はDMM表記（作品名なし）</span>
                <span>•</span>
                <span>PayPay・楽天ペイ対応</span>
                <span>•</span>
                <span>スマホ即再生OK</span>
              </div>
            </div>

            <div className="flex flex-col sm:flex-row lg:flex-col gap-2.5 w-full lg:w-auto flex-shrink-0">
              <a
                href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fmonthly%2Fpremium%2F&af_id=onchan555-003"
                target="_blank"
                rel="noopener noreferrer"
                className="w-full text-center text-xs font-black text-white bg-gradient-to-r from-rose-600 via-rose-500 to-pink-600 hover:from-rose-500 hover:to-pink-500 px-6 py-3 rounded-xl shadow-lg shadow-rose-600/30 transition transform hover:-translate-y-0.5"
              >
                👑 FANZA見放題ch 公式で今すぐ体験 ›
              </a>
              <div className="flex gap-2">
                <a
                  href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fsale%2F&af_id=onchan555-003"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex-1 text-center text-xs font-bold text-amber-300 hover:text-amber-200 bg-amber-400/10 hover:bg-amber-400/20 border border-amber-400/30 px-3 py-2 rounded-lg transition"
                >
                  🏷️ 100円〜セール
                </a>
                <Link
                  href="/fanza-tv-plus"
                  className="flex-1 text-center text-xs font-bold text-slate-300 hover:text-white bg-white/10 hover:bg-white/20 border border-white/20 px-3 py-2 rounded-lg transition"
                >
                  📖 徹底比較記事
                </Link>
              </div>
            </div>
          </div>
        </section>

        {/* フィルタおよび記事一覧 (クライアント側) */}
        <PostListContainer initialPosts={posts} />
        {/* 女優別・ジャンル別のクイックリンク集 (内部リンクSEO強化) */}
        <section className="bg-white border border-slate-200 rounded-2xl p-6 md:p-8 shadow-sm space-y-6">
          <div className="space-y-4">
            <h2 className="text-base font-extrabold text-slate-800 flex items-center gap-2">
              <span className="w-1.5 h-4 bg-rose-500 rounded-full" />
              人気女優から探す
            </h2>
            <div className="flex flex-wrap gap-2">
              {Array.from(new Set(posts.flatMap(p => p.actresses || [])))
                .filter(Boolean)
                .slice(0, 45)
                .map(actress => (
                  <Link
                    key={actress}
                    href={`/actress/${getActressSlug(actress)}`}
                    className="text-xs font-bold text-rose-600 bg-rose-50 hover:bg-rose-100 hover:text-rose-700 border border-rose-100 px-3.5 py-2 rounded-xl transition duration-150"
                  >
                    {actress}
                  </Link>
                ))}
            </div>
          </div>

          <div className="border-t border-slate-100 pt-6 space-y-4">
            <h2 className="text-base font-extrabold text-slate-800 flex items-center gap-2">
              <span className="w-1.5 h-4 bg-slate-700 rounded-full" />
              人気のジャンルから探す
            </h2>
            <div className="flex flex-wrap gap-2">
              {Array.from(new Set(posts.flatMap(p => p.genres || [])))
                .filter(Boolean)
                .slice(0, 30)
                .map(genre => (
                  <Link
                    key={genre}
                    href={`/genre/${getGenreSlug(genre)}`}
                    className="text-xs font-bold text-slate-600 bg-slate-50 hover:bg-slate-100 hover:text-slate-800 border border-slate-200/80 px-3.5 py-2 rounded-xl transition duration-150"
                  >
                    {genre}
                  </Link>
                ))}
            </div>
          </div>
        </section>


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
