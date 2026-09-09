"use client";

import { useState, useMemo } from "react";
import Link from "next/link";
import { PostSummary } from "@/lib/posts";
import TenSelectionCollage from "@/app/components/TenSelectionCollage";

interface FeaturesClientProps {
  tenSelectionPosts: PostSummary[];
  deepFeaturePosts: PostSummary[];
  featuredActresses: {
    name: string;
    ruby: string;
    tag: string;
    slug: string;
    count: number;
    coverImage: string;
  }[];
}

export default function FeaturesClient({
  tenSelectionPosts,
  deepFeaturePosts,
  featuredActresses,
}: FeaturesClientProps) {
  const [activeTab, setActiveTab] = useState<"ten" | "actress" | "deep">("ten");
  const [searchQuery, setSearchQuery] = useState("");
  const [displayCount, setDisplayCount] = useState(30);

  // 検索フィルター
  const filteredTenPosts = useMemo(() => {
    if (!searchQuery.trim()) return tenSelectionPosts;
    const q = searchQuery.toLowerCase().trim();
    return tenSelectionPosts.filter(
      (p) =>
        p.title.toLowerCase().includes(q) ||
        (p.actresses || []).some((a) => a.toLowerCase().includes(q)) ||
        (p.genres || []).some((g) => g.toLowerCase().includes(q))
    );
  }, [tenSelectionPosts, searchQuery]);

  const filteredDeepPosts = useMemo(() => {
    if (!searchQuery.trim()) return deepFeaturePosts;
    const q = searchQuery.toLowerCase().trim();
    return deepFeaturePosts.filter(
      (p) =>
        p.title.toLowerCase().includes(q) ||
        (p.actresses || []).some((a) => a.toLowerCase().includes(q)) ||
        (p.genres || []).some((g) => g.toLowerCase().includes(q))
    );
  }, [deepFeaturePosts, searchQuery]);

  const filteredActresses = useMemo(() => {
    if (!searchQuery.trim()) return featuredActresses;
    const q = searchQuery.toLowerCase().trim();
    return featuredActresses.filter(
      (a) =>
        a.name.toLowerCase().includes(q) ||
        a.ruby.toLowerCase().includes(q) ||
        a.tag.toLowerCase().includes(q)
    );
  }, [featuredActresses, searchQuery]);

  const handleTabChange = (tab: "ten" | "actress" | "deep") => {
    setActiveTab(tab);
    setDisplayCount(30);
  };

  return (
    <div className="space-y-10">
      {/* タブナビゲーション */}
      <div className="flex flex-col sm:flex-row items-center justify-between gap-4 border-b border-slate-200 pb-4">
        <div className="flex items-center gap-2 overflow-x-auto w-full sm:w-auto no-scrollbar">
          <button
            onClick={() => handleTabChange("ten")}
            className={`px-5 py-3 rounded-2xl font-black text-xs md:text-sm transition-all whitespace-nowrap shadow-sm flex items-center gap-2 ${
              activeTab === "ten"
                ? "bg-rose-600 text-white shadow-rose-500/25 shadow-lg scale-105"
                : "bg-white text-slate-700 hover:bg-slate-100 border border-slate-200"
            }`}
          >
            <span>👑</span>
            <span>神作10選 記事一覧</span>
            <span
              className={`text-[10px] px-2 py-0.5 rounded-full font-bold ${
                activeTab === "ten" ? "bg-white/20 text-white" : "bg-slate-100 text-slate-600"
              }`}
            >
              {tenSelectionPosts.length}件
            </span>
          </button>

          <button
            onClick={() => handleTabChange("actress")}
            className={`px-5 py-3 rounded-2xl font-black text-xs md:text-sm transition-all whitespace-nowrap shadow-sm flex items-center gap-2 ${
              activeTab === "actress"
                ? "bg-rose-600 text-white shadow-rose-500/25 shadow-lg scale-105"
                : "bg-white text-slate-700 hover:bg-slate-100 border border-slate-200"
            }`}
          >
            <span>💃</span>
            <span>人気女優 Wiki・神作10選</span>
            <span
              className={`text-[10px] px-2 py-0.5 rounded-full font-bold ${
                activeTab === "actress" ? "bg-white/20 text-white" : "bg-slate-100 text-slate-600"
              }`}
            >
              {featuredActresses.length}名
            </span>
          </button>

          <button
            onClick={() => handleTabChange("deep")}
            className={`px-5 py-3 rounded-2xl font-black text-xs md:text-sm transition-all whitespace-nowrap shadow-sm flex items-center gap-2 ${
              activeTab === "deep"
                ? "bg-rose-600 text-white shadow-rose-500/25 shadow-lg scale-105"
                : "bg-white text-slate-700 hover:bg-slate-100 border border-slate-200"
            }`}
          >
            <span>🔥</span>
            <span>シチュエーション別ディープ特集</span>
            <span
              className={`text-[10px] px-2 py-0.5 rounded-full font-bold ${
                activeTab === "deep" ? "bg-white/20 text-white" : "bg-slate-100 text-slate-600"
              }`}
            >
              {deepFeaturePosts.length}件
            </span>
          </button>
        </div>

        {/* 検索インプット */}
        <div className="w-full sm:w-72 relative">
          <input
            type="text"
            placeholder="女優名・シチュエーションで検索..."
            value={searchQuery}
            onChange={(e) => {
              setSearchQuery(e.target.value);
              setDisplayCount(30);
            }}
            className="w-full text-xs bg-white border border-slate-300 rounded-xl px-4 py-2.5 pr-8 focus:outline-none focus:border-rose-500 focus:ring-2 focus:ring-rose-200 text-slate-800"
          />
          {searchQuery && (
            <button
              onClick={() => setSearchQuery("")}
              className="absolute right-3 top-2.5 text-xs text-slate-400 hover:text-slate-600 font-bold"
            >
              ✕
            </button>
          )}
        </div>
      </div>

      {/* 1. 神作10選 記事一覧タブ */}
      {activeTab === "ten" && (
        <section className="space-y-6">
          <div className="flex items-center justify-between">
            <h2 className="text-xl md:text-2xl font-black text-slate-900 flex items-center gap-2">
              <span>👑</span>
              <span>女優別・ジャンル別「神作10選」完全アーカイブ</span>
            </h2>
            <span className="text-xs font-bold text-slate-500">
              全 {filteredTenPosts.length} 件
            </span>
          </div>

          {filteredTenPosts.length === 0 ? (
            <div className="text-center py-16 bg-white border border-slate-200 rounded-3xl text-slate-400 space-y-2">
              <p className="text-base font-bold">該当する10選記事が見つかりませんでした。</p>
              <p className="text-xs">別のキーワードで検索してみてください。</p>
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
              {filteredTenPosts.slice(0, displayCount).map((post) => {
                const actressName = (post.actresses || [])[0] || "人気女優";
                const cleanReview = (post.review || "")
                  .replace(/<[^>]*>/g, "")
                  .replace(/\s+/g, " ")
                  .trim();
                const excerpt = cleanReview.slice(0, 85) + (cleanReview.length > 85 ? "..." : "");

                return (
                  <article
                    key={post.id}
                    className="relative group bg-white border border-slate-200/90 rounded-3xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between"
                  >
                    <div>
                      {/* アイキャッチ（記事内の作品1〜4枚の2x2コラージュ） */}
                      <Link href={`/posts/${post.id}`} className="block relative group">
                        <TenSelectionCollage
                          images={post.featured_images}
                          fallbackImage={post.image}
                          title={post.title}
                          actressName={actressName}
                        />
                        <span className="absolute top-3 left-3 text-[10px] font-black bg-rose-600 text-white px-2.5 py-1 rounded-full shadow-md z-10">
                          神作10選
                        </span>
                        {post.date && (
                          <span className="absolute bottom-2 right-2 text-[9px] font-bold bg-slate-950/70 text-slate-300 px-2 py-0.5 rounded-md backdrop-blur-sm z-10">
                            {post.date.split(" ")[0]}
                          </span>
                        )}
                      </Link>

                      {/* 本文エリア */}
                      <div className="p-5 space-y-3">
                        <div className="flex flex-wrap items-center gap-1.5">
                          {actressName && (
                            <span className="text-[10px] font-black text-rose-600 bg-rose-50 border border-rose-100 px-2.5 py-0.5 rounded-md">
                              💃 {actressName}
                            </span>
                          )}
                          {(post.genres || [])
                            .filter((g) => !g.includes("10選") && g !== "特集" && g !== "FANZA")
                            .slice(0, 2)
                            .map((g) => (
                              <span
                                key={g}
                                className="text-[10px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded-md"
                              >
                                #{g}
                              </span>
                            ))}
                        </div>

                        <h3 className="text-base font-black text-slate-900 group-hover:text-rose-600 transition leading-snug line-clamp-2">
                          <Link href={`/posts/${post.id}`}>{post.title}</Link>
                        </h3>

                        {excerpt && (
                          <p className="text-xs text-slate-500 leading-relaxed line-clamp-2">
                            {excerpt}
                          </p>
                        )}
                      </div>
                    </div>

                    {/* アクションボタン */}
                    <div className="p-5 pt-0">
                      <Link
                        href={`/posts/${post.id}`}
                        className="block w-full text-center text-xs font-black text-white bg-gradient-to-r from-rose-500 to-pink-600 hover:from-rose-400 hover:to-pink-500 py-3 rounded-2xl shadow transition duration-200"
                      >
                        📖 10選まとめ記事を読む ›
                      </Link>
                    </div>
                  </article>
                );
              })}
            </div>
          )}

          {/* もっと見るボタン */}
          {filteredTenPosts.length > displayCount && (
            <div className="text-center pt-4">
              <button
                onClick={() => setDisplayCount((prev) => prev + 30)}
                className="px-8 py-3.5 bg-white border-2 border-rose-500 text-rose-600 hover:bg-rose-50 rounded-2xl text-xs font-black shadow-sm transition transform hover:-translate-y-0.5"
              >
                👇 さらに10選記事を読み込む（残り {filteredTenPosts.length - displayCount} 件）
              </button>
            </div>
          )}
        </section>
      )}

      {/* 2. 人気女優 Wiki・神作10選タブ */}
      {activeTab === "actress" && (
        <section className="space-y-6">
          <div className="flex items-center justify-between">
            <h2 className="text-xl md:text-2xl font-black text-slate-900 flex items-center gap-2">
              <span>💃</span>
              <span>トップ女優 Wikipedia風プロフィール ＆ 出演作・神作10選</span>
            </h2>
            <span className="text-xs font-bold text-slate-500">
              厳選 {filteredActresses.length} 名
            </span>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredActresses.map((item) => (
              <div
                key={item.name}
                className="relative group bg-white border border-slate-200/90 rounded-3xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between"
              >
                <div>
                  <Link href={`/actress/${item.slug}`} className="block w-full aspect-[800/538] relative bg-slate-900 overflow-hidden border-b border-slate-100">
                    {item.coverImage ? (
                      <img
                        src={item.coverImage}
                        alt={`${item.name} 特集パッケージ`}
                        referrerPolicy="no-referrer"
                        className="w-full h-full object-cover group-hover:scale-105 transition duration-500"
                        loading="lazy"
                      />
                    ) : (
                      <div className="w-full h-full flex items-center justify-center text-slate-400 text-xs">
                        No Image
                      </div>
                    )}
                    <span className="absolute top-3 right-3 text-[10px] font-black bg-rose-600 text-white px-2.5 py-1 rounded-full shadow">
                      神作10選
                    </span>
                  </Link>

                  <div className="p-6 space-y-3">
                    <div className="flex items-center justify-between">
                      <span className="text-[10px] font-black text-rose-500 bg-rose-50 border border-rose-100 px-2.5 py-0.5 rounded-md">
                        {item.tag}
                      </span>
                      <span className="text-xs font-bold text-slate-400">全{item.count}作品</span>
                    </div>
                    <h3 className="text-xl font-black text-slate-900 group-hover:text-rose-600 transition">
                      <Link href={`/actress/${item.slug}`}>{item.name}</Link>
                    </h3>
                    <p className="text-xs text-slate-500 leading-relaxed line-clamp-2">
                      【2026年最新】{item.name}の絶対に抜ける神作おすすめ10選！シチュエーション・見どころ・サンプル動画・名場面ショットを網羅解説。
                    </p>
                  </div>
                </div>

                <div className="p-6 pt-0">
                  <Link
                    href={`/actress/${item.slug}`}
                    className="block w-full text-center text-xs font-black text-white bg-gradient-to-r from-rose-500 to-pink-600 hover:from-rose-400 hover:to-pink-500 py-3.5 rounded-2xl shadow transition duration-200"
                  >
                    👑 {item.name} の10選特集を見る ›
                  </Link>
                </div>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* 3. シチュエーション別ディープ特集タブ */}
      {activeTab === "deep" && (
        <section className="space-y-6">
          <div className="flex items-center justify-between">
            <h2 className="text-xl md:text-2xl font-black text-slate-900 flex items-center gap-2">
              <span>🔥</span>
              <span>シチュエーション・企画別ディープAV特集</span>
            </h2>
            <span className="text-xs font-bold text-slate-500">
              全 {filteredDeepPosts.length} 件
            </span>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredDeepPosts.slice(0, displayCount).map((post) => {
              const cleanReview = (post.review || "")
                .replace(/<[^>]*>/g, "")
                .replace(/\s+/g, " ")
                .trim();
              const excerpt = cleanReview.slice(0, 85) + (cleanReview.length > 85 ? "..." : "");

              return (
                <article
                  key={post.id}
                  className="relative group bg-white border border-slate-200/90 rounded-3xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between"
                >
                  <div>
                    <Link href={`/posts/${post.id}`} className="block w-full aspect-[800/538] relative bg-slate-900 overflow-hidden border-b border-slate-100">
                      {post.image ? (
                        <img
                          src={post.image}
                          alt={post.title}
                          referrerPolicy="no-referrer"
                          className="w-full h-full object-cover group-hover:scale-105 transition duration-500"
                          loading="lazy"
                        />
                      ) : (
                        <div className="w-full h-full flex items-center justify-center text-slate-400 text-xs">
                          No Image
                        </div>
                      )}
                      <span className="absolute top-3 left-3 text-[10px] font-black bg-indigo-600 text-white px-2.5 py-1 rounded-full shadow-md">
                        ディープ特集
                      </span>
                    </Link>

                    <div className="p-5 space-y-3">
                      <div className="flex flex-wrap items-center gap-1.5">
                        {(post.genres || [])
                          .filter((g) => g !== "特集" && g !== "FANZA")
                          .slice(0, 3)
                          .map((g) => (
                            <span
                              key={g}
                              className="text-[10px] font-bold text-indigo-600 bg-indigo-50 border border-indigo-100 px-2 py-0.5 rounded-md"
                            >
                              #{g}
                            </span>
                          ))}
                      </div>

                      <h3 className="text-base font-black text-slate-900 group-hover:text-indigo-600 transition leading-snug line-clamp-2">
                        <Link href={`/posts/${post.id}`}>{post.title}</Link>
                      </h3>

                      {excerpt && (
                        <p className="text-xs text-slate-500 leading-relaxed line-clamp-2">
                          {excerpt}
                        </p>
                      )}
                    </div>
                  </div>

                  <div className="p-5 pt-0">
                    <Link
                      href={`/posts/${post.id}`}
                      className="block w-full text-center text-xs font-black text-white bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 py-3 rounded-2xl shadow transition duration-200"
                    >
                      🔥 特集記事を詳しく見る ›
                    </Link>
                  </div>
                </article>
              );
            })}
          </div>

          {filteredDeepPosts.length > displayCount && (
            <div className="text-center pt-4">
              <button
                onClick={() => setDisplayCount((prev) => prev + 30)}
                className="px-8 py-3.5 bg-white border-2 border-indigo-600 text-indigo-600 hover:bg-indigo-50 rounded-2xl text-xs font-black shadow-sm transition transform hover:-translate-y-0.5"
              >
                👇 さらにディープ特集を読み込む（残り {filteredDeepPosts.length - displayCount} 件）
              </button>
            </div>
          )}
        </section>
      )}
    </div>
  );
}
