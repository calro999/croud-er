import Link from "next/link";
import { Metadata } from "next";
import FanzaBanner from "../components/FanzaBanner";
import fs from "fs";
import path from "path";

export const metadata: Metadata = {
  title: "【2026年最新】お得にAVを楽しむ完全攻略ガイド！エロ動画見放題ch・セール・単品購入のコスパを徹底比較 | 背徳の深夜書斎",
  description: "【2026年最新】「AVをお得に安く楽しみたい」「毎月のおかず代を賢く節約したい」男性必見！FANZA見放題ch、単品購入、割引セールのコスパ徹底比較から、危険な無料サイトの隠れた代償、性癖別の元が取れる活用術まで多角的に解説。今すぐ使えるお得技を完全網羅！",
  keywords: "お得にAVを楽しむ方法, エロ動画 お得, AV 安く見る方法, AV サブスク 比較, FANZA 見放題ch, エロ動画 コスパ, アダルト動画 節約, FANZA セール 比較, エロ動画 定額, AV おすすめ 見放題",
  alternates: {
    canonical: "https://haitoku.pages.dev/fanza-tv-plus",
  },
  openGraph: {
    title: "【2026年最新】お得にAVを楽しむ完全攻略ガイド！エロ動画見放題ch・セール・単品購入のコスパ徹底比較",
    description: "単品買いで毎月数万円溶かしていた筆者が、最もお得にエロ動画を楽しみ尽くす方法を暴露！無料サイトのリスク比較や最新おすすめ作品も掲載。",
    url: "https://haitoku.pages.dev/fanza-tv-plus",
    siteName: "背徳の深夜書斎",
    type: "article",
  },
};

interface ShowcaseItem {
  title: string;
  url: string;
  image: string;
  price: string;
  actress: string;
  maker: string;
}

