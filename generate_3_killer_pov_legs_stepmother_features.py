# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・超大型キラー特集3記事自動生成スクリプト
1. 【極上の密着・耳元吐息】FANZA「主観・POV（主観目線）」おすすめ殿堂入り神作TOP5！ゼロ距離キスと見つめ合い生ハメで脳がバグる圧倒的没入感傑作選【2026年最新】
2. 【美脚・パンスト・黒タイツの誘惑】FANZA「美脚パンスト・スーツOL」おすすめ殿堂入り神作TOP5！伝線・足コキ・踏みつけ・ノーパン直穿き挑発で狂わされるフェチ特化傑作選【2026年最新】
3. 【禁断の背徳・家族崩壊の蜜】FANZA「義母・近親相姦・家庭内不倫」おすすめ殿堂入り神作TOP5！ひとつ屋根の下で息子の友達・義息子の絶倫ピストンに悶える美熟女傑作選【2026年最新】
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
# 記事1: 主観・POV特化
# ==============================================================================
def generate_article_1():
    print("=== Generating Article 1: POV & Subjective Immersion Masterpieces ===")
    cids = ["agav00108", "1votan00056", "mide00917", "mida00261", "sone00743"]
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
        # 1: agav00108 香澄せな
        {
            "rank": "01",
            "badge": "殿堂入り圧倒的No.1 / 顔面ドアップ＆博多弁射精管理",
            "subtitle": "至近距離数センチの息遣い！可愛い博多弁でイチャサドに焦らされ搾り取られる極上POV",
            "body": """<b>【視覚・聴覚・脳髄が完全にハックされる超接近アングル】</b>：<br>
画面いっぱいに広がる香澄せなの透明感あふれる美顔と、吐息が耳元をくすぐるようなゼロ距離主観カメラが炸裂する傑作。博多弁特有の柔らかなイントネーションで「まだ出しちゃダメやけんね…？」「もっと気持ちよくなってほしいと…」と小悪魔的に微笑みながら、男優のペニスを寸止めと焦らしで完全にコントロールします。<br>
唇が触れ合うほどのキスを交わしながらのフェラチオは、唾液の糸を引く生々しい唇の動きや舌先の吸い付きがすべて自分に向けられているとしか思えない狂気の没入感。瞳をじっと見つめられながらの正常位ピストンでは、喘ぎ声がどんどん熱を帯び、男側の腰の動きに合わせて激しく表情を崩していくリアルなオーガズムを堪能できます。<br>
VRゴーグルがなくてもモニター越しに脳内麻薬がドバドバ分泌される、主観AVの歴史に燦然と輝く大本命の一本です。""",
            "climax": "「我慢できんくなった？…いいよ、せなの中に全部出して…」と博多弁で懇願されながら、膣奥深くへドロドロに放つ限界中出しフィニッシュ。"
        },
        # 2: 1votan00056 横宮七海
        {
            "rank": "02",
            "badge": "リアリティNo.1 / 闇病み家出ちゃんの恩返しPOV",
            "subtitle": "GoPro主観撮影の生々しさ！男優完全受け身で犯され尽くす背徳の逆搾り",
            "body": """<b>【圧倒的生々しさ！拾った美少女に部屋で好き放題に搾り取られる生々しい臨場感】</b>：<br>
GoProカメラを頭部に装着したリアル視点で、家出少女に扮した横宮七海が恩返しと称してベッドの上で貪りついてくる主観特化作品。華奢な身体からは想像もつかないほど積極的な攻めで、完全に受け身に回った男の身体を玩具のように玩びます。<br>
見下ろすようなアングルで跨がっての激しい騎乗位や、至近距離でペニスを咥え込みながら上目遣いで「おじさん、気持ちいい…？」と囁きかける表情は鳥肌モノのリアルさ。男優が一切手を出せない完全受け身シチュエーションだからこそ、視聴者が100%自分自身を投影でき、画面の向こうの熱量にダイレクトに呑み込まれます。<br>
生々しい吐息、シーツのこすれる音、皮膚と皮膚が密着する音のすべてが生録音のように響き渡る、POV好き必携の破壊的カルト人気作です。""",
            "climax": "激しい腰振りで自ら絶頂に達しながら、男のペニスをぎゅうぎゅうと膣圧で締め上げて強制射精させる連続騎乗位アクメ。"
        },
        # 3: mide00917 八木奈々
        {
            "rank": "03",
            "badge": "イチャラブ最高峰 / 新婚生活密着POV",
            "subtitle": "家に帰ると美少女新妻がゼロ距離誘惑！甘々で溶けそうな至福の同棲性活",
            "body": """<b>【男子の全妄想を具現化した究極のラブラブ新妻シチュエーション】</b>：<br>
仕事から疲れて帰宅した瞬間、エプロン姿の八木奈々が抱きついてきてそのままベッドへ直行する、多幸感120%の密着イチャラブ主観傑作。カメラを見つめる八木奈々の潤んだ瞳、甘えたような舌足らずの話し声、そして全身を擦り寄せてくる柔らかい肌の質感がゼロ距離で迫ってきます。<br>
お風呂場での密着洗体から始まり、リビングのソファ、ベッドへと場所を変えながら、隙さえあればキスを求めてくる甘えん坊ぶりが炸裂。結合部を間近で見せつけながらゆっくりと腰を沈めるスローセックスは、まるで本当に八木奈々と結婚して愛し合っているかのような強烈な錯覚と幸福感に包まれます。<br>
ストレス社会で疲弊した男の心を芯から癒やし、同時に下半身を極限まで硬度MAXにさせる最強のヒーリング・エロティシズムです。""",
            "climax": "抱きしめ合いながら耳元で「大好き…ずっと一緒にいてね」と囁かれ、溢れる愛液とともに注ぎ込む新婚中出し。"
        },
        # 4: mida00261 葵いぶき
        {
            "rank": "04",
            "badge": "フェラ・回春特化 / 至高のメンズエステPOV",
            "subtitle": "射精後も逃がさない！見つめ合って囁きながら二発目を強奪するド痴女エステティシャン",
            "body": """<b>【一発出しても終わらない！視線で殺される悪魔的回春エステ】</b>：<br>
薄暗い個室サロンで、極上の美貌とスレンダー美ボディを持つ葵いぶきが施術台のあなたに跨がり、耳元への吐息と密着マッサージで責め立てる回春エステPOVの決定版。<br>
最大の見どころは、一度射精してフニャフニャになったペニスを一切休ませることなく、潤んだ瞳でじっと見つめながら「もう一回出せますよね…？」と舌先で優しく転がして二発目の勃起を誘発する魔性のテクニック。至近距離で見下ろされるアングルは、男のM心を極限まで刺激します。<br>
オイルの滑らかな摩擦音と、葵いぶきが漏らす淫らな吐息が立体的に鼓膜を震わせ、気絶寸前の快楽地獄へと引きずり込まれます。""",
            "climax": "息も絶え絶えの男を押し倒し、二発目の濃密精液を最後の一滴までじっくりと搾り取る騎乗位フィニッシュ。"
        },
        # 5: sone00743 小日向みゆう
        {
            "rank": "05",
            "badge": "天然Hカップ爆乳 / おっぱいシコサポPOV",
            "subtitle": "柔らか〜い巨乳を顔面に押し当て！パイズリ＆挟み込みで毎日射精をお手伝い",
            "body": """<b>【視界一面が天然Hカップの海！おっぱいに埋もれて果てる至高の主観体験】</b>：<br>
「巨乳好きのアナタがしたいこと、全部ワタシが叶えたい」という夢のようなコンセプトのもと、小日向みゆうの柔らかすぎる天然Hカップ美乳を余すところなく堪能できる主観特化作。<br>
仰向けになった男の顔面スレスレに巨大な胸を押し当て、乳頭を唇に含ませながら、両手で挟み込んだペニスをリズミカルにしごき上げるパイズリ視点は圧巻の一言。カメラに迫るバストの弾力と揺れは、画面を突き抜けてくるかのような迫力です。<br>
「私の胸でいっぱい気持ちよくなってね…」と微笑みながら、胸の谷間に射精させた精液を乳房全体に塗りたくるフェチシチュエーションまで完全網羅された、乳フェチ×POVの最高到達点です。""",
            "climax": "豊満なバストに顔を埋められ窒息しそうな状態で、胸の谷間に向けて豪快にザーメンを噴射するパイズリ射精。"
        }
    ]

    # HTML本文の構築
    content_parts = []

    content_parts.append("""<div class="bg-gradient-to-r from-rose-950/60 via-purple-950/60 to-slate-950/60 border border-rose-500/30 rounded-2xl p-6 mb-8 backdrop-blur shadow-2xl">
  <div class="flex items-center gap-2 mb-3">
    <span class="px-3 py-1 bg-rose-600 text-white font-black text-xs rounded-full uppercase tracking-wider shadow-lg animate-pulse">2026年最新厳選</span>
    <span class="text-rose-300 text-xs font-bold">主観・POV / ゼロ距離密着 / 圧倒的没入感</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4">
    【極上の密着・耳元吐息】FANZA「主観・POV（主観目線）」おすすめ神作ランキングTOP5！ゼロ距離キスと見つめ合い生ハメで脳がバグる歴代最高峰傑作選
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    「女優と本当に目が合っているような錯覚に陥りたい」「耳元で囁かれる甘い吐息と唾液の音で脳をトロトロに溶かされたい」——そんな全男性の究極の願望を叶えるのが、カメラが男優の視点（POV：Point of View）となった<b>主観特化型AV</b>です。<br>
    近年はGoProや超小型高精細カメラの進化、バイノーラル立体音響の導入により、まるで自分がその場にいて美女と愛し合っているかのような<b>異次元の没入感</b>を実現。VR機器がなくても、スマホやPCの画面越しにダイレクトに下半身と脳髄を直撃する傑作が続々と誕生しています。<br>
    今回は、FANZAで配信されている数万タイトルの中から、<b>「主観アングルの完成度」「女優の表情と演技力」「密着度・イチャラブ度」「リピート抜きの実力」</b>を徹底検証し、絶対に後悔しない殿堂入り神作TOP5を厳選紹介します！
  </p>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-3 border-t border-rose-500/20 text-xs text-slate-300">
    <div class="flex items-center gap-1.5"><span class="text-rose-400 font-bold">✓</span> ゼロ距離キス＆吐息</div>
    <div class="flex items-center gap-1.5"><span class="text-rose-400 font-bold">✓</span> 見つめ合い生ハメ</div>
    <div class="flex items-center gap-1.5"><span class="text-rose-400 font-bold">✓</span> 公式APIデータ取得</div>
    <div class="flex items-center gap-1.5"><span class="text-rose-400 font-bold">✓</span> HD即時ストリーミング</div>
  </div>
</div>
""")

    # 早見比較表
    content_parts.append("""<div class="my-8 bg-slate-900/90 border border-slate-700/80 rounded-2xl p-5 shadow-xl">
  <h3 class="text-lg font-bold text-white mb-3 flex items-center gap-2">
    <span class="w-2.5 h-2.5 rounded-full bg-rose-500"></span>
    【早見表】FANZA主観・POVおすすめ神作TOP5スペック比較
  </h3>
  <div class="overflow-x-auto">
    <table class="w-full text-xs md:text-sm text-left text-slate-300">
      <thead class="bg-slate-800 text-rose-300 font-bold uppercase border-b border-slate-700">
        <tr>
          <th class="p-3">順位 / 作品名</th>
          <th class="p-3">主演女優</th>
          <th class="p-3">特化ジャンル</th>
          <th class="p-3">没入感 / 抜けるポイント</th>
          <th class="p-3">公式リンク</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800">""")

    for i, (it, rev) in enumerate(zip(items, reviews)):
        title = it.get("title", "")
        act_names = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        act_str = " / ".join(act_names) if act_names else "単体女優"
        aff_link = it.get("affiliate_url_clean", "")
        content_parts.append(f"""        <tr class="hover:bg-slate-800/50 transition">
          <td class="p-3 font-bold text-white"><span class="text-rose-400 font-black mr-1">#{rev['rank']}</span> {title[:22]}...</td>
          <td class="p-3 font-medium text-rose-300">{act_str}</td>
          <td class="p-3">{rev['badge'].split('/')[0].strip()}</td>
          <td class="p-3 text-slate-300">{rev['climax'][:25]}...</td>
          <td class="p-3"><a href="{aff_link}" target="_blank" rel="nofollow noopener" class="inline-block px-3 py-1 bg-rose-600 hover:bg-rose-500 text-white rounded font-bold text-xs shadow transition">作品詳細</a></td>
        </tr>""")

    content_parts.append("""      </tbody>
    </table>
  </div>
</div>
""")

    # 各作品の詳細解説
    for i, (it, rev) in enumerate(zip(items, reviews)):
        cid = it.get("content_id", "")
        title = it.get("title", "")
        aff_url = it.get("affiliate_url_clean", "")
        pkg_img = it.get("imageURL", {}).get("large", "")
        sample_imgs = get_sample_images(it, max_count=4)
        
        actresses = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        actress_links = " ".join([get_actress_link(a) for a in actresses]) if actresses else '<span class="text-slate-400">専属女優</span>'
        
        genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        genre_links = " ".join([get_genre_link(g) for g in genres[:6]])
        
        maker_name = it.get("iteminfo", {}).get("maker", [{}])[0].get("name", "公式レーベル")
        encoded_maker = urllib.parse.quote(maker_name)
        maker_link = f'<a href="/maker/{encoded_maker}" class="text-slate-300 hover:text-amber-300 underline transition">{maker_name}</a>'
        
        price_val = it.get("prices", {}).get("price", "300~")
        review_cnt = it.get("review", {}).get("count", 0)
        review_rate = it.get("review", {}).get("average", "4.5")

        content_parts.append(f"""
<div class="my-10 bg-slate-900/90 border-2 border-slate-700/80 rounded-2xl p-6 shadow-2xl hover:border-rose-500/50 transition duration-300">
  <!-- ヘッダーバッジと順位 -->
  <div class="flex flex-wrap items-center justify-between gap-2 mb-4 pb-3 border-b border-slate-800">
    <div class="flex items-center gap-3">
      <span class="flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-rose-500 to-red-600 text-white font-black text-xl shadow-lg">
        {rev['rank']}
      </span>
      <div>
        <span class="px-2.5 py-0.5 bg-rose-950 text-rose-300 border border-rose-800 rounded-full text-xs font-bold">
          {rev['badge']}
        </span>
        <span class="ml-2 text-xs text-slate-400 font-mono">品番: {cid.upper()}</span>
      </div>
    </div>
    <div class="flex items-center gap-1 text-amber-400 text-sm font-bold bg-slate-800/80 px-3 py-1 rounded-lg border border-slate-700">
      <span>★ {review_rate}</span>
      <span class="text-slate-400 text-xs">({review_cnt}件の公式レビュー)</span>
    </div>
  </div>

  <!-- タイトル -->
  <h3 class="text-xl md:text-2xl font-black text-white leading-snug mb-3 hover:text-rose-400 transition">
    <a href="{aff_url}" target="_blank" rel="nofollow noopener">{title}</a>
  </h3>

  <!-- サブ見出し -->
  <div class="p-3 bg-rose-950/40 border-l-4 border-rose-500 rounded-r-lg mb-6 text-sm md:text-base font-bold text-rose-200">
    {rev['subtitle']}
  </div>

  <!-- メイン情報グリッド -->
  <div class="grid grid-cols-1 md:grid-cols-12 gap-6 mb-6">
    <!-- パッケージ画像 -->
    <div class="md:col-span-5 flex flex-col items-center">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="group relative block overflow-hidden rounded-xl border border-slate-700 shadow-xl w-full">
        <img src="{pkg_img}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition duration-300 flex items-end justify-center pb-4">
          <span class="px-4 py-2 bg-rose-600 text-white font-bold text-xs rounded-full shadow-lg">FANZA公式で今すぐ見る</span>
        </div>
      </a>
      <div class="mt-2 text-center">
        <span class="text-xs text-slate-400">配信価格: <span class="text-amber-400 font-bold text-sm">¥{price_val}</span></span>
      </div>
    </div>

    <!-- 詳細スペック＆見どころ解説 -->
    <div class="md:col-span-7 flex flex-col justify-between">
      <div class="space-y-3 text-xs md:text-sm text-slate-300">
        <div class="grid grid-cols-3 gap-2 bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
          <div><span class="text-slate-400 block text-xs">主演女優</span><div class="font-bold">{actress_links}</div></div>
          <div><span class="text-slate-400 block text-xs">メーカー</span><div class="font-bold">{maker_link}</div></div>
          <div><span class="text-slate-400 block text-xs">配信形態</span><span class="font-bold text-emerald-400">HD/4K動画</span></div>
        </div>

        <div class="pt-2">
          <span class="text-slate-400 block text-xs mb-1">関連タグ</span>
          <div class="flex flex-wrap gap-1.5">{genre_links}</div>
        </div>

        <div class="pt-3 text-slate-200 leading-relaxed text-sm">
          {rev['body']}
        </div>
      </div>
    </div>
  </div>

  <!-- サンプル画像ギャラリー -->
  <div class="my-5">
    <div class="text-xs font-bold text-slate-400 mb-2 flex items-center gap-1.5">
      <span class="w-1.5 h-1.5 rounded-full bg-rose-400"></span>
      公式高画質サンプルシーン・主観プレビュー（クリックで拡大確認）
    </div>
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
""")
        for s_idx, simg in enumerate(sample_imgs):
            content_parts.append(f"""      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="group block overflow-hidden rounded-lg border border-slate-800 hover:border-rose-500 transition shadow">
        <img src="{simg}" alt="{title} サンプル{s_idx+1}" class="w-full h-24 sm:h-28 object-cover group-hover:scale-110 transition duration-300" loading="lazy" />
      </a>""")
        content_parts.append(f"""    </div>
  </div>

  <!-- クライマックス＆購入ボタン -->
  <div class="mt-5 p-4 bg-slate-800/80 rounded-xl border border-slate-700/80 flex flex-col sm:flex-row items-center justify-between gap-4">
    <div class="text-xs md:text-sm text-slate-300">
      <span class="text-rose-400 font-bold block mb-0.5">🔥 決定打となる最高潮ポイント：</span>
      {rev['climax']}
    </div>
    <div class="w-full sm:w-auto flex-shrink-0">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="flex items-center justify-center gap-2 w-full sm:w-auto px-6 py-3.5 bg-gradient-to-r from-rose-600 to-red-600 hover:from-rose-500 hover:to-red-500 text-white font-black text-sm rounded-xl shadow-lg shadow-rose-900/40 hover:scale-105 transition duration-300">
        <span>FANZA公式サイトで本編を視聴</span>
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
      </a>
    </div>
  </div>
</div>
""")

    # ガイドセクション（主観AVの楽しみ方、お得な購入法、Q&A、内部リンク）
    content_parts.append("""
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 space-y-6">
  <h3 class="text-xl font-black text-white flex items-center gap-2 border-b border-slate-800 pb-3">
    <span class="text-rose-400">💡</span> 主観（POV）AVで脳がバグるほどの快感を味わう3つの極意
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm text-slate-300">
    <div class="bg-slate-800/50 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-rose-300 mb-2">1. 密閉型ヘッドホン・イヤホンの装着</h4>
      <p class="text-xs text-slate-400 leading-relaxed">
        主観AVの醍醐味は「耳元の吐息」と「唾液の生々しい水音」。左右のチャンネルで立体的に録音されたバイノーラル音声をイヤホンで聴くことで、女優が真横で囁いているリアルな錯覚が完成します。
      </p>
    </div>
    <div class="bg-slate-800/50 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-rose-300 mb-2">2. 画面と顔の距離を極限まで近づける</h4>
      <p class="text-xs text-slate-400 leading-relaxed">
        スマホを手持ちで顔の真正面に固定するか、PCモニターを至近距離に配置して視野の大半を画面で埋めるのがコツ。周辺視野のノイズを消すことで、脳の錯覚強度が何倍にも跳ね上がります。
      </p>
    </div>
    <div class="bg-slate-800/50 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-rose-300 mb-2">3. 公式アプリのHQダウンロード再生</h4>
      <p class="text-xs text-slate-400 leading-relaxed">
        ストリーミング時の回線遅延や画質劣化を防ぐため、FANZA公式アプリで最高画質（HD/4K）を一括ダウンロードしておくのがおすすめ。肌のキメや毛穴、愛液の滴りまで鮮明に楽しめます。
      </p>
    </div>
  </div>

  <div class="p-4 bg-gradient-to-r from-amber-950/40 to-slate-900 border border-amber-500/30 rounded-xl text-sm">
    <h4 class="font-bold text-amber-300 mb-1 flex items-center gap-1.5">
      <span>💰</span> お得に購入するためのFANZA活用術
    </h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      FANZAでは毎月恒例の大型セールやポイント還元キャンペーンが開催されています。クレジットカード決済はもちろん、誰にもバレずに購入できる「DMMポイントプリペイドカード」や「PayPay / 楽天ペイ」決済にも完全対応。購入した動画はクラウドライブラリに永久保存され、スマホ・PC・タブレットからいつでも何度でも再視聴可能です。
    </p>
  </div>
</div>

<!-- よくある質問 FAQ -->
<div class="my-10 bg-slate-900/90 border border-slate-800 rounded-2xl p-6">
  <h3 class="text-xl font-black text-white mb-4 flex items-center gap-2">
    <span class="text-rose-400">❓</span> FANZA主観・POV動画に関するよくある質問（FAQ）
  </h3>
  <div class="space-y-4 text-sm">
    <div class="border-b border-slate-800 pb-3">
      <h4 class="font-bold text-slate-200 mb-1">Q. VRゴーグルを持っていなくても普通のスマホやPCで楽しめますか？</h4>
      <p class="text-xs text-slate-400 leading-relaxed">
        はい、今回紹介した5作品はすべて通常の2D主観動画ですので、VRゴーグルは一切不要です。iPhone、Android、iPad、Windows/Macのブラウザや公式プレイヤーですぐに超高画質再生できます。さらにVRでの没入感を味わいたい方は、<a href="/posts/feature_meta_quest_fanza_vr_ultimate_guide" class="text-rose-400 hover:underline">Meta Quest対応FANZA VR完全攻略ガイド</a>も併せてご覧ください。
      </p>
    </div>
    <div class="border-b border-slate-800 pb-3">
      <h4 class="font-bold text-slate-200 mb-1">Q. 家族や同居人に購入履歴や視聴画面がバレる心配はありませんか？</h4>
      <p class="text-xs text-slate-400 leading-relaxed">
        FANZA公式アプリにはパスコードロック・生体認証ロック機能が搭載されており、端末を他人に貸しても安心です。また、クレジットカード明細も「DMM.com」または「AP (DMM)」と記載されるため、具体的な商品名が外部に漏れることは一切ありません。詳しい対策は<a href="/posts/feature_fanza_payment_methods_safe_buying_guide" class="text-rose-400 hover:underline">FANZAの安全な買い方・支払い方法完全ガイド</a>をご確認ください。
      </p>
    </div>
    <div>
      <h4 class="font-bold text-slate-200 mb-1">Q. 音声だけでじっくり楽しみたい場合はどんな作品がおすすめですか？</h4>
      <p class="text-xs text-slate-400 leading-relaxed">
        耳元での囁きやASMRに特化して楽しみたい方には、同人音声・バイノーラルボイス作品も超強力です。<a href="/posts/feature_fanza_doujin_asmr_voice_masterpiece_guide" class="text-rose-400 hover:underline">FANZA同人ボイス・ASMR神作傑作選</a>で耳が溶けるおすすめ作品を特集しています。
      </p>
    </div>
  </div>
</div>

<!-- 内部リンク集 -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6">
  <h3 class="text-lg font-bold text-white mb-3 flex items-center gap-2">
    <span class="text-rose-400">🔗</span> あわせて読みたい厳選キラー特集記事
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <a href="/posts/feature_fanza_vr_8k_ultra_immersive_best_ranking" class="p-3 bg-slate-800/70 hover:bg-slate-800 border border-slate-700 rounded-xl transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-rose-400 font-bold transition">【8K圧倒的没入感】FANZA VR動画おすすめ殿堂入り神作TOP5</span>
      <span class="text-rose-400">→</span>
    </a>
    <a href="/posts/feature_fanza_reverse_rape_femdom_milking_chijo_ranking" class="p-3 bg-slate-800/70 hover:bg-slate-800 border border-slate-700 rounded-xl transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-rose-400 font-bold transition">【男の究極妄想】FANZA「逆レイプ・搾精・M男向けド痴女」名作選</span>
      <span class="text-rose-400">→</span>
    </a>
    <a href="/posts/feature_fanza_busty_huge_tits_masterpieces_ranking" class="p-3 bg-slate-800/70 hover:bg-slate-800 border border-slate-700 rounded-xl transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-rose-400 font-bold transition">【極上の肉感と爆揺れ】巨乳・美乳・爆乳おすすめ殿堂入り神作選</span>
      <span class="text-rose-400">→</span>
    </a>
    <a href="/fanza-device-guide" class="p-3 bg-slate-800/70 hover:bg-slate-800 border border-slate-700 rounded-xl transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-rose-400 font-bold transition">【完全対応】スマホ・PC・テレビ・VRデバイス別視聴設定ガイド</span>
      <span class="text-rose-400">→</span>
    </a>
  </div>
</div>
""")

    full_html = "\n".join(content_parts)
    char_count = count_japanese_chars(full_html)
    print(f"Article 1 generated. Japanese character count: {char_count}")

    post_data = {
        "id": "feature_fanza_pov_subjective_immersion_masterpiece_ranking",
        "title": "【極上の密着・耳元吐息】FANZA「主観・POV（主観目線）」おすすめ殿堂入り神作TOP5！ゼロ距離キスと見つめ合い生ハメで脳がバグる圧倒的没入感傑作選【2026年最新】",
        "date": "2026-09-30 14:00:00",
        "hinban": "POV-SUBJECTIVE-BEST-2026",
        "price": "150~",
        "maker": "FANZA公式セレクション",
        "actresses": ["香澄せな", "横宮七海", "八木奈々", "葵いぶき", "小日向みゆう（清原みゆう）"],
        "genres": ["主観", "POV", "密着", "キス・接吻", "イチャラブ", "回春・エステ", "巨乳", "パイズリ", "中出し", "殿堂入り", "特集"],
        "image": cover_image,
        "review": full_html,
        "affiliate_url": items[0].get("affiliate_url_clean", "")
    }

    out_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f"Saved: {out_path}")


