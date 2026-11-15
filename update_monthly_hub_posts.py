# -*- coding: utf-8 -*-
import os
import json
import requests
import random
import html
import re
from datetime import datetime

# ==============================================================================
# Configuration & Credentials
# ==============================================================================
API_ID = os.environ.get("FANZA_API_ID") or "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = os.environ.get("FANZA_AFFILIATE_ID") or "onchan555-999"
SITE_AFFILIATE_ID = "onchan555-003"
POSTS_DIR = os.path.join("src", "data", "posts")
CACHE_FILE = "posted_hub_cids.txt"

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

GEMINI_MODELS = [
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-2.5-flash-lite",
    "gemini-2.0-flash-lite",
    "gemini-2.5-pro",
    "gemini-3-flash",
    "gemini-3.1-pro",
    "gemini-3.1-flash-lite",
    "gemini-3.5-flash-lite",
    "gemini-3.5-flash",
    "gemini-3.6-flash",
    "gemini-3.7-flash"
]

CATCH_TEMPLATES = {
    "人妻・熟女": [
        "背徳の蜜壺…理性を捨てて喘ぎ乱れる艶やかな隣の人妻",
        "禁断の密会劇！若者を貪り尽くす熟れた肉体と危険なフェロモン",
        "夫には絶対に見せられない…恥じらいと快楽に悶絶する極上若妻",
        "潤んだ瞳と滴る愛液…家庭を忘れて貪り合う濃密中出しSEX",
        "豊満な柔肌が揺れる！年下男に跨がり狂乱騎乗位でイキ崩れる未亡人"
    ],
    "巨乳・爆乳": [
        "視界を埋め尽くす神乳！圧倒的肉感と弾力で攻め立てるパイズリ地獄",
        "揺れ狂う極上バスト！激しいピストンで波打つ肉体美に射精不可避",
        "たわわに実った極上果実！顔面を包み込む密着フェラと至福の快楽",
        "ブラから溢れる圧倒的質量！汗ばむ谷間に挟まれて理性が溶け出す",
        "重量級の巨乳が跳ねる！息を呑むエロスと迫力のハメ狂いピストン"
    ],
    "単体専属・美少女": [
        "息を呑む圧倒的透明感…トップ単体女優が魅せる本気のメス堕ちSEX",
        "至高の美少女が快感に蕩ける！滴る愛液と生々しい吐息に大興奮",
        "可憐な素顔が淫らに歪む…専属クオリティの極上フェラ＆濃密ピストン",
        "完全撮り下ろし専属作！美しすぎる肢体が快楽の絶頂で震え上がる",
        "見つめ合って深々と挿入…切なさとエロスが交錯する最高純度の中出し"
    ],
    "素人・ハメ撮り": [
        "カメラの前で露わになる本性！素人娘が生々しく喘ぎ乱れるリアル交尾",
        "ナンパから即ホテルへ直行！警戒心を解いて潮吹きアクメに沈む生ハメ",
        "ネットで知り合った神ボディ素人！恥じらいながらもチンポを求める生中出し",
        "完全密着プライベート個室！プロにはない素朴な反応とガチイキの連続",
        "カメラを忘れて腰を振る！本気で気持ち良くなってしまった素人美女の絶頂顔"
    ],
    "レズ・百合": [
        "舌先が絡み合う濃密接吻…美女二人が貪り合う至極のレズビアン快楽",
        "濡れそぼる秘部を愛撫し合う…女同士だからこそ届く最深部の絶頂責め",
        "貝合わせで滴る蜜液！指先と舌で互いを極限までイカせ合う百合の極み",
        "柔らかな肌と肌が密着…甘い吐息と痙攣が止まらない濃厚レズセックス",
        "理性を奪うクンニ地獄！快感に涙を流しながら絶頂を重ねる極上美女"
    ],
    "成人コミック・新作漫画": [
        "美麗な筆致で描かれる極上エロス！背徳と快楽の限界を突破する神作",
        "圧倒的な画力と生々しい肉感描写！読めば確実に抜ける今月の大注目作",
        "フェチズムが暴走する超濃密シチュエーション！ページをめくる手が止まらない",
        "表情の歪みと愛液の描写が凄まじい…同人界隈を震撼させる最高峰の快楽劇",
        "圧倒的ボリュームと抜きどころの連続！一度読んだら忘れられない至高の傑作"
    ],
    "総合新作AV": [
        "今月絶対に見逃せない大ヒット作！ハイクオリティな演出と極上の絡み",
        "売上・話題性ともに独占！トップ女優と名門メーカーが放つ本気の傑作",
        "圧倒的臨場感で脳を揺さぶる！高画質映像で楽しむ至福のピストン劇",
        "ファン絶賛の濃厚エロス！息遣いまで伝わるリアルな快楽ドキュメント",
        "今月のFANZAランキングを席巻！最初から最後まで抜けるシーンの連続"
    ]
}

