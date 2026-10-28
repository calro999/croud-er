import Link from "next/link";
import { notFound } from "next/navigation";
import { Metadata } from "next";
import { censorText } from "@/lib/censor";
import { getActressSlug, getGenreSlug } from "@/lib/slugs";
import UnlimitedPromotionBox from "@/app/components/UnlimitedPromotionBox";
import TenSelectionCollage from "@/app/components/TenSelectionCollage";
import FloatingCta from "@/app/components/FloatingCta";
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
      title: "記事が見つかりません",
    };
  }

  const isFeature = post.id.startsWith("feature_");

  if (isFeature) {
    const cleanContent = (post.review || (post as any).content || "").replace(/<[^>]*>/g, "").replace(/\s+/g, " ");
    const desc = cleanContent.slice(0, 155) + "...";
    return {
      title: post.title,
      description: desc,
      keywords: (post.genres || post.labels || []).join(","),
      alternates: {
        canonical: `https://haitoku.pages.dev/posts/${id}`,
      },
      openGraph: {
        title: post.title,
        description: desc,
        url: `https://haitoku.pages.dev/posts/${id}`,
        type: "article",
        publishedTime: post.date || undefined,
        authors: ["背徳エロス編集部"],
        images: post.image ? [{ url: post.image, alt: post.title, width: 800, height: 538 }] : [],
      },
      twitter: {
        card: "summary_large_image",
        title: post.title,
        description: desc,
        images: post.image ? [post.image] : [],
      }
    };
  }

  try {
    const hinbanText = post.hinban || post.id;
    const actressText = (post.actresses || []).join("・");
    const genreText = (post.genres || []).slice(0, 3).join("・");

    // タイトルから装飾や重複品番をクリーンアップ
    const rawCleanTitle = post.title.replace(/【.*?】|\[.*?\]/g, "").trim() || post.title;
    const cleanTitle = rawCleanTitle.length > 40 ? rawCleanTitle.slice(0, 40) + '…' : rawCleanTitle;

    // タイトルとディスクリプションを検索クエリ（品番・女優・正式タイトル・感想・抜きどころ）に完全一致させるSEO設計
    const hash = (post.id || "").split("").reduce((acc, char) => acc + char.charCodeAt(0), 0);
    const titlePatterns = [
      actressText
        ? `【${hinbanText}】${actressText}『${cleanTitle}』の見どころと実用度を本音レビュー`
        : `【${hinbanText}】『${cleanTitle}』の見どころ＆抜きどころ徹底解剖レビュー`,
      actressText
        ? `${hinbanText} ${actressText}『${cleanTitle}』は本当に抜ける？濃厚シーン・実用度検証`
        : `${hinbanText}『${cleanTitle}』ガチ評価！見どころ・抜けるポイント徹底解説`,
      actressText
        ? `【${hinbanText} レビュー】${actressText}主演『${cleanTitle}』の見逃せない名シーンまとめ`
        : `【${hinbanText} レビュー】『${cleanTitle}』のシチュエーションと魅力を徹底検証`,
    ];
    const titleText = titlePatterns[hash % titlePatterns.length];

    const cleanReview = ((post as any).body || post.review || (post as any).content || "").replace(/<[^>]*>/g, "").replace(/\s+/g, " ");
    const reviewExcerpt = cleanReview.slice(0, 75) + "...";

    const descPatterns = [
      actressText
        ? `【品番：${hinbanText}】${actressText}出演『${cleanTitle}』の配信速報＆本音レビュー！${reviewExcerpt} 無料サンプル動画や見どころ、実用度スコアを徹底解説。`
        : `【品番：${hinbanText}】話題作『${cleanTitle}』の公式レビュー！${reviewExcerpt} 濃厚シーンの抜けるポイントや無料プレビュー情報を詳しく解説。`,
      actressText
        ? `${actressText}の熱演が光る${hinbanText}『${cleanTitle}』の独自評価まとめ。${reviewExcerpt} 実際に抜ける重要シーンや購入前のポイントをチェック！`
        : `注目作${hinbanText}『${cleanTitle}』の見どころと実用度を詳しくレビュー！${reviewExcerpt} 視聴前の参考にどうぞ。`,
    ];
    const descriptionText = descPatterns[hash % descPatterns.length];

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

  const isFeature = post.id.startsWith("feature_");

  // ==========================================
  // 🌟 特集記事専用の独立レンダリング（ダークテーマ・AVテンプレート汚染ゼロ）
  // ==========================================
  if (isFeature) {
    const articleContent = (post as any).content || post.review || "";
    const featureSchema = {
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": post.title,
      "description": post.title,
      "image": post.image ? [post.image] : [],
      "author": {
        "@type": "Organization",
        "name": "背徳エロス編集部",
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
      }
    };

    return (
      <>
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(featureSchema) }} />

        <div className="space-y-6 max-w-5xl mx-auto pb-16" lang="ja">
          {/* 特集用パンくずナビ */}
          <nav aria-label="パンくずリスト" className="flex items-center gap-1.5 text-xs font-medium text-slate-500">
            <Link href="/" className="hover:text-purple-600 transition-colors">ホーム</Link>
            <span className="text-slate-300">›</span>
            <Link href="/features" className="hover:text-purple-600 transition-colors">特集一覧</Link>
            <span className="text-slate-300">›</span>
            <Link href="/manga" className="hover:text-purple-600 transition-colors">漫画コーナー</Link>
            <span className="text-slate-300">›</span>
            <span className="text-slate-700 font-bold line-clamp-1 max-w-[240px]">{post.title}</span>
          </nav>

          {/* 特集コンテンツ本体（独自の背景・文字色完全分離） */}
          <div className="bg-slate-950 text-slate-100 rounded-3xl p-4 sm:p-8 md:p-10 shadow-2xl border border-slate-800">
            <div dangerouslySetInnerHTML={{ __html: articleContent }} />
          </div>

          {/* 特集記事下部：FANZA見放題ch 特設キラー誘導ボックス */}
          <UnlimitedPromotionBox />

          {/* 🏷️ 【成約率爆上げ】FANZA公式セール＆100円〜ワンコイン動画特設ボックス */}
          <section className="rounded-3xl bg-gradient-to-br from-amber-950/40 via-slate-900 to-slate-950 border-2 border-amber-500/40 p-6 md:p-8 text-white shadow-xl space-y-4">
            <div className="flex flex-wrap items-center justify-between gap-2">
              <div className="flex items-center gap-2">
                <span className="text-[10px] font-black text-amber-950 bg-amber-400 px-3 py-1 rounded-full uppercase tracking-wider shadow">
                  🔥 期間限定・大感謝祭
                </span>
                <span className="text-[10px] font-bold text-amber-300 bg-amber-500/10 border border-amber-500/30 px-2.5 py-0.5 rounded-full">
                  100円〜 / 最大70%OFF
                </span>
              </div>
              <span className="text-[11px] text-slate-400">※FANZA公式にて毎日更新中</span>
            </div>

            <div className="space-y-1">
              <h3 className="text-base md:text-xl font-black text-white leading-snug">
                「単品購入より安く楽しみたい」という方必見！<br className="hidden sm:inline" />
                <span className="text-amber-400">100円〜ワンコイン＆最大70%OFFセール開催中</span>
              </h3>
              <p className="text-xs md:text-sm text-slate-300 leading-relaxed">
                FANZAでは人気単体女優の過去作や話題作が100円〜500円で手に入る激安セールを随時実施中。登録不要で今すぐ観られる公式無料動画コーナーも大充実！
              </p>
            </div>

            <div className="pt-2 flex flex-col sm:flex-row gap-3">
              <a
                href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fsale%2F&af_id=onchan555-003"
                target="_blank"
                rel="noopener noreferrer"
                className="flex-1 inline-flex items-center justify-center text-xs md:text-sm font-black text-slate-950 bg-gradient-to-r from-amber-400 via-amber-300 to-yellow-400 hover:from-amber-300 hover:to-yellow-300 px-6 py-3.5 rounded-xl shadow-lg shadow-amber-500/20 transition duration-200 text-center transform hover:-translate-y-0.5"
              >
                🏷️ 今すぐFANZA公式セール会場をチェック（100円〜） ›
              </a>
              <a
                href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Ffree%2F&af_id=onchan555-003"
                target="_blank"
                rel="noopener noreferrer"
                className="sm:w-auto inline-flex items-center justify-center text-xs md:text-sm font-bold text-slate-200 hover:text-white bg-white/10 hover:bg-white/20 border border-white/20 px-5 py-3.5 rounded-xl transition text-center"
              >
                🎁 公式無料動画コーナーを見る（完全無料）
              </a>
            </div>

            <div className="pt-2 flex flex-wrap items-center justify-center gap-4 text-[11px] text-slate-400 border-t border-slate-800">
              <span className="flex items-center gap-1 font-bold text-slate-300">🔒 クレカ明細はDMM表記（作品名なし）</span>
              <span className="flex items-center gap-1">💳 PayPay・楽天ペイ・クレカ対応</span>
              <span className="flex items-center gap-1">📱 専用アプリ不要・ブラウザ即再生</span>
            </div>
          </section>

          {/* 漫画コーナートップへの回遊導線 */}
          <div className="text-center pt-4 space-y-3">
            <Link
              href="/manga"
              className="inline-flex items-center gap-2 px-8 py-3.5 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white font-bold text-sm rounded-xl shadow-lg transition transform hover:-translate-y-0.5"
            >
              <span>📚</span><span>FANZA漫画コーナー（全3,600作品以上）をもっと見る</span>
            </Link>
          </div>
        </div>
      </>
    );
  }

  // ==========================================
  // 🎬 通常のAV作品レビュー詳細レンダリング
  // ==========================================
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

  // 作品固有の魅力的で熱狂的な動的CTA文言生成
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

          {/* アートジャケット画像 / 10選コラージュ画像 */}
          <section className="flex justify-center bg-slate-900 rounded-2xl p-4 border border-slate-800 overflow-hidden" aria-label="作品ジャケット">
            {post.featured_images && post.featured_images.length >= 4 ? (
              <div className="w-full max-w-2xl rounded-2xl overflow-hidden shadow-2xl">
                <TenSelectionCollage
                  images={post.featured_images}
                  fallbackImage={post.image}
                  title={post.title}
                  actressName={mainActress || "人気女優"}
                />
              </div>
            ) : (
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
            )}
          </section>

          {/* セール・価格・配信形態ボックス */}
          <section className="bg-gradient-to-r from-slate-900 to-slate-950 text-white p-5 md:p-6 rounded-2xl border border-slate-800 space-y-4">
            <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 border-b border-slate-800/80 pb-4">
              <div className="space-y-1 text-left">
                <div className="flex items-center gap-2">
                  <span className="text-[10px] font-black text-amber-400 uppercase tracking-widest bg-amber-400/10 px-2.5 py-0.5 rounded border border-amber-400/20">
                    OFFICIAL STREAMING & DOWNLOAD
                  </span>
                  <span className="text-[10px] text-emerald-400 font-bold bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20">
                    🔒 クレカ明細はDMM表記のみ
                  </span>
                </div>
                <h2 className="text-sm md:text-base font-black text-white">
                  FANZA公式で <span className="text-amber-400 text-lg">ストリーミング＆ダウンロード</span> 配信中！
                </h2>
                <p className="text-xs text-slate-400">
                  専用アプリ不要！スマホ・PCのブラウザから今すぐ高画質HD/4Kで視聴できます。
                </p>
              </div>
              <div className="text-[11px] text-slate-400 flex flex-wrap sm:flex-col gap-1.5 flex-shrink-0">
                <span className="flex items-center gap-1 text-slate-300">💳 PayPay・楽天ペイ・クレカOK</span>
                <span className="flex items-center gap-1 text-emerald-400">🛡️ 作品名は一切出ず家族バレゼロ</span>
              </div>
            </div>

            <div className="flex flex-col sm:flex-row gap-3">
              <a
                href={post.affiliate_url}
                target="_blank"
                rel="noopener noreferrer"
                className="flex-1 text-center px-6 py-3.5 bg-gradient-to-r from-rose-600 via-rose-500 to-pink-600 hover:from-rose-500 hover:to-pink-500 text-white text-xs md:text-sm font-black rounded-xl shadow-lg shadow-rose-600/30 transition flex items-center justify-center gap-2"
              >
                <span>🔥</span>
                <span>この作品の無料プレビュー・本編を見る（FANZA公式）</span>
                <span className="text-xs opacity-80">›</span>
              </a>
              <a
                href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fmonthly%2Fpremium%2F&af_id=onchan555-003"
                target="_blank"
                rel="noopener noreferrer"
                className="sm:w-auto text-center px-5 py-3.5 bg-slate-800 hover:bg-slate-700 border border-amber-400/40 hover:border-amber-400 text-amber-300 hover:text-amber-200 text-xs md:text-sm font-bold rounded-xl shadow transition flex items-center justify-center gap-1.5"
                title="単品買いより圧倒的にお得な月額見放題"
              >
                <span>👑</span>
                <span>単品よりお得！15万本見放題ch</span>
              </a>
            </div>
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

          {/* メタ情報・タグ探索ボックス */}
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
                <span className="text-slate-400 font-bold uppercase tracking-wider block text-[9px]">公式配信状況</span>
                <span className="text-rose-600 font-black text-sm block">
                  公式配信中（セール随時実施）
                </span>
              </div>
            </div>

            {/* 出演女優タグ */}
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

            {/* 作品属性タグ */}
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

          {/* レビューテキスト */}
          <section className="prose prose-slate max-w-none text-slate-700 space-y-6 leading-relaxed text-sm md:text-base font-medium" aria-label="詳細考察レビュー">
            <div
              className="review-content-html"
              dangerouslySetInnerHTML={{ __html: post.review || (post as any).content || "" }}
            />
          </section>

          {/* 🔰 特集ピックアップ：動画だけでなくFANZA電子書籍・漫画も楽しみたい方へ */}
          <section className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-indigo-950 via-slate-900 to-purple-950 border-2 border-indigo-500/40 p-6 md:p-8 text-white shadow-xl space-y-4">
            <div className="flex flex-wrap items-center gap-2">
              <span className="text-[10px] font-black text-indigo-300 bg-indigo-500/20 border border-indigo-500/40 px-2.5 py-0.5 rounded-full uppercase tracking-wider">
                📚 FANZAおすすめ特集
              </span>
              <span className="text-[10px] font-bold text-emerald-400 bg-emerald-400/10 border border-emerald-400/20 px-2 py-0.5 rounded-full">
                安心・購入ガイド
              </span>
            </div>

            <div className="space-y-2">
              <h3 className="text-lg md:text-xl font-black text-white leading-snug">
                【あわせて読みたい】動画と並んで人気のFANZA同人・電子コミックをこっそり楽しむ方法
              </h3>
              <p className="text-xs md:text-sm text-slate-300 leading-relaxed">
                映像作品をチェックした後は、よりディープなシチュエーションを描いたFANZA同人・エロ漫画もおすすめ。スマホやPCからブラウザで即読破可能で、クレジットカードの請求も作品名は出ず安心です。
              </p>
            </div>

            <div className="pt-2 flex flex-col sm:flex-row items-center gap-3">
              <Link
                href="/posts/feature_why_buy_fanza_manga_complete_guide"
                className="w-full sm:w-auto inline-flex items-center justify-center text-xs md:text-sm font-black text-white bg-gradient-to-r from-indigo-600 via-purple-600 to-rose-600 hover:opacity-95 px-6 py-3.5 rounded-xl shadow-lg transition duration-150 transform hover:-translate-y-0.5 text-center"
              >
                📖 初心者向けFANZA漫画購入ガイド＆名作特集を見る ›
              </Link>
              <span className="text-[11px] text-slate-400">
                ※無料立ち読み多数 / PayPay・楽天ペイ・クレカ対応
              </span>
            </div>
          </section>

          {/* 個別作品クリック誘導ボタン（レビュー直後・CVR最大化） */}
          <section className="py-5 text-center space-y-4 bg-gradient-to-r from-rose-50 via-pink-50 to-rose-50 border border-rose-200/80 rounded-3xl p-6 shadow-sm">
            <div className="space-y-1">
              <span className="text-[10px] font-black text-rose-600 bg-rose-100/90 px-3 py-1 rounded-full uppercase tracking-wider">
                OFFICIAL STREAMING & DOWNLOAD
              </span>
              <h3 className="text-base md:text-lg font-black text-slate-900 pt-1">
                この作品の本編・無料プレビューを今すぐ楽しむ
              </h3>
              <p className="text-xs text-slate-600">
                専用アプリ不要！ブラウザから今すぐHD高画質で即再生できます。
              </p>
            </div>

            <div className="flex flex-col sm:flex-row items-center justify-center gap-3 pt-1">
              <a
                href={post.affiliate_url}
                target="_blank"
                rel="noopener noreferrer"
                className="w-full sm:w-auto px-8 py-4 text-sm md:text-base font-black text-white bg-gradient-to-r from-rose-600 via-rose-500 to-pink-600 hover:from-rose-500 hover:to-pink-500 rounded-xl shadow-lg shadow-rose-600/30 transition duration-200 transform hover:-translate-y-0.5"
              >
                {dynamicCtaText}
              </a>
              <a
                href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fmonthly%2Fpremium%2F&af_id=onchan555-003"
                target="_blank"
                rel="noopener noreferrer"
                className="w-full sm:w-auto px-6 py-4 text-xs md:text-sm font-black text-amber-900 bg-amber-400 hover:bg-amber-300 rounded-xl shadow-md transition duration-200 text-center"
              >
                👑 15万本見放題の「FANZA見放題ch」で見る
              </a>
            </div>

            <div className="pt-2 flex flex-wrap items-center justify-center gap-4 text-[11px] text-slate-500 border-t border-rose-200/50">
              <span className="flex items-center gap-1 font-bold text-slate-700">🔒 クレカ明細はDMM表記（作品名なし）</span>
              <span className="flex items-center gap-1">💳 PayPay・楽天ペイ・コンビニ決済対応</span>
              <span className="flex items-center gap-1">📱 スマホ・PCで今すぐ即再生OK</span>
            </div>
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

          {/* 類似作品レコメンド */}
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

          {/* 女優レコメンド */}
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

          {/* 関連ジャンル一覧 */}
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

          {/* 🏷️ 【成約率爆上げ】FANZA公式セール＆100円〜ワンコイン動画特設ボックス */}
          <section className="rounded-3xl bg-gradient-to-br from-amber-950/40 via-slate-900 to-slate-950 border-2 border-amber-500/40 p-6 md:p-8 text-white shadow-xl space-y-4">
            <div className="flex flex-wrap items-center justify-between gap-2">
              <div className="flex items-center gap-2">
                <span className="text-[10px] font-black text-amber-950 bg-amber-400 px-3 py-1 rounded-full uppercase tracking-wider shadow">
                  🔥 期間限定・大感謝祭
                </span>
                <span className="text-[10px] font-bold text-amber-300 bg-amber-500/10 border border-amber-500/30 px-2.5 py-0.5 rounded-full">
                  100円〜 / 最大70%OFF
                </span>
              </div>
              <span className="text-[11px] text-slate-400">※FANZA公式にて毎日更新中</span>
            </div>

            <div className="space-y-1">
              <h3 className="text-base md:text-xl font-black text-white leading-snug">
                「単品2,000円〜はちょっと高い…」という方必見！<br className="hidden sm:inline" />
                <span className="text-amber-400">100円〜ワンコイン＆最大70%OFFセール開催中</span>
              </h3>
              <p className="text-xs md:text-sm text-slate-300 leading-relaxed">
                FANZAでは人気単体女優の過去作や話題作が100円〜500円で手に入る激安セールを随時実施中。さらに登録不要で即再生できる公式無料動画コーナーも大充実！
              </p>
            </div>

            <div className="pt-2 flex flex-col sm:flex-row gap-3">
              <a
                href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fsale%2F&af_id=onchan555-003"
                target="_blank"
                rel="noopener noreferrer"
                className="flex-1 inline-flex items-center justify-center text-xs md:text-sm font-black text-slate-950 bg-gradient-to-r from-amber-400 via-amber-300 to-yellow-400 hover:from-amber-300 hover:to-yellow-300 px-6 py-3.5 rounded-xl shadow-lg shadow-amber-500/20 transition duration-200 text-center transform hover:-translate-y-0.5"
              >
                🏷️ 今すぐFANZA公式セール会場をチェック（100円〜） ›
              </a>
              <a
                href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Ffree%2F&af_id=onchan555-003"
                target="_blank"
                rel="noopener noreferrer"
                className="sm:w-auto inline-flex items-center justify-center text-xs md:text-sm font-bold text-slate-200 hover:text-white bg-white/10 hover:bg-white/20 border border-white/20 px-5 py-3.5 rounded-xl transition text-center"
              >
                🎁 公式無料動画コーナーを見る（完全無料）
              </a>
            </div>
          </section>

          {/* 極上のプレミアムCTAボタン（最下部） */}
          <section className="pt-6 border-t border-slate-100 text-center space-y-4" aria-label="視聴誘導">
            <div className="space-y-1">
              <span className="text-[10px] font-black text-rose-600 bg-rose-50 border border-rose-200 px-3 py-1 rounded-full uppercase tracking-wider">
                OFFICIAL HD/4K STREAMING
              </span>
              <h3 className="text-base md:text-xl font-black text-slate-900 pt-1">
                『{post.title}』をFANZA公式で今すぐ視聴する
              </h3>
            </div>

            <div className="flex flex-col sm:flex-row items-center justify-center gap-3">
              <a
                href={post.affiliate_url}
                target="_blank"
                rel="noopener noreferrer"
                className="w-full sm:w-auto px-8 py-4.5 text-base font-extrabold text-white bg-gradient-to-r from-rose-600 via-rose-500 to-pink-600 hover:from-rose-500 hover:to-pink-500 rounded-2xl shadow-xl shadow-rose-600/30 transition duration-200 cursor-pointer transform hover:-translate-y-0.5"
              >
                {dynamicCtaText}
              </a>
            </div>

            <div className="flex flex-wrap items-center justify-center gap-4 text-[11px] text-slate-500">
              <span className="flex items-center gap-1 font-bold text-slate-700">🔒 クレカ明細はDMM表記（作品名なし）</span>
              <span className="flex items-center gap-1">💳 PayPay・楽天ペイ・クレカ対応</span>
              <span className="flex items-center gap-1">📱 アプリ不要・スマホで今すぐ再生</span>
            </div>
            <p className="text-[10px] text-slate-400">
              ※クリックするとFANZA（公式18禁ストア）へ直接遷移します。安全・高画質でお楽しみいただけます。
            </p>
          </section>
        </div>

        {/* 画面下部追従フロートCTA（モバイル＆デスクトップの離脱防止・CVR最大化） */}
        <FloatingCta
          affiliateUrl={post.affiliate_url}
          title={post.title}
          actressName={mainActress || undefined}
          hinbanText={hinbanText}
        />
      </article>
    </>
  );
}
