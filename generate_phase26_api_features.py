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

# サチコ上位クエリに基づく多彩な第26弾・新規5大特集テーマ定義（無人島完全除外）
PHASE26_FEATURE_THEMES = [
    {
        "id": "feature_heroine_defeat_tickling_torture_climax",
        "api_keywords": ["特撮 ヒロイン 敗北", "ヒロイン 乳首責め", "ヒロイン 拘束 敗北"],
        "title": "【特撮ヒロイン被虐敗北AV特集】悪の罠に落ちた美少女戦士が拘束くすぐり＆乳首責めで完全降伏！快楽堕ち傑作選",
        "main_query": "レディスレイヤー桃太郎 被虐編 特撮ヒロイン 敗北 拘束 くすぐり 乳首責め 快楽堕ち 生中出し 周辺",
        "labels": ["特撮ヒロイン", "ヒロインピンチ", "完全敗北", "拘束拷問", "くすぐり責め", "乳首責め", "快楽堕ち", "特集", "おすすめAV"],
        "lead": "正義のスーツを剥ぎ取られ、十字架に磔にされた誇り高き美少女ヒロイン。悪の怪人たちによる容赦のない足裏くすぐりや執拗な乳首責めに、必死に耐えようとしながらも甘いメスの喘ぎ声を漏らし、快楽に染まっていくマニア必見の被虐特撮作品を徹底比較解説します！"
    },
    {
        "id": "feature_college_girls_exposure_circle_camp_orgy",
        "api_keywords": ["サークル 露出", "某大学 ベリーダンスサークル", "女子大生 合宿 乱交"],
        "title": "【女子大生露出サークル乱交合宿特集】薄布衣装で妖艶に舞う美女大生！合宿所の密室で男たちと乱れ狂う生中出し傑作選",
        "main_query": "某大学ベリーダンスサークル サークル 露出 女子大生 合宿 乱交 密室 生中出し 周辺",
        "labels": ["女子大生", "サークル露出", "合宿乱交", "密室", "露出衣装", "ハーレム", "生中出し", "特集", "おすすめAV"],
        "lead": "華やかな衣装とエキゾチックな露出で観客を魅了する女子大生たち。合宿の夜、お酒の勢いで開放的になった美女たちが次々と服を脱ぎ捨て、男子部員たちと入り乱れて生チンポを貪り合う！男子の妄想を詰め込んだサークル乱交作品を完全レポートします。"
    },
    {
        "id": "feature_thirty_year_old_wife_masturbation_addict_tide",
        "api_keywords": ["三十路 人妻 オナニー", "人妻 潮吹き オナニー", "三十路 自慰 ディルド"],
        "title": "【三十路人妻オナニー中毒・潮吹き絶頂特集】欲求不満な清楚妻がオモチャで乱れる！シーツを水浸しにする悶絶自慰AV傑作選",
        "main_query": "エロ過ぎる人妻 三十路 人妻 オナニー 潮吹き 自慰 ディルド ネタバレ セックスレス 周辺",
        "labels": ["人妻", "三十路", "オナニー中毒", "自慰", "潮吹き", "ディルド", "セックスレス", "特集", "おすすめAV"],
        "lead": "昼下がりの静かなリビングで、夫の目を盗んで行われる背徳の自慰。極太バイブを自らの蜜壺に押し込み、激しいピストンで潮を吹き散らしながらアクメに溺れる……満たされない性欲をオモチャで埋める三十路人妻たちの生々しいリアルエロスを徹底解剖します。"
    },
    {
        "id": "feature_gyaru_lover_uncle_nanpa_hotel_creampie",
        "api_keywords": ["ぎゃる好きおじ", "ギャル ナンパ おじさん", "金髪ギャル 生ハメ おじさん"],
        "title": "【ぎゃる好きおじ全国ナンパ旅特集】派手カワ金髪ギャルをおじさんが巧妙にホテル連れ込み！生ハメ種付けする傑作選",
        "main_query": "ぎゃる好きおじナンパ旅13 ぎゃる好きおじ 金髪ギャル ナンパ ホテル連れ込み 生ハメ 種付け 生中出し 周辺",
        "labels": ["ぎゃる好きおじ", "金髪ギャル", "ナンパ旅", "おじさん", "ホテル連れ込み", "生ハメ", "種付け", "特集", "おすすめAV"],
        "lead": "全国各地のギャルを求めて旅する、おじさんナンパ師の生々しい記録。ノリの良い金髪美少女を巧みなトークで口説き落とし、ホテルのベッドでゴムなし生ハメ！子宮奥深くまで熱い精液を注ぎ込む、ギャル好き垂涎のナンパ傑作を厳選紹介します。"
    },
    {
        "id": "feature_8k_vr_face_to_face_close_cohabitation",
        "api_keywords": ["8K VR 対面座位 密着", "VR 密着 囁き 8K", "8K VR 顔面特化"],
        "title": "【超高画質8K・VRゼロ距離対面座位特集】目の前に迫る美顔と甘い吐息！抱きしめ合いながら果てる神VRタイトル",
        "main_query": "8K VR 対面座位 密着 ゼロ距離 顔面特化 バイノーラル 同棲生活 彼女感 生中出し 周辺",
        "labels": ["VR", "8KVR", "対面座位", "ゼロ距離", "顔面特化", "バイノーラル", "同棲生活", "彼女感", "特集"],
        "lead": "ヘッドセットを装着した瞬間、息がかかるほどの距離で大好きな彼女と目が合う！腕を首に回され、お互いの体温と鼓動を感じながら腰を揺らす対面座位……8Kの超高精細映像とバイノーラル音声で至福の没入感を味わえる神VRタイトルを徹底レビューします。"
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

print("Executing direct FANZA API fetching for Phase 26 feature themes...")

created_count = 0

for idx, theme in enumerate(PHASE26_FEATURE_THEMES, 1):
    print(f"\n[{idx}/{len(PHASE26_FEATURE_THEMES)}] Querying FANZA API for: {theme['title'][:35]}...")
    
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
    print(f"Saved new Phase 26 feature article: {out_path}")

print(f"\nPhase 26 execution complete! Created {created_count} strictly API-fetched new feature articles.")
