# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・超大型キラー特集3記事自動生成スクリプト
1. 【極上の肉感と爆揺れ】FANZA「巨乳・美乳・爆乳」おすすめ殿堂入り神作TOP5＆歴代売上No.1クラス傑作選
2. 【脳が狂う背徳の悦楽】FANZA「NTR・寝取られ・略奪」おすすめ神作ランキングTOP5！
3. 【男の究極妄想】FANZA「逆レイプ・搾精・M男向けド痴女」おすすめ殿堂入り名作選！
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
# 記事1: 巨乳・爆乳・神乳特化
# ==============================================================================
def generate_article_1():
    print("=== Generating Article 1: Busty & Huge Tits Masterpieces ===")
    cids = ["pppd00993", "pred00674", "sone00866", "ssis00889", "mide00898"]
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
        raise Exception("Failed to fetch all 5 items for Article 1")

    cover_image = items[0].get("imageURL", {}).get("large", "")

    reviews = [
        # 1: pppd00993 夕美しおん
        {
            "rank": "01",
            "badge": "殿堂入り圧倒的No.1 / 逆バニー爆乳パイズリ",
            "subtitle": "こぼれ落ちる豊満バストで肉棒を包み込む！逆バニー×高級エステの極上密着ご奉仕",
            "body": """<b>【視覚と触覚が狂う逆バニー姿と、窒息寸前の超濃密パイズリ】</b>：<br>
布面積極少のハイレグ逆バニーに身を包んだ夕美しおんが、規格外の柔らかさを誇る美巨乳を惜しげもなく押し当ててくる超高級メンズエステ体験。<br>
オイルでぬらぬらと濡れ光る双丘の谷間に肉棒を挟み込み、上目遣いで耳元に吐息を吹きかけながらギュウギュウと押し潰すようにしごき上げるパイズリテクニックはまさに昇天必至。先端から溢れ出す我慢汁を乳房全体に塗りたくりながら、さらに腰をグラインドさせて結合部を密着させます。<br>
そのまま我慢限界のペニスを生挿入すれば、肉厚な膣壁がバキュームのように締め付け、逆バニーの胸元を激しく揺らしながら乱れ狂う本気イキへと突入。おっぱい好きなら一度は脳裏に焼き付けるべき、贅沢の極みのような濃厚密着作です。""",
            "climax": "両手で巨大な胸を寄せて亀頭を完全に飲み込み、息遣いを乱しながら一滴残らずザーメンを搾り取った直後の恍惚笑顔。"
        },
        # 2: pred00674 楪カレン
        {
            "rank": "02",
            "badge": "色気爆発 / スナックママの濃密中出し不倫",
            "subtitle": "夜の街で出会った色気ムンムンの豊満お姉さん！カウンター裏と密室で貪り合う肉欲の宴",
            "body": """<b>【男を惑わす大人のフェロモンと、服の上からでも主張するデカ乳ボイン】</b>：<br>
スナックのカウンター越しに胸元をチラつかせ、耳打ちするように酒を注いでくる妖艶なママ・楪カレン。酒と香水の匂いが混ざり合う密室で二人きりになった瞬間、抑えきれない欲望が爆発します。<br>
ドレスを捲り上げられて露わになった白く弾力のある爆乳は、揉むたびに手のひらから溢れ出し、指の隙間からこぼれるほどの質量感。男にしがみつかれながら乳首を甘噛みされると、甘い喘ぎ声を漏らして秘部をびしょ濡れにしていきます。アフターのホテルで繰り広げられる本番では、男の上に跨がって豊満なバストを上下左右に波打たせながらの激しいグラインド騎乗位。大人のオンナが快楽に溺れていく生々しい表情と肉体の躍動が、観る者の理性を粉々に破壊します。""",
            "climax": "対面座位で巨乳を顔面に押し付けられ、息ができないほどの肉圧の中で膣奥深くへドロドロの白濁液を注ぎ込む濃厚射精。"
        },
        # 3: sone00866 木村愛心
        {
            "rank": "03",
            "badge": "規格外Lカップ / 甘やかしおっぱい風俗",
            "subtitle": "頭を丸ごと包み込む神の果実！異次元のLカップ美女が全てを許し甘えさせてくれる究極癒やし",
            "body": """<b>【人類の夢がここに！触れれば沈み込む異次元クラスの超巨大マシュマロバスト】</b>：<br>
驚異のLカップを誇る癒やし系女神・木村愛心が、疲れた男の全てを包み込んでくれる風俗シチュエーション。<br>
もはや枕のように巨大でフワフワな胸に顔を埋め、赤子のように甘やかされながら受ける洗体とパイズリは、現代のストレスを一瞬で吹き飛ばす圧倒的快感です。重力に逆らえないほどの重量感を持つバストが、男の腰振りに合わせてドサドサと激しく跳ね回るバックピストンは圧巻の一言。おっぱいの揺れと肉のぶつかり合う重低音、そして彼女の優しく包容力あふれる囁き声が重なり合い、下半身への血流が一気に限界を突破します。とにかくデカくて柔らかい本物の胸に溺れたい人にとって、これ以上の楽園はありません。""",
            "climax": "背後から両手で重たいLカップを掴み上げ、激ピストンで膣奥を突き上げながら乳房を波打たせる同時絶頂。"
        },
        # 4: ssis00889 みなみ羽琉
        {
            "rank": "04",
            "badge": "高身長×Kカップ / 圧巻の黄金比プロポーション",
            "subtitle": "身長175cm・バスト108cm！日本人離れしたダイナミックボディが躍動する歴史的デビュー作",
            "body": """<b>【モデル級の長身スレンダーに搭載された奇跡のKカップ天然美巨乳】</b>：<br>
画面を覆い尽くすほどの迫力を持つ、身長175cm・胸囲108cmの超大型新人・みなみ羽琉（みなと羽琉）の鮮烈なインパクト。<br>
引き締まった美くびれと長い美脚、そしてその上に堂々とそびえ立つ重量級のバストのコントラストが芸術的な美しさを放ちます。ベッドの上で四つん這いにさせると、重力で垂れ下がる巨乳が男の視界をジャック。激しいピストンに合わせてダイナミックに円を描いて揺れる様子は、CGでも再現不可能な本物の生々しさです。初めての快楽に戸惑いながらも、次第に身体を弓なりに反らせて淫らに悦びを覚えていくピュアな反応も破壊力抜群。視覚的な美しさとエロティシズムが高次元で融合した必見作です。""",
            "climax": "長い脚を大きく広げた正常位で、巨乳を揉みしだかれながら初めての子宮ノックにビクビクと体を震わせる限界昇天。"
        },
        # 5: mide00898 水卜さくら
        {
            "rank": "05",
            "badge": "美少女×至高の美乳 / 温泉旅館ハメ狂い",
            "subtitle": "可憐なフェイスに隠された極上美乳！嫌悪が快楽へと塗り替えられていく濃密温泉接待",
            "body": """<b>【透き通るような白肌と、手のひらに吸い付くようなパーフェクト美乳の誘惑】</b>：<br>
圧倒的透明感を持つ美少女・水卜さくらが、オヤジ上司の罠に嵌められ、逃げ場のない温泉旅館で一晩中抱かれ続ける濃密ドラマ。<br>
湯煙の中で露わになる彼女の胸は、形、弾力、乳首の色合いに至るまで全てが完璧な黄金比。浴衣をはだけさせられ、嫌がりながらも敏感な乳首を転がされるうちに、吐息が次第に艶めかしい嬌声へと変化していきます。畳の上で乱暴に突かれ、純白の巨乳がパシャパシャと音を立てて激しく弾けるシーンは背徳感の極致。清楚な美少女が肉欲の快楽に屈服し、自分の意志に反してアソコを濡らして狂っていく姿に、男の本能的なサディズムが激しく刺激されます。""",
            "climax": "温泉上がりの火照った体で後ろから激突され、涙目になりながらも巨乳を揺らして何度も潮を吹き上げる連続痙攣。"
        }
    ]

    # HTML生成
    html = f"""<div class="space-y-10 text-slate-200 leading-relaxed font-sans">

    <!-- 導入部リード文 -->
    <div class="bg-gradient-to-br from-slate-900 via-rose-950/40 to-slate-900 border border-rose-500/30 rounded-2xl p-6 sm:p-8 shadow-2xl backdrop-blur-sm">
        <div class="flex items-center space-x-2 text-rose-400 text-sm font-bold uppercase tracking-widest mb-3">
            <span class="w-2.5 h-2.5 rounded-full bg-rose-500 animate-ping"></span>
            <span>FANZA BUSTY & HUGE TITS SELECTION</span>
        </div>
        <h1 class="text-2xl sm:text-3xl font-black text-white tracking-tight mb-4">
            【極上の肉感と爆揺れ】FANZA「巨乳・美乳・爆乳」おすすめ殿堂入り神作TOP5＆歴代売上No.1クラス傑作選
        </h1>
        <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-4">
            男の根源的な欲望を刺激してやまない「おっぱい」。画面いっぱいに広がる圧倒的な質量感、手のひらからこぼれ落ちる柔らかさ、そして激しい腰振りに呼応して乱れ狂うダイナミックな揺れ――巨乳作品には、他のジャンルでは絶対に味わえない唯一無二の多幸感と視覚的快楽が存在します。
        </p>
        <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-4">
            しかしFANZA内に無数に存在するタイトルの中から、「本当に胸の造形が美しく、パイズリや揺れの演出が神がかっている作品」を見極めるのは容易ではありません。
        </p>
        <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
            本記事では、FANZAで歴代トップクラスの売上と高評価レビューを誇る<strong>「本物の巨乳・美乳・爆乳名作」</strong>を厳選。JカップやLカップの超ド級肉感から、息を呑む造形美を誇る美乳まで、今夜のオナニーを最高峰の射精体験へと導く珠玉の5本を詳細に解説します。
        </p>
    </div>

    <!-- おっぱい作品で失敗しない選び方・3つの鑑賞ポイント -->
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 sm:p-8 shadow-xl">
        <h2 class="text-xl sm:text-2xl font-bold text-white mb-6 flex items-center gap-3 border-b border-slate-800 pb-4">
            <span class="p-2 bg-rose-500/20 text-rose-400 rounded-lg text-lg">💡</span>
            <span>巨乳・爆乳作品を120%楽しむための3大チェックポイント</span>
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div class="bg-slate-800/60 p-5 rounded-xl border border-slate-700/60 hover:border-rose-500/50 transition">
                <div class="text-rose-400 font-bold text-base mb-2">① 肉感と重力を感じる「揺れ」</div>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
                    単にサイズが大きいだけでなく、騎乗位やバック時に重力に従ってドサドサと躍動する「生々しい揺れ」があるかを重視。カメラアングルの良さが快感を何倍にも高めます。
                </p>
            </div>
            <div class="bg-slate-800/60 p-5 rounded-xl border border-slate-700/60 hover:border-rose-500/50 transition">
                <div class="text-rose-400 font-bold text-base mb-2">② 密着度MAXの「パイズリ＆挟まれ」</div>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
                    ペニス全体を胸の肉で完全に覆い隠し、ローションや体液でぬらぬらとしごき上げるパイズリシーンのクオリティ。女優の吐息や上目遣いの表情も重要な抜き要素です。
                </p>
            </div>
            <div class="bg-slate-800/60 p-5 rounded-xl border border-slate-700/60 hover:border-rose-500/50 transition">
                <div class="text-rose-400 font-bold text-base mb-2">③ 乳首への愛撫と女優のガチ反応</div>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
                    先端の感度が高く、指先で摘まれたり舌で転がされるだけで腰を浮かせて喘ぎ声を漏らす本気のアクメ反応。胸を責められることで濡れそぼる秘部との連動が見どころです。
                </p>
            </div>
        </div>
    </div>

    <!-- メインランキングセクション -->
    <div class="space-y-12">
        <h2 class="text-2xl sm:text-3xl font-black text-white tracking-tight flex items-center gap-3">
            <span class="w-2 h-8 bg-rose-500 rounded-full inline-block"></span>
            <span>FANZA巨乳・美乳・爆乳おすすめ神作ランキングTOP5</span>
        </h2>
"""

    for i, it in enumerate(items):
        r = reviews[i]
        title = it.get("title", "")
        cid = it.get("content_id", "")
        aff_url = it.get("affiliate_url_clean", "")
        cover_img = it.get("imageURL", {}).get("large", "")
        sample_imgs = get_sample_images(it, 4)
        review_count = it.get("review", {}).get("count", 0)
        review_rate = it.get("review", {}).get("average", "4.5")
        
        actress_names = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        actress_html_list = [get_actress_link(name) for name in actress_names]
        actress_str = " / ".join(actress_html_list) if actress_html_list else "専属女優"
        
        genre_names = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        genre_html_list = [get_genre_link(g) for g in genre_names[:6]]
        genre_str = " ".join(genre_html_list)

        sample_img_html = ""
        if sample_imgs:
            sample_img_html = '<div class="grid grid-cols-2 sm:grid-cols-4 gap-2 mt-4">'
            for s_img in sample_imgs:
                sample_img_html += f'<div class="overflow-hidden rounded-lg border border-slate-700/60 aspect-video bg-slate-800"><img src="{s_img}" alt="{title} サンプル場面写真" class="w-full h-full object-cover hover:scale-105 transition duration-300" loading="lazy"></div>'
            sample_img_html += '</div>'

        html += f"""
        <!-- 作品カード {r['rank']} -->
        <div class="bg-slate-900 border border-slate-800 hover:border-rose-500/50 rounded-2xl overflow-hidden shadow-2xl transition duration-300">
            <div class="p-5 sm:p-7 border-b border-slate-800 flex flex-wrap items-center justify-between gap-3 bg-slate-950/40">
                <div class="flex items-center gap-3">
                    <span class="flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-rose-500 to-pink-600 text-white font-black text-xl shadow-lg shadow-rose-900/40">
                        {r['rank']}
                    </span>
                    <span class="text-xs sm:text-sm font-bold text-rose-400 bg-rose-950/60 border border-rose-800/60 px-3 py-1 rounded-full">
                        {r['badge']}
                    </span>
                </div>
                <div class="flex items-center gap-2 text-amber-400 font-bold text-sm bg-slate-900 px-3 py-1 rounded-lg border border-slate-800">
                    <span>★ {review_rate}</span>
                    <span class="text-slate-500 text-xs">({review_count}件の公式レビュー)</span>
                </div>
            </div>

            <div class="p-5 sm:p-8 space-y-6">
                <h3 class="text-lg sm:text-2xl font-black text-white leading-snug hover:text-rose-400 transition">
                    <a href="{aff_url}" target="_blank" rel="nofollow noopener">{title}</a>
                </h3>

                <div class="text-rose-300 font-bold text-base sm:text-lg border-l-4 border-rose-500 pl-3">
                    {r['subtitle']}
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
                    <div class="lg:col-span-5 space-y-3">
                        <div class="relative group rounded-xl overflow-hidden border border-slate-700 shadow-xl bg-slate-950">
                            <a href="{aff_url}" target="_blank" rel="nofollow noopener">
                                <img src="{cover_img}" alt="{title} 公式パッケージ画像" class="w-full h-auto object-cover group-hover:scale-102 transition duration-300" loading="lazy">
                                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition flex items-end justify-center p-4">
                                    <span class="text-white font-bold text-sm bg-rose-600 px-4 py-2 rounded-full shadow-lg">FANZA公式で高画質サンプルを見る</span>
                                </div>
                            </a>
                        </div>
                    </div>

                    <div class="lg:col-span-7 space-y-4">
                        <div class="text-slate-300 text-sm sm:text-base leading-relaxed">
                            {r['body']}
                        </div>

                        <div class="bg-rose-950/30 border border-rose-800/40 rounded-xl p-4">
                            <div class="text-rose-400 font-bold text-xs uppercase tracking-wider mb-1 flex items-center gap-1.5">
                                <span>⚡</span> ここで抜く！決定的昇天シーン
                            </div>
                            <div class="text-white text-sm font-medium leading-relaxed">
                                {r['climax']}
                            </div>
                        </div>

                        <div class="space-y-2 pt-2 text-xs">
                            <div class="flex items-center gap-2">
                                <span class="text-slate-400 font-semibold">主演女優:</span>
                                <span class="text-slate-200">{actress_str}</span>
                            </div>
                            <div class="flex flex-wrap items-center gap-1.5 pt-1">
                                <span class="text-slate-400 font-semibold mr-1">関連タグ:</span>
                                {genre_str}
                            </div>
                        </div>
                    </div>
                </div>

                <!-- サンプル画像プレビュー -->
                <div>
                    <div class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-1">
                        📸 劇中ハイライトプレビュー
                    </div>
                    {sample_img_html}
                </div>

                <!-- CTAボタン -->
                <div class="pt-2">
                    <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block w-full text-center bg-gradient-to-r from-rose-600 via-pink-600 to-rose-600 hover:from-rose-500 hover:to-pink-500 text-white font-black py-4 px-6 rounded-xl shadow-xl hover:shadow-rose-900/50 transition transform hover:-translate-y-0.5 text-base sm:text-lg">
                        👉 『{title[:25]}…』をFANZA公式で今すぐ無料サンプル視聴する
                    </a>
                </div>
            </div>
        </div>
        """

    html += f"""
    </div>

    <!-- 巨乳作品の楽しみ方をさらに深めるQ&A -->
    <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 sm:p-8 space-y-6">
        <h2 class="text-xl sm:text-2xl font-bold text-white flex items-center gap-3 border-b border-slate-800 pb-4">
            <span class="text-rose-400">❓</span>
            <span>巨乳・爆乳ジャンルに関するよくある疑問と回答</span>
        </h2>
        <div class="space-y-4">
            <div class="bg-slate-800/50 p-5 rounded-xl border border-slate-700/50">
                <h4 class="text-white font-bold text-sm sm:text-base mb-2">Q. パイズリシーンで本当に気持ちよく抜ける作品の特徴は？</h4>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
                    A. パイズリで最も重要なのは「密着度」と「女優の表情」です。胸の間に隙間ができず、亀頭から竿全体までが肉の圧力で押し包まれていること、そしてローションや唾液が絡むジュポジュポという生々しい水音がクリアに録音されている作品を選ぶと、没入感が段違いになります。
                </p>
            </div>
            <div class="bg-slate-800/50 p-5 rounded-xl border border-slate-700/50">
                <h4 class="text-white font-bold text-sm sm:text-base mb-2">Q. スマホやタブレットで視聴する場合、画質はどれくらいがおすすめ？</h4>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
                    A. 巨乳作品は肌の質感や汗の滴り、乳首の立ち上がりなどの微細な描写が興奮の鍵を握るため、FANZA公式プレイヤーの「HD画質（フルHD）」以上でのダウンロード視聴を強く推奨します。細部まで鮮明に見えることで、まるで目の前でおっぱいが揺れているかのような錯覚を楽しめます。
                </p>
            </div>
        </div>
    </div>

    <!-- サイト内関連記事リンク -->
    <div class="bg-slate-950 border border-slate-800 rounded-2xl p-6 sm:p-8">
        <h3 class="text-lg font-bold text-white mb-4 flex items-center gap-2">
            <span class="text-rose-400">🔗</span> あわせて読みたいおすすめ特集
        </h3>
        <ul class="space-y-3 text-sm">
            <li>
                <a href="/posts/feature_fanza_top_exclusive_actresses_ranking_masterpiece" class="text-rose-400 hover:text-rose-300 underline font-semibold transition">
                    👉 【2026年最新】FANZAで今もっとも抜ける「単体専属トップ女優」最強ランキング＆絶対に後悔しない歴史的代表作おすすめ傑作選
                </a>
            </li>
            <li>
                <a href="/posts/feature_fanza_super_long_omnibus_best_selection_ranking" class="text-rose-400 hover:text-rose-300 underline font-semibold transition">
                    👉 【コスパ最強の極致】FANZA超長尺BEST・歴代神作総集編（8時間〜16時間）おすすめ傑作選！1本で数十回抜ける大容量パック完全攻略
                </a>
            </li>
            <li>
                <a href="/posts/feature_fanza_mature_milf_wives_best_selection_ranking" class="text-rose-400 hover:text-rose-300 underline font-semibold transition">
                    👉 【2026年最新】FANZAで最も売れている「人妻・美熟女」神作ランキングTOP5＆絶対抜ける殿堂入り名作傑作選
                </a>
            </li>
        </ul>
    </div>

</div>"""

    post_data = {
        "id": "feature_fanza_busty_huge_tits_masterpieces_ranking",
        "title": "【極上の肉感と爆揺れ】FANZA「巨乳・美乳・爆乳」おすすめ殿堂入り神作TOP5＆歴代売上No.1クラス傑作選【パイズリ・挟まれ・乳フェチ必見】",
        "content": html,
        "review": "FANZAで歴代圧倒的人気を誇る巨乳・爆乳・美乳の殿堂入り名作を徹底特集。JカップやLカップの重量級バストから完璧なプロポーションの美乳まで、パイズリと激揺れSEXが堪能できる超人気神作TOP5。",
        "image": cover_image,
        "date": "2026-09-30 08:40:00",
        "genres": ["巨乳", "爆乳", "パイズリ", "美乳", "ハイビジョン", "独占配信", "メンズエステ", "騎乗位"],
        "actresses": ["夕美しおん", "楪カレン", "木村愛心", "みなみ羽琉", "水卜さくら"],
        "maker": "FANZA",
        "price": "500円〜",
        "affiliate_url": items[0].get("affiliate_url_clean", "")
    }

    file_path = os.path.join(OUTPUT_DIR, "feature_fanza_busty_huge_tits_masterpieces_ranking.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)

    char_count = count_japanese_chars(html)
    print(f" -> Successfully saved Article 1 ({char_count} chars): {file_path}")


# ==============================================================================
# 記事2: NTR・寝取られ特化
# ==============================================================================
def generate_article_2():
    print("=== Generating Article 2: NTR & Netorare Cuckold Masterpieces ===")
    cids = ["adn00325", "adn00397", "dasd00958", "1start00633", "meyd00844"]
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
        raise Exception("Failed to fetch all 5 items for Article 2")

    cover_image = items[0].get("imageURL", {}).get("large", "")

    reviews = [
        # 1: adn00325 向井藍
        {
            "rank": "01",
            "badge": "ATTACKERS最高峰 / 夫の目の前で寝取られ",
            "subtitle": "縛り付けられた夫の視線の先で…かつての暴漢に身体を弄ばれ快楽に屈服する哀しい人妻",
            "body": """<b>【息の詰まる緊張感と、夫への罪悪感に抗えない肉体の裏切り】</b>：<br>
NTRジャンルの金字塔レーベル「アタッカーズ」が放つ、胸を抉るような背徳ドラマの最高傑作。平穏な幸せを築いていた向井藍の前に、かつて彼女を蹂躙した忌まわしい男が再び現れます。<br>
拘束され声を出すこともできない夫の目の前で、着物を剥ぎ取られ、白く美しい身体を執拗に愛撫されていく妻。最初は涙を流して拒絶していたものの、男の凶暴な指使いと肉棒の快楽に徐々に抗えなくなり、膣内を愛液で濡らしていきます。夫と目が合うたびに羞恥と罪悪感で顔を歪めながらも、奥深くまで突き刺さるピストンに自ら腰を密着させてしまう背徳のリアリズム。心理描写の緊迫感とエロティシズムが極限まで高められた、NTRファン必携の歴史的名盤です。""",
            "climax": "夫の涙ながらの視線を受け止めながら、男の肉棒に子宮を突かれて声にならない絶叫アクメを漏らす瞬間。"
        },
        # 2: adn00397 藤田こずえ
        {
            "rank": "02",
            "badge": "鬼畜上司×オフィス玩具化 / 逃げられない屈従",
            "subtitle": "清楚な美人OLが密室で調教される！彼氏に言えない秘密の快楽と社内性奴隷化",
            "body": """<b>【エリートOLのプライドが崩壊し、上司の性処理ペットへと堕ちる快楽地獄】</b>：<br>
非の打ち所がない美しい容姿と知性を持つOL・藤田こずえが、立場を利用した鬼畜上司の罠によって逃げ場を失っていくオフィスNTRの傑作。<br>
彼氏とのデートの約束があるにもかかわらず、残業時間の会議室や役員室で下着を奪われ、バイブや手淫でアソコを弄ばれます。机に手をつかされ、後ろからスーツのスカートを捲り上げられて生挿入される屈辱。彼氏からの着信音が鳴り響く中で、上司の激しいピストンに耐えきれず「あんっ…ダメです…！」と甘い嬌声を漏らしてしまう姿はゾクゾクするほどの背徳感を呼び起こします。清楚な女性が欲望に抗えず崩れていくグラデーションが完璧に描かれています。""",
            "climax": "彼氏と通話させられた状態で後ろから突かれ、声を押し殺しながら膣内へドクドクと中出しされるオフィス密室SEX。"
        },
        # 3: dasd00958 篠田ゆう
        {
            "rank": "03",
            "badge": "DAS!人格崩壊シリーズ / 媚薬×元カレ快楽堕ち",
            "subtitle": "大嫌いな元カレの媚薬にカラダが震える！ヨダレと精子まみれで理性が吹き飛ぶ限界アクメ",
            "body": """<b>【極上ボディの篠田ゆうが魅せる、本能剥き出しのトランス絶頂アヘ顔】</b>：<br>
完璧なプロポーションと美貌を誇る篠田ゆうが、強烈な媚薬を盛られて理性を完全に破壊されるDAS!の大ヒットシリーズ。<br>
心では激しく拒絶しているのに、媚薬によって感度を何十倍にも跳ね上げられた肉体は、指先が触れるだけでビクビクと痙攣。大嫌いなはずの元カレの肉棒を口いっぱいに咥え込まされ、ヨダレを垂らしながら夢中で貪り始めます。ベッドの上で腰をガクガクと震わせ、白目を剥きながら「もっと奥まで突いてぇ！」とおねだりする姿はまさに快楽の狂気。男優たちの濃厚なザーメンを顔面と口内に浴びせられ、精子まみれになりながら恍惚の笑みを浮かべる圧巻のラストまでノンストップで脳が痺れます。""",
            "climax": "媚薬で敏感になりすぎたクリトリスを擦られながらの連続ピストンで、身体を激しく弓なりに反らせて潮を吹き散らす人格崩壊アクメ。"
        },
        # 4: 1start00633 唯井まひろ
        {
            "rank": "04",
            "badge": "妊活NTR / 30日間の生中出し着床記録",
            "subtitle": "「アナタ以外の人で妊娠するところ見てて…」新婚夫婦の絶望と快楽が交錯する着床NTR",
            "body": """<b>【子宝に恵まれない夫婦の選択…他人の種付けに溺れていく若妻の禁断記録】</b>：<br>
天使のような透明感を持つ人気女優・唯井まひろが、不妊に悩む夫のために選んだ「他人の精子による妊娠」という極限のシチュエーション。<br>
最初は夫への愛情のために義務として他人の肉棒を受け入れていた若妻が、日に日に濃厚になる生ハメと中出しの快感に目覚めていきます。夫の目の前で逞しい男に抱かれ、奥深くまで種付けされるたびに、罪悪感を忘れ去ったような淫らな表情へと変貌。30日間の記録の中で、次第に自ら腰を振って精液を欲しがるようになる心理変化が痛烈に突き刺さります。切なさと濃密なエロスが同居する、感情を激しく揺さぶる傑作です。""",
            "climax": "夫が見守る真横で、排卵日の膣奥へ大量のザーメンを流し込まれ、子宮を愛撫されて蕩けきった笑顔を見せる瞬間。"
        },
        # 5: meyd00844 佐山愛
        {
            "rank": "05",
            "badge": "美熟女教師 / 真夜中のプール輪姦",
            "subtitle": "夜の学校で犯される豊満人妻！不良生徒たちの若く逞しい肉棒に群がられる背徳の罠",
            "body": """<b>【グラマラスボディの熟女教師が、夜の静寂に響かせる狂おしい絶頂喘ぎ】</b>：<br>
圧倒的な肉感と包容力を持つ佐山愛が、真夜中の学校のプールサイドで複数の男たちに囲まれるハードNTR。<br>
水着を引き裂かれ、月明かりの下で水滴を弾く豊満な肉体が無遠慮に弄ばれます。教師としての威厳を保とうとする言葉も虚しく、代わる代わる挿入される若い肉棒の激しい突き上げに、次第に理性を失い腰をくねらせていく様は壮絶。水飛沫と肉のぶつかる音が静かな夜のプールに反響し、幾重にも重なるピストンによって完全に肉便器へと堕とされていきます。熟女の肉体美と輪姦シチュエーションが完璧に融合した名作です。""",
            "climax": "プールサイドに押し倒され、前後から同時に責め立てられながら満月の下で絶頂を繰り返す濃密アクメ。"
        }
    ]

    html = f"""<div class="space-y-10 text-slate-200 leading-relaxed font-sans">

    <!-- 導入部リード文 -->
    <div class="bg-gradient-to-br from-slate-900 via-purple-950/40 to-slate-900 border border-purple-500/30 rounded-2xl p-6 sm:p-8 shadow-2xl backdrop-blur-sm">
        <div class="flex items-center space-x-2 text-purple-400 text-sm font-bold uppercase tracking-widest mb-3">
            <span class="w-2.5 h-2.5 rounded-full bg-purple-500 animate-ping"></span>
            <span>FANZA NTR & NETORARE SELECTION</span>
        </div>
        <h1 class="text-2xl sm:text-3xl font-black text-white tracking-tight mb-4">
            【脳が狂う背徳の悦楽】FANZA「NTR・寝取られ・略奪」おすすめ神作ランキングTOP5！最愛の彼女・妻が絶倫チンポに堕ちていく歴代最高傑作選
        </h1>
        <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-4">
            愛する女性が他人の男に抱かれ、最初は激しく拒絶しながらも、次第に肉体の快楽に抗えなくなり理性を奪われていく――「NTR（寝取られ）」ジャンルには、男の嫉妬心、背徳感、そして禁断の興奮を極限まで掻き立てる強烈な魔力が潜んでいます。
        </p>
        <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-4">
            心理的なドラマ性の高さと生々しい肉欲のコントラストこそがNTRの真髄であり、単なる抜きを超えて脳の芯まで痺れるようなカタルシスをもたらします。
        </p>
        <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
            本記事では、アタッカーズをはじめとする名門レーベルが生み出した<strong>「FANZA歴代屈指の寝取られ神作」</strong>を厳選。夫の目の前での陵辱、オフィスでの性奴隷化、媚薬による人格崩壊、妊活種付けまで、観る者の脳をバグらせる圧倒的クオリティの5作品を完全解説します。
        </p>
    </div>

    <!-- NTR作品の醍醐味・3つの鑑賞ポイント -->
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 sm:p-8 shadow-xl">
        <h2 class="text-xl sm:text-2xl font-bold text-white mb-6 flex items-center gap-3 border-b border-slate-800 pb-4">
            <span class="p-2 bg-purple-500/20 text-purple-400 rounded-lg text-lg">💔</span>
            <span>NTR・寝取られ作品で脳汁を噴出させる3つの鑑賞ポイント</span>
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div class="bg-slate-800/60 p-5 rounded-xl border border-slate-700/60 hover:border-purple-500/50 transition">
                <div class="text-purple-400 font-bold text-base mb-2">① 「拒絶」から「快楽屈服」へのグラデーション</div>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
                    最初は涙を流して嫌がっていたヒロインが、執拗な愛撫と絶倫ピストンによって身体を裏切られ、甘い喘ぎ声を漏らしてしまう瞬間の表情変化。
                </p>
            </div>
            <div class="bg-slate-800/60 p-5 rounded-xl border border-slate-700/60 hover:border-purple-500/50 transition">
                <div class="text-purple-400 font-bold text-base mb-2">② 夫・彼氏への「罪悪感」と背徳の視線</div>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
                    電話越しの声、あるいは拘束された夫の目の前で犯されるシチュエーション。愛する相手を意識しながらも肉棒に腰を振ってしまう背徳の極致。
                </p>
            </div>
            <div class="bg-slate-800/60 p-5 rounded-xl border border-slate-700/60 hover:border-purple-500/50 transition">
                <div class="text-purple-400 font-bold text-base mb-2">③ 容赦のない「濃厚生中出し」と種付け</div>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
                    他人の精液で満たされたアソコから白濁液が溢れ出し、完全に肉体を奪われたことを決定づける決定的な中出しシーンの破壊力。
                </p>
            </div>
        </div>
    </div>

    <!-- メインランキングセクション -->
    <div class="space-y-12">
        <h2 class="text-2xl sm:text-3xl font-black text-white tracking-tight flex items-center gap-3">
            <span class="w-2 h-8 bg-purple-500 rounded-full inline-block"></span>
            <span>FANZA寝取られ・NTRおすすめ神作ランキングTOP5</span>
        </h2>
"""

    for i, it in enumerate(items):
        r = reviews[i]
        title = it.get("title", "")
        cid = it.get("content_id", "")
        aff_url = it.get("affiliate_url_clean", "")
        cover_img = it.get("imageURL", {}).get("large", "")
        sample_imgs = get_sample_images(it, 4)
        review_count = it.get("review", {}).get("count", 0)
        review_rate = it.get("review", {}).get("average", "4.5")
        
        actress_names = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        actress_html_list = [get_actress_link(name) for name in actress_names]
        actress_str = " / ".join(actress_html_list) if actress_html_list else "専属女優"
        
        genre_names = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        genre_html_list = [get_genre_link(g) for g in genre_names[:6]]
        genre_str = " ".join(genre_html_list)

        sample_img_html = ""
        if sample_imgs:
            sample_img_html = '<div class="grid grid-cols-2 sm:grid-cols-4 gap-2 mt-4">'
            for s_img in sample_imgs:
                sample_img_html += f'<div class="overflow-hidden rounded-lg border border-slate-700/60 aspect-video bg-slate-800"><img src="{s_img}" alt="{title} サンプル場面写真" class="w-full h-full object-cover hover:scale-105 transition duration-300" loading="lazy"></div>'
            sample_img_html += '</div>'

        html += f"""
        <!-- 作品カード {r['rank']} -->
        <div class="bg-slate-900 border border-slate-800 hover:border-purple-500/50 rounded-2xl overflow-hidden shadow-2xl transition duration-300">
            <div class="p-5 sm:p-7 border-b border-slate-800 flex flex-wrap items-center justify-between gap-3 bg-slate-950/40">
                <div class="flex items-center gap-3">
                    <span class="flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-purple-500 to-indigo-600 text-white font-black text-xl shadow-lg shadow-purple-900/40">
                        {r['rank']}
                    </span>
                    <span class="text-xs sm:text-sm font-bold text-purple-400 bg-purple-950/60 border border-purple-800/60 px-3 py-1 rounded-full">
                        {r['badge']}
                    </span>
                </div>
                <div class="flex items-center gap-2 text-amber-400 font-bold text-sm bg-slate-900 px-3 py-1 rounded-lg border border-slate-800">
                    <span>★ {review_rate}</span>
                    <span class="text-slate-500 text-xs">({review_count}件の公式レビュー)</span>
                </div>
            </div>

            <div class="p-5 sm:p-8 space-y-6">
                <h3 class="text-lg sm:text-2xl font-black text-white leading-snug hover:text-purple-400 transition">
                    <a href="{aff_url}" target="_blank" rel="nofollow noopener">{title}</a>
                </h3>

                <div class="text-purple-300 font-bold text-base sm:text-lg border-l-4 border-purple-500 pl-3">
                    {r['subtitle']}
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
                    <div class="lg:col-span-5 space-y-3">
                        <div class="relative group rounded-xl overflow-hidden border border-slate-700 shadow-xl bg-slate-950">
                            <a href="{aff_url}" target="_blank" rel="nofollow noopener">
                                <img src="{cover_img}" alt="{title} 公式パッケージ画像" class="w-full h-auto object-cover group-hover:scale-102 transition duration-300" loading="lazy">
                                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition flex items-end justify-center p-4">
                                    <span class="text-white font-bold text-sm bg-purple-600 px-4 py-2 rounded-full shadow-lg">FANZA公式で高画質サンプルを見る</span>
                                </div>
                            </a>
                        </div>
                    </div>

                    <div class="lg:col-span-7 space-y-4">
                        <div class="text-slate-300 text-sm sm:text-base leading-relaxed">
                            {r['body']}
                        </div>

                        <div class="bg-purple-950/30 border border-purple-800/40 rounded-xl p-4">
                            <div class="text-purple-400 font-bold text-xs uppercase tracking-wider mb-1 flex items-center gap-1.5">
                                <span>⚡</span> ここで抜く！決定的背徳シーン
                            </div>
                            <div class="text-white text-sm font-medium leading-relaxed">
                                {r['climax']}
                            </div>
                        </div>

                        <div class="space-y-2 pt-2 text-xs">
                            <div class="flex items-center gap-2">
                                <span class="text-slate-400 font-semibold">主演女優:</span>
                                <span class="text-slate-200">{actress_str}</span>
                            </div>
                            <div class="flex flex-wrap items-center gap-1.5 pt-1">
                                <span class="text-slate-400 font-semibold mr-1">関連タグ:</span>
                                {genre_str}
                            </div>
                        </div>
                    </div>
                </div>

                <!-- サンプル画像プレビュー -->
                <div>
                    <div class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-1">
                        📸 劇中ハイライトプレビュー
                    </div>
                    {sample_img_html}
                </div>

                <!-- CTAボタン -->
                <div class="pt-2">
                    <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block w-full text-center bg-gradient-to-r from-purple-600 via-indigo-600 to-purple-600 hover:from-purple-500 hover:to-indigo-500 text-white font-black py-4 px-6 rounded-xl shadow-xl hover:shadow-purple-900/50 transition transform hover:-translate-y-0.5 text-base sm:text-lg">
                        👉 『{title[:25]}…』をFANZA公式で今すぐ無料サンプル視聴する
                    </a>
                </div>
            </div>
        </div>
        """

    html += f"""
    </div>

    <!-- サイト内関連記事リンク -->
    <div class="bg-slate-950 border border-slate-800 rounded-2xl p-6 sm:p-8">
        <h3 class="text-lg font-bold text-white mb-4 flex items-center gap-2">
            <span class="text-purple-400">🔗</span> あわせて読みたいおすすめ特集
        </h3>
        <ul class="space-y-3 text-sm">
            <li>
                <a href="/posts/feature_fanza_mature_milf_wives_best_selection_ranking" class="text-purple-400 hover:text-purple-300 underline font-semibold transition">
                    👉 【2026年最新】FANZAで最も売れている「人妻・美熟女」神作ランキングTOP5＆絶対抜ける殿堂入り名作傑作選
                </a>
            </li>
            <li>
                <a href="/posts/feature_fanza_magic_mirror_go_real_amateur_best_ranking" class="text-purple-400 hover:text-purple-300 underline font-semibold transition">
                    👉 【25年売れ続ける伝説】マジックミラー号＆リアル素人ナンパ傑作選！生々しい恥じらいと本気アクメに悶絶する歴代神回ランキング
                </a>
            </li>
            <li>
                <a href="/posts/feature_fanza_payment_methods_safe_buying_guide" class="text-purple-400 hover:text-purple-300 underline font-semibold transition">
                    👉 【クレカなし＆絶対家族バレしない】FANZAの安全な買い方・支払い方法完全ガイド！
                </a>
            </li>
        </ul>
    </div>

</div>"""

    post_data = {
        "id": "feature_fanza_ntr_netorare_cuckold_best_masterpieces",
        "title": "【脳が狂う背徳の悦楽】FANZA「NTR・寝取られ・略奪」おすすめ神作ランキングTOP5！最愛の彼女・妻が絶倫チンポに堕ちていく歴代最高傑作選",
        "content": html,
        "review": "FANZAで絶大な支持を集めるNTR・寝取られ・略奪ジャンルの最高傑作を特集。夫の目の前での調教、オフィス性奴隷、媚薬による快楽堕ちまで、背徳感と肉欲が脳を刺激するおすすめ神作TOP5。",
        "image": cover_image,
        "date": "2026-09-30 08:45:00",
        "genres": ["寝取られ", "NTR", "人妻", "不倫", "ハイビジョン", "独占配信", "オフィス", "媚薬"],
        "actresses": ["向井藍", "藤田こずえ", "篠田ゆう", "唯井まひろ", "佐山愛"],
        "maker": "FANZA",
        "price": "500円〜",
        "affiliate_url": items[0].get("affiliate_url_clean", "")
    }

    file_path = os.path.join(OUTPUT_DIR, "feature_fanza_ntr_netorare_cuckold_best_masterpieces.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)

    char_count = count_japanese_chars(html)
    print(f" -> Successfully saved Article 2 ({char_count} chars): {file_path}")


# ==============================================================================
# 記事3: 逆レイプ・搾精・M男向け痴女特化
# ==============================================================================
def generate_article_3():
    print("=== Generating Article 3: Reverse Rape & Femdom Milking Masterpieces ===")
    cids = ["mkmp00644", "mide00693", "cjod00171", "sone00335", "mkmp00744"]
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
        raise Exception("Failed to fetch all 5 items for Article 3")

    cover_image = items[0].get("imageURL", {}).get("large", "")

    reviews = [
        # 1: mkmp00644 逢沢みゆ
        {
            "rank": "01",
            "badge": "ド痴女ナース / 顔騎×ギアチェン騎乗位",
            "subtitle": "毎晩の容赦ない腰振りにチ●ポがバカになる！搾り取られる快感に悶絶する究極の逆調教",
            "body": """<b>【息継ぎも許さない濃厚顔騎と、男の腰を跳ね上げる変速グラインド】</b>：<br>
白衣を身にまとったド痴女ナース・逢沢みゆが、身動きの取れない入院患者のペニスを毎晩骨抜きにしていく搾精パラダイス。<br>
顔面に重たい尻をドスンと落として鼻と口を塞ぐ窒息顔騎からスタートし、アソコの匂いと愛液を存分に吸い込ませて男の理性を麻痺させます。ビンビンに勃起したペニスの上に跨がるやいなや、低速のねっとり回転から突如トップスピードへと切り替える「ギアチェン騎乗位」が炸裂。膣奥の吸着力と激しい腰のうねりに、男は「もう出ちゃう！」と懇願するも「まだまだ出すまで許さないから♡」と冷酷かつ妖艶な笑顔でピストンを加速。射精後も一切抜かずに連続でイカされ続ける、男のM心を完全に制圧する神作です。""",
            "climax": "射精でビクビク跳ねるペニスを膣内に閉じ込めたまま、腰を激しく振って2発目・3発目を強制搾精する極悪ノンストップ騎乗位。"
        },
        # 2: mide00693 日下部加奈
        {
            "rank": "02",
            "badge": "爆乳Jカップ痴女 / 身動き封じ連射責め",
            "subtitle": "逃げられない状態でムギュっと包まれる！Jカップの肉圧と執拗な痴女手淫で連続射精",
            "body": """<b>【圧倒的な質量を持つJカップ巨乳で窒息寸前！手足を固定されたM男の天国と地獄】</b>：<br>
圧倒的プロポーションを誇る日下部加奈が、ベッドに縛り付けられた男を思う存分玩具にするシチュエーション。<br>
重たいJカップの谷間にペニスを強引に挟み込み、上から覆いかぶさって顔面を巨乳で押し潰しながら、手コキとフェラチオを休みなく仕掛けてきます。一度射精しても拘束されているため逃げ場がなく、敏感になった亀頭を柔らかな舌先とローションまみれの胸で転がされて強制勃起。「まだこんなに硬いじゃん♡」と耳元で淫語を囁かれながら、体内のザーメンが枯れ果てるまで連射を強いられます。巨乳フェチとM男の欲望を同時に叶える贅沢すぎる1本です。""",
            "climax": "両手両足を固定されたままJカップパイズリで発射させられ、直後に跨がられて強制中出しされる連続昇天。"
        },
        # 3: cjod00171 咲々原リン
        {
            "rank": "03",
            "badge": "追撃男潮吹き / 絶倫お姉さんの強制ピストン",
            "subtitle": "「もう出てるってばぁ！」365日ピストンを止めてくれない絶倫お姉さんに犯され尽くす日々",
            "body": """<b>【男がイキ果ててもピストンを緩めない！快楽の向こう側へと連れ去られる追撃中出し】</b>：<br>
底なしの性欲を持つ絶倫お姉さん・咲々原リンに捕まり、毎日朝から晩まで搾り取られ続ける禁断の同居生活。<br>
「もう無理、出ちゃう！」と叫んで精液をドクドクと放出した瞬間、普通なら終わるはずが彼女の腰振りはさらに加速。「もっと気持ちよくなっていいんだよ？」と妖しく微笑みながら、敏感すぎる先端を奥深くへ擦りつけられ、男は前立腺を直撃されて前代未聞の“男潮吹き”状態へと追い込まれます。完全に受け身の状態で快楽の嵐に翻弄される快感は、一度味わうと普通のセックスでは満足できなくなるほどの破壊力です。""",
            "climax": "射精の痙攣が収まらないペニスを膣奥に押し込んだまま、激しく腰を上下させて男潮を吹き出させる極限追撃ピストン。"
        },
        # 4: sone00335 奥田咲・小島みなみ
        {
            "rank": "04",
            "badge": "Wアラサー痴女 / チ●ポ奪い合いハーレム",
            "subtitle": "婚活パーティーで肉食美女2人に逆お持ち帰り！熟練の舌技と二重騎乗位で搾り尽くされる",
            "body": """<b>【極上美女2人に挟まれて受ける贅沢の極み！交互にしゃぶられ跨がれる至福の搾精劇】</b>：<br>
熟練のテクニックと大人の色香を放つトップ女優・奥田咲と小島みなみの2大美女がタッグを組んだ夢の逆レイプ作品。<br>
冴えない男をホテルへ連れ込み、両脇から耳元、乳首、太ももへと舌を這わせる同時責めで完全に骨抜きに。1人がペニスを根元までくわえ込んでいる間、もう1人が顔面に跨がってアソコを押し付けるという息もつかせぬ波状攻撃が繰り広げられます。ベッドの上で奪い合うように代わる代わる騎乗位で腰を振られ、どちらが先に射精させるか競い合われる贅沢すぎる責め苦に、男の下半身は限界を突破します。""",
            "climax": "2人の美女に同時にキスされながら左右から胸を押し当てられ、交互に腰を振られて一滴残らずザーメンを放出するW絶頂。"
        },
        # 5: mkmp00744 乙アリス
        {
            "rank": "05",
            "badge": "早漏撲滅ゲーム / 金髪ギャルの凄腕逆ナン",
            "subtitle": "街で見かけた早漏M男を逆ナン！神ワザテクニックで絶対に我慢できない暴発射精",
            "body": """<b>【抜群のプロポーションと神がかったフェラテク！ギャルの挑発に1分も持たない男たち】</b>：<br>
ドSな金髪美巨乳ギャル・乙アリスが、自信のない素人M男を街で逆ナンし、ホテルの密室で徹底的にイジメ抜く大人気シリーズ。<br>
「我慢できたら中出ししていいよ？」と甘い餌をチラつかせながら、巧みな指使いと吸い付くようなバキュームフェラで容赦なく攻め立てます。男が必死に耐えようとする表情を見てクスクスと笑い、耳元で「もうイク？イクの？」と煽り立てるドSっぷりが最高潮。結局耐えきれずに暴発射精した情けない男を嘲笑いながら、休む間もなく次の責めへと移行する痛快かつエロすぎる名作です。""",
            "climax": "手コキで暴発寸前まで追い込まれたペニスを素早く口に含み、口内で豪快に発射させながら上目遣いで見つめる瞬間。"
        }
    ]

    html = f"""<div class="space-y-10 text-slate-200 leading-relaxed font-sans">

    <!-- 導入部リード文 -->
    <div class="bg-gradient-to-br from-slate-900 via-amber-950/40 to-slate-900 border border-amber-500/30 rounded-2xl p-6 sm:p-8 shadow-2xl backdrop-blur-sm">
        <div class="flex items-center space-x-2 text-amber-400 text-sm font-bold uppercase tracking-widest mb-3">
            <span class="w-2.5 h-2.5 rounded-full bg-amber-500 animate-ping"></span>
            <span>FANZA REVERSE RAPE & FEMDOM SELECTION</span>
        </div>
        <h1 class="text-2xl sm:text-3xl font-black text-white tracking-tight mb-4">
            【男の究極妄想】FANZA「逆レイプ・搾精・M男向けド痴女」おすすめ殿堂入り名作選！受け身で犯され尽くす連続射精バイブル【ノンストップ追撃】
        </h1>
        <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-4">
            「自分からは腰を振らず、圧倒的な美女に主導権を握られて犯されたい」「射精した直後でも休ませてもらえず、骨抜きになるまで搾り取られたい」――そんな男なら誰もが一度は夢見る究極の受け身願望を叶えてくれるのが、「逆レイプ・搾精・ド痴女」ジャンルです。
        </p>
        <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-4">
            激しい腰振りの騎乗位、呼吸困難に陥るほどの顔騎、そして射精の瞬間すら無視してピストンを続ける追撃アクメは、一度体験すると抜け出せなくなるほどの快楽中毒を生み出します。
        </p>
        <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
            本記事では、FANZAでM男・痴女好きから熱狂的な支持を集める<strong>「受け身で搾り尽くされる歴代神作」</strong>を厳選。ドSナースのギアチェン騎乗位、爆乳拘束連射、絶倫お姉さんの追撃ピストンまで、今夜のオナニーで完全に射精の限界を迎える至高の5本を徹底解説します。
        </p>
    </div>

    <!-- 逆レイプ・搾精ジャンルで射精を極める3大ポイント -->
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 sm:p-8 shadow-xl">
        <h2 class="text-xl sm:text-2xl font-bold text-white mb-6 flex items-center gap-3 border-b border-slate-800 pb-4">
            <span class="p-2 bg-amber-500/20 text-amber-400 rounded-lg text-lg">👑</span>
            <span>搾精・逆レイプ作品で完全昇天するための3つの注目ポイント</span>
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div class="bg-slate-800/60 p-5 rounded-xl border border-slate-700/60 hover:border-amber-500/50 transition">
                <div class="text-amber-400 font-bold text-base mb-2">① 主導権を100%握る「ドSな淫語と煽り」</div>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
                    「もうイッちゃうの？」「もっと出して♡」と男の情けない喘ぎを嘲笑いながら、耳元で囁かれる生々しい淫語の数々。
                </p>
            </div>
            <div class="bg-slate-800/60 p-5 rounded-xl border border-slate-700/60 hover:border-amber-500/50 transition">
                <div class="text-amber-400 font-bold text-base mb-2">② 射精後も止まらない「ノンストップ追撃ピストン」</div>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
                    発射した瞬間もペニスを抜かず、敏感になった亀頭を奥深くまで擦りつける追撃責め。男を快楽の限界へと追い込む演出。
                </p>
            </div>
            <div class="bg-slate-800/60 p-5 rounded-xl border border-slate-700/60 hover:border-amber-500/50 transition">
                <div class="text-amber-400 font-bold text-base mb-2">③ 腰振りの技術が光る「変速・回転騎乗位」</div>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
                    上下運動だけでなく、円を描くグラインドや突如スピードを上げるギアチェンジなど、男の急所を的確にえぐる卓越した腰使い。
                </p>
            </div>
        </div>
    </div>

    <!-- メインランキングセクション -->
    <div class="space-y-12">
        <h2 class="text-2xl sm:text-3xl font-black text-white tracking-tight flex items-center gap-3">
            <span class="w-2 h-8 bg-amber-500 rounded-full inline-block"></span>
            <span>FANZA逆レイプ・搾精・ド痴女おすすめ神作ランキングTOP5</span>
        </h2>
"""

    for i, it in enumerate(items):
        r = reviews[i]
        title = it.get("title", "")
        cid = it.get("content_id", "")
        aff_url = it.get("affiliate_url_clean", "")
        cover_img = it.get("imageURL", {}).get("large", "")
        sample_imgs = get_sample_images(it, 4)
        review_count = it.get("review", {}).get("count", 0)
        review_rate = it.get("review", {}).get("average", "4.5")
        
        actress_names = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        actress_html_list = [get_actress_link(name) for name in actress_names]
        actress_str = " / ".join(actress_html_list) if actress_html_list else "専属女優"
        
        genre_names = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        genre_html_list = [get_genre_link(g) for g in genre_names[:6]]
        genre_str = " ".join(genre_html_list)

        sample_img_html = ""
        if sample_imgs:
            sample_img_html = '<div class="grid grid-cols-2 sm:grid-cols-4 gap-2 mt-4">'
            for s_img in sample_imgs:
                sample_img_html += f'<div class="overflow-hidden rounded-lg border border-slate-700/60 aspect-video bg-slate-800"><img src="{s_img}" alt="{title} サンプル場面写真" class="w-full h-full object-cover hover:scale-105 transition duration-300" loading="lazy"></div>'
            sample_img_html += '</div>'

        html += f"""
        <!-- 作品カード {r['rank']} -->
        <div class="bg-slate-900 border border-slate-800 hover:border-amber-500/50 rounded-2xl overflow-hidden shadow-2xl transition duration-300">
            <div class="p-5 sm:p-7 border-b border-slate-800 flex flex-wrap items-center justify-between gap-3 bg-slate-950/40">
                <div class="flex items-center gap-3">
                    <span class="flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-amber-500 to-orange-600 text-white font-black text-xl shadow-lg shadow-amber-900/40">
                        {r['rank']}
                    </span>
                    <span class="text-xs sm:text-sm font-bold text-amber-400 bg-amber-950/60 border border-amber-800/60 px-3 py-1 rounded-full">
                        {r['badge']}
                    </span>
                </div>
                <div class="flex items-center gap-2 text-amber-400 font-bold text-sm bg-slate-900 px-3 py-1 rounded-lg border border-slate-800">
                    <span>★ {review_rate}</span>
                    <span class="text-slate-500 text-xs">({review_count}件の公式レビュー)</span>
                </div>
            </div>

            <div class="p-5 sm:p-8 space-y-6">
                <h3 class="text-lg sm:text-2xl font-black text-white leading-snug hover:text-amber-400 transition">
                    <a href="{aff_url}" target="_blank" rel="nofollow noopener">{title}</a>
                </h3>

                <div class="text-amber-300 font-bold text-base sm:text-lg border-l-4 border-amber-500 pl-3">
                    {r['subtitle']}
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
                    <div class="lg:col-span-5 space-y-3">
                        <div class="relative group rounded-xl overflow-hidden border border-slate-700 shadow-xl bg-slate-950">
                            <a href="{aff_url}" target="_blank" rel="nofollow noopener">
                                <img src="{cover_img}" alt="{title} 公式パッケージ画像" class="w-full h-auto object-cover group-hover:scale-102 transition duration-300" loading="lazy">
                                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition flex items-end justify-center p-4">
                                    <span class="text-white font-bold text-sm bg-amber-600 px-4 py-2 rounded-full shadow-lg">FANZA公式で高画質サンプルを見る</span>
                                </div>
                            </a>
                        </div>
                    </div>

                    <div class="lg:col-span-7 space-y-4">
                        <div class="text-slate-300 text-sm sm:text-base leading-relaxed">
                            {r['body']}
                        </div>

                        <div class="bg-amber-950/30 border border-amber-800/40 rounded-xl p-4">
                            <div class="text-amber-400 font-bold text-xs uppercase tracking-wider mb-1 flex items-center gap-1.5">
                                <span>⚡</span> ここで抜く！決定的搾精シーン
                            </div>
                            <div class="text-white text-sm font-medium leading-relaxed">
                                {r['climax']}
                            </div>
                        </div>

                        <div class="space-y-2 pt-2 text-xs">
                            <div class="flex items-center gap-2">
                                <span class="text-slate-400 font-semibold">主演女優:</span>
                                <span class="text-slate-200">{actress_str}</span>
                            </div>
                            <div class="flex flex-wrap items-center gap-1.5 pt-1">
                                <span class="text-slate-400 font-semibold mr-1">関連タグ:</span>
                                {genre_str}
                            </div>
                        </div>
                    </div>
                </div>

                <!-- サンプル画像プレビュー -->
                <div>
                    <div class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-1">
                        📸 劇中ハイライトプレビュー
                    </div>
                    {sample_img_html}
                </div>

                <!-- CTAボタン -->
                <div class="pt-2">
                    <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block w-full text-center bg-gradient-to-r from-amber-600 via-orange-600 to-amber-600 hover:from-amber-500 hover:to-orange-500 text-white font-black py-4 px-6 rounded-xl shadow-xl hover:shadow-amber-900/50 transition transform hover:-translate-y-0.5 text-base sm:text-lg">
                        👉 『{title[:25]}…』をFANZA公式で今すぐ無料サンプル視聴する
                    </a>
                </div>
            </div>
        </div>
        """

    html += f"""
    </div>

    <!-- サイト内関連記事リンク -->
    <div class="bg-slate-950 border border-slate-800 rounded-2xl p-6 sm:p-8">
        <h3 class="text-lg font-bold text-white mb-4 flex items-center gap-2">
            <span class="text-amber-400">🔗</span> あわせて読みたいおすすめ特集
        </h3>
        <ul class="space-y-3 text-sm">
            <li>
                <a href="/posts/feature_fanza_doujin_asmr_voice_masterpiece_guide" class="text-amber-400 hover:text-amber-300 underline font-semibold transition">
                    👉 【耳が溶ける快楽】FANZA同人ボイス・ASMR完全攻略ガイド！イヤホン1本で脳直撃のバイノーラル録音＆おすすめ神作傑作選
                </a>
            </li>
            <li>
                <a href="/posts/feature_fanza_doujin_pc_game_top_masterpieces_guide" class="text-amber-400 hover:text-amber-300 underline font-semibold transition">
                    👉 【動いて喘ぐ極上ヌキゲー】FANZA同人ゲームおすすめ殿堂入り名作選！アニメーションCG×超豪華ボイスで骨抜きにされる神作RPG・SLG完全攻略
                </a>
            </li>
            <li>
                <a href="/posts/feature_fanza_top_exclusive_actresses_ranking_masterpiece" class="text-amber-400 hover:text-amber-300 underline font-semibold transition">
                    👉 【2026年最新】FANZAで今もっとも抜ける「単体専属トップ女優」最強ランキング＆絶対に後悔しない歴史的代表作おすすめ傑作選
                </a>
            </li>
        </ul>
    </div>

</div>"""

    post_data = {
        "id": "feature_fanza_reverse_rape_femdom_milking_chijo_ranking",
        "title": "【男の究極妄想】FANZA「逆レイプ・搾精・M男向けド痴女」おすすめ殿堂入り名作選！受け身で犯され尽くす連続射精バイブル【ノンストップ追撃】",
        "content": html,
        "review": "FANZAで絶大な人気を誇る逆レイプ・搾精・M男向けド痴女作品を特集。ドSナースのギアチェン騎乗位、Jカップ爆乳での拘束連射、追撃男潮吹きまで、受け身で搾り取られる快楽に悶絶するおすすめ神作TOP5。",
        "image": cover_image,
        "date": "2026-09-30 08:50:00",
        "genres": ["痴女", "逆レイプ", "搾精", "M男", "騎乗位", "ハイビジョン", "独占配信", "顔騎"],
        "actresses": ["逢沢みゆ", "日下部加奈", "咲々原リン", "奥田咲", "小島みなみ", "乙アリス"],
        "maker": "FANZA",
        "price": "500円〜",
        "affiliate_url": items[0].get("affiliate_url_clean", "")
    }

    file_path = os.path.join(OUTPUT_DIR, "feature_fanza_reverse_rape_femdom_milking_chijo_ranking.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)

    char_count = count_japanese_chars(html)
    print(f" -> Successfully saved Article 3 ({char_count} chars): {file_path}")


if __name__ == "__main__":
    generate_article_1()
    print("-" * 50)
    generate_article_2()
    print("-" * 50)
    generate_article_3()
    print("=== All 3 killer feature articles generated successfully! ===")
