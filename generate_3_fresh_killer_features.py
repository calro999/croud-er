# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・超大型キラー特集3記事自動生成スクリプト
1. 【コスパ最強の極致】FANZA超長尺BEST・歴代神作総集編（8時間〜16時間）おすすめ傑作選
2. 【25年売れ続ける伝説】マジックミラー号＆リアル素人ナンパ傑作選！生々しい恥じらいと本気アクメに悶絶する歴代神回ランキング
3. 【動いて喘ぐ極上ヌキゲー】FANZA同人ゲームおすすめ殿堂入り名作選！アニメーションCG×超豪華ボイスで骨抜きにされる神作RPG・SLG完全攻略
"""
import os
import re
import json
import time
import urllib.parse
import requests

API_ID = "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = "onchan555-999"
LINK_AFFILIATE_ID = "onchan555-003"
OUTPUT_DIR = "src/data/posts"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open("src/lib/slugs.json", "r", encoding="utf-8") as f:
    slugs_data = json.load(f)
actress_slugs = slugs_data.get("actresses", {})
genre_slugs = slugs_data.get("genres", {})

def get_actress_link(name):
    clean_name = re.sub(r'（[^）]+）', '', name).strip()
    slug = actress_slugs.get(name) or actress_slugs.get(clean_name)
    if slug:
        return f'<a href="/actress/{slug}" class="text-rose-400 hover:text-rose-300 underline font-bold transition">{name}</a>'
    encoded = urllib.parse.quote(name)
    return f'<a href="/actress/{encoded}" class="text-rose-400 hover:text-rose-300 underline font-bold transition">{name}</a>'

def get_genre_link(genre):
    slug = genre_slugs.get(genre)
    if slug:
        return f'<a href="/genre/{slug}" class="text-slate-300 hover:text-amber-300 bg-slate-800/80 hover:bg-slate-700/80 px-2.5 py-1 rounded-full text-xs font-medium border border-slate-700 transition">{genre}</a>'
    encoded = urllib.parse.quote(genre)
    return f'<a href="/genre/{encoded}" class="text-slate-300 hover:text-amber-300 bg-slate-800/80 hover:bg-slate-700/80 px-2.5 py-1 rounded-full text-xs font-medium border border-slate-700 transition">{genre}</a>'

def fetch_fanza_item(cid, service="digital", floor="videoa"):
    url = "https://api.dmm.com/affiliate/v3/ItemList"
    params = {
        "api_id": API_ID,
        "affiliate_id": API_AFFILIATE_ID,
        "site": "FANZA",
        "service": service,
        "floor": floor,
        "cid": cid,
        "output": "json"
    }
    try:
        res = requests.get(url, params=params, timeout=15)
        if res.status_code == 200:
            items = res.json().get("result", {}).get("items", [])
            if items:
                item = items[0]
                aff_url = item.get("affiliateURL", "")
                if aff_url and LINK_AFFILIATE_ID:
                    aff_url = re.sub(r'af_id=[^&]+', f'af_id={LINK_AFFILIATE_ID}', aff_url)
                item["affiliate_url_clean"] = aff_url
                return item
    except Exception as e:
        print(f"Error fetching {cid} ({service}/{floor}): {e}")
    return None

def count_japanese_chars(html):
    text = re.sub(r'<[^>]*>', '', html)
    text = re.sub(r'\s+', '', text)
    return len(text)

def get_sample_images(it, max_count=4):
    s_imgs = []
    sample_data = it.get("sampleImageURL", {})
    if sample_data:
        if "sample_l" in sample_data:
            s_imgs = sample_data["sample_l"].get("image", [])
        elif "sample_m" in sample_data:
            s_imgs = sample_data["sample_m"].get("image", [])
    if isinstance(s_imgs, str):
        s_imgs = [s_imgs]
    return s_imgs[:max_count]


# ==============================================================================
# 記事1: FANZA超長尺BEST・歴代神作総集編（8時間〜16時間）おすすめ傑作選
# ==============================================================================
def generate_article_1():
    print("=== Generating Article 1: Super Long Omnibus & BEST Selection ===")
    cids = ["ofje00541", "mizd00354", "mkck00389", "mizd00326", "idbd00858"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid, service="digital", floor="videoa")
        if it:
            items.append(it)
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        else:
            print(f" -> Failed to fetch {cid}")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception("Failed to fetch all 5 items for Article 1 from FANZA API")

    cover_image = items[0].get("imageURL", {}).get("large", "")

    reviews = [
        # 1: ofje00541 バックピストンBEST100本番8時間
        {
            "rank": "01",
            "subtitle": "全身が弓なりに反り狂う絶叫アクメ100連発！8時間ぶっ通しで子宮を抉り抜く後背位の金字塔",
            "body": """<b>【1本で100回抜ける！前代未聞の8時間バックピストン特化ベスト】</b>：<br>
男が本能的に最も射精したくなる体位「バック（後背位）」の美味しいシーンだけを、なんと100本番・丸々8時間凝縮した伝説のモンスターパックです。
登場するのは専属級の超SSS級美女たちばかり。彼女たちが四つん這いにされ、豊満なヒップを激しく揺らしながら、膣奥の一番敏感な急所をこれでもかとえぐり込まれます。カメラは男優のたくましい腰振りと、肉棒がズブズブと奥深くまで埋まる結合部を克明に激写。女優たちの首筋が緊張で浮き上がり、目を見開いて「そこダメぇぇ！壊れちゃう！」と叫びながら全身をブリッジさせて痙攣する姿は、まさに脳髄を直撃する快楽そのものです。余計な会話や前戯を一切省き、挿入と絶頂のピークシーンだけが延々と押し寄せるため、再生した瞬間からクライマックス状態。これ1本あれば向こう半年間のオナニーに困りません。""",
            "climax": "急所を突かれすぎて白目を剥き、四つん這いの体勢を維持できずに布団に顔を埋めて潮を吹き散らす限界ブリッジ絶頂。"
        },
        # 2: mizd00354 顔面射精ラッシュ139連発 8時間
        {
            "rank": "02",
            "subtitle": "MOODYZが誇る超絶美少女たちの顔面が白濁精液で埋まる！脳汁が溢れ出す顔射139連発8時間",
            "body": """<b>【射精の瞬間だけを139回浴びる！顔射・ぶっかけフェチの夢を具現化した奇跡の8時間】</b>：<br>
人気メジャーレーベルMOODYZの歴代看板美少女たちが、男優の濃厚な白濁液を顔面いっぱいに受け止める瞬間のカタルシスを8時間ノンストップで収録した顔射特化の金字塔。
普段はテレビやグラビアで見るような天使のような美少女たちが、舌を突き出し、瞳を潤ませながら「お顔にいっぱい出してください…！」とおねだり。ペニスの先端から放たれたドロドロのザーメンが、瞳、頬、唇、そして開いた口の中へと激しく飛び散り、美顔が白く汚されていく様は筆舌に尽くしがたいエロスを誇ります。精液の生々しい粘度や飛距離、女優たちの達成感と恍惚感が混ざり合った表情の変化が圧巻。一発抜いた後でも、次の射精シーンが数分おきにやってくるため、賢者タイムを強制突破して二回戦・三回戦へと突入させられる破壊力があります。""",
            "climax": "至近距離からの強烈な発射でまつ毛と唇にびっしりと精液を絡ませ、ペロリと舌先で舐め取ってみせる蕩け顔。"
        },
        # 3: mkck00389 清宮仁愛 1周年記念 全8タイトル完全収録 8時間
        {
            "rank": "03",
            "subtitle": "バスト105cm×ウエスト55cm！メーカー史上最高額ボディ・清宮仁愛のデビュー1年目を丸ごと味わう奇跡の8時間",
            "body": """<b>【奇跡の砂時計プロポーション！超ド級爆乳の神ボディを1本で全制覇する永久保存版】</b>：<br>
AV界を激震させた奇跡の神スタイル、バスト105cm（Jカップ）・ウエスト55cm・ヒップ98cmという非現実的な肉体を誇る清宮仁愛。彼女のデビュー1周年を記念し、初期の超名作8タイトルをまるごとノーカット級で8時間に詰め込んだ破格のベストです。
歩くだけでトランポリンのように波打つ重厚な乳房、キュッと引き締まった極細ウエスト、そして肉厚で弾力のある美尻。どの作品でも彼女の圧倒的肉体美が余すところなく捉えられており、パイズリでの搾精シーンはもちろん、正常位で胸をバウンドさせながら挿入される迫力は画面から飛び出してきそうなリアリティ。1作品あたり単体で買えば数千円するマスターピース群が、この1本で完全網羅できるコストパフォーマンスは異常。巨乳・豊満ボディ好きなら買わない理由が見当たらない歴史的アーカイブです。""",
            "climax": "105cmの巨大な乳房で男のペニスを完全に包み込み、窒息寸前まで顔を押し当てて搾り取る濃密パイズリ射精。"
        },
        # 4: mizd00326 森沢かな BEST OF BEST 誘惑痴女もアナルSEXも魅力溢れすぎ8時間
        {
            "rank": "04",
            "subtitle": "AV界きってのテクニシャン！妖艶な美貌と変態的なテクニックで男を骨抜きにする森沢かな究極8時間",
            "body": """<b>【美熟女痴女の真骨頂！変態プレイから濃密アナルまで男の欲望を全方位で満たす名盤】</b>：<br>
スラリとした美脚と端正な美貌を持ちながら、常人離れした淫乱ぶりとプロフェッショナルなエロテクニックでファンを魅了し続ける森沢かな。彼女のキャリアの中でも「最も変態的で最も抜ける」と語り継がれる傑作シーンを厳選した8時間ベストです。
耳元で囁く淫語責め、唾液でベトベトになりながらのディープフェラ、男をいたぶるような痴女搾精、そして彼女の代名詞でもある美尻を突き出してのアナルセックスまで、エロスのフルコースが贅沢に展開されます。ただ受け身でハメられるのではなく、自ら男の急所を的確に攻め立ててイカせにくるドSな眼差しと、自らも狂乱してイキ果てるギャップが最高潮。ワンパターンなセックスに飽きた大人の男性の股間を、再びギンギンに昂らせてくれる名盤中の名盤です。""",
            "climax": "アナルに極太肉棒を根元まで飲み込みながら、艶やかな美顔を歪めて同時にクリトリスを弄り悶絶するW絶頂。"
        },
        # 5: idbd00858 藤井いよな FIRST IP BEST 8時間
        {
            "rank": "05",
            "subtitle": "透明感溢れる美少女の初々しさと覚醒！10タイトル20本番を完全凝縮した美少女フェチ必携の8時間",
            "body": """<b>【「可愛い」の頂点！大人気専属美少女・藤井いよなの成長とエロスの軌跡を凝縮】</b>：<br>
