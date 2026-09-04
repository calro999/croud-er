import Link from "next/link";
import { Metadata } from "next";
import FanzaBanner from "../components/FanzaBanner";

export const metadata: Metadata = {
  title: "【2026年最新】FANZA動画はどうやって見る？対応デバイス一覧＆視聴方法完全ガイド | 背徳の深夜書斎",
  description: "【初心者向け】FANZA動画の全対応デバイス（パソコン、iPhone/iPad、Android、PS4/PS5、Fire TV Stick、Chromecast、スマートテレビ）の視聴方法・設定手順をわかりやすく解説！家族バレ防止策やおすすめ視聴環境、高画質で快適に楽しむテクニックも徹底網羅。",
  keywords: "FANZA 見る方法, FANZA 対応デバイス, FANZA テレビ 見方, FANZA PS5, FANZA Fire TV Stick, FANZA スマホ 再生, FANZA アプリ, DMM TV アプリ",
  alternates: {
    canonical: "https://haitoku.pages.dev/fanza-device-guide",
  },
  openGraph: {
    title: "【2026年最新】FANZA動画はどうやって見る？対応デバイス一覧＆視聴方法完全ガイド",
    description: "パソコン・スマホ・PS4/PS5・Fire TV・テレビアプリでの視聴手順から、購入時の注意点・家族バレ防止策まで徹底解説！",
    url: "https://haitoku.pages.dev/fanza-device-guide",
    siteName: "背徳の深夜書斎",
    type: "article",
  },
};

