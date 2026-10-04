# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・超大型キラー特集3記事自動生成スクリプト
1. 【幼馴染・お泊まり宅飲み＆実家帰省特化】
   『【昔の面影と大人の色気】FANZA「幼馴染・お泊まり宅飲み＆実家帰省の秘密」おすすめ神作ランキングTOP5！無警戒な寝顔と素肌の温もりに理性を奪われて貪り合う背徳中出しAV選【2026年最新】』
2. 【終電逃し・無防備部屋着・お泊まり特化】
   『【終電逃しから始まる部屋着の誘惑】FANZA「同僚・後輩女子宅へのお泊まり＆無防備部屋着」おすすめ神作ランキングTOP5！ノーブラすっぴんの隙だらけボディに理性が狂う一夜限りの生中出しAV選【2026年最新】』
3. 【凄テク我慢・耐えたらご褒美生中出し特化】
   『【男の限界を試す極上テクニック】FANZA「凄テク我慢できれば生中出しSEX」おすすめ神作ランキングTOP5！名器と神技フェラに耐え抜いてご褒美膣内射精を勝ち取る実用度MAX・AV選【2026年最新】』
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

def generate_individual_post_if_needed(it, special_labels=None, custom_review=None):
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
        
    act_str = "・".join(acts) if acts else "トップ女優"
    
    if custom_review:
        review_html = custom_review
    else:
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
# 記事1: 幼馴染・お泊まり宅飲み＆実家帰省の秘密 特化
# ==============================================================================
def generate_article_childhood_friend():
    print("=== Generating Article 1: 幼馴染お泊まり・帰省一線越え特化 ===")
    cids = ["midv00757", "mida00101", "ssis00429", "cjod00467", "midv00035"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["幼馴染", "お泊まり", "再会", "中出し", "コソ練", "殿堂入り"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 1 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-amber-950/40 via-slate-900 to-slate-950 border border-amber-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-amber-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-amber-500/20 text-amber-300 border border-amber-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">CHILDHOOD FRIEND PREMIUM SPECIAL</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月05日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【昔の面影と大人の色気】FANZA「幼馴染・お泊まり宅飲み＆実家帰省の秘密」おすすめ神作ランキングTOP5！無警戒な寝顔と素肌の温もりに理性を奪われて貪り合う背徳中出しAV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    泥だらけになって一緒に遊んでいた幼少期、名前を呼び合って何でも打ち明け合えた気心の知れた関係――そんな「幼馴染」が、いつの間にか息をのむほど艶やかな大人の女性へと成長していたら。男なら誰もが一度は妄想し、心の奥底で渇望してやまない究極のノスタルジック・エロティシズム、それが「幼馴染モノ」の真髄です。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    昔の距離感のまま無警戒に部屋へ上がり込んできて、畳の上で足を投げ出してくつろぐ無防備な姿。ふわりと漂うシャンプーの甘い香り、胸元から覗く豊満な谷間、そして「ねぇ、私のこと女として見たことある？」という何気ない一言。幼馴染という絶対的な安心感があるからこそ、一度タガが外れた瞬間の背徳感と肉欲の爆発力は他のどんなシチュエーションをも凌駕します。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、小野六花が魅せる「彼氏ができたからセックスの練習して？」という禁断の懇願から、石川澪の早漏克服コソ練、小倉七海の小悪魔的イチャつき再会、春陽モカの同窓会ほろ酔いギャル化お泊まり、そして中山ふみかの欲求不満爆発・馬乗り交尾まで、実用度・没入感ともに最高峰を誇る【幼馴染神作TOP5】を徹底解説します。
  </p>
</div>

<!-- 選び方の基準 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-amber-400">🏡</span> 幼馴染モノで極上射精を迎えるための3大チェックポイント
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-amber-300 mb-2">① 「練習」「コソ練」という背徳の口実</h4>
      <p class="text-slate-300 leading-relaxed">「彼氏と初体験する前の練習台になって」「早漏を治す手伝いをしてあげる」など、幼馴染だからこそ成立する言い訳から理性が崩壊していく過程が最高に興奮を煽ります。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-amber-300 mb-2">② 無防備なお泊まりと実家の密室感</h4>
      <p class="text-slate-300 leading-relaxed">親の不在、実家帰省、宅飲み後の雑魚寝。薄い布団一枚、壁一枚隔てた空間で、吐息を押し殺しながら肌を重ねるスリルが実用度を跳ね上げます。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-amber-300 mb-2">③ タメ口から雌の甘い喘ぎ声への激変</h4>
      <p class="text-slate-300 leading-relaxed">「ちょっと、どこ触ってんのよ…バカ」とからかっていた態度が、結合した瞬間に潤んだ瞳で「あっ…ダメ、これ気持ちよすぎる…！」と蕩けていく落差こそが至高の抜きどころです。</p>
    </div>
  </div>
</div>"""
    html_parts.append(intro_html)

    reviews_data = {
        "midv00757": {
            "desc": """<h4>【作品解説・見どころ】小野六花が懇願する「セックスの練習台になって…」から始まる三日三晩の肉欲地獄</h4>
<p>AV界トップクラスの透明感と小悪魔的な可愛さを併せ持つ小野六花が、両親の不在を狙って幼馴染の部屋へやって来る衝撃の導入。「初めて彼氏ができたんだけど、痛かったら怖いから一回だけ練習してくれない？」とコンドームを1個だけ差し出してくる姿に、男なら誰しも下半身が熱く疼くはずです。ぎこちない手つきで始まったはずの愛撫が、肌と肌が触れ合う熱量によって徐々に本能の暴走へと変貌していきます。</p>
<h4>【実用ポイント】ゴム無しの生ハメに目覚め、止まらなくなる激ピストン</h4>
<p>「一回だけ」という約束は完全に霧散し、小野六花の敏感すぎる肉体が本気で快楽に目覚めてしまいます。ゴムを外した生の亀頭が膣口を押し広げ、奥深くの最深部をズブズブと貫くたびに、六花はベッドのシーツを握りしめて激しくのたうち回ります。汗だくになりながら三日三晩にわたって繰り返される中出し交尾は、鑑賞者の射精中枢を容赦なく破壊する凄まじい実用度を誇ります。</p>""",
            "rating": "★★★★★ 5.0 / 5.0",
            "service_score": "幼馴染萌え度: 100% | 生中出し背徳感: 100% | 実用性: 100%"
        },
        "mida00101": {
            "desc": """<h4>【作品解説・見どころ】石川澪のお節介コソ練！早漏なボクをチンポ調教する極上育精サポート</h4>
<p>可憐な美少女・石川澪が、お節介焼きで面倒見の良い幼馴染を演じる大人気作。「アンタ、女の子とエッチしたことないからって、そんなすぐイッちゃダメでしょ？」と、早漏に悩む主人公を見かねて自らの手と口、そして温かなアソコを使って“射精トレーニング”を施してくれる夢のようなシチュエーションです。からかい混じりの笑顔で見つめられながら、先端をちろちろと舌先で転がされるフェラチオは瞬殺必至の快感。</p>
<h4>【実用ポイント】焦らしと密着騎乗位で搾り取られる濃厚種付け</h4>
<p>ギリギリまで寸止めを繰り返された末、石川澪自らが上に跨がり、ゆっくりと肉棒を飲み込んでいく騎乗位シーンは圧巻のひと言。「まだ出しちゃダメだよ…我慢して…」と囁きながら、腰をくねらせて男の弱点を的確に刺激してくる姿は、可愛らしさと淫乱さが極限のバランスで融合しています。男の精力を根こそぎ搾り取る濃密なフィニッシュに悶絶すること間違いありません。</p>""",
            "rating": "★★★★★ 4.9 / 5.0",
            "service_score": "コソ練フェチ度: 99% | 早漏焦らし度: 100% | 実用性: 99%"
        },
        "ssis00429": {
            "desc": """<h4>【作品解説・見どころ】小倉七海との久しぶりの再会！ウブだった少女が魅せる小悪魔イチャつき責め</h4>
<p>圧倒的スタイルとアイドル級のルックスで絶大な支持を集めた小倉七海が、久しぶりに再会した幼馴染を徹底的に翻弄する傑作。子供の頃は大人しくて純情だった七海ちゃんが、見違えるような美貌と色香を漂わせて目の前に現れるだけで息を呑みます。二人きりになった部屋で、昔話を口実に距離を詰めてきて、耳元に甘い吐息を吹きかけながら「私のこと、どんな風に思い出してた？」と小悪魔な視線を投げかけてきます。</p>
<h4>【実用ポイント】昼間から朝焼けまで止まらない濃密スキンシップ交尾</h4>
<p>一度唇を重ねてしまえば、そこからは昼夜の境目を失うほどのイチャラブ濃密セックスへ。七海ちゃんの吸い付くような柔らかい美肌、キュッと引き締まったウエスト、そして結合部から溢れ出る愛液の音。正常位で抱きしめ合いながら互いの体温を確かめ合い、何度も何度も絶頂を重ねていく幸福感と背徳感は、まさに幼馴染モノの理想郷です。</p>""",
            "rating": "★★★★★ 4.9 / 5.0",
            "service_score": "ビジュアル完成度: 100% | イチャラブ度: 98% | 実用性: 99%"
        },
        "cjod00467": {
            "desc": """<h4>【作品解説・見どころ】春陽モカがキレカワ最強ギャルに変貌！同窓会ほろ酔いラブホ連れ込み</h4>
<p>地味だった幼馴染が、同窓会で再会したら息をのむほど洗練されたキレカワ最強ギャルに大変身していたという男の夢が詰まった1本。春陽モカの抜群のプロポーションと茶髪ショートの華やかさが眩しすぎます。酒が進むにつれて「昔からアンタのこと気になってたんだよね」と急接近。そのまま勢いでラブホテルへと連れ込まれ、ほろ酔い気分のまま貪り合うように舌を絡め合います。</p>
<h4>【実用ポイント】強気なギャルがメスの顔で中出しをおねだりするギャップ</h4>
<p>最初はギャル特有のノリでリードしていた春陽モカが、生ハメピストンの深さと逞しさに呑まれて次第にトロ顔へと崩壊していく様がたまらなくエロい。「中に出して…お願い、全部出してぇ！」と喘ぎながら、男の腰を太ももでぎゅっとロックして種付けを懇願するシーンは、脳髄が痺れるほどの快感をもたらします。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "ギャル変貌度: 100% | ほろ酔いエロス: 98% | 実用性: 98%"
        },
        "midv00035": {
            "desc": """<h4>【作品解説・見どころ】中山ふみかの禁欲巨乳騎乗位！彼氏と別れて帰省中の欲求不満幼馴染</h4>
<p>圧倒的な肉感とド迫力の巨乳を誇る中山ふみかが、彼氏と別れた傷心と溜まりに溜まった性欲を抱えて地元へ帰省してきた1歳年上の幼馴染を熱演。久々に実家で顔を合わせた彼女は、失恋の寂しさを紛らわせるかのように酒を煽り、無防備な胸元をはだけさせて男の部屋に乱入してきます。男の股間が膨らんでいるのを見逃さず、「ねぇ、慰めてよ…」と馬乗りになってくる導入から興奮度はMAXです。</p>
<h4>【実用ポイント】豊満な胸が激しく波打つエンドレス馬乗り搾精</h4>
<p>中山ふみかの重量級バストが上下左右に揺れ動き、男のペニスを根元まで飲み込みながら狂ったように腰を振る騎乗位は圧巻のド迫力。男が射精してもなお「まだ足りない…もっとちょうだい」と腰を浮かせず、連続で精子を搾り取ろうとする飢えた肉食ぶりは、実用度・抜きやすさともにトップクラスの破壊力です。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "巨乳肉感度: 100% | 騎乗位迫力度: 99% | 実用性: 98%"
        }
    }

    for idx, it in enumerate(items):
        cid = it.get("content_id")
        title = it.get("title")
        aff_url = it.get("affiliate_url_clean")
        large_img = it.get("imageURL", {}).get("large", "")
        acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        act_html = " ".join([get_actress_link(a) for a in acts])
        genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        genre_html = " ".join([get_genre_link(g) for g in genres[:6]])
        sample_imgs = get_sample_images(it, 4)
        c_data = reviews_data.get(cid, {})

        sample_imgs_html = ""
        if sample_imgs:
            img_tags = "".join([f'<img src="{sim}" alt="{title} サンプル{s_idx+1}" class="w-full h-28 object-cover rounded-lg border border-slate-700/80 hover:scale-105 transition transform duration-300" loading="lazy" />' for s_idx, sim in enumerate(sample_imgs)])
            sample_imgs_html = f'<div class="grid grid-cols-2 md:grid-cols-4 gap-2 my-4">{img_tags}</div>'

        item_block = f"""
<div class="my-10 bg-slate-900/90 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-2xl relative">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-2">
      <span class="bg-amber-600 text-white font-black text-sm px-3 py-1 rounded-lg">第{idx+1}位</span>
      <span class="text-xs text-slate-400 font-mono tracking-wider">品番: {cid.upper()}</span>
    </div>
    <div class="text-amber-400 font-black text-sm tracking-wide">{c_data.get('rating', '★★★★★ 5.0 / 5.0')}</div>
  </div>

  <h3 class="text-xl md:text-2xl font-black text-white leading-snug mb-4 hover:text-amber-400 transition">
    <a href="{aff_url}" target="_blank" rel="nofollow noopener">{title}</a>
  </h3>

  <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-start">
    <div class="md:col-span-5">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block group overflow-hidden rounded-xl border border-slate-700/80 shadow-lg relative">
        <img src="{large_img}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition duration-300 flex items-end p-4">
          <span class="bg-amber-600 text-white font-bold text-xs px-3 py-1.5 rounded-full shadow-lg">FANZA公式で今すぐ無料サンプル再生 ▶</span>
        </div>
      </a>
      <div class="mt-3 text-xs bg-slate-800/60 p-2.5 rounded-lg border border-slate-700/50 text-slate-300">
        <div class="mb-1"><span class="text-slate-400">主演女優:</span> {act_html}</div>
        <div><span class="text-slate-400">スペック評価:</span> <span class="text-amber-300 font-medium">{c_data.get('service_score', '実用性 100%')}</span></div>
      </div>
    </div>

    <div class="md:col-span-7 space-y-4 text-slate-300 text-sm md:text-base leading-relaxed">
      {c_data.get('desc', '')}
      
      <div class="pt-2">
        <div class="text-xs text-slate-400 mb-2 font-medium">関連ジャンルタグ:</div>
        <div class="flex flex-wrap gap-1.5">{genre_html}</div>
      </div>
    </div>
  </div>

  {sample_imgs_html}

  <div class="mt-6 flex flex-col sm:flex-row items-center justify-between gap-4 bg-slate-950/80 p-4 rounded-xl border border-slate-800">
    <div class="text-xs text-slate-400">
      高画質ストリーミング／ダウンロード対応・スマホ即時視聴可能
    </div>
    <div class="flex items-center gap-3 w-full sm:w-auto">
      <a href="/posts/{cid}" class="text-center px-4 py-2.5 rounded-xl border border-slate-700 text-slate-300 hover:text-white hover:bg-slate-800 text-xs font-bold transition w-1/2 sm:w-auto">
        詳細個別レビューを見る
      </a>
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="text-center bg-gradient-to-r from-amber-600 to-orange-600 hover:from-amber-500 hover:to-orange-500 text-white text-sm font-black px-6 py-2.5 rounded-xl shadow-lg shadow-amber-900/40 hover:shadow-amber-800/60 transition transform hover:-translate-y-0.5 w-1/2 sm:w-auto">
        FANZA公式で今すぐ本編を見る ▶
      </a>
    </div>
  </div>
</div>"""
        html_parts.append(item_block)

    faq_html = """<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl">
  <h3 class="text-xl md:text-2xl font-black text-white mb-6 flex items-center gap-2">
    <span class="text-amber-400">❓</span> 幼馴染AVに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-6 text-sm md:text-base">
    <div class="border-b border-slate-800 pb-4">
      <h4 class="font-bold text-amber-300 mb-2">Q1. 幼馴染モノの最大の魅力・抜きどころは何ですか？</h4>
      <p class="text-slate-300 leading-relaxed">何と言っても「過去の無邪気な思い出」と「目の前にある成熟した肉体」の圧倒的なギャップです。友達関係という防壁があるからこそ、一度唇を重ねて一線を越えてしまったときの背徳感と、タメ口で乱れ喘ぐ生々しさが最高の射精カタルシスを生み出します。</p>
    </div>
    <div class="border-b border-slate-800 pb-4">
      <h4 class="font-bold text-amber-300 mb-2">Q2. 初めて見るならどの作品が一番おすすめですか？</h4>
      <p class="text-slate-300 leading-relaxed">まずは第1位の小野六花『彼氏ができたからセックスの練習して？』が鉄板中の鉄板です。導入の可愛らしさから中盤以降の生ハメ依存症への変貌まで、幼馴染モノの醍醐味が全て凝縮されています。甘えん坊でイチャラブ重視なら第2位の石川澪や第3位の小倉七海がおすすめです。</p>
    </div>
    <div>
      <h4 class="font-bold text-amber-300 mb-2">Q3. スマホでも高画質で視聴できますか？</h4>
      <p class="text-slate-300 leading-relaxed">はい、FANZAのデジタル動画はスマホ・タブレット・PCのブラウザから高画質HD/4Kストリーミング再生が可能です。購入後すぐに視聴でき、専用アプリを使えばオフライン再生にも対応しています。</p>
    </div>
  </div>
</div>"""
    html_parts.append(faq_html)

    related_links_html = """<div class="my-8 bg-slate-950 border border-slate-800 rounded-2xl p-6">
  <h4 class="text-base font-bold text-white mb-3">🔥 あわせて読みたい人気キラー特集</h4>
  <ul class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm text-amber-300">
    <li><a href="/posts/feature_fanza_teasing_sister_devilish_seduction_ranking_2026" class="hover:underline">▶ 小悪魔妹の無邪気な誘惑ランキングTOP5！一つ屋根の下の禁断生活</a></li>
    <li><a href="/posts/feature_fanza_home_tutor_private_lesson_seduction_ranking_2026" class="hover:underline">▶ 美人家庭教師・密室個人レッスンランキングTOP5！大人の授業</a></li>
    <li><a href="/posts/feature_fanza_class_reunion_married_classmate_affair_ranking_2026" class="hover:underline">▶ 同窓会再会・人妻クラスメイトとの泥酔W不倫ランキングTOP5！</a></li>
    <li><a href="/posts/feature_fanza_neighbor_young_wife_forbidden_affair_ranking_2026" class="hover:underline">▶ 隣の若妻・留守中のベランダ密会＆玄関先不倫ランキングTOP5！</a></li>
  </ul>
</div>"""
    html_parts.append(related_links_html)

    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "ItemList",
                "name": "幼馴染おすすめ神作ランキングTOP5",
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
                        "name": "幼馴染モノの最大の魅力・抜きどころは何ですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "過去の無邪気な思い出と現在の成熟した肉体のギャップです。友達関係の防壁が崩れ、タメ口で乱れ喘ぐ生々しさが最高の実用度を誇ります。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "初めて見るならどの作品が一番おすすめですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第1位の小野六花『彼氏ができたからセックスの練習して？』が鉄板です。導入の可愛らしさから生ハメ依存症への変貌が圧巻です。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "スマホでも高画質で視聴できますか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "はい、FANZA公式のデジタル配信によりスマホ・タブレット・PCのブラウザから高画質HDストリーミング再生が可能です。"
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
        "id": "feature_fanza_childhood_friend_sleepover_first_night_ranking_2026",
        "title": "【昔の面影と大人の色気】FANZA「幼馴染・お泊まり宅飲み＆実家帰省の秘密」おすすめ神作ランキングTOP5！無警戒な寝顔と素肌の温もりに理性を奪われて貪り合う背徳中出しAV選【2026年最新】",
        "date": "2026-10-05 01:00:00",
        "hinban": "CHILDHOOD-FRIEND-SLEEPOVER-2026",
        "price": "300~",
        "maker": "FANZA公式セレクション",
        "actresses": ["小野六花", "石川澪", "小倉七海", "春陽モカ", "中山ふみか"],
        "genres": ["幼馴染", "お泊まり", "宅飲み", "実家帰省", "コソ練", "中出し", "騎乗位", "美少女", "特集", "殿堂入り"],
        "image": cover_image,
        "review": full_html
    }

    file_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f" -> Successfully saved Article 1 ({char_count} chars) to {file_path}")


# ==============================================================================
# 記事2: 終電逃し・無防備部屋着・お泊まり特化
# ==============================================================================
def generate_article_roomwear():
    print("=== Generating Article 2: 終電逃し・無防備部屋着お泊まり特化 ===")
    cids = ["ipx00515", "cawd00863", "pppe00435", "cawd00963", "ipzz00857"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["部屋着", "終電逃し", "お泊まり", "同僚", "後輩", "中出し"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 2 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-purple-950/40 via-slate-900 to-slate-950 border border-purple-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-purple-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-purple-500/20 text-purple-300 border border-purple-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">ROOMWEAR SLEEPOVER SPECIAL</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月05日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【終電逃しから始まる部屋着の誘惑】FANZA「同僚・後輩女子宅へのお泊まり＆無防備部屋着」おすすめ神作ランキングTOP5！ノーブラすっぴんの隙だらけボディに理性が狂う一夜限りの生中出しAV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    会社の飲み会や残業帰り、ふと時計を見れば無情にも過ぎ去った終電の時刻。「始発まで時間あるし、ウチで飲み直しませんか？」――普段はオフィスでビシッとスーツを着こなしている職場の同僚や後輩女子からの一言で、男の心臓は激しく跳ね上がります。彼女のワンルームに足を踏み入れた瞬間、そこには昼間の張り詰めた空気など微塵もありません。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    メイクを落としたあどけないすっぴんの素顔、ゆったりとしたTシャツやショートパンツの部屋着。屈むたびにチラリと覗くノーブラの谷間や乳首の突起、足を組み替えるたびに露わになる柔らかな生足。彼女自身は何気ないつもりでも、密室の中で漂う無防備な生活臭と色香は、男の理性を限界まで焼き切ります。「ゴムなくなっちゃった…生でもいいよ」という囁きが耳に届いたとき、もはや止まる術はありません。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、楓カレンのノーパンノーブラ部屋着に狂わされる絶倫ハメから、日向由奈のゴム切れ生ハメ、彩月七緒の巨乳後輩胸チラ誘惑、松岡美桜の乳首ポッチ部屋着、そして山田鈴奈の豪雨雨宿り密着まで、リアルな臨場感と実用度で圧倒的人気を誇る【終電部屋着神作TOP5】を徹底特集します。
  </p>
</div>

<!-- 選び方の基準 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-purple-400">🛋️</span> 部屋着・お泊まりモノで極上の興奮を味わう3大チェックポイント
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-purple-300 mb-2">① スーツからのギャップ！すっぴん＆ノーブラ</h4>
      <p class="text-slate-300 leading-relaxed">昼間のしっかりしたOL姿と、夜の部屋着での気の抜けた無防備さ。薄手の生地越しに浮かぶ乳首や下着のラインが、男の征服欲を激しく刺激します。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-purple-300 mb-2">② 宅飲みでの酔いと近すぎる距離感</h4>
      <p class="text-slate-300 leading-relaxed">缶ビール片手に床に座り込み、肩が触れ合うほどの至近距離で始まる会話。ほろ酔いでとろんとした視線で見つめられるシチュエーションがリアリティ満点です。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-purple-300 mb-2">③ なし崩しの生ハメと朝までの連射</h4>
      <p class="text-slate-300 leading-relaxed">「帰れないんだから朝まで一緒にいよ？」と身体を預けてこられ、避妊具が切れても止まらない濃厚中出しピストンこそが最高の抜きどころです。</p>
    </div>
  </div>
</div>"""
    html_parts.append(intro_html)

    reviews_data = {
        "ipx00515": {
            "desc": """<h4>【作品解説・見どころ】楓カレンの伝説的傑作！恋人が待っているのに終電逃しでノーパンノーブラ部屋着に溺れる夜</h4>
<p>スレンダー美女の頂点に君臨した楓カレンが、美人すぎる同僚女子社員を演じるFANZA屈指のメガヒット作。「終電ないなら、ウチで飲みませんか？」という甘い誘いに乗り、彼女の自宅へ。ドアを開けた彼女は、なんと下着を着けないノーパン・ノーブラのゆったりした部屋着姿。屈むたびに揺れる胸の谷間と、スリットから覗く滑らかな太ももに、家に彼女がいるはずの主人公の理性は一瞬で崩壊します。</p>
<h4>【実用ポイント】美しすぎる裸体と一晩中ヤリまくる濃密交尾</h4>
<p>酒の勢いで抱き寄せた瞬間、楓カレンも熱い吐息を漏らして男の首に腕を巻きつけます。ベッドに押し倒して部屋着を捲り上げ、濡れそぼった秘部に直挿入。透き通るような白い肌が汗で輝き、何度も痙攣しながらイキ狂う楓カレンの姿はまさに芸術的なエロスです。一晩中休むことなく抜き差しを繰り返す絶倫プレイは、実用度120％の殿堂入りクオリティです。</p>""",
            "rating": "★★★★★ 5.0 / 5.0",
            "service_score": "背徳ギャップ度: 100% | スレンダー美貌: 100% | 実用性: 100%"
        },
        "cawd00863": {
            "desc": """<h4>【作品解説・見どころ】日向由奈の生々しいリアル感！「ゴムなくなっちゃった…生でもいいよ」のキラーワード</h4>
<p>清楚で愛らしいルックスの日向由奈が、残業帰りに終電を逃した後輩女子社員を熱演。部屋に着いてリラックスした彼女は、ゆったりしたスウェットに短い短パンという究極の部屋着スタイル。フローリングに座って缶チューハイを飲む横顔、ふと目が合った瞬間の照れ笑いが圧倒的なリアリティを醸し出します。初めは恐る恐る始まったキスが、徐々に激しさを増していき…。</p>
<h4>【実用ポイント】生中出しの快感に溺れ、妻ともしたことない濃厚ピストンへ</h4>
<p>用意していたゴムを使い果たした深夜、「ゴムなくなっちゃった…でも、生でもいいよ」と耳元で囁かれる破壊力は筆舌に尽くしがたいものがあります。直に触れ合う膣内の温もりと吸い付きに男の腰は本能のまま加速。日向由奈が喘ぎ声を必死に押し殺しながらイク姿に、鑑賞者も一瞬で限界射精へと誘われます。</p>""",
            "rating": "★★★★★ 4.9 / 5.0",
            "service_score": "リアル生ハメ度: 100% | 部屋着生足度: 99% | 実用性: 99%"
        },
        "pppe00435": {
            "desc": """<h4>【作品解説・見どころ】彩月七緒のむっちり巨乳！「うちに泊まっていきます？」小悪魔後輩の胸チラ誘惑</h4>
<p>圧倒的な肉感と張りのある美巨乳を誇る彩月七緒が、会社の飲み会で終電を逃した先輩を部屋に招く極上シチュエーション。普段のオフィスカジュアルでは隠しきれなかった豊満なバストが、ゆったりした部屋着の胸元から惜しげもなくこぼれ落ちます。お酒を注いでくれるたびに目の前に迫る巨乳の谷間に、男のペニスはフル勃起を禁じ得ません。</p>
<h4>【実用ポイント】たわわに実った爆乳パイズリと押し倒され騎乗位</h4>
<p>理性を失って胸を揉みしだくと、彩月七緒は「先輩、ずっと私の胸見てましたよね？」と妖しく微笑み、肉棒を豊満なバストで挟み込む極上パイズリを開始。さらに自分から跨がって奥深くまで肉棒を沈め、豊満な肉体を揺らしながら連続でイキ狂う姿は、巨乳好き・後輩フェチにとってこれ以上ないご馳走です。</p>""",
            "rating": "★★★★★ 4.9 / 5.0",
            "service_score": "巨乳弾力度: 100% | 小悪魔挑発度: 98% | 実用性: 99%"
        },
        "cawd00963": {
            "desc": """<h4>【作品解説・見どころ】松岡美桜の無防備すぎる乳首ポッチ！理性が焼き切れるお泊まりの夜</h4>
<p>透明感あふれるルックスと端正な顔立ちの松岡美桜が、終電逃しで後輩女子社員の自宅へ泊まる名作。シャワーを浴びて出てきた彼女が身に纏っていたのは、薄手のTシャツ1枚。ノーブラのため、くっきりと浮き出た乳首の突起が目の前に迫ります。「先輩、お酒まだ飲みますか？」と屈託なく微笑む無警戒さに、男の野生が一気に解き放たれます。</p>
<h4>【実用ポイント】「生でもいいですよ」から始まる明け方までの追撃中出し</h4>
<p>我慢できずに抱きしめてキスを奪うと、松岡美桜も熱い吐息を吐きながら身を委ねてきます。ゴムを使い切った後も「生でもいいですよ…先輩の全部欲しいです」と懇願され、膣奥深くに熱い精液をドクドクと注ぎ込むカタルシス。朝の光がカーテンの隙間から差し込むまでハメ狂う多幸感は格別です。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "乳首ポッチ度: 100% | 追撃中出し度: 98% | 実用性: 98%"
        },
        "ipzz00857": {
            "desc": """<h4>【作品解説・見どころ】山田鈴奈の小動物系ピュア美少女！突然の豪雨で雨宿りお泊まり</h4>
<p>守ってあげたくなるような愛らしさを持つ山田鈴奈が、ゲリラ豪雨で立ち往生した先輩を自宅へ招き入れる胸キュン＆激エロ作品。ずぶ濡れになった服を着替え、大きめのシャツをワンピースのように着こなす彼女の姿は破壊的な可愛さです。温かいお茶を飲みながら縮まっていく二人の距離、少し触れ合った指先の温もりに、互いの心臓の鼓動が部屋中に響き渡ります。</p>
<h4>【実用ポイント】彼女持ちの罪悪感を吹き飛ばす極上フェラと生ハメ</h4>
<p>彼女持ちという立場でありながら、山田鈴奈のウルウルとした瞳で見つめられ、小さく柔らかい手で股間をまさぐられた瞬間、すべての道徳心が吹き飛びます。ベッドの上で華奢な身体を抱き上げ、奥深くまで突き刺すたびに切ない声で喘ぐ姿は、男の保護欲と性欲を限界まで満たしてくれます。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "美少女小動物度: 100% | 雨宿り密室度: 98% | 実用性: 98%"
        }
    }

    for idx, it in enumerate(items):
        cid = it.get("content_id")
        title = it.get("title")
        aff_url = it.get("affiliate_url_clean")
        large_img = it.get("imageURL", {}).get("large", "")
        acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        act_html = " ".join([get_actress_link(a) for a in acts])
        genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        genre_html = " ".join([get_genre_link(g) for g in genres[:6]])
        sample_imgs = get_sample_images(it, 4)
        c_data = reviews_data.get(cid, {})

        sample_imgs_html = ""
        if sample_imgs:
            img_tags = "".join([f'<img src="{sim}" alt="{title} サンプル{s_idx+1}" class="w-full h-28 object-cover rounded-lg border border-slate-700/80 hover:scale-105 transition transform duration-300" loading="lazy" />' for s_idx, sim in enumerate(sample_imgs)])
            sample_imgs_html = f'<div class="grid grid-cols-2 md:grid-cols-4 gap-2 my-4">{img_tags}</div>'

        item_block = f"""
<div class="my-10 bg-slate-900/90 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-2xl relative">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-2">
      <span class="bg-purple-600 text-white font-black text-sm px-3 py-1 rounded-lg">第{idx+1}位</span>
      <span class="text-xs text-slate-400 font-mono tracking-wider">品番: {cid.upper()}</span>
    </div>
    <div class="text-amber-400 font-black text-sm tracking-wide">{c_data.get('rating', '★★★★★ 5.0 / 5.0')}</div>
  </div>

  <h3 class="text-xl md:text-2xl font-black text-white leading-snug mb-4 hover:text-purple-400 transition">
    <a href="{aff_url}" target="_blank" rel="nofollow noopener">{title}</a>
  </h3>

  <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-start">
    <div class="md:col-span-5">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block group overflow-hidden rounded-xl border border-slate-700/80 shadow-lg relative">
        <img src="{large_img}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition duration-300 flex items-end p-4">
          <span class="bg-purple-600 text-white font-bold text-xs px-3 py-1.5 rounded-full shadow-lg">FANZA公式で今すぐ無料サンプル再生 ▶</span>
        </div>
      </a>
      <div class="mt-3 text-xs bg-slate-800/60 p-2.5 rounded-lg border border-slate-700/50 text-slate-300">
        <div class="mb-1"><span class="text-slate-400">主演女優:</span> {act_html}</div>
        <div><span class="text-slate-400">スペック評価:</span> <span class="text-purple-300 font-medium">{c_data.get('service_score', '実用性 100%')}</span></div>
      </div>
    </div>

    <div class="md:col-span-7 space-y-4 text-slate-300 text-sm md:text-base leading-relaxed">
      {c_data.get('desc', '')}
      
      <div class="pt-2">
        <div class="text-xs text-slate-400 mb-2 font-medium">関連ジャンルタグ:</div>
        <div class="flex flex-wrap gap-1.5">{genre_html}</div>
      </div>
    </div>
  </div>

  {sample_imgs_html}

  <div class="mt-6 flex flex-col sm:flex-row items-center justify-between gap-4 bg-slate-950/80 p-4 rounded-xl border border-slate-800">
    <div class="text-xs text-slate-400">
      高画質ストリーミング／ダウンロード対応・スマホ即時視聴可能
    </div>
    <div class="flex items-center gap-3 w-full sm:w-auto">
      <a href="/posts/{cid}" class="text-center px-4 py-2.5 rounded-xl border border-slate-700 text-slate-300 hover:text-white hover:bg-slate-800 text-xs font-bold transition w-1/2 sm:w-auto">
        詳細個別レビューを見る
      </a>
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="text-center bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500 text-white text-sm font-black px-6 py-2.5 rounded-xl shadow-lg shadow-purple-900/40 hover:shadow-purple-800/60 transition transform hover:-translate-y-0.5 w-1/2 sm:w-auto">
        FANZA公式で今すぐ本編を見る ▶
      </a>
    </div>
  </div>
</div>"""
        html_parts.append(item_block)

    faq_html = """<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl">
  <h3 class="text-xl md:text-2xl font-black text-white mb-6 flex items-center gap-2">
    <span class="text-purple-400">❓</span> 終電逃し・部屋着AVに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-6 text-sm md:text-base">
    <div class="border-b border-slate-800 pb-4">
      <h4 class="font-bold text-purple-300 mb-2">Q1. 部屋着・お泊まりモノの何がそんなに興奮するのですか？</h4>
      <p class="text-slate-300 leading-relaxed">普段は会社で見せる「よそ行きの顔」から、密室で見せる「無防備なプライベートの素顔」への劇的なギャップです。ノーブラの胸元や生足の生活感、アルコールが入って距離感がバグった瞬間の生々しさは、男の妄想を極限まで掻き立てます。</p>
    </div>
    <div class="border-b border-slate-800 pb-4">
      <h4 class="font-bold text-purple-300 mb-2">Q2. 一番抜きやすい作品はどれですか？</h4>
      <p class="text-slate-300 leading-relaxed">スレンダー美女の極致と圧倒的な背徳感なら第1位の楓カレンが絶対峰です。また、「生でもいいよ」という甘い囁きとリアルな生活感に溺れたいなら第2位の日向由奈や第4位の松岡美桜が激推しです。</p>
    </div>
    <div>
      <h4 class="font-bold text-purple-300 mb-2">Q3. 購入後の安全性やプライバシーは大丈夫ですか？</h4>
      <p class="text-slate-300 leading-relaxed">FANZA公式の購入履歴やクレジットカード明細には作品名が一切記載されず、厳重にプライバシーが保護されます。スマホブラウザですぐに視聴できるため家族や知人にバレる心配もありません。</p>
    </div>
  </div>
</div>"""
    html_parts.append(faq_html)

    related_links_html = """<div class="my-8 bg-slate-950 border border-slate-800 rounded-2xl p-6">
  <h4 class="text-base font-bold text-white mb-3">🔥 あわせて読みたい人気キラー特集</h4>
  <ul class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm text-purple-300">
    <li><a href="/posts/feature_fanza_female_boss_office_overtime_hotel_ranking_2026" class="hover:underline">▶ 美人女上司・残業密室＆出張相部屋ランキングTOP5！オフィスで豹変</a></li>
    <li><a href="/posts/feature_fanza_cabin_attendant_flight_hotel_ranking_2026" class="hover:underline">▶ 美人CA・客室乗務員ランキングTOP5！フライト先ホテルの禁断ステイ</a></li>
    <li><a href="/posts/feature_fanza_nurse_hospital_secret_care_ranking_2026" class="hover:underline">▶ 美人ナース・看護師ランキングTOP5！夜勤病室の献身ケアと密会</a></li>
    <li><a href="/posts/feature_fanza_subjective_pov_whispering_masturbation_support_ranking_2026" class="hover:underline">▶ 完全主観オナサポランキングTOP5！ゼロ距離囁き淫語と射精管理</a></li>
  </ul>
</div>"""
    html_parts.append(related_links_html)

    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "ItemList",
                "name": "終電逃し・部屋着おすすめ神作ランキングTOP5",
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
                        "name": "部屋着・お泊まりモノの何がそんなに興奮するのですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "職場のよそ行きの顔からプライベートの無防備な素顔へのギャップです。ノーブラ部屋着と宅飲みの距離感が最高のリアリティを生み出します。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "一番抜きやすい作品はどれですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "スレンダー美貌と背徳感なら第1位の楓カレン、「生でもいいよ」のリアル感なら第2位の日向由奈が圧倒的におすすめです。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "購入後の安全性やプライバシーは大丈夫ですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "FANZA公式の購入履歴やカード明細に作品名は記載されず、厳重にプライバシー保護された状態で安全に視聴可能です。"
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
        "id": "feature_fanza_missed_last_train_roomwear_sleepover_ranking_2026",
        "title": "【終電逃しから始まる部屋着の誘惑】FANZA「同僚・後輩女子宅へのお泊まり＆無防備部屋着」おすすめ神作ランキングTOP5！ノーブラすっぴんの隙だらけボディに理性が狂う一夜限りの生中出しAV選【2026年最新】",
        "date": "2026-10-05 01:10:00",
        "hinban": "MISSED-LAST-TRAIN-ROOMWEAR-2026",
        "price": "300~",
        "maker": "FANZA公式セレクション",
        "actresses": ["楓カレン", "日向由奈", "彩月七緒", "松岡美桜", "山田鈴奈"],
        "genres": ["部屋着", "終電逃し", "お泊まり", "同僚", "後輩", "ノーブラ", "すっぴん", "生中出し", "特集", "殿堂入り"],
        "image": cover_image,
        "review": full_html
    }

    file_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f" -> Successfully saved Article 2 ({char_count} chars) to {file_path}")


