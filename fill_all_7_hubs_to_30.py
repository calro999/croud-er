# -*- coding: utf-8 -*-
import os
import json
import re

POSTS_DIR = os.path.join("src", "data", "posts")
hubs = [
    ("latest_av", "総合新作AV", "digital", "videoa", None),
    ("mature_wife", "人妻・熟女", "digital", "videoa", "人妻"),
    ("busty_beauty", "巨乳・爆乳", "digital", "videoa", "巨乳"),
    ("single_actress", "単体専属・美少女", "digital", "videoa", "単体"),
    ("amateur_pickup", "素人・ハメ撮り", "digital", "videoa", "素人"),
    ("lesbian_yuri", "レズ・百合", "digital", "videoa", "レズ"),
    ("manga_comic", "成人コミック・新作漫画", "ebook", "comic", None)
]

import update_monthly_hub_posts

for cat_key, cat_title, service, floor, kw in hubs:
    hub_id = f"feature_2026_11_{cat_key}_masterpiece_summary"
    hub_path = os.path.join(POSTS_DIR, f"{hub_id}.json")
    
    if not os.path.exists(hub_path):
        print(f"[{cat_key}] File not found, skipping")
        continue

    with open(hub_path, "r", encoding="utf-8") as f:
        d = json.load(f)
    
    review = d.get("review", "")
    current_count = len(re.findall(r'<!-- (?:追加カード|第\d+位 作品カード):', review))
    print(f"[{cat_key}] Current card count: {current_count}")
    
    needed = 30 - current_count
    if needed > 0:
        print(f"[{cat_key}] Fetching {needed} more items to reach 30...")
        # Fetch directly from FANZA API with hits=50
        items = update_monthly_hub_posts.fetch_fanza_items(service, floor, keyword=kw, hits=50)
        cached_cids = update_monthly_hub_posts.load_cache()
        
        existing_cids = set(re.findall(r'<!-- (?:追加カード|第\d+位 作品カード):\s*([A-Z0-9_\-]+)\s*-->', review, re.I))
        
        new_items = []
        for item in items:
            cid = item.get("content_id")
            if cid and cid.upper() not in [c.upper() for c in existing_cids]:
                new_items.append(item)
                existing_cids.add(cid)
                if len(new_items) >= needed:
                    break
        
        print(f"[{cat_key}] Found {len(new_items)} new API items to add.")
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
        with open(hub_path, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        
        update_monthly_hub_posts.save_cache(cached_cids)
        print(f"[{cat_key}] Successfully filled to 30 items via FANZA API!")
    else:
        print(f"[{cat_key}] Already has {current_count} items (>= 30).")