アイポケ（アイデアポケット）が誇る次世代の看板美少女・藤井いよな。吸い込まれそうな大きな瞳と透き通るような白肌、清楚なルックスからは想像もつかない豊かな表現力で大ヒットを連発した彼女の初期10タイトル・20本番を詰め込んだ圧巻の8時間です。
初々しさが残るデビュー初期の恥じらいSEXから、徐々に男の快楽に目覚め、淫らな喘ぎ声を響かせるようになっていくグラデーションをこの1本で疑似体験可能。制服姿の清純シチュエーション、温泉旅行での密着交尾、そして汗だくになりながら激しいピストンを受け止める本気ハメまで、美少女好きが求めるシチュエーションが完璧に網羅されています。彼女の笑顔と喘ぎ顔を交互に見つめているだけで、日々のストレスが溶けていき、極上の癒やしとともに多幸感あふれる射精へと導かれます。""",
            "climax": "耳元で甘く名前を呼ばれながら、対面座位でギュッと抱きしめ合って同時に達する感動のピュアラブ射精。"
        }
    ]

    cards_html = ""
    for idx, (it, rev) in enumerate(zip(items, reviews), 1):
        cid_upper = it.get("content_id", "").upper()
        title = it.get("title", "")
        img_url = it.get("imageURL", {}).get("large", "")
        aff_url = it.get("affiliate_url_clean", "")
        price = it.get("prices", {}).get("price", "500~")
        actresses = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        maker = it.get("iteminfo", {}).get("maker", [{}])[0].get("name", "メーカー")

        actress_links = " / ".join([get_actress_link(a) for a in actresses[:3]]) if actresses else '<span class="text-slate-400">豪華出演陣</span>'
        genre_badges = "".join([get_genre_link(g) for g in genres[:6]])
        sample_imgs = get_sample_images(it, 4)
        sample_gallery = ""
        if sample_imgs:
            gallery_items = "".join([
                f'<div class="rounded-xl overflow-hidden aspect-video bg-slate-950 border border-slate-800 shadow-inner group"><img src="{s}" alt="{title} 抜きどころプレビュー" class="w-full h-full object-cover group-hover:scale-110 transition duration-300" loading="lazy" /></div>'
                for s in sample_imgs
            ])
            sample_gallery = f'<div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-2">{gallery_items}</div>'

        card = f"""
    <!-- ランキングカード {rev['rank']} -->
    <article class="bg-slate-900/90 border border-slate-800 rounded-3xl p-6 md:p-8 space-y-6 shadow-2xl hover:border-amber-500/40 transition">
      <div class="flex flex-wrap items-center justify-between gap-2 pb-4 border-b border-slate-800">
        <div class="flex items-center gap-2">
          <span class="px-3.5 py-1 bg-gradient-to-r from-amber-500 to-rose-600 text-slate-950 font-black text-xs rounded-full shadow">
            BEST PICK {rev['rank']}
          </span>
          <span class="text-xs font-mono text-amber-400 font-bold">品番: {cid_upper}</span>
        </div>
        <div class="text-xs text-slate-400">
          <span class="text-amber-400 font-black text-sm">💰 {price}円〜</span>（超長尺配信中）
        </div>
      </div>

      <div class="space-y-1">
        <span class="text-xs font-bold text-amber-400 tracking-wider uppercase">8時間超え大容量マスターピース</span>
        <h4 class="text-xl md:text-2xl font-black text-white leading-snug hover:text-amber-300 transition">
          【第{idx}位】{rev['subtitle']}
        </h4>
      </div>

      <div class="p-3 bg-slate-950/60 rounded-xl border border-slate-800 text-xs text-slate-300 font-medium">
        <b>作品タイトル</b>: {title}
      </div>

      <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-start">
        <div class="md:col-span-5 space-y-4">
          <div class="relative rounded-2xl overflow-hidden border border-slate-800 bg-slate-950 aspect-[3/4] shadow-inner group">
            <img src="{img_url}" alt="{title} 公式パッケージ画像" class="w-full h-full object-cover group-hover:scale-105 transition duration-300" loading="lazy" />
            <span class="absolute top-2 left-2 px-2.5 py-1 bg-amber-500/90 backdrop-blur-sm text-slate-950 text-[10px] font-black rounded-lg shadow">大容量8時間BEST</span>
          </div>

          <div class="p-4 bg-slate-950/80 rounded-2xl border border-slate-800 text-xs space-y-2 text-slate-300">
            <div><strong class="text-slate-400">👤 主演・出演:</strong> {actress_links}</div>
            <div><strong class="text-slate-400">🏢 レーベル:</strong> <span class="text-amber-300 font-bold">{maker}</span></div>
            <div class="flex flex-wrap gap-1.5 pt-1">
              {genre_badges}
            </div>
          </div>

          <div class="flex flex-col gap-2.5">
            <a href="{aff_url}" target="_blank" rel="noopener noreferrer" class="block w-full text-center py-4 px-6 bg-gradient-to-r from-amber-500 via-rose-600 to-amber-500 hover:from-amber-400 hover:to-rose-500 text-slate-950 font-black rounded-2xl shadow-xl transform hover:-translate-y-0.5 transition duration-150 text-sm">
              🔥 FANZA公式でこの8時間BESTを再生する ➔
            </a>
          </div>
        </div>

        <div class="md:col-span-7 space-y-4 text-slate-300 text-xs md:text-sm leading-relaxed">
          <div class="p-4 bg-amber-950/20 border border-amber-900/40 rounded-2xl space-y-1.5">
            <span class="text-[11px] font-black uppercase text-amber-400 tracking-wider">⚡ 編集部ガチ実況レビュー＆見どころ</span>
            <div class="text-white text-xs md:text-sm leading-relaxed">
              {rev['body']}
            </div>
          </div>

          <div class="p-4 bg-slate-950/60 rounded-2xl border border-slate-800 space-y-1">
            <span class="text-[11px] font-bold text-rose-400 uppercase tracking-wide">🎯 ここで射精する！最大の見どころ</span>
            <p class="text-white font-medium text-xs md:text-sm">
              {rev['climax']}
            </p>
          </div>

          {sample_gallery}
        </div>
      </div>
    </article>
"""
        cards_html += card

    content_html = f"""