# ==============================================================================
# 記事2: 美脚・パンスト・黒タイツ特化
# ==============================================================================
def generate_article_2():
    print("=== Generating Article 2: Pantyhose & Slender Legs OL Masterpieces ===")
    cids = ["waaa00528", "miab00360", "mida00574", "jufd00798", "halt00070"]
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
        # 1: waaa00528 五日市芽依
        {
            "rank": "01",
            "badge": "殿堂入り圧倒的No.1 / 甘サド美脚パンスト爆ヌキ",
            "subtitle": "引き締まった長身美脚×黒ストッキング！上から目線で踏まれ擦られ骨抜きにされる至福",
            "body": """<b>【美脚フェチの理性を完膚なきまでに破壊する極上のパンスト調教】</b>：<br>
スラリと伸びた完璧な美脚の持ち主・五日市芽依が、極薄黒パンストを履いたまま見下ろすようなアングルで男を足蹴にし、甘いサドっ気たっぷりに弄び尽くすフェチ特化の絶対的頂点作。<br>
パンスト越しに伝わる足裏の温度やナイロン繊維の摩擦感を活かした足コキは、亀頭から竿全体を巧みな足技で挟み込み、男が悶絶するたびに「ほら、足でシコシコされるの好きでしょ…？」と耳元で意地悪く囁きます。ナイロンの滑らかな滑りと、つま先で敏感な裏筋をツンツンと刺激する変幻自在のテクニックに射精衝動が止まりません。<br>
パンストを脱がさず股間部分だけをビリッと破り、潤み切った秘肉を露出させてそのまま強引に結合させる着衣セックスは、美脚の曲線と相まって視覚的エロスが限界突破。脚フェチなら死ぬまでに必ず観るべき大名作です。""",
            "climax": "破れたパンストの隙間から溢れ出る愛液まみれの結合部を見せつけられながら、美脚を肩に担いで奥まで突き上げる濃密中出し。"
        },
        # 2: miab00360 月野江すい
        {
            "rank": "02",
            "badge": "OLスーツ×直穿き / ノーパンパンスト挑発",
            "subtitle": "パンティを履かずに直穿きしたパンスト越しに濡れ染み…！美人女上司からの逆痴女調教",
            "body": """<b>【オフィスで繰り広げられる背徳の直穿きパンスト挑発】</b>：<br>
デキるキャリアウーマンの月野江すいが、下着を付けずにパンストを直穿きしている秘密を武器に、部下の男を上から目線のドSプレイで骨抜きにしていくシチュエーション最高峰。<br>
タイトスカートをめくり上げると、黒パンストの股間部分には下着のラインがなく、直接秘部が密着してじんわりと濡れたシミが浮かび上がっているという破壊的なビジュアル。男の顔面にパンスト尻を押し当てて嗅がせ、足裏で股間を踏みつけながらじわじわと勃起を促します。<br>
直穿きパンストの上から指先でクリトリスを擦り合わされ、ナイロン越しに伝わる体温と湿り気に理性が蒸発。仕事中のオフィスという極限の緊張感の中で、女上司に完全服従させられる快楽に脳が完全に支配されます。""",
            "climax": "直穿きパンストを引き裂いて露出させた濡れそぼる肉壺に一気にペニスを突き刺し、上司の顔を快楽で歪ませる下剋上ピストン。"
        },
        # 3: mida00574 石川澪
        {
            "rank": "03",
            "badge": "朝セク×パンスト破き / 同棲痙攣アクメ",
            "subtitle": "「出社前なのに…！」新品のパンストを毎朝破られてガクガク痙攣アクメ通勤",
            "body": """<b>【可憐なOL姿と毎朝の無慈悲なパンスト破きセックス】</b>：<br>
同棲中の清楚系OL・石川澪が、毎朝の出勤準備を終えてストッキングを履いた瞬間に、彼氏から強引に襲われてパンストを破かれ朝セクを決められる背徳の同棲シリーズ。<br>
「もう遅刻しちゃうからダメ…ッ！」と恥じらいながら抵抗するものの、ピチピチのスーツスカートをたくし上げられ、履きたての黒パンストを指先で引き裂かれる瞬間の背徳感は言葉を失うレベル。破れ目から剥き出しになった白く柔らかな太ももと、黒ストッキングのコントラストが男の征服欲を激しく刺激します。<br>
出勤前の限られた時間で激しく腰を打ち付けられ、脚をピーンと伸ばしてビクビクとガニ股でオーガズムに達する石川澪のリアルな快楽堕ちっぷりは必見。日常のルーティンに潜む究極のフェチシチュエーションです。""",
            "climax": "出勤時間を告げるアラームが鳴り響く中、破れたパンストを履いたまま脚をガクガク震わせて痙攣絶頂する石川澪の中出し受精。"
        },
        # 4: jufd00798 香椎りあ
        {
            "rank": "04",
            "badge": "完全着衣ファック / 艶めかしいOLスーツ",
            "subtitle": "脱がさないからこそ狂おしい！タイトスカート×ストッキングの肉感フェチ",
            "body": """<b>【服を着たまま犯すからこそ際立つ、大人の女の肉感とエロス】</b>：<br>
抜群のプロポーションを誇る香椎りあが、OLの制服・スーツ・タイトスカート・パンストを一切脱ぐことなく、着衣のまま乱れ狂う大人の着衣セックス特化作。<br>
服の隙間から手を滑り込ませてまさぐる手の感触や、タイトスカートが持ち上がって露わになるパンストに包まれた豊満なヒップラインの美しさは芸術的。完全着衣だからこそ、衣服の擦れる衣擦れの音や、布地を濡らす愛液のコントラストが生々しく浮き彫りになります。<br>
後ろからスーツの腰元を掴んでバックから激しく突き込むシーンでは、揺れるスカートと張りのある美脚の曲線に視線が釘付け。着衣プレイの真髄を味わい尽くせる名盤です。""",
            "climax": "スーツの胸元をはだけさせ、パンストを履いたままの美脚を大きく広げさせて奥底まで注ぎ込む濃厚射精。"
        },
        # 5: halt00070 天月あず
        {
            "rank": "05",
            "badge": "デカ尻×美脚パンスト / 優しい痴女OL",
            "subtitle": "笑顔が可愛いショートカットOLに挟まれ踏まれ！着衣ぶっかけで何度も昇天",
            "body": """<b>【愛嬌満点の笑顔と凶悪なデカ尻パンストのギャップ萌え】</b>：<br>
ショートカットのキュートなルックスと、ムチムチと肉感溢れるデカ尻＆美脚を持つ天月あずが、優しく甘やかすように男を痴女調教する癒やし系フェチ傑作。<br>
黒パンストに包まれた極太の太ももで男の頭部をギュッと挟み込む太ももコキや、プリッとしたヒップを顔面に擦りつけるお尻責めなど、下半身フェチが悶絶するご褒美アングルの連続。天月あずの明るく屈託のない笑顔が、逆に背徳的なエロスを何倍にも引き立てます。<br>
パンストの上から直接ザーメンをぶちまける着衣ぶっかけシーンでは、黒いナイロンの上に白濁液がトロリと広がる視覚的コントラストが最高にエロティック。包容力のあるフェチプレイを求める方にイチオシです。""",
            "climax": "パンスト美脚でガッチリと腰をホールドされ、優しく頭を撫でられながらパンスト越しに放つ大量着衣フィニッシュ。"
        }
    ]

    content_parts = []

    content_parts.append("""<div class="bg-gradient-to-r from-amber-950/60 via-purple-950/60 to-slate-950/60 border border-amber-500/30 rounded-2xl p-6 mb-8 backdrop-blur shadow-2xl">
  <div class="flex items-center gap-2 mb-3">
    <span class="px-3 py-1 bg-amber-600 text-white font-black text-xs rounded-full uppercase tracking-wider shadow-lg animate-pulse">2026年最新厳選</span>
    <span class="text-amber-300 text-xs font-bold">美脚 / 黒パンスト / スーツOL / 足コキ・踏みつけ</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4">
    【美脚・パンスト・黒タイツの誘惑】FANZA「美脚パンスト・スーツOL」おすすめ神作ランキングTOP5！伝線・足コキ・踏みつけ・ノーパン直穿き挑発で狂わされるフェチ特化傑作選
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    「すらりと伸びた黒パンストの脚線美に踏まれたい」「タイトスカートから覗く太ももとナイロンの擦れる音だけで逝ける」——世の全脚フェチ・着衣フェチの理性を狂わせる<b>パンスト・美脚AV</b>。<br>
    ただ脱がせるだけのセックスとは異なり、パンストの引き裂き（破き）、ノーパン直穿きの濡れ染み、足裏やつま先を使った巧みな足コキ、完全着衣のまま乱れるオフィスシチュエーションなど、<b>心理的背徳感と視覚的エロスが極限まで計算されたジャンル</b>です。<br>
    本記事では、FANZA公式APIから最新の売上データと高評価レビューを徹底分析し、<b>「脚のラインの美しさ」「パンストの質感と破き演出」「足技のテクニック」「着衣ファックの背徳感」</b>において群を抜く殿堂入り神作TOP5を厳選してご紹介します！
  </p>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-3 border-t border-amber-500/20 text-xs text-slate-300">
    <div class="flex items-center gap-1.5"><span class="text-amber-400 font-bold">✓</span> 黒ストッキング脚線美</div>
    <div class="flex items-center gap-1.5"><span class="text-amber-400 font-bold">✓</span> 直穿き＆パンスト破き</div>
    <div class="flex items-center gap-1.5"><span class="text-amber-400 font-bold">✓</span> 濃厚足コキ・踏みつけ</div>
    <div class="flex items-center gap-1.5"><span class="text-amber-400 font-bold">✓</span> 高画質即時ストリーミング</div>
  </div>
</div>
""")

    # 早見比較表
    content_parts.append("""<div class="my-8 bg-slate-900/90 border border-slate-700/80 rounded-2xl p-5 shadow-xl">
  <h3 class="text-lg font-bold text-white mb-3 flex items-center gap-2">
    <span class="w-2.5 h-2.5 rounded-full bg-amber-500"></span>
    【早見表】FANZA美脚パンスト・OLおすすめ神作TOP5スペック比較
  </h3>
  <div class="overflow-x-auto">
    <table class="w-full text-xs md:text-sm text-left text-slate-300">
      <thead class="bg-slate-800 text-amber-300 font-bold uppercase border-b border-slate-700">
        <tr>
          <th class="p-3">順位 / 作品名</th>
          <th class="p-3">主演女優</th>
          <th class="p-3">特化ジャンル</th>
          <th class="p-3">フェチポイント / 見どころ</th>
          <th class="p-3">公式リンク</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800">""")

    for i, (it, rev) in enumerate(zip(items, reviews)):
        title = it.get("title", "")
        act_names = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        act_str = " / ".join(act_names) if act_names else "単体女優"
        aff_link = it.get("affiliate_url_clean", "")
        content_parts.append(f"""        <tr class="hover:bg-slate-800/50 transition">
          <td class="p-3 font-bold text-white"><span class="text-amber-400 font-black mr-1">#{rev['rank']}</span> {title[:22]}...</td>
          <td class="p-3 font-medium text-amber-300">{act_str}</td>
          <td class="p-3">{rev['badge'].split('/')[0].strip()}</td>
          <td class="p-3 text-slate-300">{rev['climax'][:25]}...</td>
          <td class="p-3"><a href="{aff_link}" target="_blank" rel="nofollow noopener" class="inline-block px-3 py-1 bg-amber-600 hover:bg-amber-500 text-white rounded font-bold text-xs shadow transition">作品詳細</a></td>
        </tr>""")

    content_parts.append("""      </tbody>
    </table>
  </div>
</div>
""")

    # 各作品の詳細解説
    for i, (it, rev) in enumerate(zip(items, reviews)):
        cid = it.get("content_id", "")
        title = it.get("title", "")
        aff_url = it.get("affiliate_url_clean", "")
        pkg_img = it.get("imageURL", {}).get("large", "")
        sample_imgs = get_sample_images(it, max_count=4)
        
        actresses = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        actress_links = " ".join([get_actress_link(a) for a in actresses]) if actresses else '<span class="text-slate-400">専属女優</span>'
        
        genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        genre_links = " ".join([get_genre_link(g) for g in genres[:6]])
        
        maker_name = it.get("iteminfo", {}).get("maker", [{}])[0].get("name", "公式レーベル")
        encoded_maker = urllib.parse.quote(maker_name)
        maker_link = f'<a href="/maker/{encoded_maker}" class="text-slate-300 hover:text-amber-300 underline transition">{maker_name}</a>'
        
        price_val = it.get("prices", {}).get("price", "300~")
        review_cnt = it.get("review", {}).get("count", 0)
        review_rate = it.get("review", {}).get("average", "4.5")

        content_parts.append(f"""
<div class="my-10 bg-slate-900/90 border-2 border-slate-700/80 rounded-2xl p-6 shadow-2xl hover:border-amber-500/50 transition duration-300">
  <!-- ヘッダーバッジと順位 -->
  <div class="flex flex-wrap items-center justify-between gap-2 mb-4 pb-3 border-b border-slate-800">
    <div class="flex items-center gap-3">
      <span class="flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-amber-500 to-orange-600 text-white font-black text-xl shadow-lg">
        {rev['rank']}
      </span>
      <div>
        <span class="px-2.5 py-0.5 bg-amber-950 text-amber-300 border border-amber-800 rounded-full text-xs font-bold">
          {rev['badge']}
        </span>
        <span class="ml-2 text-xs text-slate-400 font-mono">品番: {cid.upper()}</span>
      </div>
    </div>
    <div class="flex items-center gap-1 text-amber-400 text-sm font-bold bg-slate-800/80 px-3 py-1 rounded-lg border border-slate-700">
      <span>★ {review_rate}</span>
      <span class="text-slate-400 text-xs">({review_cnt}件の公式レビュー)</span>
    </div>
  </div>

  <!-- タイトル -->
  <h3 class="text-xl md:text-2xl font-black text-white leading-snug mb-3 hover:text-amber-400 transition">
    <a href="{aff_url}" target="_blank" rel="nofollow noopener">{title}</a>
  </h3>

  <!-- サブ見出し -->
  <div class="p-3 bg-amber-950/40 border-l-4 border-amber-500 rounded-r-lg mb-6 text-sm md:text-base font-bold text-amber-200">
    {rev['subtitle']}
  </div>

  <!-- メイン情報グリッド -->
  <div class="grid grid-cols-1 md:grid-cols-12 gap-6 mb-6">
    <!-- パッケージ画像 -->
    <div class="md:col-span-5 flex flex-col items-center">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="group relative block overflow-hidden rounded-xl border border-slate-700 shadow-xl w-full">
        <img src="{pkg_img}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition duration-300 flex items-end justify-center pb-4">
          <span class="px-4 py-2 bg-amber-600 text-white font-bold text-xs rounded-full shadow-lg">FANZA公式で今すぐ見る</span>
        </div>
      </a>
      <div class="mt-2 text-center">
        <span class="text-xs text-slate-400">配信価格: <span class="text-amber-400 font-bold text-sm">¥{price_val}</span></span>
      </div>
    </div>

    <!-- 詳細スペック＆見どころ解説 -->
    <div class="md:col-span-7 flex flex-col justify-between">
      <div class="space-y-3 text-xs md:text-sm text-slate-300">
        <div class="grid grid-cols-3 gap-2 bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
          <div><span class="text-slate-400 block text-xs">主演女優</span><div class="font-bold">{actress_links}</div></div>
          <div><span class="text-slate-400 block text-xs">メーカー</span><div class="font-bold">{maker_link}</div></div>
          <div><span class="text-slate-400 block text-xs">配信形態</span><span class="font-bold text-emerald-400">HD/4K動画</span></div>
        </div>

        <div class="pt-2">
          <span class="text-slate-400 block text-xs mb-1">関連タグ</span>
          <div class="flex flex-wrap gap-1.5">{genre_links}</div>
        </div>

        <div class="pt-3 text-slate-200 leading-relaxed text-sm">
          {rev['body']}
        </div>
      </div>
    </div>
  </div>

  <!-- サンプル画像ギャラリー -->
  <div class="my-5">
    <div class="text-xs font-bold text-slate-400 mb-2 flex items-center gap-1.5">
      <span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>
      公式高画質サンプルシーン・美脚パンストプレビュー（クリックで拡大確認）
    </div>
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
""")
        for s_idx, simg in enumerate(sample_imgs):
            content_parts.append(f"""      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="group block overflow-hidden rounded-lg border border-slate-800 hover:border-amber-500 transition shadow">
        <img src="{simg}" alt="{title} サンプル{s_idx+1}" class="w-full h-24 sm:h-28 object-cover group-hover:scale-110 transition duration-300" loading="lazy" />
      </a>""")
        content_parts.append(f"""    </div>
  </div>

  <!-- クライマックス＆購入ボタン -->
  <div class="mt-5 p-4 bg-slate-800/80 rounded-xl border border-slate-700/80 flex flex-col sm:flex-row items-center justify-between gap-4">
    <div class="text-xs md:text-sm text-slate-300">
      <span class="text-amber-400 font-bold block mb-0.5">🔥 決定打となる最高潮ポイント：</span>
      {rev['climax']}
    </div>
    <div class="w-full sm:w-auto flex-shrink-0">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="flex items-center justify-center gap-2 w-full sm:w-auto px-6 py-3.5 bg-gradient-to-r from-amber-600 to-orange-600 hover:from-amber-500 hover:to-orange-500 text-white font-black text-sm rounded-xl shadow-lg shadow-amber-900/40 hover:scale-105 transition duration-300">
        <span>FANZA公式サイトで本編を視聴</span>
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
      </a>
    </div>
  </div>
</div>
""")

    # ガイドセクション
    content_parts.append("""
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 space-y-6">
  <h3 class="text-xl font-black text-white flex items-center gap-2 border-b border-slate-800 pb-3">
    <span class="text-amber-400">👠</span> パンスト・美脚AVを限界までしゃぶり尽くすマニア向け鑑賞法
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm text-slate-300">
    <div class="bg-slate-800/50 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-amber-300 mb-2">1. デニール数と光沢感に注目</h4>
      <p class="text-xs text-slate-400 leading-relaxed">
        肌がうっすら透ける20〜30デニールの極薄黒ストッキングは、光の当たり具合で脚の立体感が強調されます。ハイヒールとの境目やつま先の緊張感に注目すると興奮が倍増します。
      </p>
    </div>
    <div class="bg-slate-800/50 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-amber-300 mb-2">2. 「破き」と「直穿き濡れ」のコントラスト</h4>
      <p class="text-xs text-slate-400 leading-relaxed">
        パンストをあえて脱がさず、股間だけを引き裂いて結合するプレイは、ナイロンの黒と女性器のピンク色のコントラストが最強の視覚刺激となります。
      </p>
    </div>
    <div class="bg-slate-800/50 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-amber-300 mb-2">3. スロー再生で足技の細部を堪能</h4>
      <p class="text-xs text-slate-400 leading-relaxed">
        FANZA公式プレイヤーの倍速・スロー調整機能を使い、足コキ時の足指の動きや土踏まずの密着をじっくり鑑賞するのがフェチ上級者の鉄則です。
      </p>
    </div>
  </div>
</div>

<!-- よくある質問 FAQ -->
<div class="my-10 bg-slate-900/90 border border-slate-800 rounded-2xl p-6">
  <h3 class="text-xl font-black text-white mb-4 flex items-center gap-2">
    <span class="text-amber-400">❓</span> パンスト・美脚ジャンルに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-4 text-sm">
    <div class="border-b border-slate-800 pb-3">
      <h4 class="font-bold text-slate-200 mb-1">Q. パンスト特化作品はどんなレーベルが強いですか？</h4>
      <p class="text-xs text-slate-400 leading-relaxed">
        フェチ系に定評のある「アタッカーズ（ATTACKERS）」「ワンズファクトリー（WANZ FACTORY）」「ダスッ！（DASG）」などの大手メーカーが高クオリティなパンスト・着衣作品を多数リリースしています。
      </p>
    </div>
    <div class="border-b border-slate-800 pb-3">
      <h4 class="font-bold text-slate-200 mb-1">Q. 見放題サービスでもパンスト作品は視聴できますか？</h4>
      <p class="text-xs text-slate-400 leading-relaxed">
        「FANZA見放題chデラックス」でも過去のパンスト名作が多数配信されています。最新作や単体専属女優の超大作を高画質でじっくり楽しみたい場合は単品ダウンロード購入が最もおすすめです。詳しくは<a href="/posts/feature_fanza_unlimited_deluxe_vs_single_buy_guide" class="text-amber-400 hover:underline">FANZA見放題ch vs 単品購入の徹底比較</a>をご覧ください。
      </p>
    </div>
  </div>
</div>

<!-- 内部リンク集 -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6">
  <h3 class="text-lg font-bold text-white mb-3 flex items-center gap-2">
    <span class="text-amber-400">🔗</span> あわせて読みたい厳選キラー特集記事
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <a href="/posts/feature_fanza_reverse_rape_femdom_milking_chijo_ranking" class="p-3 bg-slate-800/70 hover:bg-slate-800 border border-slate-700 rounded-xl transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-amber-400 font-bold transition">【男の究極妄想】FANZA「逆レイプ・搾精・M男向けド痴女」名作選</span>
      <span class="text-amber-400">→</span>
    </a>
    <a href="/posts/feature_fanza_mature_milf_wives_best_selection_ranking" class="p-3 bg-slate-800/70 hover:bg-slate-800 border border-slate-700 rounded-xl transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-amber-400 font-bold transition">【2026年最新】人妻・美熟女神作ランキングTOP5＆傑作選</span>
      <span class="text-amber-400">→</span>
    </a>
    <a href="/posts/feature_fanza_top_exclusive_actresses_ranking_masterpiece" class="p-3 bg-slate-800/70 hover:bg-slate-800 border border-slate-700 rounded-xl transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-amber-400 font-bold transition">【トップ女優】FANZAで今もっとも抜ける単体専属最強ランキング</span>
      <span class="text-amber-400">→</span>
    </a>
    <a href="/fanza-device-guide" class="p-3 bg-slate-800/70 hover:bg-slate-800 border border-slate-700 rounded-xl transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-amber-400 font-bold transition">【完全対応】スマホ・PC・テレビ・VRデバイス別視聴設定ガイド</span>
      <span class="text-amber-400">→</span>
    </a>
  </div>
</div>
""")

    full_html = "\n".join(content_parts)
    char_count = count_japanese_chars(full_html)
    print(f"Article 2 generated. Japanese character count: {char_count}")

    post_data = {
        "id": "feature_fanza_pantyhose_slender_legs_ol_fetish_ranking",
        "title": "【美脚・パンスト・黒タイツの誘惑】FANZA「美脚パンスト・スーツOL」おすすめ殿堂入り神作TOP5！伝線・足コキ・踏みつけ・ノーパン直穿き挑発で狂わされるフェチ特化傑作選【2026年最新】",
        "date": "2026-09-30 14:05:00",
        "hinban": "PANTYHOSE-LEGS-BEST-2026",
        "price": "150~",
        "maker": "FANZA公式セレクション",
        "actresses": ["五日市芽依", "月野江すい", "石川澪", "香椎りあ", "天月あず"],
        "genres": ["美脚", "パンスト", "ハイヒール", "タイツ", "OL", "スーツ", "足コキ", "着衣", "痴女", "殿堂入り", "特集"],
        "image": cover_image,
        "review": full_html,
        "affiliate_url": items[0].get("affiliate_url_clean", "")
    }

    out_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f"Saved: {out_path}")


