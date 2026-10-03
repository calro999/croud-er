# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・超大型キラー特集3記事自動生成スクリプト（完全独立書き下ろし・2026最新版）
1. 【美人女上司・オフィス残業密室＆出張相部屋の下剋上特化】
   『【オフィスで豹変するキャリア美女】FANZA「美人女上司・残業密室＆出張相部屋」おすすめ神作ランキングTOP5！普段は冷徹な高嶺の花が部下の絶倫ピストンに理性を溶かされ朝まで喘ぎ狂う下剋上AV選【2026年最新】』
2. 【同窓会再会・人妻クラスメイトとの泥酔W不倫特化】
   『【十数年ぶりの再会と初恋の情火】FANZA「同窓会再会・人妻クラスメイトとの泥酔W不倫」おすすめ神作ランキングTOP5！昔憧れだった清楚なマドンナがラブホテルで理性崩壊・朝まで中出しを貪り合う背徳AV選【2026年最新】』
3. 【隣の若妻・留守中のベランダ密会＆玄関先不倫特化】
   『【壁一枚隔てた背徳の温もり】FANZA「隣の若妻・留守中のベランダ密会＆玄関先不倫」おすすめ神作ランキングTOP5！清楚なエプロン姿から欲求不満を爆発させて男を貪る濃厚中出しAV選【2026年最新】』
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
        
    act_str = "・".join(acts) if acts else "トップ女優"
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
# 記事1: 美人女上司・オフィス残業密室＆出張相部屋の下剋上特化
# ==============================================================================
def generate_article_female_boss():
    print("=== Generating Article 1: 美人女上司・残業＆出張相部屋特化 ===")
    cids = ["1stars00892", "1fns00205", "miab00474", "pred00321", "smok00021"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["女上司", "キャリアウーマン", "オフィス", "下剋上"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 1 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-indigo-950/40 via-slate-900 to-slate-950 border border-indigo-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-indigo-500/20 text-indigo-300 border border-indigo-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">OFFICE FEMALE BOSS SPECIAL</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月04日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【オフィスで豹変するキャリア美女】FANZA「美人女上司・残業密室＆出張相部屋」おすすめ神作ランキングTOP5！普段は冷徹な高嶺の花が部下の絶倫ピストンに理性を溶かされ朝まで喘ぎ狂う下剋上AV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    働く男たちにとって永遠のロマンであり、FANZAでも屈指の人気と購買率を誇り続けるメガヒットジャンル、それが「美人女上司シチュエーション」です。昼間のオフィスでは隙のないタイトスーツとパンスト美脚に身を包み、鋭い眼差しで部下をテキパキと指導するクールなキャリアウーマン。手が届かない高嶺の花として君臨する彼女たちが、深夜残業の密室やトラブルによる出張先のホテル相部屋という逃げ場のない空間で、ふとしたきっかけから雌の顔を覗かせる瞬間の興奮は言葉を絶します。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    このジャンル最大の抜きどころは、上下関係が完全に逆転する「下剋上のカタルシス」と、理性の防壁が崩壊していく過程の生々しさにあります。最初は「私たちは上司と部下なのよ」「こんなこと許されるわけないでしょ」と毅然と拒絶していた美女が、部下の力強い抱擁と止まらない激ピストンによって徐々にトロ顔へと変わり、最後には「もう許して…もっと突いてぇ！」と泣き叫びながら腰を激しく振る姿は、男の本能を極限まで刺激します。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、大人気女優・星乃莉子の出張相部屋神作から、つばさ舞の痛快モラハラ逆転作、黒川すみれの美脚パンスト痴女責め、希島あいりの愛人部長出張録、辻井ほのかの濃厚残業ベロキス作まで、FANZAレビュー星4.5超え・実用度満点の【美人女上司×下剋上神作TOP5】を徹底紹介します。
  </p>
</div>

<!-- 選び方の基準 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-indigo-400">💼</span> 失敗しない女上司モノ選び！最高に没入できる3大チェックポイント
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-indigo-300 mb-2">① 昼間の「厳格・冷徹」と夜の「乱れ・メス堕ち」のギャップ</h4>
      <p class="text-slate-300 leading-relaxed">普段の仕事ができるプライドの高さがしっかりと描かれているからこそ、肉欲に負けて喘ぎ声を漏らした瞬間の背徳感が何倍にも跳ね上がります。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-indigo-300 mb-2">② スーツ・パンスト・タイトスカートの着衣フェチ描写</h4>
      <p class="text-slate-300 leading-relaxed">全裸にするのではなく、パンストを破いて指を入れたり、スカートをたくし上げてバックから突く着衣プレイの生々しさが作品の完成度を決定づけます。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-indigo-300 mb-2">③ 立場逆転で懇願させる濃厚ピストンと中出し</h4>
      <p class="text-slate-300 leading-relaxed">「上司の命令」から「一人の女としての懇願」へとセリフが変化し、部下の精子を膣内深くに注ぎ込まれて白目を剥くクライマックスの迫力が鍵です。</p>
    </div>
  </div>
</div>"""
    html_parts.append(intro_html)

    reviews_data_1 = {
        "1stars00892": {
            "desc": """<h4>【作品解説・見どころ】星乃莉子が魅せる出張先相部屋の奇跡！童貞部下に狂わされるエリート美女</h4>
<p>圧倒的な透明感と美しいスタイルを誇るトップ女優・星乃莉子が、仕事熱心で部下に厳しいエリート女上司を熱演。地方出張先の手違いでダブルベッドひとつのホテルに相部屋宿泊することになってしまった夜、張り詰めた緊張感の中でドラマが動き出します。お風呂上がりの無防備なバスローブ姿、ほのかに香るアルコールとシャンプーの匂い。普段の凛としたスーツ姿からは想像もつかない艶やかな色香に、童貞部下の理性が吹き飛びます。押し倒された星乃莉子は必死に抵抗するものの、執拗な耳元への吐息と情熱的なディープキスに次第に身体が熱を帯び、自ら舌を絡め取っていく展開は鳥肌モノの完成度です。</p>
<h4>【実用ポイント】夜通し繰り返される絶倫ピストンと蕩けきったメス顔</h4>
<p>本作の真骨頂は、一度火がついた後の星乃莉子の壊れっぷり。童貞ならではの無尽蔵のスタミナで一晩中激しく突き上げられ、「もうダメ…頭おかしくなっちゃう！」と涙目で絶叫しながら幾度も潮を吹き散らします。翌朝、すっかり部下のチ○ポに屈服し、甘えた声で朝立ちペニスを咥え込むエンディングまで、実用度120%の傑作です。</p>""",
            "rating": "★★★★★ 5.0 / 5.0",
            "service_score": "立場逆転度: 100% | 着衣エロス: 99% | 実用性: 100%"
        },
        "1fns00205": {
            "desc": """<h4>【作品解説・見どころ】つばさ舞のドSモラハラが一変！雑魚マン発覚で痙攣潮吹きアクメ連発</h4>
<p>冷徹で高圧的なモラハラ女上司として部下を「使えない雑魚」と罵倒し続けるつばさ舞。しかし、残業中に反撃に出た部下にペニスをねじ込まれると、実は誰よりも感度が良すぎる超絶「雑魚マンコ」だったことが暴かれます。最初のツンツンした侮蔑の眼差しから、突かれた瞬間に「ひゃんっ！」と情けない声を上げてビクビクと体を震わせる豹変ぶりはまさに圧巻。言葉とは裏腹に愛液が洪水のように溢れ出し、責められるたびにシーツを水浸しにしていく生々しい反応がファンの心を鷲掴みにします。</p>
<h4>【実用ポイント】屈辱と快楽の狭間でイキ狂う最高の下剋上ピストン</h4>
<p>「やめなさい…私が上司よ…！」と必死に威厳を保とうとするものの、部下に弱点である子宮口をゴリゴリと抉られ、最後は「雑魚でごめんなさい！イッちゃう、またイッちゃうぅ！」と完全降伏。体全身を痙攣させながら潮を吹き尽くすつばさ舞の姿は、Sっ気のある男性なら絶対に抜ける痛快かつ超濃厚な仕上がりです。</p>""",
            "rating": "★★★★★ 4.9 / 5.0",
            "service_score": "立場逆転度: 100% | 痙攣感度: 100% | 実用性: 98%"
        },
        "miab00474": {
            "desc": """<h4>【作品解説・見どころ】黒川すみれの極上美脚パンスト！ノーパン直穿きで部下を弄ぶド痴女上司</h4>
<p>スラリと伸びた完璧な美脚の持ち主・黒川すみれが、部下の性癖を熟知した上で弄び尽くす官能オフィスドラマ。なんと彼女は、タイトスカートの下にノーパンでパンストを直穿きして出社。デスクの下で部下の足にすり寄せたり、残業中のオフィスでスカートをめくって透ける秘部を見せつけたりと、悪魔的な挑発を仕掛けてきます。上から目線で「見てるだけで勃起しちゃったの？情けない部下ね」と囁きながら、パンスト越しに肉棒をしごき上げる手技はまさに悶絶必至です。</p>
<h4>【実用ポイント】20発射精の極限管理！破いたパンストから貪り食われる結合劇</h4>
<p>我慢の限界を迎えた部下がパンストの股間部分を乱暴に引き裂き、濡れそぼった膣口に一気に挿入。すると黒川すみれは待ってましたとばかりに腰をうねらせ、部下の精子を根こそぎ搾り取る貪欲な騎乗位を披露します。20回に及ぶ連続発射管理と、パンストの摩擦音が混ざり合う濃厚な絡み合いは、脚フェチ・ストッキング好きにはたまらない永久保存版です。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "美脚パンスト度: 100% | 挑発度: 98% | 実用性: 98%"
        },
        "pred00321": {
            "desc": """<h4>【作品解説・見どころ】希島あいり部長がチ○ポの言いなりに！出張先で貪り合う背徳不倫旅行</h4>
<p>圧倒的な美貌と知性で社内中の憧れの的である希島あいり部長。しかし裏では、部下の極太チ○ポに完全に胃袋ならぬ子宮を掴まれており、彼の言いなりになってしまっているという背徳設定。出張という名目で二人きりの温泉宿に泊まり、チェックイン直後から浴衣をはだけて貪り合います。普段の凛々しい部長としての姿は完全に消え去り、「あなたの硬いのがないと私、仕事も手につかないの…」と切なげに肉棒を懇願する姿は破壊力抜群です。</p>
<h4>【実用ポイント】美熟女の極上肉体と濃密な中出しピストン</h4>
<p>希島あいりの磨き上げられた美しい肢体、ふくよかなバストとしなやかな腰つきが、温泉の湯気と相まって最高の官能美を醸し出します。正常位でじっくりと奥を突き崩され、膣内射精された瞬間に幸福感に満ちたため息を漏らす表情はまさに至高。大人の女の色気と濃厚な絡み合いを堪能したい方に強く推奨します。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "背徳中毒度: 99% | 熟女美貌: 98% | 実用性: 97%"
        },
        "smok00021": {
            "desc": """<h4>【作品解説・見どころ】辻井ほのかの長い舌が絡みつく！残業密室でのよだれダラダラ濃密ベロキス</h4>
<p>豊満なスタイルと妖艶なフェロモンでファンを魅了する辻井ほのかが、残業中のオフィスで部下を誘惑するセクハラ上司に扮した傑作。誰もいなくなった夜のフロアで、コピー機の前や会議室の隅で二人きりになり、部下の耳元に熱い吐息を吹きかけます。本作最大の武器は、辻井ほのかの天下一品とも言える「ベロキス」。部下の口内に長い舌をねじ込み、唾液をダラダラと垂らしながら貪るように唇を奪い、脳をトロトロに溶かしていきます。</p>
<h4>【実用ポイント】唾液まみれの密着フェラと吸い付くような生ハメ</h4>
<p>キスだけで完全に勃起させられた部下をソファに押し倒し、溢れる唾液を潤滑油にしてじっくりとしゃぶり上げるフェラチオは圧巻。そのまま濡れ切った自らの秘部に肉棒を導き入れ、机の上で激しく腰を打ち付けるシーンでは、生々しい水音と喘ぎ声が静かなオフィスに反響します。残業シチュエーションの良さが極限まで凝縮された名作です。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "ベロキス粘度: 100% | 密室背徳度: 97% | 実用性: 98%"
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
        c_data = reviews_data_1.get(cid, {})

        sample_imgs_html = ""
        if sample_imgs:
            img_tags = "".join([f'<img src="{sim}" alt="{title} サンプル{s_idx+1}" class="w-full h-28 object-cover rounded-lg border border-slate-700/80 hover:scale-105 transition transform duration-300" loading="lazy" />' for s_idx, sim in enumerate(sample_imgs)])
            sample_imgs_html = f'<div class="grid grid-cols-2 md:grid-cols-4 gap-2 my-4">{img_tags}</div>'

        item_block = f"""
<div class="my-10 bg-slate-900/90 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-2xl relative">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-2">
      <span class="bg-indigo-600 text-white font-black text-sm px-3 py-1 rounded-lg">第{idx+1}位</span>
      <span class="text-xs text-slate-400 font-mono tracking-wider">品番: {cid.upper()}</span>
    </div>
    <div class="text-amber-400 font-black text-sm tracking-wide">{c_data.get('rating', '★★★★★ 5.0 / 5.0')}</div>
  </div>

  <h3 class="text-xl md:text-2xl font-black text-white leading-snug mb-4 hover:text-indigo-400 transition">
    <a href="{aff_url}" target="_blank" rel="nofollow noopener">{title}</a>
  </h3>

  <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-start">
    <div class="md:col-span-5">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block group overflow-hidden rounded-xl border border-slate-700/80 shadow-lg relative">
        <img src="{large_img}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition duration-300 flex items-end p-4">
          <span class="bg-indigo-600 text-white font-bold text-xs px-3 py-1.5 rounded-full shadow-lg">FANZA公式で今すぐ無料サンプル再生 ▶</span>
        </div>
      </a>
      <div class="mt-3 text-xs bg-slate-800/60 p-2.5 rounded-lg border border-slate-700/50 text-slate-300">
        <span class="text-indigo-300 font-bold">評価スペック：</span> {c_data.get('service_score', '高水準')}
      </div>
    </div>

    <div class="md:col-span-7 space-y-4">
      <div class="space-y-2">
        <div class="text-xs text-slate-400"><strong class="text-slate-300">出演女優：</strong> {act_html if act_html else "人気単体女優"}</div>
        <div class="text-xs text-slate-400"><strong class="text-slate-300">関連タグ：</strong> {genre_html}</div>
      </div>

      <div class="prose prose-invert text-slate-300 text-sm leading-relaxed border-t border-slate-800/80 pt-3">
        {c_data.get('desc', '')}
      </div>

      {sample_imgs_html}

      <div class="pt-2 flex flex-col sm:flex-row gap-3">
        <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="flex-1 text-center bg-gradient-to-r from-indigo-600 via-indigo-500 to-indigo-700 hover:from-indigo-500 hover:to-indigo-600 text-white font-black py-3 px-6 rounded-xl shadow-lg transform active:scale-95 transition">
          FANZAで本編を見る（動画・高画質配信中）
        </a>
        <a href="/posts/{cid}" class="text-center bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold py-3 px-4 rounded-xl border border-slate-600 transition text-xs flex items-center justify-center">
          個別詳細ページ
        </a>
      </div>
    </div>
  </div>
</div>"""
        html_parts.append(item_block)

    faq_html = """<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl">
  <h3 class="text-xl md:text-2xl font-bold text-white mb-6 flex items-center gap-2">
    <span class="text-indigo-400">❓</span> 女上司シチュエーションに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-6 text-sm">
    <div class="border-b border-slate-800 pb-4">
      <h4 class="font-bold text-indigo-300 mb-2">Q1. 女上司モノで一番興奮するシチュエーションは何ですか？</h4>
      <p class="text-slate-300 leading-relaxed">圧倒的人気は「出張先のホテル相部屋」と「深夜残業の密室」です。普段は絶対的な上下関係がある二人が、物理的に逃げられない閉鎖空間に置かれることで、理性が崩壊するスリルと背徳感が最大化されます。</p>
    </div>
    <div class="border-b border-slate-800 pb-4">
      <h4 class="font-bold text-indigo-300 mb-2">Q2. 着衣プレイと全裸、どちらが見どころですか？</h4>
      <p class="text-slate-300 leading-relaxed">女上司モノの醍醐味は間違いなく「着衣」です。オフィスカジュアルやタイトスカート、ストッキングを身につけたまま、下着だけをずらして挿入する背徳描写こそが、このジャンルならではの最高の抜きどころです。</p>
    </div>
    <div>
      <h4 class="font-bold text-indigo-300 mb-2">Q3. 初めて見るならどれから鑑賞すべきですか？</h4>
      <p class="text-slate-300 leading-relaxed">まずは第1位の星乃莉子作品を推奨します。ストーリー構成の丁寧さ、女優の美貌、そして童貞部下に突き上げられてメスへと堕ちていく心理描写のリアリティが群を抜いており、誰でも確実に満足できます。</p>
    </div>
  </div>
</div>"""
    html_parts.append(faq_html)

    related_links_html = """<div class="my-8 bg-slate-950 border border-slate-800 rounded-2xl p-6">
  <h4 class="text-base font-bold text-white mb-3">🔥 あわせて読みたい人気キラー特集</h4>
  <ul class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm text-indigo-300">
    <li><a href="/posts/feature_fanza_pantyhose_slender_legs_ol_fetish_ranking" class="hover:underline">▶ 美脚・パンストOL特集！黒タイツとスーツ美女の足コキ＆密着</a></li>
    <li><a href="/posts/feature_fanza_pov_subjective_immersion_masterpiece_ranking" class="hover:underline">▶ 完全主観目線（POV）神作ランキング！ゼロ距離キスと見つめ合い</a></li>
    <li><a href="/posts/feature_fanza_creampie_breeding_deep_ejaculation_ranking" class="hover:underline">▶ 生中出し・種付け解禁ランキングTOP5！膣奥に注ぎ込まれる背徳</a></li>
    <li><a href="/posts/feature_fanza_luxury_soapland_foam_mat_play_ranking_2026" class="hover:underline">▶ 高級ソープ泡踊りマットプレイランキングTOP5！極上洗体奉仕</a></li>
  </ul>
</div>"""
    html_parts.append(related_links_html)

    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "ItemList",
                "name": "美人女上司・残業密室＆出張相部屋おすすめ神作ランキングTOP5",
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
                        "name": "女上司モノで一番興奮するシチュエーションは何ですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "圧倒的人気は「出張先のホテル相部屋」と「深夜残業の密室」です。普段は絶対的な上下関係がある二人が逃げられない閉鎖空間に置かれることで背徳感が最大化されます。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "着衣プレイと全裸、どちらが見どころですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "女上司モノの醍醐味は着衣です。タイトスカートやストッキングを身につけたまま下着だけをずらして挿入する背徳描写が最高の抜きどころです。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "初めて見るならどれから鑑賞すべきですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第1位の星乃莉子作品を推奨します。ストーリー構成の丁寧さ、女優の美貌、メスへと堕ちていく心理描写が群を抜いています。"
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
        "id": "feature_fanza_female_boss_office_overtime_hotel_ranking_2026",
        "title": "【オフィスで豹変するキャリア美女】FANZA「美人女上司・残業密室＆出張相部屋」おすすめ神作ランキングTOP5！普段は冷徹な高嶺の花が部下の絶倫ピストンに理性を溶かされ朝まで喘ぎ狂う下剋上AV選【2026年最新】",
        "date": "2026-10-04 01:00:00",
        "hinban": "FEMALE-BOSS-OVERTIME-HOTEL-BEST-2026",
        "price": "300~",
        "maker": "FANZA公式セレクション",
        "actresses": ["星乃莉子", "つばさ舞", "黒川すみれ", "希島あいり", "辻井ほのか"],
        "genres": ["女上司", "キャリアウーマン", "オフィス", "残業", "出張相部屋", "下剋上", "特集", "殿堂入り"],
        "image": cover_image,
        "review": full_html
    }

    file_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f" -> Successfully saved Article 1 ({char_count} chars) to {file_path}")


