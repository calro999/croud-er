import fs from "fs";
import path from "path";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Metadata } from "next";
import { censorText } from "@/lib/censor";
import { getActressSlug, getActressNameBySlug, getGenreSlug } from "@/lib/slugs";

interface Post {
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

export const dynamicParams = false;

export async function generateStaticParams() {
  const postsDir = path.join(process.cwd(), "src", "data", "posts");
  if (!fs.existsSync(postsDir)) return [];
  try {
    const files = fs.readdirSync(postsDir).filter(f => f.endsWith(".json"));
    const actressSet = new Set<string>();
    for (const file of files) {
      try {
        const content = fs.readFileSync(path.join(postsDir, file), "utf-8");
        const post: Post = JSON.parse(content);
        (post.actresses || []).forEach(a => actressSet.add(a));
      } catch { /* skip */ }
    }
    return Array.from(actressSet).map(name => ({ name: getActressSlug(name) }));
  } catch {
    return [];
  }
}

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

export async function generateMetadata({ params }: { params: Promise<{ name: string }> }): Promise<Metadata> {
  const { name } = await params;
  const actressName = getActressNameBySlug(name);
  const titleText = `【品番特定】「${actressName}」あのSNSで話題のシチュエーション動画の正体はこれ！出演作まとめ`;
  const descriptionText = `Xや5chで「可愛すぎる」「エロすぎる」と話題の、${actressName}のアダルト動画・品番を特定！あの抜ける神作の概要、見どころ、お得にFANZAで視聴する方法をどこよりも分かりやすく解説します。`;

  const allPosts = getAllPosts();
  const actressPosts = allPosts
    .filter(p => (p.actresses || []).includes(actressName))
    .sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
  const ogImage = actressPosts.length > 0 && actressPosts[0].image ? actressPosts[0].image : undefined;

  return {
    title: titleText,
    description: descriptionText,
    keywords: [
      `${actressName} レビュー`,
      `${actressName} 出演作品`,
      `${actressName} AV`,
      `${actressName} FANZA`,
      `${actressName} 動画`,
      `${actressName} おすすめ`,
      "AV女優 レビュー",
      "FANZA 女優"
    ].join(","),
    alternates: { canonical: `https://haitoku.pages.dev/actress/${name}` },
    openGraph: {
      title: censorText(titleText),
      description: censorText(descriptionText),
      url: `https://haitoku.pages.dev/actress/${name}`,
      type: "website",
      images: ogImage ? [{ url: ogImage, width: 800, height: 538 }] : [],
    },
    twitter: {
      card: "summary_large_image",
      title: censorText(titleText),
      description: censorText(descriptionText),
      images: ogImage ? [ogImage] : [],
    },
  };
}

export default async function ActressPage({ params }: { params: Promise<{ name: string }> }) {
  const { name } = await params;
  const actressName = getActressNameBySlug(name);
  const allPosts = getAllPosts();
  const actressPosts = allPosts
    .filter(p => (p.actresses || []).includes(actressName))
    .sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());

  if (actressPosts.length === 0) notFound();

  const relatedGenres = Array.from(new Set(actressPosts.flatMap(p => p.genres || []))).slice(0, 8);
  const coActresses = Array.from(
    new Set(actressPosts.flatMap(p => (p.actresses || []).filter(a => a !== actressName)))
  ).slice(0, 6);

