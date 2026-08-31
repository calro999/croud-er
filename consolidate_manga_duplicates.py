import os
import json
import glob
import re
from collections import defaultdict

manga_dir = "src/data/manga"
files = glob.glob(f"{manga_dir}/*.json")

def normalize_title(title):
    t = re.sub(r'【.*?】', '', title)
    t = re.sub(r'\[.*?\]', '', t)
    t = re.sub(r'（.*?）', '', t)
    t = re.sub(r'\(.*?\)', '', t)
    t = re.sub(r'[\s　]+', '', t)
    # 単話番号や巻数を除去 (例: 第1話, 1, #1)
    t = re.sub(r'(第?\d+話|第?\d+巻|vol\.\d+|\#\d+|\d+$)', '', t, flags=re.IGNORECASE)
    return t.strip() or title

def rank_candidate(d):
    title = d.get("title", "")
    score = 0
    if "完全版" in title:
        score += 100
    if "合冊版" in title:
        score += 80
    if "特装版" in title:
        score += 50
    if "単話" in title or "分冊版" in title:
        score -= 50
    if d.get("tachiyomi_url"):
        score += 20
    if len(d.get("genres", [])) > 0:
        score += len(d.get("genres", []))
    score += len(d.get("review", "")) / 1000.0
    return score

groups = defaultdict(list)
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
        norm = normalize_title(d.get("title", ""))
        groups[norm].append((f, d))

to_delete = []
consolidated_count = 0

for norm, items in groups.items():
    if len(items) > 1:
        consolidated_count += 1
        # スコア順にソート (最も完全なものを先頭に残す)
        items_sorted = sorted(items, key=lambda x: rank_candidate(x[1]), reverse=True)
        best_f, best_d = items_sorted[0]
        
        # 統合: ジャンルや作者情報を取りこぼさないようにマージ
        all_genres = set(best_d.get("genres", []))
        all_authors = set(best_d.get("author", []))
        all_labels = set(best_d.get("labels", []))
        
        for other_f, other_d in items_sorted[1:]:
            to_delete.append(other_f)
            for g in other_d.get("genres", []):
                all_genres.add(g)
            for a in other_d.get("author", []):
                all_authors.add(a)
            for l in other_d.get("labels", []):
                all_labels.add(l)
            if not best_d.get("tachiyomi_url") and other_d.get("tachiyomi_url"):
                best_d["tachiyomi_url"] = other_d.get("tachiyomi_url")
        
        best_d["genres"] = list(all_genres)
        best_d["author"] = list(all_authors)
        best_d["labels"] = list(all_labels)
        
        # 保存
        with open(best_f, 'w', encoding='utf-8') as fp:
            json.dump(best_d, fp, ensure_ascii=False, indent=2)

print(f"Total duplicate groups processed: {consolidated_count}")
print(f"Files to delete: {len(to_delete)}")

# 削除実行
for f in to_delete:
    os.remove(f)
    print(f"Deleted duplicate: {os.path.basename(f)}")

remaining = glob.glob(f"{manga_dir}/*.json")
print(f"Remaining clean manga files: {len(remaining)}")