REVIEW_TEMPLATES = {
    "人妻・熟女": [
        "家庭や日常の枠組みから解き放たれ、一人のメスとして快楽に溺れていく心理描写と生々しい肉体美が圧巻。しっとりと濡れた秘部に深々と挿入され、背徳感に震えながら腰をくねらせるシーンは必見です。",
        "年齢を重ねるごとに増すフェロモンと、我慢できない快楽に蕩けていく表情が男の本能を刺激。控えめな態度から一転、我を忘れて淫語を漏らしながら中出しを求める姿に理性が崩壊します。"
    ],
    "巨乳・爆乳": [
        "画面いっぱいに広がる迫力のバストと、ピストンの衝撃に合わせて激しく波打つ圧倒的質量感。手や口だけでなく全身の柔肌を使って包み込むような密着愛撫は、巨乳ファンならずとも息を呑む破壊力です。",
        "ただ大きいだけでなく、張りと柔らかさを兼ね備えた極上の美乳。激しいピストンの中で汗ばみ、桃色の乳首をビンビンに尖らせながらイキ乱れるシーンの連続に射精が止まりません。"
    ],
    "単体専属・美少女": [
        "トップ単体女優ならではの卓越したビジュアルと、作品全体を包み込む贅沢なカメラワーク。男優のリードに身を委ね、徐々に羞恥心を脱ぎ捨てて本気の快楽に没入していく姿が極上のエロスを生み出しています。",
        "見つめ合う瞳、耳元で囁かれるリアルな吐息、そして絶頂時に見せる無防備な表情。単なる演技を超えた熱量とエロスが詰まっており、最初から最後まで没入感たっぷりに楽しめます。"
    ],
    "素人・ハメ撮り": [
        "演出されたAVでは決して味わえない、リアルな緊張感と生々しい反応が最大の魅力。ぎこちない手つきから徐々に快感に目覚め、本気でチ〇ポを締め付けてくるリアルな交尾に興奮が最高潮に達します。",
        "個室空間での密着から、徐々に理性が外れていくドキュメント感。カメラの前で晒されるリアルな恥じらいと、我慢できずに漏れ出る喘ぎ声が男の本能を直撃します。"
    ],
    "レズ・百合": [
        "女性特有の繊細なタッチと、貪り合うような濃密な舌使いが織りなす極上の百合世界。相手の性感帯を熟知した攻めで何度も絶頂を繰り返し、互いの愛液で全身を濡らし合う映像美に圧倒されます。",
        "視線の交わし合いから徐々に高まっていくエロスの熱量。男の介在しない二人だけの密室で、愛と快楽が完全に溶け合った極上のレズプレイは何度見ても飽きさせません。"
    ],
    "成人コミック・新作漫画": [
        "コマ割り、構図、トーンワークのすべてが読者の興奮を極限まで高めるよう計算し尽くされた傑作。キャラクターの細やかな表情の変化や、溢れ出る愛液・汗の質感描写が抜群の抜けを提供します。",
        "ストーリーの導入からクライマックスの乱れ狂いまで、読者を引き込んで離さない構成力。フェチ心をくすぐるシチュエーションが完璧に描かれており、コレクションに加える価値のある一冊です。"
    ],
    "総合新作AV": [
        "名門メーカーのこだわり抜かれた企画力と、出演キャストの圧倒的ポテンシャルが見事に融合した今月の代表作。映像のクリアさ、音響の生々しさ、そして何より絡みの濃厚さが群を抜いています。",
        "導入のシチュエーションからラストの怒涛の絶頂ラッシュまで一切の無駄がない充実の構成。今月どの作品を観るべきか迷っているなら、まず間違いなく押さえておくべきイチオシのタイトルです。"
    ]
}

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return set(line.strip() for line in f if line.strip())
    return set()