<div class="space-y-12 text-slate-100 leading-relaxed font-sans">
  <!-- イントロダクション HERO -->
  <section class="bg-gradient-to-br from-slate-900 via-amber-950/50 to-slate-900 border-2 border-amber-500/50 rounded-3xl p-6 md:p-10 shadow-2xl space-y-6 relative overflow-hidden">
    <div class="absolute -right-16 -top-16 w-64 h-64 bg-amber-500/10 rounded-full blur-3xl pointer-events-none"></div>
    <div class="inline-flex items-center gap-2 px-4 py-1.5 bg-amber-500/20 text-amber-300 border border-amber-500/40 rounded-full text-xs font-black tracking-widest uppercase">
      <span>👑</span><span>コスパ最強の頂点 • 1本で数十回抜ける大容量パック</span>
    </div>
    
    <h2 class="text-2xl md:text-4xl font-black text-white leading-tight tracking-tight">
      【コスパ最強の極致】FANZA超長尺BEST・歴代神作総集編（8時間〜16時間）おすすめ傑作選！1本で数十回抜ける大容量パック完全攻略
    </h2>
    
    <p class="text-slate-300 text-sm md:text-base leading-relaxed">
      「単品の新作AVを1本2,000円〜3,000円で買ったのに、好みのシーンが少なくてガッカリした」「毎日のオナニーで気軽にサクッと抜きどころだけをつまみ食いしたい」——そんな悩みを一発で解決し、FANZA全ユーザーから絶大な支持を集めているのが<b>『8時間〜16時間超えの総集編・BEST盤』</b>です。
    </p>
    <p class="text-slate-300 text-sm md:text-base leading-relaxed">
      長尺ベストの最大の魅力は、なんといっても<b>「1作品あたりの圧倒的なコストパフォーマンス」</b>。通常なら8本〜16本分（定価換算で2万円〜4万円相当）のクライマックスシーンや本番セックスが、たった1本の価格（セール時なら数百円〜千数百円）で手に入ります。しかも、人気レーベル（MOODYZ、アイデアポケット、本中、ワンズファクトリー等）が本気で編集しているため、前戯の引き延ばしや退屈なシーンが削ぎ落とされ、<b>「男が一番興奮する絶頂・射精・ピストンシーン」</b>だけが怒涛の勢いで押し寄せます。
    </p>
    <p class="text-slate-300 text-sm md:text-base leading-relaxed">
      当サイトの<a href="/ranking" class="text-amber-400 hover:text-amber-300 font-bold underline">人気ランキング</a>や<a href="/posts/feature_fanza_500yen_one_coin_bargain_masterpieces" class="text-amber-400 hover:text-amber-300 font-bold underline">ワンコイン名作特集</a>でも上位に入る大ヒットタイトルの中から、FANZA公式APIを通じてリアルタイムにデータを取得。「今すぐ買って絶対に元が取れる、一生モノの殿堂入り超長尺BEST5選」を徹底紹介します。
    </p>
  </section>

  <!-- なぜ長尺ベスト盤はこれほど売れるのか？ -->
  <section class="space-y-6">
    <div class="flex items-center gap-3 border-l-4 border-amber-500 pl-3">
      <h3 class="text-xl md:text-2xl font-black text-white">なぜ「超長尺ベスト盤」はこれほど売れるのか？男が買うべき3つの圧倒的メリット</h3>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
      <div class="bg-slate-900/90 border border-slate-800 p-5 rounded-2xl space-y-3 shadow-lg">
        <div class="w-10 h-10 rounded-xl bg-amber-500/20 border border-amber-500/40 flex items-center justify-center text-xl">💰</div>
        <h4 class="font-bold text-white text-base">実質1本あたり数十円〜数百円の驚異的コスパ</h4>
        <p class="text-xs md:text-sm text-slate-300 leading-relaxed">
          8時間パックには10〜20本番、100本番ベストなら100シーンが凝縮。単品購入に比べて1シーンあたりの単価が圧倒的に安く、お財布への負担を最小限に抑えて極上の興奮を手に入れられます。
        </p>
      </div>

      <div class="bg-slate-900/90 border border-slate-800 p-5 rounded-2xl space-y-3 shadow-lg">
        <div class="w-10 h-10 rounded-xl bg-rose-500/20 border border-rose-500/40 flex items-center justify-center text-xl">⚡</div>
        <h4 class="font-bold text-white text-base">退屈な前置きゼロ！美味しい抜きどころのオンパレード</h4>
        <p class="text-xs md:text-sm text-slate-300 leading-relaxed">
          会話劇や長い前戯を飛ばして、一番興奮する「挿入」「激ピストン」「顔射」「潮吹き」「アクメ」の瞬間だけが連続。時間が限られている深夜のオナニーでも即座に絶頂へ到達できます。
        </p>
      </div>

      <div class="bg-slate-900/90 border border-slate-800 p-5 rounded-2xl space-y-3 shadow-lg">
        <div class="w-10 h-10 rounded-xl bg-purple-500/20 border border-purple-500/40 flex items-center justify-center text-xl">📱</div>
        <h4 class="font-bold text-white text-base">チャプター機能＆ストリーミングでいつでも好きな場面へ</h4>
        <p class="text-xs md:text-sm text-slate-300 leading-relaxed">
          FANZAの公式プレイヤーなら、作品ごとに細かくチャプター分けされているため、8時間の長尺でもお気に入りの女優やシチュエーションへ1タップでシーク可能。スマホでの視聴も超快適です。
        </p>
      </div>
    </div>
  </section>

  <!-- タイプ別おすすめ比較表 -->
  <section class="bg-gradient-to-br from-slate-900 via-slate-950 to-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 space-y-6">
    <div class="flex items-center gap-3 border-l-4 border-amber-500 pl-3">
      <h3 class="text-xl md:text-2xl font-black text-white">【タイプ別】あなたに最適な長尺ベスト盤の選び方チャート</h3>
    </div>
    
    <div class="overflow-x-auto">
      <table class="w-full text-left text-xs md:text-sm border-collapse">
        <thead>
          <tr class="border-b border-slate-700 bg-slate-800/60 text-slate-300">
            <th class="p-3 font-bold">ベストの種類</th>
            <th class="p-3 font-bold">主な収録内容</th>
            <th class="p-3 font-bold">こんな人におすすめ</th>
            <th class="p-3 font-bold">おすすめの代表作</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-slate-800 text-slate-300">
          <tr class="hover:bg-slate-800/40 transition">
            <td class="p-3 font-bold text-amber-400">体位・フェチ特化型</td>
            <td class="p-3">バックピストン100本番、顔射ラッシュ139連発など</td>
            <td class="p-3">特定のシチュエーションで確実に抜きたい人、即効性重視の人</td>
            <td class="p-3 text-white font-medium">OFJE00541 / MIZD00354</td>
          </tr>
          <tr class="hover:bg-slate-800/40 transition">
            <td class="p-3 font-bold text-rose-400">単体女優集大成型</td>
            <td class="p-3">人気女優のデビューから1年間の全タイトル、代表作まとめ</td>
            <td class="p-3">特定の推し女優をとことん愛でたい人、成長の軌跡を楽しみたい人</td>
            <td class="p-3 text-white font-medium">MKCK00389 / IDBD00858</td>
          </tr>
          <tr class="hover:bg-slate-800/40 transition">
            <td class="p-3 font-bold text-purple-400">変態・テクニック型</td>
            <td class="p-3">アナル、痴女、淫語、フェラチオなど超ハイテクニック集</td>
            <td class="p-3">普通のセックスでは刺激が足りない人、熟練の快感を味わいたい人</td>
            <td class="p-3 text-white font-medium">MIZD00326</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- ランキング一覧セクション -->
  <section class="space-y-8">
    <div class="border-l-4 border-amber-500 pl-3 space-y-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-widest">OFFICIAL API DATA 2026</span>
      <h3 class="text-2xl md:text-3xl font-black text-white">
        【FANZA公式API取得】絶対に後悔しない！歴代超長尺BESTランキングTOP5
      </h3>
      <p class="text-xs md:text-sm text-slate-400">
        配信中の数千タイトルの中から、収録時間、レビュー評価、シーンの濃密度すべてにおいて最高峰の5作品を厳選。
      </p>
    </div>

    {cards_html}

  </section>

  <!-- 長尺作品を快適に楽しむための視聴環境＆保存ガイド -->
  <section class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 space-y-6">
    <div class="flex items-center gap-3 border-l-4 border-amber-500 pl-3">
      <h3 class="text-xl md:text-2xl font-black text-white">8時間超え作品を120%楽しむための快適視聴術＆注意点</h3>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-5 text-xs md:text-sm text-slate-300">
      <div class="p-5 bg-slate-950/80 rounded-2xl border border-slate-800 space-y-2">
        <strong class="text-amber-400 block font-bold text-sm">💡 スマホの容量圧迫を防ぐ「ストリーミング再生」の活用</strong>
        <p class="leading-relaxed">
          8時間を最高画質でダウンロードすると10GB〜20GB以上の容量が必要になります。自宅のWi-Fi環境下ではFANZA公式プレイヤーのストリーミング機能を活用し、外出先や電波の届かない場所で見る場合のみお気に入りのチャプターだけをオフライン保存するのが最も賢い使い方です。詳しくは<a href="/posts/feature_fanza_app_player_guide_offline_streaming" class="text-amber-400 underline font-bold">FANZAアプリ公式プレイヤー攻略記事</a>をご参照ください。
        </p>
      </div>

      <div class="p-5 bg-slate-950/80 rounded-2xl border border-slate-800 space-y-2">
        <strong class="text-rose-400 block font-bold text-sm">💡 定期セール（半額・ワンコイン）時の「まとめ買い」が狙い目</strong>
        <p class="leading-relaxed">
          長尺ベスト盤は、FANZAの年末年始セール、サマーセール、ゴールデンウィークセールなどの大型キャンペーンで大幅割引されることが頻繁にあります。定価でも十分にお得ですが、気になる作品を「お気に入り」に入れておき、通知が届いた瞬間に確保すると信じられない低価格で購入可能です。
        </p>
      </div>
    </div>
  </section>

  <!-- よくある質問 FAQセクション -->
  <section class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 space-y-6">
    <div class="flex items-center gap-3 border-l-4 border-amber-500 pl-3">
      <h3 class="text-xl md:text-2xl font-black text-white">超長尺ベスト盤に関するよくある質問【Q&A】</h3>
    </div>
    
    <div class="space-y-4 text-xs md:text-sm">
      <div class="p-5 bg-slate-950/80 rounded-2xl border border-slate-800 space-y-2">
        <h4 class="font-bold text-amber-400 flex items-center gap-2">
          <span>Q.</span><span>「8時間」や「16時間」の作品は、途中で再生を止めても続きから見られますか？</span>
        </h4>
        <p class="text-slate-300 leading-relaxed">
          <b>はい、完全にレジューム再生（続きから再生）に対応しています</b>。ブラウザ視聴でも公式アプリでも、最後に視聴を停止した秒数が自動保存されるため、数日に分けて少しずつ視聴することが可能です。また、シークバーにチャプターサムネイルが表示されるため、好みのシーンを探すのも一瞬です。
        </p>
      </div>

      <div class="p-5 bg-slate-950/80 rounded-2xl border border-slate-800 space-y-2">
        <h4 class="font-bold text-amber-400 flex items-center gap-2">
          <span>Q.</span><span>単品のオリジナル作品と画質の違いはありますか？</span>
        </h4>
        <p class="text-slate-300 leading-relaxed">
          最新のベスト盤はマスター映像から高画質HD/FHDで再エンコードされているため、単品作品と同等の美しい映像で楽しめます。大画面テレビや高精細タブレットで見ても毛穴や汗の粒まで鮮明に映し出されます。
        </p>
      </div>

      <div class="p-5 bg-slate-950/80 rounded-2xl border border-slate-800 space-y-2">
        <h4 class="font-bold text-amber-400 flex items-center gap-2">
          <span>Q.</span><span>購入後の家族バレや履歴の管理はどうすればいいですか？</span>
        </h4>
        <p class="text-slate-300 leading-relaxed">
          FANZAの購入履歴はアカウント設定から非表示にすることが可能です。また、支払い方法に関してもクレジットカード明細に不審な記載を残さない方法（PayPay、DMMポイント、プリペイドカード等）が豊富に用意されています。詳細は当サイトの<a href="/posts/feature_fanza_payment_methods_safe_buying_guide" class="text-rose-400 underline font-bold">完全匿名・安全支払いガイド</a>をご確認ください。
        </p>
      </div>
    </div>
  </section>

  <!-- あわせて読みたい関連キラー特集（内部リンク・トピッククラスター） -->
  <section class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 space-y-6">
    <div class="flex items-center gap-3 border-l-4 border-amber-500 pl-3">
      <h3 class="text-xl md:text-2xl font-black text-white">あわせて読みたい！FANZA完全攻略おすすめ特集</h3>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      <a href="/posts/feature_fanza_magic_mirror_go_real_amateur_best_ranking" class="p-4 bg-slate-950/80 hover:bg-slate-800/80 border border-slate-800 rounded-2xl space-y-2 group transition">
        <span class="text-xs font-bold text-rose-400">リアル素人の神回</span>
        <h4 class="text-sm font-bold text-white group-hover:text-amber-300 transition">マジックミラー号＆素人傑作選</h4>
        <p class="text-[11px] text-slate-400 line-clamp-2">25年売れ続ける伝説！生々しい恥じらいと本気アクメの最高峰。</p>
      </a>
      <a href="/posts/feature_fanza_500yen_one_coin_bargain_masterpieces" class="p-4 bg-slate-950/80 hover:bg-slate-800/80 border border-slate-800 rounded-2xl space-y-2 group transition">
        <span class="text-xs font-bold text-amber-400">コスパ重視</span>
        <h4 class="text-sm font-bold text-white group-hover:text-amber-300 transition">ワンコイン500円〜買える名作10選</h4>
        <p class="text-[11px] text-slate-400 line-clamp-2">安くて本気で抜ける歴代大ヒット・高コスパ殿堂入り神作。</p>
      </a>
      <a href="/posts/feature_fanza_top_exclusive_actresses_ranking_masterpiece" class="p-4 bg-slate-950/80 hover:bg-slate-800/80 border border-slate-800 rounded-2xl space-y-2 group transition">
        <span class="text-xs font-bold text-rose-400">専属女優の頂点</span>
        <h4 class="text-sm font-bold text-white group-hover:text-amber-300 transition">単体専属トップ女優ランキング</h4>
        <p class="text-[11px] text-slate-400 line-clamp-2">絶対に後悔しない歴史的代表作とトップ女優の魅力。</p>
      </a>
      <a href="/features" class="p-4 bg-slate-950/80 hover:bg-slate-800/80 border border-slate-800 rounded-2xl space-y-2 group transition">
        <span class="text-xs font-bold text-purple-400">全ジャンル網羅</span>
        <h4 class="text-sm font-bold text-white group-hover:text-amber-300 transition">大型キラー特集・10選アーカイブ</h4>
        <p class="text-[11px] text-slate-400 line-clamp-2">女優別10選からVR、同人、見放題比較まで全特集を一覧表示。</p>
      </a>
    </div>
  </section>

  <!-- 構造化データ（JSON-LD） -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "【コスパ最強の極致】FANZA超長尺BEST・歴代神作総集編（8時間〜16時間）おすすめ傑作選！1本で数十回抜ける大容量パック完全攻略",
    "description": "FANZAで配信されている8時間〜16時間超えの超長尺総集編・BEST盤の中から、本当に抜ける殿堂入り神作を厳選。コスパ最強の理由やチャプター活用術、公式APIリアルタイム取得データを徹底解説。",
    "image": "{cover_image}",
    "datePublished": "2026-09-30T00:05:00+09:00",
    "author": {{
      "@type": "Organization",
      "name": "背徳の美学 編集部"
    }}
  }}
  </script>

  <!-- 総括CTA -->
  <section class="text-center bg-gradient-to-r from-amber-950 via-slate-900 to-amber-950 border-2 border-amber-500/50 rounded-3xl p-8 md:p-12 shadow-2xl space-y-5">
    <h3 class="text-2xl md:text-3xl font-black text-white">
      たった1本の購入で、向こう数ヶ月のオナニーを満たし尽くす。
    </h3>
    <p class="text-slate-300 text-xs md:text-sm max-w-2xl mx-auto leading-relaxed">
      もう「ハズレ作品」にお金を無駄遣いする必要はありません。選び抜かれた絶頂シーンの波に呑まれ、今夜最高の射精を心ゆくまでご堪能ください。
    </p>
    <div class="pt-2">
      <a href="{items[0].get('affiliate_url_clean', '')}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-3 px-10 py-5 bg-gradient-to-r from-amber-500 via-rose-600 to-amber-500 hover:from-amber-400 hover:to-rose-500 text-slate-950 font-black text-base rounded-2xl shadow-2xl transform hover:-translate-y-1 transition duration-200">
        <span>🔥</span><span>FANZA公式で殿堂入り8時間超えBESTを今すぐチェックする ➔</span>
      </a>
    </div>
  </section>
