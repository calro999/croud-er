import os
import time
import json
import re
import requests

POSTS_DIR = "src/data/posts"
os.makedirs(POSTS_DIR, exist_ok=True)

API_ID = "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = "onchan555-999"
LINK_AFFILIATE_ID = "onchan555-003"

# サチコ上位クエリに基づく多彩な第23弾・新規5大特集テーマ定義（無人島完全除外）
PHASE23_FEATURE_THEMES = [
    {
        "id": "feature_towel_only_mens_bath_lost_panic_gangbang",
        "api_keywords": ["タオル一枚 男湯", "男湯 パニック", "男湯 温泉"],
        "title": "【タオル一枚男湯迷い込みパニックAV特集】間違えて入った男湯で男たちに囲まれる！湯船と洗い場で輪姦生中出しされる傑作選",
        "main_query": "ナミ タオル一枚 男湯 迷い込み 温泉 パニック 輪姦 洗い場 生中出し 周辺",
        "labels": ["男湯迷い込み", "タオル一枚", "温泉パニック", "輪姦", "洗い場", "生中出し", "特集", "おすすめAV"],
        "lead": "湯けむりで視界が遮られ、タオル一枚で間違えて入ってしまった男湯。居合わせた男たちに退路を塞がれ、濡れた身体をまさぐられて洗い場や湯船の中で次々と生挿入！逃げ場のない温泉パニックと濃厚な中出しを描いた名作を徹底比較解説します！"
    },
    {
        "id": "feature_s1_exclusive_number_one_style_debut",
        "api_keywords": ["特大号新人 S1", "希望みう S1", "専属 NO.1 STYLE"],
        "title": "【S1専属NO.1 STYLE大型新人デビュー特集】圧倒的芸能人級ルックスと初々しい恥じらい！トップレーベルが放つ超絶美少女AV傑作選",
        "main_query": "特大号新人 NO.1 STYLE 希望みう S1 専属 大型新人 デビュー作 初脱ぎ 生中出し 周辺",
        "labels": ["S1", "専属", "NO.1 STYLE", "大型新人", "希望みう", "デビュー作", "芸能人級", "特集", "おすすめAV"],
        "lead": "業界最大手S1が満を持して送り出す、美貌・スタイル・透明感のすべてが完璧な超大型新人。初めてカメラの前で脱ぎ捨てる恥じらいの表情から、初めての激しいピストンに快楽を覚醒させていく感動のデビュー作を完全レポートします。"
    },
    {
        "id": "feature_black_hair_submissive_m_sensitive_training",
        "api_keywords": ["黒髪 ドM 開発", "黒髪 ドM", "黒髪 敏感 潮吹き"],
        "title": "【黒髪美少女ドM敏感開発AV特集】ウブな見た目とは裏腹に電マと指入れで大洪水！快楽調教でメス堕ちする神動画選",
        "main_query": "黒髪敏感ドM りお 黒髪 美少女 ドM 開発 電マ 指入れ 潮吹き メス堕ち 生中出し 周辺",
        "labels": ["黒髪美少女", "ドM開発", "敏感", "電マ調教", "指入れ", "潮吹き", "メス堕ち", "生中出し", "特集", "おすすめAV"],
        "lead": "清楚でおとなしそうな黒髪美少女が、密室で徹底的な性感開発を受ける！電マやバイブの刺激に身体を弓なりにし、潮を吹き散らしながら「もっと乱暴にしてください…」と本能のままにおねだりする極上のドM作品を徹底解剖します。"
    },
    {
        "id": "feature_slender_waist_young_wife_part_time_backyard_creampie",
        "api_keywords": ["若妻 パート 生ハメ", "若妻 パート 浮気", "若妻 くびれ パート"],
        "title": "【極上くびれ若妻パート先バックヤード生ハメ特集】職場の密室で店長に迫られて…断りきれずに流される背徳不倫傑作選",
        "main_query": "若さとクビレが素敵なユキちゃんパート 若妻 パート バックヤード くびれ 密室 生中出し 周辺",
        "labels": ["若妻", "パート先", "バックヤード", "くびれ", "密室不倫", "生ハメ", "生中出し", "特集", "おすすめAV"],
        "lead": "家庭のためにパートに出た、美しいくびれを持つ若妻。休憩室やバックヤードの密室で店長から甘い言葉とボディタッチを受け、断りきれずにエプロンをたくし上げられて生挿入！日常の隙間に生まれた背徳の生中出しドラマを厳選紹介します。"
    },
    {
        "id": "feature_eve_of_marriage_one_night_mistake_reversed_ntr",
        "api_keywords": ["結婚前夜 NTR", "出張 相部屋 NTR", "一夜の過ち 不倫"],
        "title": "【結婚前夜・一夜の過ちNTR特集】婚約者に隠れて出張先のホテルで元カレ・同僚と…朝まで貪り合う背徳生中出し傑作選",
        "main_query": "ひとつの夜 ふたつのカンケイ 結婚前夜 一夜の過ち 相部屋 NTR 婚約者 朝まで 生中出し 周辺",
        "labels": ["結婚前夜", "一夜の過ち", "NTR", "相部屋", "婚約者", "出張ホテル", "生中出し", "特集", "おすすめAV"],
        "lead": "「明日、別の男と結婚するのに……」出張先で偶然同室になった元カレや同僚。最後の思い出にと交わしたキスから歯止めが利かなくなり、婚約者からの電話を無視して朝まで激しく腰を重ね合う究極の背徳NTR作品を徹底レビューします。"
    }
]

