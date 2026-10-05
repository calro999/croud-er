"use client";

import { useEffect, useState } from "react";

interface FloatingCtaProps {
  affiliateUrl: string;
  title: string;
  actressName?: string;
  hinbanText?: string;
}

export default function FloatingCta({
  affiliateUrl,
  title,
  actressName,
  hinbanText,
}: FloatingCtaProps) {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      // 画面を350px以上スクロールした時に表示
      if (window.scrollY > 350) {
        setIsVisible(true);
      } else {
        setIsVisible(false);
      }
    };

    window.addEventListener("scroll", handleScroll, { passive: true });
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  if (!isVisible) return null;

  return (
    <div className="fixed bottom-0 left-0 right-0 z-50 p-2 sm:p-3 bg-slate-950/90 backdrop-blur-md border-t border-rose-500/30 shadow-2xl transition-all duration-300 animate-in slide-in-from-bottom">
      <div className="max-w-4xl mx-auto flex items-center justify-between gap-3">
        <div className="hidden sm:block flex-1 min-w-0">
          <div className="flex items-center gap-1.5 text-[10px] text-amber-400 font-bold mb-0.5">
            {hinbanText && <span className="bg-amber-400/20 px-1.5 py-0.2 rounded">{hinbanText}</span>}
            {actressName && <span>出演: {actressName}</span>}
          </div>
          <p className="text-xs font-bold text-white truncate max-w-md">{title}</p>
        </div>

        <a
          href={affiliateUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="flex-1 sm:flex-initial w-full sm:w-auto text-center px-5 py-3 sm:py-2.5 bg-gradient-to-r from-rose-600 via-rose-500 to-pink-600 hover:from-rose-500 hover:to-pink-500 text-white font-black text-xs sm:text-sm rounded-xl shadow-lg shadow-rose-600/30 flex items-center justify-center gap-2 transform active:scale-95 transition"
        >
          <span>🔥</span>
          <span>今すぐFANZA公式で作品を見る（最安300円〜/プレビュー）</span>
          <span className="text-[10px] opacity-80">›</span>
        </a>
      </div>
    </div>
  );
}
