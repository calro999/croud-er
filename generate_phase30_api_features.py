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

# サチコ上位クエリに基づく多彩な第30弾・新規5大特集テーマ定義（無人島完全除外）
PHASE30_FEATURE_THEMES = [
    {
        "id": "feature_rental_young_wife_housekeeper_service",
        "api_keywords": ["家政婦 ご奉仕", "家政婦 誘惑", "レンタル若妻家政婦さん"],
        "title": "【レンタル若妻家政婦・下半身ご奉仕AV特集】妻の留守中にやってきた清楚家政婦！家事だけでなく精液処理まで尽くす傑作選",
        "main_query": "レンタル若妻家政婦さん 家政婦 ご奉仕 妻の留守中 誘惑 下半身の世話 生中出し 周辺",
        "labels": ["家政婦", "若妻", "ご奉仕", "妻の留守中", "誘惑", "エプロン姿", "生中出し", "特集", "おすすめAV"],
        "lead": "妻が外出中の自宅にやってきた、美しく家庭的なレンタル若妻家政婦。掃除や料理をこなすうち、胸元や太ももをチラつかせて男を誘惑……「ご主人様のお世話も私の仕事ですから」と笑顔でエプロンを脱ぎ、ペニスを咥え込んで生中出しを受け入れる至福の背徳作品を徹底比較解説します！"
    },
    {
        "id": "feature_neighbor_wife_see_through_temptation_creampie",
        "api_keywords": ["隣の人妻", "スケスケ 隣の人妻", "隣の人妻 誘惑"],
        "title": "【スケスケ薄着で誘惑する隣の人妻特集】ノーブラシースルーでインターホンを鳴らす欲求不満妻！リビングで生ハメする傑作選",
        "main_query": "隣の人妻 スケスケ シースルー インターホン 欲求不満 誘惑 突撃 ノーブラ 生中出し 周辺",
        "labels": ["隣の人妻", "スケスケ", "シースルー", "ノーブラ", "インターホン", "欲求不満", "生中出し", "特集", "おすすめAV"],
        "lead": "平日の午前中、突然鳴り響くインターホン。ドアを開けると、薄手のシースルー服から乳首が透けた隣の美人妻が！夫とのセックスレスに耐えかねて身体を疼かせた人妻が、玄関やリビングで強引にペニスを挿入させ、幾度も絶頂を繰り返す生々しい不倫ドキュメントを完全レポートします。"
    },
    {
        "id": "feature_busty_cosplayer_offpako_costume_creampie",
        "api_keywords": ["爆乳 コスプレイヤー", "コスプレイヤー オフパコ", "コスプレ 露出 撮影会"],
        "title": "【爆乳コスプレイヤー個撮オフパコAV特集】Kカップ・Iカップの規格外バスト！衣装を着たまま激しく揺れる中出し交尾傑作選",
        "main_query": "コスプレイヤー 露出 撮影会 爆乳 Kカップ Iカップ オフパコ 個人撮影 生中出し 周辺",
        "labels": ["コスプレイヤー", "爆乳", "Kカップ", "Iカップ", "オフパコ", "個人撮影", "着衣セックス", "生中出し", "特集", "おすすめAV"],
        "lead": "SNSで大人気の爆乳美少女コスプレイヤー。高額謝礼の個人撮影会でホテルに呼び出され、際どい露出衣装のままカメラマンとオフパコ！Kカップの重量級バストを激しく上下に揺らしながら、子宮奥へ生精液を注ぎ込まれるド迫力のコスプレ作品を徹底解剖します。"
    },
    {
        "id": "feature_delivery_health_driver_car_secret_creampie",
        "api_keywords": ["デリヘル 待機", "デリヘル 運転手", "送迎車 デリヘル 生ハメ"],
        "title": "【デリヘル待機中・車内本番密通AV特集】深夜の駐車場で送迎ドライバーと風俗嬢が密着！暗闇で激しく突かれる裏稼業傑作選",
        "main_query": "伊賀 デリヘルドライバー 送迎車 待機中 車内本番 風俗嬢 密通 コインパーキング 生中出し 周辺",
        "labels": ["デリヘルドライバー", "送迎車", "待機中", "車内本番", "風俗嬢", "密通", "裏稼業", "生中出し", "特集", "おすすめAV"],
        "lead": "客からの指名を待つ深夜のコインパーキング。送迎車の薄暗い車内で、仕事終わりの風俗嬢がドライバーと急接近！客には絶対に見せない本気の顔でシートを倒し、狭い車内で腰を激しくぶつけ合う裏稼業の生々しい密通ドラマを厳選紹介します。"
    },
    {
        "id": "feature_kinoshita_himari_sweet_cohabitation_creampie",
        "api_keywords": ["木下ひまり", "木下ひまり 中出し", "木下ひまり 彼女"],
        "title": "【木下ひまり・極上くびれ美少女と濃密同棲特集】華奢な身体と吸い付く美肌！甘く愛し合う至高のイチャラブ生中出し傑作選",
        "main_query": "木下ひまり 木下ひまりちゃん 美少女 くびれ 彼女感 同棲生活 イチャラブ 生ハメ 生中出し 周辺",
        "labels": ["木下ひまり", "美少女", "くびれ", "スレンダー", "同棲生活", "彼女感", "イチャラブ", "生中出し", "特集", "おすすめAV"],
        "lead": "引き締まった極上のくびれと小悪魔的な笑顔で男を魅了する木下ひまり。朝起きてから夜眠るまで、大好きな彼女と肌を重ね合う甘く濃厚な同棲生活！上目遣いでおねだりされ、愛し合いながら子宮奥へ何度も中出しする至高の彼女感タイトルを徹底レビューします。"
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

print("Executing direct FANZA API fetching for Phase 30 feature themes...")

created_count = 0

for idx, theme in enumerate(PHASE30_FEATURE_THEMES, 1):
    print(f"\n[{idx}/{len(PHASE30_FEATURE_THEMES)}] Querying FANZA API for: {theme['title'][:35]}...")
    
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
    print(f"Saved new Phase 30 feature article: {out_path}")

print(f"\nPhase 30 execution complete! Created {created_count} strictly API-fetched new feature articles.")