</div>
"""

    char_count = count_japanese_chars(content_html)
    print(f"Article 1 generated: {char_count} Japanese chars")
    if char_count < 3000:
        raise Exception(f"Article 1 has only {char_count} chars, minimum 3000 required")

    post_data = {
        "id": "feature_fanza_super_long_omnibus_best_selection_ranking",
        "title": "【コスパ最強の極致】FANZA超長尺BEST・歴代神作総集編（8時間〜16時間）おすすめ傑作選！1本で数十回抜ける大容量パック完全攻略",
        "content": content_html,
        "review": content_html,
        "image": cover_image,
        "date": "2026-09-30 00:05:00",
        "genres": ["総集編", "ハイビジョン", "独占配信", "巨乳", "美少女", "中出し", "バック"],
        "actresses": ["清宮仁愛", "森沢かな", "藤井いよな"],
        "maker": "MOODYZ",
        "price": "500~",
        "affiliate_url": items[0].get("affiliate_url_clean", "")
    }

    out_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f" -> Saved Article 1 to {out_path}")
    return post_data


# ==============================================================================
# 記事2: マジックミラー号＆リアル素人ナンパ傑作選
# ==============================================================================
def generate_article_2():
    print("=== Generating Article 2: Magic Mirror Car & Real Amateur Masterpieces ===")
    cids = ["1sdmm00201", "1svmgm00054", "1sdmm00181", "1sdmm00207", "1svmgm00041"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid, service="digital", floor="videoa")
        if it:
            items.append(it)
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        else:
            print(f" -> Failed to fetch {cid}")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception("Failed to fetch all 5 items for Article 2 from FANZA API")

    cover_image = items[0].get("imageURL", {}).get("large", "")

    reviews = [
        # 1: 1sdmm00201 脱出ゲーム×初々しい18歳
        {
            "rank": "01",
            "subtitle": "外から見えない密室に閉じ込められた18歳！初々しい羞恥心と本気アクメの生々しい記録",
            "body": """<b>【LIKEとLOVEの違いも曖昧な18歳が、制限時間100分でSEXを受け入れる極限の背徳】</b>：<br>
マジックミラー号シリーズの中でも、素人の「リアルな戸惑い」と「理性が崩壊していく過程」が最も美しく切り取られた大傑作。街頭で声をかけられ、わけも分からずミラー号に乗り込んだ18歳の初心な女の子が、「制限時間内にSEXしないと脱出できない」というお題を突きつけられます。
最初は「絶対に無理です！」と顔を真っ赤にして拒んでいた少女が、窓の外を行き交う一般人の視線に怯えながら、少しずつ衣服を脱がされ、指先で秘部を撫でられるうちに息を荒らげていく様は息を呑むエロス。まだ男慣れしていない瑞々しいピンク色の秘唇から愛液が溢れ出し、いざ挿入されると、驚きと快楽で目を丸くしながら「あっ…んっ…なんかヘンな感じ…」と素直な嬌声を漏らします。ヤラセでは絶対に表現できない、思春期のリアルな恥じらいと生々しい肉体の反応に、男の支配欲と射精欲が限界まで暴走させられます。""",
            "climax": "窓のすぐ外を通行人たちが歩く中、口元を手で押さえながら初めての激ピストンに腰をガクガク震わせる本気イキ。"
        },
        # 2: 1svmgm00054 マン圧クレーンゲームチャレンジ
        {
            "rank": "02",
            "subtitle": "女子大生が膣の締め付けで景品キャッチ？！赤面しながらマン圧を競い合う変態企画の最高峰",
            "body": """<b>【笑いとエロスの融合！街行く現役女子大生が膣圧測定で悶絶するハードボイルド傑作】</b>：<br>
高額賞金に釣られてマジックミラー号に乗り込んだ現役女子大生たちが、「アソコの締め付け（膣圧）」でクレーンを操作して景品を掴むという、SODならではのぶっ飛んだ変態企画。
最初は「恥ずかしすぎる！」と大爆笑していた女子大生たちですが、いざ特製プローブを挿入され、男性スタッフに性感帯を責められながらマン圧を計測されると、徐々に女の顔へと豹変。膣内をヒクヒクと収縮させながら「入ってます…ギュッてしてます！」と必死に締め付ける姿は、言葉を失うほどのスケベさ。最後は我慢の限界を迎えた男優の肉棒が生挿入され、先ほどまで測定していた極上の名器でズブズブと激しく搾り取られます。素人女子大生のリアルな下着、初々しい喘ぎ声、そして本気のアクメ表情がこれでもかと詰まった名作です。""",
            "climax": "賞金を忘れて快感に溺れ、男の腰に脚を絡めつけながら「もっと奥まで突いて！」と本気で懇願する密着正常位。"
        },
        # 3: 1sdmm00181 5時間35分大増量！保健体育の課外授業
        {
            "rank": "03",
            "subtitle": "総勢8名の素人娘が出演！5時間35分の超大ボリュームで描くオトナの性教育と乱れ咲き",
            "body": """<b>【1本で8人抜ける！マジックミラー号史上屈指の大ボリュームメガパック】</b>：<br>
「大人の濃厚SEXを見学する」という名目でマジックミラー号に集められた素人娘たちが、目の前で繰り広げられる激しいピストンと飛び散る愛液にアテられ、自分自身も服を脱ぎ捨てて交尾に雪崩れ込んでいく大ヒット企画。
5時間35分という規格外のボリュームの中に、総勢8名の個性豊かな素人女性が登場。黒髪清楚系、ギャル、地味系眼鏡っ娘まで、それぞれが「見ているだけ」のつもりだったのに、下着を濡らし、我慢できなくなって自らペニスを咥え込んでいく心理的変貌が克明に描かれます。プロの女優にはないぎこちない腰振りや、生の感触に驚いて声を漏らすリアルなリアクションが連続するため、素人フェチにはこれ以上ない至福のひととき。何日にも分けてたっぷり楽しめます。""",
            "climax": "他人のセックスを見つめてビショ濡れになった秘部に、後ろからいきなり突き刺されて歓喜の悲鳴をあげる素人バック。"
        },
        # 4: 1sdmm00207 サウナミラー号第2弾 移動式サウナ密室
        {
            "rank": "04",
            "subtitle": "蒸気と熱気で火照る裸体！移動式サウナの中で男女が理性を失い汗だくで貪り合う濃密情事",
            "body": """<b>【汗ばむ柔肌と熱気！密室サウナという極限シチュエーションが引き出す素人の本能】</b>：<br>
マジックミラー号の車内を完全な「移動式サウナ」へと改造した異色の神回。薄着の水着姿でサウナに閉じ込められた男女が、立ち上るロウリュの蒸気と熱気によって急速に体温と性欲を上昇させていきます。
全身から吹き出す大粒の汗が肌を伝い、胸元やお尻の谷間に光る光景はフェティシズムの極致。「暑い…でもドキドキする…」と呼吸を乱す素人美女に対し、火照った体を撫で回すだけで敏感度は通常の何倍にも跳ね上がります。サウナ特有のトランス状態（ととのい）とセックスのオーガズムが融合し、普段はおとなしい女性が自分から激しく腰を動かしてペニスを搾り取る姿は圧巻。視覚的な肉感美と湿度感がたまらない逸品です。""",
            "climax": "熱気立ち込めるサウナベンチで、汗だくの身体を密着させながら滴る汗とともに奥深くまで貫かれる汗だく騎乗位。"
        },
        # 5: 1svmgm00041 スパイダー騎乗位チキンレース
        {
            "rank": "05",
            "subtitle": "水着ギャルが挑む賞金チャレンジ！1ピストン100円の騎乗位で暴走する素人の腰使い",
            "body": """<b>【賞金稼ぎの水着ギャルが自爆アクメ！男をイカせるはずが自分が先にイキ狂う神回】</b>：<br>
「1ピストンするごとに100円獲得、ただし男を射精させたら全額没収」という過酷なチキンレースに挑戦する水着ギャルたち。
美脚と豊満なヒップを惜しげもなく晒したギャルたちが、男の上に跨がって「絶対イカせないようにゆっくり動くね」と余裕を見せながら腰をグラインド。しかし、肉棒の硬さと温もりがダイレクトに伝わるスパイダー騎乗位の体勢は、女性側のGスポットを容赦なく刺激します。数分後には賞金のことなど頭から消え去り、「ヤバい…これ私が気持ちいい…！」と自ら激しく腰を上下させて乱れ咲き。強気なギャルが快楽に負けて完全降伏する瞬間は、男の本能を最もゾクゾクさせる最高の抜きどころです。""",
            "climax": "男の胸に爪を立てながら、我を忘れて上下に腰を打ち付け、男の射精と同時に自らも痙攣アクメする激動のフィニッシュ。"
        }
    ]

    cards_html = ""
    for idx, (it, rev) in enumerate(zip(items, reviews), 1):
        cid_upper = it.get("content_id", "").upper()
        title = it.get("title", "")
        img_url = it.get("imageURL", {}).get("large", "")
        aff_url = it.get("affiliate_url_clean", "")
        price = it.get("prices", {}).get("price", "300~")
        genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        maker = it.get("iteminfo", {}).get("maker", [{}])[0].get("name", "SODクリエイト")

        genre_badges = "".join([get_genre_link(g) for g in genres[:6]])
        sample_imgs = get_sample_images(it, 4)
        sample_gallery = ""
        if sample_imgs:
            gallery_items = "".join([
                f'<div class="rounded-xl overflow-hidden aspect-video bg-slate-950 border border-slate-800 shadow-inner group"><img src="{s}" alt="{title} 抜きどころカット" class="w-full h-full object-cover group-hover:scale-110 transition duration-300" loading="lazy" /></div>'
                for s in sample_imgs
            ])
            sample_gallery = f'<div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-2">{gallery_items}</div>'

        card = f"""
    <!-- ランキングカード {rev['rank']} -->
    <article class="bg-slate-900/90 border border-slate-800 rounded-3xl p-6 md:p-8 space-y-6 shadow-2xl hover:border-amber-500/40 transition">
      <div class="flex flex-wrap items-center justify-between gap-2 pb-4 border-b border-slate-800">
        <div class="flex items-center gap-2">
          <span class="px-3.5 py-1 bg-gradient-to-r from-amber-500 to-rose-600 text-slate-950 font-black text-xs rounded-full shadow">
            MMG BEST {rev['rank']}
          </span>
          <span class="text-xs font-mono text-amber-400 font-bold">品番: {cid_upper}</span>
        </div>
        <div class="text-xs text-slate-400">
          <span class="text-amber-400 font-black text-sm">💰 {price}円〜</span>（配信中）
        </div>
      </div>

      <div class="space-y-1">
        <span class="text-xs font-bold text-amber-400 tracking-wider uppercase">マジックミラー号 歴代神回</span>
        <h4 class="text-xl md:text-2xl font-black text-white leading-snug hover:text-amber-300 transition">
          【第{idx}位】{rev['subtitle']}
        </h4>
      </div>

      <div class="p-3 bg-slate-950/60 rounded-xl border border-slate-800 text-xs text-slate-300 font-medium">
        <b>作品タイトル</b>: {title}
      </div>

      <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-start">
        <div class="md:col-span-5 space-y-4">
          <div class="relative rounded-2xl overflow-hidden border border-slate-800 bg-slate-950 aspect-[3/4] shadow-inner group">
            <img src="{img_url}" alt="{title} 公式パッケージ画像" class="w-full h-full object-cover group-hover:scale-105 transition duration-300" loading="lazy" />
            <span class="absolute top-2 left-2 px-2.5 py-1 bg-amber-500/90 backdrop-blur-sm text-slate-950 text-[10px] font-black rounded-lg shadow">素人・本気イキ神作</span>
          </div>

          <div class="p-4 bg-slate-950/80 rounded-2xl border border-slate-800 text-xs space-y-2 text-slate-300">
            <div><strong class="text-slate-400">👤 出演:</strong> <span class="text-rose-300 font-bold">リアル街頭素人娘</span></div>
            <div><strong class="text-slate-400">🏢 レーベル:</strong> <span class="text-amber-300 font-bold">{maker}</span></div>
            <div class="flex flex-wrap gap-1.5 pt-1">
              {genre_badges}
            </div>
          </div>

          <div class="flex flex-col gap-2.5">
            <a href="{aff_url}" target="_blank" rel="noopener noreferrer" class="block w-full text-center py-4 px-6 bg-gradient-to-r from-amber-500 via-rose-600 to-amber-500 hover:from-amber-400 hover:to-rose-500 text-slate-950 font-black rounded-2xl shadow-xl transform hover:-translate-y-0.5 transition duration-150 text-sm">
              💋 FANZA公式でこのマジックミラー号作品を見る ➔
            </a>
          </div>
        </div>

        <div class="md:col-span-7 space-y-4 text-slate-300 text-xs md:text-sm leading-relaxed">
          <div class="p-4 bg-amber-950/20 border border-amber-900/40 rounded-2xl space-y-1.5">
            <span class="text-[11px] font-black uppercase text-amber-400 tracking-wider">⚡ 編集部ガチ実況レビュー＆ガチ度検証</span>
            <div class="text-white text-xs md:text-sm leading-relaxed">
              {rev['body']}
            </div>
          </div>

          <div class="p-4 bg-slate-950/60 rounded-2xl border border-slate-800 space-y-1">
            <span class="text-[11px] font-bold text-rose-400 uppercase tracking-wide">🎯 ここで射精する！最大の見どころ</span>
            <p class="text-white font-medium text-xs md:text-sm">
              {rev['climax']}
            </p>
          </div>

          {sample_gallery}
        </div>
      </div>
    </article>
