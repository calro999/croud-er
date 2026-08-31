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

groups = defaultdict(list)
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
        norm = normalize_title(d.get("title", ""))
        groups[norm].append((f, d))

duplicates = {k: v for k, v in groups.items() if len(v) > 1}
print(f"Total manga files: {len(files)}")
print(f"Unique normalized title groups: {len(groups)}")
print(f"Duplicate groups count: {len(duplicates)}")

total_dup_files = sum(len(v) for v in duplicates.values())
print(f"Total duplicate files to consolidate: {total_dup_files} -> {len(duplicates)}")

for k, v in list(duplicates.items())[:10]:
    print(f"\nGroup: '{k}' ({len(v)} files)")
    for f, d in v:
        print(f"   - {d.get('id')}: {d.get('title')}")