export default function FanzaDeviceGuidePage() {
  const articleSchema = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "【2026年最新】FANZA動画はどうやって見る？対応デバイス一覧＆視聴方法完全ガイド",
    "description": "FANZA動画の全対応デバイス（パソコン、iPhone/iPad、Android、PS4/PS5、Fire TV Stick、Chromecast、スマートテレビ）の視聴方法・設定手順を解説。",
    "author": {
      "@type": "Organization",
      "name": "背徳の深夜書斎 編集部",
      "url": "https://haitoku.pages.dev"
    },
    "publisher": {
      "@type": "Organization",
      "name": "背徳の深夜書斎",
      "url": "https://haitoku.pages.dev"
    },
    "mainEntityOfPage": "https://haitoku.pages.dev/fanza-device-guide"
  };

  const faqSchema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "iPhoneやAndroidのアプリから作品を直接買えないのはなぜですか？",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Apple（App Store）およびGoogle（Google Play）の規約により、公式アプリ内ではアダルト作品の販売・決済が禁止されているためです。作品の購入はSafariやChromeなどのWebブラウザで行い、購入後にアプリやブラウザで視聴する流れとなります。"
        }
      },
      {
        "@type": "Question",
        "name": "テレビでFANZAを見るには何が一番おすすめですか？",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "最も安価で設定が簡単なのは『Amazon Fire TV Stick』です。テレビのHDMI端子に挿してWi-Fiに接続し、『DMM TV』または『DMM.com』アプリをインストールするだけで、リモコン操作で大画面視聴が楽しめます。すでにPS4やPS5をお持ちなら、追加機器なしでそのまま視聴可能です。"
        }
      },
      {
        "@type": "Question",
        "name": "家族にバレずにテレビやスマホで視聴するコツはありますか？",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "テレビアプリでは視聴後にログアウトするか、プロフィール暗証番号ロックをかけておくのが有効です。スマホやPCではプライベートブラウズモード（シークレットモード）で購入・視聴するか、ブラウザの閲覧履歴・キャッシュを定期的に削除することをおすすめします。"
        }
      }
    ]
  };

  const devices = [
    {
      name: "スマートフォン・タブレット",
      targets: "iOS (iPhone) / iPadOS / Android",
      icon: "📱",
      badge: "手軽さNo.1",
      badgeColor: "bg-blue-600",
      desc: "ベッドの中や自室、移動先でも手軽に視聴可能。ブラウザでそのままストリーミング再生できるほか、アプリへダウンロードしておけば通信量を気にせずオフライン再生できます。",
      steps: [
        "SafariやChromeなどのWEBブラウザでFANZAにアクセス・ログインして作品を購入",
        "購入後、ブラウザ上の『購入済み商品』からワンタップで即ストリーミング再生",
        "外出先やオフラインで見る場合は公式動画プレイヤーアプリにダウンロード"
      ],
      notice: "App StoreやGoogle Playのアプリ内ではアダルト作品の購入ができません。購入手続きは必ずWEBブラウザで行いましょう。"
    },
    {
      name: "パソコン (PC)",
      targets: "Windows / Mac (Chrome, Safari, Edge等)",
      icon: "💻",
      badge: "高画質＆操作性抜群",
      badgeColor: "bg-emerald-600",
      desc: "大画面モニターで高ビットレートの迫力映像を堪能。シークバー操作、10秒スキップ、倍速再生、チャプタージャンプがマウスやキーボードで最も快適に行えます。",
      steps: [
        "WEBブラウザでFANZA公式サイトにログイン",
        "マイリストや『購入済み商品』から作品を選んで『再生する』をクリック",
        "専用ソフトなしでブラウザ上でそのまま高画質フルスクリーン鑑賞"
      ],
      notice: "家族共有PCの場合は、プライベートウィンドウでの利用または視聴後のブラウザ履歴・Cookie削除を徹底しましょう。"
    },
    {
      name: "PlayStation 4 / 5",
      targets: "PS4 / PS4 Pro / PS5 / PS5 Pro",
      icon: "🎮",
      badge: "ゲーマーなら追加投資ゼロ",
      badgeColor: "bg-indigo-600",
      desc: "プレステをお持ちなら、追加のストリーミング機器を買う必要はありません。強力な描画性能により、4K対応作品や高画質ストリーミングもカクつきなく滑らかに描写されます。",
      steps: [
        "PlayStation Networkの『PlayStation Store』を開く",
        "無料の『DMM TV』アプリを検索してダウンロード・インストール",
        "アプリを起動し、画面に表示される案内に従ってDMM/FANZAアカウントでログイン",
        "コントローラーで作品を選んですぐに大画面テレビで再生"
      ],
      notice: "DualSenseやDUALSHOCKコントローラーで早送り・巻き戻しも直感的に操作可能です。"
    },
    {
      name: "ストリーミング端末",
      targets: "Amazon Fire TV Stick / Chromecast with Google TV",
      icon: "📺",
      badge: "テレビ鑑賞で最もおすすめ",
      badgeColor: "bg-rose-600",
      desc: "テレビのHDMI端子に挿すだけで、自室やリビングの液晶テレビがFANZA専用シアターに早変わり。専用リモコンで片手操作できる快適性は一度味わうと戻れません。",
      steps: [
        "テレビのHDMI端子に端末を接続し、Wi-Fi設定を完了",
        "アプリストア（Amazon Appstore / Google Play）から『DMM TV』アプリを検索してインストール",
        "アプリを起動し、スマホでQRコードを読み取るかログインID/PASSを入力して連携",
        "購入済みライブラリからリモコン操作で再生スタート"
      ],
      notice: "同居人がいるご家庭では、テレビアプリの起動時PINコードロックを有効にしておくと安心です。"
    },
    {
      name: "スマートテレビ",
      targets: "Android TV搭載テレビ / 各社スマートTV (DMM TV・DMM.comアプリ対応機種)",
      icon: "🖥️",
      badge: "外付け機器不要",
      badgeColor: "bg-amber-600",
      desc: "テレビ本体にアプリストアが内蔵されているスマートテレビなら、スティック機器やゲーム機を挿す必要すらありません。テレビ付属のリモコンひとつで完結します。",
      steps: [
        "テレビのホーム画面からアプリ一覧（Google Play等）を開く",
        "『DMM TV』または『DMM.com』アプリをインストール",
        "お持ちのFANZAアカウントでログインし、購入済み作品を再生"
      ],
      notice: "メーカーや型番（年式）によって『DMM TV』または『DMM.com』のどちらが配信されているかが異なります。"
    }
  ];

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(articleSchema) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema) }}
      />

      <div className="space-y-8 max-w-4xl mx-auto">
        {/* パンくずリスト */}
        <nav className="flex items-center gap-1.5 text-xs font-medium text-slate-500" aria-label="パンくずリスト">
          <Link href="/" className="hover:text-rose-600 transition-colors">ホーム</Link>
          <span className="text-slate-300">›</span>
          <Link href="/features" className="hover:text-rose-600 transition-colors">特集一覧</Link>
          <span className="text-slate-300">›</span>
          <span className="text-slate-700 font-bold">FANZA対応デバイス・視聴ガイド</span>
        </nav>

        {/* 記事メインコンテナ */}
        <article className="bg-white border border-slate-200/80 rounded-3xl p-6 md:p-12 shadow-sm space-y-10">
          
          {/* ヘッダーエリア */}
          <header className="space-y-4 border-b border-slate-100 pb-8">
            <div className="flex flex-wrap items-center gap-2">
              <span className="bg-rose-600 text-white text-[10px] font-black tracking-widest px-3 py-1 rounded-full uppercase shadow-sm">
                📖 初心者向け完全マニュアル
              </span>
              <span className="bg-emerald-100 text-emerald-900 border border-emerald-200 text-[10px] font-bold px-2.5 py-0.5 rounded-full">
                2026年最新対応表
              </span>
              <span className="text-xs text-slate-400 font-medium ml-auto">
                読了目安: 4分
              </span>
            </div>

            <h1 className="text-2xl md:text-4xl font-black text-slate-900 leading-tight tracking-tight">
              【2026年最新】FANZA動画はどうやって見る？対応デバイス一覧＆視聴方法完全ガイド
            </h1>

            <p className="text-sm md:text-base text-slate-600 leading-relaxed">
              「FANZAで動画を買ったけど、どの端末で見られる？」「テレビの大画面やプレステでも再生できる？」<br />
              そんな疑問を持つ初心者のために、全対応デバイス別の再生手順から、最も快適な視聴環境の選び方、家族バレを防ぐ鉄則まで分かりやすく解説します。
            </p>
          </header>

          {/* 導入セクション */}
          <section className="space-y-4 text-slate-700 text-sm md:text-base leading-relaxed">
            <p>
              国内最大手のアダルト配信プラットフォームである<strong>FANZA（DMM）</strong>は、パソコンやスマホだけでなく、リビングのテレビや最新ゲーム機まで多彩な視聴デバイスに対応しています。
            </p>
            <p>
              「手元のスマホでこっそり見たい」「テレビの超大型スクリーンとスピーカーで迫力の没入感を味わいたい」など、好みのスタイルに合わせて自由に選べるのが大きな強みです。
            </p>

            <div className="bg-gradient-to-r from-rose-50 to-amber-50 border-l-4 border-rose-500 p-5 rounded-r-2xl my-6">
              <h3 className="text-slate-900 font-black text-base mb-2">💡 初心者がまず覚えるべき重要鉄則：</h3>
              <p className="text-slate-800 text-sm leading-relaxed">
                <strong>『購入はスマホやPCのWEBブラウザで行い、見るのは好きなデバイス（アプリやテレビ）を使う』</strong><br />
                この基本ルールさえ知っていれば、アプリ内課金の制限やトラブルに迷うことは一切ありません。
              </p>
            </div>

            {/* CTA 1回目：見放題ch誘導バナー */}
            <div className="my-8 py-6 px-4 bg-slate-50 border border-slate-200 rounded-2xl flex flex-col items-center justify-center text-center space-y-3 shadow-inner">
              <span className="text-xs font-bold text-rose-600 bg-rose-100 px-3 py-1 rounded-full">
                ▼ 月額定額で人気作が見放題！まずは対象作品をチェック ▼
              </span>
              <FanzaBanner bannerId="164_300_250" affiliateId="onchan555-003" width={300} height={250} />
              <div className="pt-2">
                <a
                  href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fmonthly%2Fpremium%2F&af_id=onchan555-003&ch=toolbar"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-rose-600 to-red-600 hover:from-rose-500 hover:to-red-500 text-white font-extrabold text-sm rounded-xl shadow-md transition transform hover:-translate-y-0.5"
                >
                  <span>🔥</span>
                  <span>FANZA見放題chの全対応作品を見る（公式）</span>
                  <span>→</span>
                </a>
              </div>
            </div>
          </section>

          {/* セクション1：対応デバイス早見表 */}
          <section className="space-y-4">
            <h2 className="text-xl md:text-2xl font-black text-slate-900 border-l-4 border-rose-600 pl-3.5 leading-none">
              1. FANZA動画の全対応デバイス一覧・早見表
            </h2>
            <p className="text-slate-700 text-sm md:text-base leading-relaxed">
              現在、FANZA動画（単品購入・月額見放題ch）の再生を公式サポートしている機器一覧です。
            </p>

            <div className="overflow-x-auto my-4">
              <table className="w-full text-left border-collapse border border-slate-200 text-xs md:text-sm">
                <thead>
                  <tr className="bg-slate-100 text-slate-800 font-bold border-b border-slate-200">
                    <th className="p-3">デバイス</th>
                    <th className="p-3">対応機種・OS</th>
                    <th className="p-3">視聴方法</th>
                    <th className="p-3">おすすめ度</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-200">
                  <tr>
                    <td className="p-3 font-bold text-slate-900">パソコン (PC)</td>
                    <td className="p-3 text-slate-600">Windows / macOS</td>
                    <td className="p-3 text-slate-600">Webブラウザ（Chrome/Safari等）</td>
                    <td className="p-3 font-bold text-amber-600">★★★★★</td>
                  </tr>
                  <tr>
                    <td className="p-3 font-bold text-slate-900">スマホ / タブレット</td>
                    <td className="p-3 text-slate-600">iOS (iPhone) / iPadOS / Android</td>
                    <td className="p-3 text-slate-600">Webブラウザ / 公式動画プレイヤー</td>
                    <td className="p-3 font-bold text-amber-600">★★★★★</td>
                  </tr>
                  <tr>
                    <td className="p-3 font-bold text-slate-900">ゲーム機</td>
                    <td className="p-3 text-slate-600">PS4 / PS4 Pro / PS5 / PS5 Pro</td>
                    <td className="p-3 text-slate-600">DMM TVアプリ（PS Store）</td>
                    <td className="p-3 font-bold text-amber-600">★★★★☆</td>
                  </tr>
                  <tr>
                    <td className="p-3 font-bold text-slate-900">ストリーミング端末</td>
                    <td className="p-3 text-slate-600">Fire TV端末 / Chromecast with Google TV</td>
                    <td className="p-3 text-slate-600">テレビ版DMM TVアプリ</td>
                    <td className="p-3 font-bold text-amber-600">★★★★★</td>
                  </tr>
                  <tr>
                    <td className="p-3 font-bold text-slate-900">スマートテレビ</td>
                    <td className="p-3 text-slate-600">Android TV搭載テレビ / 各社スマートTV</td>
                    <td className="p-3 text-slate-600">DMM TVアプリ / DMM.comアプリ</td>
                    <td className="p-3 font-bold text-amber-600">★★★★☆</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </section>

          {/* セクション2：デバイス別詳細ガイド */}
          <section className="space-y-6">
            <h2 className="text-xl md:text-2xl font-black text-slate-900 border-l-4 border-rose-600 pl-3.5 leading-none">
              2. 【デバイス別】おすすめ視聴手順とメリット・注意点
            </h2>

            <div className="space-y-6">
              {devices.map((dev, idx) => (
                <div key={idx} className="bg-slate-50 border border-slate-200/90 rounded-2xl p-5 md:p-7 space-y-4 shadow-sm">
                  <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-200 pb-3">
                    <div className="flex items-center gap-2">
                      <span className="text-2xl">{dev.icon}</span>
                      <h3 className="text-lg md:text-xl font-black text-slate-900">{dev.name}</h3>
                    </div>
                    <div className="flex items-center gap-2">
                      <span className="text-[10px] text-slate-500 font-bold bg-white px-2 py-0.5 rounded border border-slate-200">
                        {dev.targets}
                      </span>
                      <span className={`text-white text-[10px] font-black px-2.5 py-0.5 rounded-full ${dev.badgeColor}`}>
                        {dev.badge}
                      </span>
                    </div>
                  </div>

                  <p className="text-slate-700 text-sm leading-relaxed">
                    {dev.desc}
                  </p>

                  <div className="bg-white rounded-xl p-4 border border-slate-200 space-y-2">
                    <h4 className="text-xs font-black text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                      <span>📌</span><span>視聴までのステップ</span>
                    </h4>
                    <ol className="list-decimal list-inside text-xs md:text-sm text-slate-600 space-y-1.5 leading-relaxed pl-1">
                      {dev.steps.map((step, sIdx) => (
                        <li key={sIdx}>{step}</li>
                      ))}
                    </ol>
                  </div>

                  <div className="bg-amber-50 border border-amber-200/80 rounded-xl p-3 text-xs text-amber-900 flex items-start gap-2">
                    <span className="text-base flex-shrink-0">⚠️</span>
                    <div>
                      <strong>注意点・ポイント：</strong> {dev.notice}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </section>

          {/* セクション3：シーン別のおすすめ環境選び */}
          <section className="space-y-4">
            <h2 className="text-xl md:text-2xl font-black text-slate-900 border-l-4 border-rose-600 pl-3.5 leading-none">
              3. あなたに最適な視聴環境はどれ？利用スタイル別診断
            </h2>
            <p className="text-slate-700 text-sm md:text-base leading-relaxed">
              どの方法で見ればいいか迷っている方は、以下のスタイルに合わせて選ぶのがベストです。
            </p>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 my-4">
              <div className="bg-white border-2 border-slate-200 p-5 rounded-2xl space-y-2 text-center hover:border-rose-400 transition">
                <span className="text-3xl block mb-1">🛌</span>
                <h3 className="font-extrabold text-slate-900 text-sm">ベッドで手軽に楽しみたい</h3>
                <p className="text-xs text-slate-600 leading-relaxed">
                  <strong>スマホ＋イヤホン</strong>の一択。誰にも邪魔されず、寝転がりながらサクッと楽しめます。
                </p>
              </div>

              <div className="bg-white border-2 border-rose-500/50 p-5 rounded-2xl space-y-2 text-center shadow-md bg-gradient-to-b from-rose-50/30 to-white">
                <span className="text-3xl block mb-1">👑</span>
                <h3 className="font-extrabold text-slate-900 text-sm">迫力の大画面で没入したい</h3>
                <p className="text-xs text-slate-600 leading-relaxed">
                  <strong>Fire TV Stick 4K または PS5</strong>。女優の息遣いや肌の質感までテレビの大画面で圧倒的に堪能できます。
                </p>
              </div>

              <div className="bg-white border-2 border-slate-200 p-5 rounded-2xl space-y-2 text-center hover:border-rose-400 transition">
                <span className="text-3xl block mb-1">🖥️</span>
                <h3 className="font-extrabold text-slate-900 text-sm">お気に入りシーンを厳選したい</h3>
                <p className="text-xs text-slate-600 leading-relaxed">
                  <strong>パソコン（PCモニター）</strong>。キーボードでの秒単位スキップや倍速再生を駆使して一番効率よく抜けます。
                </p>
              </div>
            </div>
          </section>

          {/* セクション4：同居人・家族バレを防ぐセキュリティ対策 */}
          <section className="space-y-4">
            <h2 className="text-xl md:text-2xl font-black text-slate-900 border-l-4 border-rose-600 pl-3.5 leading-none">
              4. 家族・同居人バレを防ぐ！安心視聴の3大防衛テクニック
            </h2>
            <p className="text-slate-700 text-sm md:text-base leading-relaxed">
              特にリビングのテレビや共有PCを使う場合、履歴や画面が家族に見られないよう以下の対策を講じておきましょう。
            </p>

            <div className="space-y-3">
              <div className="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-1">
                <h3 className="text-sm font-black text-slate-900">① テレビアプリは「視聴後のログアウト」または「暗証番号ロック」</h3>
                <p className="text-xs text-slate-600 leading-relaxed">
                  Fire TVやスマートテレビのDMM TVアプリには、アプリ起動時やアダルトジャンル表示時に暗証番号（PIN）を要求する保護設定があります。リビングのテレビに導入する場合は必ず設定しておきましょう。
                </p>
              </div>

              <div className="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-1">
                <h3 className="text-sm font-black text-slate-900">② スマホ・PCは「シークレットモード」で購入・閲覧</h3>
                <p className="text-xs text-slate-600 leading-relaxed">
                  SafariのプライベートブラウズやChromeのシークレットウィンドウを使えば、検索履歴・閲覧履歴・Cookieが端末に残るのを防げます。
                </p>
              </div>

              <div className="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-1">
                <h3 className="text-sm font-black text-slate-900">③ Bluetoothイヤホン・ヘッドホンの接続確認</h3>
                <p className="text-xs text-slate-600 leading-relaxed">
                  深夜にテレビやスマホで視聴する際、Bluetoothのペアリングが外れてスピーカーから大音量で音声が漏れるトラブルを防ぐため、再生前に必ず音量レベルと接続状態を確認しましょう。
                </p>
              </div>
            </div>
          </section>

          {/* よくある質問 (FAQ) */}
          <section className="space-y-4">
            <h2 className="text-xl md:text-2xl font-black text-slate-900 border-l-4 border-rose-600 pl-3.5 leading-none">
              5. FANZA動画の視聴に関するよくある質問（Q&A）
            </h2>

            <div className="space-y-3">
              <div className="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-1.5">
                <h3 className="text-sm font-black text-slate-900 flex items-center gap-2">
                  <span className="text-rose-600 font-black">Q.</span>
                  <span>iPhoneのアプリストアで「FANZA」と検索しても出てきません。</span>
                </h3>
                <p className="text-xs md:text-sm text-slate-600 leading-relaxed pl-6">
                  <strong>A.</strong> App StoreやGoogle Playでは成人向けアプリの直接配信が規制されています。公式プレイヤーは「DMM動画プレイヤー」などの名称で配信されているほか、購入はSafari等のブラウザからFANZAサイトへアクセスして行います。
                </p>
              </div>

              <div className="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-1.5">
                <h3 className="text-sm font-black text-slate-900 flex items-center gap-2">
                  <span className="text-rose-600 font-black">Q.</span>
                  <span>同じアカウントで複数の端末から同時に見ることはできますか？</span>
                </h3>
                <p className="text-xs md:text-sm text-slate-600 leading-relaxed pl-6">
                  <strong>A.</strong> 1つのアカウントで複数端末での同時ストリーミング再生は原則できません。ただし、事前ダウンロードした作品であればオフラインで同時鑑賞が可能です。
                </p>
              </div>

              <div className="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-1.5">
                <h3 className="text-sm font-black text-slate-900 flex items-center gap-2">
                  <span className="text-rose-600 font-black">Q.</span>
                  <span>一度買った作品は、後から別のデバイスでも見られますか？</span>
                </h3>
                <p className="text-xs md:text-sm text-slate-600 leading-relaxed pl-6">
                  <strong>A.</strong> はい。購入した作品はあなたのアカウントの「ライブラリ（購入済み商品）」に永久保存されるため、PCで買った作品をスマホやテレビ、PS5で何度でも再生できます。
                </p>
              </div>
            </div>
          </section>

          {/* まとめ＆最終CTAコンテナ */}
          <footer className="pt-8 border-t border-slate-200 space-y-6">
            <div className="bg-gradient-to-br from-slate-900 to-rose-950 text-white rounded-3xl p-6 md:p-10 shadow-xl space-y-5 text-center">
              <span className="text-xs font-bold text-amber-400 bg-amber-400/10 border border-amber-400/20 px-3 py-1 rounded-full uppercase tracking-wider">
                CONCLUSION • まとめ
              </span>
              <h3 className="text-xl md:text-3xl font-black tracking-tight">
                お好みのデバイスで、今夜最高の動画体験を！
              </h3>
              <p className="text-xs md:text-sm text-slate-300 leading-relaxed max-w-2xl mx-auto">
                FANZAなら、スマホ・PC・テレビ・ゲーム機の中からあなたの生活スタイルに合わせた自由な視聴が可能です。<br />
                まずは公式ページで気になる作品や見放題対象タイトルをチェックして、極上の鑑賞環境を整えてみてください！
              </p>

              {/* 最終CTAボタン群 */}
              <div className="pt-4 flex flex-col sm:flex-row items-center justify-center gap-4">
                <a
                  href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2F&af_id=onchan555-003&ch=toolbar"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-full sm:w-auto px-8 py-4 bg-gradient-to-r from-rose-600 to-red-600 hover:from-rose-500 hover:to-red-500 text-white font-black text-sm md:text-base rounded-2xl shadow-lg transition transform hover:-translate-y-0.5 flex items-center justify-center gap-2"
                >
                  <span>🎬</span>
                  <span>FANZA動画 公式サイトで最新作をチェック</span>
                  <span>→</span>
                </a>
                <Link
                  href="/fanza-tv-plus"
                  className="w-full sm:w-auto px-6 py-4 bg-white/10 hover:bg-white/20 border border-white/20 text-white font-bold text-sm md:text-base rounded-2xl transition flex items-center justify-center gap-2"
                >
                  <span>🔥</span>
                  <span>定額で見放題にしたいならこちら（レビュー）</span>
                </Link>
              </div>
            </div>

            {/* 回遊内部リンク */}
            <div className="pt-4 text-center">
              <Link href="/features" className="text-xs text-rose-600 hover:underline font-bold">
                ← 人気AV女優のおすすめ神作10選・特集一覧に戻る
              </Link>
            </div>
          </footer>

        </article>
      </div>
    </>
  );
}
