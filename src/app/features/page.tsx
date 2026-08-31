import fs from "fs";
import path from "path";
import Link from "next/link";
import { Metadata } from "next";
import { getActressSlug } from "@/lib/slugs";

export const metadata: Metadata = {
  title: "【2026年最新】人気AV女優のおすすめ神作10選・キラー特集一覧 | 背徳の深夜書斎",
  description: "瀬戸環奈、松本いちか、由良かな、石川澪、逢沢みゆ、篠田ゆう、松永あかりなど、トップAV女優の『絶対に抜ける神作おすすめ10選』を徹底レビュー！シチュエーション・見どころ・サンプル動画・画像を一挙紹介。",
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
];

import { getAllSummaryPosts, PostSummary } from "@/lib/posts";

type Post = PostSummary;

function getAllPosts(): Post[] {
  return getAllSummaryPosts();
}

export default function FeaturesPage() {
  const posts = getAllPosts();

  const featureList = FEATURED_ACTRESSES.map(actressObj => {
    const name = actressObj.name;
    const slug = getActressSlug(name);
    const actressPosts = posts.filter(p => (p.actresses || []).includes(name));
    const coverImage = actressPosts.length > 0 ? actressPosts[0].image : "";
    return {
      ...actressObj,
      slug,
      count: actressPosts.length,
      coverImage
    };
  });

  return (
    <div className="space-y-8 max-w-6xl mx-auto">
      {/* パンくずナビ */}
      <nav className="flex items-center gap-1.5 text-xs font-medium text-slate-500" aria-label="パンくずリスト">
        <Link href="/" className="hover:text-rose-600 transition-colors">ホーム</Link>
        <span className="text-slate-300">›</span>
        <span className="text-slate-700 font-bold">女優神作10選 特集一覧</span>
      </nav>

      {/* ヘッダーセクション */}
      <section className="rounded-3xl bg-gradient-to-r from-slate-900 via-rose-950 to-slate-900 p-8 md:p-12 border border-slate-800 text-white shadow-2xl space-y-4">
        <span className="inline-flex text-[10px] font-black tracking-widest text-amber-400 bg-amber-400/10 border border-amber-400/20 px-3.5 py-1 rounded-full uppercase">
          SPECIAL SELECTION • 特集一覧
        </span>
        <h1 className="text-3xl md:text-5xl font-black tracking-tight leading-tight">
          人気AV女優の『神作10選』＆ おすすめ特集
        </h1>
        <p className="text-slate-300 text-xs md:text-sm leading-relaxed max-w-3xl">
          当サイトマニアが厳選！月額見放題chの徹底比較から人気トップ女優の出演作品まで、シチュエーション・見どころ・名場面ショットを徹底分析した特集一覧です。
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

      {/* 漫画購入完全ガイド・キラーバナー */}
      <section className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-indigo-950 via-purple-950 to-slate-950 border-2 border-indigo-500/50 shadow-2xl p-6 md:p-8 text-white">
        <div className="absolute top-0 right-0 -mr-16 -mt-16 w-64 h-64 bg-indigo-500/20 rounded-full blur-3xl pointer-events-none" />
        
        <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6 relative z-10">
          <div className="space-y-3 max-w-2xl">
            <div className="flex flex-wrap items-center gap-2">
              <span className="inline-flex items-center text-[10px] font-black text-indigo-300 bg-indigo-500/20 border border-indigo-500/40 px-3 py-1 rounded-full uppercase tracking-wider">
                🔰 初めての電子書籍
              </span>
              <span className="text-[11px] font-bold text-emerald-400 bg-emerald-400/10 border border-emerald-400/20 px-2.5 py-0.5 rounded-full">
                クレカ明細・安全性・買い方完全解説
              </span>
            </div>
            
            <h2 className="text-2xl md:text-3xl font-black tracking-tight text-white">
              なぜみんなFANZAで漫画を買うのか？メリット・購入方法・人気傑作10選
            </h2>
            
            <p className="text-xs md:text-sm text-slate-300 leading-relaxed">
              「家族にバレない？」「スマホで快適に読める？」といった疑問をゼロから解決。FANZAで本を買う圧倒的メリットと購入手順、今すぐ試せる売れ筋傑作10選を徹底まとめ！
            </p>
          </div>
          
          <div className="flex-shrink-0 w-full lg:w-auto">
            <Link
              href="/posts/feature_why_buy_fanza_manga_complete_guide"
              className="inline-flex items-center justify-center w-full lg:w-auto text-sm font-black text-white bg-gradient-to-r from-indigo-600 via-purple-600 to-rose-600 hover:opacity-95 px-8 py-4 rounded-2xl shadow-xl hover:shadow-indigo-500/25 transition duration-200 transform hover:-translate-y-0.5 text-center"
            >
              🚀 購入完全ガイドを読む ›
            </Link>
          </div>
        </div>
      </section>

      {/* 特集カードグリッド */}
      <section className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {featureList.map(item => (
          <div key={item.name} className="relative group bg-white border border-slate-200/80 rounded-3xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between">
            <div>
              {/* カバー画像 */}
              <div className="w-full aspect-[800/538] relative bg-slate-900 overflow-hidden border-b border-slate-100">
                {item.coverImage ? (
                  <img
                    src={item.coverImage}
                    alt={`${item.name} 特集パッケージ`}
                    referrerPolicy="no-referrer"
                    className="w-full h-full object-cover group-hover:scale-105 transition duration-500"
                    loading="lazy"
                  />
                ) : (
                  <div className="w-full h-full flex items-center justify-center text-slate-400 text-xs">No Image</div>
                )}
                <span className="absolute top-3 right-3 text-[10px] font-black bg-rose-600 text-white px-2.5 py-1 rounded-full shadow">
                  神作10選
                </span>
              </div>

              {/* 情報エリア */}
              <div className="p-6 space-y-3">
                <div className="flex items-center justify-between">
                  <span className="text-[10px] font-black text-rose-500 bg-rose-50 border border-rose-100 px-2.5 py-0.5 rounded-md">
                    {item.tag}
                  </span>
                  <span className="text-xs font-bold text-slate-400">全{item.count}作品</span>
                </div>
                <h2 className="text-xl font-black text-slate-900 group-hover:text-rose-600 transition">
                  {item.name}
                </h2>
                <p className="text-xs text-slate-500 leading-relaxed line-clamp-2">
                  【2026年最新】{item.name}の絶対に抜ける神作おすすめ10選！シチュエーション・見どころ・サンプル動画・名場面ショットを網羅解説。
                </p>
              </div>
            </div>

            {/* CTAボタン */}
            <div className="p-6 pt-0">
              <Link
                href={`/actress/${item.slug}`}
                className="block w-full text-center text-xs font-black text-white bg-gradient-to-r from-rose-500 to-pink-600 hover:from-rose-400 hover:to-pink-500 py-3.5 rounded-2xl shadow transition duration-200"
              >
                👑 {item.name} の10選特集を見る
              </Link>
            </div>
          </div>
        ))}
      </section>
    </div>
  );
}
