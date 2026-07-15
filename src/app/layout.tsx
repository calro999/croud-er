import type { Metadata } from "next";
import Script from "next/script";
import AmateurBanner from "./components/AmateurBanner";
import TagCloud from "./components/TagCloud";
import "./globals.css";

export const metadata: Metadata = {
  metadataBase: new URL("https://haitoku.pages.dev"),
  title: {
    default: "背徳の深夜書斎 | AV・アダルト動画レビュー・感想まとめ【FANZA厳選】",
    template: "%s | 背徳の深夜書斎",
  },
  description: "FANZAの人気AV作品を徹底レビュー！人気女優の出演作・ジャンル別おすすめ・品番検索まで対応。巨乳・単体女優・人妻・素人など豊富なジャンルから厳選したレビューをまとめています。",
  keywords: [
    // 主要検索キーワード
    "AV レビュー", "アダルト動画 感想", "FANZA おすすめ", "AV 品番 検索",
    // ジャンル系
    "巨乳 AV", "単体女優 レビュー", "人妻 AV おすすめ", "素人 流出", "フェラ 動画",
    "騎乗位 おすすめ", "ハイビジョン AV", "美乳 女優", "中出し 動画",
    // サイト名
    "背徳の深夜書斎", "大人向けレビュー", "アダルトビデオ 評価",
    // ロングテール
    "AV女優 おすすめ 2026", "FANZA 人気ランキング", "アダルト動画 ランキング 2026"
  ],
  referrer: "no-referrer",
  alternates: {
    canonical: "https://haitoku.pages.dev",
  },
  openGraph: {
    type: "website",
    locale: "ja_JP",
    url: "https://haitoku.pages.dev",
    siteName: "背徳の深夜書斎",
    title: "背徳の深夜書斎 | AV・アダルト動画レビュー・感想まとめ【FANZA厳選】",
    description: "FANZAの人気AV作品を徹底レビュー！人気女優の出演作・ジャンル別おすすめ・品番検索まで対応。",
  },
  twitter: {
    card: "summary_large_image",
    title: "背徳の深夜書斎 | AV・アダルト動画レビュー・感想まとめ",
    description: "FANZAの人気AV作品を徹底レビュー！人気女優・ジャンル別おすすめ・品番検索まで対応。",
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
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
                背徳の深夜書斎
              </span>
              <span className="text-[9px] font-bold tracking-widest text-slate-500 uppercase border border-slate-300 px-2 py-0.5 rounded-md bg-white">
                AMATEUR
              </span>
            </a>
            <nav className="flex items-center gap-5 text-xs font-bold text-slate-500">
              <a href="/" className="hover:text-slate-950 transition">Home</a>
              <span className="text-slate-300">/</span>
              <a href="/ranking" className="hover:text-rose-600 transition">ランキング</a>
              <span className="text-slate-300">/</span>
              <a href="https://er-2.pages.dev/" target="_blank" rel="noopener noreferrer" className="hover:text-rose-600 transition text-rose-700 border border-rose-500/30 px-2 py-1 rounded">姉妹サイト: バクロファイル</a>
              <span className="text-slate-300">/</span>
              <a href="https://er-3.pages.dev/" target="_blank" rel="noopener noreferrer" className="hover:text-rose-600 transition text-rose-700 border border-rose-500/30 px-2 py-1 rounded">姉妹サイト: 美女ギャル</a>
              <span className="text-slate-300">/</span>
              <span className="text-[10px] bg-rose-500 text-white font-black px-2 py-0.5 rounded">
                R-18
              </span>
            </nav>
          </div>
        </header>

        {/* メインコンテンツ */}
        <div className="flex-grow w-full relative flex justify-center items-start">
          {/* 左サイド追従バナー */}
          <aside className="hidden xl:flex flex-col fixed left-4 top-24 w-[270px] z-30 space-y-6 items-center">
            <AmateurBanner affiliateId="onchan555-003" bannerId="1082_300_250" />
            <AmateurBanner affiliateId="onchan555-003" bannerId="377_300_250" />
            <AmateurBanner affiliateId="onchan555-003" bannerId="1980_300_250" />
          </aside>

          <main className="flex-grow max-w-6xl w-full mx-auto px-4 py-8 md:py-12">
            {children}
          </main>

          {/* 右サイド追従バナー */}
          <aside className="hidden xl:flex flex-col fixed right-4 xl:right-[calc((100vw-1152px)/4-135px)] top-24 w-[270px] z-30 space-y-6 items-center">
            <AmateurBanner affiliateId="onchan555-003" bannerId="75_300_250" />
            <AmateurBanner affiliateId="onchan555-003" bannerId="68_300_250" />
            <AmateurBanner affiliateId="onchan555-003" bannerId="1506_300_250" />
          </aside>
        </div>





        {/* ランダムタグクラウド */}
        <TagCloud />

        {/* ミニマル・モダンなフッター */}
        <footer className="border-t border-slate-200 bg-white py-10 text-xs text-slate-500 shadow-inner">
          <div className="max-w-6xl mx-auto px-4 flex flex-col md:flex-row items-center justify-between gap-6">
            <div className="space-y-1.5 text-center md:text-left">
              <p className="font-bold text-slate-700">© 2026 背徳の深夜書斎. All Rights Reserved.</p>
              <p className="text-[10px] max-w-md leading-relaxed text-slate-400">
                当サイトに記載されているアフィリエイトリンクは適正に管理されており、紹介する作品はマニアが厳選した大人の作品のみです。
              </p>
            </div>
            <div className="flex flex-wrap gap-4 text-[10px] font-bold text-slate-500 justify-center md:justify-end">
              <a href="/" className="hover:text-slate-950">ホーム</a>
              <span>•</span>
              <a href="/archives" className="hover:text-rose-600 text-slate-600 font-bold">全記事一覧（サイトマップ）</a>
              <span>•</span>
              <span className="text-slate-400">姉妹サイト:</span>
              <a href="https://er-2.pages.dev/" target="_blank" rel="noopener noreferrer" className="hover:text-rose-600 text-rose-700">禁断のバクロファイル</a>
              <span>•</span>
              <a href="https://er-3.pages.dev/" target="_blank" rel="noopener noreferrer" className="hover:text-rose-600 text-rose-700">美女ギャルクロニクル</a>
            </div>
          </div>
        </footer>

        {/* 忍者AdMax (ユーザー指定により /body の直前に配置) */}
        <script async src="https://adm.shinobi.jp/st/auto.js" data-admax-id="6940cf426d8b05585fbd28930455285d" suppressHydrationWarning />
      </body>
    </html>
  );
}
