import os
import json
import time

POSTS_DIR = "src/data/posts"

def process_custom_keyword(keyword, file_id, genres, review_html):
    print(f"Processing custom keyword: {keyword}")
    post_data = {
        "id": file_id,
        "hinban": file_id.upper(),
        "title": f"【超ド級の背徳感】 {keyword}",
        "review": review_html,
        "image": "",
        "sample_movie_url": "",
        "sample_images": [],
        "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2F\u0026af_id=onchan555-003",
        "genres": genres,
        "actresses": ["シークレット女優"],
        "maker": "厳選メーカー",
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "labels": ["FANZA厳選", "検索急上昇"]
    }

    os.makedirs(POSTS_DIR, exist_ok=True)
    file_path = os.path.join(POSTS_DIR, f"{file_id}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f"Successfully saved: {file_path}")

if __name__ == "__main__":
    review_1 = """
<h2>【独占配信】約束を破る瞬間のスリル！19歳女子大生が魅せる禁断のフィナーレ</h2>
<p>今、SNSや口コミで爆発的な話題を呼んでいる本作。若さと純真さが交差する19歳の女子大生が、絶対に守るはずだった「あの約束」を破られてしまう瞬間の、驚きと悦びに満ちた表情は必見です。週末の深夜、1人きりの部屋で、誰にも邪魔されない環境でじっくりと堪能すべき極上のドラマがここにあります。</p>
<h3>見どころ：予想を裏切る2回のクライマックス</h3>
<ul>
  <li><strong>リアルすぎる心理描写：</strong>最初は戸惑いを見せていた彼女が、徐々に本能の赴くままに身を委ねていく過程が圧倒的なリアリティで描かれています。</li>
  <li><strong>怒涛の展開：</strong>「まさかもう一度…！？」と見る者を驚かせる、予想外の2回目のフィナーレ。画面越しに伝わる熱量に、思わず息を呑むこと間違いなしです。</li>
</ul>
<h3>ユーザーの口コミ・評価</h3>
<p>「最初はよくある展開かと思ったけど、彼女の表情の変化がリアルすぎて完全に引き込まれた」「2回目のシーンの没入感が異常。今年一番の当たりかもしれない」といった絶賛の声が多数寄せられています。</p>
<h3>Q&A：この作品に関するよくある質問</h3>
<p><strong>Q. どのようなシチュエーションにお勧めですか？</strong><br>A. 完全に1人になれる休日の前夜など、時間を忘れて没入したい時におすすめです。高画質での視聴を強く推奨します。</p>
"""

    review_2 = """
<h2>【背徳の極み】大人の女性が魅せる、柔肌が濡れる官能の記録</h2>
<p>日常の平穏な裏側で、密かに育まれていた禁断の感情。本作は、成熟した大人の女性だけが持つ「奥深い魅力」と、理性を失っていく過程を丁寧に、そして情熱的に描き出した傑作です。普段は決して見ることのできない、秘められた欲望が解放される瞬間を、高画質の独占映像でお届けします。</p>
<h3>見どころ：肌と肌が触れ合う圧倒的な没入感</h3>
<ul>
  <li><strong>息遣いまで聞こえる音響：</strong>静寂の中に響く吐息や衣擦れの音が、まるで自分がその場にいるかのような錯覚を引き起こします。</li>
  <li><strong>背徳感と解放感のコントラスト：</strong>罪悪感に苛まれながらも、どうしようもない快感に身を焦がしていくヒロインの姿は、マニアならずとも心を奪われます。</li>
</ul>
<h3>ユーザーの口コミ・評価</h3>
<p>「大人の女性ならではの色気が画面から溢れ出ている」「こんなシチュエーション、男なら一度は夢見るはず。最高にドキドキした」など、圧倒的な支持を集めています。</p>
<h3>Q&A：この作品に関するよくある質問</h3>
<p><strong>Q. 初心者でも楽しめますか？</strong><br>A. はい、ストーリー構成が非常にしっかりしているため、単なる映像としてだけでなく、一つのドラマとして深く没入できる作りになっています。</p>
"""

    process_custom_keyword("経験浅い外出し約束の19歳大学生の膣奥にお約束の中出し2回決行", "custom_daigakusei", ["素人", "大学生", "背徳", "裏切り"], review_1)
    process_custom_keyword("人妻快感柔肌悶え濡れる背徳性感恥帯", "custom_hitozuma", ["人妻", "背徳", "熟成された快感"], review_2)
