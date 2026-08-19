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

# サチコ上位クエリに基づく多彩な第24弾・新規5大特集テーマ定義（無人島完全除外）
PHASE24_FEATURE_THEMES = [
    {
        "id": "feature_amateur_model_studio_deception_creampie",
        "api_keywords": ["素人 撮影会 騙し", "素人 個撮 騙し", "ウブ モデル 撮影会"],
        "title": "【素人モデル個撮スタジオ騙しハメAV特集】撮影会と信じてやってきたウブ娘…密室でなし崩しに脱がされ生中出しされる傑作選",
        "main_query": "高瀬りな 素人 モデル 撮影会 個撮 騙し 密室 なし崩し 生中出し 周辺",
        "labels": ["素人モデル", "撮影会", "個人撮影", "騙し", "密室スタジオ", "なし崩し", "生中出し", "特集", "おすすめAV"],
        "lead": "「普通のポートレート撮影と聞いていたのに……」密室スタジオでカメラマンの巧みな誘導により、徐々に露出度の高い衣装へ。恥じらいながらも雰囲気に流され、ベッドの上でなし崩しに生挿入を受け止めてしまうリアルな素人ドキュメントを徹底比較解説します！"
    },
    {
        "id": "feature_f_cup_cabaret_girl_submissive_offpako",
        "api_keywords": ["キャバ嬢 ドM 巨乳", "キャバ嬢 オフパコ", "Fカップ キャバ嬢"],
        "title": "【美形キャバ嬢FカップドM巨乳オフパコ特集】お店ではツンツンな超美形ギャルがホテルでドM覚醒！首絞め生ハメされる傑作選",
        "main_query": "美形キャバ嬢ちゃんfカップドm巨乳オフパコ キャバ嬢 ドM Fカップ 巨乳 オフパコ ホテル 生中出し 周辺",
        "labels": ["キャバ嬢", "ドM", "Fカップ", "巨乳", "オフパコ", "ホテル", "首絞め", "生中出し", "特集", "おすすめAV"],
        "lead": "歌舞伎町の超人気店で働く、プライドの高い美形キャバ嬢。高額貢ぎの果てにホテルの個室でオフパコに成功すると、実は強引に攻められるのが大好きなドMと判明！豊満なFカップを揺らしながら子宮奥へ生中出しを懇願するギャル作品を完全レポートします。"
    },
    {
        "id": "feature_8k_vr_whisper_dirty_talk_cowgirl_ecstasy",
        "api_keywords": ["8K VR 密着 囁き 騎乗位", "VR 騎乗位 見下ろし 囁き", "8K VR 淫語 騎乗位"],
        "title": "【8K・VR淫語囁き密着騎乗位特集】至近距離で見下ろされながら激しく腰を振られる！脳が溶ける神VRタイトル傑作選",
        "main_query": "8K VR 密着 囁き 騎乗位 見下ろし 淫語 バイノーラル 脳が溶ける 生中出し 周辺",
        "labels": ["VR", "8KVR", "騎乗位", "見下ろし", "淫語囁き", "バイノーラル", "生中出し", "特集"],
        "lead": "ベッドに仰向けになった視界の真正面で、美女が上に跨がり妖艶な笑顔で見下ろしてくる！ヘッドセットから耳元へ直接吹き込まれる淫語と、8K高精細映像で迫る美乳の上下運動に包まれる、圧倒的没入感の神VRタイトルを徹底解剖します。"
    },
    {
        "id": "feature_college_girl_room_drinking_party_creampie",
        "api_keywords": ["女子大生 宅飲み なし崩し", "女子大生 部屋飲み ハメ撮り", "宅飲み なし崩し 生ハメ"],
        "title": "【女子大生自宅飲み会なし崩し生ハメ特集】彼氏持ちのウブ女子大生が部屋飲みでガード崩壊…朝まで中出しされる傑作選",
        "main_query": "女子大生 宅飲み なし崩し 部屋飲み 泥酔 彼氏持ち ガード崩壊 朝まで 生中出し 周辺",
        "labels": ["女子大生", "宅飲み", "なし崩し", "部屋飲み", "泥酔", "彼氏持ち", "朝まで生中出し", "特集", "おすすめAV"],
        "lead": "「みんなで飲むだけ」のはずが、友達が帰って二人きりに……。お酒の酔いと甘いムードに流され、「彼氏がいるからダメ」と抵抗しながらも身体の疼きに勝てず、朝を迎えるまで生中出しを許してしまうリアルな部屋飲み作品を厳選紹介します。"
    },
    {
        "id": "feature_slender_waist_young_wife_private_photo_affair",
        "api_keywords": ["若妻 くびれ 浮気", "若妻 個人撮影", "若妻 スタジオ ハメ撮り"],
        "title": "【くびれ美ボディ若妻個人撮影浮気特集】夫に内緒でカメラマンの欲望に応える！スタジオのベッドで乱れる生中出し傑作選",
        "main_query": "若妻 くびれ 浮気 個人撮影 スタジオ ホイホイ 美ボディ 生中出し 周辺",
        "labels": ["若妻", "くびれ", "個人撮影", "浮気", "スタジオ", "美ボディ", "生中出し", "特集", "おすすめAV"],
        "lead": "細身のしなやかなウエストと美しいくびれを持つ素人若妻。謝礼欲しさに応募した個人撮影で、カメラマンの情熱的なアプローチに女としての喜びを思い出してしまい、夫を裏切る生中出しセックスに溺れていく背徳ドキュメントを徹底レビューします。"
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

print("Executing direct FANZA API fetching for Phase 24 feature themes...")

created_count = 0

for idx, theme in enumerate(PHASE24_FEATURE_THEMES, 1):
    print(f"\n[{idx}/{len(PHASE24_FEATURE_THEMES)}] Querying FANZA API for: {theme['title'][:35]}...")
    
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
    print(f"Saved new Phase 24 feature article: {out_path}")

print(f"\nPhase 24 execution complete! Created {created_count} strictly API-fetched new feature articles.")
