# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・超大型キラー特集3記事自動生成スクリプト
1. 【美脚CA・客室乗務員シチュエーション特化】
   『【フライト先ホテルの禁断ステイ】FANZA「美人CA・客室乗務員」おすすめ神作ランキングTOP5！制服パンスト美脚と気品あふれる空の女神が理性を溶かす濃厚交尾AV選【2026年最新】』
2. 【白衣の天使・ナース・看護師シチュエーション特化】
   『【夜勤病室の献身ケアと背徳の密会】FANZA「美人ナース・看護師」おすすめ神作ランキングTOP5！清楚な白衣の下に隠した淫らな素顔に癒やされ尽くす極上入院AV選【2026年最新】』
3. 【美人家庭教師・女子大生カテキョ密室指導特化】
   『【二人きりの勉強部屋で始まる大人の授業】FANZA「美人家庭教師・密室個人レッスン」おすすめ神作ランキングTOP5！清楚な知性派美女が教え子と貪り合う背徳の中出しAV選【2026年最新】』
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
# 記事1: 美脚CA・客室乗務員シチュエーション特化
# ==============================================================================
def generate_article_cabin_attendant():
    print("=== Generating Article 1: 美脚CA・客室乗務員特化 ===")
    cids = ["snos00377", "midv00530", "halt00066", "hmn00910", "rprj00003"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["キャビンアテンダント", "CA", "スチュワーデス", "美脚", "制服"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 1 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-sky-950/40 via-slate-900 to-slate-950 border border-sky-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-sky-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-sky-500/20 text-sky-300 border border-sky-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">CABIN ATTENDANT PREMIUM SPECIAL</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月04日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【フライト先ホテルの禁断ステイ】FANZA「美人CA・客室乗務員」おすすめ神作ランキングTOP5！制服パンスト美脚と気品あふれる空の女神が理性を溶かす濃厚交尾AV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    男性にとって永遠の憧れの職業であり、高嶺の花の象徴として君臨し続ける「CA（キャビンアテンダント・客室乗務員）」。空港のロビーを颯爽と歩く凛とした佇まい、洗練された笑顔と完璧なマナー、そしてタイトスカートのスリットから覗く黒パンスト美脚。普段は手の届かない別世界の美女たちが、フライト先の見知らぬホテルの密室で、日頃の過酷なプレッシャーから解放されて欲望のままに乱れ狂うシチュエーションは、男の支配欲と性衝動を極限まで掻き立てます。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    CAモノが圧倒的な人気を誇る最大の理由は、その「圧倒的なギャップ」と「着衣のフェティシズム」にあります。上空数万フィートで何百人もの乗客に優雅に接客していた才色兼備の美女が、夜のホテルでは制服を半ば着崩したまま汗だくで腰を振り、耳元で甘い喘ぎ声を漏らしながら肉棒を貪り尽くす姿。ストッキングを破かれ、擦れ合うナイロンの摩擦音とともに奥深くまで貫かれる瞬間の表情は、言葉にできない官能のカタルシスをもたらします。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、令和のトップアイコン・河北彩花が魅せる至高の甘えん坊CA作から、新ありなの圧巻スレンダー美脚足フェチ調教、沙月ふみのの欲求不満爆発ハメ、五日市芽依のノーパン直穿き騎乗位、そして本堂彩海のエアライン学生ドM堕ちまで、FANZAレビュー星4.5超え・実用度満点の【CA神作TOP5】を徹底紹介します。
  </p>
</div>

<!-- 選び方の基準 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-sky-400">✈️</span> 失敗しないCAモノ選び！極上の興奮を約束する3大チェックポイント
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-sky-300 mb-2">① タイトスカート＆パンスト美脚の着衣エロス</h4>
      <p class="text-slate-300 leading-relaxed">全裸にするのではなく、制服スカーフを首に巻き、黒パンストの股間部だけを破いて結合する着衣の生々しさが作品の完成度を決定づけます。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-sky-300 mb-2">② フライト先ホテルという密室の背徳感</h4>
      <p class="text-slate-300 leading-relaxed">見知らぬ土地の静まり返った客室で、翌朝のフライトを控えながらも快楽の泥沼に沈んでいく時間制限付きの緊迫感が抜きどころを跳ね上げます。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-sky-300 mb-2">③ 気品ある敬語から雌の乱れ喘ぎへの変貌</h4>
      <p class="text-slate-300 leading-relaxed">普段の丁寧なアナウンス口調が徐々に崩れ、「もうダメ…もっと奥まで突いてぇ！」と本能丸出しで懇願する表情の落差こそが最高の実用性です。</p>
    </div>
  </div>
</div>"""
    html_parts.append(intro_html)

    reviews_data = {
        "snos00377": {
            "desc": """<h4>【作品解説・見どころ】絶対的女王・河北彩花が魅せる！普段は清楚なCA彼女の裏の顔</h4>
<p>AV界の至宝・河北彩花が、誰もが羨むキャビンアテンダントの恋人役を熱演。フライトの過酷な勤務から帰宅した彼女が、照れくさそうに「今日はアブノーマルなエッチがしたい…」と甘えてくる導入から男の心臓は高鳴りっぱなしです。制服姿のまま目隠しをされ、言葉責めを受けながら愛撫される河北彩花。気品に満ちた普段の表情から一転、快楽の波に呑まれて首筋を紅潮させ、喘ぎ声を必死に押し殺そうとする姿はまさに息をのむ美しさです。</p>
<h4>【実用ポイント】清楚な美女が徐々に変態性に目覚めていく濃厚ピストン</h4>
<p>クライマックスの激しい結合では、彼女自身が秘めていた激しい性欲が完全に解放。正常位で奥深くを抉られるたびに瞳を潤ませ、男の首に細い腕を絡めつけながら幾度も絶頂に達します。最高峰の美貌とアブノーマルなシチュエーションが完璧に調和した、FANZA史上に残る超名作です。</p>""",
            "rating": "★★★★★ 5.0 / 5.0",
            "service_score": "美貌・気品: 100% | 着衣エロス: 98% | 実用性: 100%"
        },
        "midv00530": {
            "desc": """<h4>【作品解説・見どころ】奇跡のスタイル新ありな！美脚でドM男を弄ぶ足フェチ天国</h4>
<p>スラリと伸びた圧倒的な脚線美を誇る新ありなが、小悪魔的な甘サドCAに扮した足フェチ垂涎の逸品。フライト後のホテルで、ドMな部下や男性客を前にハイヒールと黒パンストを履き替えるシーンから視線が釘付けになります。冷ややかな笑みを浮かべながら「私の足、触りたいの？」「我慢できなくなっちゃった？」と囁き、足裏で股間をじっくりと踏みしだくプレイは悶絶必至の破壊力です。</p>
<h4>【実用ポイント】パンスト越しの濃密愛撫と狂おしいほどの騎乗位ピストン</h4>
<p>焦らしに焦らされた後、破いたパンストの間から結合するシーンの生々しさは鳥肌モノ。新ありなが自ら腰をグラインドさせ、恍惚の表情で男の精力を根こそぎ搾り取る騎乗位は圧巻のひと言です。美脚マニアなら絶対にコレクションに加えるべき最高峰の1本と言えます。</p>""",
            "rating": "★★★★★ 4.9 / 5.0",
            "service_score": "美脚フェチ度: 100% | サド挑発度: 99% | 実用性: 99%"
        },
        "halt00066": {
            "desc": """<h4>【作品解説・見どころ】沙月ふみのの高身長美巨乳！欲求不満が臨界点突破した濃厚交尾</h4>
<p>抜群のプロポーションと豊かなバストを兼ね備えた沙月ふみのが、フライト続きで3ヶ月も欲求不満を溜め込んだCAを演じる濃厚作。乗客として乗り合わせた男性の逞しい身体に目を奪われ、ステイ先のホテルで偶然を装って密会。部屋に入るや否や、溜まりに溜まった性欲を爆発させて男の唇を貪り、制服のボタンを引きちぎるように脱ぎ捨てていく肉食ぶりがたまりません。</p>
<h4>【実用ポイント】汗ばむ豊満ボディと止まらない激しい腰使い</h4>
<p>大人の色気たっぷりの肉体が激しく揺れ、豊満な胸が波打つバックピストンは圧巻の迫力。奥深くまで突き入れられるたびに「ああっ、もうずっと欲しかったの…！」と歓喜の叫びを上げ、何度もシーツを濡らしながらイク姿は、本物の欲求不満人妻や大人の女性を抱いているかのような生々しい没入感を与えてくれます。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "欲求不満度: 100% | 巨乳弾力度: 98% | 実用性: 98%"
        },
        "hmn00910": {
            "desc": """<h4>【作品解説・見どころ】五日市芽依のノーパン直穿き！滞在先ホテルで搾り取られる限界ハメ</h4>
<p>小悪魔的な可愛さと大胆なエロティシズムで人気の五日市芽依が、なんとノーパンで黒パンストを直穿きして接客するトンデモ航空のCAに扮した話題作。機内でのチラリズムで勃起させられた男性が、ホテルまで追いかけて部屋に押し入ると、彼女は何食わぬ顔で迎え入れます。ストッキングを透かして見える秘部を指先でなぞられた瞬間にびくびくと体を震わせる姿がエロすぎます。</p>
<h4>【実用ポイント】観光も忘れて翌朝まで生ハメ騎乗位で連続搾精</h4>
<p>滞在先の観光など一切目もくれず、ベッドの上で朝まで繰り広げられる濃厚な交わり。五日市芽依の柔らかく吸い付くような腰使いに翻弄され、射精してもなお「まだ帰りの分も出してもらわなきゃ困りますよ？」と笑顔でペニスを咥え直されるエンドレスな快楽地獄を味わえます。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "ノーパン着衣度: 100% | 騎乗位搾精度: 97% | 実用性: 97%"
        },
        "rprj00003": {
            "desc": """<h4>【作品解説・見どころ】本堂彩海の清楚なエアライン学生がドM覚醒！徹底調教の記録</h4>
<p>将来を嘱望された航空会社の訓練生・本堂彩海が、厳しい教官や男たちの要求に屈服し、内なるドMの雌へと開花していくドキュメンタリータッチの傑作。最初は規律正しい立ち振る舞いと清潔感あふれる笑顔を見せていた彼女が、執拗な身体検査と性感開発によって次第に快楽の奴隷へと堕ちていく心理描写が非常にリアルです。</p>
<h4>【実用ポイント】規律と恥辱の狭間でイキ狂う哀愁とエロティシズム</h4>
<p>制服を着たままで四つん這いにされ、お尻を突き出して後背位で奥まで抉られるシーンは必見。高貴なプライドが完全に粉砕され、涙と涎で顔をぐしゃぐしゃにしながら快楽を懇願する本堂彩海の体当たり演技は、見る者の男の本能を狂わせる凄まじい熱量を放っています。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "ドM開花度: 99% | 制服調教度: 98% | 実用性: 98%"
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
      <span class="bg-sky-600 text-white font-black text-sm px-3 py-1 rounded-lg">第{idx+1}位</span>
      <span class="text-xs text-slate-400 font-mono tracking-wider">品番: {cid.upper()}</span>
    </div>
    <div class="text-amber-400 font-black text-sm tracking-wide">{c_data.get('rating', '★★★★★ 5.0 / 5.0')}</div>
  </div>

  <h3 class="text-xl md:text-2xl font-black text-white leading-snug mb-4 hover:text-sky-400 transition">
    <a href="{aff_url}" target="_blank" rel="nofollow noopener">{title}</a>
  </h3>

  <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-start">
    <div class="md:col-span-5">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block group overflow-hidden rounded-xl border border-slate-700/80 shadow-lg relative">
        <img src="{large_img}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition duration-300 flex items-end p-4">
          <span class="bg-sky-600 text-white font-bold text-xs px-3 py-1.5 rounded-full shadow-lg">FANZA公式で今すぐ無料サンプル再生 ▶</span>
        </div>
      </a>
      <div class="mt-3 text-xs bg-slate-800/60 p-2.5 rounded-lg border border-slate-700/50 text-slate-300">
        <span class="text-slate-400">注目スコア：</span>
        <span class="font-bold text-amber-300">{c_data.get('service_score', '実用性抜群')}</span>
      </div>
    </div>

    <div class="md:col-span-7 space-y-4">
      <div class="space-y-1.5 text-xs text-slate-400">
        <div><strong class="text-slate-300">出演キャスト：</strong> {act_html or "単体トップ女優"}</div>
        <div><strong class="text-slate-300">収録ジャンル：</strong> {genre_html}</div>
        <div><strong class="text-slate-300">メーカー：</strong> {it.get('iteminfo', {}).get('maker', [{}])[0].get('name', 'FANZA独占')}</div>
      </div>

      <div class="text-slate-200 text-sm md:text-base leading-relaxed space-y-3 bg-slate-950/60 p-4 rounded-xl border border-slate-800/80">
        {c_data.get('desc', '')}
      </div>

      {sample_imgs_html}

      <div class="pt-2 flex flex-col sm:flex-row gap-3">
        <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="flex-1 text-center bg-gradient-to-r from-sky-600 to-blue-600 hover:from-sky-500 hover:to-blue-500 text-white font-black py-3 px-6 rounded-xl shadow-lg transform active:scale-95 transition">
          FANZAで本編を見る・無料サンプル動画 ▶
        </a>
        <a href="/posts/{cid}" class="text-center bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold py-3 px-4 rounded-xl border border-slate-700 transition">
          詳細レビュー
        </a>
      </div>
    </div>
  </div>
</div>"""
        html_parts.append(item_block)

    # 比較まとめテーブル
    summary_table = """
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-2xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-sky-400">📊</span> 【徹底比較】おすすめCA・客室乗務員AV神作スペック一覧表
  </h3>
  <div class="overflow-x-auto">
    <table class="w-full text-left text-xs md:text-sm text-slate-300 border-collapse">
      <thead>
        <tr class="border-b border-slate-700 bg-slate-800/80 text-white">
          <th class="p-3">順位</th>
          <th class="p-3">作品名 / 主演</th>
          <th class="p-3">シチュエーション</th>
          <th class="p-3">最大の見どころ・フェチ</th>
          <th class="p-3">公式リンク</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800">
        <tr>
          <td class="p-3 font-bold text-sky-400">第1位</td>
          <td class="p-3"><strong>snos00377</strong><br />河北彩花</td>
          <td class="p-3">甘えん坊CA彼女の変態開花</td>
          <td class="p-3">目隠し拘束×極上美貌のメス堕ち</td>
          <td class="p-3"><a href="/posts/snos00377" class="text-sky-400 underline">詳細を見る</a></td>
        </tr>
        <tr>
          <td class="p-3 font-bold text-sky-400">第2位</td>
          <td class="p-3"><strong>midv00530</strong><br />新ありな</td>
          <td class="p-3">黒パンスト美脚足フェチ調教</td>
          <td class="p-3">甘サド挑発からの濃厚騎乗位</td>
          <td class="p-3"><a href="/posts/midv00530" class="text-sky-400 underline">詳細を見る</a></td>
        </tr>
        <tr>
          <td class="p-3 font-bold text-sky-400">第3位</td>
          <td class="p-3"><strong>halt00066</strong><br />沙月ふみの</td>
          <td class="p-3">フライト先ホテル密会ハメ</td>
          <td class="p-3">高身長巨乳の欲求不満爆発交尾</td>
          <td class="p-3"><a href="/posts/halt00066" class="text-sky-400 underline">詳細を見る</a></td>
        </tr>
        <tr>
          <td class="p-3 font-bold text-sky-400">第4位</td>
          <td class="p-3"><strong>hmn00910</strong><br />五日市芽依</td>
          <td class="p-3">ノーパン直穿き黒パンスト接客</td>
          <td class="p-3">翌朝まで搾り取られるエンドレスSEX</td>
          <td class="p-3"><a href="/posts/hmn00910" class="text-sky-400 underline">詳細を見る</a></td>
        </tr>
        <tr>
          <td class="p-3 font-bold text-sky-400">第5位</td>
          <td class="p-3"><strong>rprj00003</strong><br />本堂彩海</td>
          <td class="p-3">エアライン学生のドM調教</td>
          <td class="p-3">制服着衣の後背位ピストンと涙の懇願</td>
          <td class="p-3"><a href="/posts/rprj00003" class="text-sky-400 underline">詳細を見る</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>"""
    html_parts.append(summary_table)

    # よくある質問 (FAQ)
    faq_html = """
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-2xl">
  <h3 class="text-xl md:text-2xl font-bold text-white mb-6 flex items-center gap-2">
    <span class="text-sky-400">❓</span> CA・客室乗務員シチュエーションに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-4 text-xs md:text-sm">
    <div class="border-b border-slate-800 pb-4">
      <h4 class="font-bold text-sky-300 mb-2">Q1. CAモノで一番実用度が高いポイントはどこですか？</h4>
      <p class="text-slate-300 leading-relaxed">やはり「黒パンスト美脚」と「制服着衣」のフェティシズムです。完全に脱がせるのではなく、タイトスカートをたくし上げ、パンストの股間部分を引き裂いて結合する生々しさは他のジャンルにはない唯一無二の興奮を生み出します。</p>
    </div>
    <div class="border-b border-slate-800 pb-4">
      <h4 class="font-bold text-sky-300 mb-2">Q2. 初めて見るならどの作品が一番おすすめですか？</h4>
      <p class="text-slate-300 leading-relaxed">まずは圧倒的なビジュアルと神がかった演技力を誇る第1位の河北彩花（snos00377）を強く推奨します。清楚な彼女がアブノーマルな快楽に溺れていく過程は、どんな性癖の男性でも絶対に満足できます。</p>
    </div>
    <div>
      <h4 class="font-bold text-sky-300 mb-2">Q3. スタイル抜群系とドS系、どちらが人気ですか？</h4>
      <p class="text-slate-300 leading-relaxed">足技や挑発を楽しみたい方は第2位の新ありな、濃厚な肉体美と包容力で抜きたい方は第3位の沙月ふみのや第4位の五日市芽依が抜群の人気を集めています。</p>
    </div>
  </div>
</div>"""
    html_parts.append(faq_html)

    related_links_html = """<div class="my-8 bg-slate-950 border border-slate-800 rounded-2xl p-6">
  <h4 class="text-base font-bold text-white mb-3">🔥 あわせて読みたい人気キラー特集</h4>
  <ul class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm text-sky-300">
    <li><a href="/posts/feature_fanza_pantyhose_slender_legs_ol_fetish_ranking" class="hover:underline">▶ 美脚パンスト・OLフェチランキングTOP5！オフィスの誘惑</a></li>
    <li><a href="/posts/feature_fanza_female_boss_office_overtime_hotel_ranking_2026" class="hover:underline">▶ 美人女上司・残業密室＆出張相部屋ランキングTOP5！下剋上交尾</a></li>
    <li><a href="/posts/feature_fanza_huge_ass_back_piston_ranking_2026" class="hover:underline">▶ 超巨尻・美尻×バック後背位ピストンランキングTOP5！顔面騎乗</a></li>
    <li><a href="/posts/feature_fanza_creampie_breeding_deep_ejaculation_ranking" class="hover:underline">▶ 生中出し・種付け解禁ランキングTOP5！膣奥に注ぎ込まれる白濁精液</a></li>
  </ul>
</div>"""
    html_parts.append(related_links_html)

    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "ItemList",
                "name": "CA・客室乗務員おすすめ神作ランキングTOP5",
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
                        "name": "CAモノで一番実用度が高いポイントはどこですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "黒パンスト美脚と制服着衣のフェティシズムです。タイトスカートをたくし上げパンストを破いて結合する生々しさは格別です。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "初めて見るならどの作品が一番おすすめですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "圧倒的なビジュアルと演技力を誇る第1位の河北彩花（snos00377）を強く推奨します。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "スタイル抜群系とドS系、どちらが人気ですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "足技や挑発を楽しみたい方は第2位の新ありな、濃厚な肉体美で抜きたい方は第3位の沙月ふみのが大人気です。"
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
        "id": "feature_fanza_cabin_attendant_flight_hotel_ranking_2026",
        "title": "【フライト先ホテルの禁断ステイ】FANZA「美人CA・客室乗務員」おすすめ神作ランキングTOP5！制服パンスト美脚と気品あふれる空の女神が理性を溶かす濃厚交尾AV選【2026年最新】",
        "date": "2026-10-04 12:30:00",
        "hinban": "CABIN-ATTENDANT-HOTEL-2026",
        "price": "300~",
        "maker": "FANZA公式セレクション",
        "actresses": ["河北彩花（河北彩伽）", "新ありな", "沙月ふみの", "五日市芽依", "本堂彩海"],
        "genres": ["キャビンアテンダント", "CA", "スチュワーデス", "美脚", "パンスト", "制服", "ホテル", "特集", "殿堂入り"],
        "image": cover_image,
        "review": full_html
    }

    file_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f" -> Successfully saved Article 1 ({char_count} chars) to {file_path}")


# ==============================================================================
# 記事2: 白衣の天使・ナース・看護師シチュエーション特化
# ==============================================================================
def generate_article_nurse():
    print("=== Generating Article 2: 白衣の天使・ナース特化 ===")
    cids = ["ssis00253", "1start00038", "midv00889", "dvaj00740", "1start00548"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["看護師", "ナース", "白衣", "入院", "夜勤"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 2 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-rose-950/40 via-slate-900 to-slate-950 border border-rose-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-rose-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-rose-500/20 text-rose-300 border border-rose-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">WHITE ANGEL NURSE SPECIAL</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月04日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【夜勤病室の献身ケアと背徳の密会】FANZA「美人ナース・看護師」おすすめ神作ランキングTOP5！清楚な白衣の下に隠した淫らな素顔に癒やされ尽くす極上入院AV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    怪我や病気で心身ともに弱っている入院患者にとって、優しく微笑みかけてくれる看護師はまさに地上に舞い降りた「白衣の天使」。しかし、消灯時間を過ぎてシンと静まり返った深夜の病棟、カーテン一枚で仕切られた薄暗いベッドサイドで、その清楚なナースが男の股間の熱狂を鎮めるために禁断のケアを施してくれるとしたら――これ以上の甘美な妄想が存在するでしょうか。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    ナースシチュエーションがAV界で不動のキラージャンルであり続ける秘密は、「献身的な奉仕」と「人目を忍ぶ背徳のスリル」の絶妙な調和にあります。「声を出したら他の患者さんにバレちゃいますよ」と耳元で囁かれながら行われる濃厚なフェラチオ、白衣をたくし上げて跨り、腰を静かにグラインドさせる密着騎乗位。普段の真面目な看護業務とのギャップが、男の脳内麻薬をドバドバと分泌させます。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、神乳・小宵こなんの失神必至パイズリケアから、紗倉まなの即尺夜勤フェラ、Himariの規格外Qカップ密着NTR、月野かすみの顔近スパイダー騎乗位ASMR、青空ひかりの院内人気ナース裏営業まで、FANZAレビュー星4.5超え・実用度満点の【白衣のナース神作TOP5】を徹底解説します。
  </p>
</div>

<!-- 選び方の基準 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-rose-400">💉</span> 失敗しないナースモノ選び！身も心もとろける3大チェックポイント
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-rose-300 mb-2">① 「医療ケア」という大義名分による奉仕</h4>
      <p class="text-slate-300 leading-relaxed">陰部洗浄や下半身の鬱血治療という名目で、恥じらいながらも丹念にペニスを手技や口技で介抱してくれる導入のリアリティが重要です。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-rose-300 mb-2">② カーテン越し・消灯後のサイレントエロス</h4>
      <p class="text-slate-300 leading-relaxed">同室の患者や他のナースの巡回を警戒し、声を出せない極限の緊張感の中で交わされる密着プレイが興奮を何倍にも増幅させます。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-rose-300 mb-2">③ ナース服・ナースキャップのコスチューム美</h4>
      <p class="text-slate-300 leading-relaxed">清潔感のあるピンクやホワイトのナース服から覗く柔らかな谷間、ストッキング美脚の生々しさが作品の完成度を完璧なものにします。</p>
    </div>
  </div>
</div>"""
    html_parts.append(intro_html)

    reviews_data_2 = {
        "ssis00253": {
            "desc": """<h4>【作品解説・見どころ】奇跡の神乳・小宵こなん！極上パイズリで骨抜きにされる特濃看護</h4>
<p>爆発的な人気を誇るトップ女優・小宵こなんが、患者の健康管理のために自慢の美巨乳を惜しみなく捧げる至福のナース作。白衣の胸元からこぼれ落ちそうなHカップの柔らかいバストで、硬く勃起したペニスを包み込み、温かいローションを絡めながら上下に激しく擦り上げるパイズリシーンはまさに絶景です。小宵こなんの甘くとろけるような笑顔と、「私の胸、気持ちいいですか…？」という愛らしい囁きに、我慢の限界を迎えない男はいません。</p>
<h4>【実用ポイント】挟射からの中出し結合！甘えん坊ナースの究極ご奉仕</h4>
<p>胸でたっぷりと射精させられた後、さらに火照った体を密着させて自らの秘部に肉棒を導き入れる小宵こなん。柔らかい肉壁で締め付けられながら、ベッドがきしむ音を響かせて腰を振る姿は、実用性の頂点を極めています。巨乳フェチ・奉仕好きなら絶対に視聴すべき金字塔です。</p>""",
            "rating": "★★★★★ 5.0 / 5.0",
            "service_score": "神乳パイズリ度: 100% | 癒やし奉仕度: 100% | 実用性: 100%"
        },
        "1start00038": {
            "desc": """<h4>【作品解説・見どころ】紗倉まなの人妻夜勤ナース！消灯時間を過ぎたら即尺の暴走痴女</h4>
<p>レジェンド女優・紗倉まなが、深夜の病棟で患者のペニスを狂ったようにしゃぶり尽くす濃厚夜勤ドラマ。消灯ラッパが鳴り終わると同時にベッドのカーテンを潜り込み、寝ている患者の布団をめくってペニスを即座に口内へ。ジュルジュルと音を立てながら喉奥深くまで咥え込む圧倒的なフェラチオ技術と、上目遣いで男の反応を伺う淫らな視線が凄まじい威力を誇ります。</p>
<h4>【実用ポイント】唾液まみれの貪欲ディープスロートと声漏れピストン</h4>
<p>「早く出してください、次の見回り来ちゃいますから…」と焦らしながらも、自ら激しく腰を動かして男をイカせようとする紗倉まな。一度繋がれば声を出せない状況下で激しいバックピストンが炸裂し、息を切らしながら歓喜の表情を浮かべる彼女の姿に完全にノックアウトされます。</p>""",
            "rating": "★★★★★ 4.9 / 5.0",
            "service_score": "即尺フェラ度: 100% | スリル度: 99% | 実用性: 99%"
        },
        "midv00889": {
            "desc": """<h4>【作品解説・見どころ】異次元のQカップ・Himari！妻の目を盗んで挟射堕ちさせられるNTR看護</h4>
<p>人間離れした超弩級Qカップの持ち主・Himariが、入院中の男性を肉欲の虜にして家庭崩壊へと導く背徳ナースドラマ。看病に訪れる妻の目の届かない隙を突き、巨大すぎるおっぱいで患者の顔面や下半身を包み込む圧倒的な質量攻撃。包容力という言葉では片付けられないほどの肉の温もりと重圧に、男の理性は完全に粉砕されます。</p>
<h4>【実用ポイント】肉の壁に埋もれる快感！圧倒的な巨乳密着交尾</h4>
<p>病室のベッドの上でHimariが跨り、巨大なバストを上下に波打たせながら腰を打ち付けるシーンは圧巻の迫力。視界のすべてがおっぱいで埋め尽くされ、愛液と汗が混ざり合う濃厚な結合に、鑑賞者も完全にノックアウトされます。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "爆乳質量度: 100% | 背徳NTR度: 98% | 実用性: 98%"
        },
        "dvaj00740": {
            "desc": """<h4>【作品解説・見どころ】月野かすみの超没入ASMR！顔近スパイダー騎乗位と淫語囁き</h4>
<p>繊細な演技と美しいルックスでファンを魅了する月野かすみが、深夜の病室で男の顔面に覆いかぶさりながら腰を振るASMR特化の超名作。耳元で生々しい吐息と淫語を囁きかけ、カーテン越しに他人に聞かれないようギリギリのトーンで話しかけてくる臨場感は鳥肌モノです。男の音や雑音が排除され、プレイ音と喘ぎ声だけに全集中できる音響設計も完璧です。</p>
<h4>【実用ポイント】密着スパイダー騎乗位による逃げ場のない快楽責め</h4>
<p>月野かすみが手足をベッドについて男の上に覆いかぶさり、至近距離で見つめ合いながら腰をくねらせるスパイダー騎乗位。結合部のクチュクチュという水音が耳元でダイレクトに響き渡り、視覚と聴覚の両方から脳を蕩けさせられます。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "ASMR没入度: 100% | 囁き淫語度: 98% | 実用性: 98%"
        },
        "1start00548": {
            "desc": """<h4>【作品解説・見どころ】青空ひかりの院内人気ナース！清楚な笑顔の下に隠した男漁りの裏の顔</h4>
<p>誰からも愛される院内のムードメーカー看護師・青空ひかり。昼間は笑顔を絶やさず献身的に働く彼女が、実は若くて元気な入院患者を密かに品定めし、夜の病室で性処理を施していたという極上シチュエーション。青空ひかりの透明感あふれる美少女フェイスと、ペニスを目の前にした途端に下品に舌を舐めずり回すギャップが男心を狂わせます。</p>
<h4>【実用ポイント】元気ハツラツ美少女が快楽に溺れてトロ顔へと崩れる瞬間</h4>
<p>診察室や当直室のデスクの上で足を広げられ、激しいピストンを受ける青空ひかり。普段の爽やかな笑顔が快楽の波によって完全に崩壊し、涎を垂らしながら白目を剥いてイキ狂う姿は、ギャップ萌え好きにはたまらない破壊力を持っています。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "清楚ギャップ度: 99% | 密室裏営業度: 98% | 実用性: 97%"
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
        <span class="text-slate-400">注目スコア：</span>
        <span class="font-bold text-amber-300">{c_data.get('service_score', '実用性抜群')}</span>
      </div>
    </div>

    <div class="md:col-span-7 space-y-4">
      <div class="space-y-1.5 text-xs text-slate-400">
        <div><strong class="text-slate-300">出演キャスト：</strong> {act_html or "単体トップ女優"}</div>
        <div><strong class="text-slate-300">収録ジャンル：</strong> {genre_html}</div>
        <div><strong class="text-slate-300">メーカー：</strong> {it.get('iteminfo', {}).get('maker', [{}])[0].get('name', 'FANZA独占')}</div>
      </div>

      <div class="text-slate-200 text-sm md:text-base leading-relaxed space-y-3 bg-slate-950/60 p-4 rounded-xl border border-slate-800/80">
        {c_data.get('desc', '')}
      </div>

      {sample_imgs_html}

      <div class="pt-2 flex flex-col sm:flex-row gap-3">
        <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="flex-1 text-center bg-gradient-to-r from-rose-600 to-pink-600 hover:from-rose-500 hover:to-pink-500 text-white font-black py-3 px-6 rounded-xl shadow-lg transform active:scale-95 transition">
          FANZAで本編を見る・無料サンプル動画 ▶
        </a>
        <a href="/posts/{cid}" class="text-center bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold py-3 px-4 rounded-xl border border-slate-700 transition">
          詳細レビュー
        </a>
      </div>
    </div>
  </div>
</div>"""
        html_parts.append(item_block)

    # 比較表
    summary_table = """
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-2xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-rose-400">📊</span> 【徹底比較】おすすめナース・看護師AV神作スペック一覧表
  </h3>
  <div class="overflow-x-auto">
    <table class="w-full text-left text-xs md:text-sm text-slate-300 border-collapse">
      <thead>
        <tr class="border-b border-slate-700 bg-slate-800/80 text-white">
          <th class="p-3">順位</th>
          <th class="p-3">作品名 / 主演</th>
          <th class="p-3">シチュエーション</th>
          <th class="p-3">最大の見どころ・フェチ</th>
          <th class="p-3">公式リンク</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800">
        <tr>
          <td class="p-3 font-bold text-rose-400">第1位</td>
          <td class="p-3"><strong>ssis00253</strong><br />小宵こなん</td>
          <td class="p-3">神乳パイズリによる極上看護</td>
          <td class="p-3">Hカップ挟射からの濃厚結合中出し</td>
          <td class="p-3"><a href="/posts/ssis00253" class="text-rose-400 underline">詳細を見る</a></td>
        </tr>
        <tr>
          <td class="p-3 font-bold text-rose-400">第2位</td>
          <td class="p-3"><strong>1start00038</strong><br />紗倉まな</td>
          <td class="p-3">消灯後の即尺フェラチオ夜勤</td>
          <td class="p-3">喉奥ディープスロート×背徳ピストン</td>
          <td class="p-3"><a href="/posts/1start00038" class="text-rose-400 underline">詳細を見る</a></td>
        </tr>
        <tr>
          <td class="p-3 font-bold text-rose-400">第3位</td>
          <td class="p-3"><strong>midv00889</strong><br />Himari</td>
          <td class="p-3">超弩級Qカップ密着NTR看護</td>
          <td class="p-3">妻の目を盗んだ規格外バスト圧搾SEX</td>
          <td class="p-3"><a href="/posts/midv00889" class="text-rose-400 underline">詳細を見る</a></td>
        </tr>
        <tr>
          <td class="p-3 font-bold text-rose-400">第4位</td>
          <td class="p-3"><strong>dvaj00740</strong><br />月野かすみ</td>
          <td class="p-3">顔近スパイダー騎乗位ASMR</td>
          <td class="p-3">耳元囁き淫語と静かな病室の水音</td>
          <td class="p-3"><a href="/posts/dvaj00740" class="text-rose-400 underline">詳細を見る</a></td>
        </tr>
        <tr>
          <td class="p-3 font-bold text-rose-400">第5位</td>
          <td class="p-3"><strong>1start00548</strong><br />青空ひかり</td>
          <td class="p-3">人気看護師の秘密の裏営業</td>
          <td class="p-3">清楚笑顔が崩れ落ちる診察台ハメ</td>
          <td class="p-3"><a href="/posts/1start00548" class="text-rose-400 underline">詳細を見る</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>"""
    html_parts.append(summary_table)

    # FAQ
    faq_html = """
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-2xl">
  <h3 class="text-xl md:text-2xl font-bold text-white mb-6 flex items-center gap-2">
    <span class="text-rose-400">❓</span> ナース・看護師AVに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-4 text-xs md:text-sm">
    <div class="border-b border-slate-800 pb-4">
      <h4 class="font-bold text-rose-300 mb-2">Q1. ナースモノの最大の抜きどころは何ですか？</h4>
      <p class="text-slate-300 leading-relaxed">「病室という静寂の密室」で「献身的な看護ケア」を装って行われる行為そのものです。声を出せない状況下で布団の中で行われる手技やフェラチオ、そして密着騎乗位は、男性の妄想を極限まで掻き立てます。</p>
    </div>
    <div class="border-b border-slate-800 pb-4">
      <h4 class="font-bold text-rose-300 mb-2">Q2. 巨乳系とテクニック系、どちらがおすすめですか？</h4>
      <p class="text-slate-300 leading-relaxed">包容力とおっぱいでの癒やしを求めるなら第1位の小宵こなんや第3位のHimari、生々しいフェラや臨場感を味わいたいなら第2位の紗倉まなや第4位の月野かすみが最適です。</p>
    </div>
    <div>
      <h4 class="font-bold text-rose-300 mb-2">Q3. VR版と通常版、どちらが楽しめますか？</h4>
      <p class="text-slate-300 leading-relaxed">通常版は精緻なアングルとドラマ性が魅力でじっくり抜くのに適しています。病室の臨場感を肌で味わいたい方は本作のような通常高画質配信を大画面で鑑賞するのが最もおすすめです。</p>
    </div>
  </div>
</div>"""
    html_parts.append(faq_html)

    related_links_html = """<div class="my-8 bg-slate-950 border border-slate-800 rounded-2xl p-6">
  <h4 class="text-base font-bold text-white mb-3">🔥 あわせて読みたい人気キラー特集</h4>
  <ul class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm text-rose-300">
    <li><a href="/posts/feature_fanza_mens_esthe_secret_massage_ranking" class="hover:underline">▶ メンズエステ密着施術ランキングTOP5！オイルまみれの禁断ご奉仕</a></li>
    <li><a href="/posts/feature_fanza_luxury_soapland_foam_mat_play_ranking_2026" class="hover:underline">▶ 高級ソープ泡踊り＆マットプレイ神作TOP5！全身密着の究極洗体</a></li>
    <li><a href="/posts/feature_fanza_busty_huge_tits_masterpieces_ranking" class="hover:underline">▶ 爆乳・巨乳AV名作ランキングTOP5！揺れる神乳と圧倒的パイズリ</a></li>
    <li><a href="/posts/feature_fanza_squirt_climax_convulsion_best_ranking" class="hover:underline">▶ 潮吹き・絶頂痙攣ランキングTOP5！快楽の限界を突破する連続アクメ</a></li>
  </ul>
</div>"""
    html_parts.append(related_links_html)

    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "ItemList",
                "name": "美人ナース・看護師おすすめ神作ランキングTOP5",
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
                        "name": "ナースモノの最大の抜きどころは何ですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "静寂の密室で看護ケアを装って行われる行為です。声を出せない状況下でのフェラチオや騎乗位が極限の興奮を生みます。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "巨乳系とテクニック系、どちらがおすすめですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "おっぱいの癒やしなら第1位の小宵こなん、フェラや臨場感なら第2位の紗倉まなや第4位の月野かすみが最適です。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "VR版と通常版、どちらが楽しめますか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "精緻なアングルとドラマ性をじっくり味わうなら通常高画質配信を大画面で鑑賞するのが最もおすすめです。"
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
        "id": "feature_fanza_nurse_hospital_secret_care_ranking_2026",
        "title": "【夜勤病室の献身ケアと背徳の密会】FANZA「美人ナース・看護師」おすすめ神作ランキングTOP5！清楚な白衣の下に隠した淫らな素顔に癒やされ尽くす極上入院AV選【2026年最新】",
        "date": "2026-10-04 12:45:00",
        "hinban": "NURSE-HOSPITAL-CARE-2026",
        "price": "300~",
        "maker": "FANZA公式セレクション",
        "actresses": ["小宵こなん", "紗倉まな", "Himari", "月野かすみ", "青空ひかり"],
        "genres": ["看護師", "ナース", "白衣", "入院", "夜勤", "パイズリ", "フェラ", "騎乗位", "特集", "殿堂入り"],
        "image": cover_image,
        "review": full_html
    }

    file_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f" -> Successfully saved Article 2 ({char_count} chars) to {file_path}")


# ==============================================================================
# 記事3: 美人家庭教師・女子大生カテキョ密室指導特化
# ==============================================================================
def generate_article_home_tutor():
    print("=== Generating Article 3: 美人家庭教師・密室個人レッスン特化 ===")
    cids = ["midv00553", "sone00968", "pred00889", "ipzz00944", "miab00110"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["家庭教師", "女子大生", "個人指導", "密室", "勉強部屋"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 3 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-emerald-950/40 via-slate-900 to-slate-950 border border-emerald-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">PRIVATE HOME TUTOR SPECIAL</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月04日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【二人きりの勉強部屋で始まる大人の授業】FANZA「美人家庭教師・密室個人レッスン」おすすめ神作ランキングTOP5！清楚な知性派美女が教え子と貪り合う背徳の中出しAV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    思春期の少年時代、あるいは大人の男になっても決して色褪せない甘酸っぱく背徳的な憧れ、それが「美人家庭教師との禁断の密室シチュエーション」です。机を並べて座り、ノートを指差すたびにふわりと漂うシャンプーの香りや柔軟剤の匂い。かがみ込んだ胸元からチラリと覗く柔らかな谷間、太もも同士が偶然触れ合った瞬間の心臓の跳ね上がり――勉強に集中できるはずのない極上の誘惑がそこにあります。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    家庭教師モノが持つ最高の醍醐味は、「指導する側とされる側」という立場を巧みに利用したエロティックな駆け引きです。「勉強を頑張ったご褒美をあげる」「大人のキスを教えてあげる」と優しく導いてくれるお姉さん系から、教え子の抑えきれない男らしさに押し倒されてメスへと堕ちていく知的美女まで、密室という逃げ場のない空間で交わされる濃密な情事は実用性抜群です。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、大人気女優・神宮寺ナオの両親不在7日間中出し合宿から、紫堂るいのグラドル級Iカップ誘惑レッスン、三好佑香のベロキス童貞搾取、白石るなの優しすぎる中出し救済、そして皆月ひかる＆都崎あやめの嫉妬接吻レクチャーまで、FANZAレビュー高評価・屈指の興奮を誇る【美人家庭教師神作TOP5】を徹底紹介します。
  </p>
</div>

<!-- 選び方の基準 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-emerald-400">📖</span> 失敗しない家庭教師モノ選び！勉強部屋で熱狂できる3大チェックポイント
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-emerald-300 mb-2">① 知的な眼鏡・清楚スタイルと無防備な胸元</h4>
      <p class="text-slate-300 leading-relaxed">知的で真面目な雰囲気を漂わせながらも、教える姿勢で胸元や太ももが無防備に露出する日常の隙が男心を激しく揺さぶります。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-emerald-300 mb-2">② 隣の部屋に家族がいるかもしれないスリル</h4>
      <p class="text-slate-300 leading-relaxed">両親がリビングにいる状況でドア一枚隔てて行われる声漏れ厳禁の密会や、留守中の完全二人きりの解放感の演出が鍵となります。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-emerald-300 mb-2">③ 優しく手解きしてくれるご褒美エロス</h4>
      <p class="text-slate-300 leading-relaxed">「テストの点数が上がったら」「勉強頑張ったら」と段階的にエスカレートしていく接吻や手技のご褒美描写が最高のカタルシスを生みます。</p>
    </div>
  </div>
</div>"""
    html_parts.append(intro_html)

    reviews_data_3 = {
        "midv00553": {
            "desc": """<h4>【作品解説・見どころ】神宮寺ナオが魅せる！両親不在の1週間・24時間濃厚中出し合宿</h4>
<p>美しさと狂気的な色気を併せ持つトップ女優・神宮寺ナオが、両親が旅行で留守にしている教え子の家に泊まり込みで指導を行う夢のようなシチュエーション。最初は真面目に教えていた彼女ですが、二人きりの解放感と教え子の若々しいペニスに目を奪われ、徐々に逆痴女へと豹変。朝から晩まで勉強机の上、リビングのソファ、風呂場と家中どこでもペニスを咥え込み、搾り取るように中出しを貪り続けます。</p>
<h4>【実用ポイント】骨抜きにされるまで続く極上の連続射精管理</h4>
<p>神宮寺ナオの吸い付くようなディープキスと、愛液でぐちょぐちょになった秘部で幾度も激しく腰を振る騎乗位は圧巻。教え子がイッても決して離さず、「まだ出せるでしょ？先生に全部頂戴…」と微笑みながら腰をくねらせる姿は、男の精力を根こそぎ奪い去る超ド級の実用性です。</p>""",
            "rating": "★★★★★ 5.0 / 5.0",
            "service_score": "逆痴女度: 100% | 連続中出し度: 100% | 実用性: 100%"
        },
        "sone00968": {
            "desc": """<h4>【作品解説・見どころ】グラドル級Iカップ紫堂るい！おっぱいが気になって勉強どころじゃない</h4>
<p>規格外の天然Iカップ巨乳を誇る紫堂るいが家庭教師としてやってくる、全男子学生の夢を映像化した傑作。薄手のサマーニットを押し上げるように主張する巨大なバスト、かがみ込むたびに目の前に迫る深い谷間に、生徒は勉強どころではありません。その視線に気づいた紫堂るいが、「ふふ、気になっちゃう？じゃあ触りながら勉強する？」と悪戯っぽく微笑んで胸を差し出すシーンは失神必至の破壊力です。</p>
<h4>【実用ポイント】巨大バストでペニスを包み込む極楽パイズリと密着正常位</h4>
<p>柔らかなおっぱいに顔を埋められ、息ができなくなるほどの抱擁感の中で行われるパイズリは至福のひと言。そのままベッドに押し倒され、豊満な肉体を揺らしながら奥深くまで貫かれる紫堂るいの恍惚の表情は、巨乳好きなら昇天間違いなしのクオリティです。</p>""",
            "rating": "★★★★★ 4.9 / 5.0",
            "service_score": "Iカップ破壊力: 100% | 悪戯誘惑度: 98% | 実用性: 99%"
        },
        "pred00889": {
            "desc": """<h4>【作品解説・見どころ】三好佑香の濃厚ベロキス！腰ガク射精する童貞生徒を弄ぶ痴女先生</h4>
<p>妖艶な美貌と確かな演技力で人気の三好佑香が、童貞生徒の初々しい反応を面白がりながら弄び尽くす官能レッスン。唾液をダラダラと垂らしながら舌を奥深くまで絡め取るベロキスで生徒の理性を完全に狂わせます。キスだけで我慢できずに腰をガクガク震わせる生徒を優しく包み込み、「可愛い…もっと先生のこと気持ちよくして？」と肉棒を自らの濡れそぼった秘部へと導きます。</p>
<h4>【実用ポイント】耳元への甘い吐息と何度も中出しさせる貪欲ピストン</h4>
<p>三好佑香の蕩けきった表情と、激しく腰を打ち付けられて「んあっ、そこダメぇ！」と嬌声を上げる生々しい反応がファンの心を鷲掴みに。童貞を卒業させると同時に肉欲の虜にしてしまう背徳のドラマ性は、大人のエンタメとして完璧な仕上がりです。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "ベロキス粘度: 100% | 童貞開発度: 99% | 実用性: 98%"
        },
        "ipzz00944": {
            "desc": """<h4>【作品解説・見どころ】白石るなの聖母のような優しさ！女性不信の僕を癒やしてくれた中出しレッスン</h4>
<p>透明感あふれる美貌と穏やかな雰囲気が魅力の白石るなが、過去のトラウマから女性不信になってしまった引きこもりの生徒を温かく包み込む純愛エロス。「先生のこと、卒業まで本当の恋人だと思っていいよ」と優しく微笑み、傷ついた少年の心と身体を全身全霊で癒やしていきます。優しく包み込むようなフェラチオと、慈愛に満ちた眼差しで見つめられながらの交わりは涙が出るほど感動的です。</p>
<h4>【実用ポイント】心の通い合った濃厚結合と生々しい中出しの温もり</h4>
<p>ただ抜くだけでなく、深い愛情と信頼関係の上で交わされるセックスだからこそ、射精時のカタルシスが桁違いに跳ね上がります。正常位でしっかりと抱き合い、奥深くに精液を注ぎ込まれた瞬間に白石るなが見せる幸福感に満ちた表情は必見です。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "包容力・癒やし: 100% | 慈愛エロス: 98% | 実用性: 98%"
        },
        "miab00110": {
            "desc": """<h4>【作品解説・見どころ】皆月ひかる＆都崎あやめ！女子大生カテキョの接吻指導を見つめる妹</h4>
<p>人気美少女・皆月ひかると都崎あやめが共演するシチュエーションの傑作。優秀な女子大生家庭教師・都崎あやめから、毎日勉強部屋で濃厚な接吻レクチャーを受けてどんどんエッチが上達していくお兄ちゃん。その密室の様子を、嫉妬に燃える妹・皆月ひかるがドアの隙間から息を呑んで見つめるという、二重の背徳感がたまらない名作です。</p>
<h4>【実用ポイント】唾液が糸を引く濃密キスと姉妹・生徒のハーレム展開</h4>
<p>知的な都崎あやめの情熱的なディープキスと、それに負けじと身体を寄せてくる皆月ひかるの可愛らしさ。二人の極上美女に挟まれ、順番にフェラチオを受けたり腰を振ったりする贅沢極まりないシーンは、ハーレム・背徳好きにとっての至宝です。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "接吻レクチャー度: 100% | 嫉妬背徳度: 97% | 実用性: 98%"
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
      <span class="bg-emerald-600 text-white font-black text-sm px-3 py-1 rounded-lg">第{idx+1}位</span>
      <span class="text-xs text-slate-400 font-mono tracking-wider">品番: {cid.upper()}</span>
    </div>
    <div class="text-amber-400 font-black text-sm tracking-wide">{c_data.get('rating', '★★★★★ 5.0 / 5.0')}</div>
  </div>

  <h3 class="text-xl md:text-2xl font-black text-white leading-snug mb-4 hover:text-emerald-400 transition">
    <a href="{aff_url}" target="_blank" rel="nofollow noopener">{title}</a>
  </h3>

  <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-start">
    <div class="md:col-span-5">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block group overflow-hidden rounded-xl border border-slate-700/80 shadow-lg relative">
        <img src="{large_img}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition duration-300 flex items-end p-4">
          <span class="bg-emerald-600 text-white font-bold text-xs px-3 py-1.5 rounded-full shadow-lg">FANZA公式で今すぐ無料サンプル再生 ▶</span>
        </div>
      </a>
      <div class="mt-3 text-xs bg-slate-800/60 p-2.5 rounded-lg border border-slate-700/50 text-slate-300">
        <span class="text-slate-400">注目スコア：</span>
        <span class="font-bold text-amber-300">{c_data.get('service_score', '実用性抜群')}</span>
      </div>
    </div>

    <div class="md:col-span-7 space-y-4">
      <div class="space-y-1.5 text-xs text-slate-400">
        <div><strong class="text-slate-300">出演キャスト：</strong> {act_html or "単体トップ女優"}</div>
        <div><strong class="text-slate-300">収録ジャンル：</strong> {genre_html}</div>
        <div><strong class="text-slate-300">メーカー：</strong> {it.get('iteminfo', {}).get('maker', [{}])[0].get('name', 'FANZA独占')}</div>
      </div>

      <div class="text-slate-200 text-sm md:text-base leading-relaxed space-y-3 bg-slate-950/60 p-4 rounded-xl border border-slate-800/80">
        {c_data.get('desc', '')}
      </div>

      {sample_imgs_html}

      <div class="pt-2 flex flex-col sm:flex-row gap-3">
        <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="flex-1 text-center bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-black py-3 px-6 rounded-xl shadow-lg transform active:scale-95 transition">
          FANZAで本編を見る・無料サンプル動画 ▶
        </a>
        <a href="/posts/{cid}" class="text-center bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold py-3 px-4 rounded-xl border border-slate-700 transition">
          詳細レビュー
        </a>
      </div>
    </div>
  </div>
</div>"""
        html_parts.append(item_block)

    # 比較表
    summary_table = """
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-2xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-emerald-400">📊</span> 【徹底比較】おすすめ家庭教師AV神作スペック一覧表
  </h3>
  <div class="overflow-x-auto">
    <table class="w-full text-left text-xs md:text-sm text-slate-300 border-collapse">
      <thead>
        <tr class="border-b border-slate-700 bg-slate-800/80 text-white">
          <th class="p-3">順位</th>
          <th class="p-3">作品名 / 主演</th>
          <th class="p-3">シチュエーション</th>
          <th class="p-3">最大の見どころ・フェチ</th>
          <th class="p-3">公式リンク</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800">
        <tr>
          <td class="p-3 font-bold text-emerald-400">第1位</td>
          <td class="p-3"><strong>midv00553</strong><br />神宮寺ナオ</td>
          <td class="p-3">両親不在7日間の逆痴女中出し合宿</td>
          <td class="p-3">骨抜きにされる連続射精管理騎乗位</td>
          <td class="p-3"><a href="/posts/midv00553" class="text-emerald-400 underline">詳細を見る</a></td>
        </tr>
        <tr>
          <td class="p-3 font-bold text-emerald-400">第2位</td>
          <td class="p-3"><strong>sone00968</strong><br />紫堂るい</td>
          <td class="p-3">天然Iカップおっぱい誘惑指導</td>
          <td class="p-3">視界を埋め尽くす極楽パイズリと結合</td>
          <td class="p-3"><a href="/posts/sone00968" class="text-emerald-400 underline">詳細を見る</a></td>
        </tr>
        <tr>
          <td class="p-3 font-bold text-emerald-400">第3位</td>
          <td class="p-3"><strong>pred00889</strong><br />三好佑香</td>
          <td class="p-3">唾液ダラダラ濃厚ベロキスレッスン</td>
          <td class="p-3">童貞生徒を弄ぶ妖艶痴女ピストン</td>
          <td class="p-3"><a href="/posts/pred00889" class="text-emerald-400 underline">詳細を見る</a></td>
        </tr>
        <tr>
          <td class="p-3 font-bold text-emerald-400">第4位</td>
          <td class="p-3"><strong>ipzz00944</strong><br />白石るな</td>
          <td class="p-3">聖母のような優しさで包む中出し救済</td>
          <td class="p-3">心の通い合った情熱的正常位交尾</td>
          <td class="p-3"><a href="/posts/ipzz00944" class="text-emerald-400 underline">詳細を見る</a></td>
        </tr>
        <tr>
          <td class="p-3 font-bold text-emerald-400">第5位</td>
          <td class="p-3"><strong>miab00110</strong><br />皆月ひかる・都崎あやめ</td>
          <td class="p-3">接吻レクチャーと嫉妬妹の視線</td>
          <td class="p-3">美女二人に挟まれた贅沢ハーレムハメ</td>
          <td class="p-3"><a href="/posts/miab00110" class="text-emerald-400 underline">詳細を見る</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>"""
    html_parts.append(summary_table)

    # FAQ
    faq_html = """
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-2xl">
  <h3 class="text-xl md:text-2xl font-bold text-white mb-6 flex items-center gap-2">
    <span class="text-emerald-400">❓</span> 家庭教師AVに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-4 text-xs md:text-sm">
    <div class="border-b border-slate-800 pb-4">
      <h4 class="font-bold text-emerald-300 mb-2">Q1. 家庭教師モノの最大の抜きどころは何ですか？</h4>
      <p class="text-slate-300 leading-relaxed">「勉強を教えるという日常のすぐ隣にある背徳感」です。机を並べて座り、ノートの上で手が重なり合う緊張感から、一気にベッドや机の上で激しく求め合う展開への爆発力が最大の魅力です。</p>
    </div>
    <div class="border-b border-slate-800 pb-4">
      <h4 class="font-bold text-emerald-300 mb-2">Q2. お姉さん痴女系と清楚癒やし系、どちらが人気ですか？</h4>
      <p class="text-slate-300 leading-relaxed">どちらも絶大な支持があります。骨抜きにされたいドM気質の方は第1位の神宮寺ナオや第3位の三好佑香、包容力と優しい愛撫に包まれたい方は第2位の紫堂るいや第4位の白石るなが鉄板です。</p>
    </div>
    <div>
      <h4 class="font-bold text-emerald-300 mb-2">Q3. 作品選びで失敗しないためのポイントは？</h4>
      <p class="text-slate-300 leading-relaxed">シチュエーション設定がしっかり作り込まれている単体トップ女優作を選ぶことです。本記事で紹介した5作品はどれもレビュー星4.8以上を獲得している折り紙付きの名作ばかりですので安心して選んでいただけます。</p>
    </div>
  </div>
</div>"""
    html_parts.append(faq_html)

    related_links_html = """<div class="my-8 bg-slate-950 border border-slate-800 rounded-2xl p-6">
  <h4 class="text-base font-bold text-white mb-3">🔥 あわせて読みたい人気キラー特集</h4>
  <ul class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm text-emerald-300">
    <li><a href="/posts/feature_fanza_teasing_sister_devilish_seduction_ranking_2026" class="hover:underline">▶ 小悪魔妹の無邪気な誘惑ランキングTOP5！一つ屋根の下の禁断生活</a></li>
    <li><a href="/posts/feature_fanza_female_teacher_school_guidance_ranking" class="hover:underline">▶ 美人女教師・放課後指導ランキングTOP5！職員室と教室の秘密</a></li>
    <li><a href="/posts/feature_fanza_subjective_pov_whispering_masturbation_support_ranking_2026" class="hover:underline">▶ 完全主観オナサポランキングTOP5！ゼロ距離囁き淫語</a></li>
    <li><a href="/posts/feature_fanza_creampie_breeding_deep_ejaculation_ranking" class="hover:underline">▶ 生中出し・種付け解禁ランキングTOP5！膣奥に注ぎ込まれる白濁精液</a></li>
  </ul>
</div>"""
    html_parts.append(related_links_html)

    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "ItemList",
                "name": "美人家庭教師おすすめ神作ランキングTOP5",
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
                        "name": "家庭教師モノの最大の抜きどころは何ですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "勉強を教える日常のすぐ隣にある背徳感です。ノートの上で手が重なり合う緊張感から激しい交わりへの展開が魅力です。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "お姉さん痴女系と清楚癒やし系、どちらが人気ですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "骨抜きにされたいなら第1位の神宮寺ナオ、包容力と愛撫に包まれたいなら第2位の紫堂るいや第4位の白石るなが鉄板です。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "作品選びで失敗しないためのポイントは？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "シチュエーション設定が作り込まれている単体トップ女優作を選ぶことです。"
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
        "id": "feature_fanza_home_tutor_private_lesson_seduction_ranking_2026",
        "title": "【二人きりの勉強部屋で始まる大人の授業】FANZA「美人家庭教師・密室個人レッスン」おすすめ神作ランキングTOP5！清楚な知性派美女が教え子と貪り合う背徳の中出しAV選【2026年最新】",
        "date": "2026-10-04 13:00:00",
        "hinban": "HOME-TUTOR-PRIVATE-LESSON-2026",
        "price": "300~",
        "maker": "FANZA公式セレクション",
        "actresses": ["神宮寺ナオ", "紫堂るい", "三好佑香", "白石るな", "皆月ひかる", "都崎あやめ"],
        "genres": ["家庭教師", "女子大生", "個人指導", "密室", "勉強部屋", "逆痴女", "ベロキス", "中出し", "特集", "殿堂入り"],
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
    generate_article_cabin_attendant()
    print("--------------------------------------------------")
    generate_article_nurse()
    print("--------------------------------------------------")
    generate_article_home_tutor()
    print("==================================================")
    print("3記事すべての生成が正常に完了しました！")
    print("==================================================")

if __name__ == "__main__":
    main()