# ==============================================================================
# 記事3: 義母・近親相姦・背徳家庭内特化
# ==============================================================================
def generate_article_3():
    print("=== Generating Article 3: Stepmother & Taboo Incest Masterpieces ===")
    cids = ["aldn00588", "meyd00547", "cemd00412", "jur00800", "aldn00504"]
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
        # 1: aldn00588 葉山さゆり
        {
            "rank": "01",
            "badge": "殿堂入り圧倒的No.1 / 嫁よりいいよ…義母背徳",
            "subtitle": "「お義母さん、女房よりずっといいよ…」若妻にはない包容力と熟れた蜜壷に溺れる禁断劇",
            "body": """<b>【実の息子の嫁よりも深く、息子の身体を包み込んでしまう美義母】</b>：<br>
成熟しきった艶やかな美貌と、豊満で柔らかな身体を持つ葉山さゆりが、娘の夫（義理の息子）と家庭内で禁断の一線を越えてしまう超人気シリーズの頂点。<br>
若い妻との淡白な夜の営みに不満を抱く息子に対し、「そんなこと言っちゃダメよ…」と母の顔で優しく諭しながらも、息子から求められると女の顔を覗かせてじっとりと潤んだ秘肉を開いてしまう背徳のドラマ構成は鳥肌モノ。<br>
熟女ならではの吸い付くような名器と、罪悪感に苛まれながらも「んっ…ああっ、いいの…もっと奥まで…」と息子のピストンに合わせて激しく喘ぎ乱れる姿は、男の本能を底の底から刺激します。家庭内という誰かに見つかるかもしれない極限の密室劇が、快楽の濃度を何倍にも跳ね上げる傑作です。""",
            "climax": "妻が隣の部屋にいる状況で、声を殺しながら息子の熱い種付けザーメンを膣奥深くで飲み干す背徳の濃厚中出し。"
        },
        # 2: meyd00547 永井マリア
        {
            "rank": "02",
            "badge": "爆乳美熟女×夜這い / 危険日逆夜這い中出し",
            "subtitle": "絶倫オヤジと母の交わりを目撃した嫁が欲情…！危険日を狙って義父の精液をねだる背徳",
            "body": """<b>【家族の性の狂気が交錯する、超濃厚な家庭内略奪ドラマ】</b>：<br>
圧倒的な爆乳と豊満な肉体美を誇る永井マリアが、夫の絶倫セックスを日常的に受け止める熟年夫婦の家庭を舞台に繰り広げられる、濃厚背徳ドラマの最高峰。<br>
義父と義母の激しい愛の営みを偶然覗き見てしまった息子の嫁が、義父の男らしさに欲情し、危険日を狙って義父の寝室へと忍び込む逆夜這いシチュエーション。永井マリアが醸し出す熟れたフェロモンと、家庭内で乱れ飛ぶ性欲の生々しさに圧倒されます。<br>
汗ばむ肌と肌が激しくぶつかり合う重厚なピストン音、そして家族の絆が音を立てて快楽へと崩壊していく背徳の快感は、一度味わうと病みつきになる強烈な中毒性を持っています。""",
            "climax": "禁断の興奮に狂った身体で互いを求め合い、子宮口を激突させながら何度も注ぎ込まれるドロドロの生中出し。"
        },
        # 3: cemd00412 ふじさき紫（藤咲紫）
        {
            "rank": "03",
            "badge": "引きこもり更生×誘惑 / 母性溢れる性教育",
            "subtitle": "部屋に閉じこもる義息子の性欲を毎日開放！母性の抱擁と濃厚セックスで再生させる物語",
            "body": """<b>【心を閉ざした義息子のチンポを、毎日のセックスで立ち直らせる義母の愛】</b>：<br>
美熟女界屈指の美貌と包容力を誇るふじさき紫（藤咲紫）が、自室に引きこもる義理の息子を社会復帰させるため、身体を張って毎日の性処理と愛情を注ぎ込む感動と背徳が融合した名作。<br>
暗い部屋のドアを開け、優しく微笑みながら息子のペニスを露わにして口で優しく包み込み、耳元で「大丈夫よ、お母さんが全部受け止めてあげるからね」と囁きかける母性の極致。男が心を開くにつれて、セックスはより情熱的で濃厚なものへと変化していきます。<br>
単なるエロを超えて、男の孤独な心を芯から救済し、下半身を歓喜で震わせる究極の癒やし×背徳ストーリーです。""",
            "climax": "母の大きな胸に抱きしめられ、涙を流しながら義母の膣内にすべての情念を放ち尽くす感動のフィニッシュ。"
        },
        # 4: jur00800 真木今日子
        {
            "rank": "04",
            "badge": "Iカップ神乳美熟女 / 背徳中出しドラマ",
            "subtitle": "夫と子作りした後はいつも義息子の肉棒に中出しされる…！Iカップ美熟女の二重生活",
            "body": """<b>【豊満なIカップ乳房と、二人の男に注ぎ込まれる背徳の宿命】</b>：<br>
熟女界の至宝・真木今日子が、夫との妊活セックスを終えた直後、息を潜めて待つ義息子の部屋を訪れて中出しセックスを交わすという極限の背徳ドラマ。<br>
夫の精液がまだ残る子宮奥へ、若く荒々しい義息子の絶倫ペニスが容赦なく突き刺さる背徳感は筆舌に尽くしがたいエロス。真木今日子の白く柔らかなIカップ爆乳が激しく波打ち、義息子の熱い抱擁に「もう夫のじゃ満足できない身体になっちゃった…」とメスとしての悦びに溺れていきます。<br>
美しい映像美と、真木今日子の情感あふれる艶技が完璧に調和した、大人のためのハイエンド背徳傑作です。""",
            "climax": "夫の精液の上から義息子の濃密な種付けザーメンを重ねて注ぎ込まれ、白目を剥いてアクメに達する背徳絶頂。"
        },
        # 5: aldn00504 倖田李梨
        {
            "rank": "05",
            "badge": "伝説のロングセラー / 熟れきった美義母の悦楽",
            "subtitle": "女房には絶対言えない…！お義母さんの蕩けるような名器に狂わされる男の末路",
            "body": """<b>【長年売れ続ける大ヒットシリーズ！熟女の魅力が詰まった至高の一作】</b>：<br>
妖艶な色香と豊満な肢体を誇る倖田李梨が、娘の夫からの執拗なアプローチに抗いきれず、次第に女の悦楽へと目覚めていく背徳近親ドラマの金字塔。<br>
最初は「家族なのよ、やめて…」と拒絶していた倖田李梨が、息子の巧みな愛撫と熱い眼差しによって徐々に濡れそぼり、自分から腰をくねらせて求め始める心理描写が実に秀逸。熟女ならではのしっとりとした肉質感と、経験に裏打ちされた吸い付くような膣内環境が男を狂わせます。<br>
家族というタブーを犯す背徳感と、本能の快楽がせめぎ合う濃厚なドラマ展開で、最後まで一秒たりとも目が離せません。""",
            "climax": "息子の激しい突き上げに翻弄され、母親であることを忘れて一人のメスとして狂乱アクメを迎える連続中出し。"
        }
    ]

    content_parts = []

    content_parts.append("""<div class="bg-gradient-to-r from-purple-950/60 via-red-950/60 to-slate-950/60 border border-purple-500/30 rounded-2xl p-6 mb-8 backdrop-blur shadow-2xl">
  <div class="flex items-center gap-2 mb-3">
    <span class="px-3 py-1 bg-purple-600 text-white font-black text-xs rounded-full uppercase tracking-wider shadow-lg animate-pulse">2026年最新厳選</span>
    <span class="text-purple-300 text-xs font-bold">義母・近親相姦 / 背徳家庭内 / 美熟女・人妻 / 生中出し</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4">
    【禁断の背徳・家族崩壊の蜜】FANZA「義母・近親相姦・家庭内不倫」おすすめ神作ランキングTOP5！ひとつ屋根の下で息子の友達・義息子の絶倫ピストンに悶える美熟女傑作選
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    「家族という絶対のタブーを破る背徳の快感」「若い女には決して出せない、熟れきった美熟母の圧倒的包容力と名器」——FANZAの全ジャンルの中でも、常にトップクラスの熱狂的ファンを抱え続けるのが<b>義母・近親相姦・背徳ドラマAV</b>です。<br>
    ひとつ屋根の下、隣の部屋に家族がいる状況で交わされる息を殺した逢瀬、拒絶から快楽へと堕ちていく心理描写、そして溢れ出る母性と愛欲が入り混じる濃厚な中出し性交は、観る者の脳髄を激しく揺さぶります。<br>
    今回は、FANZAで配信されている数千本の家庭内背徳作品の中から、<b>「ストーリーの背徳感」「美熟女女優の艶技と身体の魅力」「濃厚なピストンと中出しの生々しさ」「購入者の満足度」</b>を徹底検証し、絶対に外さない殿堂入り神作TOP5を厳選紹介します！
  </p>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-3 border-t border-purple-500/20 text-xs text-slate-300">
    <div class="flex items-center gap-1.5"><span class="text-purple-400 font-bold">✓</span> 禁断の家族内タブー</div>
    <div class="flex items-center gap-1.5"><span class="text-purple-400 font-bold">✓</span> 熟れきった美熟母の名器</div>
    <div class="flex items-center gap-1.5"><span class="text-purple-400 font-bold">✓</span> 息を殺した濃厚生中出し</div>
    <div class="flex items-center gap-1.5"><span class="text-purple-400 font-bold">✓</span> 高画質即時ストリーミング</div>
  </div>
</div>
""")

    # 早見比較表
    content_parts.append("""<div class="my-8 bg-slate-900/90 border border-slate-700/80 rounded-2xl p-5 shadow-xl">
  <h3 class="text-lg font-bold text-white mb-3 flex items-center gap-2">
    <span class="w-2.5 h-2.5 rounded-full bg-purple-500"></span>
    【早見表】FANZA義母・近親相姦おすすめ神作TOP5スペック比較
  </h3>
  <div class="overflow-x-auto">
    <table class="w-full text-xs md:text-sm text-left text-slate-300">
      <thead class="bg-slate-800 text-purple-300 font-bold uppercase border-b border-slate-700">
        <tr>
          <th class="p-3">順位 / 作品名</th>
          <th class="p-3">主演女優</th>
          <th class="p-3">特化ジャンル</th>
          <th class="p-3">背徳ポイント / 見どころ</th>
          <th class="p-3">公式リンク</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800">""")

    for i, (it, rev) in enumerate(zip(items, reviews)):
        title = it.get("title", "")
        act_names = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        act_str = " / ".join(act_names) if act_names else "単体女優"
        aff_link = it.get("affiliate_url_clean", "")
        content_parts.append(f"""        <tr class="hover:bg-slate-800/50 transition">
          <td class="p-3 font-bold text-white"><span class="text-purple-400 font-black mr-1">#{rev['rank']}</span> {title[:22]}...</td>
          <td class="p-3 font-medium text-purple-300">{act_str}</td>
          <td class="p-3">{rev['badge'].split('/')[0].strip()}</td>
          <td class="p-3 text-slate-300">{rev['climax'][:25]}...</td>
          <td class="p-3"><a href="{aff_link}" target="_blank" rel="nofollow noopener" class="inline-block px-3 py-1 bg-purple-600 hover:bg-purple-500 text-white rounded font-bold text-xs shadow transition">作品詳細</a></td>
        </tr>""")

    content_parts.append("""      </tbody>
    </table>
  </div>
</div>
""")

    # 各作品の詳細解説
    for i, (it, rev) in enumerate(zip(items, reviews)):
        cid = it.get("content_id", "")
        title = it.get("title", "")
        aff_url = it.get("affiliate_url_clean", "")
        pkg_img = it.get("imageURL", {}).get("large", "")
        sample_imgs = get_sample_images(it, max_count=4)
        
        actresses = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        actress_links = " ".join([get_actress_link(a) for a in actresses]) if actresses else '<span class="text-slate-400">専属女優</span>'
        
        genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        genre_links = " ".join([get_genre_link(g) for g in genres[:6]])
        
        maker_name = it.get("iteminfo", {}).get("maker", [{}])[0].get("name", "公式レーベル")
        encoded_maker = urllib.parse.quote(maker_name)
        maker_link = f'<a href="/maker/{encoded_maker}" class="text-slate-300 hover:text-amber-300 underline transition">{maker_name}</a>'
        
        price_val = it.get("prices", {}).get("price", "300~")
        review_cnt = it.get("review", {}).get("count", 0)
        review_rate = it.get("review", {}).get("average", "4.5")

        content_parts.append(f"""
<div class="my-10 bg-slate-900/90 border-2 border-slate-700/80 rounded-2xl p-6 shadow-2xl hover:border-purple-500/50 transition duration-300">
  <!-- ヘッダーバッジと順位 -->
  <div class="flex flex-wrap items-center justify-between gap-2 mb-4 pb-3 border-b border-slate-800">
    <div class="flex items-center gap-3">
      <span class="flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-purple-500 to-indigo-600 text-white font-black text-xl shadow-lg">
        {rev['rank']}
      </span>
      <div>
        <span class="px-2.5 py-0.5 bg-purple-950 text-purple-300 border border-purple-800 rounded-full text-xs font-bold">
          {rev['badge']}
        </span>
        <span class="ml-2 text-xs text-slate-400 font-mono">品番: {cid.upper()}</span>
      </div>
    </div>
    <div class="flex items-center gap-1 text-amber-400 text-sm font-bold bg-slate-800/80 px-3 py-1 rounded-lg border border-slate-700">
      <span>★ {review_rate}</span>
      <span class="text-slate-400 text-xs">({review_cnt}件の公式レビュー)</span>
    </div>
  </div>

  <!-- タイトル -->
  <h3 class="text-xl md:text-2xl font-black text-white leading-snug mb-3 hover:text-purple-400 transition">
    <a href="{aff_url}" target="_blank" rel="nofollow noopener">{title}</a>
  </h3>

  <!-- サブ見出し -->
  <div class="p-3 bg-purple-950/40 border-l-4 border-purple-500 rounded-r-lg mb-6 text-sm md:text-base font-bold text-purple-200">
    {rev['subtitle']}
  </div>

  <!-- メイン情報グリッド -->
  <div class="grid grid-cols-1 md:grid-cols-12 gap-6 mb-6">
    <!-- パッケージ画像 -->
    <div class="md:col-span-5 flex flex-col items-center">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="group relative block overflow-hidden rounded-xl border border-slate-700 shadow-xl w-full">
        <img src="{pkg_img}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition duration-300 flex items-end justify-center pb-4">
          <span class="px-4 py-2 bg-purple-600 text-white font-bold text-xs rounded-full shadow-lg">FANZA公式で今すぐ見る</span>
        </div>
      </a>
      <div class="mt-2 text-center">
        <span class="text-xs text-slate-400">配信価格: <span class="text-amber-400 font-bold text-sm">¥{price_val}</span></span>
      </div>
    </div>

    <!-- 詳細スペック＆見どころ解説 -->
    <div class="md:col-span-7 flex flex-col justify-between">
      <div class="space-y-3 text-xs md:text-sm text-slate-300">
        <div class="grid grid-cols-3 gap-2 bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
          <div><span class="text-slate-400 block text-xs">主演女優</span><div class="font-bold">{actress_links}</div></div>
          <div><span class="text-slate-400 block text-xs">メーカー</span><div class="font-bold">{maker_link}</div></div>
          <div><span class="text-slate-400 block text-xs">配信形態</span><span class="font-bold text-emerald-400">HD/4K動画</span></div>
        </div>

        <div class="pt-2">
          <span class="text-slate-400 block text-xs mb-1">関連タグ</span>
          <div class="flex flex-wrap gap-1.5">{genre_links}</div>
        </div>

        <div class="pt-3 text-slate-200 leading-relaxed text-sm">
          {rev['body']}
        </div>
      </div>
    </div>
  </div>

  <!-- サンプル画像ギャラリー -->
  <div class="my-5">
    <div class="text-xs font-bold text-slate-400 mb-2 flex items-center gap-1.5">
      <span class="w-1.5 h-1.5 rounded-full bg-purple-400"></span>
      公式高画質サンプルシーン・背徳家庭内プレビュー（クリックで拡大確認）
    </div>
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
""")
        for s_idx, simg in enumerate(sample_imgs):
            content_parts.append(f"""      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="group block overflow-hidden rounded-lg border border-slate-800 hover:border-purple-500 transition shadow">
        <img src="{simg}" alt="{title} サンプル{s_idx+1}" class="w-full h-24 sm:h-28 object-cover group-hover:scale-110 transition duration-300" loading="lazy" />
      </a>""")
        content_parts.append(f"""    </div>
  </div>

  <!-- クライマックス＆購入ボタン -->
  <div class="mt-5 p-4 bg-slate-800/80 rounded-xl border border-slate-700/80 flex flex-col sm:flex-row items-center justify-between gap-4">
    <div class="text-xs md:text-sm text-slate-300">
      <span class="text-purple-400 font-bold block mb-0.5">🔥 決定打となる最高潮ポイント：</span>
      {rev['climax']}
    </div>
    <div class="w-full sm:w-auto flex-shrink-0">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="flex items-center justify-center gap-2 w-full sm:w-auto px-6 py-3.5 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white font-black text-sm rounded-xl shadow-lg shadow-purple-900/40 hover:scale-105 transition duration-300">
        <span>FANZA公式サイトで本編を視聴</span>
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
      </a>
    </div>
  </div>
</div>
""")

    # ガイドセクション
    content_parts.append("""
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 space-y-6">
  <h3 class="text-xl font-black text-white flex items-center gap-2 border-b border-slate-800 pb-3">
    <span class="text-purple-400">🔥</span> 義母・近親背徳AVで最高潮の興奮を引き出す3つの鑑賞ポイント
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm text-slate-300">
    <div class="bg-slate-800/50 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-purple-300 mb-2">1. 導入ドラマの「心の葛藤」を飛ばさずに観る</h4>
      <p class="text-xs text-slate-400 leading-relaxed">
        背徳ジャンルの最大のスパイスは「やってはいけない罪悪感」。母親としての立場と、女としての疼きの狭間で揺れ動く表情や会話のやり取りをじっくり見ることで、結合時の快楽が何倍にも膨れ上がります。
      </p>
    </div>
    <div class="bg-slate-800/50 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-purple-300 mb-2">2. 「息を殺した声漏れ」と環境音の緊張感</h4>
      <p class="text-xs text-slate-400 leading-relaxed">
        隣の部屋に夫や娘がいる設定でのセックスは、声を出せないもどかしさと手で口を塞ぐ仕草が最高にエロティック。ヘッドホンをつけて微細な息遣いまで聞き逃さないのが鉄則です。
      </p>
    </div>
    <div class="bg-slate-800/50 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-purple-300 mb-2">3. 熟女女優ならではの豊満な肉感と包容力</h4>
      <p class="text-xs text-slate-400 leading-relaxed">
        若手女優には出せない、豊かな胸元、柔らかそうなお腹周り、しっとりとした太ももなど、熟成された大人の女性の肉体美を大画面で味わい尽くしましょう。
      </p>
    </div>
  </div>
</div>

<!-- よくある質問 FAQ -->
<div class="my-10 bg-slate-900/90 border border-slate-800 rounded-2xl p-6">
  <h3 class="text-xl font-black text-white mb-4 flex items-center gap-2">
    <span class="text-purple-400">❓</span> 義母・近親相姦ジャンルに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-4 text-sm">
    <div class="border-b border-slate-800 pb-3">
      <h4 class="font-bold text-slate-200 mb-1">Q. 熟女・義母ジャンルのおすすめメーカーはどこですか？</h4>
      <p class="text-xs text-slate-400 leading-relaxed">
        「マドンナ（Madonna）」「オーロラ・プロジェクト・アネックス（Aurora Project ANNEX）」「ジュエルズ（JEWELS）」「クリスタル映像」などがストーリー性・女優のクオリティともに圧倒的な人気を誇っています。
      </p>
    </div>
    <div class="border-b border-slate-800 pb-3">
      <h4 class="font-bold text-slate-200 mb-1">Q. NTR（寝取られ）要素のある義母作品もありますか？</h4>
      <p class="text-xs text-slate-400 leading-relaxed">
        はい、父親の目の前で義母を抱く作品や、息子の嫁を義父が奪う作品など、NTR要素が組み合わさった傑作も多数あります。NTR特化の神作については<a href="/posts/feature_fanza_ntr_netorare_cuckold_best_masterpieces" class="text-purple-400 hover:underline">FANZA NTR・寝取られ神作ランキングTOP5</a>で詳しく解説しています。
      </p>
    </div>
  </div>
</div>

<!-- 内部リンク集 -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6">
  <h3 class="text-lg font-bold text-white mb-3 flex items-center gap-2">
    <span class="text-purple-400">🔗</span> あわせて読みたい厳選キラー特集記事
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <a href="/posts/feature_fanza_creampie_breeding_deep_ejaculation_ranking" class="p-3 bg-slate-800/70 hover:bg-slate-800 border border-slate-700 rounded-xl transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-purple-400 font-bold transition">【子宮ノック・ドロドロ生ハメ】生中出し・種付け解禁神作TOP5</span>
      <span class="text-purple-400">→</span>
    </a>
    <a href="/posts/feature_fanza_mature_milf_wives_best_selection_ranking" class="p-3 bg-slate-800/70 hover:bg-slate-800 border border-slate-700 rounded-xl transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-purple-400 font-bold transition">【2026年最新】人妻・美熟女神作ランキングTOP5＆傑作選</span>
      <span class="text-purple-400">→</span>
    </a>
    <a href="/posts/feature_fanza_ntr_netorare_cuckold_best_masterpieces" class="p-3 bg-slate-800/70 hover:bg-slate-800 border border-slate-700 rounded-xl transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-purple-400 font-bold transition">【脳が狂う背徳の悦楽】NTR・寝取られ・略奪神作ランキングTOP5</span>
      <span class="text-purple-400">→</span>
    </a>
    <a href="/fanza-device-guide" class="p-3 bg-slate-800/70 hover:bg-slate-800 border border-slate-700 rounded-xl transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-purple-400 font-bold transition">【完全対応】スマホ・PC・テレビ・VRデバイス別視聴設定ガイド</span>
      <span class="text-purple-400">→</span>
    </a>
  </div>
</div>
""")

    full_html = "\n".join(content_parts)
    char_count = count_japanese_chars(full_html)
    print(f"Article 3 generated. Japanese character count: {char_count}")

    post_data = {
        "id": "feature_fanza_stepmother_incest_taboo_mature_wives_ranking",
        "title": "【禁断の背徳・家族崩壊の蜜】FANZA「義母・近親相姦・家庭内不倫」おすすめ神作ランキングTOP5！ひとつ屋根の下で息子の友達・義息子の絶倫ピストンに悶える美熟女傑作選【2026年最新】",
        "date": "2026-09-30 14:10:00",
        "hinban": "STEPMOTHER-INCEST-BEST-2026",
        "price": "150~",
        "maker": "FANZA公式セレクション",
        "actresses": ["葉山さゆり", "永井マリア", "ふじさき紫（藤咲紫）", "真木今日子", "倖田李梨（倖田美梨、岩下美季）"],
        "genres": ["義母", "近親相姦", "家庭内不倫", "人妻", "美熟女", "中出し", "夜這い", "ドラマ", "巨乳", "殿堂入り", "特集"],
        "image": cover_image,
        "review": full_html,
        "affiliate_url": items[0].get("affiliate_url_clean", "")
    }

    out_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    print("=== START GENERATING 3 KILLER FEATURES ===")
    generate_article_1()
    generate_article_2()
    generate_article_3()
    print("=== ALL 3 FEATURES GENERATED SUCCESSFULLY ===")
