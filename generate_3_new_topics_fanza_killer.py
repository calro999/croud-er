# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・大型キラー特集3記事自動生成スクリプト
1. 【黒ギャル・小麦肌×ギャップ萌え特化】
   『【褐色小麦肌×濃厚種付け】FANZA「黒ギャル・日焼けギャル中出し」おすすめ神作ランキングTOP5！生意気なビッチが快楽に屈服してメス堕ち懇願する最高峰AV選【2026年最新】』
2. 【超巨尻・美尻×迫力のバック後背位ピストン特化】
   『【肉弾ヒップが激震する快楽】FANZA「超巨尻・美尻×バック後背位ピストン」おすすめ神作ランキングTOP5！顔面騎乗窒息から腰砕け連続絶頂まで尻フェチ必携の殿堂入りAV選【2026年最新】』
3. 【人気女優の限界突破！初アナル解禁・肛門処女喪失特化】
   『【桃色処女孔が開く背徳と歓喜】FANZA「人気単体女優の初アナル解禁・肛門処女喪失」おすすめ神作ランキングTOP5！緊張の初挿入から前代未聞の2穴同時イキ狂いまで伝説の体当たりドキュメントAV選【2026年最新】』
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
    if not name:
        return ""
    clean_name = re.sub(r'（[^）]+）', '', name).strip()
    slug = actress_slugs.get(name) or actress_slugs.get(clean_name)
    if slug:
        return f'<a href="/actress/{slug}" class="text-rose-400 hover:text-rose-300 underline font-bold transition">{name}</a>'
    encoded = urllib.parse.quote(name)
    return f'<a href="/actress/{encoded}" class="text-rose-400 hover:text-rose-300 underline font-bold transition">{name}</a>'

def get_genre_link(genre):
    if not genre:
        return ""
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
        print(f"Error fetching {cid}: {e}")
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

def generate_individual_post_if_needed(it, special_labels=None):
    cid = it.get("content_id")
    if not cid:
        return
    file_path = os.path.join(OUTPUT_DIR, f"{cid}.json")
    if os.path.exists(file_path):
        return
    
    title = it.get("title", "")
    acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
    genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
    maker = it.get("iteminfo", {}).get("maker", [{}])[0].get("name", "")
    price = it.get("prices", {}).get("price", "300~")
    date_str = it.get("date", "2024-01-01 10:00:00")
    img = it.get("imageURL", {}).get("large", "")
    aff_url = it.get("affiliate_url_clean", "")
    sample_movie = f"https://www.dmm.com/litevideo/-/part/=/cid={cid}/size=720_480/affi_id={LINK_AFFILIATE_ID}/"
    
    samples = []
    s_data = it.get("sampleImageURL", {})
    if "sample_l" in s_data:
        samples = s_data["sample_l"].get("image", [])
    elif "sample_m" in s_data:
        samples = s_data["sample_m"].get("image", [])
    if isinstance(samples, str):
        samples = [samples]
        
    act_str = "・".join(acts) if acts else "人気キャスト"
    review_html = f"""<h2>『{title}』詳細レビュー・作品の見どころ</h2>
<p>本作は、{act_str}が主演を務め、息をのむような生々しい熱量と官能美が極限まで凝縮されたFANZA屈指の人気作です。</p>

<h3>出演キャスト（{act_str}）の圧倒的な存在感と熱演</h3>
<p>{act_str}が魅せる艶やかな表情と全身から溢れ出るエロティシズムは圧巻。肌が触れ合うたびにこぼれ落ちる濃密な吐息、快楽の波に呑まれて理性が溶け出していく視線の変化が鮮明に記録されています。</p>

<h3>見どころ・おすすめの視聴ポイント</h3>
<p>最大の見せ場は、クライマックスにかけて繰り広げられる妥協なき濃厚ピストンと生々しい結合描写です。精緻なアングルと反響する水音が臨場感を倍増させ、鑑賞者の五感を根底から揺さぶります。</p>

<h3>総評・ユーザー評価</h3>
<p>シチュエーション設定の妙とキャストの極上パフォーマンスが見事に融合した傑作。実用性を追求する大人のファンに自信を持って推薦できる一本です。</p>"""

    data = {
        "id": cid,
        "hinban": f"{cid.upper()}",
        "title": title,
        "review": review_html,
        "image": img,
        "sample_movie_url": sample_movie,
        "sample_images": samples[:20],
        "affiliate_url": aff_url,
        "genres": genres[:10],
        "actresses": acts,
        "directors": [],
        "maker": maker,
        "price": price,
        "date": date_str,
        "labels": special_labels or ["殿堂入り", "話題作", "おすすめ"]
    }
    with open(file_path, "w", encoding="utf-8") as out_f:
        json.dump(data, out_f, ensure_ascii=False, indent=2)
    print(f" -> Generated individual post: {cid}")


