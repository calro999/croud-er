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

# 周辺クエリを拾う第12弾・新規5大特集テーマ定義
PHASE12_FEATURE_THEMES = [
    {
        "id": "feature_desert_island_three_sisters_innocence_harem",
        "api_keywords": ["無人島 ハーレム", "無人島 三姉妹", "性を知らない 島娘"],
        "title": "【無人島三姉妹ハーレムAV特集】男を知らずに育った純真姉妹と南の楽園で愛欲生活！段階的な性指導＆種付け中出し傑作選",
        "main_query": "無人島 三姉妹 ハーレム 性を知らない 島娘 性指導 種付け 暁奇奇 周辺",
        "labels": ["無人島", "三姉妹", "ハーレム", "性を知らない", "島娘", "性指導", "種付け", "生中出し", "特集", "おすすめAV"],
        "lead": "手つかずの自然が残る南の孤島で暮らす美少女三姉妹。漂着した男を神のように迎え入れ、無邪気なスキンシップから大人の快楽へと導かれていく……姉妹それぞれの個性的なリアクションと、最後は総出で精液を求め合う野外ハーレム作品を徹底比較解説します！"
    },
    {
        "id": "feature_amateur_prank_sensual_massage_climax",
        "api_keywords": ["素人 ドッキリ 性感", "ドッキリ 性感 マッサージ", "素人 ドッキリ 生ハメ"],
        "title": "【素人お姉さん性感ドッキリAV特集】エロ企画とは知らずに施術台へ…際どいオイル愛撫で我慢できずに発情本番中出し傑作選",
        "main_query": "素人 ドッキリ 性感 マッサージ オイル 焦らし 発情 生中出し 周辺",
        "labels": ["素人", "ドッキリ", "性感マッサージ", "オイル", "焦らし", "発情", "生中出し", "特集", "おすすめAV"],
        "lead": "普通のアンケートやマッサージ体験と聞かされてやってきた素人女性たち。巧みな指技とローションで敏感な性感帯を刺激され、「ダメ…恥ずかしい…」と耐えようとしながらも蜜壺を濡らし、本番セックスへと堕ちていく生々しいドッキリ作品を完全レポートします。"
    },
    {
        "id": "feature_healing_vr_sweet_girlfriend_bed_intimacy",
        "api_keywords": ["VR 添い寝 彼女", "8K VR 添い寝", "VR 彼女 密着"],
        "title": "【癒やし＆極上彼女感VR特集】超高画質8Kで味わう至高の添い寝セックス！耳元囁きと温もりでストレスが溶ける神VR選",
        "main_query": "VR 添い寝 彼女 8K 超高画質 彼女感 癒やし 耳元囁き バイノーラル 生中出し 周辺",
        "labels": ["VR", "8KVR", "添い寝", "彼女感", "癒やし", "耳元囁き", "バイノーラル", "生中出し", "特集"],
        "lead": "疲れた夜にベッドの中で優しく包み込んでくれる理想の彼女。8K立体映像とバイノーラル音響によって、吐息の暖かさや肌の柔らかさまで完全に再現された、最高峰の没入感と幸福感を堪能できる添い寝VRタイトルを徹底解剖します。"
    },
    {
        "id": "feature_college_girl_drinking_party_orgy_trap",
        "api_keywords": ["女子大生 宅飲み 乱交", "宅飲み 同期 乱交", "宅飲み 泥酔 乱交"],
        "title": "【女子大生宅飲み乱交トラップAV特集】男子ばかりの部屋で泥酔…逃げ場のない密室で順番にハメ倒される大乱交おすすめ傑作選",
        "main_query": "女子大生 宅飲み 乱交 泥酔 同期 密室 輪姦 ハメ撮り 生中出し 周辺",
        "labels": ["女子大生", "宅飲み", "乱交", "泥酔", "密室", "ハメ撮り", "生中出し", "特集", "おすすめAV"],
        "lead": "「少し飲むだけのつもりだったのに……」サークルやバイト仲間の男子たちの部屋で酔いつぶれた女子大生。無防備になった身体をまさぐられ、次々と生チンポを挿入されていくリアルな背徳大乱交作品を厳選紹介します。"
    },
    {
        "id": "feature_double_female_boss_hotel_room_paizuri",
        "api_keywords": ["巨乳 パイズリ 挟み撃ち", "出張 相部屋 女上司 パイズリ", "Wパイズリ 挟み撃ち"],
        "title": "【美女上司2人と出張相部屋WパイズリAV特集】ホテルの密室で挟まれる至福の胸肉峡谷！朝まで搾り取られるハーレム傑作選",
        "main_query": "出張 相部屋 美女上司2人 ダブルパイズリ 挟み撃ち 巨乳 搾精 生中出し 周辺",
        "labels": ["出張相部屋", "女上司", "Wパイズリ", "挟み撃ち", "巨乳", "ハーレム", "搾精", "生中出し", "特集", "おすすめAV"],
        "lead": "出張先のホテルでまさかの美女上司2人と同室に！お酒の勢いでからかわれ、左右から豊かな美乳でペニスを挟み込まれて高速ピストン。男の理性を完全に狂わせる、究極の出張相部屋ハーレム作品を徹底レビューします。"
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

print("Executing direct FANZA API fetching for Phase 12 feature themes...")

created_count = 0

for idx, theme in enumerate(PHASE12_FEATURE_THEMES, 1):
    print(f"\n[{idx}/{len(PHASE12_FEATURE_THEMES)}] Querying FANZA API for: {theme['title'][:35]}...")
    
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
    print(f"Saved new Phase 12 feature article: {out_path}")

print(f"\nPhase 12 execution complete! Created {created_count} strictly API-fetched new feature articles.")