export default function FanzaTvPlusPage() {
  // FANZA APIから直接取得した作品データを読み込み
  let showcaseData: Record<string, ShowcaseItem[]> = {};
  try {
    const jsonPath = path.join(process.cwd(), "public/data/featured_showcase.json");
    if (fs.existsSync(jsonPath)) {
      showcaseData = JSON.parse(fs.readFileSync(jsonPath, "utf-8"));
    }
  } catch (e) {
    console.error("Failed to read showcase data", e);
  }

  const articleSchema = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "【2026年最新】お得にAVを楽しむ完全攻略ガイド！エロ動画見放題ch・セール・単品購入のコスパを徹底比較",
    "description": "FANZA見放題ch、単品購入、割引セールのコスパ比較や、安全・お得にエロ動画を楽しむ方法を多角的に解説。",
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
    "mainEntityOfPage": "https://haitoku.pages.dev/fanza-tv-plus"
  };

  const faqSchema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "お得にAVを楽しむには、結局どの方法が一番安上がりですか？",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "視聴頻度によって最適解が異なります。月に2本以上観る方なら定額見放題（FANZA見放題ch）が最も1本あたりの単価が下がり圧倒的にお得です。年に数本しか観ない方は大型セール（10円〜500円セールなど）の単品買いが向いています。"
        }
      },
      {
        "@type": "Question",
        "name": "無料の海外エロ動画サイトで見るのと、有料公式サブスクは何が違いますか？",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "画質（HD/4Kの圧倒的な美しさ）、安全性（ウイルス・不正スクリプト・個人情報漏洩の危険性ゼロ）、再生快適性（怪しいポップアップや広告に邪魔されずノンストレス）、そしてフル尺本編で観られる点が決定的に違います。無料サイトを探す時間やリスクを考慮すると、公式サブスクの方が遥かに高コスパです。"
        }
      },
      {
        "@type": "Question",
        "name": "FANZA見放題chはスマホやタブレット、テレビでも見られますか？",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "はい、iPhone/iPad、Androidスマホ、PCブラウザはもちろん、Fire TV StickやChromecastを使えばご自宅の大型テレビでも高画質ストリーミング再生が可能です。"
        }
      },
      {
        "@type": "Question",
        "name": "1ヶ月だけお試しで利用して、すぐ解約することはできますか？",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "可能です。契約期間の縛りや違約金は一切ありません。マイページから24時間いつでも数クリックで簡単に解約手続きを行えます。"
        }
      },
      {
        "@type": "Question",
        "name": "クレジットカードの利用明細に『FANZA』や『エロ動画』などの名前は載りますか？",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "明細にはサービス名ではなく運営会社である『DMM.com』または決済代行名義で記載されるため、家族やパートナーに具体的な購入ジャンルがバレる心配はありません。"
        }
      }
    ]
  };

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
          <span className="text-slate-700 font-bold">お得にAVを楽しむ完全攻略ガイド</span>
        </nav>

        {/* 記事メインコンテナ */}
        <article className="bg-white border border-slate-200/80 rounded-3xl p-6 md:p-12 shadow-sm space-y-12">
          
          {/* ヘッダーエリア */}
          <header className="space-y-4 border-b border-slate-100 pb-8">
            <div className="flex flex-wrap items-center gap-2">
              <span className="bg-rose-600 text-white text-[10px] font-black tracking-widest px-3 py-1 rounded-full uppercase shadow-sm">
                👑 2026年完全保存版
              </span>
              <span className="bg-amber-100 text-amber-900 border border-amber-200 text-[10px] font-bold px-2.5 py-0.5 rounded-full">
                おかず代節約＆コスパ最大化
              </span>
              <span className="text-xs text-slate-400 font-medium ml-auto">
                読了目安: 5分
              </span>
            </div>

            <h1 className="text-2xl md:text-4xl font-black text-slate-900 leading-tight tracking-tight">
              【2026年最新】お得にAVを楽しむ完全攻略ガイド！エロ動画見放題ch・セール・単品購入のコスパを徹底比較
            </h1>

            <p className="text-sm md:text-base text-slate-600 leading-relaxed">
              「毎月のおかず代を賢く抑えたい」「怪しい無料動画サイトはリスクが怖くて卒業したい」——そんな男性のために、国内最大の公式プラットフォームをフル活用して<strong>最もお得に、かつ最高画質・安全にAVを楽しみ尽くす多角的なアプローチ</strong>を徹底解説します。
            </p>
          </header>

          {/* 導入セクション */}
          <section className="space-y-4 text-slate-700 text-sm md:text-base leading-relaxed">
            <div className="bg-slate-50 border border-slate-200 rounded-2xl p-5 space-y-2">
              <h2 className="text-base font-extrabold text-slate-900 flex items-center gap-2">
                <span>💡</span> あなたは今、こんな損やストレスを感じていませんか？
              </h2>
              <ul className="space-y-1.5 text-xs md:text-sm text-slate-700 list-disc list-inside">
                <li>気になる新作をポチポチ単品購入していたら、クレカの請求が毎月1〜2万円を超えていた…</li>
                <li>「パッケージ買い」したものの、肝心の本編が自分の性癖に刺さらず大後悔した経験がある…</li>
                <li>無料サイトを探し回っても画質はモザイクだらけ、怪しい詐欺広告やウイルス感染のリスクに怯えている…</li>
                <li>冒頭の10分だけ観て「違うな」と思っても、買ったお金が戻ってこないのが悔しい…</li>
              </ul>
            </div>

            <p>
              エロ動画を楽しむ方法は、ここ数年で劇的に進化しました。かつてのように「1本2,500円〜3,500円で買い切る」時代から、音楽や映画と同じように<strong>「公式サブスク（定額見放題）で賢くつまみ食いする」</strong>のが圧倒的な新常識となっています。
            </p>

            <div className="bg-rose-50 border-l-4 border-rose-500 p-4 rounded-r-xl my-4 text-rose-950 font-medium">
              🔥 <strong>ズバリ結論：</strong>「月に2本以上エロ動画を観ているなら、今すぐ定額見放題（FANZA見放題ch）に切り替えないと、年間で数万円〜十数万円を余計にドブに捨てている」状態です！
            </div>

            {/* バナー配置 1回目（導入直後・興味喚起） */}
            <div className="my-8 py-6 px-4 bg-slate-50 border border-slate-200 rounded-2xl flex flex-col items-center justify-center text-center space-y-3">
              <span className="text-xs font-bold text-rose-600 bg-rose-100 px-3 py-1 rounded-full">
                ▼ 今すぐ人気作をチェック！圧倒的ラインナップが見放題 ▼
              </span>
              <FanzaBanner bannerId="164_300_250" affiliateId="onchan555-003" width={300} height={250} />
              <p className="text-[11px] text-slate-500">※初回登録・最新の配信ラインナップは公式サイトで即確認できます</p>
            </div>
          </section>

          {/* セクション1：徹底比較シミュレーション */}
          <section className="space-y-4">
            <h2 className="text-xl md:text-2xl font-black text-slate-900 border-l-4 border-rose-600 pl-3.5 leading-none">
              1. 徹底比較！単品買い・大型セール・見放題chの年間出費シミュレーション
            </h2>
            <p className="text-slate-700 text-sm md:text-base leading-relaxed">
              エロ動画にお金をかけるとき、どの買い方が一番財布に優しいのでしょうか？「単品買い」「セール待ち買い」「定額見放題ch」の3つのパターンで比較検証してみましょう。
            </p>

            {/* 比較テーブル */}
            <div className="overflow-x-auto my-6 border border-slate-200 rounded-2xl shadow-sm">
              <table className="w-full text-left text-xs md:text-sm">
                <thead>
                  <tr className="bg-slate-900 text-white">
                    <th className="p-3.5 font-bold">比較項目</th>
                    <th className="p-3.5 font-bold">① 単品購入（都度買い）</th>
                    <th className="p-3.5 font-bold">② 大型セール狙い撃ち</th>
                    <th className="p-3.5 font-bold bg-rose-600 text-white">③ FANZA見放題ch（推奨）</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-200 bg-white">
                  <tr>
                    <td className="p-3.5 font-bold text-slate-800">1本あたりの価格目安</td>
                    <td className="p-3.5 text-slate-600">約2,000円〜3,500円</td>
                    <td className="p-3.5 text-slate-600">約100円〜1,000円（旧作中心）</td>
                    <td className="p-3.5 font-extrabold text-rose-600">観れば観るほど実質数十円〜数円！</td>
                  </tr>
                  <tr className="bg-slate-50">
                    <td className="p-3.5 font-bold text-slate-800">月5本観た場合の月額</td>
                    <td className="p-3.5 text-rose-600 font-bold">約12,000円〜17,500円</td>
                    <td className="p-3.5 text-slate-600">約2,500円〜5,000円</td>
                    <td className="p-3.5 font-extrabold text-rose-600">完全定額（何本観ても追加0円）</td>
                  </tr>
                  <tr>
                    <td className="p-3.5 font-bold text-slate-800">年間想定トータル出費</td>
                    <td className="p-3.5 text-rose-600 font-bold">約140,000円〜200,000円</td>
                    <td className="p-3.5 text-slate-600">約30,000円〜60,000円</td>
                    <td className="p-3.5 font-bold text-emerald-600">年間で十数万円以上の大幅節約に！</td>
                  </tr>
                  <tr className="bg-slate-50">
                    <td className="p-3.5 font-bold text-slate-800">「ハズレ」を引いたリスク</td>
                    <td className="p-3.5 text-rose-600">大損（お金も気分も激痛）</td>
                    <td className="p-3.5 text-slate-600">多少の損失（安物買いの銭失い）</td>
                    <td className="p-3.5 font-bold text-emerald-600">損失ゼロ（1秒で別作品に切り替え）</td>
                  </tr>
                  <tr>
                    <td className="p-3.5 font-bold text-slate-800">作品の選びやすさ</td>
                    <td className="p-3.5 text-slate-600">失敗が怖くて慎重になりがち</td>
                    <td className="p-3.5 text-slate-600">セール対象品に限定される</td>
                    <td className="p-3.5 font-bold text-emerald-600">気になったら即再生・自由無制限</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div className="bg-amber-50 border border-amber-200 p-4 rounded-2xl text-xs md:text-sm text-amber-950 space-y-1">
              <strong className="font-black text-amber-900">💡 「セール待ち」だけでは満たされない理由</strong>
              <p>
                「セールまで待って買えばいい」と思いがちですが、人気作や旬の単体女優作品が大幅値引きされるのは半年〜1年以上先になるケースがほとんどです。「今すぐシコりたい」「旬の女優の最高潮を観たい」という熱量を我慢するストレスを考えると、いつでも定額でライブラリを開放できる見放題chの優位性は圧倒的です。
              </p>
            </div>
          </section>

          {/* セクション2：無料サイトの隠れた代償 */}
          <section className="space-y-4">
            <h2 className="text-xl md:text-2xl font-black text-slate-900 border-l-4 border-rose-600 pl-3.5 leading-none">
              2. 「無料動画サイト」の隠れた代償！実は一番コストが高いって知ってた？
            </h2>
            <p className="text-slate-700 text-sm md:text-base leading-relaxed">
              「タダで見られるなら無料動画サイトで十分じゃないか」と考える方もいるかもしれません。しかし、無料サイトを利用することには、金銭以上の甚大な見えないコストやリスクが潜んでいます。
            </p>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 my-4">
              <div className="bg-rose-50/60 border border-rose-200 p-4 rounded-2xl space-y-2">
                <span className="text-2xl">⏳</span>
                <h3 className="font-extrabold text-slate-900 text-sm">時間の無駄遣い（探索コスト）</h3>
                <p className="text-xs text-slate-600 leading-relaxed">
                  「消去済み」「リンク切れ」「分割動画」に振り回され、気づけば1時間以上も探し回って賢者タイム…なんて経験はありませんか？ 公式なら検索1発・3秒で本編スタートです。
                </p>
              </div>

              <div className="bg-rose-50/60 border border-rose-200 p-4 rounded-2xl space-y-2">
                <span className="text-2xl">⚠️</span>
                <h3 className="font-extrabold text-slate-900 text-sm">ウイルス・個人情報漏洩のリスク</h3>
                <p className="text-xs text-slate-600 leading-relaxed">
                  悪質な広告からのワンクリック詐欺、不正マイニングスクリプト、クレカ情報窃取型マルウェアなど、スマホやPCを危険に晒す代償は月額料金より遥かに高額です。
                </p>
              </div>

              <div className="bg-rose-50/60 border border-rose-200 p-4 rounded-2xl space-y-2">
                <span className="text-2xl">📺</span>
                <h3 className="font-extrabold text-slate-900 text-sm">圧倒的な低画質＆カット編集</h3>
                <p className="text-xs text-slate-600 leading-relaxed">
                  無料サイトは帯域節約のためガビガビ画質で巨大モザイク、一番肝心なピストン場面がカットされていることも。公式の最高峰HD/4K超高画質とは興奮の次元が違います。
                </p>
              </div>
            </div>

            {/* バナー配置 2回目（安全性・快適性の訴求後CTA） */}
            <div className="my-8 py-6 px-4 bg-slate-50 border border-slate-200 rounded-2xl flex flex-col items-center justify-center text-center space-y-3">
              <span className="text-xs font-bold text-rose-600 bg-rose-100 px-3 py-1 rounded-full">
                ▼ ウイルス不安ゼロ＆最高画質！安全安心に抜くなら公式一択 ▼
              </span>
              <FanzaBanner bannerId="164_300_250" affiliateId="onchan555-003" width={300} height={250} />
            </div>
          </section>

          {/* セクション3：多角的な楽しみ方・性癖別元取り術 */}
          <section className="space-y-4">
            <h2 className="text-xl md:text-2xl font-black text-slate-900 border-l-4 border-rose-600 pl-3.5 leading-none">
              3. 性癖・スタイル別！見放題chで「確実に元を取る」多角的活用術
            </h2>
            <p className="text-slate-700 text-sm md:text-base leading-relaxed">
              FANZA見放題chは、あなたの性癖や好みのプレイスタイルに合わせて何通りもの楽しみ方ができます。
            </p>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 my-4">
              <div className="bg-slate-50 border border-slate-200 p-5 rounded-2xl space-y-2">
                <div className="flex items-center gap-2">
                  <span className="text-xl">💎</span>
                  <h3 className="font-extrabold text-slate-900 text-sm">トップ単体女優の代表作をコンプリート</h3>
                </div>
                <p className="text-xs text-slate-600 leading-relaxed">
                  S1やMOODYZ、アイデアポケットなどに所属する超人気女優の過去作・出世作・激ヤバ企画まで一挙に網羅。お気に入りの女優を1人決めて、出演作を片っ端から制覇する贅沢なマラソンが定額で可能です。
                </p>
              </div>

              <div className="bg-slate-50 border border-slate-200 p-5 rounded-2xl space-y-2">
                <div className="flex items-center gap-2">
                  <span className="text-xl">🔍</span>
                  <h3 className="font-extrabold text-slate-900 text-sm">素人・ハメ撮り・フェチの「つまみ食い」</h3>
                </div>
                <p className="text-xs text-slate-600 leading-relaxed">
                  人妻、巨乳、美脚、痴女、アナル、レズ、マジックミラー号など、単品買いでは「もしハズれたら…」と躊躇してしまうディープな性癖ジャンルも、見放題ならノーリスクで心ゆくまで開拓できます。
                </p>
              </div>

              <div className="bg-slate-50 border border-slate-200 p-5 rounded-2xl space-y-2">
                <div className="flex items-center gap-2">
                  <span className="text-xl">🥽</span>
                  <h3 className="font-extrabold text-slate-900 text-sm">超没入！VR専用動画で目の前に召喚</h3>
                </div>
                <p className="text-xs text-slate-600 leading-relaxed">
                  VRゴーグル（Meta Quest等）やスマホ用VRゴーグルを装着すれば、女優の吐息や体温まで伝わってきそうな超臨場感VRが見放題対象に多数ラインナップ。自宅の部屋が一瞬でプライベート空間に変わります。
                </p>
              </div>

              <div className="bg-slate-50 border border-slate-200 p-5 rounded-2xl space-y-2">
                <div className="flex items-center gap-2">
                  <span className="text-xl">⚡</span>
                  <h3 className="font-extrabold text-slate-900 text-sm">シコりシーン直行のチャプター再生</h3>
                </div>
                <p className="text-xs text-slate-600 leading-relaxed">
                  「前置きのストーリーやインタビューはいらない、今すぐ本番シーンだけ観たい！」という時も、見放題ならチャプター移動や倍速再生を駆使して最速で最高潮に到達できます。
                </p>
              </div>
            </div>
          </section>

          {/* セクション4：FANZA API連携・人気作ラインナップ実例 */}
          {Object.keys(showcaseData).length > 0 && (
            <section className="space-y-6">
              <div className="border-l-4 border-rose-600 pl-3.5">
                <h2 className="text-xl md:text-2xl font-black text-slate-900 leading-none">
                  4. 【リアルタイム取得】見放題chで今すぐ観たい注目おすすめ作品
                </h2>
                <p className="text-xs text-slate-500 mt-1">※FANZA公式APIより最新の人気作データを直接取得しています</p>
              </div>

              <div className="space-y-6">
                {Object.entries(showcaseData).map(([category, items], idx) => (
                  <div key={idx} className="space-y-3 bg-slate-50/70 border border-slate-200/80 p-5 rounded-2xl">
                    <h3 className="font-black text-slate-900 text-sm md:text-base flex items-center gap-2">
                      <span className="w-2 h-2 rounded-full bg-rose-600 inline-block"></span>
                      {category}
                    </h3>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                      {items.map((item, itemIdx) => (
                        <a
                          key={itemIdx}
                          href={item.url}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="group bg-white border border-slate-200 rounded-xl overflow-hidden shadow-sm hover:shadow-md hover:border-rose-300 transition-all flex flex-col"
                        >
                          <div className="aspect-[4/3] bg-slate-100 overflow-hidden relative">
                            {/* eslint-disable-next-line @next/next/no-img-element */}
                            <img
                              src={item.image}
                              alt={item.title}
                              className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                              loading="lazy"
                            />
                            <span className="absolute top-2 left-2 bg-slate-900/80 text-white text-[10px] font-bold px-2 py-0.5 rounded backdrop-blur-sm">
                              {item.maker}
                            </span>
                          </div>
                          <div className="p-3 flex-1 flex flex-col justify-between space-y-2">
                            <h4 className="text-xs font-bold text-slate-800 line-clamp-2 group-hover:text-rose-600 transition-colors">
                              {item.title}
                            </h4>
                            <div className="flex items-center justify-between text-[11px] pt-1 border-t border-slate-100">
                              <span className="text-rose-600 font-extrabold">{item.actress}</span>
                              <span className="text-slate-400">公式配信中</span>
                            </div>
                          </div>
                        </a>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </section>
          )}

          {/* セクション5：さらにお得に使う裏ワザ＆契約サイクル */}
          <section className="space-y-4">
            <h2 className="text-xl md:text-2xl font-black text-slate-900 border-l-4 border-rose-600 pl-3.5 leading-none">
              5. 賢い大人の節約術！見放題chをさらにお得に使い倒すテクニック
            </h2>
            <p className="text-slate-700 text-sm md:text-base leading-relaxed">
              定額見放題サービスをさらに賢く、1円も無駄にせず利用するためのプロの活用テクニックをご紹介します。
            </p>

            <div className="space-y-3 my-4">
              <div className="bg-slate-50 border border-slate-200/80 p-4 rounded-2xl flex items-start gap-3.5">
                <span className="bg-amber-500 text-white font-black text-xs px-2.5 py-1 rounded-lg shrink-0">裏ワザ 1</span>
                <div className="space-y-1">
                  <h3 className="font-extrabold text-slate-900 text-sm">連休や長期休暇だけの「スポット契約」もOK！</h3>
                  <p className="text-xs text-slate-600 leading-relaxed">
                    FANZA見放題chには「最低◯ヶ月継続」といった契約の縛りが一切ありません。年末年始、GW、お盆休み、あるいは仕事が一段落した月だけ1ヶ月契約し、飽きたら即マイページから解約すれば、わずかな出費で長期間楽しめます。
                  </p>
                </div>
              </div>

              <div className="bg-slate-50 border border-slate-200/80 p-4 rounded-2xl flex items-start gap-3.5">
                <span className="bg-amber-500 text-white font-black text-xs px-2.5 py-1 rounded-lg shrink-0">裏ワザ 2</span>
                <div className="space-y-1">
                  <h3 className="font-extrabold text-slate-900 text-sm">DMMポイント還元やPayPay決済の併用</h3>
                  <p className="text-xs text-slate-600 leading-relaxed">
                    DMMカードやキャンペーンで貯まったDMMポイント、またはPayPayポイント等を支払いに充当可能。普段のお買い物で貯まったポイントを使えば、実質タダ感覚で見放題を楽しむことも可能です。
                  </p>
                </div>
              </div>

              <div className="bg-slate-50 border border-slate-200/80 p-4 rounded-2xl flex items-start gap-3.5">
                <span className="bg-amber-500 text-white font-black text-xs px-2.5 py-1 rounded-lg shrink-0">裏ワザ 3</span>
                <div className="space-y-1">
                  <h3 className="font-extrabold text-slate-900 text-sm">テレビの大画面・Fire TV Stickで鑑賞環境を最大化</h3>
                  <p className="text-xs text-slate-600 leading-relaxed">
                    スマホの小さな画面だけで観るのはもったいない！Fire TV StickやChromecastをリビングのテレビに挿せば、大迫力・高画質で鑑賞可能。家族が留守の間の至福の時間を劇的にアップグレードできます。
                  </p>
                </div>
              </div>
            </div>
          </section>

          {/* セクション6：登録・解約手順 */}
          <section className="space-y-4">
            <h2 className="text-xl md:text-2xl font-black text-slate-900 border-l-4 border-rose-600 pl-3.5 leading-none">
              6. わずか3分で即視聴！登録＆解約手順も超カンタン
            </h2>
            <p className="text-slate-700 text-sm md:text-base leading-relaxed">
              大手DMMグループの公式サービスのため、手続きは極めて明瞭。煩わしい手続きや解約時の引き止めアンケートなどもありません。
            </p>

            <div className="space-y-3 my-4">
              <div className="flex items-start gap-3 bg-slate-50 p-4 rounded-2xl border border-slate-200/80">
                <span className="bg-rose-600 text-white font-black text-xs px-2.5 py-1 rounded-lg shrink-0">STEP 1</span>
                <div>
                  <h3 className="font-extrabold text-slate-900 text-sm">公式バナーリンクから見放題chへアクセス</h3>
                  <p className="text-xs text-slate-600 mt-1">本ページの公式リンクから見放題ch専用ページに進みます。</p>
                </div>
              </div>

              <div className="flex items-start gap-3 bg-slate-50 p-4 rounded-2xl border border-slate-200/80">
                <span className="bg-rose-600 text-white font-black text-xs px-2.5 py-1 rounded-lg shrink-0">STEP 2</span>
                <div>
                  <h3 className="font-extrabold text-slate-900 text-sm">DMMアカウントでログイン（または無料作成）</h3>
                  <p className="text-xs text-slate-600 mt-1">メールアドレスまたはGoogle/LINE連携ですぐに完了します。</p>
                </div>
              </div>

              <div className="flex items-start gap-3 bg-slate-50 p-4 rounded-2xl border border-slate-200/80">
                <span className="bg-rose-600 text-white font-black text-xs px-2.5 py-1 rounded-lg shrink-0">STEP 3</span>
                <div>
                  <h3 className="font-extrabold text-slate-900 text-sm">支払い方法を選択して登録完了！即視聴可能</h3>
                  <p className="text-xs text-slate-600 mt-1">クレジットカード、DMMポイント、PayPay、キャリア決済などに対応。完了した瞬間からすべての対象動画が見放題になります。</p>
                </div>
              </div>
            </div>

            <div className="bg-emerald-50 border border-emerald-200 p-4 rounded-2xl text-xs md:text-sm text-emerald-900">
              <strong>💡 解約もマイページからワンクリックでいつでも可能</strong><br />
              契約期間の縛りは一切ありません。「今月だけ楽しみたい」という場合も、マイページから24時間いつでも即座に解約できます。
            </div>
          </section>

          {/* セクション7：よくある質問 FAQ */}
          <section className="space-y-4">
            <h2 className="text-xl md:text-2xl font-black text-slate-900 border-l-4 border-rose-600 pl-3.5 leading-none">
              7. よくある質問（FAQ）
            </h2>

            <div className="space-y-3 my-4">
              <div className="bg-slate-50 border border-slate-200/80 p-4 rounded-2xl space-y-1.5">
                <h3 className="font-extrabold text-slate-900 text-sm flex items-center gap-2">
                  <span className="text-rose-600 font-black">Q.</span> お得にAVを楽しむには、結局どの方法が一番安上がりですか？
                </h3>
                <p className="text-xs text-slate-600 leading-relaxed pl-5">
                  視聴頻度によって最適解が異なります。月に2本以上観る方なら定額見放題（FANZA見放題ch）が最も1本あたりの単価が下がり圧倒的にお得です。年に数本しか観ない方は大型セール（10円〜500円セールなど）の単品買いが向いています。
                </p>
              </div>

              <div className="bg-slate-50 border border-slate-200/80 p-4 rounded-2xl space-y-1.5">
                <h3 className="font-extrabold text-slate-900 text-sm flex items-center gap-2">
                  <span className="text-rose-600 font-black">Q.</span> 無料動画サイトで見るのと、有料公式サブスクは何が違いますか？
                </h3>
                <p className="text-xs text-slate-600 leading-relaxed pl-5">
                  画質（HD/4Kの圧倒的な美しさ）、安全性（ウイルス・不正スクリプト・個人情報漏洩の危険性ゼロ）、再生快適性（怪しいポップアップや広告に邪魔されずノンストレス）、そしてフル尺本編で観られる点が決定的に違います。無料サイトを探す時間やリスクを考慮すると、公式サブスクの方が遥かに高コスパです。
                </p>
              </div>

              <div className="bg-slate-50 border border-slate-200/80 p-4 rounded-2xl space-y-1.5">
                <h3 className="font-extrabold text-slate-900 text-sm flex items-center gap-2">
                  <span className="text-rose-600 font-black">Q.</span> クレジットカードの明細にエロ動画やFANZAの名前は載りますか？
                </h3>
                <p className="text-xs text-slate-600 leading-relaxed pl-5">
                  明細にはサービス名ではなく『DMM.com』または決済代行名義で記載されるため、家族やパートナーに具体的な購入ジャンルがバレる心配はありません。
                </p>
              </div>

              <div className="bg-slate-50 border border-slate-200/80 p-4 rounded-2xl space-y-1.5">
                <h3 className="font-extrabold text-slate-900 text-sm flex items-center gap-2">
                  <span className="text-rose-600 font-black">Q.</span> 途中で解約した場合、違約金などは発生しますか？
                </h3>
                <p className="text-xs text-slate-600 leading-relaxed pl-5">
                  一切発生しません。契約期間の縛りはなく、マイページからいつでも数クリックで解約が可能です。
                </p>
              </div>
            </div>
          </section>

          {/* まとめ・最終クロージングCTA */}
          <section className="bg-gradient-to-br from-slate-900 via-rose-950 to-slate-900 p-6 md:p-10 rounded-3xl text-white text-center space-y-6 shadow-xl border border-slate-800">
            <span className="inline-block text-[10px] font-bold text-amber-400 bg-amber-400/10 border border-amber-400/20 px-3 py-1 rounded-full uppercase tracking-widest">
              CONCLUSION
            </span>
            <h2 className="text-xl md:text-3xl font-black tracking-tight">
              もう「ハズレ」や「おかず代」に怯える必要はありません
            </h2>
            <p className="text-xs md:text-sm text-slate-300 max-w-xl mx-auto leading-relaxed">
              怪しい無料動画サイトを探し回る時間とウイルスリスクから解放され、今夜から最高峰の画質と膨大なラインナップを心ゆくまで味わい尽くしましょう！
            </p>

            {/* バナー配置 3回目（最終クロージングCTA） */}
            <div className="pt-2 flex flex-col items-center justify-center space-y-3">
              <span className="text-xs font-black text-amber-300 bg-amber-950/80 border border-amber-500/30 px-4 py-1.5 rounded-full shadow">
                ＼ 迷ったらまずは登録！今すぐ極上の見放題体験をスタート ／
              </span>
              <div className="p-3 bg-white/5 rounded-2xl backdrop-blur-md border border-white/10">
                <FanzaBanner bannerId="164_300_250" affiliateId="onchan555-003" width={300} height={250} />
              </div>
              <p className="text-[11px] text-slate-400">※登録完了後、すぐに動画を視聴できます</p>
            </div>
          </section>

        </article>
      </div>
    </>
  );
}
