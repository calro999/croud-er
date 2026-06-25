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

  // 重複のないラベル（タグ）リストを作成
  const allLabels = ["すべて", ...Array.from(new Set(posts.flatMap((post) => post.labels || [])))];

  // フィルタリングされた記事一覧
  const filteredPosts = selectedLabel === "すべて"
    ? posts
    : posts.filter((post) => post.labels?.includes(selectedLabel));

  return (
    <div className="space-y-12">
      {/* ヒーローセクション */}
      <section className="relative rounded-2xl overflow-hidden border border-[#2d123a] bg-gradient-to-br from-[#1b0825] to-[#07030a] p-8 md:p-12 shadow-2xl">
        <div className="absolute top-0 right-0 w-96 h-96 bg-purple-900/10 rounded-full filter blur-3xl pointer-events-none" />
        <div className="absolute bottom-0 left-0 w-96 h-96 bg-pink-900/10 rounded-full filter blur-3xl pointer-events-none" />
        
        <div className="relative max-w-2xl space-y-6">
          <span className="inline-block text-xs font-black text-pink-500 tracking-widest uppercase border border-pink-500/40 px-3 py-1 rounded bg-pink-500/5">
            マニアによる超濃厚AVレビュー
          </span>
          <h1 className="text-3xl md:text-5xl font-black tracking-tight leading-tight">
            背徳に飢えた貴方へ贈る、<br />
            <span className="bg-gradient-to-r from-pink-500 to-purple-400 bg-clip-text text-transparent neon-glow-pink">
              人妻と不倫の深淵。
            </span>
          </h1>
          <p className="text-gray-400 leading-relaxed text-sm md:text-base">
            公式のあらすじだけでは分からない「登場人物たちの葛藤の表情」「日常が崩壊していく背徳の心理描写」を、熱狂的レビュアーが一切の妥協なく綴ります。
          </p>
        </div>
      </section>

      {/* ラベルフィルタタブ */}
      <div className="flex flex-wrap gap-2 pb-4 border-b border-[#2d123a]">
        {allLabels.map((label) => (
          <button
            key={label}
            onClick={() => setSelectedLabel(label)}
            className={`px-4 py-2 rounded-full text-xs font-bold transition-all cursor-pointer ${
              selectedLabel === label
                ? "bg-pink-600 text-white shadow-lg shadow-pink-600/30 border border-pink-500 scale-105"
                : "bg-[#180922] text-gray-400 hover:text-white border border-[#301642]"
            }`}
          >
            #{label}
          </button>
        ))}
      </div>

      {/* 記事一覧グリッド */}
      {loading ? (
        <div className="text-center py-20">
          <div className="inline-block animate-spin rounded-full h-8 w-8 border-t-2 border-pink-600 border-r-2" />
          <p className="mt-4 text-xs text-gray-500">レビュー書庫を紐解いています...</p>
        </div>
      ) : filteredPosts.length === 0 ? (
        <div className="text-center py-20 border border-dashed border-[#2d123a] rounded-xl bg-[#0f0714]/30">
          <p className="text-gray-500">まだレビューが登録されていません。30分ごとの更新をお待ちください。</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {filteredPosts.map((post) => (
            <article
              key={post.id}
              className="flex flex-col rounded-xl overflow-hidden border border-[#2d123a] bg-[#120718]/40 hover:bg-[#120718]/80 hover:border-pink-600/40 transition-all duration-300 shadow-xl group hover:shadow-pink-900/10"
            >
              {/* アイキャッチ画像 */}
              <div className="aspect-[4/3] relative overflow-hidden bg-black flex items-center justify-center border-b border-[#2d123a]">
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
                <span className="absolute top-3 left-3 text-[10px] bg-red-600 text-white font-extrabold px-2 py-0.5 rounded shadow">
                  18禁
                </span>
              </div>

              {/* コンテンツ詳細 */}
              <div className="p-6 flex-grow flex flex-col justify-between space-y-4">
                <div className="space-y-3">
                  <span className="text-[10px] font-bold text-gray-400 tracking-wider">
                    {post.date} | {post.maker || "単体作品"}
                  </span>
                  <h2 className="text-lg font-black leading-snug group-hover:text-pink-500 transition duration-300 line-clamp-2">
                    {post.title}
                  </h2>
                  <div
                    className="text-xs text-gray-400 leading-relaxed line-clamp-4"
                    dangerouslySetInnerHTML={{ __html: post.review }}
                  />
                </div>

                <div className="pt-4 flex items-center justify-between gap-4 border-t border-[#2d123a]/50">
                  <div className="flex flex-wrap gap-1">
                    {post.labels?.slice(0, 3).map((lbl) => (
                      <span key={lbl} className="text-[10px] text-pink-400 font-bold">
                        #{lbl}
                      </span>
                    ))}
                  </div>
                  <a
                    href={`/posts/${post.id}`}
                    className="text-xs font-bold text-white bg-gradient-to-r from-pink-600 to-purple-600 hover:from-pink-500 hover:to-purple-500 px-4 py-2 rounded-lg shadow-lg hover:shadow-pink-600/20 transition cursor-pointer"
                  >
                    詳細レビューを見る
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
