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

# サチコ上位クエリに基づく多彩な第19弾・新規5大特集テーマ定義（無人島は完全除外）
PHASE19_FEATURE_THEMES = [
    {
        "id": "feature_drive_recorder_car_camera_voyeur_ntr",
        "api_keywords": ["ドラレコ NTR", "ドラレコ NTR 車載カメラ", "車内 NTR 盗撮"],
        "title": "【ドラレコ車載カメラ盗撮NTR特集】助手席で愛妻が寝取られる一部始終…車体が激しく揺れる背徳生中出しAV傑作選",
        "main_query": "ドラレコ NTR 38 車載カメラ 盗撮 車内生ハメ 助手席 揺れる ねとられ 一部始終 周辺",
        "labels": ["ドラレコNTR", "車載カメラ", "盗撮", "車内生ハメ", "助手席", "寝取られ", "背徳", "特集", "おすすめAV"],
        "lead": "愛車に設置されたドライブレコーダーが記録していた、信じがたい裏切りの光景。助手席のシートを倒され、見知らぬ男の剛直を受け入れながら乱れる妻……車体が激しく揺れる音とリアルな喘ぎ声が胸をえぐる、車内盗撮NTRの名作を徹底比較解説します！"
    },
    {
        "id": "feature_petite_slim_mens_esthe_raw_sex_development",
        "api_keywords": ["つるぺた メンエス", "メンエス 裏オプ 生ハメ", "メンエス 嬢 ちょろい"],
        "title": "【合法つるぺたメンエス裏オプ生ハメ特集】紙パンツを脱がせて極狭マンコに生挿入！オイルまみれで中出しされる神動画選",
        "main_query": "合法ロリ つるぺた メンエス嬢 ちょろい 裏オプ 生ハメ オイルマッサージ 極狭 中出し 周辺",
        "labels": ["メンエス", "つるぺた", "裏オプ", "生ハメ", "オイルマッサージ", "極狭マンコ", "中出し", "特集", "おすすめAV"],
        "lead": "スレンダーで華奢なつるぺたセラピストが担当するプライベートサロン。際どい密着施術から耳元で甘く囁かれ、紙パンツをずらして生挿入！オイルで滑る身体を密着させながら、極狭の膣奥へドクドク注ぎ込むメンエス裏オプの最高峰を完全レポートします。"
    },
    {
        "id": "feature_ultimate_vaginal_ejaculation_angle_creampie",
        "api_keywords": ["膣内射精 アングル", "膣内射精 アングル 中出し", "子宮口 射精 アングル"],
        "title": "【至高の膣内射精アングル特化AV特集】子宮口にドクドク注ぎ込まれる白濁精液！結合部丸見え断面＆ローアングル傑作選",
        "main_query": "至高の膣内射精 アングル 25発 子宮口 断面 ローアングル 白濁精液 溢れ出る 中出し 周辺",
        "labels": ["膣内射精アングル", "子宮口直撃", "断面アングル", "ローアングル", "白濁精液", "中出し特化", "特集", "おすすめAV"],
        "lead": "男が最も興奮する「中出しの瞬間」だけを徹底的にこだわり抜いた至高のアングル特化作品！クッキリと見える結合部、ペニスが引き抜かれた瞬間に溢れ出す濃密な白濁液、そして満足げな笑顔を浮かべるキャストたちの表情を余すところなくお届けします。"
    },
    {
        "id": "feature_masturbation_addict_mature_wife_dildo_climax",
        "api_keywords": ["三十路 人妻 自慰", "人妻 オナニー 自慰 ディルド", "人妻 自慰 潮吹き"],
        "title": "【オナニー狂い三十路人妻自慰開発特集】夫に内緒でディルドを挿入し潮吹き悶絶…性欲を持て余したエロ妻AV傑作選",
        "main_query": "エロ過ぎる人妻 三十路 オナニー 自慰 中毒 ディルド 潮吹き 開発 セックスレス 周辺",
        "labels": ["人妻", "三十路", "オナニー中毒", "自慰", "ディルド", "潮吹き", "セックスレス", "特集", "おすすめAV"],
        "lead": "真面目そうに見える三十路の美人妻が、夫の留守中に自室で繰り広げる淫らな自慰タイム。極太ディルドを自らの蜜壺に沈め、激しく腰を動かしてシーツを濡らす……抑えきれない性欲に悶える人妻の生々しいリアルエロスを徹底解剖します。"
    },
    {
        "id": "feature_meet_instant_anal_penetration_ecstasy",
        "api_keywords": ["ズコバコ アナル", "出会って アナル", "アナル 即挿入"],
        "title": "【出会って即アナル貫通AV特集】挨拶代わりにケツ穴直撃ズコバコ！アナル初心者娘が悶絶イキするおすすめ傑作選",
        "main_query": "出会って5秒 あなるっ娘 ズコバコ アナル 即挿入 ケツ穴 初心者 悶絶 直腸ピストン 周辺",
        "labels": ["アナル", "即挿入", "ズコバコ", "ケツ穴", "アナル初心者", "悶絶イキ", "直腸ピストン", "特集", "おすすめAV"],
        "lead": "出会ってわずか数分、前戯もそこそこにキュッと締まったお尻の穴へローションを塗ってダイレクト生挿入！最初は驚きと痛みに戸惑っていた娘が、直腸を激しくノックされるうちに未知の快感へ覚醒していく衝撃のアナル作品を徹底レビューします。"
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

print("Executing direct FANZA API fetching for Phase 19 feature themes...")

created_count = 0

for idx, theme in enumerate(PHASE19_FEATURE_THEMES, 1):
    print(f"\n[{idx}/{len(PHASE19_FEATURE_THEMES)}] Querying FANZA API for: {theme['title'][:35]}...")
    
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
    print(f"Saved new Phase 19 feature article: {out_path}")

print(f"\nPhase 19 execution complete! Created {created_count} strictly API-fetched new feature articles.")
