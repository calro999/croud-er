import Link from "next/link";
import Script from "next/script";
import { notFound } from "next/navigation";
import Image from "next/image";
import { Metadata } from "next";
import { censorText } from "@/lib/censor";
import { getActressSlug, getGenreSlug } from "@/lib/slugs";
import UnlimitedPromotionBox from "@/app/components/UnlimitedPromotionBox";
import { getAllPostIds, getPostById, getSimilarPosts, PostDetail } from "@/lib/posts";
import { getActressWikiData, getSimilarActresses } from "@/lib/actress";

type Post = PostDetail;

export const dynamicParams = false;

export async function generateStaticParams() {
  const ids = getAllPostIds();
  return ids.map((id) => ({ id }));
}

export async function generateMetadata({ params }: { params: Promise<{ id: string }> }): Promise<Metadata> {
  const { id } = await params;
  const post = getPostById(id);

  if (!post) {
    return {
      title: "作品が見つかりません",
    };
  }

  try {
    const hinbanText = post.hinban || post.id;
    const actressText = (post.actresses || []).join("・");
    const genreText = (post.genres || []).slice(0, 3).join("・");
    const shortTitle = post.title.length > 15 ? post.title.slice(0, 15) + '…' : post.title;
    const titleText = actressText 
      ? `【ガチ評価】${hinbanText}（${shortTitle}）は本当に抜ける？${actressText}の出演シーンを徹底レビュー！`
      : `【ガチ評価】${hinbanText}（${shortTitle}）は本当に抜ける？出演シーンを徹底レビュー！`;

    const cleanReview = post.review ? post.review.replace(/<[^>]*>/g, "").replace(/\s+/g, " ") : "";
    const reviewExcerpt = cleanReview.slice(0, 50) + "...";

    const descriptionText = actressText
      ? `${actressText}の最新作『${hinbanText}』を最速レビュー！SNSで話題の「${genreText || '注目ジャンル'}」はサンプル詐欺じゃない？【${reviewExcerpt}】ハズレを引きたくない方は購入前の参考にどうぞ！`
      : `最新作『${hinbanText}』を最速レビュー！SNSで話題の「${genreText || '注目ジャンル'}」はサンプル詐欺じゃない？【${reviewExcerpt}】ハズレを引きたくない方は購入前の参考にどうぞ！`;

    const keywords = [
      ...(post.actresses || []).map(a => `${a} レビュー`),
      ...(post.actresses || []).map(a => `${a} 出演作品`),
      ...(post.genres || []),
      hinbanText,
      post.title,
      "FANZA", "AV レビュー", "アダルト動画 感想"
    ];

    return {
      title: titleText,
      description: descriptionText.slice(0, 155),
      keywords: keywords.join(","),
      alternates: {
        canonical: `https://haitoku.pages.dev/posts/${id}`,
      },
      openGraph: {
        title: censorText(titleText),
        description: censorText(descriptionText.slice(0, 155)),
        url: `https://haitoku.pages.dev/posts/${id}`,
        type: "article",
        publishedTime: post.date || undefined,
        authors: ["背徳の深夜書斎"],
        images: post.image ? [{ url: post.image, alt: censorText(post.title), width: 800, height: 538 }] : [],
      },
      twitter: {
        card: "summary_large_image",
        title: censorText(titleText),
        description: censorText(descriptionText.slice(0, 155)),
        images: post.image ? [post.image] : [],
      }
    };
  } catch (e) {
    console.error(`Failed to generate metadata for post ${id}:`, e);
    return {
      title: "背徳の深夜書斎",
    };
  }
}