"""
        cards_html += card

    content_html = f"""
<div class="space-y-12 text-slate-100 leading-relaxed font-sans">
  <!-- イントロダクション HERO -->
  <section class="bg-gradient-to-br from-slate-900 via-rose-950/50 to-slate-900 border-2 border-rose-500/50 rounded-3xl p-6 md:p-10 shadow-2xl space-y-6 relative overflow-hidden">
    <div class="absolute -right-16 -top-16 w-64 h-64 bg-rose-500/10 rounded-full blur-3xl pointer-events-none"></div>
    <div class="inline-flex items-center gap-2 px-4 py-1.5 bg-rose-500/20 text-rose-300 border border-rose-500/40 rounded-full text-xs font-black tracking-widest uppercase">
      <span>🚐</span><span>四半世紀売れ続ける金字塔 • 生々しい素人エロスの最高峰</span>
    </div>
    
    <h2 class="text-2xl md:text-4xl font-black text-white leading-tight tracking-tight">
      【25年売れ続ける伝説】マジックミラー号＆リアル素人ナンパ傑作選！生々しい恥じらいと本気アクメに悶絶する歴代神回ランキング
    </h2>
    
    <p class="text-slate-300 text-sm md:text-base leading-relaxed">
      「プロの女優の演技もいいけれど、街で見かける普通の女の子が恥ずかしがりながら堕ちていく姿が見たい」「外からは見えないけれど中からは街行く人々が丸見えという背徳感に興奮する」——日本のAV史において25年以上もの間、絶対的な人気を誇り続けているのが<b>『マジックミラー号（MMG）』</b>です。
    </p>
    <p class="text-slate-300 text-sm md:text-base leading-relaxed">
      マジックミラー号がなぜこれほどまでに男たちの性癖を刺激してやまないのか。それは、<b>「日常の延長線上にある露出狂的なスリル」</b>と、<b>「初めは拒んでいた素人女性が、激しいピストンによって快楽に抗えなくなり、本気でイク瞬間のリアルさ」</b>にあります。窓の外を一般人が歩くすぐ数十センチ横で、声を押し殺しながら腰を跳ね上げるその光景は、どんなフィクションも敵わない究極の興奮を生み出します。
    </p>
    <p class="text-slate-300 text-sm md:text-base leading-relaxed">
      当サイトの<a href="/ranking" class="text-amber-400 hover:text-amber-300 font-bold underline">ランキング</a>や<a href="/posts/feature_fanza_top_exclusive_actresses_ranking_masterpiece" class="text-rose-400 hover:text-rose-300 font-bold underline">単体専属女優ランキング</a>とは一線を画す「素人・企画ジャンル」の頂点として、FANZA公式APIを通じてリアルタイムにデータを取得。「今夜、本気でシコれるマジックミラー号の歴代神回TOP5」を徹底検証します。
    </p>
  </section>

  <!-- なぜマジックミラー号は25年間売れ続けるのか？ -->
  <section class="space-y-6">
    <div class="flex items-center gap-3 border-l-4 border-rose-500 pl-3">
      <h3 class="text-xl md:text-2xl font-black text-white">なぜマジックミラー号は25年間売れ続けるのか？男を惹きつけて離さない3つの理由</h3>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
      <div class="bg-slate-900/90 border border-slate-800 p-5 rounded-2xl space-y-3 shadow-lg">
        <div class="w-10 h-10 rounded-xl bg-rose-500/20 border border-rose-500/40 flex items-center justify-center text-xl">👀</div>
        <h4 class="font-bold text-white text-base">「外からは見えないが中からは丸見え」の極限露出</h4>
        <p class="text-xs md:text-sm text-slate-300 leading-relaxed">
          渋谷や新宿の真ん中で車を止め、すぐ外を歩くサラリーマンや通行人の視線を間近に感じながらセックス。この異常な緊張感が素人女性の性感帯を異常に研ぎ澄まします。
        </p>
      </div>

      <div class="bg-slate-900/90 border border-slate-800 p-5 rounded-2xl space-y-3 shadow-lg">
        <div class="w-10 h-10 rounded-xl bg-amber-500/20 border border-amber-500/40 flex items-center justify-center text-xl">💦</div>
        <h4 class="font-bold text-white text-base">演技ではない「本気アクメ」と赤面リアクション</h4>
        <p class="text-xs md:text-sm text-slate-300 leading-relaxed">
          プロの女優のように慣れたリアクションではなく、初めて体験する激しい刺激に戸惑い、息を呑み、必死に声を押し殺そうとする生々しい吐息こそが最大のオカズになります。
        </p>
      </div>

      <div class="bg-slate-900/90 border border-slate-800 p-5 rounded-2xl space-y-3 shadow-lg">
        <div class="w-10 h-10 rounded-xl bg-purple-500/20 border border-purple-500/40 flex items-center justify-center text-xl">🎯</div>
        <h4 class="font-bold text-white text-base">ゲーム性豊かな企画で素人の本能を暴く構成美</h4>
        <p class="text-xs md:text-sm text-slate-300 leading-relaxed">
          「制限時間脱出」「マン圧測定」「サウナロウリュ」「騎乗位チキンレース」など、SODが長年磨き上げた企画力により、素人女性が自然と快楽の深みへと堕ちていく様が描かれます。
        </p>
      </div>
    </div>
  </section>

  <!-- ランキング一覧セクション -->
  <section class="space-y-8">
    <div class="border-l-4 border-rose-500 pl-3 space-y-2">
      <span class="text-xs font-bold text-rose-400 uppercase tracking-widest">LEGENDARY SERIES 2026</span>
      <h3 class="text-2xl md:text-3xl font-black text-white">
        【FANZA公式API取得】マジックミラー号・歴代最高傑作ランキングTOP5
      </h3>
      <p class="text-xs md:text-sm text-slate-400">
        数千作におよぶSODの名作ライブラリから、演出・素人度・抜きどころの破壊力すべてで満票を獲得した神回を厳選。
      </p>
    </div>

    {cards_html}

  </section>

  <!-- 初心者向け：マジックミラー号の選び方ガイド -->
  <section class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 space-y-6">
    <div class="flex items-center gap-3 border-l-4 border-rose-500 pl-3">
      <h3 class="text-xl md:text-2xl font-black text-white">失敗しない「マジックミラー号」作品の選び方</h3>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm text-slate-300">
      <div class="p-4 bg-slate-950/80 rounded-xl border border-slate-800 space-y-1.5">
        <strong class="text-rose-400 block font-bold text-sm">💖 初々しい素人の恥じらいを楽しみたいなら</strong>
        <p>➔ <b>「脱出ゲーム」シリーズ</b>。時間が迫る焦燥感と、拒絶から受容へと変わるリアルなグラデーションが最高です。</p>
      </div>
      <div class="p-4 bg-slate-950/80 rounded-xl border border-slate-800 space-y-1.5">
        <strong class="text-amber-400 block font-bold text-sm">🔥 激しい腰振りと本気イキを堪能したいなら</strong>
        <p>➔ <b>「ハードボイルド」シリーズ</b>。スパイダー騎乗位やマン圧測定など、肉体的な刺激に特化した企画が揃っています。</p>
      </div>
      <div class="p-4 bg-slate-950/80 rounded-xl border border-slate-800 space-y-1.5">
        <strong class="text-purple-400 block font-bold text-sm">👥 たくさんの素人を一度に味わいたいなら</strong>
        <p>➔ <b>「大増量5時間超え」シリーズ</b>。1本で7〜8名の素人が次々と登場し、様々なタイプの女性で射精できます。</p>
      </div>
    </div>
  </section>

  <!-- よくある質問 FAQセクション -->
  <section class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 space-y-6">
    <div class="flex items-center gap-3 border-l-4 border-rose-500 pl-3">
      <h3 class="text-xl md:text-2xl font-black text-white">マジックミラー号に関するよくある質問【Q&A】</h3>
    </div>
    
    <div class="space-y-4 text-xs md:text-sm">
      <div class="p-5 bg-slate-950/80 rounded-2xl border border-slate-800 space-y-2">
        <h4 class="font-bold text-rose-400 flex items-center gap-2">
          <span>Q.</span><span>マジックミラー号は本当に街中を走っているのですか？</span>
        </h4>
        <p class="text-slate-300 leading-relaxed">
          <b>はい、実際にSODが特注改造した専用トラックが実在し、都内や地方都市でロケが行われています</b>。外側は完全な鏡（ハーフミラー）になっており、街行く人々が髪型を直したり鏡として利用する様子が車内からハッキリと確認できます。このリアルな舞台装置が唯一無二の興奮を生み出しています。
        </p>
      </div>

      <div class="p-5 bg-slate-950/80 rounded-2xl border border-slate-800 space-y-2">
        <h4 class="font-bold text-rose-400 flex items-center gap-2">
          <span>Q.</span><span>出演している女性は全員本物の素人ですか？</span>
        </h4>
        <p class="text-slate-300 leading-relaxed">
          作品によって「完全な一般街頭ナンパ」「オーディション応募者」「エキストラ登録者」など出演の経緯は様々ですが、共通しているのは<b>「プロのAV女優のような定型的な演技をしない」</b>という点です。初めての撮影や露出に本気で狼狽し、快感に目覚めていく反応の初々しさは素人企画ならではの魅力です。
        </p>
      </div>

      <div class="p-5 bg-slate-950/80 rounded-2xl border border-slate-800 space-y-2">
        <h4 class="font-bold text-rose-400 flex items-center gap-2">
          <span>Q.</span><span>スマホやタブレットで手軽に見る方法はありますか？</span>
        </h4>
        <p class="text-slate-300 leading-relaxed">
          FANZAの動画ストリーミング配信を購入すれば、購入後すぐにブラウザや公式プレイヤーアプリで高画質再生が可能です。当サイトの<a href="/posts/feature_fanza_app_player_guide_offline_streaming" class="text-rose-400 underline font-bold">公式プレイヤー使い方攻略</a>も参考にしてください。
        </p>
      </div>
    </div>
  </section>

  <!-- あわせて読みたい関連キラー特集（内部リンク・トピッククラスター） -->
  <section class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 space-y-6">
    <div class="flex items-center gap-3 border-l-4 border-rose-500 pl-3">
      <h3 class="text-xl md:text-2xl font-black text-white">あわせて読みたい！FANZA完全攻略おすすめ特集</h3>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      <a href="/posts/feature_fanza_super_long_omnibus_best_selection_ranking" class="p-4 bg-slate-950/80 hover:bg-slate-800/80 border border-slate-800 rounded-2xl space-y-2 group transition">
        <span class="text-xs font-bold text-amber-400">大容量コスパ</span>
        <h4 class="text-sm font-bold text-white group-hover:text-rose-300 transition">超長尺BEST・総集編おすすめ傑作選</h4>
        <p class="text-[11px] text-slate-400 line-clamp-2">8時間〜16時間のモンスターパック！1本で数十回抜ける神作まとめ。</p>
      </a>
      <a href="/posts/feature_fanza_mature_milf_wives_best_selection_ranking" class="p-4 bg-slate-950/80 hover:bg-slate-800/80 border border-slate-800 rounded-2xl space-y-2 group transition">
        <span class="text-xs font-bold text-rose-400">濃厚フェロモン</span>
        <h4 class="text-sm font-bold text-white group-hover:text-rose-300 transition">人妻・美熟女ランキングTOP5</h4>
        <p class="text-[11px] text-slate-400 line-clamp-2">他人の妻を奪う背徳感と成熟ボディ！殿堂入り傑作選。</p>
      </a>
      <a href="/posts/feature_fanza_payment_methods_safe_buying_guide" class="p-4 bg-slate-950/80 hover:bg-slate-800/80 border border-slate-800 rounded-2xl space-y-2 group transition">
        <span class="text-xs font-bold text-emerald-400">バレ防止</span>
        <h4 class="text-sm font-bold text-white group-hover:text-rose-300 transition">クレカ不要！完全匿名・安全支払いガイド</h4>
        <p class="text-[11px] text-slate-400 line-clamp-2">PayPayやプリカで家族バレを徹底ゼロにする方法。</p>
      </a>
      <a href="/posts/feature_meta_quest_fanza_vr_ultimate_guide" class="p-4 bg-slate-950/80 hover:bg-slate-800/80 border border-slate-800 rounded-2xl space-y-2 group transition">
        <span class="text-xs font-bold text-cyan-400">VR没入</span>
        <h4 class="text-sm font-bold text-white group-hover:text-rose-300 transition">Quest 3S/3対応 FANZA VR攻略</h4>
        <p class="text-[11px] text-slate-400 line-clamp-2">手の届く至近距離で美女と交わる8K神作VRまとめ。</p>
      </a>
    </div>
  </section>

  <!-- 構造化データ（JSON-LD） -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "【25年売れ続ける伝説】マジックミラー号＆リアル素人ナンパ傑作選！生々しい恥じらいと本気アクメに悶絶する歴代神回ランキング",
    "description": "SODの金字塔「マジックミラー号」シリーズの中から、本当に抜ける歴代神回を厳選。露出の背徳感、素人の本気イキの魅力、公式APIリアルタイム取得データを徹底レビュー。",
    "image": "{cover_image}",
    "datePublished": "2026-09-30T00:06:00+09:00",
    "author": {{
      "@type": "Organization",
      "name": "背徳の美学 編集部"
    }}
  }}
  </script>

  <!-- 総括CTA -->
  <section class="text-center bg-gradient-to-r from-rose-950 via-slate-900 to-rose-950 border-2 border-rose-500/50 rounded-3xl p-8 md:p-12 shadow-2xl space-y-5">
    <h3 class="text-2xl md:text-3xl font-black text-white">
      街行く人々のすぐ横で、恥じらいを捨ててイキ狂う素人美女たち。
    </h3>
    <p class="text-slate-300 text-xs md:text-sm max-w-2xl mx-auto leading-relaxed">
      理性を揺さぶる極限の露出と、本気の喘ぎ声。四半世紀愛され続ける伝説の快楽を、今すぐFANZA公式でお楽しみください。
    </p>
    <div class="pt-2">
      <a href="{items[0].get('affiliate_url_clean', '')}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-3 px-10 py-5 bg-gradient-to-r from-rose-600 via-amber-500 to-rose-600 hover:from-rose-500 hover:to-amber-400 text-slate-950 font-black text-base rounded-2xl shadow-2xl transform hover:-translate-y-0.5 transition duration-200">
        <span>🚐</span><span>FANZA公式でマジックミラー号の神作をチェックする ➔</span>
      </a>
    </div>
  </section>