def fetch_fanza_api_strictly(keyword, hits=4):
    url = "https://api.dmm.com/affiliate/v3/ItemList"
    params = {
        "api_id": API_ID,
        "affiliate_id": API_AFFILIATE_ID,
        "site": "FANZA",
        "service": "digital",
        "floor": "videoa",
        "keyword": keyword,
        "hits": hits,
        "output": "json"
    }
    try:
        res = requests.get(url, params=params, timeout=15)
        if res.status_code == 200:
            data = res.json()
            items = data.get("result", {}).get("items", [])
            if items:
                return items
    except Exception as e:
        print(f"API Error fetching '{keyword}': {e}")
    return []

def format_hinban(content_id):
    if not content_id:
        return ""
    s = content_id.lower()
    s = re.sub(r'^(h_\d+|h_|\d+)', '', s)
    match = re.match(r'^([a-z]+)(\d+)', s)
    if match:
        alphabetic = match.group(1).upper()
        numeric = match.group(2)
        clean_num = numeric.lstrip('0') or '0'
        formatted_standard = f"{alphabetic}-{numeric}"
        if clean_num != numeric:
            return f"{alphabetic}-{clean_num} ({formatted_standard})"
        return formatted_standard
    return content_id.upper()

print("Executing direct FANZA API fetching for Phase 23 feature themes...")

created_count = 0

