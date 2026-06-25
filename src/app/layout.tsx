import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "【極上の悦楽】大人の深夜書斎 - 人妻・ネトラレ専門濃厚レビュー",
  description: "ネットの片隅で、熱狂的マニアが綴る人妻・ネトラレ・背徳系アダルト映像の超濃厚レビューサイト。感情的な心理描写と共におすすめの作品を紹介します。",
  keywords: ["人妻", "ネトラレ", "背徳", "不倫", "AVレビュー", "DMMアフィリエイト"],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ja" className="h-full dark">
      <body className="min-h-full flex flex-col bg-[#0a050d] text-gray-100 selection:bg-pink-600 selection:text-white">
        {/* グローバルヘッダー */}
        <header className="border-b border-[#2d123a] bg-[#120718]/90 backdrop-blur-md sticky top-0 z-50 py-4 px-6 shadow-lg">
          <div className="max-w-6xl mx-auto flex items-center justify-between">
            <a href="/" className="flex items-center gap-2">
              <span className="text-2xl font-black tracking-widest bg-gradient-to-r from-pink-500 to-purple-500 bg-clip-text text-transparent hover:from-pink-400 hover:to-purple-400 transition">
                深夜の背徳書斎
              </span>
            </a>
            <nav className="flex items-center gap-6 text-sm font-bold text-gray-300">
              <a href="/" className="hover:text-pink-500 transition">ホーム</a>
              <span className="text-[#3c1b4e]">|</span>
              <span className="text-xs bg-red-600 text-white font-black px-2.5 py-0.5 rounded-full uppercase tracking-wider animate-pulse">
                R-18
              </span>
            </nav>
          </div>
        </header>

        {/* メインコンテンツ */}
        <main className="flex-grow max-w-6xl w-full mx-auto px-4 py-8">
          {children}
        </main>

        {/* グローバルフッター */}
        <footer className="border-t border-[#2d123a] bg-[#07030a] py-8 text-center text-xs text-gray-500">
          <div className="max-w-6xl mx-auto px-4 flex flex-col gap-3">
            <p>© 2026 深夜の背徳書斎. All Rights Reserved. (18歳未満の閲覧は禁止されています)</p>
            <p className="text-gray-600 max-w-xl mx-auto">
              当サイトに掲載されているアフィリエイトリンクを経由して生じた売上は、今後のサイト運営と更なるニッチ作品の濃厚レビュー執筆に充てられます。
            </p>
          </div>
        </footer>
      </body>
    </html>
  );
}