def save_cache(cids):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        for cid in sorted(cids):
            f.write(f"{cid}\n")

# ==============================================================================
# Gemini / Groq API Text Polish
# ==============================================================================
def polish_review_with_llm(title, actress, maker, genres_str, raw_desc, category_title, idx):
    prompt = f"""
以下の新作作品の見どころを、アダルト動画マニアの男性ライターとして熱量高く人間味のある文章で清書してください。
「AI」「自動」などのメタ表現や、定型句（〜をご紹介します、いかがでしょうか等）は一切使わないでください。

【作品情報】
・タイトル: {title}
・出演者/著者: {actress}
・メーカー/レーベル: {maker}
・ジャンル: {genres_str}
・作品概要: {raw_desc}

【出力フォーマット】
以下の2項目のみを出力してください：
キャッチコピー: （読者が思わず息を呑むような25〜35文字の刺激的な一行）
見どころレビュー: （女優の生々しい魅力、シチュエーションの良さ、抜けるポイントを語った150〜220文字程度の熱い文章）
"""
    if GEMINI_API_KEY:
        models_to_try = list(GEMINI_MODELS)
        random.shuffle(models_to_try)
        for model in models_to_try:
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={GEMINI_API_KEY}"
                payload = {
                    "contents": [{"parts": [{"text": prompt}]}],
                    "generationConfig": {"temperature": 0.7, "maxOutputTokens": 500}
                }
                res = requests.post(url, json=payload, timeout=12)
                if res.status_code == 200:
                    cand = res.json().get("candidates", [{}])[0]
                    text = cand.get("content", {}).get("parts", [{}])[0].get("text", "").strip()
                    if len(text) > 50:
                        return text
            except Exception:
                pass

    if GROQ_API_KEY:
        for m in ["llama-3.3-70b-versatile", "llama3-70b-8192"]:
            try:
                h = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
                p = {
                    "model": m,
                    "messages": [
                        {"role": "system", "content": "あなたは熱量あふれるアダルトレビューライターです。"},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.7
                }
                r = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=h, json=p, timeout=12)
                if r.status_code == 200:
                    text = r.json()["choices"][0]["message"]["content"].strip()
                    if len(text) > 50:
                        return text
            except Exception:
                pass

    # High quality fallback from varied copy banks
    copy_list = CATCH_TEMPLATES.get(category_title, CATCH_TEMPLATES["総合新作AV"])
    rev_list = REVIEW_TEMPLATES.get(category_title, REVIEW_TEMPLATES["総合新作AV"])
    chosen_copy = copy_list[(idx - 1) % len(copy_list)]
    if actress and "ほか" not in actress and len(actress) < 15:
        chosen_copy = f"【{actress}】{chosen_copy}"
    chosen_rev = rev_list[(idx - 1) % len(rev_list)]
    return f"キャッチコピー: {chosen_copy}\n見どころレビュー: {chosen_rev}"

# ==============================================================================
# FANZA API Client
# ==============================================================================
def fetch_fanza_items(service, floor, keyword=None, hits=15):
    url = "https://api.dmm.com/affiliate/v3/ItemList"
    params = {
        "api_id": API_ID,
        "affiliate_id": API_AFFILIATE_ID,
        "site": "FANZA",
        "service": service,
        "floor": floor,
        "hits": hits,
        "sort": "date",
        "output": "json"
    }
    if keyword:
        params["keyword"] = keyword

    try:
        res = requests.get(url, params=params, timeout=15)
        data = res.json()
        items = data.get("result", {}).get("items", [])
        if not items:
            params.pop("sort")
            params["sort"] = "rank"
            res = requests.get(url, params=params, timeout=15)
            data = res.json()
            items = data.get("result", {}).get("items", [])
        return items
    except Exception as e:
        print(f"FANZA API error ({service}/{floor}/{keyword}): {e}")
        return []

