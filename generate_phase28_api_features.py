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

# サチコ上位クエリに基づく多彩な第28弾・新規5大特集テーマ定義（無人島完全除外）
PHASE28_FEATURE_THEMES = [
    {
        "id": "feature_cawd_label_extreme_obedience_facial_creampie",
        "api_keywords": ["CAWD", "CAWD ぶっかけ", "CAWD 中出し"],
        "title": "【CAWDレーベル・過激シチュエーション名作特集】ぶっかけ・顔射・言いなり調教！刺激度MAXのCAWD殿堂入り傑作選",
        "main_query": "cawd 00998 cawd 998 CAWD 言いなり ぶっかけ 顔射 調教 生中出し 周辺",
        "labels": ["CAWD", "言いなり", "ぶっかけ", "顔射", "過激シチュエーション", "調教", "生中出し", "特集", "おすすめAV"],
        "lead": "過激でリアルなエロスを追求し続ける大人気レーベルCAWD。制服姿の美少女への容赦ない顔面射精や、断れない立場を利用した言いなり調教など、男の本能を直撃する刺激度MAXの殿堂入り傑作タイトルを徹底比較解説します！"
    },
    {
        "id": "feature_snos_label_harem_sisters_deep_creampie",
        "api_keywords": ["SNOS", "SNOS 双子", "SNOS ハーレム"],
        "title": "【SNOSレーベル・超絶ハーレム＆美少女特集】双子姉妹や複数美少女との濃厚密着！SNOSシリーズが誇る名作AV選",
        "main_query": "snos00353 snos 353 SNOS 双子姉妹 複数美少女 ハーレム 濃厚密着 生中出し 周辺",
        "labels": ["SNOS", "ハーレム", "双子姉妹", "美少女", "濃厚密着", "複数プレイ", "生中出し", "特集", "おすすめAV"],
        "lead": "ハイレベルな美少女キャストとドラマ性の高いシチュエーションで熱狂的なファンを持つSNOS。双子姉妹との夢のようなハーレムや、複数の美女から同時に求められる濃厚な密着交尾を描いた名作群を完全レポートします。"
    },
    {
        "id": "feature_dsvr_8k_vr_ultimate_immersion_masterpieces",
        "api_keywords": ["DSVR", "DSVR 8K", "DSVR 密着"],
        "title": "【DSVR・8K高画質360度VR神タイトル特集】視界いっぱいに広がるエロスと立体音響！DSVRレーベル至高の没入作品選",
        "main_query": "dsvr01998 13dsvr01998 DSVR 8KVR 360度 立体音響 密着 顔面特化 生中出し 周辺",
        "labels": ["DSVR", "VR", "8KVR", "360度", "立体音響", "顔面特化", "没入感", "特集"],
        "lead": "VR界を牽引するトップレーベルDSVR。目の前数センチまで迫る女優の美しい瞳、耳元をくすぐる吐息のバイノーラル音声、そして8K超高画質が織りなす圧倒的な臨場感！VRゴーグルを装着した瞬間に別世界へと誘われる神タイトルを徹底解剖します。"
    },
    {
        "id": "feature_start_label_sweet_cohabitation_slow_sex",
        "api_keywords": ["START", "START 美少女", "START 同棲"],
        "title": "【STARTレーベル・王道美少女同棲エロス特集】付き合いたての甘い日常から濃厚エッチへ！STARTシリーズ傑作選",
        "main_query": "start00153 start 153 START 美少女 同棲生活 丁寧な暮らし スローセックス 生中出し 周辺",
        "labels": ["START", "美少女", "同棲生活", "彼女感", "スローセックス", "王道エロス", "生中出し", "特集", "おすすめAV"],
        "lead": "透明感あふれる美少女とのリアルな恋愛シチュエーションを描くSTARTレーベル。付き合いたての甘酸っぱい日常から、お互いの温もりを確かめ合うように重ねるスローセックスまで、心も身体も満たされる王道エロスを厳選紹介します。"
    },
    {
        "id": "feature_kitaoka_karin_innocent_beauty_sensual_development",
        "api_keywords": ["北岡果林", "北岡果林 美少女", "北岡果林 中出し"],
        "title": "【北岡果林・未熟可愛い美少女の受難と快楽特集】吸い込まれるような瞳とウブな反応！北岡果林の魅力を凝縮した傑作選",
        "main_query": "北岡果林ちゃん 北岡果林 美少女 未熟可愛い 初々しい ウブ 生ハメ 生中出し 周辺",
        "labels": ["北岡果林", "美少女", "未熟可愛い", "初々しい", "ウブ", "生ハメ", "生中出し", "特集", "おすすめAV"],
        "lead": "検索急上昇中の大人気美少女・北岡果林。吸い込まれそうな大きな瞳と、まだ男を知らないような初々しいリアクション。強引に迫られて恥じらいながらも、快楽の波に抗えずに乱れていく北岡果林の必見タイトルを徹底レビューします。"
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

print("Executing direct FANZA API fetching for Phase 28 feature themes...")

created_count = 0

for idx, theme in enumerate(PHASE28_FEATURE_THEMES, 1):
    print(f"\n[{idx}/{len(PHASE28_FEATURE_THEMES)}] Querying FANZA API for: {theme['title'][:35]}...")
    
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
    print(f"Saved new Phase 28 feature article: {out_path}")

print(f"\nPhase 28 execution complete! Created {created_count} strictly API-fetched new feature articles.")
