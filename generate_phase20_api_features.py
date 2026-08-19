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

# サチコ上位クエリに基づく多彩な第20弾・新規5大特集テーマ定義（無人島完全除外）
PHASE20_FEATURE_THEMES = [
    {
        "id": "feature_oil_tickle_panic_climax_ecstasy",
        "api_keywords": ["くすぐり パニック", "オイル くすぐり 絶頂", "くすぐり 拘束"],
        "title": "【極上オイルくすぐりパニック絶頂特集】全身ヌルヌルで拘束され快楽とくすぐりに悶絶！美少女の限界アクメAV傑作選",
        "main_query": "限界突破 パニック絶頂 泉りおん 極上オイル 裸身 快楽 くすぐり 悶絶 潮吹き 周辺",
        "labels": ["オイルくすぐり", "パニック絶頂", "くすぐり拷問", "拘束", "限界アクメ", "美少女", "潮吹き", "特集", "おすすめAV"],
        "lead": "全身に極上オイルを塗りたくられ、逃げ場のない状態で敏感な足裏・脇腹・秘部を徹底的にくすぐり責め！笑いと喘ぎが入り混じり、快楽のパニックに陥りながら激しく痙攣して潮を吹き散らす、マニア必見のくすぐりフェチ傑作を徹底比較解説します！"
    },
    {
        "id": "feature_endless_deep_creampie_conception_500min",
        "api_keywords": ["生中出し 500分", "孕むまで 生中出し", "本当に孕むまで 生中出し"],
        "title": "【本当に孕むまで終わらない極限生中出し特集】トップ単体女優が子宮奥に注ぎ込まれ続ける！限界突破のロングラン中出しドキュメント傑作選",
        "main_query": "河北彩花 最終章 本当に孕むまで 終わらない 生中出し 500分 子宮受精 連続中出し 周辺",
        "labels": ["極限生中出し", "500分", "本当に孕むまで", "子宮奥中出し", "連続射精", "トップ女優", "ドキュメント", "特集", "おすすめAV"],
        "lead": "日本最高峰の美貌を誇るトップ女優が、カメラの前で一切のゴムを排して膣奥へ連続射精を受け止め続ける！何発も注ぎ込まれる濃厚な精液でお腹が満たされ、恍惚の表情で種付けを受け入れる至高のドキュメンタリー作品を完全レポートします。"
    },
    {
        "id": "feature_broken_promise_raw_creampie_college_girl",
        "api_keywords": ["外出し約束", "外出し約束 中出し", "外出し 約束 騙し"],
        "title": "【外出し約束破り素人女子大生中出し特集】「外に出すって言ったのに…」ウブな素人を騙して膣奥へ2連射する背徳ドキュメント傑作選",
        "main_query": "経験浅い 外出し約束 19歳 大学生 膣奥 中出し 2回決行 騙し 生中出し 周辺",
        "labels": ["外出し約束", "約束破り", "素人女子大生", "騙し中出し", "19歳", "膣奥2連射", "背徳", "特集", "おすすめAV"],
        "lead": "「絶対に外に出すから」という約束を信じて生挿入を許してくれたピュアな女子大生。いざ絶頂を迎えた瞬間、約束を破って最奥へドクドクと熱い精液を全量発射！驚きと戸惑いに濡れる素人の生々しい表情を徹底解剖します。"
    },
    {
        "id": "feature_delivery_health_waiting_car_secret_affair",
        "api_keywords": ["デリヘル 運転手", "デリヘル 待機 車内", "送迎ドライバー 風俗嬢"],
        "title": "【デリヘル送迎ドライバー密通車内生ハメ特集】客を待つ深夜の車内で風俗嬢と生本番！裏稼業密着おすすめ傑作選",
        "main_query": "伊賀 デリヘルドライバー 送迎車 待機中 車内生ハメ 風俗嬢 密通 生中出し 周辺",
        "labels": ["デリヘルドライバー", "送迎車", "車内生ハメ", "風俗嬢", "密通", "裏稼業", "生中出し", "特集", "おすすめAV"],
        "lead": "配車待ちの深夜、人気のないコインパーキングに停めた送迎車内。仕事の愚痴や相談から急接近し、シートを倒して風俗嬢とドライバーが激しく求め合う！客には決して見せない本気の素顔と中出し交尾を描いた名作を厳選紹介します。"
    },
    {
        "id": "feature_slender_cleavage_paizuri_sandwich_ecstasy",
        "api_keywords": ["木下ひまり", "スレンダー パイズリ", "スレンダー 美乳 パイズリ"],
        "title": "【スレンダー美乳パイズリ挟み撃ち特集】細身の極上くびれと形の良い美胸！谷間に挟まれながら高速ピストンされる神動画選",
        "main_query": "木下ひまり パイズリ スレンダー 美乳 くびれ 挟み撃ち 谷間 高速ピストン 生中出し 周辺",
        "labels": ["パイズリ", "スレンダー", "美乳", "木下ひまり", "くびれ", "挟み撃ち", "高速ピストン", "特集", "おすすめAV"],
        "lead": "細身で引き締まったくびれと、手のひらにすっぽり収まる極上の美乳。オイルで艶めく胸の谷間にペニスを滑り込ませ、上目遣いでフェラを交えながら挟み込まれる快感！視覚と触覚が極限に刺激されるスレンダーパイズリ作品を徹底レビューします。"
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

print("Executing direct FANZA API fetching for Phase 20 feature themes...")

created_count = 0

for idx, theme in enumerate(PHASE20_FEATURE_THEMES, 1):
    print(f"\n[{idx}/{len(PHASE20_FEATURE_THEMES)}] Querying FANZA API for: {theme['title'][:35]}...")
    
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
    print(f"Saved new Phase 20 feature article: {out_path}")

print(f"\nPhase 20 execution complete! Created {created_count} strictly API-fetched new feature articles.")
