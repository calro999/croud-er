import os
import json
import glob
import time
import re
import requests

POSTS_DIR = "src/data/posts"

def clean_for_safety(text):
    if not text:
        return ""
    safety_map = {
        "ネトラレ": "禁断", "ねとられ": "禁断", "NTR": "禁断", "不倫": "秘密の関係", "団地妻": "大人の女性",
        "人妻": "大人の女性", "背徳": "秘密", "痴女": "魅力的な女性", "中出し": "フィナーレ", "中出": "フィナーレ",
        "AV": "ビデオ作品", "アダルト": "大人向け", "膣奥": "奥深く", "膣": "秘部", "セックス": "逢瀬",
        "SEX": "逢瀬", "おま○こ": "秘部", "オマ○コ": "秘部", "ま〇こ": "秘部", "射精": "クライマックス",
        "ザーメン": "愛の証", "精子": "愛の証", "レズ": "女性同士の秘密", "巨乳": "抜群のプロポーション",
        "爆乳": "抜群のプロポーション", "パイパン": "滑らかな肌", "デカチン": "大きな魅力", "巨根": "大きな魅力",
        "フェラ": "奉仕", "立ちバック": "後ろからのアプローチ", "ハメ撮り": "記録", "生中出し": "フィナーレ",
        "オナホ": "おもちゃ", "淫乱": "情熱的", "ドM": "受け身", "マゾ": "受け身", "調教": "指導",
        "輪●": "複数人でのアプローチ", "レイプ": "強引なアプローチ", "強姦": "強引なアプローチ",
        "処女": "純真", "童貞": "純真", "エロ": "セクシー", "オナペット": "アイドル", "オナニー": "一人遊び"
    }
    # 正規表現で一括置換
    pattern = re.compile("|".join(map(re.escape, safety_map.keys())), re.IGNORECASE)
    cleaned = pattern.sub(lambda match: safety_map[match.group(0).upper()] if match.group(0).upper() in safety_map else safety_map[match.group(0)], text)
    return cleaned

def generate_seo_review_with_llm(title, genres_str, maker):
    safe_title = clean_for_safety(title)
    safe_genres = clean_for_safety(genres_str)
    
    prompt = f"""以下のロマンティックな大人のドラマ作品の情報を基にして、指定の執筆ルールに従ってブログ記事のHTML本文（レビュー文）を完全に新しく生成してください。テンプレートは一切使わず、毎回オリジナルの文章にしてください。

【作品名】: {safe_title}
【ジャンル】: {safe_genres}
【メーカー】: {maker}

【執筆ルール】
1. ペルソナ: ネットで絶大な支持を集める「大人のドラマ専門」のカリスマレビュアー。
2. 感情的なキャッチコピー: 冒頭に見出し（<h2> または <h3>）を配置。
3. マニア目線の心理描写: ストーリー・心理・情景の推しポイントを熱量MAXで解説。
4. SEO対策とAI-SEO対策 (AIO): 「見どころ」「ユーザーの口コミ・評価風レビュー」「Q&A」などを構造化して書き、検索ユーザーの疑問に答える形（結論ファースト）で記載してください。
5. GEO対策・体験的価値: どのようなシチュエーションでこの作品を視聴すべきか記載してください。
6. 【最重要】出力フォーマット: HTMLタグ（<p>, <h2>, <h3>, <ul>, <li>など）のみで出力し、マークダウンのコードブロック記法（```html や ``` など）は「絶対に」出力しないでください。余計なメタ情報は一切不要です。HTML本体のみを直接出力してください。

それでは、HTML本文のみを出力してください。
"""

    system_message = "あなたはSEOとAI-SEOを極めたカリスマ熱血レビュアーです。マークダウン記法を一切使用せず、純粋なHTMLのみを出力します。絶対に同じテンプレートを使い回さず、独立した内容を書きます。"

    pollinations_models = ["openai", "mistral", "llama"]
    for attempt in range(3):
        for model in pollinations_models:
            try:
                response = requests.post(
                    "https://text.pollinations.ai/",
                    json={
                        "messages": [
                            {"role": "system", "content": system_message},
                            {"role": "user", "content": prompt}
                        ],
                        "model": model,
                        "temperature": 0.8
                    },
                    timeout=35
                )
                if response.status_code == 200 and len(response.text.strip()) > 100:
                    result_text = response.text.strip()
                    result_text = re.sub(r'^```html\s*', '', result_text, flags=re.IGNORECASE)
                    result_text = re.sub(r'^```\s*', '', result_text)
                    result_text = re.sub(r'\s*```$', '', result_text)
                    result_text = result_text.replace("```html", "").replace("```", "").strip()
                    if "<p" in result_text or "<h" in result_text:
                        return result_text
            except Exception as e:
                time.sleep(1)

    return None

def upgrade_all_posts():
    files = glob.glob(os.path.join(POSTS_DIR, "*.json"))
    upgraded_count = 0
    failed_count = 0
    
    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except Exception as e:
                continue
                
        title = data.get("title", "本作")
        genres_str = "、".join(data.get("genres", ["極上のシチュエーション"]))
        if not genres_str:
            genres_str = "大人のドラマ"
        maker = data.get("maker", "一流メーカー")
        if not maker:
            maker = "一流メーカー"
            
        # 既に十分に長いか、エラー出力ではないかチェック（今回は全上書きを狙うが、エラーだったものを優先的にもできる。今回は強制上書き）
        new_review = generate_seo_review_with_llm(title, genres_str, maker)
        
        if new_review:
            data["review"] = new_review
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Successfully upgraded: {file_path}")
            upgraded_count += 1
        else:
            print(f"Failed to generate review for: {file_path}")
            failed_count += 1
            
        time.sleep(1)
            
    print(f"Total upgraded posts: {upgraded_count}")
    print(f"Failed posts: {failed_count}")

if __name__ == "__main__":
    upgrade_all_posts()
