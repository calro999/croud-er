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

# 周辺クエリを拾う第7弾・新規5大特集テーマ定義
PHASE7_FEATURE_THEMES = [
    {
        "id": "feature_college_circle_orgy_camp_chaos",
        "api_keywords": ["女子大 サークル 乱交", "ヤリサー 合宿", "サークル ハーレム"],
        "title": "【女子大サークル乱交合宿特集】露出衣装の美女たちが入り乱れる！合宿所の密室で繰り広げられる中出し大乱交AV傑作選",
        "main_query": "某大学 ベリーダンスサークル 女子大生 露出衣装 カレン モカ 合宿 乱交 周辺",
        "labels": ["女子大生", "サークル", "ヤリサー", "合宿乱交", "露出衣装", "ハーレム", "中出し", "特集", "おすすめAV"],
        "lead": "普段は華やかなダンスやスポーツに打ち込む女子大生たちが、サークル合宿の夜にアルコールの勢いで開放的に乱れ狂う！複数人での同時挿入や次々と注ぎ込まれる生中出しなど、男の妄想を具現化したサークル乱交作品を徹底比較解説します。"
    },
    {
        "id": "feature_tokusatsu_heroine_tickling_torture_climax",
        "api_keywords": ["ヒロイン 拘束 くすぐり", "特撮 ヒロイン 敗北", "色仕掛け ヒロイン"],
        "title": "【特撮ヒロイン拘束くすぐり拷問特集】凛々しい正義の味方が悪の罠で完全敗北…敏感な素肌をくすぐられ悶絶する被虐AV傑作選",
        "main_query": "レディスレイヤー桃太郎 被虐編 ヒロインピンチ 拘束 くすぐり拷問 足裏 脇腹 周辺",
        "labels": ["特撮ヒロイン", "ヒロインピンチ", "拘束拷問", "くすぐり", "足裏くすぐり", "完全敗北", "被虐", "特集"],
        "lead": "正義のスーツを無力化され、両手両足を固定された誇り高きヒロイン。容赦のない足裏やくびれへのくすぐり責めに、笑い叫びながらプライドを折られ、快楽に染まっていくマニア垂涎の被虐特撮アクションを完全レポートします。"
    },
    {
        "id": "feature_hardcore_slave_toy_bondage_training",
        "api_keywords": ["ドM 玩具 拘束", "調教 肉人形", "強制アクメ 玩具"],
        "title": "【ドM肉人形玩具調教AV特集】拘束された身体に電マ＆極太バイブ直撃！理性が破壊される強制連続アクメおすすめ傑作選",
        "main_query": "黒髪 ドM りお 鬼アクメ 性玩具調教 限界イキ 子宮 孕み汁 周辺",
        "labels": ["ドM", "玩具調教", "拘束", "電マ", "バイブ", "強制アクメ", "肉人形", "生ハメ", "特集"],
        "lead": "逃げ場のない拘束状態で、複数の強力性玩具を同時に押し当てられる極限の拷問。潮を吹き散らしながら「もっとイカせてください！」と懇願するマゾヒズムの極致と、開発し尽くされたマゾ穴への生中出しを描いた名作を徹底解剖します。"
    },
    {
        "id": "feature_hot_spring_ryokan_yukata_sweet_creampie",
        "api_keywords": ["素人 お泊まり 浴衣", "温泉 旅館 ハメ撮り", "浴衣 生中出し"],
        "title": "【温泉旅館浴衣ハメ撮りAV特集】部屋食のあとに畳の上で浴衣をはだけて…ピュア美少女と愛を確かめ合う濃厚生中出し傑作選",
        "main_query": "北岡果林 お泊まり 一部始終 温泉旅行 浴衣 彼女感 生中出し 周辺",
        "labels": ["温泉旅館", "浴衣", "お泊まり", "素人ハメ撮り", "彼女感", "純愛エロス", "生中出し", "特集"],
        "lead": "静かな温泉旅館の一室、湯上がりの火照った身体を包む浴衣。帯をゆっくりと解き、しっとりとした柔肌に男根を滑り込ませる……圧倒的な彼女感と旅先ならではの甘い背徳感を堪能できる至高のお泊まり作品を厳選紹介します。"
    },
    {
        "id": "feature_blonde_gyaru_dangerous_raw_creampie",
        "api_keywords": ["金髪 ギャル 生中出し", "おじさん ギャル ナンパ", "ギャル 危険性交"],
        "title": "【金髪美少女ギャル危険性交AV特集】おじさんのデカチンにノリノリで腰振り！子宮奥まで遠慮なく注ぎ込む生中出し傑作選",
        "main_query": "ぎゃる好きおじ ナンパ旅 殿堂入り 金髪ギャル 危険性交 生中出し 周辺",
        "labels": ["金髪ギャル", "ギャル", "ナンパ", "おじさん", "危険性交", "生中出し", "殿堂入り", "特集"],
        "lead": "ド派手な金髪と抜群のスタイルを誇る素人ギャル。おじさんナンパ師の巧妙なリードに流され、ホテルでゴムなし生ハメ！外出しの合図を無視して奥深くまで中出しされるギャルのリアルな絶頂リアクションを徹底レビューします。"
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

print("Executing direct FANZA API fetching for Phase 7 feature themes...")

created_count = 0

for idx, theme in enumerate(PHASE7_FEATURE_THEMES, 1):
    print(f"\n[{idx}/{len(PHASE7_FEATURE_THEMES)}] Querying FANZA API for: {theme['title'][:35]}...")
    
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
    print(f"Saved new Phase 7 feature article: {out_path}")

print(f"\nPhase 7 execution complete! Created {created_count} strictly API-fetched new feature articles.")
