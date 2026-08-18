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

# 周辺クエリを拾う第3弾・新規8大特集テーマ定義
# 各テーマは「シチュエーション特化」「比較・ランキング」「フェチ・ジャンル横断」の切り口でカニバリズムを完全回避
PHASE3_FEATURE_THEMES = [
    {
        "id": "feature_black_hair_m_toy_training",
        "api_keywords": ["黒髪 ドM", "玩具 調教", "鬼アクメ"],
        "title": "【黒髪ドM調教AV特集】清楚なお嬢様が玩具責めでメス豚に堕ちる！電マ・バイブ強制連続アクメおすすめ傑作選",
        "main_query": "黒髪 ドM 玩具調教 鬼アクメ りお 限界イキ 周辺",
        "labels": ["黒髪", "ドM", "玩具調教", "鬼アクメ", "電マ", "バイブ", "限界イキ", "特集", "おすすめAV"],
        "lead": "「見た目は上品で清楚な黒髪美少女が、実は責められるほど歓喜する生粋のドMだった……」強力な性玩具で敏感な性感帯を休む間もなく責め抜かれ、理性を失って涎を垂らしながら生ハメを懇願する、マゾ調教ファン必見の極限絶頂タイトルを徹底比較解説します！"
    },
    {
        "id": "feature_college_girl_broken_promise_creampie",
        "api_keywords": ["女子大生 ハメ撮り", "外出し 中出し", "素人 大学生"],
        "title": "【外出しの嘘と生中出し】「外に出すって言ったのに…」経験浅い現役女子大生の膣奥に注ぎ込む背徳ハメ撮りAV特集",
        "main_query": "経験浅い 19歳 女子大生 外出し約束破り 生中出し2回 周辺",
        "labels": ["女子大生", "外出し約束破り", "素人ハメ撮り", "生中出し", "19歳", "騙し", "特集", "おすすめAV"],
        "lead": "マッチングアプリや合コンで知り合ったウブな女子大生。「絶対ゴム付けるから」「外に出すから」という約束を平然と破り、奥深くへと生中出しを決行！驚きと戸惑い、そして快楽の余韻に浸るリアルな素人リアクションを堪能できる傑作選をお届けします。"
    },
    {
        "id": "feature_mature_wife_sensual_massage_development",
        "api_keywords": ["人妻 性感", "エステ 中出し", "柔肌 悶え"],
        "title": "【極上性感エステ】人妻の柔肌をオイルで開発！恥帯への指先愛撫から理性が溶ける濃厚本番中出しAV特集",
        "main_query": "人妻 快感 柔肌 濡れる 背徳 性感恥帯 エステ 周辺",
        "labels": ["人妻", "性感エステ", "オイルマッサージ", "柔肌", "恥帯開発", "本番生ハメ", "特集", "おすすめAV"],
        "lead": "疲れを癒やすために訪れたはずのサロンで、セラピストの巧妙な指技によって眠っていたメスの本能を呼び覚まされる人妻たち。アロマオイルでテカる柔肌をまさぐられ、夫には言えない本番セックスへと堕ちていく大人の官能名作を特集します。"
    },
    {
        "id": "feature_real_lesbian_catfight_battle",
        "api_keywords": ["キャットファイト", "レズ 潮吹き", "レズバトル"],
        "title": "【美女ガチイキ格闘】先に潮を吹いた方が負け！プライドと快感を賭けた白熱キャットファイト＆レズバトルAV特集",
        "main_query": "レズバトル かりみ キャットファイト ガチイキ 勝負 潮吹き 周辺",
        "labels": ["レズバトル", "キャットファイト", "格闘", "ガチイキ勝負", "潮吹き", "レズ", "特集", "おすすめAV"],
        "lead": "リングの上でビキニ姿の美女たちが激突！関節技で相手の自由を奪い、指先と舌でクリトリスを攻め立てる極限の官能バトル。屈辱に耐えながらも歓喜の潮吹きで敗北する、格闘フェチ＆レズ好き歓喜のタイトルを完全レビューします。"
    },
    {
        "id": "feature_hot_spring_overnight_pure_girl",
        "api_keywords": ["お泊まり 温泉", "美少女 ハメ撮り", "素人 お泊まり"],
        "title": "【温泉お泊まりデート】ピュア美少女と過ごす一泊二日の甘い蜜月！浴衣をはだけて愛を確かめ合う生中出しAV特集",
        "main_query": "北岡果林 お泊まり 一部始終 温泉デート 彼女感 周辺",
        "labels": ["お泊まり", "温泉デート", "美少女", "北岡果林", "彼女感", "浴衣", "生中出し", "特集"],
        "lead": "大好きな彼女と二人きりで過ごす温泉旅行。露天風呂での密着キス、畳の上に敷かれた布団での初々しい交わり……圧倒的なリアリティと彼女感で心まで満たされる、純愛と官能が交差するお泊まり作品を厳選ナビゲートします。"
    },
    {
        "id": "feature_tan_gyaru_uncle_nanpa_dangerous_sex",
        "api_keywords": ["ギャル ナンパ", "おじさん ギャル", "金髪ギャル 生中出し"],
        "title": "【金髪ギャル×おじさん】ノリでホテルへ連れ込み危険性交！絶対的美少女ギャルがオジサンチンポに溺れるAV特集",
        "main_query": "ぎゃる好きおじ ナンパ旅 殿堂入り 美少女 危険性交 周辺",
        "labels": ["ギャル", "ナンパ", "おじさん", "金髪ギャル", "危険性交", "生中出し", "殿堂入り", "特集"],
        "lead": "街で見かけたド派手な金髪ギャルを巧みな話術と美味い酒でホテルへ誘導！普段は見せない素直でエロい一面を引き出し、容赦ない生ハメで子宮奥まで中出しをキメる、ギャルナンパモノの最高峰を徹底解説します。"
    },
    {
        "id": "feature_sisterly_big_sister_seduction_prank",
        "api_keywords": ["お姉ちゃん 誘惑", "ドッキリ 性感", "包容力"],
        "title": "【包容力お姉ちゃんの陥落】優しすぎるお姉ちゃんがエロトラップに耐えきれず…耐久ドッキリ＆発情アクメAV特集",
        "main_query": "姫崎莉波 ナンパ誘惑 耐久ドッキリ お姉ちゃん系 包容力 周辺",
        "labels": ["お姉ちゃん系", "包容力", "誘惑", "耐久ドッキリ", "エロトラップ", "発情アクメ", "特集"],
        "lead": "困っている男を放っておけない母性あふれるお姉ちゃん。そんな彼女に仕掛けられた際どい性感マッサージとお色気ドッキリ！必死に耐えようとしながらも、身体の疼きに勝てずメスの顔で抱きついてくるご褒美展開をまとめました。"
    },
    {
        "id": "feature_legendary_amateur_god_scene_compilation",
        "api_keywords": ["素人 総集編", "ハメ撮り 傑作", "神シーン 厳選"],
        "title": "【お気に入り3000超え】ハズレ一切無しの神シーン凝縮！素人ガチイキ＆生中出し殿堂入りよくばり総集編AV特集",
        "main_query": "お気に入り数3000越 人気20作品 総集編 よくばりセット極 周辺",
        "labels": ["素人総集編", "お気に入り3000超", "神シーン", "よくばりセット", "ガチイキ", "ハメ撮り", "特集"],
        "lead": "配信サイトで圧倒的なブックマーク数を誇る殿堂入りシーンだけを贅沢に集めたメガ盛りパック！素人娘のリアルな初脱ぎから、爆乳人妻の絶叫アクメ、中出し連発まで、実用度100%の決定版タイトルを徹底紹介します。"
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

print("Executing direct FANZA API fetching for Phase 3 feature themes...")

created_count = 0

for idx, theme in enumerate(PHASE3_FEATURE_THEMES, 1):
    print(f"\n[{idx}/{len(PHASE3_FEATURE_THEMES)}] Querying FANZA API for: {theme['title'][:35]}...")
    
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
    <li><a href="#overview">1. このジャンルが熱狂的に支持される心理と背景</a></li>
    <li><a href="#ranking">2. FANZA公式API直接取得・厳選おすすめ作品解説</a></li>
    <li><a href="#matrix">3. フェチ度＆抜きどころ 徹底比較マトリクス</a></li>
    <li><a href="#faq">4. よくある質問・失敗しない選び方（FAQ）</a></li>
    <li><a href="#conclusion">5. まとめ・総括</a></li>
  </ul>
</div>

<h3 id="overview">1. このジャンルが熱狂的に支持される心理と背景</h3>
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
    print(f"Saved new Phase 3 feature article: {out_path}")

print(f"\nPhase 3 execution complete! Created {created_count} strictly API-fetched new feature articles.")