# ==============================================================================
# HTML Card Generator
# ==============================================================================
def build_hub_card_html(item, idx, category_label, service):
    cid = item.get("content_id") or ""
    title = item.get("title") or ""
    img_large = item.get("imageURL", {}).get("large") or ""
    iteminfo = item.get("iteminfo", {})
    
    actresses = [a.get("name") for a in iteminfo.get("actress", []) if a.get("name")]
    author = [a.get("name") for a in iteminfo.get("author", []) if a.get("name")]
    maker = iteminfo.get("maker", [{}])[0].get("name", "公式レーベル") if iteminfo.get("maker") else "公式レーベル"
    genres = [g.get("name") for g in iteminfo.get("genre", []) if g.get("name")]
    date_str = item.get("date", "").split(" ")[0]
    
    is_manga = (service == "ebook" or service == "digital_book")
    if is_manga:
        clean_aff_url = f"https://al.fanza.co.jp/?lurl=https%3A%2F%2Fbook.dmm.co.jp%2Fproduct%2F{cid}%2F&af_id={SITE_AFFILIATE_ID}&ch=api"
        if len(author) > 3:
            creator_text = "、".join(author[:3]) + " ほか"
        else:
            creator_text = "、".join(author) if author else "人気作家"
        creator_label = "著者・サークル"
    else:
        clean_aff_url = f"https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D{cid}&af_id={SITE_AFFILIATE_ID}&ch=api"
        creator_text = "、".join(actresses) if actresses else "特選美女キャスト"
        creator_label = "出演女優"

    genres_str = "、".join(genres[:4]) if genres else "新作"
    raw_desc = (item.get("review") or item.get("description") or title)[:200]
    polished = polish_review_with_llm(title, creator_text, maker, genres_str, raw_desc, category_label, idx)
    
    catch_copy = "今月絶対に見逃せない至高の注目作"
    review_desc = polished
    for line in polished.split("\n"):
        line = line.strip()
        if "キャッチコピー" in line:
            catch_copy = line.split(":", 1)[-1].strip() or line.split("：", 1)[-1].strip()
        elif "見どころレビュー" in line or "レビュー" in line:
            review_desc = line.split(":", 1)[-1].strip() or line.split("：", 1)[-1].strip()

    samples = item.get("sampleImageURL", {}).get("sample_l", {}).get("image", [])
    if not samples:
        samples = item.get("sampleImageURL", {}).get("sample_s", {}).get("image", [])
    samples_slice = samples[:4]

    sample_images_html = ""
    if samples_slice:
        sample_images_html = f"""
        <div class="mt-4">
          <p class="text-xs font-bold text-slate-400 mb-2 flex items-center gap-1">
            <span>📸</span><span>公式高画質サンプル場面カット</span>
          </p>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
            {''.join([f'<a href="{clean_aff_url}" target="_blank" rel="noopener noreferrer sponsored" class="block aspect-video overflow-hidden rounded-lg border border-slate-700 bg-slate-800 hover:border-rose-500 transition"><img src="{s}" alt="{html.escape(title)} サンプル" class="w-full h-full object-cover hover:scale-105 transition duration-300" loading="lazy" /></a>' for s in samples_slice])}
          </div>
        </div>
        """

    cta_btn_text = "FANZA公式で無料試し読み・本編を見る" if is_manga else "FANZA公式で無料プレビュー・本編を見る"

    return f"""
    <!-- 追加カード: {cid.upper()} -->
    <article class="bg-slate-900/90 border border-slate-800 hover:border-rose-500/50 rounded-2xl p-5 sm:p-7 shadow-xl transition-all duration-300 space-y-5">
      <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800/80 pb-3">
        <div class="flex items-center gap-2">
          <span class="inline-flex items-center justify-center w-7 h-7 rounded-full bg-gradient-to-r from-rose-600 to-pink-600 text-white font-black text-xs shadow-md">#{idx}</span>
          <span class="text-xs font-bold px-2.5 py-0.5 rounded bg-rose-500/10 text-rose-400 border border-rose-500/20">
            {cid.upper()}
          </span>
          <span class="text-xs text-slate-400 font-medium">{date_str} 配信</span>
        </div>
        <div class="text-xs font-bold text-rose-400 flex items-center gap-1">
          <span>🔥</span><span>{category_label} 注目作速報</span>
        </div>
      </div>

      <div class="space-y-1.5">
        <p class="text-xs font-bold text-rose-400 tracking-wide">{html.escape(catch_copy)}</p>
        <h3 class="text-base sm:text-lg font-black text-white hover:text-rose-400 transition leading-snug">
          <a href="{clean_aff_url}" target="_blank" rel="noopener noreferrer sponsored">
            {html.escape(title)}
          </a>
        </h3>
        <div class="flex flex-wrap items-center gap-x-4 gap-y-1 text-xs text-slate-300 pt-1">
          <span class="text-slate-400">{creator_label}: <strong class="text-rose-300 font-bold">{html.escape(creator_text)}</strong></span>
          <span class="text-slate-400">レーベル: <strong class="text-slate-200">{html.escape(maker)}</strong></span>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-12 gap-5 items-center">
        <div class="md:col-span-5 relative group overflow-hidden rounded-xl border border-slate-800 bg-black flex items-center justify-center">
          <a href="{clean_aff_url}" target="_blank" rel="noopener noreferrer sponsored" class="block w-full">
            <img src="{img_large}" alt="{html.escape(title)} 公式画像" class="w-full h-auto max-h-[360px] object-contain group-hover:scale-105 transition duration-300" loading="lazy" />
            <div class="absolute inset-0 bg-slate-950/40 opacity-0 group-hover:opacity-100 transition duration-200 flex items-center justify-center">
              <span class="text-xs font-black text-white bg-rose-600 px-4 py-2 rounded-xl shadow-lg flex items-center gap-1">
                <span>🔥</span><span>公式プレビューを即再生</span>
              </span>
            </div>
          </a>
        </div>
        
        <div class="md:col-span-7 space-y-4">
          <div class="bg-slate-950/60 border border-slate-800/80 rounded-xl p-4 space-y-2 text-xs leading-relaxed text-slate-300">
            <p class="font-bold text-rose-400 flex items-center gap-1.5">
              <span>💎</span><span>見どころ＆おすすめポイント</span>
            </p>
            <p>{html.escape(review_desc)}</p>
          </div>

          <div class="flex flex-col sm:flex-row items-center gap-3 pt-1">
            <a href="{clean_aff_url}" target="_blank" rel="noopener noreferrer sponsored" class="w-full sm:flex-1 py-3 px-5 text-center bg-gradient-to-r from-rose-600 via-rose-500 to-pink-600 hover:from-rose-500 hover:to-pink-500 text-white font-black text-xs sm:text-sm rounded-xl shadow-lg shadow-rose-600/30 transition flex items-center justify-center gap-2">
              <span>🔥</span>
              <span>{cta_btn_text}</span>
              <span class="text-xs opacity-80">›</span>
            </a>
          </div>
          <div class="flex items-center justify-between text-[11px] text-slate-400 px-1">
            <span class="text-emerald-400 font-bold">🔒 明細はDMM表記・即時視聴対応</span>
            <span>単体購入・セール対応</span>
          </div>
        </div>
      </div>

      {sample_images_html}
    </article>
    """

