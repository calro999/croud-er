import os
import random
import re
import time
import json
import requests
from update_all_manga_articles import generate_deep_custom_review

SITE = "blogger-er"
CACHE_FILE = "manga_cache.txt"
POSTS_DIR = "src/data/manga"
API_ID = "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = "onchan555-999"
LINK_AFFILIATE_ID = "onchan555-003"
TARGET_NEW_POSTS = 500  # さらに500作品を直接FANZA APIから追加

# レズ・百合・NTR・人妻・美少女・背徳など、当サイトに最も適した多様な検索キーワード
SEARCH_KEYWORDS = [
    "百合", "レズ", "NTR", "人妻", "寝取られ", "女性同士", "女子校生", "巨乳", "美少女", 
    "幼なじみ", "女教師", "お姉さん", "ギャル", "催眠", "調教", "不倫", "フルカラー",
    "同棲", "義母", "義妹", "後輩", "先輩", "令嬢", "メイド", "コスプレ", "露出", "温泉", "密着",
    "ハメ撮り", "痴女", "主婦", "OL", "放課後", "黒ギャル", "淫乱", "処女", "肉便器", "アナル", "中出し",
    "近親相姦", "母乳", "パイズリ", "妹", "姉", "女装", "男の娘", "逆レイプ", "監禁", "洗脳", "マゾ", "サド",
    "オタサーの姫", "ツンデレ", "クーデレ", "ヤンデレ", "エルフ", "獣耳", "JK", "JD", "処女喪失", "ザーメン", "子宮", "開発",
    "水着", "下着", "制服", "ナース", "女上司", "若妻", "寝取り", "ハーレム", "媚薬", "羞恥", "拘束", "玩具"
]
EXCLUDE_WORDS = ["熟女", "五十路", "四十路", "六十路", "高齢", "ニューハーフ", "おばさん", "マダム"]

def generate_hinban(content_id):
    if not content_id:
        return ""
    s = content_id.lower()
    s = re.sub(r'^(h_\d+|h_|\d+)', '', s)
    match = re.match(r'^([a-z]+)(\d+)', s)
    if match:
        a = match.group(1).upper()
        n = match.group(2)
        c = n.lstrip('0') or '0'
        std = f"{a}-{n}"
        return f"{a}-{c} ({std})" if c != n else std
    return content_id.upper()

def normalize_manga_title(title):
    if not title:
        return ""
    t = re.sub(r'【.*?】', '', title)
    t = re.sub(r'\[.*?\]', '', t)
    t = re.sub(r'（.*?）', '', t)
    t = re.sub(r'\(.*?\)', '', t)
    t = re.sub(r'[\s　]+', '', t)
    t = re.sub(r'(第?\d+話|第?\d+巻|vol\.\d+|\#\d+|\d+$)', '', t, flags=re.IGNORECASE)
    return t.strip() or title

def load_posted_cache():
    cache_ids = set()
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            cache_ids = set(line.strip() for line in f if line.strip())
    
    existing_titles = set()
    if os.path.exists(POSTS_DIR):
        for f in os.listdir(POSTS_DIR):
            if f.endswith(".json"):
                try:
                    with open(os.path.join(POSTS_DIR, f), "r", encoding="utf-8") as fp:
                        data = json.load(fp)
                        norm = normalize_manga_title(data.get("title", ""))
                        if norm:
                            existing_titles.add(norm)
                        if data.get("id"):
                            cache_ids.add(data.get("id"))
                except:
                    pass
    return cache_ids, existing_titles

def save_to_cache(content_id):
    with open(CACHE_FILE, "a", encoding="utf-8") as f:
        f.write(f"{content_id}\n")

def save_manga_post(post_data):
    os.makedirs(POSTS_DIR, exist_ok=True)
    filename = os.path.join(POSTS_DIR, f"{post_data['id']}.json")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f"  [SAVED] {filename} -> {post_data['title'][:40]}")

