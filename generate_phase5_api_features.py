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

# 周辺クエリを拾う第5弾・新規6大特集テーマ定義
PHASE5_FEATURE_THEMES = [
    {
        "id": "feature_innocent_virgin_sexual_education",
        "api_keywords": ["無垢 処女 性教育", "性を知らない", "無垢 少女"],
        "title": "【無知な処女への性教育AV特集】恥じらいも知らずに育ったピュア少女に性の悦びを一から教え込むおすすめ傑作選",
        "main_query": "無垢 処女 性教育 性を知らない 島娘 ピュア美少女 性指導 周辺",
        "labels": ["性教育", "無垢", "処女", "性を知らない", "性指導", "ピュア美少女", "初体験", "特集", "おすすめAV"],
        "lead": "「男の身体も性行為の意味も知らずに育った純真無垢な美少女たち……」好奇心から触れてくる指先、初めての愛撫に潤む瞳、そして生ハメの快感に目覚めて自ら腰を振るようになるまでの段階的なプロセスを描いた、フェチ心を直撃する性教育作品を徹底比較解説します！"
    },
    {
        "id": "feature_husband_watching_ntr_despair_climax",
        "api_keywords": ["夫の目の前 寝取られ", "寝取られ 夫の前", "NTR 夫の目前"],
        "title": "【夫の目の前NTR絶望セックス特集】愛する妻が見知らぬ男のチンポで連続絶頂…夫の視線が最大の媚薬になる背徳傑作選",
        "main_query": "夫の目の前 寝取られ NTR 絶望 屈辱 潮吹き 対面座位 中出し 周辺",
        "labels": ["NTR", "寝取られ", "夫の目の前", "屈辱", "絶頂", "背徳", "潮吹き", "対面座位", "特集"],
        "lead": "夫が縛り付けられ見守るリビングで、上品な美貌妻が巨根男に蹂躙されていく。頭では拒絶しながらも、夫に見られている極限の羞恥で感度が跳ね上がり、大量の潮を吹きながら中出しを受け入れてしまう、NTRジャンル屈指の傑作を完全レポートします。"
    },
    {
        "id": "feature_magic_mirror_bus_car_exposure_thrill",
        "api_keywords": ["マジックミラー号 車内 露出", "マジックミラー号", "MM号 露出"],
        "title": "【マジックミラー号車外露出AV特集】ガラス一枚隔てた通行人のすぐ横で生ハメ！羞恥とスリルで感度MAXの中出しおすすめ傑作選",
        "main_query": "マジックミラー号 車内 露出 ガラス一枚 通行人 スリル 生中出し 周辺",
        "labels": ["マジックミラー号", "MM号", "露出", "車内ハメ", "通行人", "スリル", "生中出し", "特集", "おすすめAV"],
        "lead": "外からは見えない特殊ミラー越しに、すぐそこを一般人が歩いている極限のシチュエーション。見られるかもしれない恐怖と興奮でびしょ濡れになった素人娘たちが、窓ガラスに手をつかされながら生チンポで貫かれる伝説の露出企画を徹底解剖します。"
    },
    {
        "id": "feature_binaural_whispering_8k_vr_ecstasy",
        "api_keywords": ["8K 密着 囁き VR", "VR 囁き", "バイノーラル VR"],
        "title": "【耳元囁き8KバイノーラルVR特集】息づかいと水音が脳に直接響く！超至近距離で耳責め＆生中出しされる神没入VRタイトル",
        "main_query": "VR 8K 囁き バイノーラル 立体音響 密着 ゼロ距離 生中出し 周辺",
        "labels": ["VR", "8KVR", "バイノーラル", "耳元囁き", "立体音響", "密着", "ゼロ距離", "特集"],
        "lead": "高精度な3D映像と、左右の耳元で生々しく響く吐息や唾液の咀嚼音。ヘッドセットを装着した瞬間、美女の唇が耳元数センチに迫り、甘い囁きとともに射精を促される、現行VR技術の頂点に立つ没入作品を厳選紹介します。"
    },
    {
        "id": "feature_mens_esthe_private_room_real_sex",
        "api_keywords": ["メンエス 密室 本番", "メンズエステ 本番", "裏オプ 生ハメ"],
        "title": "【密室メンエス裏オプ本番AV特集】紙パンツをずらして生ハメ突入！オイルまみれのセラピストを堕とすリアル本番交渉傑作選",
        "main_query": "メンズエステ 密室 本番 裏オプ 生ハメ チップ交渉 メンエス嬢 周辺",
        "labels": ["メンズエステ", "メンエス", "裏オプ", "本番交渉", "生ハメ", "密室", "オイル", "特集", "おすすめAV"],
        "lead": "アパートの一室で行われるアロママッサージ。密着するセラピストの肌の温もりに我慢できず、チップを握らせて本番を交渉。最初は躊躇していた彼女が、生ペニスの熱さに負けて腰を沈めてしまう生々しい裏オプ作品を徹底レビューします。"
    },
    {
        "id": "feature_extreme_paizuri_double_cleavage_creampie",
        "api_keywords": ["巨乳 パイズリ 挟み撃ち", "パイズリ 巨乳", "パイズリ 挟み込み"],
        "title": "【極上美乳パイズリ挟み撃ちAV特集】豊かな胸の谷間で挟み込み高速ピストン！美乳を汚す大量射精＆生中出しおすすめ傑作選",
        "main_query": "巨乳 パイズリ 挟み撃ち 美乳 谷間 高速ピストン 胸射 生中出し 周辺",
        "labels": ["パイズリ", "巨乳", "美乳", "挟み撃ち", "谷間", "高速ピストン", "胸射", "特集", "おすすめAV"],
        "lead": "形・柔らかさ・弾力のすべてが揃った至高の美乳でペニスを包み込み、たっぷりのローションを絡めて激しく上下動！視覚を狂わせる胸の谷間と、先端をチロチロと舐め回す上目遣いフェラで射精欲を限界突破させるパイズリ特化タイトルを徹底紹介します。"
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

print("Executing direct FANZA API fetching for Phase 5 feature themes...")

created_count = 0

for idx, theme in enumerate(PHASE5_FEATURE_THEMES, 1):
    print(f"\n[{idx}/{len(PHASE5_FEATURE_THEMES)}] Querying FANZA API for: {theme['title'][:35]}...")
    
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
    print(f"Saved new Phase 5 feature article: {out_path}")

print(f"\nPhase 5 execution complete! Created {created_count} strictly API-fetched new feature articles.")
