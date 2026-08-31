import fs from "fs";
import path from "path";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Metadata } from "next";
import { getAllManga, MangaPostSummary } from "@/lib/manga";
import { getGenreSlug } from "@/lib/slugs";
import UnlimitedPromotionBox from "@/app/components/UnlimitedPromotionBox";

export const dynamicParams = false;

export async function generateStaticParams() {
  const allManga = getAllManga();
  const authorSet = new Set<string>();
  for (const m of allManga) {
    (m.author || []).forEach(a => {
      const cleanA = a.trim();
      if (cleanA) authorSet.add(cleanA);
    });
  }
  return Array.from(authorSet).map(name => ({ name: encodeURIComponent(name) }));
}

export async function generateMetadata({ params }: { params: Promise<{ name: string }> }): Promise<Metadata> {
  const { name } = await params;
  const authorName = decodeURIComponent(name);
  const allManga = getAllManga();
  const authorManga = allManga.filter(m => (m.author || []).includes(authorName));

  const titleText = `【作家特集】${authorName} 先生の成人向け漫画おすすめ作品・レビュー一覧`;
  const descriptionText = `人気漫画家・イラストレーター「${authorName}」先生のFANZA配信コミックを徹底紹介！あらすじ、見どころ、試し読み情報をまとめました。（全${authorManga.length}作品）`;

  return {
    title: titleText,
    description: descriptionText,
    keywords: [
      `${authorName}`,
      `${authorName} 漫画`,
      `${authorName} FANZA`,
      `${authorName} おすすめ`,
      "アダルト漫画",
      "同人コミック"
    ].join(","),
    alternates: { canonical: `https://haitoku.pages.dev/author/${name}` },
    openGraph: {
      title: titleText,
      description: descriptionText,
      url: `https://haitoku.pages.dev/author/${name}`,
      type: "website",
      images: authorManga.length > 0 && authorManga[0].image ? [{ url: authorManga[0].image, width: 800, height: 538 }] : [],
    },
  };
}