  const breadcrumbSchema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "ホーム", "item": "https://haitoku.pages.dev" },
      { "@type": "ListItem", "position": 2, "name": `${actressName} レビュー`, "item": `https://haitoku.pages.dev/actress/${name}` }
    ]
  };

  const faqSchema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": `${actressName}の作品はどこで見られますか？`,
        "acceptedAnswer": {
          "@type": "Answer",
          "text": `${actressName}の作品はFANZA（DMM）で配信されています。当サイトでは${actressPosts.length}作品のレビューを掲載しています。`
        }
      },
      {
        "@type": "Question",
        "name": `${actressName}のおすすめ作品は？`,
        "acceptedAnswer": {
          "@type": "Answer",
          "text": `当サイトでレビューしている${actressName}の人気作品は「${actressPosts[0]?.title || ""}」などです。各作品ページで詳しいレビュー・感想をご確認ください。`
        }
      },
      ...(relatedGenres.length > 0 ? [{
        "@type": "Question",
        "name": `${actressName}はどんなジャンルに出演していますか？`,
        "acceptedAnswer": {
          "@type": "Answer",
          "text": `${actressName}の主な出演ジャンルは「${relatedGenres.join("・")}」などです。`
        }
      }] : [])
    ]
  };

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema) }} />

      <div className="space-y-8 max-w-5xl mx-auto">
        <nav className="flex items-center gap-1.5 text-xs font-medium text-slate-500" aria-label="パンくずリスト">
          <Link href="/" className="hover:text-rose-600 transition-colors">ホーム</Link>
          <span className="text-slate-300">›</span>
          <span className="text-slate-700 font-bold">{actressName}</span>
        </nav>

        <section className="rounded-2xl bg-gradient-to-br from-slate-800 to-slate-950 p-8 md:p-10 border border-slate-700/30 shadow-sm">
          <div className="flex flex-col md:flex-row items-start md:items-center gap-6 justify-between">
            <div className="space-y-3">
              <span className="inline-flex text-[9px] font-bold tracking-widest text-rose-400 bg-rose-500/10 border border-rose-500/20 px-3 py-1 rounded">
                ACTRESS REVIEW
              </span>
              <h1 className="text-3xl md:text-4xl font-black text-white tracking-tight">{actressName}</h1>
              <p className="text-slate-400 text-sm leading-relaxed max-w-lg">
                {actressName}の全出演作品レビュー・感想まとめ。当サイトでは
                <strong className="text-slate-200">{actressPosts.length}作品</strong>のレビューを掲載しています。
              </p>
            </div>
            <div className="flex flex-wrap gap-3">
              <div className="text-center bg-white/5 border border-white/10 rounded-xl px-6 py-4">
                <span className="block text-3xl font-black text-rose-500">{actressPosts.length}</span>
                <span className="text-[9px] font-bold text-slate-400 uppercase tracking-widest">REVIEWS</span>
              </div>
            </div>
          </div>
        </section>

        {relatedGenres.length > 0 && (
          <section className="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-3">
            <h2 className="text-xs font-bold text-slate-500 uppercase tracking-widest">{actressName} の主な出演ジャンル</h2>
            <div className="flex flex-wrap gap-2">
              {relatedGenres.map(genre => (
                <Link key={genre} href={`/genre/${getGenreSlug(genre)}`}
                  className="text-xs font-bold text-slate-600 bg-slate-100 hover:bg-rose-50 hover:text-rose-600 border border-slate-200 hover:border-rose-200 px-3 py-1.5 rounded-full transition-colors duration-200">
                  {genre}
                </Link>
              ))}
            </div>
          </section>
        )}

        {/* 👑 キラーコンテンツ：【厳選10選】絶対に見るべき神作ランキング＆詳細シチュエーション解説 */}
        <section className="bg-gradient-to-b from-slate-900 via-slate-900 to-slate-950 border border-slate-800 rounded-3xl p-6 md:p-10 shadow-2xl space-y-8 text-white">
          <div className="space-y-3 text-center md:text-left border-b border-slate-800 pb-6">
            <span className="inline-flex text-[10px] font-black tracking-widest text-amber-400 bg-amber-400/10 border border-amber-400/20 px-3.5 py-1 rounded-full uppercase">
              SPECIAL FEATURE • 神作厳選
            </span>
            <h2 className="text-2xl md:text-3xl font-black tracking-tight text-white">
              【2026年最新】{actressName} の絶対に抜ける「神作」おすすめ10選！
            </h2>
            <p className="text-xs md:text-sm text-slate-400 leading-relaxed max-w-3xl">
              ファン必見！{actressName}の圧倒的なシチュエーション没入感、表情変化、プレイ内容（フェラ・体位・アングル・絶頂シーン）を徹底考察。ハズレなしの最高傑作10選をご紹介します。
            </p>
          </div>

          <div className="space-y-8">
            {actressPosts.slice(0, 10).map((post, idx) => {
              const cleanReviewText = post.review ? post.review.replace(/<[^>]*>/g, "").replace(/\s+/g, " ") : "";
              const excerpt = cleanReviewText.slice(0, 140) + "...";
              const rankNum = idx + 1;
              const isTop3 = rankNum <= 3;
              
              return (
                <div key={post.id} className="relative bg-slate-950/80 border border-slate-800/80 rounded-2xl p-5 md:p-7 shadow-md transition duration-200 hover:border-slate-700 flex flex-col md:flex-row gap-6 items-stretch">
                  {/* 順位バッジ */}
                  <div className={`absolute top-4 left-4 z-10 w-8 h-8 md:w-10 md:h-10 rounded-xl flex items-center justify-center font-black text-sm md:text-base shadow-lg ${
                    rankNum === 1 ? 'bg-amber-400 text-slate-950' : rankNum === 2 ? 'bg-slate-300 text-slate-950' : rankNum === 3 ? 'bg-amber-700 text-white' : 'bg-slate-800 text-slate-300'
                  }`}>
                    #{rankNum}
                  </div>

                  {/* ジャケット写真 */}
                  <div className="w-full md:w-64 flex-shrink-0 aspect-[16/10] md:aspect-[4/3] relative rounded-xl overflow-hidden bg-slate-900 border border-slate-800">
                    {post.image ? (
                      <img src={post.image} alt={`${post.title} ジャケット`} referrerPolicy="no-referrer" className="w-full h-full object-cover" loading="lazy" />
                    ) : (
                      <div className="w-full h-full flex items-center justify-center text-slate-500 text-xs">No Image</div>
                    )}
                  </div>

                  {/* 内容＆見どころ・プレイ解説 */}
                  <div className="flex-grow flex flex-col justify-between space-y-4">
                    <div className="space-y-3">
                      <div className="flex flex-wrap items-center gap-2 text-[10px] font-extrabold text-slate-400">
                        {post.hinban && (
                          <span className="text-rose-400 bg-rose-500/10 border border-rose-500/20 px-2 py-0.5 rounded font-black uppercase">
                            {post.hinban}
                          </span>
                        )}
                        <span>•</span>
                        <span>{post.maker}</span>
                      </div>
                      <h3 className="text-base md:text-lg font-black text-white leading-snug">
                        {post.title}
                      </h3>
                      <p className="text-xs md:text-sm text-slate-300 leading-relaxed font-medium bg-slate-900/60 p-3.5 rounded-xl border border-slate-800/60">
                        <strong className="text-amber-400 block mb-1 font-bold">🔥 プレイの見どころ・推しポイント：</strong>
                        {excerpt}
                      </p>

                      {/* 🎥 サンプル動画（表示可能時） */}
                      {post.sample_movie_url && (
                        <div className="space-y-1.5 pt-1">
                          <span className="text-[10px] font-bold text-amber-400 uppercase tracking-widest block">🎥 サンプル動画プレビュー</span>
                          <div className="w-full aspect-video rounded-xl overflow-hidden bg-black border border-slate-800">
                            <iframe
                              src={post.sample_movie_url}
                              className="w-full h-full border-none"
                              allowFullScreen
                              scrolling="no"
                              title={`${post.title} サンプル動画`}
                            />
                          </div>
                        </div>
                      )}

                      {/* 📷 サンプル画像プレビュー（alt属性完全対応） */}
                      {post.sample_images && post.sample_images.length > 0 && (
                        <div className="space-y-1.5 pt-1">
                          <span className="text-[10px] font-bold text-slate-400 uppercase tracking-widest block">📷 現場カット（サンプル写真）</span>
                          <div className="grid grid-cols-4 sm:grid-cols-6 gap-2">
                            {post.sample_images.slice(0, 6).map((img, i) => (
                              <a key={i} href={post.affiliate_url} target="_blank" rel="noopener noreferrer" className="block aspect-video relative overflow-hidden rounded-lg border border-slate-800 bg-slate-900 hover:border-amber-400 transition">
                                <img
                                  src={img}
                                  alt={`${actressName} ${post.title} サンプル名場面ショット ${i + 1}`}
                                  className="w-full h-full object-cover opacity-80 hover:opacity-100 transition"
                                  loading="lazy"
                                />
                              </a>
                            ))}
                          </div>
                        </div>
                      )}
                    </div>

                    {/* タグ＆CTAボタン */}
                    <div className="space-y-3 pt-2">
                      <div className="flex flex-wrap gap-1.5">
                        {(post.genres || []).slice(0, 5).map(g => (
                          <span key={g} className="text-[10px] font-bold text-slate-400 bg-slate-900 border border-slate-800 px-2.5 py-1 rounded-lg">
                            #{g}
                          </span>
                        ))}
                      </div>
                      <div className="flex flex-col sm:flex-row gap-2.5 pt-1">
                        <Link href={`/posts/${post.id}`} className="flex-1 text-center text-xs font-bold text-slate-200 bg-slate-900 border border-slate-700 hover:bg-slate-800 py-3 rounded-xl transition">
                          詳細レビューを読む
                        </Link>
                        <a href={post.affiliate_url} target="_blank" rel="noopener noreferrer" className="flex-1 text-center text-xs font-bold text-white bg-gradient-to-r from-rose-500 to-rose-600 hover:from-rose-400 hover:to-rose-500 py-3 rounded-xl shadow-lg transition">
                          🔥 FANZAで今すぐ視聴する
                        </a>
                      </div>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </section>

        <section className="space-y-4">
          <h2 className="text-lg font-extrabold text-slate-800">{actressName} の全出演作品レビュー（{actressPosts.length}件）</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
            {actressPosts.map(post => (
              <article key={post.id} className="flex flex-col rounded-2xl overflow-hidden bg-white border border-slate-200/80 shadow-sm card-hover-effect">
                <div className="aspect-[16/10] relative overflow-hidden bg-slate-100">
                  {post.image ? (
                    <img src={post.image} alt={`${post.title} ジャケット`} referrerPolicy="no-referrer" className="w-full h-full object-cover" loading="lazy" />
                  ) : (
                    <div className="w-full h-full flex items-center justify-center text-slate-400 text-xs">No Image</div>
                  )}
                  <span className="absolute top-3 left-3 text-[9px] font-bold bg-rose-500 text-white px-2 py-0.5 rounded shadow">18+</span>
                </div>
                <div className="p-4 flex-grow flex flex-col justify-between space-y-3">
                  <div className="space-y-1.5">
                    <div className="flex items-center justify-between text-[9px] font-bold text-slate-400">
                      <time dateTime={post.date}>{post.date?.split(" ")[0]}</time>
                      {post.hinban && <span className="text-rose-600 bg-rose-50 px-1.5 py-0.5 rounded border border-rose-100">{post.hinban}</span>}
                    </div>
                    <h3 className="text-sm font-extrabold text-slate-800 leading-snug line-clamp-2">{post.title}</h3>
                    <div className="flex flex-wrap gap-1">
                      {(post.genres || []).slice(0, 3).map(g => (
                        <span key={g} className="text-[9px] font-bold text-slate-500 bg-slate-100 border border-slate-200 px-1.5 py-0.5 rounded">{g}</span>
                      ))}
                    </div>
                  </div>
                  <div className="flex gap-2">
                    <Link href={`/posts/${post.id}`} className="flex-1 text-center text-xs font-bold text-slate-700 bg-white border border-slate-300 hover:bg-slate-50 py-2 rounded-lg transition">レビューを読む</Link>
                    <a href={post.affiliate_url} target="_blank" rel="noopener noreferrer" className="flex-1 text-center text-xs font-bold text-white bg-gradient-to-r from-rose-500 to-rose-600 hover:from-rose-400 hover:to-rose-500 py-2 rounded-lg shadow transition">視聴する</a>
                  </div>
                </div>
              </article>
            ))}
          </div>
        </section>

        {coActresses.length > 0 && (
          <section className="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-3">
            <h2 className="text-xs font-bold text-slate-500 uppercase tracking-widest">{actressName} の共演女優</h2>
            <div className="flex flex-wrap gap-2">
              {coActresses.map(actress => (
                <Link key={actress} href={`/actress/${getActressSlug(actress)}`}
                  className="text-xs font-bold text-rose-600 bg-rose-50 hover:bg-rose-100 border border-rose-200 px-3 py-1.5 rounded-full transition-colors">
                  {actress}
                </Link>
              ))}
            </div>
          </section>
        )}

        <section className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm space-y-4">
          <h2 className="text-sm font-extrabold text-slate-800">{actressName} に関するよくある質問</h2>
          <div className="space-y-4 divide-y divide-slate-100">
            <div className="pt-4 first:pt-0 space-y-1.5">
              <p className="text-sm font-bold text-slate-700">Q. {actressName}の作品はどこで見られますか？</p>
              <p className="text-xs text-slate-500 leading-relaxed">A. {actressName}の作品はFANZA（DMM）で配信されています。当サイトでは{actressPosts.length}作品のレビューを掲載しています。</p>
            </div>
            <div className="pt-4 space-y-1.5">
              <p className="text-sm font-bold text-slate-700">Q. {actressName}のおすすめ作品は？</p>
              <p className="text-xs text-slate-500 leading-relaxed">A. {actressPosts[0]?.title || ""}などがおすすめです。各作品ページで詳しいレビュー・感想をご確認ください。</p>
            </div>
          </div>
        </section>

        <section className="text-center py-6">
          <a href={`https://al.fanza.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fsearch%2F-%2F%3Fsearchstr%3D${encodeURIComponent(actressName)}%2F&af_id=onchan555-003`}
            target="_blank" rel="noopener noreferrer"
            className="inline-block px-8 py-4 text-base font-extrabold text-white bg-gradient-to-r from-rose-500 via-rose-600 to-pink-600 hover:from-rose-400 hover:to-rose-500 rounded-xl shadow-md transition duration-200">
            ✨ {actressName} の全作品をFANZAで見る
          </a>
          <p className="text-[10px] text-slate-400 mt-2">※クリックするとFANZA（18禁公式サイト）へ遷移します</p>
        </section>
      </div>
    </>
  );
}
