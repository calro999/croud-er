import Link from "next/link";
import { notFound } from "next/navigation";
import { Metadata } from "next";
import { censorText } from "@/lib/censor";
import { getActressSlug, getActressNameBySlug, getGenreSlug } from "@/lib/slugs";
import UnlimitedPromotionBox from "@/app/components/UnlimitedPromotionBox";
import { getAllSummaryPosts, PostSummary } from "@/lib/posts";
import { getActressWikiData, getSimilarActresses } from "@/lib/actress";

type Post = PostSummary;

export const dynamicParams = false;

export async function generateStaticParams() {
  const posts = getAllSummaryPosts();
  const actressSet = new Set<string>();
  for (const post of posts) {
    (post.actresses || []).forEach(a => actressSet.add(a));
  }
  return Array.from(actressSet).map(name => ({ name: getActressSlug(name) }));
}

function getAllPosts(): Post[] {
  return getAllSummaryPosts();
}

export async function generateMetadata({ params }: { params: Promise<{ name: string }> }): Promise<Metadata> {
  const { name } = await params;
  const actressName = getActressNameBySlug(name);
  const wiki = getActressWikiData(actressName);
  
  const cupText = wiki?.cup ? `${wiki.cup}カップ` : "";
  const titleText = `【完全版Wiki】「${actressName}」プロフィール・神作おすすめ10選・監督別全出演作まとめ`;
  const descriptionText = `${actressName}（${wiki?.ruby || actressName}）の公式プロフィール${cupText ? '（' + cupText + '）' : ''}、出演作品の監督名、おすすめ神作10選、全出演作タイトル一覧を完全網羅！お得にFANZAで視聴する方法を徹底解説。`;

  const allPosts = getAllPosts();
  const actressPosts = allPosts
    .filter(p => (p.actresses || []).includes(actressName))
    .sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
  const ogImage = wiki?.image_large || (actressPosts.length > 0 && actressPosts[0].image ? actressPosts[0].image : undefined);

  return {
    title: titleText,
    description: descriptionText,
    keywords: [
      `${actressName} Wiki`,
      `${actressName} プロフィール`,
      `${actressName} 監督`,
      `${actressName} レビュー`,
      `${actressName} 出演作品`,
      `${actressName} FANZA`,
      `${actressName} おすすめ`,
      "AV女優 プロフィール"
    ].join(","),
    alternates: { canonical: `https://haitoku.pages.dev/actress/${name}` },
    openGraph: {
      title: censorText(titleText),
      description: censorText(descriptionText),
      url: `https://haitoku.pages.dev/actress/${name}`,
      type: "profile",
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

  // FANZA APIから取得したWikipedia級の公式データ
  const wiki = getActressWikiData(actressName);
  const similarActresses = getSimilarActresses(actressName, 4);

  const relatedGenres = Array.from(new Set(actressPosts.flatMap(p => p.genres || []))).slice(0, 10);
  const coActresses = Array.from(
    new Set(actressPosts.flatMap(p => (p.actresses || []).filter(a => a !== actressName)))
  ).slice(0, 6);

  // 構造化データ（Person / Breadcrumb / FAQ）
  const personSchema = {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": actressName,
    "alternateName": wiki?.ruby || undefined,
    "description": `${actressName}のアダルト映像作品プロフィール・出演作・監督一覧まとめ`,
    "image": wiki?.image_large || undefined,
    "jobTitle": "AV女優",
    "height": wiki?.height ? `${wiki.height}cm` : undefined,
    "birthDate": wiki?.birthday || undefined,
    "url": `https://haitoku.pages.dev/actress/${name}`
  };

  const breadcrumbSchema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "ホーム", "item": "https://haitoku.pages.dev" },
      { "@type": "ListItem", "position": 2, "name": `${actressName} Wikiプロフィール・出演作`, "item": `https://haitoku.pages.dev/actress/${name}` }
    ]
  };

  const faqSchema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": `${actressName}のプロフィール（スリーサイズ・カップ）は？`,
        "acceptedAnswer": {
          "@type": "Answer",
          "text": `${actressName}のプロフィールは、バスト: ${wiki?.bust || '非公開'}cm（${wiki?.cup || ''}カップ）、ウエスト: ${wiki?.waist || '非公開'}cm、ヒップ: ${wiki?.hip || '非公開'}cm、身長: ${wiki?.height || '非公開'}cmです。`
        }
      },
      {
        "@type": "Question",
        "name": `${actressName}の作品はどこで見られますか？お得に視聴する方法は？`,
        "acceptedAnswer": {
          "@type": "Answer",
          "text": `${actressName}の公式作品はFANZA（DMM）にて独占配信されています。ストリーミングレンタル（300円〜）や高画質HD/4Kダウンロード、見放題chなどでいつでもお得に視聴可能です。`
        }
      },
      {
        "@type": "Question",
        "name": `${actressName}の主な担当監督は誰ですか？`,
        "acceptedAnswer": {
          "@type": "Answer",
          "text": `${actressName}が出演する人気作品の主な監督は「${wiki?.directors?.slice(0, 5).join('、 ') || '実力派監督陣'}」などです。`
        }
      }
    ]
  };

  const fanzaActressSearchUrl = `https://al.fanza.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fsearch%2F-%2F%3Fsearchstr%3D${encodeURIComponent(actressName)}%2F&af_id=onchan555-003`;

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(personSchema) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema) }} />

      <div className="space-y-10 max-w-5xl mx-auto" lang="ja">
        {/* パンくずリスト */}
        <nav className="flex items-center gap-1.5 text-xs font-medium text-slate-500" aria-label="パンくずリスト">
          <Link href="/" className="hover:text-rose-600 transition-colors">ホーム</Link>
          <span className="text-slate-300">›</span>
          <span className="text-slate-700 font-bold">{actressName}（Wikipedia風まとめ）</span>
        </nav>

        {/* 📚 Wikipedia風 公式インフォボックス ＆ ヘッダー */}
        <section className="rounded-3xl bg-white border border-slate-200/90 p-6 md:p-8 shadow-sm">
          <div className="flex flex-col lg:flex-row gap-8 items-start justify-between">
            {/* 左側：解説テキスト */}
            <div className="space-y-4 flex-1">
              <div className="flex flex-wrap items-center gap-2">
                <span className="inline-flex text-[9px] font-black tracking-widest text-rose-600 bg-rose-50 border border-rose-200 px-3 py-1 rounded-full uppercase">
                  ACTRESS WIKI & DATABASE
                </span>
                {wiki?.cup && (
                  <span className="inline-flex text-[9px] font-black tracking-wider text-amber-700 bg-amber-50 border border-amber-200 px-2.5 py-0.5 rounded-full">
                    {wiki.cup} CUP
                  </span>
                )}
              </div>

              <div>
                <h1 className="text-3xl md:text-4xl font-black text-slate-900 tracking-tight flex items-baseline gap-3">
                  {actressName}
                  {wiki?.ruby && <span className="text-sm font-bold text-slate-400">（{wiki.ruby}）</span>}
                </h1>
              </div>

              <p className="text-slate-600 text-sm leading-relaxed">
                <strong>{actressName}</strong>（{wiki?.ruby || actressName}）の公式プロフィール、出演作品、担当監督名、おすすめ神作を完全網羅したWikipedia風データベースです。当サイトでは現在<strong className="text-rose-600 font-bold">{actressPosts.length}作品</strong>の徹底レビューを掲載しています。
              </p>

              {/* 監督タグ */}
              {wiki?.directors && wiki.directors.length > 0 && (
                <div className="space-y-1.5 pt-2">
                  <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider block">
                    🎬 主な出演作の監督
                  </span>
                  <div className="flex flex-wrap gap-1.5">
                    {wiki.directors.map(dir => (
                      <span key={dir} className="text-xs font-bold text-indigo-700 bg-indigo-50 border border-indigo-100 px-2.5 py-1 rounded-lg">
                        {dir} 監督
                      </span>
                    ))}
                  </div>
                </div>
              )}

              {/* クイックアクション */}
              <div className="pt-3 flex flex-wrap gap-3">
                <a href={fanzaActressSearchUrl} target="_blank" rel="noopener noreferrer"
                  className="text-xs font-black text-white bg-gradient-to-r from-rose-500 to-pink-600 hover:from-rose-400 hover:to-pink-500 px-5 py-3 rounded-xl shadow-md transition inline-flex items-center gap-1.5">
                  <span>🔥</span> FANZA公式で全作品を見る（{wiki?.works_count || actressPosts.length}件）
                </a>
              </div>
            </div>

            {/* 右側：Wikipedia風 プロフィール表 (Infobox) */}
            <div className="w-full lg:w-80 bg-slate-50 border border-slate-200 rounded-2xl overflow-hidden shadow-inner flex-shrink-0">
              <div className="bg-slate-800 text-white text-center py-2 text-xs font-black tracking-wider">
                公式プロフィール（FANZA情報）
              </div>

              {/* 女優公式写真 */}
              <div className="p-4 bg-white flex justify-center border-b border-slate-200">
                {wiki?.image_large ? (
                  <img
                    src={wiki.image_large}
                    alt={`${actressName} 公式プロフィール写真`}
                    className="w-48 h-auto object-cover rounded-xl shadow-md border border-slate-100"
                    loading="lazy"
                  />
                ) : actressPosts[0]?.image ? (
                  <img
                    src={actressPosts[0].image}
                    alt={`${actressName} 出演作ジャケット`}
                    className="w-48 h-auto object-cover rounded-xl shadow-md border border-slate-100"
                    loading="lazy"
                  />
                ) : (
                  <div className="w-48 h-48 bg-slate-100 flex items-center justify-center text-slate-400 text-xs rounded-xl">No Image</div>
                )}
              </div>

              {/* スペックテーブル */}
              <table className="w-full text-xs text-left text-slate-700 divide-y divide-slate-200">
                <tbody>
                  <tr className="divide-x divide-slate-200">
                    <th className="py-2.5 px-3 bg-slate-100/70 font-bold text-slate-500 w-24">名前</th>
                    <td className="py-2.5 px-3 font-semibold">{actressName} {wiki?.ruby ? `(${wiki.ruby})` : ''}</td>
                  </tr>
                  <tr className="divide-x divide-slate-200">
                    <th className="py-2.5 px-3 bg-slate-100/70 font-bold text-slate-500">カップ</th>
                    <td className="py-2.5 px-3 font-black text-rose-600">{wiki?.cup ? `${wiki.cup}カップ` : '非公開'}</td>
                  </tr>
                  <tr className="divide-x divide-slate-200">
                    <th className="py-2.5 px-3 bg-slate-100/70 font-bold text-slate-500">サイズ</th>
                    <td className="py-2.5 px-3 font-semibold">
                      {wiki?.bust ? `B${wiki.bust} / W${wiki?.waist || '-'} / H${wiki?.hip || '-'}` : '非公開'}
                    </td>
                  </tr>
                  <tr className="divide-x divide-slate-200">
                    <th className="py-2.5 px-3 bg-slate-100/70 font-bold text-slate-500">身長</th>
                    <td className="py-2.5 px-3 font-semibold">{wiki?.height ? `${wiki.height} cm` : '非公開'}</td>
                  </tr>
                  <tr className="divide-x divide-slate-200">
                    <th className="py-2.5 px-3 bg-slate-100/70 font-bold text-slate-500">生年月日</th>
                    <td className="py-2.5 px-3 font-semibold">{wiki?.birthday || '非公開'}</td>
                  </tr>
                  <tr className="divide-x divide-slate-200">
                    <th className="py-2.5 px-3 bg-slate-100/70 font-bold text-slate-500">血液型</th>
                    <td className="py-2.5 px-3 font-semibold">{wiki?.blood_type ? `${wiki.blood_type}型` : '非公開'}</td>
                  </tr>
                  <tr className="divide-x divide-slate-200">
                    <th className="py-2.5 px-3 bg-slate-100/70 font-bold text-slate-500">出身地</th>
                    <td className="py-2.5 px-3 font-semibold">{wiki?.prefectures || '非公開'}</td>
                  </tr>
                  <tr className="divide-x divide-slate-200">
                    <th className="py-2.5 px-3 bg-slate-100/70 font-bold text-slate-500">趣味・特技</th>
                    <td className="py-2.5 px-3 font-semibold">{wiki?.hobby || '非公開'}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </section>

        {/* 🧭 【追加依頼4位＆6位】あなたならどれ？初心者向け探索 ＆ 目的別診断ナビ */}
        <section className="bg-gradient-to-r from-rose-500 via-pink-600 to-rose-600 text-white rounded-3xl p-6 md:p-8 shadow-lg space-y-4">
          <div className="space-y-1">
            <span className="text-[10px] font-black bg-white/20 px-3 py-1 rounded-full uppercase tracking-wider">
              WHAT TO WATCH • 迷ったらここから
            </span>
            <h2 className="text-xl md:text-2xl font-black">
              【目的別診断】あなたにピッタリの「{actressName}」作品はどれ？
            </h2>
            <p className="text-xs text-rose-100 leading-relaxed">
              「作品数が多すぎて何から見ればいいか分からない…」という方のために、好みのシチュエーション別に最適なエントリー作品をご案内します。
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-2">
            <div className="bg-white/10 backdrop-blur-md border border-white/20 p-4 rounded-2xl space-y-2">
              <span className="text-xs font-black text-amber-300 block">🏆 初心者・王道派</span>
              <h3 className="text-sm font-bold text-white">まずは人気No.1神作から</h3>
              <p className="text-[11px] text-rose-100 leading-relaxed">
                レビュー評価・売上ともに最高峰の殿堂入り作品。{actressName}の魅力を100%味わえます。
              </p>
              {actressPosts[0] && (
                <Link href={`/posts/${actressPosts[0].id}`} className="block text-center text-xs font-bold bg-white text-rose-600 py-2 rounded-xl hover:bg-rose-50 transition mt-2">
                  1位のレビューを見る
                </Link>
              )}
            </div>

            <div className="bg-white/10 backdrop-blur-md border border-white/20 p-4 rounded-2xl space-y-2">
              <span className="text-xs font-black text-pink-200 block">🔥 濃厚・背徳シチュ派</span>
              <h3 className="text-sm font-bold text-white">人妻・不倫・NTRで昂る</h3>
              <p className="text-[11px] text-rose-100 leading-relaxed">
                日常のタブーを破る生々しい演技と、恥じらいながら快楽に堕ちる表情に溺れたい方へ。
              </p>
              <a href={fanzaActressSearchUrl} target="_blank" rel="noopener noreferrer" className="block text-center text-xs font-bold bg-white text-rose-600 py-2 rounded-xl hover:bg-rose-50 transition mt-2">
                FANZAでシチュ検索
              </a>
            </div>

            <div className="bg-white/10 backdrop-blur-md border border-white/20 p-4 rounded-2xl space-y-2">
              <span className="text-xs font-black text-emerald-200 block">💰 コスパ・長編派</span>
              <h3 className="text-sm font-bold text-white">ベスト盤・8時間超えで堪能</h3>
              <p className="text-[11px] text-rose-100 leading-relaxed">
                複数の名シーンを一挙に楽しめ、1本で何日も抜ける大ボリュームの総集編。
              </p>
              <a href={fanzaActressSearchUrl} target="_blank" rel="noopener noreferrer" className="block text-center text-xs font-bold bg-white text-rose-600 py-2 rounded-xl hover:bg-rose-50 transition mt-2">
                お得なベスト盤を見る
              </a>
            </div>
          </div>
        </section>

        {/* 🏷️ 主な出演ジャンル一覧 */}
        {relatedGenres.length > 0 && (
          <section className="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-3">
            <h2 className="text-xs font-bold text-slate-500 uppercase tracking-widest">{actressName} の主な出演ジャンル（横展開）</h2>
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
              ファン必見！{actressName}の圧倒的なシチュエーション没入感、表情変化、プレイ内容（フェラ・体位・アングル・絶頂シーン）を徹底考察。監督名や価格情報も含めてハズレなしの最高傑作10選をご紹介します。
            </p>
          </div>

          <div className="space-y-8">
            {actressPosts.slice(0, 10).map((post, idx) => {
              const cleanReviewText = post.review ? post.review.replace(/<[^>]*>/g, "").replace(/\s+/g, " ") : "";
              const excerpt = cleanReviewText.slice(0, 140) + "...";
              const rankNum = idx + 1;
              
              return (
                <div key={post.id} className="relative bg-slate-950/90 border border-slate-800 rounded-3xl overflow-hidden shadow-xl transition duration-300 hover:border-slate-700 space-y-6">
                  {/* 順位バッジ */}
                  <div className={`absolute top-4 left-4 z-20 w-10 h-10 md:w-12 md:h-12 rounded-2xl flex items-center justify-center font-black text-base md:text-lg shadow-2xl backdrop-blur-md ${
                    rankNum === 1 ? 'bg-amber-400 text-slate-950' : rankNum === 2 ? 'bg-slate-200 text-slate-950' : rankNum === 3 ? 'bg-amber-600 text-white' : 'bg-slate-800/90 text-slate-300 border border-slate-700'
                  }`}>
                    #{rankNum}
                  </div>

                  {/* 👑 ヒーローパッケージ画像 */}
                  <div className="w-full aspect-[800/538] relative bg-slate-900 border-b border-slate-800 flex items-center justify-center p-2">
                    {post.image ? (
                      <img
                        src={post.image}
                        alt={`${post.title} パッケージジャケット`}
                        referrerPolicy="no-referrer"
                        className="w-full h-full object-contain rounded-xl shadow-2xl"
                        loading="lazy"
                      />
                    ) : (
                      <div className="w-full h-full flex items-center justify-center text-slate-500 text-sm">No Image</div>
                    )}
                  </div>

                  {/* 📝 タイトル・作品情報・見どころ解説セクション */}
                  <div className="px-5 md:px-8 pb-8 space-y-6">
                    <div className="space-y-3">
                      <div className="flex flex-wrap items-center gap-2 text-xs font-extrabold text-slate-400">
                        {post.hinban && (
                          <span className="text-rose-400 bg-rose-500/10 border border-rose-500/20 px-2.5 py-1 rounded-md font-black uppercase tracking-wider text-xs">
                            {post.hinban}
                          </span>
                        )}
                        <span>•</span>
                        <span className="text-slate-300">{post.maker}</span>
                        {post.directors && post.directors.length > 0 && (
                          <>
                            <span>•</span>
                            <span className="text-indigo-400 bg-indigo-500/10 border border-indigo-500/20 px-2 py-0.5 rounded text-[11px]">
                              監督: {post.directors[0]}
                            </span>
                          </>
                        )}
                      </div>
                      <h3 className="text-lg md:text-2xl font-black text-white leading-snug">
                        {post.title}
                      </h3>
                      <div className="text-xs md:text-sm text-slate-200 leading-relaxed font-medium bg-slate-900/90 p-4 md:p-5 rounded-2xl border border-slate-800 space-y-1.5 shadow-inner">
                        <strong className="text-amber-400 block text-sm font-bold flex items-center gap-1.5">
                          🔥 プレイの見どころ・推しポイント
                        </strong>
                        <p className="text-slate-300">{excerpt}</p>
                      </div>
                    </div>

                    {/* 🎥 サンプル動画 */}
                    {post.sample_movie_url && (
                      <div className="space-y-2">
                        <span className="text-xs font-extrabold text-amber-400 tracking-wider block flex items-center gap-1.5">
                          🎥 サンプル動画プレビュー
                        </span>
                        <div className="w-full aspect-video rounded-2xl overflow-hidden bg-black border border-slate-800 shadow-lg">
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

                    {/* 📷 サンプル画像プレビュー */}
                    {post.sample_images && post.sample_images.length > 0 && (
                      <div className="space-y-2">
                        <span className="text-xs font-extrabold text-slate-400 tracking-wider block flex items-center gap-1.5">
                          📷 現場カット（サンプル写真）
                        </span>
                        <div className="grid grid-cols-3 sm:grid-cols-6 gap-2">
                          {post.sample_images.slice(0, 6).map((img, i) => (
                            <a key={i} href={post.affiliate_url} target="_blank" rel="noopener noreferrer" className="block aspect-video relative overflow-hidden rounded-xl border border-slate-800 bg-slate-900 hover:border-amber-400 transition transform hover:scale-105">
                              <img
                                src={img}
                                alt={`${actressName} ${post.title} サンプル名場面ショット ${i + 1}`}
                                className="w-full h-full object-cover opacity-90 hover:opacity-100 transition"
                                loading="lazy"
                              />
                            </a>
                          ))}
                        </div>
                      </div>
                    )}

                    {/* タグ＆価格＆CTAボタン */}
                    <div className="space-y-4 pt-2 border-t border-slate-800/80">
                      <div className="flex flex-wrap items-center justify-between gap-2 pt-2">
                        <div className="flex flex-wrap gap-1.5">
                          {(post.genres || []).slice(0, 6).map(g => (
                            <span key={g} className="text-[10px] font-bold text-slate-400 bg-slate-900 border border-slate-800 px-2.5 py-1 rounded-lg">
                              #{g}
                            </span>
                          ))}
                        </div>
                        <div className="text-xs font-bold text-amber-400">
                          配信価格: <span className="text-sm font-black text-white">300円〜</span>（ストリーミング）
                        </div>
                      </div>
                      <div className="flex flex-col sm:flex-row gap-3 pt-2">
                        <Link href={`/posts/${post.id}`} className="flex-1 text-center text-xs md:text-sm font-bold text-slate-200 bg-slate-900 border border-slate-700 hover:bg-slate-800 py-3.5 rounded-xl transition">
                          詳細レビューを読む
                        </Link>
                        <a href={post.affiliate_url} target="_blank" rel="noopener noreferrer" className="flex-1 text-center text-xs md:text-sm font-bold text-white bg-gradient-to-r from-rose-500 via-rose-600 to-pink-600 hover:from-rose-400 hover:to-rose-500 py-3.5 rounded-xl shadow-lg transition">
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

        {/* 👯 【追加依頼2位】類似女優（「この女優が好きならこの人も」） */}
        {similarActresses.length > 0 && (
          <section className="bg-white border border-slate-200 rounded-3xl p-6 md:p-8 shadow-sm space-y-4">
            <div className="space-y-1">
              <span className="text-[10px] font-bold text-rose-600 bg-rose-50 border border-rose-100 px-2.5 py-0.5 rounded-full uppercase">
                RECOMMENDED ACTRESSES
              </span>
              <h2 className="text-lg md:text-xl font-black text-slate-900">
                『{actressName}』が好きならこの女優もおすすめ！
              </h2>
              <p className="text-xs text-slate-500">
                体型・ルックス・出演シチュエーションが近く、同じ系統の快感を味わえる注目女優を厳選。
              </p>
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-2">
              {similarActresses.map(sim => (
                <Link
                  key={sim.name}
                  href={`/actress/${getActressSlug(sim.name)}`}
                  className="group block bg-slate-50 border border-slate-200/90 rounded-2xl overflow-hidden hover:border-rose-300 hover:shadow-md transition duration-200"
                >
                  <div className="aspect-[4/5] bg-slate-200 relative overflow-hidden">
                    {sim.image ? (
                      <img src={sim.image} alt={`${sim.name} 写真`} className="w-full h-full object-cover group-hover:scale-105 transition duration-300" loading="lazy" />
                    ) : (
                      <div className="w-full h-full flex items-center justify-center text-slate-400 text-xs font-bold">{sim.name}</div>
                    )}
                    {sim.cup && (
                      <span className="absolute top-2 left-2 text-[9px] font-black bg-rose-600 text-white px-2 py-0.5 rounded-md shadow">
                        {sim.cup}カップ
                      </span>
                    )}
                  </div>
                  <div className="p-3 space-y-1">
                    <h3 className="text-xs font-bold text-slate-800 group-hover:text-rose-600 truncate">{sim.name}</h3>
                    <p className="text-[10px] text-slate-500 line-clamp-1">{sim.reason}</p>
                  </div>
                </Link>
              ))}
            </div>
          </section>
        )}

        {/* 📜 【追加依頼：Wikipedia化】出演作品・監督名完全一覧テーブル */}
        {wiki?.works && wiki.works.length > 0 && (
          <section className="bg-white border border-slate-200 rounded-3xl p-6 md:p-8 shadow-sm space-y-4">
            <div className="space-y-1">
              <span className="text-[10px] font-bold text-slate-400 uppercase tracking-widest">
                COMPLETE FILMOGRAPHY
              </span>
              <h2 className="text-lg md:text-xl font-black text-slate-900">
                『{actressName}』全出演作品・監督名一覧（{wiki.works.length}タイトル）
              </h2>
              <p className="text-xs text-slate-500">
                FANZAで配信されている{actressName}の出演タイトル・発売日・担当監督・制作メーカーの完全リストです。
              </p>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs border border-slate-200 rounded-xl overflow-hidden divide-y divide-slate-200">
                <thead className="bg-slate-100 text-slate-700 font-bold">
                  <tr>
                    <th className="py-3 px-4">タイトル</th>
                    <th className="py-3 px-3 w-28">監督</th>
                    <th className="py-3 px-3 w-28">メーカー</th>
                    <th className="py-3 px-3 w-24">配信価格</th>
                    <th className="py-3 px-3 w-24 text-center">リンク</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100 text-slate-600">
                  {wiki.works.map((w, idx) => (
                    <tr key={idx} className="hover:bg-slate-50 transition">
                      <td className="py-3 px-4 font-semibold text-slate-800">
                        <span className="text-[10px] text-rose-500 font-mono block mb-0.5">{w.id.toUpperCase()}</span>
                        {w.title}
                      </td>
                      <td className="py-3 px-3 font-medium text-slate-700">
                        {w.directors && w.directors.length > 0 ? w.directors.join('、 ') : '-'}
                      </td>
                      <td className="py-3 px-3 font-medium text-slate-700">{w.maker || '-'}</td>
                      <td className="py-3 px-3 font-bold text-rose-600">{w.price || '300~'}円</td>
                      <td className="py-3 px-3 text-center">
                        <a href={w.affiliate_url} target="_blank" rel="noopener noreferrer"
                          className="inline-block text-[10px] font-bold text-rose-600 bg-rose-50 hover:bg-rose-100 border border-rose-200 px-2.5 py-1 rounded-md transition">
                          公式で見る
                        </a>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        )}

        {/* 当サイト掲載全レビュー一覧 */}
        <section className="space-y-4">
          <h2 className="text-lg font-extrabold text-slate-800">{actressName} の当サイト徹底レビュー一覧（{actressPosts.length}件）</h2>
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

        {/* よくある質問 (FAQ) */}
        <section className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm space-y-4">
          <h2 className="text-sm font-extrabold text-slate-800">{actressName} に関するよくある質問</h2>
          <div className="space-y-4 divide-y divide-slate-100">
            <div className="pt-4 first:pt-0 space-y-1.5">
              <p className="text-sm font-bold text-slate-700">Q. {actressName}のプロフィール（カップ・体型）は？</p>
              <p className="text-xs text-slate-500 leading-relaxed">
                A. {actressName}のバストは{wiki?.bust ? `${wiki.bust}cm（${wiki?.cup || ''}カップ）` : '公式非公開'}、ウエスト{wiki?.waist || '-'}cm、ヒップ{wiki?.hip || '-'}cmです。
              </p>
            </div>
            <div className="pt-4 space-y-1.5">
              <p className="text-sm font-bold text-slate-700">Q. {actressName}の作品を最も安く見る方法は？</p>
              <p className="text-xs text-slate-500 leading-relaxed">
                A. FANZAのストリーミングレンタルなら1本300円〜で視聴可能です。また、定期的に開催される割引セールやFANZA見放題chを活用するとさらにお得に楽しめます。
              </p>
            </div>
          </div>
        </section>

        {/* FANZA見放題ch 特設キラー誘導ボックス */}
        <UnlimitedPromotionBox />

        {/* フッターCTA */}
        <section className="text-center py-6">
          <a href={fanzaActressSearchUrl}
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