export default async function PostPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const post = getPostById(id);

  if (!post) {
    notFound();
  }

  // 発売日時前の未発売・予約商品は発売日まで非表示（404）
  if (post.date && new Date(post.date).getTime() > Date.now()) {
    notFound();
  }

  const hinbanText = post.hinban || post.id;
  const similarItems = getSimilarPosts(post, 4);

  // 出演女優の情報
  const mainActress = (post.actresses && post.actresses.length > 0) ? post.actresses[0] : null;
  const actressWiki = mainActress ? getActressWikiData(mainActress) : null;
  const similarActresses = mainActress ? getSimilarActresses(mainActress, 3) : [];

  // AI-SEO / GEO 向け JSON-LD 構造化データ
  const cleanReviewText = post.review ? post.review.replace(/<[^>]*>/g, "") : "";
  const actressNames = (post.actresses || []).join("・");
  const genreNames = (post.genres || []).join("・");

  // 作品固有の魅力的で熱狂的な動的CTA文言生成（AI臭さゼロ・実用官能特化）
  const cleanTitle = post.title.replace(/【.*?】/g, "").trim() || post.title;
  // 「ハイビジョン」「4K」「独占配信」などの非官能タグを除外し、エロ・シチュエーション特化ジャンルを抽出
  const sexyGenres = (post.genres || []).filter(g => 
    !["ハイビジョン", "4K", "独占配信", "単体作品", "完全版", "大容量", "DMM独占", "ベスト・総集編"].includes(g)
  );
  const targetGenre = sexyGenres.length > 0 ? sexyGenres[0] : (post.genres?.[0] || "");
  
  let dynamicCtaText = "";
  if (mainActress && targetGenre) {
    dynamicCtaText = `🔥 『${mainActress}』の濃厚${targetGenre}本番シーンを今すぐフル視聴する！`;
  } else if (mainActress) {
    dynamicCtaText = `🔥 『${mainActress}』が限界まで乱れる本編を今すぐ高画質で視聴する！`;
  } else if (targetGenre) {
    dynamicCtaText = `🔥 抜きどころ満載！極上の『${targetGenre}』シーンを今すぐフル視聴する！`;
  } else {
    dynamicCtaText = `🔥 絶頂クライマックス！この作品の本編を高画質で今すぐ視聴する！`;
  }

  const articleSchema = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": `${post.title}【${hinbanText}】${actressNames ? actressNames + 'の' : ''}レビュー・感想・評価`,
    "description": cleanReviewText.slice(0, 150) + "...",
    "image": post.image ? [post.image] : [],
    "author": {
      "@type": "Organization",
      "name": "背徳の深夜書斎",
      "url": "https://haitoku.pages.dev"
    },
    "publisher": {
      "@type": "Organization",
      "name": "背徳の深夜書斎",
      "url": "https://haitoku.pages.dev"
    },
    "datePublished": post.date ? post.date.split(' ')[0] : new Date().toISOString().split('T')[0],
    "dateModified": post.date ? post.date.split(' ')[0] : new Date().toISOString().split('T')[0],
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": `https://haitoku.pages.dev/posts/${post.id}`
    },
    "keywords": [
      hinbanText,
      post.title,
      ...(post.actresses || []),
      ...(post.genres || [])
    ].join(",")
  };

  const reviewSchema = {
    "@context": "https://schema.org",
    "@type": "Review",
    "itemReviewed": {
      "@type": "Movie",
      "name": post.title,
      "image": post.image,
      "description": cleanReviewText.slice(0, 150) + "...",
      "director": {
        "@type": "Organization",
        "name": (post.directors && post.directors.length > 0) ? post.directors[0] : (post.maker || "メーカー不明")
      },
      "actor": (post.actresses || []).map(actress => ({
        "@type": "Person",
        "name": actress
      }))
    },
    "author": {
      "@type": "Organization",
      "name": "背徳の深夜書斎",
      "url": "https://haitoku.pages.dev"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": "4.8",
      "bestRating": "5",
      "worstRating": "1"
    },
    "publisher": {
      "@type": "Organization",
      "name": "背徳の深夜書斎",
      "url": "https://haitoku.pages.dev"
    },
    "datePublished": post.date ? post.date.split(' ')[0] : new Date().toISOString().split('T')[0],
    "reviewBody": cleanReviewText
  };

  const faqSchema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": `${post.title}（${hinbanText}）はどこで一番安く見られますか？`,
        "acceptedAnswer": {
          "@type": "Answer",
          "text": `「${post.title}」はFANZA（DMM）にてストリーミング配信（300円〜）されています。高画質ダウンロード版やFANZA見放題chでも楽しめます。`
        }
      },
      ...(post.actresses && post.actresses.length > 0 ? [{
        "@type": "Question",
        "name": `${post.actresses[0]}の他の出演作品や監督情報は？`,
        "acceptedAnswer": {
          "@type": "Answer",
          "text": `${post.actresses[0]}のWikipedia風プロフィールや全出演作・監督一覧は当サイトの女優専用ページでご確認いただけます。`
        }
      }] : []),
      {
        "@type": "Question",
        "name": `${post.title}のジャンルや見どころは？`,
        "acceptedAnswer": {
          "@type": "Answer",
          "text": `ジャンルは「${genreNames || '詳細はFANZAでご確認ください'}」です。詳しいレビュー・感想は当ページの本文をご覧ください。`
        }
      }
    ]
  };

  const breadcrumbSchema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "ホーム",
        "item": "https://haitoku.pages.dev"
      },
      ...(mainActress ? [{
        "@type": "ListItem",
        "position": 2,
        "name": mainActress,
        "item": `https://haitoku.pages.dev/actress/${getActressSlug(mainActress)}`
      }] : []),
      {
        "@type": "ListItem",
        "position": mainActress ? 3 : 2,
        "name": post.title,
        "item": `https://haitoku.pages.dev/posts/${post.id}`
      }
    ]
  };

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(articleSchema) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(reviewSchema) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema) }} />

      <article className="space-y-8 max-w-4xl mx-auto" lang="ja">
        {/* パンくずナビゲーション */}
        <nav aria-label="パンくずリスト" className="flex items-center gap-1.5 text-xs font-medium text-slate-500">
          <Link href="/" className="hover:text-rose-600 transition-colors duration-200">ホーム</Link>
          <span className="text-slate-300">›</span>
          {mainActress && (
            <>
              <Link href={`/actress/${getActressSlug(mainActress)}`} className="hover:text-rose-600 transition-colors duration-200">
                {mainActress}（Wiki）
              </Link>
              <span className="text-slate-300">›</span>
            </>
          )}
          <span className="text-slate-700 line-clamp-1 max-w-[220px]">{post.title}</span>
        </nav>

        {/* メイン詳細パネル */}
        <div className="border border-slate-200 bg-white rounded-3xl p-6 md:p-10 shadow-sm space-y-8">

          {/* ヘッダー情報 */}
          <header className="space-y-3">
            <div className="flex flex-wrap items-center gap-2 text-[10px] font-bold text-slate-400 uppercase tracking-widest">
              <time dateTime={post.date}>{post.date?.split(' ')[0]}</time>
              <span>•</span>
              <span className="text-rose-600">{post.maker || "単体作品"}</span>
              {post.directors && post.directors.length > 0 && (
                <>
                  <span>•</span>
                  <span className="text-indigo-600">監督: {post.directors[0]}</span>
                </>
              )}
            </div>
            <h1 className="text-xl md:text-3xl font-black leading-snug text-slate-900">
              {post.title}
            </h1>
            <div className="flex flex-wrap gap-1.5 pt-1">
              {post.labels?.map((lbl) => (
                <span key={lbl} className="bg-rose-50 text-rose-600 border border-rose-100 text-[10px] font-bold px-2.5 py-0.5 rounded-full">
                  #{lbl}
                </span>
              ))}
            </div>
          </header>

          {/* アートジャケット画像 */}
          <section className="flex justify-center bg-slate-900 rounded-2xl p-4 border border-slate-800 overflow-hidden" aria-label="作品ジャケット">
            <a href={post.affiliate_url} target="_blank" rel="noopener noreferrer" className="block relative group max-w-full">
              <img
                src={post.image}
                alt={`${post.title} ジャケット公式画像`}
                referrerPolicy="no-referrer"
                className="max-h-[500px] w-auto object-contain rounded-xl shadow-2xl group-hover:opacity-90 transition duration-300"
              />
              <div className="absolute inset-0 bg-slate-950/40 opacity-0 group-hover:opacity-100 transition duration-200 flex items-center justify-center rounded-xl">
                <span className="text-xs font-bold text-white bg-rose-600 px-5 py-3 rounded-xl shadow-xl">
                  🔥 FANZA公式サイトで高画質プレビュー
                </span>
              </div>
            </a>
          </section>

          {/* 🏷️ 【追加依頼5位】セール・価格・配信形態ボックス（「今買う理由」） */}
          <section className="bg-gradient-to-r from-slate-900 to-slate-950 text-white p-5 md:p-6 rounded-2xl border border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div className="space-y-1 text-center sm:text-left">
              <span className="text-[10px] font-black text-amber-400 uppercase tracking-widest bg-amber-400/10 px-2.5 py-0.5 rounded border border-amber-400/20">
                OFFICIAL STREAMING & DOWNLOAD
              </span>
              <h2 className="text-sm md:text-base font-black text-white">
                ストリーミングなら <span className="text-amber-400 text-lg">300円〜</span> 今すぐ視聴可能！
              </h2>
              <p className="text-xs text-slate-400">
                スマホ・PCでダウンロード保存して永久視聴（HD/4K）も選択できます。
              </p>
            </div>
            <a
              href={post.affiliate_url}
              target="_blank"
              rel="noopener noreferrer"
              className="w-full sm:w-auto text-center px-6 py-3.5 bg-gradient-to-r from-rose-500 to-pink-600 hover:from-rose-400 hover:to-pink-500 text-white text-xs md:text-sm font-black rounded-xl shadow-lg transition flex-shrink-0"
            >
              🔥 最安値で作品を見る（FANZA）
            </a>
          </section>

          {/* サンプル写真スライド */}
          {post.sample_images && post.sample_images.length > 0 && (
            <section className="space-y-3" aria-label="サンプルプレビュー画像">
              <h3 className="text-xs font-bold text-slate-500 uppercase tracking-widest">
                📷 現場の瞬間・サンプル写真（{post.sample_images.length}枚）
              </h3>
              <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-2.5">
                {post.sample_images.slice(0, 10).map((imgUrl, idx) => (
                  <a
                    key={idx}
                    href={post.affiliate_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="block aspect-video relative overflow-hidden rounded-xl border border-slate-200 bg-slate-100 hover:border-rose-500 transition duration-200 transform hover:scale-105"
                  >
                    <img
                      src={imgUrl}
                      alt={`${post.title} サンプル場面カット ${idx + 1}`}
                      referrerPolicy="no-referrer"
                      className="w-full h-full object-cover opacity-90 hover:opacity-100 transition duration-200"
                      loading="lazy"
                    />
                  </a>
                ))}
              </div>
            </section>
          )}

          {/* メタ情報・タグ探索ボックス（出演女優・作品属性・メーカー・品番） */}
          <section className="p-5 md:p-6 rounded-3xl bg-slate-50 border border-slate-200 text-xs space-y-4 shadow-sm" aria-label="作品基本スペック情報">
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-4 border-b border-slate-200/80 pb-4">
              <div className="space-y-1">
                <span className="text-slate-400 font-bold uppercase tracking-wider block text-[9px]">品番</span>
                <span className="text-slate-900 font-black font-mono text-sm">{hinbanText}</span>
              </div>
              <div className="space-y-1">
                <span className="text-slate-400 font-bold uppercase tracking-wider block text-[9px]">制作メーカー / 監督</span>
                <div className="text-slate-800 font-bold text-xs flex items-center gap-1 flex-wrap">
                  {post.maker ? (
                    <Link href={`/maker/${encodeURIComponent(post.maker)}`} className="text-slate-700 hover:text-rose-600 underline">
                      {post.maker}
                    </Link>
                  ) : "公式メーカー"}
                  {post.directors && post.directors.length > 0 && (
                    <span className="text-indigo-600 text-[11px]">（{post.directors[0]}組）</span>
                  )}
                </div>
              </div>
              <div className="space-y-1 col-span-2 sm:col-span-1">
                <span className="text-slate-400 font-bold uppercase tracking-wider block text-[9px]">公式最安配信価格</span>
                <span className="text-rose-600 font-black text-sm block">
                  300円〜（ストリーミング）
                </span>
              </div>
            </div>

            {/* 🏷️ 出演女優タグ（同女優の別作品・Wikiへワンタップ） */}
            <div className="space-y-2">
              <span className="text-[10px] font-bold text-rose-600 bg-rose-50 border border-rose-100 px-2.5 py-0.5 rounded-full uppercase inline-block">
                ACTRESS • 出演女優（別作品・まとめを見る）
              </span>
              <div className="flex flex-wrap gap-2 pt-1">
                {post.actresses && post.actresses.length > 0 ? (
                  post.actresses.map(a => (
                    <Link
                      key={a}
                      href={`/actress/${getActressSlug(a)}`}
                      className="inline-flex items-center gap-1.5 bg-white hover:bg-rose-500 text-rose-600 hover:text-white border border-rose-200 hover:border-rose-500 px-3.5 py-1.5 rounded-xl font-black text-xs shadow-sm transition duration-200 group"
                    >
                      <span>💃 {a}</span>
                      <span className="text-[10px] opacity-80 group-hover:text-white">の全出演作・神作10選 ›</span>
                    </Link>
                  ))
                ) : (
                  <span className="text-slate-500 font-medium">単体・素人作品</span>
                )}
              </div>
            </div>

            {/* 🏷️ 作品属性（ジャンル）タグ（関連ジャンルの作品群へ横展開） */}
            {post.genres && post.genres.length > 0 && (
              <div className="space-y-2 pt-2 border-t border-slate-200/60">
                <span className="text-[10px] font-bold text-indigo-600 bg-indigo-50 border border-indigo-100 px-2.5 py-0.5 rounded-full uppercase inline-block">
                  GENRES • 作品属性（同ジャンルの人気作品を見る）
                </span>
                <div className="flex flex-wrap gap-1.5 pt-1">
                  {post.genres.map(g => (
                    <Link
                      key={g}
                      href={`/genre/${getGenreSlug(g)}`}
                      className="inline-block bg-white hover:bg-indigo-600 text-slate-700 hover:text-white border border-slate-200 hover:border-indigo-600 px-2.5 py-1 rounded-lg text-xs font-bold transition shadow-2xs"
                    >
                      #{g}
                    </Link>
                  ))}
                </div>
              </div>
            )}
          </section>

          {/* 濃厚レビューテキスト */}
          <section className="prose prose-slate max-w-none text-slate-700 space-y-6 leading-relaxed text-sm md:text-base font-medium" aria-label="詳細考察レビュー">
            <div
              className="review-content-html"
              dangerouslySetInnerHTML={{ __html: post.review || (post as any).content || "" }}
            />
          </section>

          {/* 🔥 【目立つ上部CTA】レビュー直後の個別作品クリック誘導ボタン */}
          <section className="py-2 text-center space-y-2 bg-gradient-to-r from-rose-50 via-pink-50 to-rose-50 border border-rose-200/80 rounded-2xl p-5 shadow-sm">
            <span className="text-[10px] font-black text-rose-600 bg-rose-100/80 px-2.5 py-0.5 rounded-full uppercase tracking-wider">
              STREAMING & DOWNLOAD AVAILABLE
            </span>
            <div className="pt-1">
              <a
                href={post.affiliate_url}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-block w-full sm:w-auto px-8 py-4 text-sm md:text-base font-black text-white bg-gradient-to-r from-rose-500 via-rose-600 to-pink-600 hover:from-rose-400 hover:to-pink-500 rounded-xl shadow-lg hover:shadow-rose-500/25 transition duration-200"
              >
                {dynamicCtaText}
              </a>
            </div>
            <p className="text-[10px] text-slate-500">
              ※FANZA公式（最安300円〜 / 高画質HD・4K対応）で今すぐ視聴
            </p>
          </section>

          {/* サンプル動画 */}
          {post.sample_movie_url && (
            <section className="space-y-3 pt-4 border-t border-slate-100">
              <h3 className="text-xs font-bold text-slate-500 uppercase tracking-widest flex items-center gap-1.5">
                🎥 サンプル動画プレビュー
              </h3>
              <div className="w-full aspect-video rounded-2xl overflow-hidden bg-black border border-slate-800 shadow-xl">
                <iframe 
                  src={post.sample_movie_url} 
                  className="w-full h-full border-none" 
                  allowFullScreen 
                  scrolling="no"
                  title={`${post.title} サンプル動画`}
                />
              </div>
              <div className="pt-1 text-center">
                <a
                  href={post.affiliate_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-block text-xs font-black text-rose-600 hover:text-rose-500 bg-rose-50 hover:bg-rose-100/80 border border-rose-200 px-6 py-2.5 rounded-xl transition"
                >
                  👉 サンプル動画の続き・本編をFANZAでフル視聴する
                </a>
              </div>
            </section>
          )}

          {/* 🧭 【追加依頼4位＆6位】あなたならどれ？初心者向け探索 ＆ 診断ガイド */}
          <section className="bg-gradient-to-br from-slate-900 to-slate-950 text-white rounded-3xl p-6 md:p-8 shadow-xl space-y-4">
            <div className="space-y-1">
              <span className="text-[10px] font-black text-rose-400 bg-rose-500/20 px-3 py-1 rounded-full uppercase tracking-wider">
                EXPLORE & DIAGNOSIS • あなたならどれ？
              </span>
              <h2 className="text-lg md:text-xl font-black text-white">
                【視聴診断】この作品を観るべきか迷っているあなたへ
              </h2>
              <p className="text-xs text-slate-300 leading-relaxed">
                「好みに合わなかったらどうしよう…」と迷ったときの選び方チェックシートです。
              </p>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
              <div className="bg-slate-800/80 border border-slate-700/60 p-4 rounded-2xl space-y-1.5">
                <span className="text-xs font-black text-amber-400 flex items-center gap-1">✅ こんな人には絶対刺さる！</span>
                <ul className="text-xs text-slate-300 space-y-1 list-disc list-inside">
                  <li>{post.genres?.slice(0, 2).join('・') || 'このジャンル'}のシチュエーションで抜きたい</li>
                  <li>女優の生々しい表情変化や焦らしの演技を楽しみたい</li>
                  <li>前置きなしで即効性の高い実用シーンを求めている</li>
                </ul>
              </div>

              <div className="bg-slate-800/80 border border-slate-700/60 p-4 rounded-2xl space-y-1.5">
                <span className="text-xs font-black text-pink-400 flex items-center gap-1">💡 次に見るべき選択肢</span>
                <p className="text-xs text-slate-300">
                  {mainActress ? `${mainActress}の他作品をチェックするか、同系統の類似作品を下記からお選びください。` : '関連ジャンルの他作品も合わせて比較してみてください。'}
                </p>
                {mainActress && (
                  <Link href={`/actress/${getActressSlug(mainActress)}`} className="inline-block text-xs font-bold text-rose-400 hover:text-rose-300 pt-1">
                    👉 {mainActress} のWikipedia風まとめ・神作10選へ
                  </Link>
                )}
              </div>
            </div>
          </section>

          {/* 🔗 【追加依頼1位】作品 → 類似作品（「この作品が好きなら次はこれ」） */}
          <section className="pt-6 border-t border-slate-100 space-y-4" aria-label="類似作品レコメンド">
            <div className="space-y-1">
              <span className="text-[10px] font-bold text-rose-600 bg-rose-50 border border-rose-100 px-2.5 py-0.5 rounded-full uppercase">
                SIMILAR WORKS
              </span>
              <h2 className="text-lg md:text-xl font-black text-slate-900">
                『この作品が好きなら次はこれ』おすすめ類似作品
              </h2>
              <p className="text-xs text-slate-500">
                同じ系統の背徳感・シチュエーション・出演キャストで選んだ間違いのない注目作です。
              </p>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
              {similarItems.map(({ post: relPost, matchReason }) => (
                <div key={relPost.id} className="flex gap-3 p-3.5 rounded-2xl bg-slate-50 border border-slate-200/90 hover:border-rose-300 transition duration-200 group">
                  <div className="w-20 h-28 bg-slate-200 rounded-xl overflow-hidden flex-shrink-0 relative">
                    {relPost.image ? (
                      <img src={relPost.image} alt={relPost.title} referrerPolicy="no-referrer" className="w-full h-full object-cover group-hover:scale-105 transition duration-300" loading="lazy" />
                    ) : (
                      <div className="w-full h-full flex items-center justify-center text-slate-400 text-[10px]">No Image</div>
                    )}
                  </div>
                  <div className="flex-1 flex flex-col justify-between space-y-1.5">
                    <div>
                      <span className="text-[9px] font-bold text-rose-600 bg-rose-50 px-2 py-0.5 rounded-md border border-rose-100 inline-block mb-1">
                        {matchReason}
                      </span>
                      <h3 className="text-xs font-bold text-slate-900 leading-snug line-clamp-2 group-hover:text-rose-600 transition">
                        {relPost.title}
                      </h3>
                    </div>
                    <div className="flex gap-2 pt-1">
                      <Link href={`/posts/${relPost.id}`} className="flex-1 text-center text-[11px] font-bold text-slate-700 bg-white border border-slate-300 hover:bg-slate-50 py-1.5 rounded-lg transition">
                        レビュー
                      </Link>
                      <a href={relPost.affiliate_url} target="_blank" rel="noopener noreferrer" className="flex-1 text-center text-[11px] font-bold text-white bg-gradient-to-r from-rose-500 to-rose-600 hover:from-rose-400 hover:to-rose-500 py-1.5 rounded-lg shadow transition">
                        視聴する
                      </a>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </section>

          {/* 👯 【推し探し特化】女優 → 類似女優（「この女優が好きならこの人も」） */}
          {mainActress && similarActresses.length > 0 && (
            <section className="pt-6 border-t border-slate-100 space-y-4">
              <div className="space-y-1">
                <span className="text-[10px] font-bold text-indigo-600 bg-indigo-50 border border-indigo-100 px-2.5 py-0.5 rounded-full uppercase inline-block">
                  NEXT OSHI • この女優が好きならおすすめ
                </span>
                <h2 className="text-lg md:text-xl font-black text-slate-900">
                  『{mainActress}』が好きならこの女優もチェック！
                </h2>
                <p className="text-xs text-slate-500">
                  同系統の極上ボディや共通の監督・シチュエーションで魅せる注目女優です。
                </p>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-2">
                {similarActresses.map(sim => (
                  <Link
                    key={sim.name}
                    href={`/actress/${getActressSlug(sim.name)}`}
                    className="group flex sm:flex-col bg-slate-50 border border-slate-200 rounded-2xl overflow-hidden hover:border-indigo-300 hover:shadow-sm transition p-3 gap-3"
                  >
                    <div className="w-16 h-16 sm:w-20 sm:h-20 mx-auto rounded-full bg-slate-200 overflow-hidden relative flex-shrink-0">
                      {sim.image ? (
                        <img src={sim.image} alt={sim.name} className="w-full h-full object-cover group-hover:scale-110 transition" loading="lazy" />
                      ) : (
                        <div className="w-full h-full flex items-center justify-center text-xs text-slate-400 font-bold">{sim.name[0]}</div>
                      )}
                    </div>
                    <div className="flex-1 space-y-1 text-left sm:text-center">
                      <h3 className="text-xs md:text-sm font-bold text-slate-900 group-hover:text-indigo-600 truncate">{sim.name}</h3>
                      <div className="bg-white border border-indigo-100 rounded-lg p-2 text-left">
                        <span className="text-[9px] font-bold text-indigo-600 block mb-0.5">💡 推しポイント</span>
                        <p className="text-[10px] text-slate-600 line-clamp-2 leading-relaxed">{sim.reason}</p>
                      </div>
                    </div>
                  </Link>
                ))}
              </div>
            </section>
          )}

          {/* 🏷️ 関連ジャンル一覧 */}
          {post.genres && post.genres.length > 0 && (
            <section className="pt-6 border-t border-slate-100 space-y-3">
              <h3 className="text-xs font-bold text-slate-500 uppercase tracking-widest">
                🏷️ 関連ジャンル・おすすめ特集
              </h3>
              <div className="flex flex-wrap gap-2">
                {post.genres.slice(0, 10).map(g => (
                  <Link
                    key={g}
                    href={`/genre/${getGenreSlug(g)}`}
                    className="text-xs font-bold text-slate-700 bg-slate-100 hover:bg-rose-50 hover:text-rose-600 border border-slate-200 px-3.5 py-1.5 rounded-full transition"
                  >
                    #{g} 特集を見る
                  </Link>
                ))}
              </div>
            </section>
          )}

          {/* 全記事下部：FANZA見放題ch 特設キラー誘導ボックス */}
          <UnlimitedPromotionBox />

          {/* 極上のプレミアムCTAボタン（最下部） */}
          <section className="pt-6 border-t border-slate-100 text-center space-y-3" aria-label="視聴誘導">
            <a
              href={post.affiliate_url}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-block w-full sm:w-auto px-8 py-4.5 text-base font-extrabold text-white bg-gradient-to-r from-rose-500 via-rose-600 to-pink-600 hover:from-rose-400 hover:to-rose-500 rounded-2xl shadow-xl transition duration-200 cursor-pointer"
            >
              {dynamicCtaText}
            </a>
            <p className="text-[10px] text-slate-400">
              ※クリックするとFANZA（18禁公式サイト）へ直接遷移します
            </p>
          </section>
        </div>
      </article>
    </>
  );
}
