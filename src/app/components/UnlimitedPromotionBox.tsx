import Link from "next/link";
import FanzaBanner from "./FanzaBanner";

export default function UnlimitedPromotionBox() {
  return (
    <section className="my-10 overflow-hidden rounded-3xl bg-gradient-to-br from-slate-900 via-rose-950 to-slate-950 p-6 md:p-8 border-2 border-rose-500/40 shadow-2xl text-white">
      <div className="flex flex-col lg:flex-row items-center justify-between gap-8">
        
        {/* 左側：セールスコピー＆メリット */}
        <div className="space-y-4 max-w-xl text-left">
          <div className="flex items-center gap-2">
            <span className="bg-gradient-to-r from-amber-400 to-amber-600 text-slate-950 text-[10px] font-black tracking-widest px-3 py-1 rounded-full uppercase shadow">
              👑 コスパ最強・殿堂入り
            </span>
            <span className="bg-rose-500/20 border border-rose-500/30 text-rose-300 text-[10px] font-bold px-2.5 py-0.5 rounded-full">
              定額エロ動画サブスク
            </span>
          </div>

          <h3 className="text-xl md:text-2xl font-black text-white leading-snug tracking-tight">
            単品買いで損していませんか？<br />
            <span className="bg-gradient-to-r from-rose-200 via-pink-200 to-amber-200 bg-clip-text text-transparent">
              人気エロ動画が見放題の「FANZA見放題ch」
            </span>
          </h3>

          <p className="text-xs md:text-sm text-slate-300 leading-relaxed">
            1本2,000円〜3,500円の単品購入はもう卒業！月額定額で人気トップ単体女優の名作から最新作、VR、マニアック企画まで好きなだけ見放題。
          </p>

          <ul className="space-y-2 text-xs text-slate-200 font-medium">
            <li className="flex items-center gap-2">
              <span className="text-rose-400 font-bold">✔</span>
              <span><strong>圧倒的作品数</strong>：人気単体女優・大手レーベル・VRまで見放題！</span>
            </li>
            <li className="flex items-center gap-2">
              <span className="text-rose-400 font-bold">✔</span>
              <span><strong>ハズレ作品の損なし</strong>：好みに合わなければ即次の動画へスキップOK</span>
            </li>
            <li className="flex items-center gap-2">
              <span className="text-rose-400 font-bold">✔</span>
              <span><strong>縛り一切なし</strong>：スマホから3分で即視聴＆いつでもWebで解約可能</span>
            </li>
          </ul>

          <div className="pt-2 flex flex-col sm:flex-row gap-3">
            <Link
              href="/fanza-tv-plus"
              className="inline-flex items-center justify-center text-xs font-black text-white bg-gradient-to-r from-rose-600 to-pink-600 hover:from-rose-500 hover:to-pink-500 px-6 py-3.5 rounded-xl shadow-lg hover:shadow-rose-500/25 transition duration-200 text-center"
            >
              📖 見放題chの徹底本音レビューを見る ›
            </Link>
            <a
              href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F&af_id=onchan555-003"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center justify-center text-xs font-bold text-slate-300 hover:text-white bg-white/10 hover:bg-white/20 border border-white/20 px-5 py-3.5 rounded-xl transition text-center"
            >
              🎬 公式サイトを直接チェック
            </a>
          </div>
        </div>

        {/* 右側：300x250公式バナー */}
        <div className="flex-shrink-0 flex flex-col items-center justify-center p-3 bg-white/5 rounded-2xl border border-white/10 backdrop-blur-md">
          <span className="text-[10px] font-bold text-amber-300 mb-2">▼ 今すぐ見放題を体験 ▼</span>
          <FanzaBanner bannerId="164_300_250" affiliateId="onchan555-003" width={300} height={250} />
        </div>

      </div>
    </section>
  );
}
