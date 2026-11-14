# -*- coding: utf-8 -*-
import os
import json
import re

POSTS_DIR = os.path.join("src", "data", "posts")

hubs = [
    ("latest_av", "【2026年11月最新AV傑作選】FANZA話題の新作・神作タイトル完全速報まとめ", "総合新作AV"),
    ("lesbian_yuri", "【2026年11月最新レズ・百合AV傑作選】極上美女の濃密絡み・人気名作速報まとめ", "レズ・百合専門新作"),
    ("manga_comic", "【2026年11月最新成人コミック傑作選】FANZA人気同人・新作漫画レビュー速報まとめ", "成人コミック・新作漫画")
]

for cat_key, new_title, category_label in hubs:
    hub_id = f"feature_2026_11_{cat_key}_masterpiece_summary"
    hub_path = os.path.join(POSTS_DIR, f"{hub_id}.json")
    if not os.path.exists(hub_path):
        continue
    
    with open(hub_path, "r", encoding="utf-8") as f:
        d = json.load(f)
    
    d["title"] = new_title
    review = d.get("review", "")
    
    # Remove meta / automated mentions
    review = re.sub(r'【2026年11月最新】.*?おすすめ神作30選総まとめ！話題の新作・傑作選【毎日更新】', new_title, review)
    review = re.sub(r'【2026年11月最新】.*?まとめ！話題の新作・傑作選【毎日更新】', new_title, review)
    review = re.sub(r'FANZA公式API自動連携・.*?最新作デイリー更新', f'FANZA厳選・2026年11月 話題の新作セレクション', review)
    review = re.sub(r'公式APIからリアルタイムに新着・高評価作品を毎日追加更新しています。', 'FANZAで配信された注目の人気作・高評価タイトルを厳選して随時お届けしています。', review)
    review = re.sub(r'<p class="font-bold text-white">毎日自動追加</p>\s*<p class="text-\[10px\] text-slate-400">新作を最速レビュー</p>', '<p class="font-bold text-white">最新作随時更新</p>\n        <p class="text-[10px] text-slate-400">注目作を速報レビュー</p>', review)
    review = re.sub(r'<p class="font-bold text-white">毎日自動追加</p>\s*<p class="text-\[10px\] text-slate-400">最新リリースを最速網羅</p>', '<p class="font-bold text-white">最新作随時更新</p>\n        <p class="text-[10px] text-slate-400">注目作を速報レビュー</p>', review)
    review = re.sub(r'<span>🔥</span><span>FANZA公式API自動連携.*?</span>', '<span>🔥</span><span>FANZA厳選・2026年11月 話題の新作セレクション</span>', review)
    
    d["review"] = review
    with open(hub_path, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"Updated title and cleaned meta for {hub_id}")

