"use client";

import { useState, useEffect } from "react";

interface Post {
  id: string;
  title: string;
  review: string;
  image: string;
  sample_images: string[];
  affiliate_url: string;
  genres: string[];
  actresses: string[];
  maker: string;
  date: string;
  labels: string[];
}

export default function Home() {
  const [posts, setPosts] = useState<Post[]>([]);
  const [searchQuery, setSearchQuery] = useState<string>("");
  const [selectedGenre, setSelectedGenre] = useState<string>("すべて");
  const [selectedActress, setSelectedActress] = useState<string>("すべて");
  const [selectedLabel, setSelectedLabel] = useState<string>("すべて");
  const [loading, setLoading] = useState<boolean>(true);

  // モバイルアコーディオン用のフィルタートグル状態
  const [isFilterOpen, setIsFilterOpen] = useState<boolean>(false);

  useEffect(() => {
    fetch("/data/posts.json")
      .then((res) => res.json())
      .then((data) => {
        setPosts(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error loading posts:", err);
        setLoading(false);
      });
  }, []);

  // 重複のないジャンル、女優、ラベルのリストを抽出
  const allGenres = ["すべて", ...Array.from(new Set(posts.flatMap((p) => p.genres || [])))];
  const allActresses = ["すべて", ...Array.from(new Set(posts.flatMap((p) => p.actresses || []))).filter(Boolean)];
  const allLabels = ["すべて", ...Array.from(new Set(posts.flatMap((p) => p.labels || [])))];

  // フィルタリング処理（検索、ジャンル、女優、ラベル）
  const filteredPosts = posts.filter((post) => {
    const matchesSearch =
      post.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      post.review.toLowerCase().includes(searchQuery.toLowerCase()) ||
      post.maker.toLowerCase().includes(searchQuery.toLowerCase());
    
    const matchesGenre = selectedGenre === "すべて" || post.genres?.includes(selectedGenre);
    const matchesActress = selectedActress === "すべて" || post.actresses?.includes(selectedActress);
    const matchesLabel = selectedLabel === "すべて" || post.labels?.includes(selectedLabel);

    return matchesSearch && matchesGenre && matchesActress && matchesLabel;
  });

  const hasActiveFilters = searchQuery || selectedGenre !== "すべて" || selectedActress !== "すべて" || selectedLabel !== "すべて";

  return (
    <div className="space-y-12">
      {/* ヒーローセクション - メディアアート風のモダンミニマル */}
      <section className="relative rounded-3xl overflow-hidden bg-gradient-to-br from-[#0c0512] via-[#050208] to-[#020004] p-8 md:p-14 border border-white/[0.03] shadow-2xl flex flex-col md:flex-row items-start md:items-center justify-between gap-8">
        <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-rose-500/[0.02] rounded-full filter blur-3xl pointer-events-none" />
        <div className="absolute bottom-0 left-0 w-[500px] h-[500px] bg-purple-500/[0.02] rounded-full filter blur-3xl pointer-events-none" />
        
        <div className="relative max-w-2xl space-y-6">
          <span className="inline-flex text-[9px] font-bold tracking-widest text-rose-400 bg-rose-500/5 border border-rose-500/10 px-3 py-1 rounded-full uppercase">
            Curated Adult Drama Reviews
          </span>
          <h1 className="text-3xl md:text-5xl font-extrabold tracking-tight leading-[1.15]">
            真夜中に紐解く、<br />
            <span className="bg-gradient-to-r from-rose-400 via-pink-400 to-purple-400 bg-clip-text text-transparent">
              背徳のインサイドストーリー
            </span>
          </h1>
          <p className="text-slate-400 leading-relaxed text-xs md:text-sm max-w-lg">
            作品の背景にある大人の葛藤、表情に込められた罪悪感。当書斎では、単なるあらすじの模倣ではない「マニアの熱量」を美的なUIのなかで静かに綴ります。
          </p>
        </div>

        {/* スタッツカウンター - メタリック調のミニマルパネル */}
        <div className="w-full md:w-auto grid grid-cols-2 gap-4 bg-white/[0.01] border border-white/[0.05] p-6 rounded-2xl md:min-w-[240px] backdrop-blur-sm">
          <div className="text-center space-y-1">
            <span className="block text-3xl font-black text-rose-400 tracking-tight">{posts.length}</span>
            <span className="text-[9px] font-bold text-slate-500 uppercase tracking-widest block">Reviews</span>
          </div>
          <div className="text-center space-y-1 border-l border-white/[0.05]">
            <span className="block text-3xl font-black text-purple-400 tracking-tight">{allActresses.length - 1}</span>
            <span className="text-[9px] font-bold text-slate-500 uppercase tracking-widest block">Actresses</span>
          </div>
        </div>
      </section>

      {/* 検索・絞り込みパネル - モバイルファースト・モダンフィルター */}
      <section className="bg-[#09040d]/40 border border-white/[0.04] rounded-2xl p-4 md:p-6 shadow-xl space-y-4">
        
        {/* モバイル用アコーディオンヘッダー */}
        <div className="flex items-center justify-between md:hidden">
          <span className="text-xs font-bold text-slate-300">条件を指定して絞り込む</span>
          <button
            onClick={() => setIsFilterOpen(!isFilterOpen)}
            className="text-xs font-bold text-rose-400 bg-rose-500/10 px-3 py-1.5 rounded-lg border border-rose-500/20 cursor-pointer"
          >
            {isFilterOpen ? "閉じる" : "フィルターを表示"}
          </button>
        </div>

        {/* フィルターフォーム（モバイルはアコーディオン開閉、PCは常時表示） */}
        <div className={`grid grid-cols-1 md:grid-cols-4 gap-4 ${isFilterOpen ? "block" : "hidden md:grid"}`}>
          {/* 検索入力 */}
          <div className="space-y-1.5">
            <label className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">キーワード検索</label>
            <input
              type="text"
              placeholder="作品名、女優、メーカー..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full text-xs bg-[#0b0610] border border-white/[0.05] rounded-xl px-4 py-3 text-white placeholder-slate-600 focus:outline-none focus:border-rose-500/80 transition"
            />
          </div>

          {/* ジャンルフィルタ */}
          <div className="space-y-1.5">
            <label className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">ジャンル</label>
            <select
              value={selectedGenre}
              onChange={(e) => setSelectedGenre(e.target.value)}
              className="w-full text-xs bg-[#0b0610] border border-white/[0.05] rounded-xl px-4 py-3 text-white focus:outline-none focus:border-rose-500/80 transition cursor-pointer appearance-none"
            >
              {allGenres.map((g) => (
                <option key={g} value={g}>{g}</option>
              ))}
            </select>
          </div>

          {/* 女優フィルタ */}
          <div className="space-y-1.5">
            <label className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">出演女優</label>
            <select
              value={selectedActress}
              onChange={(e) => setSelectedActress(e.target.value)}
              className="w-full text-xs bg-[#0b0610] border border-white/[0.05] rounded-xl px-4 py-3 text-white focus:outline-none focus:border-rose-500/80 transition cursor-pointer appearance-none"
            >
              {allActresses.map((act) => (
                <option key={act} value={act}>{act}</option>
              ))}
            </select>
          </div>

          {/* ラベルフィルタ */}
          <div className="space-y-1.5">
            <label className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">特集レーベル</label>
            <select
              value={selectedLabel}
              onChange={(e) => setSelectedLabel(e.target.value)}
              className="w-full text-xs bg-[#0b0610] border border-white/[0.05] rounded-xl px-4 py-3 text-white focus:outline-none focus:border-rose-500/80 transition cursor-pointer appearance-none"
            >
              {allLabels.map((lbl) => (
                <option key={lbl} value={lbl}>{lbl}</option>
              ))}
            </select>
          </div>
        </div>

        {/* アクティブフィルターの状態表示 */}
        {hasActiveFilters && (
          <div className="flex items-center justify-between text-xs pt-3.5 border-t border-white/[0.04]">
            <span className="text-slate-400">
              該当作品: <strong className="text-rose-400">{filteredPosts.length}</strong> 件
            </span>
            <button
              onClick={() => {
                setSearchQuery("");
                setSelectedGenre("すべて");
                setSelectedActress("すべて");
                setSelectedLabel("すべて");
              }}
              className="text-rose-400 font-bold hover:text-rose-300 cursor-pointer"
            >
              リセット ×
            </button>
          </div>
        )}
      </section>

      {/* 記事一覧グリッド - ハイブランドのギャラリーのような余白とタイポグラフィ */}
      {loading ? (
        <div className="text-center py-24">
          <div className="inline-block animate-spin rounded-full h-6 w-6 border-t-2 border-rose-500 border-r-2" />
          <p className="mt-4 text-xs text-slate-500">書庫を整理しています...</p>
        </div>
      ) : filteredPosts.length === 0 ? (
        <div className="text-center py-24 border border-dashed border-white/[0.04] rounded-2xl bg-white/[0.01]">
          <p className="text-slate-500 text-xs">該当するレビューが見つかりませんでした。</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-10">
          {filteredPosts.map((post) => (
            <article
              key={post.id}
              className="flex flex-col rounded-2xl overflow-hidden bg-white/[0.01] border border-white/[0.03] card-hover-effect"
            >
              {/* アイキャッチ画像 - アスペクト比を16:9へ刷新してモダンに */}
              <div className="aspect-[16/10] relative overflow-hidden bg-[#020003] flex items-center justify-center border-b border-white/[0.03]">
                {post.image ? (
                  <img
                    src={post.image}
                    alt={post.title}
                    className="w-full h-full object-cover transition-transform duration-700 ease-out group-hover:scale-105"
                    loading="lazy"
                  />
                ) : (
                  <span className="text-slate-700 text-xs font-semibold">No Image</span>
                )}
                {/* プレミアムな小サイズ年齢制限タグ */}
                <span className="absolute top-4 left-4 text-[9px] font-black bg-rose-500/10 text-rose-400 border border-rose-500/20 px-2 py-0.5 rounded shadow-sm">
                  18+
                </span>
                <span className="absolute bottom-4 right-4 text-[9px] font-bold bg-[#030005]/80 backdrop-blur-sm text-slate-400 px-2.5 py-0.5 rounded-md border border-white/[0.04]">
                  {post.maker}
                </span>
              </div>

              {/* メモリアルな情報レイアウト */}
              <div className="p-6 flex-grow flex flex-col justify-between space-y-5">
                <div className="space-y-3.5">
                  <span className="text-[10px] font-bold text-slate-500 tracking-wider block">
                    {post.date}
                  </span>
                  <h2 className="text-base font-extrabold leading-snug text-slate-100 hover:text-rose-400 transition-colors duration-300 line-clamp-2">
                    {post.title}
                  </h2>
                  <div
                    className="text-xs text-slate-400 leading-relaxed line-clamp-3 font-medium"
                    dangerouslySetInnerHTML={{ __html: post.review }}
                  />
                </div>

                <div className="pt-4 flex flex-col gap-3 border-t border-white/[0.03]">
                  {/* 主要ジャンルタグ */}
                  <div className="flex flex-wrap gap-1">
                    {post.genres?.slice(0, 3).map((genre) => (
                      <span key={genre} className="text-[9px] font-bold text-slate-400 bg-white/[0.02] border border-white/[0.04] px-2 py-0.5 rounded-md">
                        {genre}
                      </span>
                    ))}
                  </div>
                  <a
                    href={`/posts/${post.id}`}
                    className="w-full text-center text-xs font-bold text-white bg-gradient-to-r from-rose-500 to-rose-600 hover:from-rose-400 hover:to-rose-500 py-3 rounded-xl shadow-lg transition-all duration-300 cursor-pointer"
                  >
                    極上レビューを読む
                  </a>
                </div>
              </div>
            </article>
          ))}
        </div>
      )}
    </div>
  );
}
