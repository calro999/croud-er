import os
import json
import glob
import re

POSTS_DIR = "src/data/posts"

# AI臭いクリシェフレーズの検出・置換辞書
AI_CLICHE_REPLACEMENTS = {
    r"いかがでしたでしょうか[？\?]?": "",
    r"いかがだったでしょうか[？\?]?": "",
    r"ぜひその目で確かめてみてください[。！!]*": "本編でその圧倒的な熱量を体感してください！",
    r"是非その目で確かめてみてください[。！!]*": "本編でその圧倒的な熱量を体感してください！",
    r"と言えるでしょう[。]": "と言えます。",
    r"に違いありません[。]": "に間違いありません。",
    r"ではないでしょうか[。]": "と実感させられます。",
    r"必見の価値ありです[。]": "見逃せない神シーンです。",
    r"一見の価値ありです[。]": "必ず観ておくべき名場面です。",
    r"チェックしてみてはいかがでしょうか[。]": "ぜひチェックしてみてください！",
    r"間違いなしです[。]": "間違いなく最高峰の仕上がりです。",
    r"至高のひとときをお過ごしください[。]": "至福の射精体験をお楽しみください！"
}

# 誤字・不自然な表現の修正辞書
TYPO_REPLACEMENTS = {
    r"オ●ニー": "オナニー",
    r"レ●プ": "調教レ○プ",
    r"＆amp;": "＆",
    r"&amp;": "&",
    r"&quot;": '"',
    r"&#39;": "'",
    r"&lt;": "<",
    r"&gt;": ">",
    r"　+": " ", # 連続全角スペースの整形
    r"<p>\s*</p>": "", # 空段落削除
    r"<h3>\s*</h3>": "", # 空見出し削除
    r"<h4>\s*</h4>": ""
}

def clean_and_polish_text(html_text):
    if not html_text:
        return ""
    
    text = html_text
    
    # 誤字・タグ整形
    for pattern, repl in TYPO_REPLACEMENTS.items():
        text = re.sub(pattern, repl, text)
        
    # AIクリシェの置換
    for pattern, repl in AI_CLICHE_REPLACEMENTS.items():
        text = re.sub(pattern, repl, text)
        
    # 余分な改行やスペースの整形
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    return text.strip()

print("Auditing and polishing all post files in src/data/posts...")

all_posts = glob.glob(os.path.join(POSTS_DIR, "*.json"))
fixed_count = 0
short_count = 0

for file_path in all_posts:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        title = data.get("title", "")
        review = data.get("review", "") or data.get("content", "")
        
        orig_review = review
        polished_review = clean_and_polish_text(review)
        
        # タイトルもクリーニング
        orig_title = title
        polished_title = clean_and_polish_text(title)
        polished_title = re.sub(r'[\r\n\t]+', ' ', polished_title).strip()
        
        changed = (orig_review != polished_review) or (orig_title != polished_title)
        
        # 短すぎる記事の検知
        if len(polished_review) < 300:
            short_count += 1
            
        if changed:
            data["title"] = polished_title
            data["review"] = polished_review
            data["content"] = polished_review
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            fixed_count += 1
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print(f"\nAudit complete! Total checked: {len(all_posts)}")
print(f"Polished & fixed files: {fixed_count}")
print(f"Short files flagged (< 300 chars): {short_count}")
