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

# 周辺クエリを狙う10大特集テーマの定義（カニバリズム回避の特集・比較・まとめ切り口）
FEATURE_THEMES = [
    {
        "id": "feature_island_sisters_innocent",
        "api_keywords": ["無人島 三姉妹", "性を知らない", "CAWD"],
        "title": "【2026年最新】無人島・秘境×無垢な少女たち！性を知らない美少女に性教育を施すおすすめ傑作AV特集",
        "main_query": "無人島 三姉妹 性指導 CAWD-998 暁奇奇 周辺",
        "labels": ["無人島", "三姉妹", "性教育", "CAWD", "特集", "まとめ", "おすすめAV", "2026最新"],
        "lead": "「文明から隔絶された無人島で育った純真無垢な美少女たちに、一から性の悦びを教え込む……」男なら誰もが一度は妄想する究極のロマン。大ヒット作『CAWD-998（暁奇奇）』を筆頭に、無知な少女たちの純真さが快楽に染まっていくおすすめ傑作タイトルを厳選して徹底比較紹介します！"
    },
    {
        "id": "feature_ntr_husband_watching",
        "api_keywords": ["夫の目の前", "ドラレコNTR", "NSM 人妻"],
        "title": "【背徳の極致】夫の目の前で犯される美貌人妻＆車載カメラNTR傑作選！屈辱と快楽に溺れる寝取られAV特集",
        "main_query": "夫の目の前 NTR ドラレコNTR NSM-074 周辺",
        "labels": ["NTR", "寝取られ", "夫の前で", "ドラレコNTR", "NSM", "人妻", "特集", "おすすめAV"],
        "lead": "愛する夫が見つめる目の前で、抵抗しながらも逞しい男の愛撫に屈してしまう妻たち。『NSM-074』や『ドラレコNTR 38』など、罪悪感と羞恥心が最高のスパイスとなり絶頂を迎える、NTRマニア必見の至高の寝取られ作品を徹底解説します。"
    },
    {
        "id": "feature_teacher_lesbian_harem",
        "api_keywords": ["放課後 レズ", "miru 村上悠華", "SNOS"],
        "title": "【学校の秘密】美女教師たちの禁断レズキスを目撃！放課後3Pハーレムに巻き込まれる背徳学園AV特集",
        "main_query": "女教師 レズキス miru 村上悠華 SNOS-353 周辺",
        "labels": ["女教師", "レズキス", "百合", "SNOS", "miru", "村上悠華", "3Pハーレム", "特集"],
        "lead": "生徒の前では厳格・優しい先生たちが、放課後の準備室で舌を絡ませ合うレズ関係に耽っていたら……？『SNOS-00353』の奇跡のWキャストをはじめ、秘密の現場を目撃したことから始まるご褒美お仕置きハーレム作品をまとめました。"
    },
    {
        "id": "feature_ultra_immersive_vr",
        "api_keywords": ["VR 高画質", "DSVR", "VRKM"],
        "title": "【圧倒的没入感】息づかいまで肌で感じる！超高画質8K/4K密着VRおすすめ傑作タイトル徹底比較",
        "main_query": "VR AV おすすめ DSVR-01998 VRKM-1776 周辺",
        "labels": ["VR", "超高画質", "8KVR", "DSVR", "VRKM", "ゼロ距離", "おすすめVR", "特集"],
        "lead": "二次元の画面越しでは絶対に味わえない、手を伸ばせば触れられるかのような実在感。『DSVR-01998』や『VRKM-1776』など、立体音響（バイノーラル）とゼロ距離アングルで脳がとろける極上VR作品を厳選ナビゲートします。"
    },
    {
        "id": "feature_mens_esthe_ura_option",
        "api_keywords": ["メンズエステ 裏オプ", "メンエス嬢", "KWBD"],
        "title": "【密室の甘い罠】ちょろいメンエス嬢を口説き落とす！裏オプ生ハメ＆中出し解禁おすすめメンズエステAV特集",
        "main_query": "メンズエステ 裏オプ 合法ロリ メンエス嬢 生ハメ 周辺",
        "labels": ["メンズエステ", "裏オプ", "生ハメ", "中出し", "つるぺた", "KWBD", "特集", "おすすめAV"],
        "lead": "アパートの一室、オイルマッサージの密室で繰り広げられる本番交渉のリアル。小柄で可愛らしいメンエス嬢がチップと甘い言葉にあっさり陥落する、男の夢を具現化した裏オプ作品の傑作選をお届けします。"
    },
    {
        "id": "feature_street_nanpa_amateur",
        "api_keywords": ["マジックミラー号", "素人ナンパ 中出し", "NSFS"],
        "title": "【完全素人ハメ撮り】街頭ナンパからホテル直行！マジックミラー号＆女子大生騙し中出しおすすめ特集",
        "main_query": "素人ナンパ マジックミラー号 MMGO-00019 NSFS-498 周辺",
        "labels": ["素人ナンパ", "マジックミラー号", "ハメ撮り", "女子大生", "生中出し", "MM号", "特集"],
        "lead": "街を行き交う素人女性たちのガードを巧妙なトークで崩し、カメラの前で本気のアクメを晒させる！『マジックミラー号（MMGO-019）』や『NSFS-498』など、作り物ではない生々しいエロスを徹底レビュー。"
    },
    {
        "id": "feature_top_actress_unlimited_creampie",
        "api_keywords": ["河北彩花 生中出し", "S1 500分", "希望みう"],
        "title": "【永久保存版】国民的トップ女優たちが理性を捨てて挑む！限界突破の生中出し＆受精特大ボリュームAV特集",
        "main_query": "河北彩花 500分 生中出し 希望みう S1 特集 周辺",
        "labels": ["河北彩花", "希望みう", "S1", "生中出し", "特大ボリューム", "500分", "女優特集", "殿堂入り"],
        "lead": "AV界の頂点に君臨する国民的美女たちが、一切のゴムなしで何発もの精液を受け止め続ける！『河北彩花 最終章500分』や大型新人『希望みう』のデビュー作など、圧倒的な美貌と狂乱の快楽が交錯する最高峰作品を集めました。"
    },
    {
        "id": "feature_smile_creampie_panic_ecstasy",
        "api_keywords": ["由良かな 膣内射精", "泉りおん パニック絶頂", "笑顔抜き"],
        "title": "【至高の笑顔抜き＆パニック絶頂】ロリ系美少女が快楽とくすぐりに悶絶！愛され中出し＆限界アクメ傑作選",
        "main_query": "由良かな 至高の膣内射精 泉りおん パニック絶頂 周辺",
        "labels": ["由良かな", "泉りおん", "笑顔抜き", "パニック絶頂", "ロリ系", "くすぐり", "中出し", "特集"],
        "lead": "心からのエンジェルスマイルで中出しを受け止める『由良かな』と、オイルまみれで理性が吹き飛ぶ『泉りおん』。対照的ながらもどちらも男の本能を直撃する、ロリ系美少女AVの最高到達点を徹底レポートします。"
    },
    {
        "id": "feature_onsen_affair_mature_wife",
        "api_keywords": ["人妻 温泉不倫", "人妻湯恋旅行", "三十路 人妻"],
        "title": "【旅情と大人の色気】露天風呂立ちバック＆和室敷布団で乱れる！風情ある温泉旅館の人妻不倫おすすめ特集",
        "main_query": "人妻 温泉不倫 人妻湯恋旅行 三十路 人妻 オナニー 周辺",
        "labels": ["人妻", "温泉不倫", "露天風呂", "人妻湯恋旅行", "三十路", "熟女", "GS", "特集"],
        "lead": "日常の家事や育児、セックスレスの悩みから解放され、旅先で女としての悦びに身を焦がす人妻たち。『人妻湯恋旅行169』をはじめ、湯けむりとしっとりした柔肌が織りなす大人の官能名作を特集します。"
    },
    {
        "id": "feature_extreme_paizuri_cabaret_girl",
        "api_keywords": ["木下ひまり パイズリ", "キャバ嬢 オフパコ", "巨乳 ドM"],
        "title": "【極上美乳の暴力】峡谷パイズリ挟み撃ち＆美形キャバ嬢オフパコ！男根を骨抜きにする搾精AV特集",
        "main_query": "木下ひまり パイズリ 美形キャバ嬢 Fカップ オフパコ 周辺",
        "labels": ["木下ひまり", "パイズリ", "キャバ嬢", "オフパコ", "巨乳", "美乳", "搾精", "特集"],
        "lead": "完璧な美乳で包み込まれる至福のパイズリと、高嶺の花のキャバ嬢がホテルでメス豚へと堕ちる生々しいオフパコ。『木下ひまり』の神乳テクニックなど、視覚と快感を極限まで刺激する搾精作品をまとめました。"
    }
]

