import type { Metadata } from "next";
import Script from "next/script";
import "./globals.css";

export const metadata: Metadata = {
  title: "禁断と背徳の書庫「深夜書斎」 - 人妻・ネトラレ・不倫ドラマ濃厚レビュー",
  description: "決して覗いてはならない、日常のすぐ裏側に潜む背徳の情事。カリスマ熱血レビュアーが圧倒的熱量で紐解く、人妻・ネトラレ・不倫・寝取られドラマの濃厚考察＆官能レビューアーカイブ。あなたの本能と妄想を極限まで刺激する秘密の記録です。",
  keywords: [
    "人妻", "ネトラレ", "背徳", "不倫", "寝取られ", "寝取り", "NTR", "禁断の恋", 
    "秘密の関係", "背徳感", "昼下がりの情事", "官能ドラマ", "大人向けレビュー"
  ],
  referrer: "no-referrer",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ja" className="h-full">
      <head>
        <meta name="referrer" content="no-referrer" />
        {/* Google Analytics */}
        <Script
          src="https://www.googletagmanager.com/gtag/js?id=G-BTJKTTHLHB"
          strategy="afterInteractive"
        />
        <Script id="google-analytics" strategy="afterInteractive">
          {`
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());

            gtag('config', 'G-BTJKTTHLHB');
          `}
        </Script>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet" />
      </head>
      <body className="min-h-full flex flex-col bg-[#f1f5f9] text-slate-900 selection:bg-rose-500 selection:text-white font-sans antialiased">
        
        {/* 極薄トップインフォバー */}
        <div className="w-full text-center py-2 bg-gradient-to-r from-slate-200 via-rose-100 to-slate-200 border-b border-slate-300/60 text-[10px] font-bold tracking-widest text-slate-600">
          FOR ADULTS ONLY • 18歳未満の閲覧は固く禁止されています
        </div>

        {/* プレミアムなクリーンガラスヘッダー */}
        <header className="border-b border-slate-200 glass-header sticky top-0 z-50 py-3.5 px-6 shadow-sm">
          <div className="max-w-6xl mx-auto flex items-center justify-between">
            <a href="/" className="flex items-center gap-2 group">
              <span className="text-xl font-black tracking-tight bg-gradient-to-r from-slate-900 via-rose-700 to-slate-800 bg-clip-text text-transparent group-hover:opacity-90 transition">
                深夜書斎
              </span>
              <span className="text-[9px] font-bold tracking-widest text-slate-500 uppercase border border-slate-300 px-2 py-0.5 rounded-md bg-white">
                ARCHIVE
              </span>
            </a>
            <nav className="flex items-center gap-5 text-xs font-bold text-slate-500">
              <a href="/" className="hover:text-slate-950 transition">Home</a>
              <span className="text-slate-300">/</span>
              <a href="https://bakuero.pages.dev/" target="_blank" rel="noopener noreferrer" className="hover:text-purple-600 transition text-purple-700 border border-purple-500/30 px-2 py-1 rounded">姉妹サイト: バクロファイル</a>
              <span className="text-slate-300">/</span>
              <span className="text-[10px] bg-rose-500 text-white font-black px-2 py-0.5 rounded">
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
        <footer className="border-t border-slate-200 bg-white py-10 text-xs text-slate-500 shadow-inner">
          <div className="max-w-6xl mx-auto px-4 flex flex-col md:flex-row items-center justify-between gap-6">
            <div className="space-y-1.5 text-center md:text-left">
              <p className="font-bold text-slate-700">© 2026 深夜書斎. All Rights Reserved.</p>
              <p className="text-[10px] max-w-md leading-relaxed text-slate-400">
                当サイトに記載されているアフィリエイトリンクは適正に管理されており、紹介する作品はマニアが厳選した大人のドラマ作品のみです。
              </p>
            </div>
            <div className="flex flex-wrap gap-4 text-[10px] font-bold text-slate-500 justify-center md:justify-end">
              <a href="/" className="hover:text-slate-950">ホーム</a>
              <span>•</span>
              <a href="#" className="hover:text-purple-600 text-purple-700">姉妹サイト: 暴露ファイル</a>
              <span>•</span>
              <a href="https://affiliate.dmm.com/" target="_blank" rel="noopener noreferrer" className="hover:text-slate-950">アフィリエイトについて</a>
            </div>
          </div>
        </footer>
      </body>
    </html>
  );
}
