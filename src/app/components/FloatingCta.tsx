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
      // 画面を300px以上スクロールした時に表示
      if (window.scrollY > 300) {
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
    <div className="fixed bottom-0 left-0 right-0 z-50 p-2 sm:p-2.5 bg-slate-950/95 backdrop-blur-md border-t border-rose-500/40 shadow-2xl transition-all duration-300 animate-in slide-in-from-bottom">
      <div className="max-w-4xl mx-auto space-y-1.5">
        {/* 上部安心マイクロインフォ（クレカ明細・セキュリティ） */}
        <div className="flex items-center justify-between text-[10px] sm:text-[11px] text-slate-400 px-1">
          <div className="flex items-center gap-2 truncate">
            <span className="text-emerald-400 font-bold flex items-center gap-0.5">
              <span>🔒</span><span>明細はDMM表記（作品名なしで安心）</span>
            </span>
            <span className="hidden sm:inline text-slate-500">•</span>
            <span className="hidden sm:inline text-amber-300 font-medium">スマホ・PCで今すぐ即再生OK</span>
          </div>
          <div className="flex items-center gap-1.5 text-slate-400 text-[10px] flex-shrink-0">
            <span>PayPay・楽天ペイ・クレカ対応</span>
          </div>
        </div>

        {/* ボタンコンテナ */}
        <div className="flex items-center gap-2 sm:gap-3">
          {/* 左側：作品情報（PCのみ表示） */}
          <div className="hidden md:block flex-1 min-w-0 pr-2">
            <div className="flex items-center gap-1.5 text-[10px] text-amber-400 font-bold mb-0.5">
              {hinbanText && <span className="bg-amber-400/20 px-1.5 py-0.2 rounded">{hinbanText}</span>}
              {actressName && <span className="truncate">出演: {actressName}</span>}
            </div>
            <p className="text-xs font-bold text-white truncate max-w-sm">{title}</p>
          </div>

          {/* サブアクション：FANZA見放題ch（15万本・高成約率） */}
          <a
            href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fmonthly%2Fpremium%2F&af_id=onchan555-003"
            target="_blank"
            rel="noopener noreferrer"
            className="flex-shrink-0 px-3 sm:px-4 py-2.5 sm:py-2.5 bg-slate-800 hover:bg-slate-700 border border-amber-400/50 hover:border-amber-400 text-amber-300 hover:text-amber-200 font-bold text-[11px] sm:text-xs rounded-xl shadow transition flex items-center justify-center gap-1 text-center"
            title="1本買うより圧倒的にお得！15万本見放題"
          >
            <span>👑</span>
            <span className="whitespace-nowrap">月額見放題ch</span>
          </a>

          {/* メインアクション：該当作品の公式本編・無料プレビュー */}
          <a
            href={affiliateUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="flex-1 text-center px-4 py-2.5 sm:py-2.5 bg-gradient-to-r from-rose-600 via-rose-500 to-pink-600 hover:from-rose-500 hover:to-pink-500 text-white font-black text-xs sm:text-sm rounded-xl shadow-lg shadow-rose-600/30 flex items-center justify-center gap-1.5 transform active:scale-95 transition"
          >
            <span>🔥</span>
            <span className="truncate">公式で本編・無料プレビューを見る</span>
            <span className="text-[10px] opacity-80">›</span>
          </a>
        </div>
      </div>
    </div>
  );
}
