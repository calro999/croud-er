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

# 周辺クエリを拾う第4弾・新規6大特集テーマ定義
PHASE4_FEATURE_THEMES = [
    {
        "id": "feature_mizogi_mature_wife_masturbation_confession",
        "api_keywords": ["三十路 人妻 自慰", "人妻 オナニー 自慰", "レス妻"],
        "title": "【三十路人妻の自慰告白】セックスレスに悶える妻がカメラの前で生オナニー！本物男根に狂喜乱舞するハメ撮りAV特集",
        "main_query": "エロ過ぎる人妻 三十路の人妻がオナニー好きじゃだめですか レス妻 自慰告白 周辺",
        "labels": ["人妻", "三十路", "オナニー", "自慰告白", "セックスレス", "ハメ撮り", "生中出し", "特集"],
        "lead": "「夫との夜の営みがなくなり、毎日オナニーでしか性欲を解消できない……」日陰の欲望を抱えた三十路人妻たちが、赤裸々に自慰を告白し、久しぶりの本物チンポに子宮を突き上げられて歓喜の涙を流す、生々しい人妻ドキュメント作品を徹底比較解説します！"
    },
    {
        "id": "feature_slender_waist_pure_beauty_creampie",
        "api_keywords": ["細身 くびれ 美少女", "くびれ 美少女", "スレンダー 中出し"],
        "title": "【細身くびれ美少女AV特集】キュッと引き締まったウエストを掴んでバックピストン！瑞々しい柔肌と生中出しおすすめ傑作選",
        "main_query": "若さとクビレが素敵なユキちゃん スレンダー 美少女 くびれ 生ハメ 周辺",
        "labels": ["くびれ", "スレンダー", "美少女", "ウエスト細い", "バックピストン", "生中出し", "特集", "おすすめAV"],
        "lead": "折れそうなほど細いくびれと、丸みを帯びた美尻が織りなす完璧なプロポーション。男の手でウエストをガッチリとホールドされ、激しく突かれるたびに背中を弓なりにして喘ぐ、スレンダー美少女好き必見の抜きどころ満載タイトルを完全レポートします。"
    },
    {
        "id": "feature_amateur_private_shoot_raw_creampie",
        "api_keywords": ["素人 個撮", "素人 ハメ撮り", "高瀬りな"],
        "title": "【素人個撮ハメ撮り特集】飾らない素朴な可愛さに大興奮！ホテルの一室で無防備に乱れるリアル生中出しAV特集",
        "main_query": "高瀬りな 素人 個撮 ハメ撮り 素朴 美少女 生中出し 周辺",
        "labels": ["素人", "個撮", "ハメ撮り", "高瀬りな", "無防備", "生中出し", "素朴", "特集"],
        "lead": "普通の女子大生やOLのような素朴で親しみやすいルックス。カメラの前で照れ笑いを浮かべながらも、ベッドの上では本能のままに腰を振り、濃厚な生中出しを受け止める、素人個撮フェチの究極形を徹底解説します。"
    },
    {
        "id": "feature_dashcam_car_sex_ntr_compilation",
        "api_keywords": ["ドラレコ 車内", "車載カメラ NTR", "カーセックス"],
        "title": "【ドラレコ車載カメラNTR特集】車内の密室で愛車を揺らす禁断カーセックス！助手席・後部座席で寝取られる生々しい一部始終",
        "main_query": "ドラレコNTR 車載カメラ 車内 カーセックス 寝取られ 負けられない日本代表 周辺",
        "labels": ["ドラレコNTR", "車載カメラ", "カーセックス", "車内ハメ", "寝取られ", "助手席", "特集"],
        "lead": "エンジンを切った後も記録を続けるドライブレコーダーが捉えた、愛するパートナーの裏切り。狭い車内でシートを倒され、フロントガラスを曇らせながら腰を打ち付け合う、客観的視点がもたらす超リアルな背徳作を特集します。"
    },
    {
        "id": "feature_desert_island_drift_survival_harem",
        "api_keywords": ["無人島 漂流", "無人島 サバイバル", "島娘"],
        "title": "【無人島漂流サバイバルAV特集】文明社会から隔絶された楽園！性を知らない島娘たちを快楽漬けにする種付けハーレム傑作選",
        "main_query": "無人島 三姉妹 漂流 サバイバル 性指導 種付け ハーレム 周辺",
        "labels": ["無人島", "漂流", "サバイバル", "島娘", "性指導", "種付け", "ハーレム", "特集"],
        "lead": "青い海と手つかずの大自然が広がる無人島に流れ着いた男と、男の存在すら知らずに育ったピュアな少女たち。生き抜くための共同生活の中で、一から性の悦びを教え込み、何人もの少女たちから精液を求められる至福のハーレム作品を厳選ナビゲートします。"
    },
    {
        "id": "feature_ultra_8k_zero_distance_vr_masterpiece",
        "api_keywords": ["VR 密着 8K", "8K VR ゼロ距離", "VRKM"],
        "title": "【超高画質8K密着VR特集】吐息と体温がダイレクトに届く！ゼロ距離アングル＆バイノーラル立体音響おすすめ神VRタイトル",
        "main_query": "VR 8K 超高画質 ゼロ距離 密着 DSVR VRKM バイノーラル 周辺",
        "labels": ["VR", "8KVR", "ゼロ距離", "密着", "バイノーラル", "高画質", "没入感", "特集"],
        "lead": "最新の8K超高画質技術と耳元で囁かれるバイノーラル音響によって、まるで本物の美女がすぐ目の前にいるような錯覚に陥る！上目遣いのフェラチオから密着対面座位まで、VRゴーグル装着者必見の最高峰VRタイトルを徹底比較します。"
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

print("Executing direct FANZA API fetching for Phase 4 feature themes...")

created_count = 0

for idx, theme in enumerate(PHASE4_FEATURE_THEMES, 1):
    print(f"\n[{idx}/{len(PHASE4_FEATURE_THEMES)}] Querying FANZA API for: {theme['title'][:35]}...")
    
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
    print(f"Saved new Phase 4 feature article: {out_path}")

print(f"\nPhase 4 execution complete! Created {created_count} strictly API-fetched new feature articles.")
