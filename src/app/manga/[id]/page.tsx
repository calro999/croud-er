import fs from "fs";
import path from "path";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Metadata } from "next";
import UnlimitedPromotionBox from "@/app/components/UnlimitedPromotionBox";
import { getMangaById, getAllManga, getSimilarManga, MangaPostSummary } from "@/lib/manga";
import { getGenreSlug } from "@/lib/slugs";

export const dynamicParams = false;

export async function generateStaticParams() {
  const allManga = getAllManga();
  return allManga.map(m => ({ id: m.id }));
}

export async function generateMetadata({ params }: { params: Promise<{ id: string }> }): Promise<Metadata> {
  const { id } = await params;
  const post = getMangaById(id);
  if (!post) return { title: "漫画が見つかりません" };

  const titleText = `【${post.hinban || id}】${post.title} ネタバレなしあらすじ・感想レビュー｜FANZA漫画おすすめ`;
  const description = `${post.title}のあらすじ・見どころ・評価を徹底レビュー！${post.author.length > 0 ? `著者：${post.author.join("、")}。` : ""}${post.genres.slice(0, 4).join("、")}が好きな方におすすめ。サンプル画像あり。`;

  return {
    title: titleText,
    description,
    keywords: [
      post.hinban || id,
      post.title,
      ...post.author,
      "漫画 レビュー",
      "漫画 ネタバレ",
      "FANZA漫画",
      "アダルト漫画",
      ...post.genres.slice(0, 5),
    ].join(","),
    alternates: { canonical: `https://haitoku.pages.dev/manga/${id}` },
    openGraph: {
      title: titleText,
      description,
      url: `https://haitoku.pages.dev/manga/${id}`,
      type: "article",
      images: post.image ? [{ url: post.image, width: 800, height: 538 }] : [],
    },
  };
}

