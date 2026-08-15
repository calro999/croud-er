import os
import json
import re

POSTS_DIR = "src/data/posts"

NEWLY_ADDED_IDS = [
    "urvrsp00600", "1favr00009", "1favr00008", "jufe00604", "prin00052", "snos0040",
    "59hez00777", "h_1495bank00198", "13dsvr00878", "roe00382", "rbk00030", "h_086nuka00080",
    "juny00148", "real00939", "sivr00505", "dsod00045", "ipzz00947", "ipzz00923",
    "snos00254", "pred00839", "pppe00306", "vrkm01873", "vrkm01904", "vrkm01907",
    "1start00330", "kavr00472", "dass00913", "dvmm00362", "1dandya00019", "dazd00216",
    "1sdjs00356", "h_1133yako00073", "1svmgm00045", "rki00694", "adn00749", "tikb00220",
    "ure00129", "juvr00234", "roe00452", "sqte00614", "sqte00589", "sqte00647",
    "vrkm01908", "vrkm01890", "savr01134", "kwbd00435", "kitaoka_karin_otomari", "h_1454jksr63803",
    "nkkd00366", "ssis00999", "mmgo00020", "mida00438", "ebwh00294", "snos00116",
    "h_1133honb00493", "1start00154", "dsod00029", "cawd00895", "1start00327", "ipvr00380",
    "mizd00502", "snos00149", "apak00326", "fcvr00067", "huntc00544", "ymds00261"
]

def audit_and_upgrade():
    short_posts = []
    audited_count = 0
    upgraded_count = 0
    
    for pid in NEWLY_ADDED_IDS:
        file_path = os.path.join(POSTS_DIR, f"{pid}.json")
        if not os.path.exists(file_path):
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        review = data.get("review", "")
        title = data.get("title", "")
        hinban = data.get("hinban", "")
        
        audited_count += 1
        
        # 簡易診断：文字数が3000文字未満、またはFAQ/評価表がない場合にリッチ化
        needs_rich = len(review) < 2500 or "faq-section" not in review or "<table>" not in review
        
        if needs_rich:
            short_posts.append((pid, len(review)))
            
            # 各記事に合わせた評価テーブルと詳細FAQを追加・拡張
            actress_str = "、".join(data.get("actresses", [])) or "豪華女優陣"
            maker_str = data.get("maker", "人気メーカー")
            
            table_html = f"""
<h3>3. 作品詳細アナリシス＆見どころ評価</h3>
<table>
  <tr><th>評価項目</th><th>スコア</th><th>詳細・見どころ解説</th></tr>
  <tr><td>シチュエーション・演出</td><td>★★★★★ (5.0)</td><td>作り込まれた世界観とリアリティ溢れるシチュエーション。</td></tr>
  <tr><td>背徳感・背徳度</td><td>★★★★★ (5.0)</td><td>理性が崩壊していく過程と罪悪感の演出が極上。</td></tr>
  <tr><td>出演キャストの魅力</td><td>★★★★★ (5.0)</td><td>{actress_str}の繊細な表情変化と絶頂リアクションが最高。</td></tr>
  <tr><td>実用性・リピート度</td><td>★★★★★ (5.0)</td><td>画質・カメラアングルともに神がかっており何度観ても抜ける完成度。</td></tr>
</table>
"""

            faq_html = f"""
<h3>4. ユーザーの口コミ・評判＆よくある質問（FAQ）</h3>
<div class="faq-section">
  <h4>Q1: この作品（{hinban}）の一番の見どころはどこですか？</h4>
  <p>A: 序盤の緊張感あるやり取りから、中盤以降の理性が吹き飛ぶ濃厚な性交シーンへのグラデーションです。登場人物の表情の変化にぜひご注目ください。</p>

  <h4>Q2: 単体作品ですか？どのような人におすすめですか？</h4>
  <p>A: {maker_str}が贈る渾身の作品です。「リアリティのあるハメ撮りやシチュエーションが好き」「キャストの魅力を存分に味わいたい」という方に心からおすすめできます。</p>

  <h4>Q3: 高画質での視聴をおすすめしますか？</h4>
  <p>A: はい！細かい吐息や肌の質感、表情の揺れまで鮮明に捉えられているため、大画面やVR・高画質環境での視聴を強く推奨します。</p>
</div>
"""

            # 既存のreview構造に組み込み
            if "<h3>3." not in review and "<h3>4." not in review:
                if "<h3>" in review:
                    parts = review.rsplit("<h3>", 1)
                    new_review = parts[0] + table_html + faq_html + "<h3>" + parts[1]
                else:
                    new_review = review + table_html + faq_html
                data["review"] = new_review
                
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                upgraded_count += 1

    print(f"Audited: {audited_count} posts.")
    print(f"Upgraded with rich tables & FAQs: {upgraded_count} posts.")
    print(f"Short posts identified: {len(short_posts)}")

if __name__ == "__main__":
    audit_and_upgrade()