# ==============================================================================
# 記事2: 同窓会再会・人妻クラスメイトとの泥酔W不倫特化
# ==============================================================================
def generate_article_class_reunion():
    print("=== Generating Article 2: 同窓会再会・人妻クラスメイト不倫特化 ===")
    cids = ["snos00392", "miab00452", "mida00624", "rbk00133", "1drpt00048"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["同窓会", "人妻", "再会", "W不倫"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 2 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-purple-950/40 via-slate-900 to-slate-950 border border-purple-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-purple-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-purple-500/20 text-purple-300 border border-purple-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">CLASS REUNION AFFAIR SPECIAL</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月04日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【十数年ぶりの再会と初恋の情火】FANZA「同窓会再会・人妻クラスメイトとの泥酔W不倫」おすすめ神作ランキングTOP5！昔憧れだった清楚なマドンナがラブホテルで理性崩壊・朝まで中出しを貪り合う背徳AV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    青春時代の淡い思い出と、大人になった現在が交錯する究極の背徳エロス、それが「同窓会×人妻再会不倫」です。学生時代には遠くから見つめることしかできなかったクラスのマドンナ、あるいは当時付き合っていた初恋の彼女。十数年の時を経て再会した彼女の薬指には結婚指輪が光り、すっかり落ち着いた大人の女性としての艶やかな色気を纏っています。お互いに重ねてきた月日を感じながら乾杯を交わし、懐かしい思い出話に花を咲かせるうちに、当時の熱情が再び胸の奥底で疼き始めます。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    一次会が終わり、二次会を抜け出して夜の街へと繰り出す二人。お酒の酔いと深夜の空気感が理性のブレーキを緩め、「終電なくなっちゃったね…」「少し休んでいかない？」という甘い口実のもとラブホテルの扉をくぐります。夫や子供の待つ日常を背負いながらも、昔の男の逞しい腕に抱かれ、首筋に熱いキスを落とされる人妻。結婚指輪をはめたまま恥じらいに頬を染め、十数年ぶりの結合に腰を震わせる姿は、他のどんなシチュエーションにも勝るリアリティと哀愁を帯びたエロティシズムを放ちます。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、金松季歩の圧巻NTR狂い咲き作から、逢沢みゆ＆北岡果林の贅沢元カノ相部屋作、葵いぶきのヤンチャ妻法事再会作、夏目彩春の恩師密会作、倉多まおの露出調教作まで、FANZAで歴代トップクラスの売上と満足度を記録する【同窓会再会・人妻W不倫神作TOP5】を厳選してお届けします。
  </p>
</div>

<!-- 選び方の基準 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-purple-400">🍷</span> 失敗しない同窓会不倫AV選び！心まで揺さぶられる3大鑑賞ポイント
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-purple-300 mb-2">① お酒が進む居酒屋からホテルへの自然な導入</h4>
      <p class="text-slate-300 leading-relaxed">ただ脱ぐのではなく、昔話で盛り上がり、手と手が触れ合い、居酒屋のトイレやタクシーの中で徐々に熱気を帯びていく過程のリアルさが興奮を煽ります。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-purple-300 mb-2">② 結婚指輪と大人の肉体のコントラスト</h4>
      <p class="text-slate-300 leading-relaxed">指に輝く指輪を隠すように顔を覆いながらも、下半身は我慢できずに愛液でドロドロに濡れそぼっている人妻の矛盾した姿に男は最高に欲情します。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-purple-300 mb-2">③ 朝を迎えるまでの執拗な貪り合い</h4>
      <p class="text-slate-300 leading-relaxed">「今夜だけ…」と言いながら一度では終わらず、シャワーを浴びた後もベッドで求め合い、夜明けまで生中出しを繰り返す濃厚な交わりが必須です。</p>
    </div>
  </div>
</div>"""
    html_parts.append(intro_html)

    reviews_data_2 = {
        "snos00392": {
            "desc": """<h4>【作品解説・見どころ】金松季歩が魅せる魂の快楽堕ち！同窓会で再会した元彼の絶倫ピストンに狂う人妻</h4>
<p>端正な美貌と豊満な肢体を兼ね備えた人気女優・金松季歩が、幸せな結婚生活を送る人妻として登場。地元で開催された同窓会で、10年ぶりに最低で自分勝手だった元彼と再会します。昔散々振り回されたはずなのに、大人になってさらに男の色気を増した元彼に酒の勢いで口説かれ、抗えない力でホテルへと連れ込まれます。最初は「私には夫がいるの、絶対にダメ」と激しく拒絶する金松季歩ですが、昔身体が覚えていた絶倫テクニックで乳首や秘部を執拗に攻め立てられると、抑え込んでいた淫乱な本性が一気に決壊。涙を流しながらも腰を浮かせて肉棒を迎え入れる姿は息を呑む迫力です。</p>
<h4>【実用ポイント】夫への罪悪感を吹き飛ばす容赦ない連続中出し</h4>
<p>元彼の荒々しいバックからの腰振りに、彼女の内壁はぎゅんぎゅんと締め付けられ、幾度も絶頂に達します。「昔みたいに中にいっぱい出して…！」と理性を失った懇願とともに膣奥深くに放たれる濃厚な精液。背徳感と純粋な快楽が極限まで混ざり合った、近年の同窓会・寝取られジャンルにおける最高峰の傑作です。</p>""",
            "rating": "★★★★★ 5.0 / 5.0",
            "service_score": "背徳リアル度: 100% | 絶頂痙攣度: 100% | 実用性: 100%"
        },
        "miab00452": {
            "desc": """<h4>【作品解説・見どころ】逢沢みゆ＆北岡果林という奇跡のWヒロイン！元カノ2人とホテル相部屋泥酔情事</h4>
<p>AV界の至宝・逢沢みゆと、可憐な透明感で絶大な人気を誇る北岡果林が夢の共演を果たした奇跡の一本。主人公の元カノである二人が同窓会で揃い踏みし、三次会終わりに終電を逃して3人でホテルのスイートルームに泊まることに。お酒の力も手伝って「どっちとのセックスの方が良かった？」と昔のベッド事情の暴露合戦が勃発。互いにライバル心を燃やしながら男の服を脱がせ、左右から耳元に吐息を吹きかけながら愛撫を仕掛けてくる展開は、男の妄想の極致です。</p>
<h4>【実用ポイント】至高の美女2人による贅沢極まる交互フェラとサンドイッチ交尾</h4>
<p>逢沢みゆのしなやかな美脚と北岡果林の初々しい身体に挟まれ、休む間もなくペニスを吸い上げられる圧巻の3Pプレイ。代わる代わる上に跨っては「私の方が気持ちいいでしょ？」と腰を競い合い、最後は二人の子宮に連続して白濁液を注ぎ込みます。画面の隅々まで極上の美女で埋め尽くされた贅沢すぎる名作です。</p>""",
            "rating": "★★★★★ 4.9 / 5.0",
            "service_score": "ハーレム贅沢度: 100% | 美女密度: 100% | 実用性: 99%"
        },
        "mida00624": {
            "desc": """<h4>【作品解説・見どころ】葵いぶきが魅せる元ヤン妻の脆さ！法事・地元同窓会で蘇る悪夢の情欲</h4>
<p>圧倒的なプロポーションと色気を誇る葵いぶきが、過去のヤンチャな黒歴史を隠して真面目な夫と暮らす人妻を熱演。地元の法事と同窓会で6年ぶりに帰郷した際、当時恐れられていた地元の先輩・元同級生たちと再会してしまいます。昔の弱みを握られ、強引にお酒を飲まされて薄暗い実家の離れや車内に連れ込まれる葵いぶき。清楚な着物やワンピース姿を乱暴にはだけられ、抵抗虚しく身体の奥底に眠っていた性欲のツボを抉られていく過程は、見る者のサディスティックな欲情を激しく煽ります。</p>
<h4>【実用ポイント】荒々しい男たちに貪り尽くされる生々しい濃厚セックス</h4>
<p>地元ヤンキーならではの粗暴で力強いピストンに、最初は嫌がっていた彼女も徐々に喘ぎ声を漏らし、最後には白目を剥いて腰をガクガクと震わせます。清楚な妻の仮面が剥がれ落ち、雄の臭いに屈服していく葵いぶきの生々しい演技が光る、背徳感MAXの一本です。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "地元背徳度: 99% | 乱れっぷり: 98% | 実用性: 98%"
        },
        "rbk00133": {
            "desc": """<h4>【作品解説・見どころ】夏目彩春の儚げな色気！終電を逃して憧れだった恩師と貪り合う一夜</h4>
<p>息を呑むような美貌と透明感を誇る夏目彩春が、同窓会でかつて密かに想いを寄せていた恩師と再会。大人になった教え子の美しさに先生も目を奪われ、二次会の後の静まり返ったBARで二人きりに。終電を逃したことをきっかけにホテルに入り、長い年月を経てようやく結ばれる二人の愛欲がドラマチックに描かれます。夏目彩春のしっとりとした白肌、慈しむように触れられる指先に敏感に反応し、切なげな吐息を漏らす姿は純文学のような官能美を放ちます。</p>
<h4>【実用ポイント】互いの身体を確かめ合う丁寧かつ濃厚な絡み合い</h4>
<p>恩師の手で優しく下着を脱がされ、恥ずかしそうに胸を隠しながらも濡れた瞳で見つめ返す夏目彩春。挿入の瞬間にはぎゅっと恩師の背中に爪を立て、じっくりとしたストロークで奥を突かれるたびに甘い声を響かせます。大人の情感とエロティシズムが高次元で融合した、心まで満たされる傑作です。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "情緒・美貌度: 100% | 切なさエロス: 98% | 実用性: 97%"
        },
        "1drpt00048": {
            "desc": """<h4>【作品解説・見どころ】倉多まおの変態的露出！10年ぶり再会の元カノに乳首リードをつけて調教</h4>
<p>抜群のプロポーションとドMな演技で熱狂的人気を誇る倉多まおが、同窓会で再会した昔の男に調教される破滅的快作。大人しく清楚な女性として現れた彼女ですが、かつて自分を調教してくれた元彼と二人きりになると、当時の快楽の記憶がフラッシュバック。服の下に乳首ピアスやリードを装着され、深夜のホテル街や非常階段を連れ回されるという過激な露出プレイへと発展します。恐怖と羞恥に震えながらも、股間からは愛液が滴り落ちて止まらない倒錯的なエロスが炸裂します。</p>
<h4>【実用ポイント】リードを引かれて悶絶するマゾヒスティックな快楽絶頂</h4>
<p>ホテルの部屋に戻った後は、溜まりに溜まった欲望を一気に爆発させる荒々しいピストン。乳首を引っ張られながら奥深くまで貫かれ、「先生…もっと狂わせてください！」と叫びながらイキ狂う倉多まおの姿は圧巻です。変態的シチュエーションを心ゆくまで楽しみたい玄人ファンに強くおすすめします。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "倒錯露出度: 100% | ドM快楽度: 99% | 実用性: 97%"
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
        c_data = reviews_data_2.get(cid, {})

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
        <span class="text-purple-300 font-bold">評価スペック：</span> {c_data.get('service_score', '高水準')}
      </div>
    </div>

    <div class="md:col-span-7 space-y-4">
      <div class="space-y-2">
        <div class="text-xs text-slate-400"><strong class="text-slate-300">出演女優：</strong> {act_html if act_html else "人気単体女優"}</div>
        <div class="text-xs text-slate-400"><strong class="text-slate-300">関連タグ：</strong> {genre_html}</div>
      </div>

      <div class="prose prose-invert text-slate-300 text-sm leading-relaxed border-t border-slate-800/80 pt-3">
        {c_data.get('desc', '')}
      </div>

      {sample_imgs_html}

      <div class="pt-2 flex flex-col sm:flex-row gap-3">
        <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="flex-1 text-center bg-gradient-to-r from-purple-600 via-purple-500 to-purple-700 hover:from-purple-500 hover:to-purple-600 text-white font-black py-3 px-6 rounded-xl shadow-lg transform active:scale-95 transition">
          FANZAで本編を見る（動画・高画質配信中）
        </a>
        <a href="/posts/{cid}" class="text-center bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold py-3 px-4 rounded-xl border border-slate-600 transition text-xs flex items-center justify-center">
          個別詳細ページ
        </a>
      </div>
    </div>
  </div>
</div>"""
        html_parts.append(item_block)

    faq_html = """<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl">
  <h3 class="text-xl md:text-2xl font-bold text-white mb-6 flex items-center gap-2">
    <span class="text-purple-400">❓</span> 同窓会不倫シチュエーションに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-6 text-sm">
    <div class="border-b border-slate-800 pb-4">
      <h4 class="font-bold text-purple-300 mb-2">Q1. 同窓会モノがなぜこれほど男に刺さるのですか？</h4>
      <p class="text-slate-300 leading-relaxed">「学生時代の手が届かなかった憧れ」と「大人になって人妻となった現在の背徳感」が完璧に結びついているからです。ノスタルジーと生々しい肉欲が同時に満たされるため、感情移入度が他のジャンルとは桁違いです。</p>
    </div>
    <div class="border-b border-slate-800 pb-4">
      <h4 class="font-bold text-purple-300 mb-2">Q2. NTR（寝取られ）要素が強い作品はありますか？</h4>
      <p class="text-slate-300 leading-relaxed">ランキング第1位の金松季歩作品や第3位の葵いぶき作品は、夫に対する罪悪感を抱きながらも身体の快楽に抗えずに堕ちていく心理描写が徹底されており、極上のNTRカタルシスを味わえます。</p>
    </div>
    <div>
      <h4 class="font-bold text-purple-300 mb-2">Q3. 純愛風と泥沼風、どちらがおすすめですか？</h4>
      <p class="text-slate-300 leading-relaxed">甘美で切ない情事を好むなら第4位の夏目彩春作品、激しい腰振りと本能剥き出しの交わりを求めるなら第1位の金松季歩作品がイチオシです。</p>
    </div>
  </div>
</div>"""
    html_parts.append(faq_html)

    related_links_html = """<div class="my-8 bg-slate-950 border border-slate-800 rounded-2xl p-6">
  <h4 class="text-base font-bold text-white mb-3">🔥 あわせて読みたい人気キラー特集</h4>
  <ul class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm text-purple-300">
    <li><a href="/posts/feature_fanza_ntr_netorare_cuckold_best_masterpieces" class="hover:underline">▶ NTR・寝取られ神作ランキングTOP5！最愛の女が絶倫チ○ポに堕ちる</a></li>
    <li><a href="/posts/feature_fanza_mature_milf_wives_best_selection_ranking" class="hover:underline">▶ 人妻・美熟女ランキングTOP5！背徳の不倫交尾と濃厚フェラ</a></li>
    <li><a href="/posts/feature_fanza_hot_spring_ryokan_trip_ranking" class="hover:underline">▶ 温泉旅行・混浴生ハメランキングTOP5！浴衣はだける湯上がり情事</a></li>
    <li><a href="/posts/feature_fanza_creampie_breeding_deep_ejaculation_ranking" class="hover:underline">▶ 生中出し・種付け解禁ランキングTOP5！膣奥に注ぎ込まれる白濁精液</a></li>
  </ul>
</div>"""
    html_parts.append(related_links_html)

    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "ItemList",
                "name": "同窓会再会・人妻クラスメイトとの泥酔W不倫おすすめ神作ランキングTOP5",
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
                        "name": "同窓会モノがなぜこれほど男に刺さるのですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "学生時代の手が届かなかった憧れと、大人になって人妻となった現在の背徳感が完璧に結びついているため、感情移入度が桁違いに高いからです。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "NTR（寝取られ）要素が強い作品はありますか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第1位の金松季歩作品や第3位の葵いぶき作品は、夫に対する罪悪感を抱きながらも快楽に抗えずに堕ちていく心理描写が徹底されています。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "純愛風と泥沼風、どちらがおすすめですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "甘美で切ない情事を好むなら第4位の夏目彩春作品、激しい腰振りと本能剥き出しの交わりを求めるなら第1位の金松季歩作品がイチオシです。"
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
        "id": "feature_fanza_class_reunion_married_classmate_affair_ranking_2026",
        "title": "【十数年ぶりの再会と初恋の情火】FANZA「同窓会再会・人妻クラスメイトとの泥酔W不倫」おすすめ神作ランキングTOP5！昔憧れだった清楚なマドンナがラブホテルで理性崩壊・朝まで中出しを貪り合う背徳AV選【2026年最新】",
        "date": "2026-10-04 01:10:00",
        "hinban": "CLASS-REUNION-AFFAIR-BEST-2026",
        "price": "300~",
        "maker": "FANZA公式セレクション",
        "actresses": ["金松季歩", "逢沢みゆ", "北岡果林", "葵いぶき", "夏目彩春", "倉多まお"],
        "genres": ["同窓会", "人妻", "再会", "初恋", "W不倫", "泥酔", "中出し", "特集", "殿堂入り"],
        "image": cover_image,
        "review": full_html
    }

    file_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f" -> Successfully saved Article 2 ({char_count} chars) to {file_path}")


# ==============================================================================
# 記事3: 隣の若妻・留守中のベランダ密会＆玄関先不倫特化
# ==============================================================================
def generate_article_neighbor_wife():
    print("=== Generating Article 3: 隣の若妻・玄関＆ベランダ不倫特化 ===")
    cids = ["wanz00869", "madm00221", "hhkl00258", "royd00316", "1svgal00009"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["隣の奥さん", "若妻", "人妻", "玄関不倫"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 3 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-amber-950/40 via-slate-900 to-slate-950 border border-amber-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-amber-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-amber-500/20 text-amber-300 border border-amber-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">NEIGHBOR WIFE SECRET AFFAIR</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月04日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【壁一枚隔てた背徳の温もり】FANZA「隣の若妻・留守中のベランダ密会＆玄関先不倫」おすすめ神作ランキングTOP5！清楚なエプロン姿から欲求不満を爆発させて男を貪る濃厚中出しAV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    日常のすぐ隣に潜む最も身近で、最も危険な情欲の結晶、それが「隣の奥さん・若妻シチュエーション」です。アパートやマンションの薄い壁一枚を隔てたすぐ隣の部屋。朝のゴミ出しや回覧板の受け渡しですれ違うたびに漂う甘い柔軟剤の匂いと、エプロンの下から覗く柔らかなボディライン。真面目で献身的な良妻に見える彼女たちが、実は夫の淡白さや長期出張による激しい欲求不満を抱えており、隣に住む独身の自分に助けを求めるように視線を投げかけてくる…という妄想は、すべての男の射精本能を強烈に刺激します。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    このジャンルの最大の魅力は、いつ誰が帰ってくるかわからない「極限のスリル」と、生活空間で行われる濃厚な絡み合いにあります。夫を見送った直後の玄関先でのわずか数分間の立ちバック、ベランダで洗濯物を干すふりをしながら交わす密着キス、そして夫の不在時に部屋へと招き入れられて行われる昼下がりの生中出し。エプロン姿のままパンティをずらされ、恥じらいながらも膣奥をヒクつかせて男の精子を欲しがる若妻の姿は、日常を忘れさせる圧倒的な実用性をもたらします。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、美尻クイーン・篠田ゆうの超絶トゥワーク騎乗位作から、桜野桃の4K極上爆乳出張喰い尽くし作、通野未帆の玄関先3分濃厚不倫作、小栗操の朝の見送り直後情事作、小那海あやの金魚妻旅館作まで、FANZAで不動の人気を誇る【隣の若妻×禁断不倫神作TOP5】を徹底レビューします。
  </p>
</div>

<!-- 選び方の基準 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-amber-400">🚪</span> 失敗しない隣の奥さんモノ選び！興奮を最大化する3大チェック基準
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-amber-300 mb-2">① エプロン・部屋着・薄着の生々しいリアル感</h4>
      <p class="text-slate-300 leading-relaxed">着飾ったドレスではなく、普段着のエプロン姿や胸元がゆるい部屋着から溢れ出る生々しい生活感とエロティシズムの融合が重要です。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-amber-300 mb-2">② 玄関・ベランダ・リビング等の日常ロケーション</h4>
      <p class="text-slate-300 leading-relaxed">ホテルではなく自宅の玄関先やドアチェーン越し、ベランダなど、足音が聞こえたら一発アウトの緊迫感が生ハメの興奮を何倍にも高めます。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-amber-300 mb-2">③ 欲求不満ゆえの貪欲な腰振りと中出し懇願</h4>
      <p class="text-slate-300 leading-relaxed">「主人のよりもずっと太い…」「中にたっぷり注いで」と、満たされない性欲を隣人男にぶつけて自ら腰を振り乱す若妻の狂態が最高の実用度を生みます。</p>
    </div>
  </div>
</div>"""
    html_parts.append(intro_html)

    reviews_data_3 = {
        "wanz00869": {
            "desc": """<h4>【作品解説・見どころ】篠田ゆうの国宝級美尻が唸る！隣人若妻による怒涛のトゥワーク腰振り責め</h4>
<p>AV界屈指の美尻とダイナミックな腰使いで絶大な人気を誇る篠田ゆうが、隣に住む欲求不満な若妻として登場。仕事で留守がちな夫への不満から、隣に引っ越してきた主人公のたくましい身体に目をつけます。「ちょっと電球を替えてくれませんか？」と自宅に招き入れ、ショートパンツから溢れんばかりのプリッとした美尻を至近距離で見せつけて誘惑。我慢できずに押し倒した主人公のペニスの上に跨ると、自慢の豊満ヒップを激しく上下左右にバウンドさせる超絶トゥワーク騎乗位を開始します。肉と肉がぶつかり合うバチバチという炸裂音と、嬉々として男を搾り取る彼女の笑顔が強烈なインパクトを残します。</p>
<h4>【実用ポイント】1週間連続で部屋に通わされ精子を搾り尽くされる極上体験</h4>
<p>一度味わったら抜け出せない麻薬のような快楽に、主人公は1週間にわたって隣の部屋に通い詰めることに。バックから激しくヒップアタックを喰らいながらのピストン、そして最後は膣内にドクドクと中出しされた瞬間、ギュッと内壁を締め上げて一滴も逃さない名器のバキューム力を発揮します。尻フェチ・人妻フェチなら絶対に観ておくべき殿堂入りの一本です。</p>""",
            "rating": "★★★★★ 5.0 / 5.0",
            "service_score": "美尻トゥワーク度: 100% | 搾精快楽度: 100% | 実用性: 100%"
        },
        "madm00221": {
            "desc": """<h4>【作品解説・見どころ】桜野桃の4K超高画質爆乳！夫の長期出張中に隣人男を喰い尽くす肉食若妻</h4>
<p>圧倒的なボリュームを誇る美巨乳と愛らしいルックスでファンを虜にする桜野桃の傑作。4K撮影による毛穴や汗の粒まで見えるような圧倒的映像美で、隣人妻のリアルな肉体美が迫ります。「私の胸…さっきからずっと見てましたよね？」と悪戯っぽく微笑み、胸元の開いたキャミソールからこぼれそうな爆乳を押し当ててくる桜野桃。夫の出張でぽっかりと空いた寂しさと疼きを埋めるため、隣人を部屋に引き入れて獣のように貪り始めます。</p>
<h4>【実用ポイント】たゆたう巨乳パイズリと子宮直撃ピストンでの大絶頂</h4>
<p>両手で抱えきれないほどの柔らかいおっぱいに肉棒を挟み込まれる濃厚パイズリは悶絶必至。本番に入ると、重力に従って激しく揺れ動くバストを下から見上げながらの正常位で、奥深くまで亀頭を突き刺します。桜野桃は歓喜の声を上げながら「奥当たってて気持ちいいのぉ！」と連続アクメに達し、溢れ出る白濁液を嬉しそうに受け止める姿が網膜に焼き付きます。</p>""",
            "rating": "★★★★★ 4.9 / 5.0",
            "service_score": "4K超高画質度: 100% | 爆乳パイズリ: 99% | 実用性: 99%"
        },
        "hhkl00258": {
            "desc": """<h4>【作品解説・見どころ】通野未帆のリアルな生々しさ！玄関先で3分間だけ交わる禁断の日常不倫</h4>
<p>独特の透明感と哀愁漂う色気で人妻モノのトップに君臨する通野未帆の伝説的タイトル。毎朝夫を送り出した後のわずかな時間、あるいはゴミ出しの帰り際、隣の部屋の玄関先で「少しだけ…」と交わされる3分間の濃厚情事。靴を履いたままエプロンをたくし上げ、ドアスコープを気にしながら無言で絡み合う二人の緊迫感は、他のAVでは決して味わえない究極のリアルを演出しています。</p>
<h4>【実用ポイント】ドア越しにいつ人が通るかわからない極限スリル立ちバック</h4>
<p>息を潜め、声を押し殺しながら行われる玄関先での立ちバック。靴音ひとつで心臓が跳ね上がる状況の中、通野未帆の秘部は緊張と興奮でぐしょぐしょに濡れそぼっています。わずか3分の制限時間の中で一気に突き上げられ、中出しされた瞬間に安堵と快楽が混ざり合った吐息を漏らす彼女の横顔は、背徳マニアを完全にノックアウトします。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "玄関先緊迫度: 100% | リアル背徳度: 99% | 実用性: 98%"
        },
        "royd00316": {
            "desc": """<h4>【作品解説・見どころ】小栗操の火照った身体！旦那を見送った直後に貪り合う朝の玄関情事</h4>
<p>熟れた果実のような豊満な肉体と母性的な色気が魅力の小栗操。夫を「いってらっしゃい」と笑顔で見送り、ドアを閉めたわずか数秒後、物陰から現れた隣人男を玄関内に引き入れて抱き合うという背徳の極み。夫の残り香がまだ漂う玄関ホールで、脱ぎたてのサンダルを散らばらせながら貪り合う二人の姿には、日常を破壊する圧倒的なエネルギーが宿っています。</p>
<h4>【実用ポイント】熟女妻の溢れる愛液とねっとり吸い付く生挿入</h4>
<p>小栗操のしっとりとした柔肌と豊かなお尻を撫で回し、玄関マットの上に腰を下ろさせての結合。夫には見せたことのない淫乱な腰使いで下から迎え入れ、「主人がいない間、ずっと私のお世話してね」と耳元で囁きます。熟女ならではの包容力と底なしの性欲に溺れたい男性に自信を持って推薦できる快作です。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "朝の背徳度: 99% | 熟女の淫靡さ: 98% | 実用性: 97%"
        },
        "1svgal00009": {
            "desc": """<h4>【作品解説・見どころ】小那海あやが魅せる金魚妻の妖艶！隣の奥さんと秘密の温泉旅行でヤリまくり</h4>
<p>端正な顔立ちとスレンダーかつしなやかなボディで人気の小那海あや。隣人同士として親しくなるうちに一線を越え、ついに夫に内緒で二人きりの温泉旅館へとお忍び旅行へ出かけることに。畳敷きの部屋に敷かれた布団の上、浴衣をはだけた彼女は「布団の中なら誰にも見られないから…」と、昼間の清楚な態度をかなぐり捨ててゲスな金魚妻へと豹変。温泉で火照った素肌を密着させながら、朝から晩まで貪り合う贅沢な時間が流れます。</p>
<h4>【実用ポイント】布団の中で繰り広げられるエンドレス中出し交尾</h4>
<p>小那海あやのしなやかな美脚を肩に担ぎ上げ、深い角度で突き刺す正常位。奥を突かれるたびに背中を弓なりにしてイキ声を響かせ、最後は布団を汚すほどの大量中出しでフィニッシュ。隣人妻を独占してヤリまくるという男の全能感を完璧に満たしてくれる極上タイトルです。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "温泉不倫度: 100% | 豹変痴女度: 98% | 実用性: 98%"
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
        c_data = reviews_data_3.get(cid, {})

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
        <span class="text-amber-300 font-bold">評価スペック：</span> {c_data.get('service_score', '高水準')}
      </div>
    </div>

    <div class="md:col-span-7 space-y-4">
      <div class="space-y-2">
        <div class="text-xs text-slate-400"><strong class="text-slate-300">出演女優：</strong> {act_html if act_html else "人気単体女優"}</div>
        <div class="text-xs text-slate-400"><strong class="text-slate-300">関連タグ：</strong> {genre_html}</div>
      </div>

      <div class="prose prose-invert text-slate-300 text-sm leading-relaxed border-t border-slate-800/80 pt-3">
        {c_data.get('desc', '')}
      </div>

      {sample_imgs_html}

      <div class="pt-2 flex flex-col sm:flex-row gap-3">
        <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="flex-1 text-center bg-gradient-to-r from-amber-600 via-amber-500 to-amber-700 hover:from-amber-500 hover:to-amber-600 text-white font-black py-3 px-6 rounded-xl shadow-lg transform active:scale-95 transition">
          FANZAで本編を見る（動画・高画質配信中）
        </a>
        <a href="/posts/{cid}" class="text-center bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold py-3 px-4 rounded-xl border border-slate-600 transition text-xs flex items-center justify-center">
          個別詳細ページ
        </a>
      </div>
    </div>
  </div>
</div>"""
        html_parts.append(item_block)

    faq_html = """<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl">
  <h3 class="text-xl md:text-2xl font-bold text-white mb-6 flex items-center gap-2">
    <span class="text-amber-400">❓</span> 隣の奥さんシチュエーションに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-6 text-sm">
    <div class="border-b border-slate-800 pb-4">
      <h4 class="font-bold text-amber-300 mb-2">Q1. なぜ「隣の奥さん」モノはこれほど興奮するのですか？</h4>
      <p class="text-slate-300 leading-relaxed">日常生活と非日常の境界線が最も曖昧なジャンルだからです。ゴミ出しや回覧板といった誰もが経験する日常風景のすぐ裏で、夫に隠れて行われる生々しい情事という背徳感が、男の脳をダイレクトに痺れさせます。</p>
    </div>
    <div class="border-b border-slate-800 pb-4">
      <h4 class="font-bold text-amber-300 mb-2">Q2. 一番おすすめの抜きどころはどこですか？</h4>
      <p class="text-slate-300 leading-relaxed">「玄関先」や「ベランダ」など、誰かが通りかかるかもしれない極限のスリルの中で行われる立ちバックや素股、そして我慢できずに膣内にぶちまけられる中出しシーンが最大の抜きどころです。</p>
    </div>
    <div>
      <h4 class="font-bold text-amber-300 mb-2">Q3. スタイル抜群系とムチムチ熟女系、どちらが人気ですか？</h4>
      <p class="text-slate-300 leading-relaxed">どちらも甲乙つけがたい人気を誇ります。超絶ヒップの篠田ゆうや4K爆乳の桜野桃のような肉体美を堪能したい方は第1位・第2位、日常のリアルな哀愁と包容力を味わいたい方は第3位の通野未帆や第4位の小栗操がイチオシです。</p>
    </div>
  </div>
</div>"""
    html_parts.append(faq_html)

    related_links_html = """<div class="my-8 bg-slate-950 border border-slate-800 rounded-2xl p-6">
  <h4 class="text-base font-bold text-white mb-3">🔥 あわせて読みたい人気キラー特集</h4>
  <ul class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm text-amber-300">
    <li><a href="/posts/feature_fanza_mature_milf_wives_best_selection_ranking" class="hover:underline">▶ 人妻・美熟女ランキングTOP5！背徳の不倫交尾と濃厚フェラ</a></li>
    <li><a href="/posts/feature_fanza_huge_ass_back_piston_ranking_2026" class="hover:underline">▶ 超巨尻・美尻×バック後背位ピストンランキングTOP5！顔面騎乗窒息</a></li>
    <li><a href="/posts/feature_fanza_creampie_breeding_deep_ejaculation_ranking" class="hover:underline">▶ 生中出し・種付け解禁ランキングTOP5！膣奥に注ぎ込まれる白濁精液</a></li>
    <li><a href="/posts/feature_fanza_ntr_netorare_cuckold_best_masterpieces" class="hover:underline">▶ NTR・寝取られ神作ランキングTOP5！最愛の女が絶倫チ○ポに堕ちる</a></li>
  </ul>
</div>"""
    html_parts.append(related_links_html)

    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "ItemList",
                "name": "隣の若妻・留守中のベランダ密会＆玄関先不倫おすすめ神作ランキングTOP5",
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
                        "name": "なぜ「隣の奥さん」モノはこれほど興奮するのですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "日常生活と非日常の境界線が最も曖昧なジャンルだからです。日常風景のすぐ裏で夫に隠れて行われる生々しい情事という背徳感が男の脳をダイレクトに刺激します。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "一番おすすめの抜きどころはどこですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "玄関先やベランダなど誰かが通りかかるかもしれない極限のスリルの中で行われる立ちバックや中出しシーンが最大の抜きどころです。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "スタイル抜群系とムチムチ熟女系、どちらが人気ですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "超絶ヒップの篠田ゆうや4K爆乳の桜野桃のような肉体美なら第1位・第2位、日常のリアルな哀愁と包容力なら第3位の通野未帆や第4位の小栗操がイチオシです。"
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
        "id": "feature_fanza_neighbor_young_wife_forbidden_affair_ranking_2026",
        "title": "【壁一枚隔てた背徳の温もり】FANZA「隣の若妻・留守中のベランダ密会＆玄関先不倫」おすすめ神作ランキングTOP5！清楚なエプロン姿から欲求不満を爆発させて男を貪る濃厚中出しAV選【2026年最新】",
        "date": "2026-10-04 01:20:00",
        "hinban": "NEIGHBOR-WIFE-AFFAIR-BEST-2026",
        "price": "300~",
        "maker": "FANZA公式セレクション",
        "actresses": ["篠田ゆう", "桜野桃", "通野未帆", "小栗操", "小那海あや"],
        "genres": ["隣の奥さん", "若妻", "人妻", "玄関不倫", "ベランダ", "留守中", "欲求不満", "中出し", "特集", "殿堂入り"],
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
    generate_article_female_boss()
    print("--------------------------------------------------")
    generate_article_class_reunion()
    print("--------------------------------------------------")
    generate_article_neighbor_wife()
    print("==================================================")
    print("3記事すべての生成が正常に完了しました！")
    print("==================================================")

if __name__ == "__main__":
    main()