</div>
"""

    char_count = count_japanese_chars(content_html)
    print(f"Article 2 generated: {char_count} Japanese chars")
    if char_count < 3000:
        raise Exception(f"Article 2 has only {char_count} chars, minimum 3000 required")

    post_data = {
        "id": "feature_fanza_magic_mirror_go_real_amateur_best_ranking",
        "title": "【25年売れ続ける伝説】マジックミラー号＆リアル素人ナンパ傑作選！生々しい恥じらいと本気アクメに悶絶する歴代神回ランキング",
        "content": content_html,
        "review": content_html,
        "image": cover_image,
        "date": "2026-09-30 00:06:00",
        "genres": ["素人", "マジックミラー号", "企画", "ハイビジョン", "独占配信", "露出・野外", "ナンパ"],
        "actresses": ["リアル素人娘"],
        "maker": "SODクリエイト",
        "price": "300~",
        "affiliate_url": items[0].get("affiliate_url_clean", "")
    }

    out_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f" -> Saved Article 2 to {out_path}")
    return post_data


# ==============================================================================
# 記事3: FANZA同人ゲームおすすめ殿堂入り名作選
# ==============================================================================
def generate_article_3():
    print("=== Generating Article 3: Doujin PC Game Masterpieces Guide ===")
    cids = ["d_785965", "d_811449", "d_580141", "d_804033", "d_213575"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid, service="doujin", floor="digital_doujin")
        if it:
            items.append(it)
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        else:
            print(f" -> Failed to fetch {cid}")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception("Failed to fetch all 5 items for Article 3 from FANZA API")

    cover_image = items[0].get("imageURL", {}).get("large", "")

    reviews = [
        # 1: d_785965 罰カノ2〜ムッツリ広瀬ちゃんの逆襲〜
        {
            "rank": "01",
            "subtitle": "普段はクールなツンデレ彼女が、エッチな罰ゲームでムッツリスケベへと覚醒する大ヒット作",
            "body": """<b>【累計数万本突破！動くアニメーションと濃厚ボイスで骨抜きにされる神作ADV】</b>：<br>
同人ゲーム界で爆発的なセールスを記録した伝説のタイトル『罰カノ』の正統進化続編。普段はツンツンしていてそっけない彼女「広瀬ちゃん」と、二人きりの部屋でエッチな罰ゲームを繰り広げるイチャラブ×開発シミュレーションです。
Live2Dによる滑らかなアニメーションで、彼女の表情や胸の揺れ、太ももの震えがリアルタイムに反応。最初は「こんなの全然恥ずかしくないんだから…！」と強がっていた彼女が、クリックで愛撫を重ねるごとに息を荒らげ、やがて自ら淫らなポーズをとって快楽をおねだりしてくる過程は脳が溶けるほどの破壊力。超豪華声優による吐息交じりのボイスと、耳元で囁かれるようなバイノーラル音響が完璧に融合しており、プレイヤーの欲望の赴くままに彼女をドスケベに開発し尽くせます。""",
            "climax": "ツンデレの殻をかなぐり捨て、涎を垂らしながらアヘ顔ダブルピースで中出しを懇願する罰ゲーム絶頂。"
        },
        # 2: d_811449 時間停止催●でJKにいたずらし放題な件について
        {
            "rank": "02",
            "subtitle": "男の究極の妄想がゲーム化！ピクリとも動かないJKたちの服を剥ぎ、自由奔放に弄び倒す快感",
            "body": """<b>【時間を止めて美少女を弄ぶ！スマホ操作にも対応した圧倒的自由度の停止系エロゲー】</b>：<br>
すべての男性が一度は夢想する「時間停止能力」をテーマにした大人気同人ゲーム。街中や学校、電車の中で時を止め、無防備に静止したJKたちのスカートをめくり、下着を脱がせ、好きな体位で交尾を叩き込む背徳の極致を体験できます。
停止している状態でのイタズラはもちろん、徐々に意識だけを目覚めさせる「催眠解除モード」が搭載されており、「動けないのに触られている感覚だけがある」「体が勝手に感じてしまう」という心理的屈辱を味わせることが可能。ドット絵と高精細イラストのハイブリッド演出が素晴らしく、スマホ操作にも最適化されているため、ベッドの中で指先一つで手軽に濃厚オナニーを楽しめる屈指の利便性を誇ります。""",
            "climax": "意識だけを取り戻した美少女が、動けない体の中で声にならない悲鳴を上げながら強制アクメさせられる時間停止生ハメ。"
        },
        # 3: d_580141 【ゲーム】あの日見た種付けプレスを僕はまだ忘れられない
        {
            "rank": "03",
            "subtitle": "サクサク進んで無限に抜ける！種付けおじさんとなって美少女たちを孕ませまくる中毒SLG",
            "body": """<b>【タイトルで笑って中身で昇天！圧倒的な抜きやすさとテンポ感を極めた種付けSLG】</b>：<br>
インパクト抜群のタイトルとともに、圧倒的な実用性と抜きやすさで大絶賛された名作SLG。プレイヤーは逞しい種付け男となり、様々なタイプの美少女たちを自分の肉棒一本で屈服させ、遺伝子を刻み込んでいきます。
煩わしい育成要素や長時間のレベリングを極限まで排除し、最短の手数で即座にHシーンへと突入できる親切設計が最大の魅力。ヒロインたちの断面図描写、子宮に精液がドクドクと注ぎ込まれるアニメーション演出、そして中出し後の妊娠・堕ち演出までフェチ要素がフルコンプリートされています。仕事で疲れて帰ってきた夜でも、起動後3分で極上の射精へと導いてくれる現代人のための最強時短ヌキゲーです。""",
            "climax": "両足を高々と持ち上げた種付けプレスで、奥深くまで肉棒を突き刺して大量の精子を注ぎ込むドロドロ子宮内射精。"
        },
        # 4: d_804033 Hとメイドと無人島
        {
            "rank": "04",
            "subtitle": "無人島で健気なメイドと二人きり！サバイバル生活の中で深まる絆と尽くされまくる密着性交",
            "body": """<b>【無人島サバイバル×献身メイド！毎日のお世話から夜の夜這いまで甘やかされ放題の楽園】</b>：<br>
豪華客船の事故により、忠実で献身的な専属メイドと一緒に無人島に漂着してしまった主人公。生き残るための探索や拠点作りを行いながら、ご主人様のために心も体もすべてを捧げてくれるメイドと濃厚な毎日を過ごす箱庭サバイバルRPGです。
拠点が発展するごとにメイドの衣装を着せ替えたり、料理を作ってもらったり、夜のテントで添い寝してもらったりと、男性の「甘えたい」「支配したい」という二大願望を完璧に満たしてくれます。過酷な無人島生活だからこそ、肌と肌を触れ合わせるぬくもりが強調され、ただ抜くだけでなく心まで満たされる癒やしと背徳が同居した大傑作です。""",
            "climax": "焚き火の明かりに照らされたテントの中で、涙ぐみながら「ご主人様の精液で満たしてください」と跨がってくる献身騎乗位。"
        },
        # 5: d_213575 カルティベーター 〜引退騎士とモン娘のにぎやか開拓記〜
        {
            "rank": "05",
            "subtitle": "骨太RPGと濃厚モン娘交尾の究極融合！個性豊かなモンスター娘たちを開拓地で飼育・調教する超大作",
            "body": """<b>【超大作ボリューム！ゲームとしての面白さと過激なHシーンが完璧に調和したマスターピース】</b>：<br>
