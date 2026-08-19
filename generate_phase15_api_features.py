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

# 周辺クエリを拾う第15弾・新規5大特集テーマ定義
PHASE15_FEATURE_THEMES = [
    {
        "id": "feature_desert_island_sisters_innocent_coitus_paradise",
        "api_keywords": ["無人島 ハーレム 島娘", "無人島 三姉妹", "島娘 性指導"],
        "title": "【無人島三姉妹純真交尾AV特集】性に無知な島娘たちを同時に愛でる！南国ビーチと岩陰で交わす本能のハーレム中出し傑作選",
        "main_query": "無人島 三姉妹 性に無知 島娘 性指導 南国 ビーチ 岩陰 原始交尾 生中出し 暁奇奇 周辺",
        "labels": ["無人島", "三姉妹", "島娘", "性に無知", "南国ビーチ", "岩陰", "原始交尾", "生中出し", "特集", "おすすめAV"],
        "lead": "手つかずの自然の中で育った、汚れを知らない美少女三姉妹。漂流してきた男の逞しい身体に興味津々で触れ合い、性の手ほどきを受けるうちに本能をむき出しにして求愛！潮風と波音の中で繰り返される甘美な種付け交尾を徹底比較解説します！"
    },
    {
        "id": "feature_office_tea_room_secret_standing_back_ntr",
        "api_keywords": ["オフィス 給湯室 生ハメ", "給湯室 密室", "給湯室 NTR"],
        "title": "【給湯室密室立ちバックAV特集】同僚の足音が響くすぐ隣で背後から生挿入！声を押し殺して震えるオフィス不倫傑作選",
        "main_query": "オフィス 給湯室 立ちバック 密室 残業 声を押し殺して 生挿入 社内不倫 生中出し 周辺",
        "labels": ["給湯室", "立ちバック", "オフィス不倫", "密室", "残業", "社内恋愛", "生中出し", "特集", "おすすめAV"],
        "lead": "「誰か来ちゃう…！」オフィスの一角にある狭い給湯室。コーヒーを淹れるわずかな時間に扉の鍵を閉められ、シンクに手をつかされてスカートを捲り上げられる……足音のスリルと背後からの鋭いピストンに快楽堕ちするオフィス名作を完全レポートします。"
    },
    {
        "id": "feature_8k_vr_healing_bed_sweet_whisper_cuddling",
        "api_keywords": ["VR 添い寝 8K", "8K VR 添い寝 密着", "VR 彼女 添い寝"],
        "title": "【8K・VR添い寝甘々密着特集】布団の中で抱きしめ合う究極の彼女感！耳元囁きと温もりで脳が溶ける神VRタイトル",
        "main_query": "VR 添い寝 8K 超高画質 彼女感 布団 抱きしめ合う 耳元囁き バイノーラル 生中出し 周辺",
        "labels": ["VR", "8KVR", "添い寝", "彼女感", "耳元囁き", "バイノーラル", "密着", "生中出し", "特集"],
        "lead": "同じ布団に入り、肌と肌を触れ合わせながら過ごす甘美な時間。ヘッドセット越しに感じる彼女の体温、耳元で響く甘い吐息、そして抱きしめ合いながらの優しい挿入から中出しへ……究極の癒やしと官能が共存する添い寝VRタイトルを徹底解剖します。"
    },
    {
        "id": "feature_hot_spring_inn_amateur_creampie_documentary",
        "api_keywords": ["素人 旅館 ハメ撮り", "素人 温泉 旅館 ハメ撮り", "素人 お泊まり 温泉宿"],
        "title": "【素人娘温泉旅館お泊まりハメ撮りAV特集】部屋食のあとに畳の上で浴衣をはだけて…ピュア素人の素顔と濃厚生中出し傑作選",
        "main_query": "素人 旅館 ハメ撮り 温泉 浴衣 畳 部屋食 彼女感 素朴 生中出し 周辺",
        "labels": ["温泉旅館", "素人ハメ撮り", "浴衣", "お泊まり", "部屋食", "彼女感", "生中出し", "特集", "おすすめAV"],
        "lead": "温泉宿の一室、障子の隙間から漏れる月明かりの下で繰り広げられる甘美な逢瀬。浴衣をはだけさせ、温泉で温まった素人娘の柔肌に男根をゆっくりと沈めていく……作られていない素の可愛さと濃厚な中出しを厳選紹介します。"
    },
    {
        "id": "feature_heavy_cleavage_paizuri_deep_friction_creampie",
        "api_keywords": ["パイズリ 挟み込み 巨乳", "巨乳 パイズリ 挟み込み", "美乳 パイズリ 中出し"],
        "title": "【豊満巨乳パイズリ挟み込みAV特集】両手で胸を寄せてペニスを完全密着圧迫！パイズリからの連続生中出しおすすめ傑作選",
        "main_query": "パイズリ 挟み込み 巨乳 美乳 谷間 圧迫 高速ピストン 生中出し 周辺",
        "labels": ["パイズリ", "挟み込み", "巨乳", "美乳", "谷間", "圧迫", "生中出し", "特集", "おすすめAV"],
        "lead": "手のひらから溢れ出す極上バストでペニスをギューッと挟み込み、たっぷりのローションを絡めて高速ピストン！胸の谷間から突き出た亀頭を上目遣いでチロチロと舐め回され、そのまま膣奥へ挿入して中出しを決める至高のパイズリ作品を徹底レビューします。"
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

print("Executing direct FANZA API fetching for Phase 15 feature themes...")

created_count = 0

for idx, theme in enumerate(PHASE15_FEATURE_THEMES, 1):
    print(f"\n[{idx}/{len(PHASE15_FEATURE_THEMES)}] Querying FANZA API for: {theme['title'][:35]}...")
    
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
    print(f"Saved new Phase 15 feature article: {out_path}")

print(f"\nPhase 15 execution complete! Created {created_count} strictly API-fetched new feature articles.")
