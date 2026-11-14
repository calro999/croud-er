# -*- coding: utf-8 -*-
import os
import json
import re

POSTS_DIR = os.path.join("src", "data", "posts")
hubs = [
    ("latest_av", "総合新作AV傑作選", "digital", "videoa", None),
    ("lesbian_yuri", "レズ・百合専門新作", "digital", "videoa", "レズ"),
    ("manga_comic", "成人向けコミック・新作漫画", "ebook", "comic", None)
]

import update_monthly_hub_posts

for cat_key, cat_title, service, floor, kw in hubs:
    hub_id = f"feature_2026_11_{cat_key}_masterpiece_summary"
    hub_path = os.path.join(POSTS_DIR, f"{hub_id}.json")
    
    with open(hub_path, "r", encoding="utf-8") as f:
        d = json.load(f)
    
    # Count current cards
    review = d.get("review", "")
    current_count = len(re.findall(r'<!-- (?:追加カード|第\d+位 作品カード):', review))
    print(f"[{cat_key}] Current card count: {current_count}")
    
    needed = 30 - current_count
    if needed > 0:
        print(f"[{cat_key}] Fetching {needed} more items to reach 30...")
        # Fetch fresh items
        items = update_monthly_hub_posts.fetch_fanza_items(service, floor, keyword=kw, hits=40)
        cached_cids = update_monthly_hub_posts.load_cache()
        
        # Extract existing CIDs in this hub
        existing_cids = set(re.findall(r'<!-- (?:追加カード|第\d+位 作品カード):\s*([A-Z0-9_\-]+)\s*-->', review, re.I))
        
        new_items = []
        for item in items:
            cid = item.get("content_id")
            if cid and cid.upper() not in [c.upper() for c in existing_cids]:
                new_items.append(item)
                existing_cids.add(cid)
                if len(new_items) >= needed:
                    break
        
        print(f"[{cat_key}] Adding {len(new_items)} items...")
        new_cards = []
        for idx, item in enumerate(new_items):
            cid = item.get("content_id")
            cached_cids.add(cid)
            card = update_monthly_hub_posts.build_hub_card_html(item, current_count + idx + 1, cat_title, service)
            new_cards.append(card)
        
        insert_marker = "<!-- HUB_CARDS_START -->"
        if insert_marker in review:
            review = review.replace(insert_marker, f"{insert_marker}\n{''.join(new_cards)}")
        else:
            review += "\n" + "".join(new_cards)
        
        d["review"] = review
        # Update title if needed
        d["title"] = f"【2026年11月最新】{cat_title}おすすめ神作30選総まとめ！話題の新作・傑作選【毎日更新】"
        with open(hub_path, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        
        update_monthly_hub_posts.save_cache(cached_cids)
        print(f"[{cat_key}] Successfully updated to 30 items!")

