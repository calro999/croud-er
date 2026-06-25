import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "深夜書斎 - 人妻・ネトラレ専門濃厚アーカイブ",
  description: "日常の裏側に潜むスリリングな関係。カリスマ熱血レビュアーが綴る人妻・ネトラレ・背徳ドラマの超濃厚レビューサイト。プレミアムな審美眼で厳選した作品を紹介します。",
  keywords: ["人妻", "ネトラレ", "背徳", "不倫", "AVレビュー", "DMMアフィリエイト"],
  viewport: "width=device-width, initial-scale=1, maximum-scale=1",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ja" className="h-full dark">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet" />
      </head>
      <body className="min-h-full flex flex-col bg-[#030005] text-slate-100 selection:bg-rose-500 selection:text-white font-sans antialiased">
        
        {/* 極薄トップインフォバー */}
        <div className="w-full text-center py-2 bg-gradient-to-r from-rose-950/40 via-purple-950/40 to-rose-950/40 border-b border-purple-950/30 text-[10px] font-bold tracking-widest text-rose-400">
          FOR ADULTS ONLY • 18歳未満の閲覧は固く禁止されています
        </div>

        {/* プレミアムなガラスモルフィズムヘッダー */}
        <header className="border-b border-white/[0.04] glass-header sticky top-0 z-50 py-3.5 px-6">
          <div className="max-w-6xl mx-auto flex items-center justify-between">
            <a href="/" className="flex items-center gap-2 group">
              <span className="text-xl font-extrabold tracking-tight bg-gradient-to-r from-rose-400 via-pink-400 to-purple-400 bg-clip-text text-transparent group-hover:opacity-90 transition">
                深夜書斎
              </span>
              <span className="text-[9px] font-bold tracking-widest text-slate-500 uppercase border border-slate-700/50 px-2 py-0.5 rounded-md bg-slate-900/30">
                ARCHIVE
              </span>
            </a>
            <nav className="flex items-center gap-5 text-xs font-semibold text-slate-400">
              <a href="/" className="hover:text-slate-100 transition">Home</a>
              <span className="text-slate-800">/</span>
              <span className="text-[10px] bg-rose-500/10 text-rose-400 border border-rose-500/20 font-black px-2 py-0.5 rounded">
                R-18
              </span>
            </nav>
          </div>
        </header>

        {/* メインコンテンツ */}
        <main className="flex-grow max-w-6xl w-full mx-auto px-4 py-8 md:py-12">
          {children}
        </main>

        {/* ミニマル・モダンなフッター */}
        <footer className="border-t border-white/[0.04] bg-[#020003] py-10 text-xs text-slate-600">
          <div className="max-w-6xl mx-auto px-4 flex flex-col md:flex-row items-center justify-between gap-6">
            <div className="space-y-1.5 text-center md:text-left">
              <p className="font-bold text-slate-500">© 2026 深夜書斎. All Rights Reserved.</p>
              <p className="text-[10px] max-w-md leading-relaxed">
                当サイトに記載されているアフィリエイトリンクは適正に管理されており、紹介する作品はマニアが厳選した大人のドラマ作品のみです。
              </p>
            </div>
            <div className="flex gap-4 text-[10px] font-bold text-slate-500">
              <a href="/" className="hover:text-slate-400">ホーム</a>
              <span>•</span>
              <a href="https://affiliate.dmm.com/" target="_blank" rel="noopener noreferrer" className="hover:text-slate-400">アフィリエイトについて</a>
            </div>
          </div>
        </footer>
      </body>
    </html>
  );
}
