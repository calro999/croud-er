import React from "react";

interface TenSelectionCollageProps {
  images?: string[];
  fallbackImage?: string;
  title: string;
  actressName?: string;
  className?: string;
}

/**
 * 神作10選記事の作品画像1〜4枚を1つの美しい2×2グリッドコラージュ画像枠としてレンダリングするコンポーネント
 */
export default function TenSelectionCollage({
  images,
  fallbackImage,
  title,
  actressName = "人気女優",
  className = "",
}: TenSelectionCollageProps) {
  // 4枚揃っている場合は2×2の1枚コラージュ画像枠
  if (images && images.length >= 4) {
    return (
      <div
        className={`w-full aspect-[800/538] relative bg-slate-950 overflow-hidden border-b border-slate-800 ${className}`}
      >
        <div className="grid grid-cols-2 grid-rows-2 w-full h-full gap-0.5 bg-slate-900">
          {images.slice(0, 4).map((imgUrl, i) => (
            <div key={i} className="relative w-full h-full overflow-hidden bg-slate-900 group-hover:opacity-95 transition">
              <img
                src={imgUrl}
                alt={`${title} 収録神作 ${i + 1}`}
                referrerPolicy="no-referrer"
                className="w-full h-full object-cover group-hover:scale-105 transition duration-500"
                loading="lazy"
              />
              <span className="absolute bottom-1 right-1 text-[8px] font-black bg-slate-950/80 text-amber-400 px-1.5 py-0.5 rounded shadow backdrop-blur-sm">
                #{i + 1}
              </span>
            </div>
          ))}
        </div>

        {/* コラージュ中央の十字区切りと中央バッジ */}
        <div className="absolute inset-0 pointer-events-none flex items-center justify-center">
          <div className="bg-slate-950/85 border border-amber-500/40 text-amber-300 px-3 py-1 rounded-full shadow-2xl backdrop-blur-md flex items-center gap-1.5">
            <span className="text-xs">👑</span>
            <span className="text-[10px] font-black tracking-wider uppercase">神作 4選ピックアップ</span>
          </div>
        </div>
      </div>
    );
  }

  // 4枚未満だがfallbackImageがある場合
  if (fallbackImage) {
    return (
      <div className={`w-full aspect-[800/538] relative bg-slate-900 overflow-hidden border-b border-slate-100 ${className}`}>
        <img
          src={fallbackImage}
          alt={title}
          referrerPolicy="no-referrer"
          className="w-full h-full object-cover group-hover:scale-105 transition duration-500"
          loading="lazy"
        />
      </div>
    );
  }

  // 画像が全くない場合のスタイリッシュなプレースホルダー
  return (
    <div
      className={`w-full aspect-[800/538] flex flex-col items-center justify-center bg-gradient-to-br from-slate-900 via-rose-950 to-slate-900 text-white p-4 text-center border-b border-slate-800 ${className}`}
    >
      <span className="text-4xl mb-2">👑</span>
      <span className="text-sm font-black text-rose-300">{actressName}</span>
      <span className="text-xs font-black text-amber-400 mt-1">絶対に抜ける神作10選</span>
    </div>
  );
}
