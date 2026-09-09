import Link from "next/link";
import { Metadata } from "next";
import { getActressSlug } from "@/lib/slugs";
import { getAllSummaryPosts, PostSummary } from "@/lib/posts";
import FeaturesClient from "./FeaturesClient";

export const metadata: Metadata = {
  title: "【2026年最新】人気AV女優のおすすめ神作10選・キラー特集一覧 | 背徳の深夜書斎",
  description: "瀬戸環奈、松本いちか、由良かな、石川澪、逢沢みゆ、篠田ゆう、松永あかりなど、トップAV女優の『絶対に抜ける神作おすすめ10選』およびシチュエーション別ディープ特集を網羅した完全一覧！",
  keywords: "AV女優 特集, 神作 10選, 瀬戸環奈, 松本いちか, 由良かな, 石川澪, 逢沢みゆ, 篠田ゆう, 松永あかり, AV おすすめ",
  alternates: { canonical: "https://haitoku.pages.dev/features" },
};

// 厳選特集対象の女優リスト
const FEATURED_ACTRESSES = [
  { name: "瀬戸環奈", ruby: "セトカン", tag: "王道美少女・SNS超話題" },
  { name: "松本いちか", ruby: "まつもといちか", tag: "小悪魔感度・神ボディ" },
  { name: "由良かな", ruby: "ゆらかな", tag: "圧倒的透明感・美少女" },
  { name: "石川澪", ruby: "いしかわみお", tag: "可憐ルックス・超絶人気" },
  { name: "逢沢みゆ", ruby: "あいざわみゆ", tag: "美肌巨乳・絶頂プレイ" },
  { name: "篠田ゆう", ruby: "しのだゆう", tag: "極上スタイル・レジェンド" },
  { name: "松永あかり", ruby: "まつながあかり", tag: "妖艶色気・熟れた肉体美" },
  { name: "石原希望", ruby: "いしはらのぞみ", tag: "爆発的感度・笑顔の天使" },
  { name: "河北彩花（河北彩伽）", ruby: "かわきたさいか", tag: "国民的トップ女優・美の頂点" },
  { name: "美園和花", ruby: "みそのわか", tag: "超絶美巨乳・甘美フェイス" },
  { name: "木下ひまり（花沢ひまり）", ruby: "きのしたひまり", tag: "圧倒的美貌・スラリ美脚" },
  { name: "弥生みづき", ruby: "やよいみづき", tag: "極上人妻フェロモン" },
];