export default async function MangaDetailPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const post = getMangaById(id);
  if (!post) notFound();

  // 類似・関連作品を取得（同一作者・同ジャンル・同レーベル）
  const similarMangaList = getSimilarManga(post, 4);

  const articleSchema = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": post.title,
    "author": post.author.map(a => ({ "@type": "Person", "name": a })),
    "datePublished": post.date,
    "image": post.image,
    "url": `https://haitoku.pages.dev/manga/${id}`,
  };

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(articleSchema) }} />

      <div className="space-y-8 max-w-4xl mx-auto">
        {/* パンくず */}
        <nav className="flex items-center gap-1.5 text-xs font-medium text-slate-500" aria-label="パンくずリスト">
          <Link href="/" className="hover:text-rose-600 transition-colors">ホーム</Link>
          <span className="text-slate-300">›</span>
          <Link href="/manga" className="hover:text-rose-600 transition-colors">漫画コーナー</Link>
          <span className="text-slate-300">›</span>
          <span className="text-slate-700 font-bold truncate max-w-[200px]">{post.title}</span>
        </nav>

        {/* ヘッダーカード */}
        <section className="rounded-2xl bg-gradient-to-br from-purple-900 to-slate-950 p-6 md:p-10 border border-purple-700/30 shadow-lg">
          <div className="flex flex-col md:flex-row gap-6 items-start">
            {post.image && (
              <div className="flex-shrink-0 w-full md:w-48">
                <img src={post.image} alt={`${post.title} 表紙`} className="w-full rounded-xl shadow-lg" />
              </div>
            )}
            <div className="flex-1 space-y-3">
              <span className="inline-flex text-[9px] font-bold tracking-widest text-purple-400 bg-purple-500/10 border border-purple-500/20 px-3 py-1 rounded">
                📚 MANGA REVIEW
              </span>
              <h1 className="text-2xl md:text-3xl font-black text-white leading-snug">{post.title}</h1>

              <div className="flex flex-wrap gap-3 text-xs text-slate-300">
                {post.author.length > 0 && (
                  <span className="flex items-center gap-1">
                    ✍️ 作者: {post.author.map((a, idx) => (
                      <span key={a}>
                        <strong className="text-purple-300 font-bold">{a}</strong>
                        {idx < post.author.length - 1 ? "、" : ""}
                      </span>
                    ))}
                  </span>
                )}
                {post.publisher && (
                  <span>🏢 レーベル: <span className="text-slate-200 font-semibold">{post.publisher}</span></span>
                )}
                <span>📅 {post.date?.split(" ")[0]}</span>
              </div>

              <div className="flex flex-wrap gap-1.5 pt-1">
                {post.genres.slice(0, 8).map(g => (
                  <Link key={g} href={`/genre/${getGenreSlug(g)}`}
                    className="text-[10px] font-bold text-purple-300 bg-purple-500/10 border border-purple-500/20 px-2 py-0.5 rounded-full hover:bg-purple-500/20 transition">
                    {g}
                  </Link>
                ))}
              </div>

              <div className="pt-2 flex flex-wrap gap-3">
                {post.tachiyomi_url ? (
                  <a href={post.tachiyomi_url} target="_blank" rel="noopener noreferrer"
                    className="inline-block px-6 py-3 text-sm font-black text-white bg-gradient-to-r from-purple-500 to-rose-500 hover:from-purple-400 hover:to-rose-400 rounded-xl shadow transition">
                    📖 無料で試し読みする（FANZA）
                  </a>
                ) : (
                  <a href={post.affiliate_url} target="_blank" rel="noopener noreferrer"
                    className="inline-block px-6 py-3 text-sm font-black text-white bg-gradient-to-r from-purple-500 to-rose-500 hover:from-purple-400 hover:to-rose-400 rounded-xl shadow transition">
                    📖 FANZAで読む（18禁）
                  </a>
                )}
              </div>
            </div>
          </div>
        </section>

        {/* レビュー本文 */}
        <section className="bg-white border border-slate-200 rounded-2xl p-6 md:p-8 shadow-sm prose prose-slate max-w-none
          [&_h2]:text-xl [&_h2]:font-black [&_h2]:text-slate-800 [&_h2]:border-b [&_h2]:border-slate-200 [&_h2]:pb-2 [&_h2]:mt-6
          [&_h3]:text-base [&_h3]:font-extrabold [&_h3]:text-slate-700 [&_h3]:mt-4
          [&_h4]:text-sm [&_h4]:font-bold [&_h4]:text-slate-600
          [&_p]:text-sm [&_p]:text-slate-600 [&_p]:leading-relaxed
          [&_table]:w-full [&_table]:text-xs [&_table]:border-collapse
          [&_th]:bg-purple-50 [&_th]:font-bold [&_th]:text-purple-700 [&_th]:p-2 [&_th]:border [&_th]:border-purple-100
          [&_td]:p-2 [&_td]:border [&_td]:border-slate-200 [&_td]:text-slate-600
          [&_ul]:list-disc [&_ul]:pl-5 [&_li]:text-sm [&_li]:text-slate-600 [&_li]:leading-relaxed">
          <div dangerouslySetInnerHTML={{ __html: post.review }} />
        </section>

        {/* 📚 【関連・類似作品レコメンド】 この漫画が好きな人におすすめの作品 */}
        {similarMangaList.length > 0 && (
          <section className="bg-white border border-purple-100 rounded-2xl p-6 md:p-8 shadow-sm space-y-4">
            <div className="space-y-1">
              <span className="text-[10px] font-bold text-purple-600 bg-purple-50 border border-purple-200 px-2.5 py-0.5 rounded-full uppercase tracking-wider">
                SIMILAR MANGA • 関連・類似作品
              </span>
              <h2 className="text-lg md:text-xl font-black text-slate-900">
                『{post.title}』が好きなあなたにおすすめの漫画
              </h2>
              <p className="text-xs text-slate-500">
                同じ作家・同ジャンル・同系統のシチュエーションから厳選した注目作品です。
              </p>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
              {similarMangaList.map(({ manga: relManga, matchReason }) => (
                <div key={relManga.id} className="flex gap-3.5 p-3.5 rounded-2xl bg-purple-50/40 border border-purple-100/80 hover:border-purple-300 transition duration-200 group">
                  <div className="w-20 h-28 bg-slate-200 rounded-xl overflow-hidden flex-shrink-0 relative">
                    {relManga.image ? (
                      <img src={relManga.image} alt={relManga.title} className="w-full h-full object-cover group-hover:scale-105 transition duration-300" loading="lazy" />
                    ) : (
                      <div className="w-full h-full flex items-center justify-center text-slate-400 text-[10px]">📚</div>
                    )}
                  </div>
                  <div className="flex-1 flex flex-col justify-between space-y-1.5">
                    <div>
                      <span className="text-[9px] font-bold text-purple-700 bg-purple-100 px-2 py-0.5 rounded-md inline-block mb-1">
                        {matchReason}
                      </span>
                      <h3 className="text-xs font-bold text-slate-900 leading-snug line-clamp-2 group-hover:text-purple-600 transition">
                        {relManga.title}
                      </h3>
                      {relManga.author.length > 0 && (
                        <p className="text-[11px] text-slate-500 mt-0.5">
                          ✍️ {relManga.author.join("、")}
                        </p>
                      )}
                    </div>
                    <div className="flex gap-2 pt-1">
                      <Link href={`/manga/${relManga.id}`} className="flex-1 text-center text-[11px] font-bold text-purple-700 bg-white border border-purple-200 hover:bg-purple-50 py-1.5 rounded-lg transition">
                        レビュー
                      </Link>
                      <a href={relManga.tachiyomi_url || relManga.affiliate_url} target="_blank" rel="noopener noreferrer" className="flex-1 text-center text-[11px] font-bold text-white bg-gradient-to-r from-purple-500 to-rose-500 hover:from-purple-400 hover:to-rose-400 py-1.5 rounded-lg shadow transition">
                        試し読み
                      </a>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* FANZA見放題ch 特設キラー誘導ボックス */}
        <UnlimitedPromotionBox />

        {/* CTAボタン */}
        <section className="text-center py-6 space-y-3">
          <a href={post.affiliate_url} target="_blank" rel="noopener noreferrer"
            className="inline-block px-10 py-4 text-base font-black text-white bg-gradient-to-r from-purple-500 via-purple-600 to-rose-500 hover:from-purple-400 hover:to-rose-400 rounded-xl shadow-lg transition">
            📖 今すぐFANZAで読む（全ページ）
          </a>
          <p className="text-[10px] text-slate-400">※クリックするとFANZA（18禁公式サイト）へ遷移します</p>
        </section>

        {/* 関連ジャンル */}
        {post.genres.length > 0 && (
          <section className="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-3">
            <h2 className="text-xs font-bold text-slate-500 uppercase tracking-widest">このジャンルの作品をもっと見る</h2>
            <div className="flex flex-wrap gap-2">
              {post.genres.map(g => (
                <Link key={g} href={`/genre/${getGenreSlug(g)}`}
                  className="text-xs font-bold text-purple-600 bg-purple-50 hover:bg-purple-100 border border-purple-200 px-3 py-1.5 rounded-full transition">
                  {g}
                </Link>
              ))}
            </div>
          </section>
        )}

        <div className="text-center pt-4">
          <Link href="/manga" className="text-xs font-bold text-purple-600 hover:underline">
            ← 漫画コーナートップに戻る
          </Link>
        </div>
      </div>
    </>
  );
}