def fetch_from_fanza_api(keyword, hits=4):
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
            return data.get("result", {}).get("items", [])
    except Exception as e:
        print(f"API Error for '{keyword}': {e}")
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

print("Starting FANZA API fetching for all 10 cluster feature themes...")

created_features = []

for idx, theme in enumerate(FEATURE_THEMES, 1):
    print(f"\n[{idx}/{len(FEATURE_THEMES)}] Querying API for theme: {theme['title'][:40]}...")
    
    all_items = []
    seen_ids = set()
    
    for kw in theme["api_keywords"]:
        items = fetch_from_fanza_api(kw, hits=3)
        for it in items:
            cid = it.get("content_id")
            if cid and cid not in seen_ids:
                seen_ids.add(cid)
                all_items.append(it)
        time.sleep(0.3) # API負荷配慮
    
    print(f" -> Found {len(all_items)} real works from FANZA API.")
    
    # 特集記事のHTMLコンテンツを構築
    feature_html = f"""<h2>{theme['title']}</h2>

<p class="feature-lead">{theme['lead']}</p>

<div class="feature-toc">
  <h3>📑 本特集の目次・見どころインデックス</h3>
  <ul>
    <li><a href="#section-overview">1. このシチュエーションが熱狂的な人気を集める理由</a></li>
    <li><a href="#section-works">2. FANZA公式・厳選おすすめタイトル徹底解剖</a></li>
    <li><a href="#section-comparison">3. タイプ別・抜きどころ比較マトリクス</a></li>
    <li><a href="#section-faq">4. よくある質問・失敗しない選び方（FAQ）</a></li>
    <li><a href="#section-summary">5. 総括・まとめ</a></li>
  </ul>
</div>

<h3 id="section-overview">1. このシチュエーションが熱狂的な人気を集める理由</h3>
<p>検索ボリュームが急上昇している「{theme['main_query']}」。なぜこれほどまでに多くの読者がこのジャンルに惹きつけられるのか。その核心は、<strong>「日常では決して味わえない究極のギャップと背徳感」</strong>にあります。作り込まれた世界観と女優陣の生々しい快楽リアクションが融合することで、単なるオナニーの道具を超えた強烈な興奮と没入感を提供してくれます。</p>

<h3 id="section-works">2. FANZA公式・厳選おすすめタイトル徹底解剖</h3>
<p>ここでは、リアルタイムに売れ筋・評価の高い実在作品をピックアップし、それぞれの見どころとおすすめポイントを詳細に解説します。</p>
"""

    for item_idx, it in enumerate(all_items[:4], 1):
        raw_title = it.get("title", "")
        cid = it.get("content_id", "")
        hinban = format_hinban(cid)
        comment = it.get("comment", "") or "公式配信中の大人気タイトル。息を呑むような臨場感と濃厚な絡みが見どころです。"
        
        aff_url = it.get("affiliateURL", "")
        if aff_url:
            aff_url = aff_url.replace("onchan555-999", LINK_AFFILIATE_ID)
            
        img_url = it.get("imageURL", {}).get("large") or it.get("imageURL", {}).get("list") or ""
        actresses = ", ".join([a.get("name", "") for a in it.get("iteminfo", {}).get("actress", [])]) or "人気キャスト"
        maker = it.get("iteminfo", {}).get("maker", [{}])[0].get("name", "公式レーベル") if it.get("iteminfo", {}).get("maker") else "公式レーベル"
        price = it.get("prices", {}).get("price", "3,280円")
        if not str(price).endswith("円"):
            price = f"{price}円"

        feature_html += f"""
<div class="work-card-feature" style="border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px; margin: 24px 0; background: #ffffff;">
  <h4>【第{item_idx}位】{raw_title}</h4>
  <p><strong>品番：</strong><span class="badge">{hinban}</span> | <strong>出演：</strong>{actresses} | <strong>メーカー：</strong>{maker} | <strong>価格：</strong>{price}</p>
  {f'<p style="text-align:center;"><a href="{aff_url}" target="_blank" rel="nofollow noopener"><img src="{img_url}" alt="{raw_title}" style="max-width:100%; border-radius:8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);" /></a></p>' if img_url else ''}
  <div class="work-description">
    <h5>💡 見どころ＆ストーリー解説</h5>
    <p>{comment}</p>
    <h5>🔥 ここが抜ける！注目ポイント</h5>
    <ul>
      <li><strong>生々しい表情の変化：</strong>恥じらいと快楽が入り混じるリアルな瞳と紅潮した肌。</li>
      <li><strong>密着アングルの破壊力：</strong>結合部と吐息が生々しく伝わる至高のカメラワーク。</li>
      <li><strong>納得のフィナーレ：</strong>惜しみなく注ぎ込まれる中出しと恍惚の余韻。</li>
    </ul>
    <p style="text-align: center; margin-top: 16px;">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" style="display: inline-block; background: #e11d48; color: #ffffff; font-weight: bold; padding: 12px 28px; border-radius: 9999px; text-decoration: none; box-shadow: 0 4px 14px rgba(225,29,72,0.35);">▶ FANZA公式サイトで作品詳細・サンプル動画を見る</a>
    </p>
  </div>
</div>
"""

    feature_html += f"""
<h3 id="section-comparison">3. タイプ別・抜きどころ比較マトリクス</h3>
<p>それぞれの作品の持つ特徴と、どんな気分・シチュエーションにおすすめかを比較表にまとめました。</p>

<table>
  <tr><th>作品・ジャンル</th><th>実用性・抜き度</th><th>シチュエーション</th><th>おすすめのユーザー層</th></tr>
  <tr><td>本特集厳選 第1位</td><td>★★★★★ (5.0)</td><td>ストーリー＆没入感重視</td><td>じっくりと興奮を高めて濃厚に射精したい方</td></tr>
  <tr><td>本特集厳選 第2位</td><td>★★★★★ (5.0)</td><td>ビジュアル＆フェチ重視</td><td>キャストの圧倒的な可愛さ・美乳を堪能したい方</td></tr>
  <tr><td>本特集厳選 第3位</td><td>★★★★☆ (4.8)</td><td>ハード＆アクメ重視</td><td>連続絶頂・激しいピストンで即抜きしたい方</td></tr>
</table>

<h3 id="section-faq">4. よくある質問・失敗しない選び方（FAQ）</h3>
<div class="faq-section">
  <h4>Q1: このジャンルの作品は初心者でも楽しめますか？</h4>
  <p>A: はい、本記事で厳選した作品はどれもシチュエーションの説明が丁寧で、感情移入しやすい王道の構成になっていますので、初めての方でも安心して楽しめます。</p>

  <h4>Q2: スマホでの視聴やストリーミング再生は可能ですか？</h4>
  <p>A: はい、FANZA公式のデジタル配信に対応しており、PCはもちろんスマートフォンやタブレットのブラウザ、専用アプリで即座に高画質ストリーミング・ダウンロード視聴が可能です。</p>

  <h4>Q3: カニバリズムを避けて自分にぴったりの1本を見つけるには？</h4>
  <p>A: 各作品の個別レビュー記事（当サイト内の詳細ネタバレ解説）と本特集を併せてご覧いただくことで、好みの体位やフェチ要素にジャストフィットする作品を確実に見つけることができます。</p>
</div>

<h3 id="section-summary">5. 総括・まとめ</h3>
<p>『{theme['title']}』で取り上げた作品群は、どれも熱狂的な支持を集め続ける名作ばかりです。気になる作品があれば、ぜひ公式サイトの無料サンプル動画をチェックして、その極上のエロティシズムを体験してみてください！</p>
"""

    # 記事データオブジェクト
    feature_post = {
        "id": theme["id"],
        "title": theme["title"],
        "hinban": f"FEATURE ({theme['id']})",
        "price": "配信価格に準ずる",
        "actress": "特集厳選キャスト",
        "director": "FANZA公式 / 特集企画班",
        "affiliate_url": all_items[0].get("affiliateURL", "").replace("onchan555-999", LINK_AFFILIATE_ID) if all_items else "https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F&af_id=onchan555-003&ch=toolbar&ch_id=link",
        "image_url": all_items[0].get("imageURL", {}).get("large", "") if all_items else "",
        "labels": theme["labels"],
        "review": feature_html,
        "content": feature_html
    }

    out_file = os.path.join(POSTS_DIR, f"{theme['id']}.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(feature_post, f, ensure_ascii=False, indent=2)

    created_features.append(out_file)
    print(f"Successfully saved feature post: {out_file}")

print(f"\nAll {len(created_features)} feature articles created successfully via direct FANZA API!")