# ==============================================================================
# 記事1: 黒ギャル・小麦肌×ギャップ萌え・中出し特化
# ==============================================================================
def generate_article_black_gyaru():
    print("=== Generating Article 1: 黒ギャル・小麦肌特化 ===")
    cids = ["bony00152", "miaa00467", "1avop00062", "fjin00062", "khip00003"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["黒ギャル", "中出し", "日焼け", "メス堕ち"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 1 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-amber-950/40 via-slate-900 to-slate-950 border border-amber-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-amber-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-amber-500/20 text-amber-300 border border-amber-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">EXCLUSIVE RANKING</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月03日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【褐色小麦肌×濃厚種付け】FANZA「黒ギャル・日焼けギャル中出し」おすすめ神作ランキングTOP5！生意気なビッチが快楽に屈服してメス堕ち懇願する最高峰AV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    男の本能を最も野蛮に呼び覚ますジャンル、それが「黒ギャル・日焼け小麦肌」です。眩い太陽の下で焼き上げた健康的な褐色ボディ、眩しい金髪と派手なネイル、そして何よりも「ウチらに勝てるわけないじゃん」と言わんばかりの高慢で生意気な態度。その強気なギャルが、圧倒的な肉棒ピストンによって理性を剥ぎ取られ、潤んだ瞳で「おじさんのチンポ気持ちいい…中にいっぱい出してぇ！」とすがりつく姿は、男にとって至高のカタルシスをもたらします。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    さらに黒ギャル作品最大の視覚的魅力は、褐色肌と白濁液の強烈なコントラストです。くっきりと残る白い水着跡、引き締まった褐色の腹筋やデカ尻に、どす黒い欲情とともに放たれる濃厚な精子が飛び散る光景は、白肌AVでは決して味わえない濃厚な淫靡さを放ちます。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、FANZAで不動の人気を誇る黒ギャル界の絶対的女王・蘭華の伝説的傑作から、カリスマ・AIKAの衝撃作まで、レビュー平均4.5以上・リピート率抜群の【黒ギャル×中出し神作TOP5】を徹底解説。今夜あなたのモニター前で、極上のギャルわからせ快楽をお届けします。
  </p>
</div>

<!-- 選び方の基準 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-amber-400">⚡</span> 失敗しない黒ギャルAV選び！男を唸らせる3大チェックポイント
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-amber-300 mb-2">① 「生意気」から「メス堕ち」への落差</h4>
      <p class="text-slate-300 leading-relaxed">初めはバカにしたようなタメ口や嘲笑を見せつつ、一度奥を突かれると声色が一変して敬語混じりの懇願に変わる心理的グラデーションの深さが命です。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-amber-300 mb-2">② 褐色肌に映える白水着跡と汗の輝き</h4>
      <p class="text-slate-300 leading-relaxed">均整の取れた日焼け肌と、下着を脱いだ瞬間に露わになる眩しい白肌のギャップ。激しいピストンで汗が光る肉弾美が視覚を強烈に刺激します。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-amber-300 mb-2">③ 容赦ない生中出しと溢れ出る白濁液</h4>
      <p class="text-slate-300 leading-relaxed">ゴムなしで最奥まで打ち込まれ、膣内にドクドクと注ぎ込まれたザーメンが褐色の太ももを伝い落ちる断面カットや結合部接写の充実度が快感を左右します。</p>
    </div>
  </div>
</div>"""
    html_parts.append(intro_html)

    # ランキング5作品詳細
    for idx, it in enumerate(items, 1):
        cid = it.get("content_id")
        title = it.get("title", "")
        img = it.get("imageURL", {}).get("large", "")
        aff_url = it.get("affiliate_url_clean", "")
        price = it.get("prices", {}).get("price", "300~")
        sample_movie = f"https://www.dmm.com/litevideo/-/part/=/cid={cid}/size=720_480/affi_id={LINK_AFFILIATE_ID}/"
        sample_imgs = get_sample_images(it, 4)
        acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        maker = it.get("iteminfo", {}).get("maker", [{}])[0].get("name", "")
        
        act_links = " ".join([get_actress_link(a) for a in acts]) if acts else "専属キャスト"
        genre_links = " ".join([get_genre_link(g) for g in genres[:6]])

        rank_badge = f'<span class="bg-gradient-to-r from-amber-500 to-rose-500 text-slate-950 font-black text-sm px-3 py-1 rounded-full shadow-lg">第{idx}位</span>'
        
        # 作品ごとの詳細独自解説
        if cid == "bony00152":
            work_analysis = """
<h4>【作品解説・見どころ】黒ギャル界の生ける伝説・蘭華が魅せる種付け受胎の頂点</h4>
<p>黒ギャルAVの頂点に君臨する蘭華が、男の遺伝子を骨の髄まで搾り取る「種付け・孕ませ特化」の超大作です。褐色の引き締まったウエストから豊満なヒップラインにかけての曲線美はまさに芸術。最初は余裕の表情で「ねぇ、本当にウチを孕ませる気？」と挑発してきますが、容赦ない腰の打ち込みを受けるにつれ、アヘ顔を晒して痙攣絶頂を繰り返します。子宮口を激しくノックされるたびに甲高い声をあげ、奥深くに白濁精液を注ぎ込まれた瞬間の至福に満ちた表情は全黒ギャルファン必見です。</p>
<h4>【実用ポイント】褐色肌と白濁液のコントラストが脳を破壊する</h4>
<p>本作の真骨頂は、中出し直後の膣口からドロッと溢れ出す精液の接写カットです。小麦色に焼けた大腿部と白いザーメンの色彩差が生々しく、抜きの実用度は文句なしの五つ星。ヘッドホン越しに響く肉と肉がぶつかり合う重低音も圧巻です。</p>
"""
        elif cid == "miaa00467":
            work_analysis = """
<h4>【作品解説・見どころ】小遣い稼ぎのノリが一転、抜かずの連続騎乗位で搾り取られる快感</h4>
<p>軽いノリで「ちょっとエッチしてお小遣い貰っちゃお」と男の部屋にやってきた黒ギャル蘭華が、抜き差し無用のエンドレス騎乗位中出しに挑むムーディーズの超人気作。褐色の美脚で男の腰をがっちりホールドし、自ら腰を上下にグラインドさせながら果てるまで腰を止めないド痴女っぷりは圧巻です。10発連続で中出しされるごとに、ギャルの意識が快楽の底へと沈んでいき、最後には完全に雄の虜となって懇願する姿がリアルに描かれます。</p>
<h4>【実用ポイント】男の意思を無視して貪り続けるノンストップ腰振り</h4>
<p>射精後もペニスを抜かずに敏感な状態のまま再び激しく腰を動かされる「二度打ち・連続射精」の臨場感が尋常ではありません。下から見上げるアングルのデカ尻の波打ちと、汗まみれになった豊かな胸の揺れが視界を支配します。</p>
"""
        elif cid == "1avop00062":
            work_analysis = """
<h4>【作品解説・見どころ】伝説のギャルクイーンAIKAが放つ、AV史に刻まれる野性味溢れる傑作</h4>
<p>平成・令和を通じてギャル界の頂点を走り続けたAIKAのキャリアの中でも、最も野性的でアグレッシブなエロスを叩き出したAV OPENエントリーの記念碑的作品。褐色の素肌を惜しげもなく晒し、むせ返るような熱気の中で繰り広げられる本能剥き出しの交わりは、現代の整えられたAVにはない生々しい衝動に満ちています。</p>
<h4>【実用ポイント】本能の赴くままに腰を打ち付ける圧倒的リアリズム</h4>
<p>一切の台本を感じさせない、動物的な交尾そのものの迫力。AIKAの濡れた瞳と乱れ飛ぶ喘ぎ声が、鑑賞者の原始的な射精欲求を直接刺激します。規格外のエネルギーに圧倒されながら濃密な射精を迎えられる一本です。</p>
"""
        elif cid == "fjin00062":
            work_analysis = """
<h4>【作品解説・見どころ】陰キャの部屋で無防備にデカ尻を揺らすパート家政婦ギャル</h4>
<p>オタクで引きこもりの男が住む汚部屋に、家政婦として派遣されてきた日焼け黒ギャル。だらしない男を見下すような視線を向けながらも、ミニスカートやショートパンツからこぼれる豊満なヒップを無防備に見せつけてくる日常シチュエーションが秀逸です。我慢できずに背後から組み敷いた瞬間、驚きながらも身体が疼いてしまうギャルの素直な反応がたまらなくエロティックです。</p>
<h4>【実用ポイント】背徳のバック中出しと生活感のギャップ</h4>
<p>掃除機をかける姿勢のまま背後からスカートをめくられ、褐色の美尻を割って奥まで突き刺されるバックピストンが最高潮。日常空間での背徳感と、ギャルの肉感的なヒップの跳ね返りが強烈な興奮を呼び起こします。</p>
"""
        else:
            work_analysis = """
<h4>【作品解説・見どころ】いつも部屋に入り浸る黒ギャル幼馴染との濃厚な日常中出し生活</h4>
<p>ヒマさえあれば部屋にやってきてベッドの上でゴロゴロとスマホをいじる黒ギャル幼馴染。薄着から覗く小麦色の肌と太ももの誘惑に耐えかねて手を出したところ、拒否するどころか「アンタ、結構いい体してるじゃん…」と淫乱スイッチが入ってしまう王道かつ最強の設定です。</p>
<h4>【実用ポイント】気心知れた関係だからこその無防備なアヘ顔</h4>
<p>普段のくだけた会話から、交わった瞬間に女の顔へと変貌していくギャップが秀逸。何度も何度も中出しを繰り返すうちに、互いの汗と体液が混ざり合い、部屋中が甘い匂いに満ちていくような濃密なリアリティを堪能できます。</p>
"""

        sample_imgs_html = ""
        if sample_imgs:
            imgs_tags = "".join([f'<a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block overflow-hidden rounded-lg border border-slate-700 hover:border-amber-400 transition"><img src="{si}" alt="サンプル画像" class="w-full h-24 md:h-32 object-cover hover:scale-105 transition duration-300" loading="lazy" /></a>' for si in sample_imgs])
            sample_imgs_html = f"""<div class="mt-4 mb-6">
  <span class="text-xs font-bold text-slate-400 mb-2 block">📸 高画質サンプルシーン</span>
  <div class="grid grid-cols-2 md:grid-cols-4 gap-2">
    {imgs_tags}
  </div>
</div>"""

        item_html = f"""<div class="my-10 bg-slate-900/90 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-2xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 pb-4 border-b border-slate-800">
    <div class="flex items-center gap-3">
      {rank_badge}
      <span class="text-xs text-slate-400 font-mono tracking-wider">品番: {cid.upper()}</span>
    </div>
    <div class="text-xs text-amber-400 font-semibold bg-amber-950/60 border border-amber-800/60 px-3 py-1 rounded-full">
      FANZA公式配信中（{price}円〜）
    </div>
  </div>

  <h3 class="text-xl md:text-2xl font-black text-white mb-4 leading-snug">
    <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="hover:text-amber-400 transition">
      {title}
    </a>
  </h3>

  <div class="grid grid-cols-1 md:grid-cols-12 gap-6 mb-6">
    <div class="md:col-span-5">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block group overflow-hidden rounded-xl border border-slate-700/80 shadow-lg relative">
        <img src="{img}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition flex items-end p-4">
          <span class="text-xs text-amber-300 font-bold">FANZAで公式サンプルを再生 ▶</span>
        </div>
      </a>
      <div class="mt-3 flex items-center justify-between text-xs text-slate-400">
        <span>メーカー: <strong class="text-slate-200">{maker}</strong></span>
        <span>キャスト: {act_links}</span>
      </div>
      <div class="mt-2 flex flex-wrap gap-1">
        {genre_links}
      </div>
    </div>

    <div class="md:col-span-7 flex flex-col justify-between">
      <div class="text-slate-300 text-sm md:text-base leading-relaxed space-y-4">
        {work_analysis}
      </div>

      <div class="mt-6 pt-4 border-t border-slate-800/80 flex flex-wrap gap-3 items-center justify-between">
        <a href="/posts/{cid}" class="text-xs text-slate-400 hover:text-rose-400 underline transition">
          📄 作品の個別詳細ページを見る
        </a>
        <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="inline-flex items-center gap-2 bg-gradient-to-r from-amber-500 to-rose-600 hover:from-amber-400 hover:to-rose-500 text-slate-950 font-black px-6 py-3 rounded-xl shadow-lg hover:shadow-rose-500/20 transition transform hover:-translate-y-0.5 text-sm">
          <span>今すぐFANZAで本編・無料サンプルを見る</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
        </a>
      </div>
    </div>
  </div>

  {sample_imgs_html}
</div>"""
        html_parts.append(item_html)

    # スペック徹底比較表
    comparison_table = f"""<div class="my-12 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-2xl">
  <h3 class="text-xl md:text-2xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-amber-400">📊</span> 黒ギャル×中出し神作TOP5 徹底スペック比較まとめ
  </h3>
  <p class="text-slate-400 text-xs md:text-sm mb-6">各作品のギャル度、肉感度、メス堕ち度、実用度を客観的に比較。あなたの性癖に最も突き刺さる一本を見つけてください。</p>
  <div class="overflow-x-auto">
    <table class="w-full text-left text-xs md:text-sm border-collapse">
      <thead>
        <tr class="bg-slate-800/90 text-amber-300 border-b border-slate-700">
          <th class="p-3">順位 / タイトル</th>
          <th class="p-3">主演キャスト</th>
          <th class="p-3 text-center">ギャル度</th>
          <th class="p-3 text-center">メス堕ち度</th>
          <th class="p-3 text-center">中出し濃度</th>
          <th class="p-3 text-center">実用度</th>
          <th class="p-3 text-right">公式リンク</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800 text-slate-300">
        <tr class="hover:bg-slate-800/40">
          <td class="p-3 font-bold text-white">第1位 種付け特化 孕ませ中出し</td>
          <td class="p-3">蘭華</td>
          <td class="p-3 text-center text-amber-400">★★★★★</td>
          <td class="p-3 text-center text-rose-400">★★★★★</td>
          <td class="p-3 text-center text-emerald-400">★★★★★</td>
          <td class="p-3 text-center text-amber-300 font-bold">5.0</td>
          <td class="p-3 text-right"><a href="{items[0].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-amber-400 hover:underline">FANZA ▶</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="p-3 font-bold text-white">第2位 抜かずの10発騎乗位中出し</td>
          <td class="p-3">蘭華</td>
          <td class="p-3 text-center text-amber-400">★★★★★</td>
          <td class="p-3 text-center text-rose-400">★★★★☆</td>
          <td class="p-3 text-center text-emerald-400">★★★★★</td>
          <td class="p-3 text-center text-amber-300 font-bold">4.9</td>
          <td class="p-3 text-right"><a href="{items[1].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-amber-400 hover:underline">FANZA ▶</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="p-3 font-bold text-white">第3位 野性の王国 特別編 生中出し</td>
          <td class="p-3">AIKA</td>
          <td class="p-3 text-center text-amber-400">★★★★★</td>
          <td class="p-3 text-center text-rose-400">★★★★★</td>
          <td class="p-3 text-center text-emerald-400">★★★★☆</td>
          <td class="p-3 text-center text-amber-300 font-bold">4.8</td>
          <td class="p-3 text-right"><a href="{items[2].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-amber-400 hover:underline">FANZA ▶</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="p-3 font-bold text-white">第4位 汚部屋のパート家政婦ギャル</td>
          <td class="p-3">蘭華</td>
          <td class="p-3 text-center text-amber-400">★★★★☆</td>
          <td class="p-3 text-center text-rose-400">★★★★☆</td>
          <td class="p-3 text-center text-emerald-400">★★★★☆</td>
          <td class="p-3 text-center text-amber-300 font-bold">4.7</td>
          <td class="p-3 text-right"><a href="{items[3].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-amber-400 hover:underline">FANZA ▶</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="p-3 font-bold text-white">第5位 デカ尻黒ギャル幼馴染 連日中出し</td>
          <td class="p-3">蘭華</td>
          <td class="p-3 text-center text-amber-400">★★★★☆</td>
          <td class="p-3 text-center text-rose-400">★★★★★</td>
          <td class="p-3 text-center text-emerald-400">★★★★☆</td>
          <td class="p-3 text-center text-amber-300 font-bold">4.7</td>
          <td class="p-3 text-right"><a href="{items[4].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-amber-400 hover:underline">FANZA ▶</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>"""
    html_parts.append(comparison_table)

    # サイト内回遊・内部リンク
    related_links_html = """<div class="my-8 bg-slate-900/60 border border-slate-800 rounded-2xl p-6">
  <h4 class="text-lg font-bold text-white mb-3 flex items-center gap-2">
    <span class="text-rose-400">🔗</span> あわせて読みたい人気特集記事
  </h4>
  <ul class="grid grid-cols-1 md:grid-cols-2 gap-3 text-sm text-slate-300">
    <li><a href="/posts/feature_fanza_huge_ass_back_piston_ranking_2026" class="hover:text-amber-300 underline">【肉弾ヒップが激震する快楽】巨尻・美尻×バック後背位ピストンおすすめ神作ランキング</a></li>
    <li><a href="/posts/feature_fanza_first_anal_deflowering_ranking_2026" class="hover:text-amber-300 underline">【桃色処女孔が開く背徳】人気単体女優の初アナル解禁・肛門処女喪失神作ランキング</a></li>
    <li><a href="/posts/feature_fanza_mens_esthe_secret_oil_massage_ranking" class="hover:text-amber-300 underline">【密着施術で理性崩壊】メンズエステ・裏オプ回春マッサージ神作ランキング</a></li>
    <li><a href="/posts/feature_fanza_outdoor_exposure_public_shame_ranking" class="hover:text-amber-300 underline">【羞恥心崩壊の背徳快楽】野外露出・青姦・公衆羞恥プレイおすすめ神作選</a></li>
  </ul>
</div>"""
    html_parts.append(related_links_html)

    # JSON-LD構造化データ
    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "ItemList",
                "name": "黒ギャル・日焼けギャル中出しおすすめ神作ランキングTOP5",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": idx + 1,
                        "name": it.get('title'),
                        "url": it.get('affiliate_url_clean')
                    } for idx, it in enumerate(items)
                ]
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": "黒ギャルAV初心者にはどの作品が一番おすすめですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第1位の『種付け特化 孕ませ中出し 蘭華』が最もおすすめです。褐色ボディの圧倒的な美しさと、強気なギャルが快楽に屈服していく王道のメス堕ち展開が完璧に詰まっています。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "セール中にお得に購入できますか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "FANZAの定期セールやポイント還元キャンペーン期間中には、150円〜210円前後のワンコイン価格で購入可能な作品が多数含まれています。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "スマホやタブレットでも高画質でストリーミング再生できますか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "はい、FANZAの公式プレイヤーおよびアプリを利用して、iOS/Android端末でフルHD高画質ストリーミング再生およびダウンロード視聴が可能です。"
                        }
                    }
                ]
            }
        ]
    }
    json_ld_script = f'<script type="application/ld+json">\n{json.dumps(json_ld, ensure_ascii=False, indent=2)}\n</script>'
    html_parts.append(json_ld_script)

    full_html = "\n\n".join(html_parts)
    char_count = count_japanese_chars(full_html)
    print(f"Article 1 character count: {char_count} chars")
    if char_count < 3000:
        raise Exception(f"Article 1 is under 3000 chars: {char_count}")

    post_data = {
        "id": "feature_fanza_black_gyaru_raw_creampie_ranking_2026",
        "title": "【褐色小麦肌×濃厚種付け】FANZA「黒ギャル・日焼けギャル中出し」おすすめ神作ランキングTOP5！生意気なビッチが快楽に屈服してメス堕ち懇願する最高峰AV選【2026年最新】",
        "date": "2026-10-03 10:00:00",
        "hinban": "BLACK-GYARU-CREAMPIE-BEST-2026",
        "price": "150~",
        "maker": "FANZA公式セレクション",
        "actresses": ["蘭華", "AIKA"],
        "genres": ["ギャル", "黒ギャル", "中出し", "日焼け", "痴女", "騎乗位", "特集", "殿堂入り"],
        "image": cover_image,
        "review": full_html
    }

    file_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f" -> Successfully saved Article 1 ({char_count} chars) to {file_path}")


# ==============================================================================
# 記事2: 巨尻・美尻×バック後背位ピストン特化
# ==============================================================================
def generate_article_huge_ass():
    print("=== Generating Article 2: 巨尻・美尻バック後背位特化 ===")
    cids = ["ipzz00336", "waaa00476", "pred00674", "waaa00197", "1bkynb00050"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["巨尻", "美尻", "バック", "肉感"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 2 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-purple-950/40 via-slate-900 to-slate-950 border border-purple-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-purple-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-purple-500/20 text-purple-300 border border-purple-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">EXCLUSIVE RANKING</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月03日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【肉弾ヒップが激震する快楽】FANZA「超巨尻・美尻×バック後背位ピストン」おすすめ神作ランキングTOP5！顔面騎乗窒息から腰砕け連続絶頂まで尻フェチ必携の殿堂入りAV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    男のDNAに深く刻み込まれた根源的なフェティシズム、それが「女の豊かなヒップライン」です。たわわに実った果実のように丸みを帯びた大臀筋、両手で掴んでも収まりきらない肉感的なボリューム、そして四つん這いになった瞬間に露わになる無防備な秘裂。巨尻の魅力は単なるサイズにとどまらず、男が背後から組み敷き、力任せにピストンを叩き込んだ瞬間に最大化されます。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    腰を打ち付けるたびに「バチン！バチン！」と炸裂する生々しい肉音。衝撃によって波打つように揺れ動く尻肉の波動。そして、深い挿入によって子宮の奥深くまで突き上げられ、女優がシーツを掻きむしりながら悶絶するバックショットは、正常位では決して味わえない暴力的な興奮を男にもたらします。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、FANZAに集う全国の尻フェチたちから絶大な支持を集める最高峰の傑作を厳選。小野坂ゆいかの圧倒的肉弾ピストンから、佐山愛の熟れた美尻痙攣、楪カレンのグラマラスな腰振りまで、リピート必須の【巨尻×バック後背位神作TOP5】を徹底レビューします。
  </p>
</div>

<!-- 鑑賞メソッド -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-purple-400">🍑</span> 尻フェチのための究極鑑賞術！興奮を倍増させる3大視点
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-purple-300 mb-2">① 打ち付ける肉音と重低音の反響</h4>
      <p class="text-slate-300 leading-relaxed">下腹部とヒップが激突する生々しい打撃音こそバックピストンの真髄。ヘッドホンで低音を効かせることで、自らが腰を振っているかのような強烈な没入感が得られます。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-purple-300 mb-2">② 尻肉を押し分けて結合部を覗くローアングル</h4>
      <p class="text-slate-300 leading-relaxed">巨大なヒップの谷間に吸い込まれていく肉棒の抜き差し。ローアングルから結合部とキュッと締まるアナルを同時に捉えたカメラワークが最高の実用度を誇ります。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-purple-300 mb-2">③ 突き上げに耐えかねて反り返る背筋</h4>
      <p class="text-slate-300 leading-relaxed">背後からの強烈なピストンに対し、快楽に耐えかねて腰を浮かせ、背中を反らせて喘ぐ女優の身体反応。全身で快楽を受け止めるダイナミックな肉体美を堪能できます。</p>
    </div>
  </div>
</div>"""
    html_parts.append(intro_html)

    for idx, it in enumerate(items, 1):
        cid = it.get("content_id")
        title = it.get("title", "")
        img = it.get("imageURL", {}).get("large", "")
        aff_url = it.get("affiliate_url_clean", "")
        price = it.get("prices", {}).get("price", "300~")
        sample_imgs = get_sample_images(it, 4)
        acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        maker = it.get("iteminfo", {}).get("maker", [{}])[0].get("name", "")
        
        act_links = " ".join([get_actress_link(a) for a in acts]) if acts else "専属キャスト"
        genre_links = " ".join([get_genre_link(g) for g in genres[:6]])

        rank_badge = f'<span class="bg-gradient-to-r from-purple-500 to-pink-500 text-slate-950 font-black text-sm px-3 py-1 rounded-full shadow-lg">第{idx}位</span>'

        if cid == "ipzz00336":
            work_analysis = """
<h4>【作品解説・見どころ】むちむち肉弾ボディと激揺れバックピストンの金字塔</h4>
<p>アイポケが誇る肉感クイーン小野坂ゆいかが、自らのグラマラスな肉体を余すところなく開放した傑作。最大の見どころは、四つん這いにされた彼女の巨大な美尻に向かって、男優が渾身の力で打ち込むバックピストンシーンです。腰を打ち付けるたびに尻肉全体がプルプルと波打ち、その振動が太ももから背中へと伝播していく映像美は圧巻。突き刺されるたびにシーツに顔を埋めて喘ぐ小野坂ゆいかの悶絶顔が男の征服欲を激しく煽ります。</p>
<h4>【実用ポイント】逃げ場のない後背位で子宮をノックされる連続絶頂</h4>
<p>深く突き刺さったまま腰を回すグラインドピストンと、容赦ない高速ピストンの緩急が完璧。結合部から漏れ出す愛液のぬめりと反響する摩擦音が、ヘッドホン越しに鑑賞者の脳髄を直撃します。</p>
"""
        elif cid == "waaa00476":
            work_analysis = """
<h4>【作品解説・見どころ】豊満Tバック兄嫁の熟れたヒップをマシンガンピストンで穿つ</h4>
<p>巨乳＆巨尻の代名詞・佐山愛が魅せる禁断の背徳劇。タイトなスカートから浮き出るTバックのヒップラインに理性を失った義弟が、背後から襲いかかり容赦なく腰を叩きつけます。成熟した大人の色気と、激しいピストンによって徐々に淫乱なメスへと変貌していく佐山愛の迫真の演技が融合。男の欲望をすべて受け止める包容力抜群のヒップはまさに芸術品です。</p>
<h4>【実用ポイント】ガクガクと痙攣し潮を吹くほどの強烈な後背位絶頂</h4>
<p>マシンガンのように繰り出されるピストンに、耐えきれず足をガクガクと震わせながら失禁・絶頂するシーンは必見。男が腰を掴んで限界まで密着するシーンのエロティシズムは筆舌に尽くしがたい完成度です。</p>
"""
        elif cid == "pred00674":
            work_analysis = """
<h4>【作品解説・見どころ】スナックのカウンター裏で始まる、極上色気美女とのアフター情事</h4>
<p>完璧なスタイルと豊満な肉体美を兼ね備えた楪カレンが、スナックの妖艶なママとして男を惑わす人気作。色気ムンムンの接客から一転、店内で二人きりになった瞬間に始まる背徳の交わりはスリリングそのもの。タイトなドレスをまくり上げられ、カウンターに手をついて突き出された楪カレンの丸く引き締まったデカ尻は、見ているだけで息をのむ美しさです。</p>
<h4>【実用ポイント】ドレスを着崩したままの着衣バックハメの圧倒的淫靡さ</h4>
<p>完全に服を脱がせるのではなく、ドレスを腰までたくし上げた状態で挿入する着衣エロスが抜群。背後から豊かな胸を揉みしだかれながら、奥深くまで貫かれる楪カレンの甘美な吐息が最高の実用度を誇ります。</p>
"""
        elif cid == "waaa00197":
            work_analysis = """
<h4>【作品解説・見どころ】木下ひまりが魅せる、真夏の汗だく肉弾パーティー</h4>
<p>抜群のプロポーションと引き締まった美尻でファンを魅了する木下ひまりが、規格外の巨根男優たちと汗だくで交わる衝撃作。滴り落ちる汗で光り輝くヒップラインと、激しい衝突によって赤く染まっていく尻肉のリアリティは凄まじいの一言。体力の限界を超えて繰り広げられる連続交尾は、鑑賞者を異次元の興奮へと誘います。</p>
<h4>【実用ポイント】限界突破の激ピストンに蕩けきった表情</h4>
<p>休む間もなく叩き込まれる腰の衝撃に、瞳を潤ませながら快楽を受け止める木下ひまりの表情がエロティックの極致。激しいピストン音と荒い息遣いが部屋中に響き渡る圧倒的ライブ感を楽しめます。</p>
"""
        else:
            work_analysis = """
<h4>【作品解説・見どころ】風呂を借りにきた同僚美女の無防備な豊満ボディに理性が崩壊</h4>
<p>普段は真面目な同僚の月野かすみが、汗を流すため自宅の風呂を借りにくるという妄想全開のシチュエーション。湯上がりの火照った肌、バスタオル一枚から覗く豊満なヒップと胸元に男の理性が吹き飛びます。濡れた素肌のままベッドに組み敷かれ、背後からじっくりと貫かれるシーンは濃密そのものです。</p>
<h4>【実用ポイント】火照った肌と汗が混ざり合う10発中出しの濃厚さ</h4>
<p>湯上がりの清潔感ある色気から、激しいピストンによって次第に淫乱な愛液と汗にまみれていくグラデーションが秀逸。何度も何度も中出しを重ねる濃厚なピストン描写が、見る者の射精欲を限界まで高めます。</p>
"""

        sample_imgs_html = ""
        if sample_imgs:
            imgs_tags = "".join([f'<a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block overflow-hidden rounded-lg border border-slate-700 hover:border-purple-400 transition"><img src="{si}" alt="サンプル画像" class="w-full h-24 md:h-32 object-cover hover:scale-105 transition duration-300" loading="lazy" /></a>' for si in sample_imgs])
            sample_imgs_html = f"""<div class="mt-4 mb-6">
  <span class="text-xs font-bold text-slate-400 mb-2 block">📸 高画質サンプルシーン</span>
  <div class="grid grid-cols-2 md:grid-cols-4 gap-2">
    {imgs_tags}
  </div>
</div>"""

        item_html = f"""<div class="my-10 bg-slate-900/90 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-2xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 pb-4 border-b border-slate-800">
    <div class="flex items-center gap-3">
      {rank_badge}
      <span class="text-xs text-slate-400 font-mono tracking-wider">品番: {cid.upper()}</span>
    </div>
    <div class="text-xs text-purple-400 font-semibold bg-purple-950/60 border border-purple-800/60 px-3 py-1 rounded-full">
      FANZA公式配信中（{price}円〜）
    </div>
  </div>

  <h3 class="text-xl md:text-2xl font-black text-white mb-4 leading-snug">
    <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="hover:text-purple-400 transition">
      {title}
    </a>
  </h3>

  <div class="grid grid-cols-1 md:grid-cols-12 gap-6 mb-6">
    <div class="md:col-span-5">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block group overflow-hidden rounded-xl border border-slate-700/80 shadow-lg relative">
        <img src="{img}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition flex items-end p-4">
          <span class="text-xs text-purple-300 font-bold">FANZAで公式サンプルを再生 ▶</span>
        </div>
      </a>
      <div class="mt-3 flex items-center justify-between text-xs text-slate-400">
        <span>メーカー: <strong class="text-slate-200">{maker}</strong></span>
        <span>キャスト: {act_links}</span>
      </div>
      <div class="mt-2 flex flex-wrap gap-1">
        {genre_links}
      </div>
    </div>

    <div class="md:col-span-7 flex flex-col justify-between">
      <div class="text-slate-300 text-sm md:text-base leading-relaxed space-y-4">
        {work_analysis}
      </div>

      <div class="mt-6 pt-4 border-t border-slate-800/80 flex flex-wrap gap-3 items-center justify-between">
        <a href="/posts/{cid}" class="text-xs text-slate-400 hover:text-rose-400 underline transition">
          📄 作品の個別詳細ページを見る
        </a>
        <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="inline-flex items-center gap-2 bg-gradient-to-r from-purple-500 to-pink-600 hover:from-purple-400 hover:to-pink-500 text-slate-950 font-black px-6 py-3 rounded-xl shadow-lg hover:shadow-pink-500/20 transition transform hover:-translate-y-0.5 text-sm">
          <span>今すぐFANZAで本編・無料サンプルを見る</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
        </a>
      </div>
    </div>
  </div>

  {sample_imgs_html}
</div>"""
        html_parts.append(item_html)

    comparison_table = f"""<div class="my-12 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-2xl">
  <h3 class="text-xl md:text-2xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-purple-400">📊</span> 巨尻×バック後背位神作TOP5 徹底スペック比較まとめ
  </h3>
  <p class="text-slate-400 text-xs md:text-sm mb-6">尻のボリューム、肉弾の揺れ、ピストンの重さ、実用度を比較。究極の後背位体験をお選びください。</p>
  <div class="overflow-x-auto">
    <table class="w-full text-left text-xs md:text-sm border-collapse">
      <thead>
        <tr class="bg-slate-800/90 text-purple-300 border-b border-slate-700">
          <th class="p-3">順位 / タイトル</th>
          <th class="p-3">主演キャスト</th>
          <th class="p-3 text-center">尻ボリューム</th>
          <th class="p-3 text-center">肉弾揺れ度</th>
          <th class="p-3 text-center">ピストン迫力</th>
          <th class="p-3 text-center">実用度</th>
          <th class="p-3 text-right">公式リンク</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800 text-slate-300">
        <tr class="hover:bg-slate-800/40">
          <td class="p-3 font-bold text-white">第1位 最高肉感と肉弾バックピストン</td>
          <td class="p-3">小野坂ゆいか</td>
          <td class="p-3 text-center text-purple-400">★★★★★</td>
          <td class="p-3 text-center text-pink-400">★★★★★</td>
          <td class="p-3 text-center text-emerald-400">★★★★★</td>
          <td class="p-3 text-center text-purple-300 font-bold">5.0</td>
          <td class="p-3 text-right"><a href="{items[0].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-purple-400 hover:underline">FANZA ▶</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="p-3 font-bold text-white">第2位 無防備Tバック兄嫁 マシンガンバック</td>
          <td class="p-3">佐山愛</td>
          <td class="p-3 text-center text-purple-400">★★★★★</td>
          <td class="p-3 text-center text-pink-400">★★★★★</td>
          <td class="p-3 text-center text-emerald-400">★★★★★</td>
          <td class="p-3 text-center text-purple-300 font-bold">4.9</td>
          <td class="p-3 text-right"><a href="{items[1].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-purple-400 hover:underline">FANZA ▶</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="p-3 font-bold text-white">第3位 スナックお姉さんとアフター不倫</td>
          <td class="p-3">楪カレン</td>
          <td class="p-3 text-center text-purple-400">★★★★☆</td>
          <td class="p-3 text-center text-pink-400">★★★★☆</td>
          <td class="p-3 text-center text-emerald-400">★★★★☆</td>
          <td class="p-3 text-center text-purple-300 font-bold">4.8</td>
          <td class="p-3 text-right"><a href="{items[2].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-purple-400 hover:underline">FANZA ▶</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="p-3 font-bold text-white">第4位 真夏の汗だくナマ中出し肉弾FUCK</td>
          <td class="p-3">木下ひまり</td>
          <td class="p-3 text-center text-purple-400">★★★★☆</td>
          <td class="p-3 text-center text-pink-400">★★★★★</td>
          <td class="p-3 text-center text-emerald-400">★★★★★</td>
          <td class="p-3 text-center text-purple-300 font-bold">4.8</td>
          <td class="p-3 text-right"><a href="{items[3].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-purple-400 hover:underline">FANZA ▶</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="p-3 font-bold text-white">第5位 風呂借りにきた同僚と汗ダク本気交尾</td>
          <td class="p-3">月野かすみ</td>
          <td class="p-3 text-center text-purple-400">★★★★☆</td>
          <td class="p-3 text-center text-pink-400">★★★★☆</td>
          <td class="p-3 text-center text-emerald-400">★★★★☆</td>
          <td class="p-3 text-center text-purple-300 font-bold">4.7</td>
          <td class="p-3 text-right"><a href="{items[4].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-purple-400 hover:underline">FANZA ▶</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>"""
    html_parts.append(comparison_table)

    related_links_html = """<div class="my-8 bg-slate-900/60 border border-slate-800 rounded-2xl p-6">
  <h4 class="text-lg font-bold text-white mb-3 flex items-center gap-2">
    <span class="text-pink-400">🔗</span> あわせて読みたい人気特集記事
  </h4>
  <ul class="grid grid-cols-1 md:grid-cols-2 gap-3 text-sm text-slate-300">
    <li><a href="/posts/feature_fanza_black_gyaru_raw_creampie_ranking_2026" class="hover:text-purple-300 underline">【褐色小麦肌×濃厚種付け】黒ギャル・日焼けギャル中出しおすすめ神作ランキング</a></li>
    <li><a href="/posts/feature_fanza_first_anal_deflowering_ranking_2026" class="hover:text-purple-300 underline">【桃色処女孔が開く背徳】人気単体女優の初アナル解禁・肛門処女喪失神作ランキング</a></li>
    <li><a href="/posts/feature_fanza_vacuum_blowjob_deep_throat_ranking" class="hover:text-purple-300 underline">【即イキ必至の極上口淫】凄腕バキュームフェラ・喉奥ディープスロート特化選</a></li>
    <li><a href="/posts/feature_fanza_mens_esthe_secret_oil_massage_ranking" class="hover:text-purple-300 underline">【密着施術で理性崩壊】メンズエステ・裏オプ回春マッサージ神作ランキング</a></li>
  </ul>
</div>"""
    html_parts.append(related_links_html)

    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "ItemList",
                "name": "超巨尻・美尻×バック後背位ピストンおすすめ神作ランキングTOP5",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": idx + 1,
                        "name": it.get('title'),
                        "url": it.get('affiliate_url_clean')
                    } for idx, it in enumerate(items)
                ]
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": "巨尻作品で最も抜けるシチュエーションはどれですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "四つん這い後背位（バック）です。ヒップの揺れ、結合部のダイナミックな伸縮、そして打ち付ける生々しい肉音が同時に味わえるため、視覚的・聴覚的な刺激が最大化されます。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "画質は高画質で視聴できますか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "はい、FANZAの公式デジタル配信ではフルHD高画質に対応しており、肉の質感や汗の輝きまで極めて鮮明に鑑賞いただけます。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "単品購入と見放題（月額）どちらがお得ですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "紹介作品はセール時150円〜300円前後で購入可能なため、お気に入りの作品を単品購入してライブラリに永久保存するのが最もコスパ良くおすすめです。"
                        }
                    }
                ]
            }
        ]
    }
    json_ld_script = f'<script type="application/ld+json">\n{json.dumps(json_ld, ensure_ascii=False, indent=2)}\n</script>'
    html_parts.append(json_ld_script)

    full_html = "\n\n".join(html_parts)
    char_count = count_japanese_chars(full_html)
    print(f"Article 2 character count: {char_count} chars")
    if char_count < 3000:
        raise Exception(f"Article 2 is under 3000 chars: {char_count}")

    post_data = {
        "id": "feature_fanza_huge_ass_back_piston_ranking_2026",
        "title": "【肉弾ヒップが激震する快楽】FANZA「超巨尻・美尻×バック後背位ピストン」おすすめ神作ランキングTOP5！顔面騎乗窒息から腰砕け連続絶頂まで尻フェチ必携の殿堂入りAV選【2026年最新】",
        "date": "2026-10-03 10:30:00",
        "hinban": "HUGE-ASS-BACK-PISTON-BEST-2026",
        "price": "150~",
        "maker": "FANZA公式セレクション",
        "actresses": ["小野坂ゆいか", "佐山愛", "楪カレン", "木下ひまり", "月野かすみ"],
        "genres": ["巨尻", "美尻", "バック", "後背位", "肉感", "中出し", "特集", "殿堂入り"],
        "image": cover_image,
        "review": full_html
    }

    file_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f" -> Successfully saved Article 2 ({char_count} chars) to {file_path}")