# ==============================================================================
# 記事3: 凄テク我慢・耐えたらご褒美生中出し特化
# ==============================================================================
def generate_article_super_technique():
    print("=== Generating Article 3: 凄テク我慢できれば生中出しSEX特化 ===")
    cids = ["waaa00336", "waaa00143", "waaa00689", "waaa00061", "wanz00970"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["凄テク", "我慢", "ご褒美", "生中出し", "射精管理", "フェラ"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 3 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-rose-950/40 via-slate-900 to-slate-950 border border-rose-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-rose-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-rose-500/20 text-rose-300 border border-rose-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">SUPER TECHNIQUE ENDURANCE SPECIAL</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月05日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【男の限界を試す極上テクニック】FANZA「凄テク我慢できれば生中出しSEX」おすすめ神作ランキングTOP5！名器と神技フェラに耐え抜いてご褒美膣内射精を勝ち取る実用度MAX・AV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    「私のテクニックに最後まで我慢できたら、生で中出ししていいよ？」――男の挑戦欲とドM心、そしてあくなき射精欲望を同時に直撃するプレステージ屈指の超人気看板シリーズ「凄テクを我慢できれば生★中出しSEX！」。目の前には国宝級の美貌と豊満な肢体を誇るトップ単体女優たち。彼女たちが惜しみなく繰り出す超絶テクニックの猛攻に耐え抜いた者だけが、極上名器への生ハメ中出しという最高のご褒美を味わうことができます。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    このジャンルが他のAVと一線を画すのは、「圧倒的な射精管理の緊張感」と「制限時間との戦い」にあります。耳元で囁かれる甘い淫語、真空バキュームで亀頭を締め上げるディープスロート、肉厚なバストで包み込むパイズリ、そして男の弱点を的確にえぐる腰振りグラインド。「もう出ちゃうの？」「もっと我慢して…♡」と挑発され、歯を食いしばりながら耐え忍ぶ男の悶絶ぶりは、鑑賞しているこちらの股間まで痛いほどのギンギン状態に追い込みます。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、ゴージャス美女・橘メアリーの規格外バキュームから、北野未奈の濃厚フェロモン搾精、天宮花南の小悪魔猛攻、三原ほのかの肉厚パイズリ地獄、そして根尾あかりの高速グラインドまで、オナニーの実用性と快楽度が極限まで突き詰められた【凄テク我慢神作TOP5】を徹底解説します。
  </p>
</div>

<!-- 選び方の基準 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-rose-400">⚡</span> 凄テク我慢シリーズで昇天するための3大チェックポイント
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-rose-300 mb-2">① 女優ごとの得意技（口淫・パイズリ・騎乗位）</h4>
      <p class="text-slate-300 leading-relaxed">ただ弄ぶだけでなく、舌先の細かな痙攣、喉奥までの飲み込み、胸の弾力を活かした挟み込みなど、女優ごとに極められた神技のバリエーションが抜きどころです。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-rose-300 mb-2">② ドSな視線と耳元囁きの言葉責め</h4>
      <p class="text-slate-300 leading-relaxed">「ピクピクしてるよ？我慢できないの？」「ここで出しちゃったら中出しできないよ？」と見下ろしながら煽ってくるサドっ気たっぷりの淫語が男の脳をトロけさせます。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-rose-300 mb-2">③ 耐え抜いた末の「生中出しご褒美」の解放感</h4>
      <p class="text-slate-300 leading-relaxed">限界まで焦らされ、膨張しきったペニスで熱い膣内へ生挿入する瞬間の快感は異次元。子宮口目掛けてドクドクと白濁液を注ぎ込むカタルシスが約束されます。</p>
    </div>
  </div>
</div>"""
    html_parts.append(intro_html)

    reviews_data = {
        "waaa00336": {
            "desc": """<h4>【作品解説・見どころ】橘メアリーの圧倒的オーラ！規格外ボディと凄テク口淫で男を虐殺する極上作</h4>
<p>日本人離れしたグラマラスな国宝級プロポーションを誇る橘メアリーが、ドM男たちを容赦のない凄テクで追い詰めるシリーズ屈指の名作。妖艶な笑みを浮かべながら現れた彼女は、豊満な胸元を惜しげもなくさらし、男の股間を指先でなぞるだけでフル勃起へと導きます。最初のステージから繰り出されるディープスロートは圧巻。喉奥深くまで亀頭を吸い込み、強烈なバキューム圧で締め上げてくる口淫に、男たちは開始数十秒で悶絶の表情を浮かべます。</p>
<h4>【実用ポイント】極上名器への生挿入と理性を吹き飛ばすド迫力ピストン</h4>
<p>我慢の限界を耐え抜いた挑戦者に与えられるのは、橘メアリーの濡れそぼった極上膣への生中出し。挿入された瞬間、橘メアリー自身も艶やかな喘ぎ声を漏らし、極上の肉圧で男のペニスをぎゅっと包み込みます。腰を激しく打ち付け合い、膣奥深くに大量の精子を注ぎ込むクライマックスは、見ているこちらの射精欲を限界まで昂らせてくれます。</p>""",
            "rating": "★★★★★ 5.0 / 5.0",
            "service_score": "神技バキューム度: 100% | 肉感ゴージャス度: 100% | 実用性: 100%"
        },
        "waaa00143": {
            "desc": """<h4>【作品解説・見どころ】北野未奈の濃厚フェロモン！男を骨抜きにする指先と舌技の魔術</h4>
<p>大人の色気と妖艶なフェロモンで絶大な人気を誇る北野未奈が登場。ゆったりとした所作の一つ一つから漂うエロスが男の理性を蝕みます。彼女の凄テクは、ただ力任せに責めるのではなく、男の性感帯を熟知した繊細かつ大胆な愛撫。亀頭の裏筋を舐め回しながら玉袋を優しく揉みしだき、耳元に「もうビクビクしてる…可愛いね」と囁きかけてくる焦らしテクニックは悶絶必至です。</p>
<h4>【実用ポイント】ご褒美の濃厚密着ピストンで子宮口を穿つ生ハメ</h4>
<p>見事耐え抜いた男を優しく抱きしめ、「よく我慢できたね、ご褒美あげる…♡」と笑顔で迎え入れる母性と淫乱さのギャップが最高です。正常位で密着しながら奥深くまで突き入れると、北野未奈の締まりの良い膣壁がペニス全体を吸い付くように締め付け、濃厚な生中出しへと導かれます。</p>""",
            "rating": "★★★★★ 4.9 / 5.0",
            "service_score": "フェロモン色気度: 100% | 焦らし指技度: 99% | 実用性: 99%"
        },
        "waaa00689": {
            "desc": """<h4>【作品解説・見どころ】天宮花南の小悪魔猛攻！可愛い笑顔で男のチンポを翻弄する天性の痴女技</h4>
<p>アイドル顔負けの可愛らしいルックスとスレンダーな肉体を持つ天宮花南が、小悪魔的な笑顔で男たちを次々と撃沈させていく快作。あどけない表情とは裏腹に、繰り出すテクニックは超本格派。高速の手コキとぬめり気たっぷりのローションフェラを巧みに組み合わせ、男がイキそうになると「ダメ〜まだ出しちゃダメだよ！」と寸止めして焦らすドSっぷりがたまりません。</p>
<h4>【実用ポイント】激しい腰振りと喘ぎ声で搾り取られる連続中出し</h4>
<p>耐え切った男に跨がり、自ら腰を上下させて奥まで飲み込む騎乗位は圧巻。天宮花南の愛らしい顔が快感で紅潮し、激しいピストンに合わせて小さな胸が揺れる姿は男の本能を狂わせます。最後は子宮奥深くに精液を全て受け止め、満足そうに微笑む姿に心まで奪われます。</p>""",
            "rating": "★★★★★ 4.9 / 5.0",
            "service_score": "小悪魔ドS度: 100% | 寸止め焦らし度: 98% | 実用性: 99%"
        },
        "waaa00061": {
            "desc": """<h4>【作品解説・見どころ】三原ほのかの肉厚パイズリ！豊かな胸で包み込まれる密着快楽地獄</h4>
<p>マシュマロのような豊満バストと柔らかな肢体を持つ三原ほのかが、自慢の胸をフル活用した凄テクで男を骨抜きにする傑作。オイルをたっぷりと塗りたくった巨乳の谷間にペニスを挟み込み、左右から圧迫しながらリズミカルにしごき上げるパイズリは、男なら誰もが即射精の危機に直面する極上の快感です。上目遣いで「私の胸、気持ちいい？」と問いかけてくる姿がエロすぎます。</p>
<h4>【実用ポイント】柔らかな肉体に包まれて果てる至福の生中出し</h4>
<p>パイズリとフェラの波状攻撃に耐え抜いた後は、クッションのように柔らかい三原ほのかの肉体に飛び込む生ハメタイム。バックで突き入れると、豊かなお尻と太ももが激しく波打ち、奥まで届くたびに熱い吐息を漏らす三原ほのか。溜まりに溜まった精子を一滴残らず吸い取られるような極上射精を味わえます。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "巨乳パイズリ度: 100% | 柔らか肉感度: 99% | 実用性: 98%"
        },
        "wanz00970": {
            "desc": """<h4>【作品解説・見どころ】根尾あかりの高速グラインド！スレンダー美脚美女が魅せる神業騎乗位</h4>
<p>抜群のプロポーションと洗練された美貌を誇る根尾あかりが、男の限界を試す過酷な凄テクチャレンジ。彼女の最大の武器は、柔軟な股関節から繰り出される変幻自在の腰使い。男の上に跨がり、前後に円を描くようにグラインドさせながら膣口とカリ首を擦り合わせるテクニックは、どんな絶倫男でも秒速でギブアップしたくなるほどの破壊力を誇ります。</p>
<h4>【実用ポイント】勝利の生中出し！締まり抜群の名器が男を締め上げる</h4>
<p>規定時間を耐え抜いて手に入れた生中出しの権利を行使し、正常位で奥深くまで一気にペニスを沈めると、根尾あかりの名器がキュッと収縮して男を歓迎。乱れ髪を振り乱しながら絶頂へと駆け上がる根尾あかりと一体になり、ドクドクと中出しを決める瞬間は最高の征服感に包まれます。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "腰使いグラインド度: 100% | 美脚スレンダー度: 98% | 実用性: 98%"
        }
    }

    for idx, it in enumerate(items):
        cid = it.get("content_id")
        title = it.get("title")
        aff_url = it.get("affiliate_url_clean")
        large_img = it.get("imageURL", {}).get("large", "")
        acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        act_html = " ".join([get_actress_link(a) for a in acts])
        genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        genre_html = " ".join([get_genre_link(g) for g in genres[:6]])
        sample_imgs = get_sample_images(it, 4)
        c_data = reviews_data.get(cid, {})

        sample_imgs_html = ""
        if sample_imgs:
            img_tags = "".join([f'<img src="{sim}" alt="{title} サンプル{s_idx+1}" class="w-full h-28 object-cover rounded-lg border border-slate-700/80 hover:scale-105 transition transform duration-300" loading="lazy" />' for s_idx, sim in enumerate(sample_imgs)])
            sample_imgs_html = f'<div class="grid grid-cols-2 md:grid-cols-4 gap-2 my-4">{img_tags}</div>'

        item_block = f"""
<div class="my-10 bg-slate-900/90 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-2xl relative">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-2">
      <span class="bg-rose-600 text-white font-black text-sm px-3 py-1 rounded-lg">第{idx+1}位</span>
      <span class="text-xs text-slate-400 font-mono tracking-wider">品番: {cid.upper()}</span>
    </div>
    <div class="text-amber-400 font-black text-sm tracking-wide">{c_data.get('rating', '★★★★★ 5.0 / 5.0')}</div>
  </div>

  <h3 class="text-xl md:text-2xl font-black text-white leading-snug mb-4 hover:text-rose-400 transition">
    <a href="{aff_url}" target="_blank" rel="nofollow noopener">{title}</a>
  </h3>

  <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-start">
    <div class="md:col-span-5">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block group overflow-hidden rounded-xl border border-slate-700/80 shadow-lg relative">
        <img src="{large_img}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition duration-300 flex items-end p-4">
          <span class="bg-rose-600 text-white font-bold text-xs px-3 py-1.5 rounded-full shadow-lg">FANZA公式で今すぐ無料サンプル再生 ▶</span>
        </div>
      </a>
      <div class="mt-3 text-xs bg-slate-800/60 p-2.5 rounded-lg border border-slate-700/50 text-slate-300">
        <div class="mb-1"><span class="text-slate-400">主演女優:</span> {act_html}</div>
        <div><span class="text-slate-400">スペック評価:</span> <span class="text-rose-300 font-medium">{c_data.get('service_score', '実用性 100%')}</span></div>
      </div>
    </div>

    <div class="md:col-span-7 space-y-4 text-slate-300 text-sm md:text-base leading-relaxed">
      {c_data.get('desc', '')}
      
      <div class="pt-2">
        <div class="text-xs text-slate-400 mb-2 font-medium">関連ジャンルタグ:</div>
        <div class="flex flex-wrap gap-1.5">{genre_html}</div>
      </div>
    </div>
  </div>

  {sample_imgs_html}

  <div class="mt-6 flex flex-col sm:flex-row items-center justify-between gap-4 bg-slate-950/80 p-4 rounded-xl border border-slate-800">
    <div class="text-xs text-slate-400">
      高画質ストリーミング／ダウンロード対応・スマホ即時視聴可能
    </div>
    <div class="flex items-center gap-3 w-full sm:w-auto">
      <a href="/posts/{cid}" class="text-center px-4 py-2.5 rounded-xl border border-slate-700 text-slate-300 hover:text-white hover:bg-slate-800 text-xs font-bold transition w-1/2 sm:w-auto">
        詳細個別レビューを見る
      </a>
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="text-center bg-gradient-to-r from-rose-600 to-red-600 hover:from-rose-500 hover:to-red-500 text-white text-sm font-black px-6 py-2.5 rounded-xl shadow-lg shadow-rose-900/40 hover:shadow-rose-800/60 transition transform hover:-translate-y-0.5 w-1/2 sm:w-auto">
        FANZA公式で今すぐ本編を見る ▶
      </a>
    </div>
  </div>
</div>"""
        html_parts.append(item_block)

    faq_html = """<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl">
  <h3 class="text-xl md:text-2xl font-black text-white mb-6 flex items-center gap-2">
    <span class="text-rose-400">❓</span> 凄テク我慢シリーズに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-6 text-sm md:text-base">
    <div class="border-b border-slate-800 pb-4">
      <h4 class="font-bold text-rose-300 mb-2">Q1. 凄テク我慢シリーズがこんなに人気なのはなぜですか？</h4>
      <p class="text-slate-300 leading-relaxed">「耐え抜いたら生中出しできる」という明確なゲーム性と、美女による容赦なき寸止め・焦らしプレイの相乗効果です。見ている側も「自分なら何秒耐えられるか」と感情移入しやすく、抜きやすさ（実用度）が圧倒的に高いことが理由です。</p>
    </div>
    <div class="border-b border-slate-800 pb-4">
      <h4 class="font-bold text-rose-300 mb-2">Q2. 一番ハードで射精を我慢できない作品はどれですか？</h4>
      <p class="text-slate-300 leading-relaxed">バキューム口淫の破壊力なら第1位の橘メアリーが別格です。テクニカルな焦らしとフェロモンなら第2位の北野未奈、巨乳パイズリの包容力なら第4位の三原ほのかが絶対に外せません。</p>
    </div>
    <div>
      <h4 class="font-bold text-rose-300 mb-2">Q3. 初めてでも楽しめますか？</h4>
      <p class="text-slate-300 leading-relaxed">はい、ルールがシンプルかつ明快で、どの作品から見ても最初から最後までクライマックスのような濃密な実用性を堪能できます。FANZA公式で無料サンプル動画も視聴可能です。</p>
    </div>
  </div>
</div>"""
    html_parts.append(faq_html)

    related_links_html = """<div class="my-8 bg-slate-950 border border-slate-800 rounded-2xl p-6">
  <h4 class="text-base font-bold text-white mb-3">🔥 あわせて読みたい人気キラー特集</h4>
  <ul class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm text-rose-300">
    <li><a href="/posts/feature_fanza_vacuum_blowjob_deep_throat_ranking" class="hover:underline">▶ 凄腕バキュームフェラ・喉奥ディープスロートランキングTOP5！即イキ必至</a></li>
    <li><a href="/posts/feature_fanza_mens_esthe_secret_massage_ranking" class="hover:underline">▶ メンズエステ・裏オプ回春マッサージランキングTOP5！密着施術で理性崩壊</a></li>
    <li><a href="/posts/feature_fanza_luxury_soapland_foam_mat_play_ranking_2026" class="hover:underline">▶ 高級ソープ・泡踊りマットプレイ本番中出しランキングTOP5！泡まみれの極上天国</a></li>
    <li><a href="/posts/feature_fanza_huge_ass_back_piston_ranking_2026" class="hover:underline">▶ 超巨尻・美尻×バック後背位ピストンランキングTOP5！肉弾ヒップが激震</a></li>
  </ul>
</div>"""
    html_parts.append(related_links_html)

    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "ItemList",
                "name": "凄テク我慢できれば生中出しSEXおすすめ神作ランキングTOP5",
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
                        "name": "凄テク我慢シリーズがこんなに人気なのはなぜですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "耐え抜いたら生中出しできるという明確なご褒美と、美女による寸止め焦らしプレイの緊張感によって、実用度が極限まで高まっているためです。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "一番ハードで射精を我慢できない作品はどれですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "バキューム口淫の破壊力なら第1位の橘メアリー、大人の焦らしフェロモンなら第2位の北野未奈が別格です。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "初めてでも楽しめますか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "はい、ルールが明快でテンポ良く最高峰の射精シーンが続くため、どの作品からでも存分に楽しめます。"
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
        "id": "feature_fanza_endure_super_technique_raw_creampie_ranking_2026",
        "title": "【男の限界を試す極上テクニック】FANZA「凄テク我慢できれば生中出しSEX」おすすめ神作ランキングTOP5！名器と神技フェラに耐え抜いてご褒美膣内射精を勝ち取る実用度MAX・AV選【2026年最新】",
        "date": "2026-10-05 01:20:00",
        "hinban": "SUPER-TECHNIQUE-ENDURANCE-2026",
        "price": "300~",
        "maker": "FANZA公式セレクション",
        "actresses": ["橘メアリー", "北野未奈", "天宮花南", "三原ほのか", "根尾あかり"],
        "genres": ["凄テク", "我慢", "ご褒美", "生中出し", "射精管理", "フェラ", "パイズリ", "騎乗位", "特集", "殿堂入り"],
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
    generate_article_childhood_friend()
    print("--------------------------------------------------")
    generate_article_roomwear()
    print("--------------------------------------------------")
    generate_article_super_technique()
    print("==================================================")
    print("3記事すべての生成が正常に完了しました！")
    print("==================================================")

if __name__ == "__main__":
    main()