def reindex_cards(review_html):
    parts = review_html.split("<!-- 追加カード:")
    header = parts[0]
    cards = parts[1:]
    new_cards = []
    for idx, cp in enumerate(cards, 1):
        cp = re.sub(
            r'<span class="inline-flex items-center justify-center w-7 h-7 rounded-full bg-gradient-to-r from-rose-600 to-pink-600 text-white font-black text-xs shadow-md">\s*#\d+\s*</span>',
            f'<span class="inline-flex items-center justify-center w-7 h-7 rounded-full bg-gradient-to-r from-rose-600 to-pink-600 text-white font-black text-xs shadow-md">#{idx}</span>',
            cp
        )
        new_cards.append("<!-- 追加カード:" + cp)
    return header + "".join(new_cards)

# ==============================================
# Hub File Creator / Appender
# ==============================================
def update_hub(category_key, category_title, service, floor, keyword=None):
    now = datetime.now()
    year_str = str(now.year)
    month_str = f"{now.month:02d}"
    
    hub_id = f"feature_{year_str}_{month_str}_{category_key}_masterpiece_summary"
    hub_path = os.path.join(POSTS_DIR, f"{hub_id}.json")
    
    cached_cids = load_cache()
    items = fetch_fanza_items(service, floor, keyword=keyword, hits=15)
    
    new_items = []
    for item in items:
        cid = item.get("content_id")
        if cid and cid not in cached_cids:
            new_items.append(item)

    print(f"[{category_key}] Found {len(new_items)} new items to add for {year_str}-{month_str}")

    existing_data = None
    if os.path.exists(hub_path):
        with open(hub_path, "r", encoding="utf-8") as fp:
            existing_data = json.load(fp)

    is_manga = (service == "ebook" or service == "digital_book")
    all_actresses = []
    
    if existing_data:
        review_html = existing_data.get("review", "")
        cur_cards_count = len(re.findall(r'<!-- (?:追加カード|第\d+位 作品カード):', review_html))
        
        if new_items:
            new_cards_html = []
            for idx, item in enumerate(new_items):
                cid = item.get("content_id")
                cached_cids.add(cid)
                card = build_hub_card_html(item, cur_cards_count + idx + 1, category_title, service)
                new_cards_html.append(card)
                for a in item.get("iteminfo", {}).get("actress", []):
                    n = a.get("name")
                    if n and n not in all_actresses:
                        all_actresses.append(n)

            insert_marker = "<!-- HUB_CARDS_START -->"
            if insert_marker in review_html:
                review_html = review_html.replace(insert_marker, f"{insert_marker}\n{''.join(new_cards_html)}")
            else:
                review_html += "\n" + "".join(new_cards_html)

            # Re-index to ensure clean #1, #2, #3 numbering
            review_html = reindex_cards(review_html)
            existing_data["review"] = review_html
            existing_data["date"] = now.strftime("%Y-%m-%d %H:%M:%S")
            with open(hub_path, "w", encoding="utf-8") as fp:
                json.dump(existing_data, fp, ensure_ascii=False, indent=2)
            print(f"Updated existing hub: {hub_path}")
        else:
            print(f"[{category_key}] No new items to append.")
    else:
        cards_html = []
        for idx, item in enumerate(new_items):
            cid = item.get("content_id")
            cached_cids.add(cid)
            card = build_hub_card_html(item, idx + 1, category_title, service)
            cards_html.append(card)
            for a in item.get("iteminfo", {}).get("actress", []):
                n = a.get("name")
                if n and n not in all_actresses:
                    all_actresses.append(n)

        main_img = new_items[0].get("imageURL", {}).get("large") if new_items else ""
        first_cid = new_items[0].get("content_id") if new_items else ""
        
        full_title = f"【{year_str}年{int(month_str)}月最新{category_title}傑作選】FANZA話題の新作・神作タイトル完全速報まとめ"
        lead_desc = f"{year_str}年{int(month_str)}月にリリースされた注目の{category_title}を徹底網羅！FANZAで配信されたばかりの話題作・高評価タイトルを厳選して随時お届けしています。"

        hub_content = f"""<!-- キラー特集コンテナ -->
<div class="space-y-10 text-slate-200">
  <header class="bg-gradient-to-br from-slate-900 via-slate-900 to-rose-950/40 border border-slate-800 rounded-3xl p-6 md:p-10 shadow-2xl space-y-6">
    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-rose-600/20 border border-rose-500/30 text-rose-400 text-xs font-black tracking-wide">
      <span>🔥</span><span>FANZA厳選・{year_str}年{int(month_str)}月 話題の新作セレクション</span>
    </div>
    <div class="space-y-3">
      <h1 class="text-xl sm:text-2xl md:text-3xl font-black text-white leading-tight tracking-tight">
        {full_title}
      </h1>
      <p class="text-xs sm:text-sm text-slate-300 leading-relaxed max-w-4xl">
        {lead_desc}
      </p>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-2 text-xs">
      <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800 text-center space-y-1">
        <span class="text-base">🎬</span>
        <p class="font-bold text-white">公式プレビュー無料</p>
        <p class="text-[10px] text-slate-400">本編ダイジェスト即再生</p>
      </div>
      <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800 text-center space-y-1">
        <span class="text-base">🔒</span>
        <p class="font-bold text-white">クレカ明細安心</p>
        <p class="text-[10px] text-slate-400">DMM表記（作品名なし）</p>
      </div>
      <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800 text-center space-y-1">
        <span class="text-base">📱</span>
        <p class="font-bold text-white">スマホ・PC即視聴</p>
        <p class="text-[10px] text-slate-400">高画質ストリーミング</p>
      </div>
      <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800 text-center space-y-1">
        <span class="text-base">⚡</span>
        <p class="font-bold text-white">最新作随時更新</p>
        <p class="text-[10px] text-slate-400">注目作を速報レビュー</p>
      </div>
    </div>
  </header>

  <section class="space-y-8">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
      <h2 class="text-lg sm:text-xl font-black text-white flex items-center gap-2">
        <span>🔥</span><span>{category_title} 注目タイトル一覧</span>
      </h2>
      <span class="text-xs text-rose-400 font-bold">新着順に随時追加中</span>
    </div>

    <!-- HUB_CARDS_START -->
    <div class="space-y-6">
      {''.join(cards_html)}
    </div>
    <!-- HUB_CARDS_END -->
  </section>

  <section class="bg-gradient-to-r from-rose-950/60 via-slate-900 to-slate-950 border border-rose-500/30 rounded-2xl p-6 sm:p-8 text-center space-y-4 shadow-2xl">
    <h3 class="text-lg sm:text-xl font-black text-white">
      さらに多くの最新作・見放題作品をお探しの方へ
    </h3>
    <p class="text-xs sm:text-sm text-slate-300 max-w-2xl mx-auto leading-relaxed">
      FANZA公式では15万本以上が見放題になる「見放題chプレミアム」や、期間限定の半額セール・独占配信タイトルを常時配信しています。
    </p>
    <div class="flex flex-col sm:flex-row items-center justify-center gap-3 pt-2">
      <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2F&af_id={SITE_AFFILIATE_ID}&ch=api" target="_blank" rel="noopener noreferrer sponsored" class="w-full sm:w-auto px-8 py-3.5 bg-gradient-to-r from-rose-600 to-pink-600 hover:from-rose-500 hover:to-pink-500 text-white font-black text-xs sm:text-sm rounded-xl shadow-lg transition">
        👉 FANZA公式 総合TOPへ
      </a>
      <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fmonthly%2Fpremium%2F&af_id={SITE_AFFILIATE_ID}" target="_blank" rel="noopener noreferrer sponsored" class="w-full sm:w-auto px-8 py-3.5 bg-slate-800 hover:bg-slate-700 border border-amber-400/50 text-amber-300 font-black text-xs sm:text-sm rounded-xl shadow transition">
        👑 15万本見放題chをチェック
      </a>
    </div>
  </section>
</div>
"""
        aff_url = f"https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D{first_cid}&af_id={SITE_AFFILIATE_ID}&ch=api" if not is_manga else f"https://al.fanza.co.jp/?lurl=https%3A%2F%2Fbook.dmm.co.jp%2Fproduct%2F{first_cid}%2F&af_id={SITE_AFFILIATE_ID}&ch=api"

        post_data = {
            "id": hub_id,
            "title": full_title,
            "date": now.strftime("%Y-%m-%d %H:%M:%S"),
            "hinban": f"{category_key.upper()}-{year_str}-{month_str}",
            "price": "300~",
            "maker": f"FANZA{category_title}",
            "actresses": all_actresses[:15],
            "genres": ["ハイビジョン", "独占配信", "最新作", "まとめ", "ランキング"],
            "image": main_img,
            "review": hub_content,
            "affiliate_url": aff_url
        }

        with open(hub_path, "w", encoding="utf-8") as fp:
            json.dump(post_data, fp, ensure_ascii=False, indent=2)
        print(f"Created new hub: {hub_path}")

    save_cache(cached_cids)

def main():
    print("--- Starting Monthly Hub Auto-Update ---")
    update_hub("latest_av", "総合新作AV", "digital", "videoa")
    update_hub("mature_wife", "人妻・熟女", "digital", "videoa", keyword="人妻")
    update_hub("busty_beauty", "巨乳・爆乳", "digital", "videoa", keyword="巨乳")
    update_hub("single_actress", "単体専属・美少女", "digital", "videoa", keyword="単体")
    update_hub("amateur_pickup", "素人・ハメ撮り", "digital", "videoa", keyword="素人")
    update_hub("lesbian_yuri", "レズ・百合", "digital", "videoa", keyword="レズ")
    update_hub("manga_comic", "成人コミック・新作漫画", "ebook", "comic")
    print("--- Monthly Hub Auto-Update Finished Successfully ---")

if __name__ == "__main__":
    main()