export default function FeaturesPage() {
  const posts = getAllSummaryPosts();

  // 1. 神作10選の個別記事（160件すべて）
  const tenSelectionPosts = posts.filter(
    (p) =>
      p.title.includes("10選") ||
      (p.genres || []).some((g) => g.includes("10選"))
  ).sort((a, b) => new Date(b.date || 0).getTime() - new Date(a.date || 0).getTime());

  // 2. その他のシチュエーション・ディープ特集記事（845件）
  const deepFeaturePosts = posts.filter(
    (p) =>
      (p.id.startsWith("feature_") || p.id.startsWith("custom_feature_")) &&
      !tenSelectionPosts.some((tp) => tp.id === p.id)
  ).sort((a, b) => new Date(b.date || 0).getTime() - new Date(a.date || 0).getTime());

  // 3. 女優Wiki・10選リスト
  const featuredActresses = FEATURED_ACTRESSES.map((actressObj) => {
    const name = actressObj.name;
    const slug = getActressSlug(name);
    const actressPosts = posts.filter((p) => (p.actresses || []).includes(name));
    const coverImage = actressPosts.length > 0 ? actressPosts[0].image : "";
    return {
      ...actressObj,
      slug,
      count: actressPosts.length,
      coverImage,
    };
  });

  return (
    <div className="space-y-8 max-w-6xl mx-auto">
      {/* パンくずナビ */}
      <nav className="flex items-center gap-1.5 text-xs font-medium text-slate-500" aria-label="パンくずリスト">
        <Link href="/" className="hover:text-rose-600 transition-colors">
          ホーム
        </Link>
        <span className="text-slate-300">›</span>
        <span className="text-slate-700 font-bold">神作10選・キラー特集アーカイブ</span>
      </nav>

      {/* ヘッダーセクション */}
      <section className="rounded-3xl bg-gradient-to-r from-slate-900 via-rose-950 to-slate-900 p-8 md:p-12 border border-slate-800 text-white shadow-2xl space-y-4">
        <span className="inline-flex text-[10px] font-black tracking-widest text-amber-400 bg-amber-400/10 border border-amber-400/20 px-3.5 py-1 rounded-full uppercase">
          SPECIAL SELECTION • 神作厳選＆特集
        </span>
        <h1 className="text-3xl md:text-5xl font-black tracking-tight leading-tight">
          人気AV女優の『神作10選』＆ おすすめ特集
        </h1>
        <p className="text-slate-300 text-xs md:text-sm leading-relaxed max-w-3xl">
          当サイトマニアが厳選！女優ごとの「神作おすすめ10選」個別記事から、月額見放題chの徹底比較、シチュエーション別の濃厚レビューまで、ハズレなしの傑作作品を一挙ご紹介。
        </p>
      </section>

      {/* 最上部固定：FANZA見放題ch 殿堂入りキラー特集 */}
      <section className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-rose-950 via-slate-900 to-slate-950 border-2 border-rose-500/50 shadow-2xl p-6 md:p-8 text-white">
        <div className="absolute top-0 right-0 -mr-16 -mt-16 w-64 h-64 bg-rose-500/20 rounded-full blur-3xl pointer-events-none" />

        <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6 relative z-10">
          <div className="space-y-3 max-w-2xl">
            <div className="flex items-center gap-2">
              <span className="bg-gradient-to-r from-amber-400 to-amber-600 text-slate-950 text-[10px] font-black tracking-widest px-3 py-1 rounded-full uppercase shadow">
                👑 殿堂入りNo.1特集
              </span>
              <span className="bg-rose-500/20 border border-rose-500/30 text-rose-300 text-[10px] font-bold px-2.5 py-0.5 rounded-full">
                定額エロ動画コスパ最強
              </span>
            </div>

            <h2 className="text-2xl md:text-3xl font-black text-white tracking-tight leading-snug">
              【2026年最新】エロ動画見放題ならFANZA見放題ch一択？コスパ・作品数・使い勝手を徹底本音レビュー！
            </h2>

            <p className="text-xs md:text-sm text-slate-300 leading-relaxed">
              「単品買いで毎月数万円溶かしていた…」そんな悩みを一発解決！人気トップ女優の名作からVR・マニアック企画まで、なぜエロ動画サブスクで見放題chが選ばれるのか徹底解説。
            </p>
          </div>

          <div className="flex-shrink-0 w-full lg:w-auto">
            <Link
              href="/fanza-tv-plus"
              className="inline-flex items-center justify-center w-full lg:w-auto text-sm font-black text-white bg-gradient-to-r from-rose-600 via-pink-600 to-rose-500 hover:from-rose-500 hover:to-pink-400 px-8 py-4 rounded-2xl shadow-xl hover:shadow-rose-500/25 transition duration-200 transform hover:-translate-y-0.5 text-center"
            >
              🔥 見放題chの本音レビューを読む ›
            </Link>
          </div>
        </div>
      </section>

      {/* 2大キラーバナー（デバイスガイド ＆ 漫画購入ガイド） */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <section className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-slate-900 via-emerald-950 to-slate-950 border border-emerald-500/40 shadow-xl p-6 text-white flex flex-col justify-between">
          <div className="space-y-2">
            <span className="bg-gradient-to-r from-emerald-400 to-teal-500 text-slate-950 text-[9px] font-black tracking-widest px-2.5 py-0.5 rounded-full uppercase">
              📱 初心者必見
            </span>
            <h3 className="text-lg font-black text-white">
              FANZA動画はどうやって見る？対応デバイス＆視聴完全ガイド
            </h3>
            <p className="text-xs text-slate-300">
              スマホ、PC、PS4/PS5、テレビでの視聴手順と家族バレ防止策を徹底解説。
            </p>
          </div>
          <div className="pt-4">
            <Link
              href="/fanza-device-guide"
              className="inline-block text-xs font-black text-emerald-300 hover:text-emerald-200 underline"
            >
              📺 視聴ガイドを読む ›
            </Link>
          </div>
        </section>

        <section className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-indigo-950 via-purple-950 to-slate-950 border border-indigo-500/40 shadow-xl p-6 text-white flex flex-col justify-between">
          <div className="space-y-2">
            <span className="bg-indigo-500/20 text-indigo-300 text-[9px] font-black tracking-widest px-2.5 py-0.5 rounded-full uppercase border border-indigo-500/30">
              📚 漫画購入ガイド
            </span>
            <h3 className="text-lg font-black text-white">
              なぜみんなFANZAで漫画を買う？メリット・買い方・人気10選
            </h3>
            <p className="text-xs text-slate-300">
              家族バレ防止策やクレカ明細の表記、今すぐ読める売れ筋傑作10選まとめ。
            </p>
          </div>
          <div className="pt-4">
            <Link
              href="/posts/feature_why_buy_fanza_manga_complete_guide"
              className="inline-block text-xs font-black text-indigo-300 hover:text-indigo-200 underline"
            >
              🚀 漫画購入ガイドを読む ›
            </Link>
          </div>
        </section>
      </div>

      {/* インタラクティブ・全特集・10選記事一覧（タブ＆検索対応） */}
      <FeaturesClient
        tenSelectionPosts={tenSelectionPosts}
        deepFeaturePosts={deepFeaturePosts}
        featuredActresses={featuredActresses}
      />
    </div>
  );
}
