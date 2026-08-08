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

interface Post {
  id: string;
  image: string;
  actresses: string[];
  date: string;
}

function getAllPosts(): Post[] {
  const postsDir = path.join(process.cwd(), "src", "data", "posts");
  if (!fs.existsSync(postsDir)) return [];
  const now = new Date();
  try {
    return fs.readdirSync(postsDir)
      .filter(f => f.endsWith(".json"))
      .map(file => {
        try {
          const post = JSON.parse(fs.readFileSync(path.join(postsDir, file), "utf-8")) as Post;
          if (post.date && new Date(post.date).getTime() > now.getTime()) return null;
          return post;
        } catch { return null; }
      })
      .filter(Boolean) as Post[];
  } catch { return []; }
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
          SPECIAL SELECTION • 女優神作10選
        </span>
        <h1 className="text-3xl md:text-5xl font-black tracking-tight leading-tight">
          人気AV女優の『絶対に抜ける神作10選』特別特集
        </h1>
        <p className="text-slate-300 text-xs md:text-sm leading-relaxed max-w-3xl">
          当サイトマニアが厳選！瀬戸環奈、松本いちか、松永あかりなど、トップAV女優たちの出演作品の中からシチュエーション・表情変化・プレイ内容を徹底分析した【ハズレなし神作10選】特集ページ一覧です。
        </p>
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
