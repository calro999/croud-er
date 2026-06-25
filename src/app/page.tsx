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

  return (
    <div className="space-y-10 md:space-y-14">
      {/* ヒーローセクション */}
      <section className="relative rounded-3xl overflow-hidden border border-[#2d123a]/60 bg-gradient-to-br from-[#12071a] via-[#0b030e] to-[#040106] p-6 md:p-12 shadow-2xl flex flex-col md:flex-row items-center justify-between gap-8">
        <div className="absolute top-0 right-0 w-80 h-80 bg-pink-500/5 rounded-full filter blur-3xl pointer-events-none" />
        <div className="absolute bottom-0 left-0 w-80 h-80 bg-purple-500/5 rounded-full filter blur-3xl pointer-events-none" />
        
        <div className="relative max-w-xl space-y-6">
          <span className="inline-block text-[10px] md:text-xs font-bold tracking-widest text-pink-500 bg-pink-500/10 border border-pink-500/20 px-3 py-1 rounded-full uppercase">
            カリスマ熱血レビュアーの秘密基地
          </span>
          <h1 className="text-3xl md:text-5xl font-black tracking-tight leading-tight">
            背徳の扉を開ける、<br />
            <span className="bg-gradient-to-r from-pink-500 via-pink-400 to-purple-400 bg-clip-text text-transparent neon-glow-pink">
              真夜中の秘密書斎
            </span>
          </h1>
          <p className="text-gray-400 leading-relaxed text-xs md:text-sm">
            人妻、ネトラレ、背徳の泥沼。公式の乾いたあらすじを超え、登場人物の葛藤の表情や崩壊していく日常の心理描写を、極上の熱量でお届けします。
          </p>
        </div>

        {/* クイックカウンター */}
        <div className="w-full md:w-auto relative grid grid-cols-2 gap-4 bg-[#1b0a24]/50 border border-[#2d123a] p-5 rounded-2xl md:min-w-[200px]">
          <div className="text-center">
            <span className="block text-2xl font-black text-pink-500 neon-glow-pink">{posts.length}</span>
            <span className="text-[10px] text-gray-400">極上レビュー数</span>
          </div>
          <div className="text-center border-l border-[#2d123a]">
            <span className="block text-2xl font-black text-purple-400">{allActresses.length - 1}</span>
            <span className="text-[10px] text-gray-400">執筆対象女優数</span>
          </div>
        </div>
      </section>

      {/* フィルタ & 検索ダッシュボード */}
      <section className="bg-[#100715]/90 border border-[#2d123a] rounded-2xl p-5 md:p-6 shadow-xl space-y-6 sticky top-20 z-40 backdrop-blur-md">
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
          {/* 検索入力 */}
          <div className="space-y-1">
            <label className="text-[10px] font-bold text-gray-400 uppercase tracking-wider">キーワード検索</label>
            <input
              type="text"
              placeholder="作品名、女優、メーカー名..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full text-xs bg-[#190a21] border border-[#2d123a] rounded-xl px-3.5 py-2.5 text-white placeholder-gray-500 focus:outline-none focus:border-pink-500 transition"
            />
          </div>

          {/* ジャンルフィルタ */}
          <div className="space-y-1">
            <label className="text-[10px] font-bold text-gray-400 uppercase tracking-wider">作品ジャンル</label>
            <select
              value={selectedGenre}
              onChange={(e) => setSelectedGenre(e.target.value)}
              className="w-full text-xs bg-[#190a21] border border-[#2d123a] rounded-xl px-3.5 py-2.5 text-white focus:outline-none focus:border-pink-500 transition cursor-pointer"
            >
              {allGenres.map((g) => (
                <option key={g} value={g}>{g}</option>
              ))}
            </select>
          </div>

          {/* 女優フィルタ */}
          <div className="space-y-1">
            <label className="text-[10px] font-bold text-gray-400 uppercase tracking-wider">出演女優</label>
            <select
              value={selectedActress}
              onChange={(e) => setSelectedActress(e.target.value)}
              className="w-full text-xs bg-[#190a21] border border-[#2d123a] rounded-xl px-3.5 py-2.5 text-white focus:outline-none focus:border-pink-500 transition cursor-pointer"
            >
              {allActresses.map((act) => (
                <option key={act} value={act}>{act}</option>
              ))}
            </select>
          </div>

          {/* ラベルフィルタ */}
          <div className="space-y-1">
            <label className="text-[10px] font-bold text-gray-400 uppercase tracking-wider">特集ラベル</label>
            <select
              value={selectedLabel}
              onChange={(e) => setSelectedLabel(e.target.value)}
              className="w-full text-xs bg-[#190a21] border border-[#2d123a] rounded-xl px-3.5 py-2.5 text-white focus:outline-none focus:border-pink-500 transition cursor-pointer"
            >
              {allLabels.map((lbl) => (
                <option key={lbl} value={lbl}>{lbl}</option>
              ))}
            </select>
          </div>
        </div>
        
        {/* アクティブフィルタのリセット */}
        {(searchQuery || selectedGenre !== "すべて" || selectedActress !== "すべて" || selectedLabel !== "すべて") && (
          <div className="flex items-center justify-between text-xs pt-2 border-t border-[#2d123a]/50">
            <span className="text-gray-400">
              該当作品: <strong className="text-pink-500">{filteredPosts.length}</strong> 件
            </span>
            <button
              onClick={() => {
                setSearchQuery("");
                setSelectedGenre("すべて");
                setSelectedActress("すべて");
                setSelectedLabel("すべて");
              }}
              className="text-pink-500 font-bold hover:underline cursor-pointer"
            >
              フィルターをクリア ×
            </button>
          </div>
        )}
      </section>

      {/* 記事一覧グリッド */}
      {loading ? (
        <div className="text-center py-20">
          <div className="inline-block animate-spin rounded-full h-8 w-8 border-t-2 border-pink-600 border-r-2" />
          <p className="mt-4 text-xs text-gray-500">レビュー書庫を紐解いています...</p>
        </div>
      ) : filteredPosts.length === 0 ? (
        <div className="text-center py-20 border border-dashed border-[#2d123a] rounded-2xl bg-[#0f0714]/30">
          <p className="text-gray-500 text-sm">該当する背徳作品は見つかりませんでした。</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 md:gap-8">
          {filteredPosts.map((post) => (
            <article
              key={post.id}
              className="flex flex-col rounded-2xl overflow-hidden border border-[#2d123a]/70 bg-[#120718]/40 hover:bg-[#120718]/80 hover:border-pink-600/40 transition-all duration-300 shadow-xl group hover:shadow-pink-900/10"
            >
              {/* アイキャッチ画像 */}
              <div className="aspect-[4/3] relative overflow-hidden bg-black flex items-center justify-center border-b border-[#2d123a]/70">
                {post.image ? (
                  <img
                    src={post.image}
                    alt={post.title}
                    className="w-full h-full object-contain group-hover:scale-105 transition duration-500"
                    loading="lazy"
                  />
                ) : (
                  <span className="text-gray-700 text-xs">No Image</span>
                )}
                {/* 年齢制限バッジ */}
                <span className="absolute top-3 left-3 text-[9px] bg-red-600 text-white font-extrabold px-2 py-0.5 rounded shadow">
                  18禁
                </span>
                {/* メーカ名ラベル */}
                <span className="absolute bottom-3 right-3 text-[9px] bg-black/60 backdrop-blur text-gray-300 px-2 py-0.5 rounded">
                  {post.maker}
                </span>
              </div>

              {/* コンテンツ詳細 */}
              <div className="p-5 flex-grow flex flex-col justify-between space-y-4">
                <div className="space-y-3">
                  <span className="text-[9px] font-bold text-gray-500 tracking-wider block">
                    {post.date}
                  </span>
                  <h2 className="text-sm md:text-base font-black leading-snug group-hover:text-pink-500 transition duration-300 line-clamp-2">
                    {post.title}
                  </h2>
                  <div
                    className="text-[11px] text-gray-400 leading-relaxed line-clamp-3"
                    dangerouslySetInnerHTML={{ __html: post.review }}
                  />
                </div>

                <div className="pt-4 flex flex-col gap-3 border-t border-[#2d123a]/50">
                  {/* 主要ジャンルタグ */}
                  <div className="flex flex-wrap gap-1">
                    {post.genres?.slice(0, 2).map((genre) => (
                      <span key={genre} className="text-[9px] bg-purple-950/20 text-purple-400 border border-purple-900/40 px-2 py-0.5 rounded">
                        {genre}
                      </span>
                    ))}
                  </div>
                  <a
                    href={`/posts/${post.id}`}
                    className="w-full text-center text-xs font-bold text-white bg-gradient-to-r from-pink-600 to-purple-600 hover:from-pink-500 hover:to-purple-500 py-2.5 rounded-xl shadow-lg hover:shadow-pink-600/20 transition cursor-pointer"
                  >
                    詳細レビューを読む
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