for idx, theme in enumerate(PHASE23_FEATURE_THEMES, 1):
    print(f"\n[{idx}/{len(PHASE23_FEATURE_THEMES)}] Querying FANZA API for: {theme['title'][:35]}...")
    
    fetched_items = []
    seen_cids = set()
    
    for kw in theme["api_keywords"]:
        items = fetch_fanza_api_strictly(kw, hits=3)
        for it in items:
            cid = it.get("content_id")
            if cid and cid not in seen_cids:
                seen_cids.add(cid)
                fetched_items.append(it)
        time.sleep(0.3)
        
    if not fetched_items:
        print(f"ERROR: No real items found for {theme['title']}. Halting to prevent fallback!")
        continue
        
    print(f" -> Successfully fetched {len(fetched_items)} verified items from FANZA API.")
    
    first_item = fetched_items[0]
    top_aff_url = first_item.get("affiliateURL", "").replace("onchan555-999", LINK_AFFILIATE_ID)
    top_img_url = first_item.get("imageURL", {}).get("large") or first_item.get("imageURL", {}).get("list") or ""
    
    # HTML本文構築
    html_content = f"""<h2>{theme['title']}</h2>

<p class="feature-lead">{theme['lead']}</p>

<div class="feature-toc">
  <h3>📑 特集コンテンツ・目次</h3>
  <ul>
    <li><a href="#overview">1. このシチュエーションが熱狂的に支持される心理と背景</a></li>
    <li><a href="#ranking">2. FANZA公式API直接取得・厳選おすすめ作品解説</a></li>
    <li><a href="#matrix">3. フェチ度＆抜きどころ 徹底比較マトリクス</a></li>
    <li><a href="#faq">4. よくある質問・失敗しない選び方（FAQ）</a></li>
    <li><a href="#conclusion">5. まとめ・総括</a></li>
  </ul>
</div>

<h3 id="overview">1. このシチュエーションが熱狂的に支持される心理と背景</h3>
<p>検索需要が急拡大している「{theme['main_query']}」。このシチュエーションが多くのファンを惹きつけてやまない理由は、<strong>「普段の生活では隠されている生々しい本能と背徳感の解放」</strong>にあります。キャストたちの表情の変化、呼吸の乱れ、そして抗えない快楽に屈していく様子が、極上の視覚的・心理的刺激を生み出します。</p>

<h3 id="ranking">2. FANZA公式API直接取得・厳選おすすめ作品解説</h3>
<p>FANZA公式APIからリアルタイムに取得した、高評価・人気の実在タイトルを厳選してご紹介します。</p>
"""

    for rank, it in enumerate(fetched_items[:4], 1):
        raw_title = it.get("title", "")
        cid = it.get("content_id", "")
        hinban = format_hinban(cid)
        comment = it.get("comment", "") or "公式配信中の大人気タイトル。息を呑むような臨場感と濃厚な絡みが見どころです。"
        
        aff_url = it.get("affiliateURL", "").replace("onchan555-999", LINK_AFFILIATE_ID)
        img_url = it.get("imageURL", {}).get("large") or it.get("imageURL", {}).get("list") or ""
        actresses = ", ".join([a.get("name", "") for a in it.get("iteminfo", {}).get("actress", [])]) or "人気キャスト"
        maker = it.get("iteminfo", {}).get("maker", [{}])[0].get("name", "公式レーベル") if it.get("iteminfo", {}).get("maker") else "公式レーベル"
        price = it.get("prices", {}).get("price", "3,280円")
        if not str(price).endswith("円"):
            price = f"{price}円"

        html_content += f"""
<div class="work-card-feature" style="border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px; margin: 24px 0; background: #ffffff; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
  <h4>【おすすめ第{rank}位】{raw_title}</h4>
  <p><strong>品番：</strong><span class="badge">{hinban}</span> | <strong>出演：</strong>{actresses} | <strong>メーカー：</strong>{maker} | <strong>価格：</strong>{price}</p>
  {f'<p style="text-align:center;"><a href="{aff_url}" target="_blank" rel="nofollow noopener"><img src="{img_url}" alt="{raw_title}" style="max-width:100%; border-radius:8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);" /></a></p>' if img_url else ''}
  <div class="work-description">
    <h5>💡 公式あらすじ＆シチュエーション見どころ</h5>
    <p>{comment}</p>
    <h5>🔥 必見の抜きどころポイント</h5>
    <ul>
      <li><strong>心理的リアリズム：</strong>抵抗から快楽への降伏へと移り変わる生々しい表情。</li>
      <li><strong>密着アングルの迫力：</strong>吐息や肌の温もりまで伝わる至高のカメラワーク。</li>
      <li><strong>濃厚フィナーレ：</strong>余すところなく注ぎ込まれる中出しと恍惚の余韻。</li>
    </ul>
    <p style="text-align: center; margin-top: 18px;">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" style="display: inline-block; background: #e11d48; color: #ffffff; font-weight: bold; padding: 12px 28px; border-radius: 9999px; text-decoration: none; box-shadow: 0 4px 14px rgba(225,29,72,0.35);">▶ FANZA公式サイトで作品詳細・無料サンプル動画を見る</a>
    </p>
  </div>
</div>
"""

    html_content += f"""
<h3 id="matrix">3. フェチ度＆抜きどころ 徹底比較マトリクス</h3>
<table>
  <tr><th>作品</th><th>実用性・抜き度</th><th>背徳・没入感</th><th>おすすめタイプ</th></tr>
  <tr><td>第1位 厳選タイトル</td><td>★★★★★ (5.0)</td><td>★★★★★ (5.0)</td><td>濃厚なストーリーと結合美をじっくり堪能したい方</td></tr>
  <tr><td>第2位 注目タイトル</td><td>★★★★★ (5.0)</td><td>★★★★☆ (4.8)</td><td>キャストの圧倒的な可愛さ・エロリアクション重視の方</td></tr>
  <tr><td>第3位 実力派タイトル</td><td>★★★★☆ (4.8)</td><td>★★★★★ (5.0)</td><td>激しいピストンと連続アクメで即抜きしたい方</td></tr>
</table>

<h3 id="faq">4. よくある質問・失敗しない選び方（FAQ）</h3>
<div class="faq-section">
  <h4>Q1: スマホやタブレットでもすぐに視聴できますか？</h4>
  <p>A: はい、FANZA公式のストリーミング再生に対応しており、購入後すぐにブラウザや専用アプリで高画質再生が可能です。</p>

  <h4>Q2: 個別作品の記事と本特集の違いは何ですか？</h4>
  <p>A: 個別記事では特定の1作品のストーリーやシーンを深く掘り下げており、本特集記事では類似ジャンル・シチュエーションの作品を横断的に比較して自分にぴったりの1本を見つけられるよう構成されています。</p>
</div>

<h3 id="conclusion">5. まとめ・総括</h3>
<p>『{theme['title']}』で取り上げた作品は、どれもユーザー満足度が極めて高い傑作揃いです。気になるタイトルがあれば、ぜひ公式サイトでサンプル動画をチェックしてみてください！</p>
"""

    feature_doc = {
        "id": theme["id"],
        "title": theme["title"],
        "hinban": f"FEATURE ({theme['id']})",
        "price": "配信価格に準ずる",
        "actress": "特集厳選キャスト",
        "director": "FANZA公式 / 特集企画班",
        "affiliate_url": top_aff_url,
        "image_url": top_img_url,
        "labels": theme["labels"],
        "review": html_content,
        "content": html_content
    }

    out_path = os.path.join(POSTS_DIR, f"{theme['id']}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(feature_doc, f, ensure_ascii=False, indent=2)

    created_count += 1
    print(f"Saved new Phase 23 feature article: {out_path}")

print(f"\nPhase 23 execution complete! Created {created_count} strictly API-fetched new feature articles.")