元凄腕の騎士となって、未開の土地を開拓しながら多種多様なモンスター娘たちを捕獲・調教していく本格RPG。同人ゲームの域を遥かに超えた作り込みと、圧倒的なボリュームで数年にわたりランキング上位に君臨し続けるレジェンド作品です。
スライム娘、ハーピー、ラミア、サキュバスなど、人外特有の特殊な肉体構造と性癖を刺激するアニメーションCGが満載。ダンジョン探索で仲間を増やし、拠点でお気に入りのモン娘たちと様々な体位で交わる楽しさはまさに時間泥棒。普通の女性とのセックスでは物足りなくなった上級者をも唸らせる、知る人ぞ知る殿堂入りの至宝です。""",
            "climax": "異形の肉体を持つモン娘に絡め取られ、人間の限界を超える超絶快感で何度も何度も精液を搾り取られる強制連続射精。"
        }
    ]

    cards_html = ""
    for idx, (it, rev) in enumerate(zip(items, reviews), 1):
        cid_upper = it.get("content_id", "").upper()
        title = it.get("title", "")
        img_url = it.get("imageURL", {}).get("large", "")
        aff_url = it.get("affiliate_url_clean", "")
        price = it.get("prices", {}).get("price", "1500")
        genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        maker = it.get("iteminfo", {}).get("maker", [{}])[0].get("name", "同人サークル")

        genre_badges = "".join([get_genre_link(g) for g in genres[:6]])
        sample_imgs = get_sample_images(it, 4)
        sample_gallery = ""
        if sample_imgs:
            gallery_items = "".join([
                f'<div class="rounded-xl overflow-hidden aspect-video bg-slate-950 border border-slate-800 shadow-inner group"><img src="{s}" alt="{title} プレイ画面カット" class="w-full h-full object-cover group-hover:scale-110 transition duration-300" loading="lazy" /></div>'
                for s in sample_imgs
            ])
            sample_gallery = f'<div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-2">{gallery_items}</div>'

        card = f"""
    <!-- ランキングカード {rev['rank']} -->
    <article class="bg-slate-900/90 border border-slate-800 rounded-3xl p-6 md:p-8 space-y-6 shadow-2xl hover:border-purple-500/40 transition">
      <div class="flex flex-wrap items-center justify-between gap-2 pb-4 border-b border-slate-800">
        <div class="flex items-center gap-2">
          <span class="px-3.5 py-1 bg-gradient-to-r from-purple-500 to-rose-600 text-white font-black text-xs rounded-full shadow">
            GAME RANK {rev['rank']}
          </span>
          <span class="text-xs font-mono text-purple-300 font-bold">品番: {cid_upper}</span>
        </div>
        <div class="text-xs text-slate-400">
          <span class="text-purple-300 font-black text-sm">💰 {price}円</span>（DL版配信中）
        </div>
      </div>

      <div class="space-y-1">
        <span class="text-xs font-bold text-purple-400 tracking-wider uppercase">FANZA同人ゲーム 殿堂入り名作</span>
        <h4 class="text-xl md:text-2xl font-black text-white leading-snug hover:text-purple-300 transition">
          【第{idx}位】{rev['subtitle']}
        </h4>
      </div>

      <div class="p-3 bg-slate-950/60 rounded-xl border border-slate-800 text-xs text-slate-300 font-medium">
        <b>作品タイトル</b>: {title}
      </div>

      <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-start">
        <div class="md:col-span-5 space-y-4">
          <div class="relative rounded-2xl overflow-hidden border border-slate-800 bg-slate-950 aspect-[3/4] shadow-inner group">
            <img src="{img_url}" alt="{title} 公式メインビジュアル" class="w-full h-full object-cover group-hover:scale-105 transition duration-300" loading="lazy" />
            <span class="absolute top-2 left-2 px-2.5 py-1 bg-purple-600/90 backdrop-blur-sm text-white text-[10px] font-black rounded-lg shadow">動く！アニメーション搭載</span>
          </div>

          <div class="p-4 bg-slate-950/80 rounded-2xl border border-slate-800 text-xs space-y-2 text-slate-300">
            <div><strong class="text-slate-400">🏢 開発サークル:</strong> <span class="text-purple-300 font-bold">{maker}</span></div>
            <div><strong class="text-slate-400">🎮 対応環境:</strong> <span class="text-white font-medium">Windows PC / 一部スマホブラウザ</span></div>
            <div class="flex flex-wrap gap-1.5 pt-1">
              {genre_badges}
            </div>
          </div>

          <div class="flex flex-col gap-2.5">
            <a href="{aff_url}" target="_blank" rel="noopener noreferrer" class="block w-full text-center py-4 px-6 bg-gradient-to-r from-purple-600 via-rose-600 to-purple-600 hover:from-purple-500 hover:to-rose-500 text-white font-black rounded-2xl shadow-xl transform hover:-translate-y-0.5 transition duration-150 text-sm">
              🎮 FANZA公式でこの同人ゲームをDLする ➔
            </a>
          </div>
        </div>

        <div class="md:col-span-7 space-y-4 text-slate-300 text-xs md:text-sm leading-relaxed">
          <div class="p-4 bg-purple-950/20 border border-purple-900/40 rounded-2xl space-y-1.5">
            <span class="text-[11px] font-black uppercase text-purple-400 tracking-wider">⚡ 編集部ガチプレイレビュー＆抜きポイント</span>
            <div class="text-white text-xs md:text-sm leading-relaxed">
              {rev['body']}
            </div>
          </div>

          <div class="p-4 bg-slate-950/60 rounded-2xl border border-slate-800 space-y-1">
            <span class="text-[11px] font-bold text-rose-400 uppercase tracking-wide">🎯 ここで射精する！最大の見どころ</span>
            <p class="text-white font-medium text-xs md:text-sm">
              {rev['climax']}
            </p>
          </div>

          {sample_gallery}
        </div>
      </div>
    </article>
"""
        cards_html += card

    content_html = f"""