def fetch_fanza_manga():
    url = "https://api.dmm.com/affiliate/v3/ItemList"
    all_items = []
    print(f"--- 📡 Fetching fresh manga directly from FANZA API ---")
    for keyword in SEARCH_KEYWORDS:
        for sort_type in ["rank", "date", "match"]:
            for offset_val in [1, 31, 61, 91, 121]:
                params = {
                    "api_id": API_ID,
                    "affiliate_id": API_AFFILIATE_ID,
                    "site": "FANZA",
                    "service": "ebook",
                    "floor": "comic",
                    "keyword": keyword,
                    "sort": sort_type,
                    "offset": offset_val,
                    "hits": 30,
                    "output": "json"
                }
                try:
                    r = requests.get(url, params=params, timeout=15)
                    if r.status_code == 200:
                        items = r.json().get("result", {}).get("items", [])
                        all_items.extend(items)
                except Exception as e:
                    pass
                time.sleep(0.12)
    random.shuffle(all_items)
    print(f"Total raw items fetched from FANZA API: {len(all_items)}")
    return all_items

def filter_items(items, posted_cache, existing_titles):
    valid = []
    seen_ids = set()
    seen_titles = set()
    for item in items:
        cid = item.get("content_id")
        if not cid or cid in posted_cache or cid in seen_ids:
            continue
        title = item.get("title", "")
        norm_title = normalize_manga_title(title)
        if not norm_title or norm_title in existing_titles or norm_title in seen_titles:
            continue
        genres = " ".join([g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])])
        if not any(w in title or w in genres for w in EXCLUDE_WORDS):
            seen_ids.add(cid)
            seen_titles.add(norm_title)
            valid.append(item)
    return valid

def generate_pure_fanza_article(item):
    """
    FANZA APIから取得した純粋な商品情報（公式あらすじ、作者、ジャンル、レーベル等）を元に、
    AI臭さ・適当な嘘のない完全オリジナルな詳細SEOレビュー記事HTMLを構築
    """
    cid = item.get("content_id", "")
    title = item.get("title", "")
    comment = item.get("comment", "")
    genres = [g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])]
    authors = [a.get("name", "") for a in item.get("iteminfo", {}).get("author", [])]
    publisher = (item.get("iteminfo", {}).get("label", [{}]) or [{}])[0].get("name", "")
    
    item_adapter = {
        "id": cid,
        "title": title,
        "hinban": generate_hinban(cid),
        "author": authors,
        "genres": genres,
        "publisher": publisher,
        "comment": comment
    }
    return generate_deep_custom_review(item_adapter)

def main():
    posted_cache, existing_titles = load_posted_cache()
    print(f"Existing cache IDs: {len(posted_cache)}, Unique Titles: {len(existing_titles)}")
    
    all_items = fetch_fanza_manga()
    valid_items = filter_items(all_items, posted_cache, existing_titles)
    print(f"\n--- Found {len(valid_items)} completely new & unique manga candidates ---")
    
    added_count = 0
    for item in valid_items:
        if added_count >= TARGET_NEW_POSTS:
            break
            
        cid = item.get("content_id")
        title = item.get("title", "")
        affiliate_url = item.get("affiliateURL", "")
        if "af_id=" in affiliate_url:
            affiliate_url = re.sub(r"af_id=[^&]+", f"af_id={LINK_AFFILIATE_ID}", affiliate_url)
            
        imgs = item.get("imageURL", {})
        image_url = imgs.get("large") or imgs.get("list") or ""
        tachiyomi_url = item.get("tachiyomi", {}).get("affiliateURL", "")
        sample_images = item.get("sampleImageURL", {}).get("sample_l", {}).get("image", []) or []
        genres = [g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])]
        authors = [a.get("name", "") for a in item.get("iteminfo", {}).get("author", [])]
        publisher = (item.get("iteminfo", {}).get("label", [{}]) or [{}])[0].get("name", "")
        date_str = item.get("date", time.strftime("%Y-%m-%d %H:%M:%S"))
        
        # 確実なSEO記事の生成
        review_html = generate_pure_fanza_article(item)
        
        post_data = {
            "id": cid,
            "type": "manga",
            "hinban": generate_hinban(cid),
            "title": title,
            "review": review_html,
            "image": image_url,
            "sample_images": sample_images,
            "affiliate_url": affiliate_url,
            "tachiyomi_url": tachiyomi_url,
            "genres": genres,
            "author": authors,
            "publisher": publisher,
            "date": date_str,
            "labels": ["漫画", "アダルト漫画", "2026年最新", "おすすめ"]
        }
        
        save_manga_post(post_data)
        save_to_cache(cid)
        existing_titles.add(normalize_manga_title(title))
        added_count += 1
        
    print(f"\n🎉 Successfully added {added_count} brand-new manga posts from direct FANZA API!")

if __name__ == "__main__":
    main()