export default async function AuthorDetailPage({ params }: { params: Promise<{ name: string }> }) {
  const { name } = await params;
  const authorName = decodeURIComponent(name);
  const allManga = getAllManga();
  const authorManga = allManga.filter(m => (m.author || []).includes(authorName));

  if (authorManga.length === 0) notFound();

  // 作家がよく描くジャンルの集計
  const genreCountMap: Record<string, number> = {};
  authorManga.forEach(m => {
    (m.genres || []).forEach(g => {
      genreCountMap[g] = (genreCountMap[g] || 0) + 1;
    });
  });
  const topGenres = Object.entries(genreCountMap)
    .sort((a, b) => b[1] - a[1])
    .map(([g]) => g)
    .slice(0, 8);

  const breadcrumbSchema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "ホーム", "item": "https://haitoku.pages.dev" },
      { "@type": "ListItem", "position": 2, "name": "漫画コーナー", "item": "https://haitoku.pages.dev/manga" },
      { "@type": "ListItem", "position": 3, "name": `${authorName} 先生の作品一覧`, "item": `https://haitoku.pages.dev/author/${name}` }
    ]
  };

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema) }} />

      <div className="space-y-8 max-w-5xl mx-auto">
        {/* パンくず */}
        <nav className="flex items-center gap-1.5 text-xs font-medium text-slate-500" aria-label="パンくずリスト">
          <Link href="/" className="hover:text-rose-600 transition-colors">ホーム</Link>
          <span className="text-slate-300">›</span>
          <Link href="/manga" className="hover:text-rose-600 transition-colors">漫画コーナー</Link>
          <span className="text-slate-300">›</span>
          <span className="text-slate-700 font-bold truncate max-w-[200px]">{authorName} 先生</span>
        </nav>

        {/* ヘッダーカード */}
        <section className="rounded-2xl bg-gradient-to-br from-purple-900 via-purple-950 to-slate-950 p-8 md:p-10 border border-purple-700/30 shadow-xl">
          <div className="flex flex-col md:flex-row items-start md:items-center gap-6 justify-between">
            <div className="space-y-3">
              <span className="inline-flex text-[9px] font-bold tracking-widest text-purple-400 bg-purple-500/10 border border-purple-500/20 px-3 py-1 rounded">
                ✍️ MANGA AUTHOR ARCHIVE
              </span>
              <h1 className="text-3xl md:text-4xl font-black text-white tracking-tight">
                {authorName} <span className="text-purple-300 text-xl font-bold">先生の作品一覧</span>
              </h1>
              <p className="text-slate-300 text-sm leading-relaxed max-w-xl">
                気鋭の漫画家・イラストレーター【<strong>{authorName}</strong>】先生が手掛ける成人向け漫画・同人コミックのレビューとおすすめ作品まとめです。
              </p>
              {topGenres.length > 0 && (
                <div className="flex flex-wrap gap-1.5 pt-2">
                  <span className="text-[10px] text-slate-400 font-bold self-center mr-1">主なジャンル:</span>
                  {topGenres.map(g => (
                    <Link key={g} href={`/genre/${getGenreSlug(g)}`}
                      className="text-[10px] font-bold text-purple-300 bg-purple-500/20 border border-purple-500/30 px-2.5 py-0.5 rounded-full hover:bg-purple-500/30 transition">
                      {g}
                    </Link>
                  ))}
                </div>
              )}
            </div>
            <div className="text-center bg-white/5 border border-white/10 rounded-2xl px-6 py-4 flex-shrink-0">
              <span className="block text-3xl font-black text-purple-400">{authorManga.length}</span>
              <span className="text-[9px] font-bold text-slate-400 uppercase tracking-widest">WORKS</span>
            </div>
          </div>
        </section>

        {/* 作品一覧 */}
        <section className="space-y-4">
          <h2 className="text-lg font-extrabold text-slate-800">
            {authorName} 先生の作品レビュー一覧（{authorManga.length}件）
          </h2>
          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
            {authorManga.map(post => (
              <article key={post.id} className="flex flex-col rounded-2xl overflow-hidden bg-white border border-purple-100/90 shadow-sm hover:shadow-md hover:-translate-y-0.5 transition-all duration-200">
                <div className="aspect-[3/4] relative overflow-hidden bg-slate-100">
                  {post.image ? (
                    <img src={post.image} alt={`${post.title} 表紙`}
                      className="w-full h-full object-cover" loading="lazy" />
                  ) : (
                    <div className="w-full h-full flex items-center justify-center text-4xl">📚</div>
                  )}
                  <span className="absolute top-2 left-2 text-[9px] font-bold bg-purple-600 text-white px-1.5 py-0.5 rounded shadow">漫画</span>
                </div>
                <div className="p-3 flex-grow flex flex-col justify-between space-y-2">
                  <div>
                    <p className="text-[10px] text-slate-400 font-bold mb-1">{post.date?.split(" ")[0]}</p>
                    <h3 className="text-xs font-extrabold text-slate-800 leading-snug line-clamp-2">{post.title}</h3>
                  </div>
                  <div className="flex gap-1.5 pt-1">
                    <Link href={`/manga/${post.id}`}
                      className="flex-1 text-center text-[10px] font-black text-purple-700 bg-purple-50 hover:bg-purple-100 border border-purple-200 py-1.5 rounded-lg transition">
                      レビュー
                    </Link>
                    <a href={post.tachiyomi_url || post.affiliate_url} target="_blank" rel="noopener noreferrer"
                      className="flex-1 text-center text-[10px] font-bold text-white bg-gradient-to-r from-purple-500 to-rose-500 hover:from-purple-400 hover:to-rose-400 py-1.5 rounded-lg shadow transition">
                      試し読み
                    </a>
                  </div>
                </div>
              </article>
            ))}
          </div>
        </section>

        {/* FANZA見放題ch 特設キラー誘導ボックス */}
        <UnlimitedPromotionBox />

        {/* CTA */}
        <section className="text-center py-6">
          <a href={`https://al.fanza.co.jp/?lurl=https%3A%2F%2Fbook.dmm.co.jp%2Fsearch%2F-%2F%3Fsearchstr%3D${encodeURIComponent(authorName)}&af_id=onchan555-003`}
            target="_blank" rel="noopener noreferrer"
            className="inline-block px-8 py-4 text-base font-extrabold text-white bg-gradient-to-r from-purple-500 via-purple-600 to-rose-500 rounded-xl shadow-md hover:opacity-90 transition">
            📚 {authorName} 先生の作品をFANZAで全件検索
          </a>
          <p className="text-[10px] text-slate-400 mt-2">※FANZA（18禁公式サイト）へ遷移します</p>
        </section>
      </div>
    </>
  );
}