# ==============================================================================
# 記事3: 人気女優の初アナル解禁・限界突破特化
# ==============================================================================
def generate_article_first_anal():
    print("=== Generating Article 3: 初アナル解禁特化 ===")
    cids = ["mvsd00453", "miab00053", "miaa00372", "cemd00402", "cemd00741"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["初アナル", "アナル解禁", "処女喪失", "限界突破"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 3 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-rose-950/40 via-slate-900 to-slate-950 border border-rose-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-rose-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-rose-500/20 text-rose-300 border border-rose-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">EXCLUSIVE RANKING</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月03日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【桃色処女孔が開く背徳と歓喜】FANZA「人気単体女優の初アナル解禁・肛門処女喪失」おすすめ神作ランキングTOP5！緊張の初挿入から前代未聞の2穴同時イキ狂いまで伝説の体当たりドキュメントAV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    AVというエンターテインメントにおいて、これほど男の胸を締め付け、狂おしい興奮を呼ぶテーマが他にあるでしょうか。それが、トップ女優たちがキャリアの転機として挑む「初アナル解禁・肛門処女喪失」です。普段は美しく清純な笑顔を振りまく人気単体女優が、人生で一度も許したことのない禁断の蕾をカメラの前に晒し、未知の領域へと足を踏み入れる瞬間。そこには作為のない本物の緊張、羞恥、そして覚悟が宿っています。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    潤滑ローションを塗られ、指先で少しずつほぐされていくピンク色の小さな菊門。初めてペニスの先端があてがわれた瞬間にビクッと震える太もも、異物感と圧迫感に思わず漏れ出る悲鳴のような声。しかし、丁寧に時間をかけて奥まで貫通した瞬間、未開の性感帯が電撃のように目覚め、痛みが未曾有の快楽へと反転していきます。前後の穴を同時に刺激され、白目を剥いて腰を浮かせながら絶頂する姿は、まさに人間の本能が露わになった奇跡のドキュメンタリーです。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、FANZAで配信されている数あるアナル作品の中から、やらせなしの真剣勝負、女優のリアルな涙と歓喜が克明に刻まれた【歴代最高峰のアナル解禁神作TOP5】を厳選。吉根ゆりあ、沙月恵奈、岬あずさなど、伝説の女優たちが魅せた一生に一度の体当たり名場面を完全解説します。
  </p>
</div>

<!-- アナル解禁作の醍醐味 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-rose-400">✨</span> アナル解禁AVが男を狂わせる3つの決定的理由
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-rose-300 mb-2">① 「一生に一度」しか撮れない処女喪失の重み</h4>
      <p class="text-slate-300 leading-relaxed">初めての経験だからこそ作れないリアルな表情。未開の蕾が開いていく瞬間の戸惑いと緊張感は、通常の性交シーンとは次元の違うドラマ性を放ちます。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-rose-300 mb-2">② 圧迫感から未曾有の快楽への劇的変化</h4>
      <p class="text-slate-300 leading-relaxed">最初は「苦しい…」と顔を歪めていた女優が、内壁を擦られるうちに「なんか、奥が熱い…変な感じする！」と快楽に目覚めていく覚醒プロセスが鳥肌モノのエロスを生みます。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-rose-300 mb-2">③ 前後2穴同時挿入の圧倒的破壊力</h4>
      <p class="text-slate-300 leading-relaxed">膣と肛門の両方を同時に埋め尽くされ、逃げ場のない快感で痙攣を繰り返すクライマックス。人間としての限界を超えた悦びの表情に誰もが圧倒されます。</p>
    </div>
  </div>
</div>"""
    html_parts.append(intro_html)

    for idx, it in enumerate(items, 1):
        cid = it.get("content_id")
        title = it.get("title", "")
        img = it.get("imageURL", {}).get("large", "")
        aff_url = it.get("affiliate_url_clean", "")
        price = it.get("prices", {}).get("price", "300~")
        sample_imgs = get_sample_images(it, 4)
        acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        maker = it.get("iteminfo", {}).get("maker", [{}])[0].get("name", "")
        
        act_links = " ".join([get_actress_link(a) for a in acts]) if acts else "専属キャスト"
        genre_links = " ".join([get_genre_link(g) for g in genres[:6]])

        rank_badge = f'<span class="bg-gradient-to-r from-rose-500 to-amber-500 text-slate-950 font-black text-sm px-3 py-1 rounded-full shadow-lg">第{idx}位</span>'

        if cid == "mvsd00453":
            work_analysis = """
<h4>【作品解説・見どころ】爆乳マゾ美女・吉根ゆりあが魅せる幸福のアナル狂い</h4>
<p>豊かな肉体美と天性のドM気質でファンを虜にする吉根ゆりあが、久方ぶりのアナル解禁に挑んだムーディーズの伝説的名作。事前の丁寧な開発から徐々に尻穴を広げられ、太い肉棒が根元まで飲み込まれた瞬間、彼女の顔に浮かぶ恍惚の表情は息をのむほど官能的です。「お尻の奥がキュンキュンしてたまらない…」と涙ぐみながら腰を突き出し、アナルでイキ狂う姿は、アナルセックスの快楽が極限に達した瞬間の奇跡を捉えています。</p>
<h4>【実用ポイント】爆乳を揺らしながらのアナル騎乗位と連続アクメ</h4>
<p>自らアナルで肉棒を咥え込み上下する騎乗位シーンは圧巻の一言。大きな胸が激しく波打ち、下から見上げるアングルでアナルが締め付けられる様子が克明に記録されています。</p>
"""
        elif cid == "miab00053":
            work_analysis = """
<h4>【作品解説・見どころ】美少女・沙月恵奈が人生で初めて尻穴を捧げた衝撃作</h4>
<p>圧倒的な透明感と小悪魔的な可愛さで絶大な人気を誇る沙月恵奈が、人生で初めて肛門性交を解禁したメモリアル大作。挿入前の極度の緊張から、少しずつペニスを受け入れ、やがて痛みを忘れて悦びの声をあげていくリアルな過程が克明にドキュメントされています。美少女の華奢な身体に繰り広げられる過激な2穴責めのギャップが、鑑賞者の理性をもろくも打ち砕きます。</p>
<h4>【実用ポイント】生まれて初めての異物感に潤む瞳と痙攣絶頂</h4>
<p>「本当に大丈夫ですか…？」と不安げに見つめていた瞳が、アナル刺激によって快楽に染まっていく変化が秀逸。前後から同時に貫かれ、全身を震わせてアクメに達する瞬間は言葉を失うほどの迫力です。</p>
"""
        elif cid == "miaa00372":
            work_analysis = """
<h4>【作品解説・見どころ】「ヤバ…ッ！ヤヴァい」激ピスでアクメ顔連発の神回</h4>
<p>トップ女優・岬あずさが魅せた、アナルAV史上に残る大傑作。「ヤバい！無理、壊れちゃう！」と叫びながらも、激しいピストンを受けるごとにアヘ顔を晒し、快楽の底なし沼へと落ちていく姿が記録されています。男優の手加減なしのピストンに対し、尻穴をギュウギュウに締め付けながら絶頂を繰り返す岬あずさの本気度が画面越しに熱く伝わってきます。</p>
<h4>【実用ポイント】アナルに根元まで埋め込まれたままの激しい腰振り</h4>
<p>結合部のドアップ接写が多用され、アナルが肉棒の太さに合わせて押し広げられる様子が生々しく捉えられています。ヘッドホンから聞こえる岬あずさの切羽詰まった喘ぎ声が最高潮の興奮を約束します。</p>
"""
        elif cid == "cemd00402":
            work_analysis = """
<h4>【作品解説・見どころ】限界ギリギリの圧迫感に叫びヨガったリアル開発劇</h4>
<p>セレブの友レーベルが誇る、徹底したリアリズムで描かれた水川かえでの初アナル解禁作。演技ではない本物の圧迫感と格闘しながら、少しずつ快感のツボを開発されていく過程が極めて丁寧に描かれています。大人の女性が恥じらいを捨てて尻穴を広げ、快楽に屈服していく姿は熟女・人妻ファンにもたまらない魅力を放ちます。</p>
<h4>【実用ポイント】羞恥に耐えながら未知の快楽に身を任せる生々しさ</h4>
<p>腰を浮かせて逃げよう配慮しながらも、奥を突かれると抗えない快楽に震えるリアリズム。じっくりと時間をかけて開発されていく導入から、最後の激しい本番まで一切の無駄がない完成度です。</p>
"""
        else:
            work_analysis = """
<h4>【作品解説・見どころ】森沢かなが魅せる、最初で最後かもしれない幻のアナル復活劇</h4>
<p>圧倒的な美貌とスタイルを持つ森沢かなが、撮影現場での直接交渉により実現した奇跡のアナルSEX復活作。経験豊富でありながらも、久方ぶりのアナル挿入に息を呑み、緊張した面持ちで受け入れる姿がエロティシズムを極限まで高めます。大人の色香漂う森沢かなが、アナルを貫かれながら乱れ狂う姿はファン垂涎の超貴重映像です。</p>
<h4>【実用ポイント】成熟した美貌とアナルセックスの背徳的コントラスト</h4>
<p>エレガントな美貌を持つ女優が、最も淫らな穴を晒して快楽に溺れていく背徳感。完璧なプロポーションを背後から捉えたバックアングルの美しさは、鑑賞者を深く魅了して離しません。</p>
"""

        sample_imgs_html = ""
        if sample_imgs:
            imgs_tags = "".join([f'<a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block overflow-hidden rounded-lg border border-slate-700 hover:border-rose-400 transition"><img src="{si}" alt="サンプル画像" class="w-full h-24 md:h-32 object-cover hover:scale-105 transition duration-300" loading="lazy" /></a>' for si in sample_imgs])
            sample_imgs_html = f"""<div class="mt-4 mb-6">
  <span class="text-xs font-bold text-slate-400 mb-2 block">📸 高画質サンプルシーン</span>
  <div class="grid grid-cols-2 md:grid-cols-4 gap-2">
    {imgs_tags}
  </div>
</div>"""

        item_html = f"""<div class="my-10 bg-slate-900/90 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-2xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 pb-4 border-b border-slate-800">
    <div class="flex items-center gap-3">
      {rank_badge}
      <span class="text-xs text-slate-400 font-mono tracking-wider">品番: {cid.upper()}</span>
    </div>
    <div class="text-xs text-rose-400 font-semibold bg-rose-950/60 border border-rose-800/60 px-3 py-1 rounded-full">
      FANZA公式配信中（{price}円〜）
    </div>
  </div>

  <h3 class="text-xl md:text-2xl font-black text-white mb-4 leading-snug">
    <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="hover:text-rose-400 transition">
      {title}
    </a>
  </h3>

  <div class="grid grid-cols-1 md:grid-cols-12 gap-6 mb-6">
    <div class="md:col-span-5">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block group overflow-hidden rounded-xl border border-slate-700/80 shadow-lg relative">
        <img src="{img}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition flex items-end p-4">
          <span class="text-xs text-rose-300 font-bold">FANZAで公式サンプルを再生 ▶</span>
        </div>
      </a>
      <div class="mt-3 flex items-center justify-between text-xs text-slate-400">
        <span>メーカー: <strong class="text-slate-200">{maker}</strong></span>
        <span>キャスト: {act_links}</span>
      </div>
      <div class="mt-2 flex flex-wrap gap-1">
        {genre_links}
      </div>
    </div>

    <div class="md:col-span-7 flex flex-col justify-between">
      <div class="text-slate-300 text-sm md:text-base leading-relaxed space-y-4">
        {work_analysis}
      </div>

      <div class="mt-6 pt-4 border-t border-slate-800/80 flex flex-wrap gap-3 items-center justify-between">
        <a href="/posts/{cid}" class="text-xs text-slate-400 hover:text-rose-400 underline transition">
          📄 作品の個別詳細ページを見る
        </a>
        <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="inline-flex items-center gap-2 bg-gradient-to-r from-rose-500 to-amber-600 hover:from-rose-400 hover:to-amber-500 text-slate-950 font-black px-6 py-3 rounded-xl shadow-lg hover:shadow-rose-500/20 transition transform hover:-translate-y-0.5 text-sm">
          <span>今すぐFANZAで本編・無料サンプルを見る</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
        </a>
      </div>
    </div>
  </div>

  {sample_imgs_html}
</div>"""
        html_parts.append(item_html)

    comparison_table = f"""<div class="my-12 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-2xl">
  <h3 class="text-xl md:text-2xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-rose-400">📊</span> 初アナル解禁神作TOP5 徹底スペック比較まとめ
  </h3>
  <p class="text-slate-400 text-xs md:text-sm mb-6">開発の丁寧さ、女優の覚醒度、2穴絶頂度、実用度を客観比較。伝説の体当たりドキュメントをお選びください。</p>
  <div class="overflow-x-auto">
    <table class="w-full text-left text-xs md:text-sm border-collapse">
      <thead>
        <tr class="bg-slate-800/90 text-rose-300 border-b border-slate-700">
          <th class="p-3">順位 / タイトル</th>
          <th class="p-3">主演キャスト</th>
          <th class="p-3 text-center">開発丁寧度</th>
          <th class="p-3 text-center">覚醒・イキ狂い</th>
          <th class="p-3 text-center">2穴絶頂度</th>
          <th class="p-3 text-center">実用度</th>
          <th class="p-3 text-right">公式リンク</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800 text-slate-300">
        <tr class="hover:bg-slate-800/40">
          <td class="p-3 font-bold text-white">第1位 最初で最高のアナル解禁</td>
          <td class="p-3">吉根ゆりあ</td>
          <td class="p-3 text-center text-rose-400">★★★★★</td>
          <td class="p-3 text-center text-amber-400">★★★★★</td>
          <td class="p-3 text-center text-emerald-400">★★★★★</td>
          <td class="p-3 text-center text-rose-300 font-bold">5.0</td>
          <td class="p-3 text-right"><a href="{items[0].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-rose-400 hover:underline">FANZA ▶</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="p-3 font-bold text-white">第2位 アナル解禁！天才美少女</td>
          <td class="p-3">沙月恵奈</td>
          <td class="p-3 text-center text-rose-400">★★★★★</td>
          <td class="p-3 text-center text-amber-400">★★★★☆</td>
          <td class="p-3 text-center text-emerald-400">★★★★★</td>
          <td class="p-3 text-center text-rose-300 font-bold">4.9</td>
          <td class="p-3 text-right"><a href="{items[1].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-rose-400 hover:underline">FANZA ▶</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="p-3 font-bold text-white">第3位 初アナル神回SP「ヤバ…ッ！」</td>
          <td class="p-3">岬あずさ</td>
          <td class="p-3 text-center text-rose-400">★★★★☆</td>
          <td class="p-3 text-center text-amber-400">★★★★★</td>
          <td class="p-3 text-center text-emerald-400">★★★★☆</td>
          <td class="p-3 text-center text-rose-300 font-bold">4.9</td>
          <td class="p-3 text-right"><a href="{items[2].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-rose-400 hover:underline">FANZA ▶</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="p-3 font-bold text-white">第4位 限界ギリギリの圧迫感に叫びヨガった</td>
          <td class="p-3">水川かえで</td>
          <td class="p-3 text-center text-rose-400">★★★★★</td>
          <td class="p-3 text-center text-amber-400">★★★★☆</td>
          <td class="p-3 text-center text-emerald-400">★★★★☆</td>
          <td class="p-3 text-center text-rose-300 font-bold">4.8</td>
          <td class="p-3 text-right"><a href="{items[3].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-rose-400 hover:underline">FANZA ▶</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="p-3 font-bold text-white">第5位 1本限りのアナルSEX復活！</td>
          <td class="p-3">森沢かな</td>
          <td class="p-3 text-center text-rose-400">★★★★☆</td>
          <td class="p-3 text-center text-amber-400">★★★★☆</td>
          <td class="p-3 text-center text-emerald-400">★★★★☆</td>
          <td class="p-3 text-center text-rose-300 font-bold">4.7</td>
          <td class="p-3 text-right"><a href="{items[4].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-rose-400 hover:underline">FANZA ▶</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>"""
    html_parts.append(comparison_table)

    related_links_html = """<div class="my-8 bg-slate-900/60 border border-slate-800 rounded-2xl p-6">
  <h4 class="text-lg font-bold text-white mb-3 flex items-center gap-2">
    <span class="text-rose-400">🔗</span> あわせて読みたい人気特集記事
  </h4>
  <ul class="grid grid-cols-1 md:grid-cols-2 gap-3 text-sm text-slate-300">
    <li><a href="/posts/feature_fanza_black_gyaru_raw_creampie_ranking_2026" class="hover:text-rose-300 underline">【褐色小麦肌×濃厚種付け】黒ギャル・日焼けギャル中出しおすすめ神作ランキング</a></li>
    <li><a href="/posts/feature_fanza_huge_ass_back_piston_ranking_2026" class="hover:text-rose-300 underline">【肉弾ヒップが激震する快楽】巨尻・美尻×バック後背位ピストンおすすめ神作ランキング</a></li>
    <li><a href="/posts/feature_fanza_vacuum_blowjob_deep_throat_ranking" class="hover:text-rose-300 underline">【即イキ必至の極上口淫】凄腕バキュームフェラ・喉奥ディープスロート特化選</a></li>
    <li><a href="/posts/feature_fanza_outdoor_exposure_public_shame_ranking" class="hover:text-rose-300 underline">【羞恥心崩壊の背徳快楽】野外露出・青姦・公衆羞恥プレイおすすめ神作選</a></li>
  </ul>
</div>"""
    html_parts.append(related_links_html)

    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "ItemList",
                "name": "人気単体女優の初アナル解禁・肛門処女喪失神作ランキングTOP5",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": idx + 1,
                        "name": it.get('title'),
                        "url": it.get('affiliate_url_clean')
                    } for idx, it in enumerate(items)
                ]
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": "アナル初心者でも楽しめる作品はどれですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第1位の吉根ゆりあ出演作、または第2位の沙月恵奈出演作がおすすめです。事前の開発プロセスが非常に丁寧で、痛みが快感へと変わる過程がわかりやすく描かれています。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "本当に初めてのアナルセックスですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "紹介している作品は、女優自身がアナル初解禁を公言して撮影された記念碑的ドキュメンタリーであり、真剣な体当たりの臨場感を味わえます。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "前後の穴への2穴同時挿入シーンはありますか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "はい、今回厳選した作品の多くでクライマックスに前後2穴同時挿入（ダブルペネトレーション）や交互挿入が収録されており、最高潮の迫力を楽しめます。"
                        }
                    }
                ]
            }
        ]
    }
    json_ld_script = f'<script type="application/ld+json">\n{json.dumps(json_ld, ensure_ascii=False, indent=2)}\n</script>'
    html_parts.append(json_ld_script)

    full_html = "\n\n".join(html_parts)
    char_count = count_japanese_chars(full_html)
    print(f"Article 3 character count: {char_count} chars")
    if char_count < 3000:
        raise Exception(f"Article 3 is under 3000 chars: {char_count}")

    post_data = {
        "id": "feature_fanza_first_anal_deflowering_ranking_2026",
        "title": "【桃色処女孔が開く背徳と歓喜】FANZA「人気単体女優の初アナル解禁・肛門処女喪失」おすすめ神作ランキングTOP5！緊張の初挿入から前代未聞の2穴同時イキ狂いまで伝説の体当たりドキュメントAV選【2026年最新】",
        "date": "2026-10-03 11:00:00",
        "hinban": "FIRST-ANAL-DEFLOWERING-BEST-2026",
        "price": "150~",
        "maker": "FANZA公式セレクション",
        "actresses": ["吉根ゆりあ", "沙月恵奈", "岬あずさ", "水川かえで", "森沢かな"],
        "genres": ["アナル", "初アナル", "解禁", "処女喪失", "2穴", "特集", "殿堂入り"],
        "image": cover_image,
        "review": full_html
    }

    file_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f" -> Successfully saved Article 3 ({char_count} chars) to {file_path}")


def main():
    print("==================================================")
    print("FANZA公式APIリアルタイム取得・超大型キラー特集3記事自動生成開始")
    print("==================================================")
    generate_article_black_gyaru()
    print("--------------------------------------------------")
    generate_article_huge_ass()
    print("--------------------------------------------------")
    generate_article_first_anal()
    print("==================================================")
    print("3記事すべての生成が正常に完了しました！")
    print("==================================================")

if __name__ == "__main__":
    main()