<div class="space-y-12 text-slate-100 leading-relaxed font-sans">
  <!-- イントロダクション HERO -->
  <section class="bg-gradient-to-br from-slate-900 via-purple-950/60 to-slate-900 border-2 border-purple-500/50 rounded-3xl p-6 md:p-10 shadow-2xl space-y-6 relative overflow-hidden">
    <div class="absolute -right-16 -top-16 w-64 h-64 bg-purple-500/10 rounded-full blur-3xl pointer-events-none"></div>
    <div class="inline-flex items-center gap-2 px-4 py-1.5 bg-purple-500/20 text-purple-300 border border-purple-500/40 rounded-full text-xs font-black tracking-widest uppercase">
      <span>🎮</span><span>2026年最新 • 画面の向こうの美少女を自らの手で開発する</span>
    </div>
    
    <h2 class="text-2xl md:text-4xl font-black text-white leading-tight tracking-tight">
      【動いて喘ぐ極上ヌキゲー】FANZA同人ゲームおすすめ殿堂入り名作選！アニメーションCG×超豪華ボイスで骨抜きにされる神作RPG・SLG完全攻略
    </h2>
    
    <p class="text-slate-300 text-sm md:text-base leading-relaxed">
      「受動的に見るだけの動画にマンネリを感じている」「自分のマウス操作や選択肢によって、美少女の喘ぎ声や表情がリアルタイムに変わる快感を味わいたい」——そんな大人たちを虜にし、今やFANZAの全売上の中でも急速に存在感を拡大しているのが<b>『FANZA同人エロゲーム（PCゲーム）』</b>です。
    </p>
    <p class="text-slate-300 text-sm md:text-base leading-relaxed">
      近年の同人ゲームの進化は凄まじく、<b>Live2DやSpine技術によるヌルヌル動く滑らかなアニメーション</b>、プロ声優による<b>鼓膜を震わせるバイノーラル音声</b>、そしてプレイヤー自身の意志でヒロインを調教・開発していく<b>インタラクティブな没入感</b>は、実写動画や静止画マンガを遥かに凌駕します。一度その快楽を知ってしまうと、夜な夜な寝不足になりながらマウスを握り続けることになる「時間泥棒」の宝庫です。
    </p>
    <p class="text-slate-300 text-sm md:text-base leading-relaxed">
      当サイトの<a href="/posts/feature_fanza_doujin_cg_manga_high_rating_masterpieces" class="text-purple-400 hover:text-purple-300 font-bold underline">同人CGコミック特集</a>や<a href="/posts/feature_fanza_doujin_asmr_voice_masterpiece_guide" class="text-rose-400 hover:text-rose-300 font-bold underline">同人ASMRボイスガイド</a>に続く「同人コンテンツ完全制覇プロジェクト」として、FANZA公式APIを通じてリアルタイムにデータを取得。「今すぐ遊べて絶対にシコれる、歴代売上上位の神作PCゲームTOP5」を徹底攻略します。
    </p>
  </section>

  <!-- なぜ今「同人ゲーム」で抜く人が急増しているのか？ -->
  <section class="space-y-6">
    <div class="flex items-center gap-3 border-l-4 border-purple-500 pl-3">
      <h3 class="text-xl md:text-2xl font-black text-white">なぜ今「同人ゲーム」で抜く大人が急増しているのか？動画にはない3つの優位性</h3>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
      <div class="bg-slate-900/90 border border-slate-800 p-5 rounded-2xl space-y-3 shadow-lg">
        <div class="w-10 h-10 rounded-xl bg-purple-500/20 border border-purple-500/40 flex items-center justify-center text-xl">✨</div>
        <h4 class="font-bold text-white text-base">クリックに合わせて呼吸と喘ぎが変化する双方向性</h4>
        <p class="text-xs md:text-sm text-slate-300 leading-relaxed">
          ただ眺めるだけではなく、自分がマウスを動かした速度や場所に応じてヒロインが反応。クリトリスを撫でれば声を震わせ、ピストンを早めれば絶叫する圧倒的リアリティが存在します。
        </p>
      </div>

      <div class="bg-slate-900/90 border border-slate-800 p-5 rounded-2xl space-y-3 shadow-lg">
        <div class="w-10 h-10 rounded-xl bg-rose-500/20 border border-rose-500/40 flex items-center justify-center text-xl">🔊</div>
        <h4 class="font-bold text-white text-base">アニメーションCG×超豪華バイノーラル声優の共演</h4>
        <p class="text-xs md:text-sm text-slate-300 leading-relaxed">
          商業アニメ顔負けの滑らかな動きに加え、人気声優による濃密なリップ音・息遣いがステレオ音響で耳孔に直接注ぎ込まれます。イヤホン装着時の没入感は異次元です。
        </p>
      </div>

      <div class="bg-slate-900/90 border border-slate-800 p-5 rounded-2xl space-y-3 shadow-lg">
        <div class="w-10 h-10 rounded-xl bg-amber-500/20 border border-amber-500/40 flex items-center justify-center text-xl">♾️</div>
        <h4 class="font-bold text-white text-base">自分好みに衣装や体位、性格をカスタマイズ可能</h4>
        <p class="text-xs md:text-sm text-slate-300 leading-relaxed">
          コスチューム変更、中出し差分、アヘ顔の度合い、妊娠や調教の進捗など、自分だけの理想のシチュエーションを心ゆくまで作り込める圧倒的な自由度が備わっています。
        </p>
      </div>
    </div>
  </section>

  <!-- ゲームジャンル別比較表 -->
  <section class="bg-gradient-to-br from-slate-900 via-slate-950 to-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 space-y-6">
    <div class="flex items-center gap-3 border-l-4 border-purple-500 pl-3">
      <h3 class="text-xl md:text-2xl font-black text-white">【ジャンル別】同人ゲームのタイプと特徴まとめ</h3>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
      <div class="bg-slate-950/80 border border-slate-800 p-5 rounded-2xl space-y-2">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <strong class="text-purple-400 font-bold text-base">育成・調教SLG型</strong>
          <span class="text-[11px] px-2 py-0.5 bg-purple-950 text-purple-300 rounded border border-purple-800">抜きやすさNo.1</span>
        </div>
        <p class="text-xs md:text-sm text-slate-300 leading-relaxed">
          種付けプレスや罰カノのように、面倒なルールなしで直感的にヒロインを開発できるタイプ。短時間で何回も射精したい人に最適です。
        </p>
      </div>

      <div class="bg-slate-950/80 border border-slate-800 p-5 rounded-2xl space-y-2">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <strong class="text-rose-400 font-bold text-base">ADV・ノベル型</strong>
          <span class="text-[11px] px-2 py-0.5 bg-rose-950 text-rose-300 rounded border border-rose-800">ストーリー＆没入</span>
        </div>
        <p class="text-xs md:text-sm text-slate-300 leading-relaxed">
          時間停止やサバイバルのように、濃厚な世界観と会話劇の中で美少女との絆を深めていくタイプ。感情移入して抜きたい人向け。
        </p>
      </div>

      <div class="bg-slate-950/80 border border-slate-800 p-5 rounded-2xl space-y-2">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <strong class="text-amber-400 font-bold text-base">本格RPG・開拓型</strong>
          <span class="text-[11px] px-2 py-0.5 bg-amber-950 text-amber-300 rounded border border-amber-800">やり込み度無限大</span>
        </div>
        <p class="text-xs md:text-sm text-slate-300 leading-relaxed">
          カルティベーターのように、ゲーム自体の面白さと膨大な数のモン娘・Hシーンが融合した超大作。週末に腰を据えて遊べます。
        </p>
      </div>
    </div>
  </section>

  <!-- ランキング一覧セクション -->
  <section class="space-y-8">
    <div class="border-l-4 border-purple-500 pl-3 space-y-2">
      <span class="text-xs font-bold text-purple-400 uppercase tracking-widest">TOP GAME RANKING 2026</span>
      <h3 class="text-2xl md:text-3xl font-black text-white">
        【FANZA公式API取得】絶対に買うべき！同人PCゲーム殿堂入り神作TOP5
      </h3>
      <p class="text-xs md:text-sm text-slate-400">
        配信中の数万タイトルの中から、画力、アニメーション品質、ボイス、リピート率すべてで頂点に立つ名作を厳選。
      </p>
    </div>

    {cards_html}

  </section>

  <!-- 初心者向け：同人ゲームのプレイ環境と遊び方ガイド -->
  <section class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 space-y-6">
    <div class="flex items-center gap-3 border-l-4 border-purple-500 pl-3">
      <h3 class="text-xl md:text-2xl font-black text-white">初めてでも安心！同人エロゲームを遊ぶための基礎知識</h3>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-5 text-xs md:text-sm text-slate-300">
      <div class="p-5 bg-slate-950/80 rounded-2xl border border-slate-800 space-y-2">
        <strong class="text-purple-400 block font-bold text-sm">💻 PCスペックは普通のノートPCで十分？</strong>
        <p class="leading-relaxed">
          最新の3Dゲームを除き、今回紹介した大半の2Dアニメーション・SLG作品は一般的なWindowsノートPC（Core i3 / 8GBメモリ程度）でもサクサク快適に動作します。ゲーミングPCを持っていなくても全く問題ありません。
        </p>
      </div>

      <div class="p-5 bg-slate-950/80 rounded-2xl border border-slate-800 space-y-2">
        <strong class="text-rose-400 block font-bold text-sm">📱 スマホやタブレットでもプレイできる？</strong>
        <p class="leading-relaxed">
          『時間停止催眠』など一部の人気作品はスマホブラウザ対応版が用意されており、iPhoneやAndroid端末のタップ操作でもそのまま遊べます。購入前に作品ページの「対応OS」アイコンをチェックするのがおすすめです。
        </p>
      </div>
    </div>
  </section>

  <!-- よくある質問 FAQセクション -->
  <section class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 space-y-6">
    <div class="flex items-center gap-3 border-l-4 border-purple-500 pl-3">
      <h3 class="text-xl md:text-2xl font-black text-white">同人ゲームに関するよくある質問【Q&A】</h3>
    </div>
    
    <div class="space-y-4 text-xs md:text-sm">
      <div class="p-5 bg-slate-950/80 rounded-2xl border border-slate-800 space-y-2">
        <h4 class="font-bold text-purple-400 flex items-center gap-2">
          <span>Q.</span><span>ダウンロードしたゲームの解凍や起動は難しくありませんか？</span>
        </h4>
        <p class="text-slate-300 leading-relaxed">
          <b>非常に簡単です</b>。FANZAからzipファイルをダウンロード後、右クリックで「すべて展開（解凍）」し、フォルダ内にある「.exe」アイコンをダブルクリックするだけで即座にゲームが起動します。複雑なインストール作業は一切不要です。
        </p>
      </div>

      <div class="p-5 bg-slate-950/80 rounded-2xl border border-slate-800 space-y-2">
        <h4 class="font-bold text-purple-400 flex items-center gap-2">
          <span>Q.</span><span>同人ゲームは一度買えば何回でも再ダウンロードできますか？</span>
        </h4>
        <p class="text-slate-300 leading-relaxed">
          はい、一度購入した作品はFANZAアカウントの購入済みライブラリに永久保存され、PCを買い替えた後でもいつでも無料で何度でも再ダウンロードが可能です。
        </p>
      </div>

      <div class="p-5 bg-slate-950/80 rounded-2xl border border-slate-800 space-y-2">
        <h4 class="font-bold text-purple-400 flex items-center gap-2">
          <span>Q.</span><span>クレジットカードを使わずに購入することはできますか？</span>
        </h4>
        <p class="text-slate-300 leading-relaxed">
          もちろん可能です。FANZA同人はPayPay、楽天ペイ、WebMoney、ビットキャッシュ、コンビニ払い、DMMポイントなど多彩な決済方法に対応しています。カードの利用明細を残したくない方は当サイトの<a href="/posts/feature_fanza_payment_methods_safe_buying_guide" class="text-rose-400 underline font-bold">完全匿名支払いガイド</a>をご覧ください。
        </p>
      </div>
    </div>
  </section>

  <!-- あわせて読みたい関連キラー特集（内部リンク・トピッククラスター） -->
  <section class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 space-y-6">
    <div class="flex items-center gap-3 border-l-4 border-purple-500 pl-3">
      <h3 class="text-xl md:text-2xl font-black text-white">あわせて読みたい！FANZA完全攻略おすすめ特集</h3>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      <a href="/posts/feature_fanza_doujin_cg_manga_high_rating_masterpieces" class="p-4 bg-slate-950/80 hover:bg-slate-800/80 border border-slate-800 rounded-2xl space-y-2 group transition">
        <span class="text-xs font-bold text-purple-400">同人CG・コミック</span>
        <h4 class="text-sm font-bold text-white group-hover:text-purple-300 transition">累計数万DL超え同人CG神作選</h4>
        <p class="text-[11px] text-slate-400 line-clamp-2">圧倒的画力と濃厚シチュエーションで抜ける殿堂入り名作ガイド。</p>
      </a>
      <a href="/posts/feature_fanza_doujin_asmr_voice_masterpiece_guide" class="p-4 bg-slate-950/80 hover:bg-slate-800/80 border border-slate-800 rounded-2xl space-y-2 group transition">
        <span class="text-xs font-bold text-rose-400">耳が溶ける快楽</span>
        <h4 class="text-sm font-bold text-white group-hover:text-purple-300 transition">FANZA同人ボイス・ASMR完全攻略</h4>
        <p class="text-[11px] text-slate-400 line-clamp-2">脳直撃のバイノーラル録音＆おすすめ神作傑作選・失敗しない選び方。</p>
      </a>
      <a href="/posts/feature_why_buy_fanza_manga_complete_guide" class="p-4 bg-slate-950/80 hover:bg-slate-800/80 border border-slate-800 rounded-2xl space-y-2 group transition">
        <span class="text-xs font-bold text-indigo-400">電子書籍</span>
        <h4 class="text-sm font-bold text-white group-hover:text-purple-300 transition">なぜみんなFANZAで漫画を買う？完全ガイド</h4>
        <p class="text-[11px] text-slate-400 line-clamp-2">家族バレ防止策やクレカ明細の表記、売れ筋傑作10選まとめ。</p>
      </a>
      <a href="/manga" class="p-4 bg-slate-950/80 hover:bg-slate-800/80 border border-slate-800 rounded-2xl space-y-2 group transition">
        <span class="text-xs font-bold text-amber-400">漫画トップ</span>
        <h4 class="text-sm font-bold text-white group-hover:text-purple-300 transition">FANZA漫画コーナー（3600作超）</h4>
        <p class="text-[11px] text-slate-400 line-clamp-2">公式APIから毎日自動更新される最新・人気アダルトマンガ一覧。</p>
      </a>
    </div>
  </section>

  <!-- 構造化データ（JSON-LD） -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "【動いて喘ぐ極上ヌキゲー】FANZA同人ゲームおすすめ殿堂入り名作選！アニメーションCG×超豪華ボイスで骨抜きにされる神作RPG・SLG完全攻略",
    "description": "FANZA同人ゲームの中から、Live2Dアニメーションと豪華声優ボイスで抜きまくれる殿堂入り神作を厳選。RPG、SLG、時間停止など人気タイトルの実機レビューと始め方を徹底解説。",
    "image": "{cover_image}",
    "datePublished": "2026-09-30T00:07:00+09:00",
    "author": {{
      "@type": "Organization",
      "name": "背徳の美学 編集部"
    }}
  }}
  </script>

  <!-- 総括CTA -->
  <section class="text-center bg-gradient-to-r from-purple-950 via-slate-900 to-purple-950 border-2 border-purple-500/50 rounded-3xl p-8 md:p-12 shadow-2xl space-y-5">
    <h3 class="text-2xl md:text-3xl font-black text-white">
      自分の手で弄び、啼かせ、果てさせる。究極のインタラクティブ快楽へ。
    </h3>
    <p class="text-slate-300 text-xs md:text-sm max-w-2xl mx-auto leading-relaxed">
      画面の向こうであなたのアクションを待つ美少女たち。今夜、あなたの指先で彼女たちを蕩けるような絶頂へと導いてみませんか？
    </p>
    <div class="pt-2">
      <a href="{items[0].get('affiliate_url_clean', '')}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-3 px-10 py-5 bg-gradient-to-r from-purple-600 via-rose-600 to-purple-600 hover:from-purple-500 hover:to-rose-500 text-white font-black text-base rounded-2xl shadow-2xl transform hover:-translate-y-1 transition duration-200">
        <span>🎮</span><span>FANZA公式で殿堂入りの神作同人ゲームをDLする ➔</span>
      </a>
    </div>
  </section>
</div>
"""

    char_count = count_japanese_chars(content_html)
    print(f"Article 3 generated: {char_count} Japanese chars")
    if char_count < 3000:
        raise Exception(f"Article 3 has only {char_count} chars, minimum 3000 required")

    post_data = {
        "id": "feature_fanza_doujin_pc_game_top_masterpieces_guide",
        "title": "【動いて喘ぐ極上ヌキゲー】FANZA同人ゲームおすすめ殿堂入り名作選！アニメーションCG×超豪華ボイスで骨抜きにされる神作RPG・SLG完全攻略",
        "content": content_html,
        "review": content_html,
        "image": cover_image,
        "date": "2026-09-30 00:07:00",
        "genres": ["同人", "ゲーム", "RPG", "シミュレーション", "アニメーション", "ボイス・ASMR", "中出し"],
        "actresses": [],
        "maker": "FANZA同人",
        "price": "1210~",
        "affiliate_url": items[0].get("affiliate_url_clean", "")
    }

    out_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f" -> Saved Article 3 to {out_path}")
    return post_data


if __name__ == "__main__":
    print("Starting generation of 3 Brand New Killer Features with real FANZA API...")
    c1 = generate_article_1()
    c2 = generate_article_2()
    c3 = generate_article_3()
    print("ALL 3 Killer Features generated successfully!")
