import os
import json
import requests

KEY = "a8f6d2b3c7e491f8a2c5b7d9e0f3g1h4"
HOST = "haitoku.pages.dev"
BASE_URL = f"https://{HOST}"

URL_SET = {
    f"{BASE_URL}/",
    f"{BASE_URL}/ranking",
    f"{BASE_URL}/archives",
    f"{BASE_URL}/manga"
}

POSTS_DIR = "src/data/posts"
MANGA_DIR = "src/data/manga"

import datetime

NOW_DT = datetime.datetime.now()

SLUGS_DATA = {}
if os.path.exists("src/lib/slugs.json"):
    with open("src/lib/slugs.json", "r", encoding="utf-8") as file:
        SLUGS_DATA = json.load(file)
ACTRESS_SLUGS = SLUGS_DATA.get("actresses", {})
GENRE_SLUGS = SLUGS_DATA.get("genres", {})

# Collect Post URLs and Taxonomy tags
if os.path.exists(POSTS_DIR):
    for f in os.listdir(POSTS_DIR):
        if f.endswith('.json'):
            try:
                with open(os.path.join(POSTS_DIR, f), 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    d_str = data.get('date', '')
                    if d_str:
                        d_clean = d_str.split('.')[0]
                        d_obj = datetime.datetime.strptime(d_clean, '%Y-%m-%d %H:%M:%S')
                        if d_obj > NOW_DT:
                            continue # 未発売の未来記事は除外
                    if data.get('id'):
                        URL_SET.add(f"{BASE_URL}/posts/{data['id']}")
                    for act in data.get('actresses', []):
                        if act:
                            act_slug = ACTRESS_SLUGS.get(act, requests.utils.quote(act))
                            URL_SET.add(f"{BASE_URL}/actress/{act_slug}")
                    for g in data.get('genres', []):
                        if g:
                            g_slug = GENRE_SLUGS.get(g, requests.utils.quote(g))
                            URL_SET.add(f"{BASE_URL}/genre/{g_slug}")
                    if data.get('maker'):
                        URL_SET.add(f"{BASE_URL}/maker/{requests.utils.quote(data['maker'])}")
            except Exception as e:
                pass

# Collect Manga URLs
if os.path.exists(MANGA_DIR):
    for f in os.listdir(MANGA_DIR):
        if f.endswith('.json'):
            try:
                with open(os.path.join(MANGA_DIR, f), 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    if data.get('id'):
                        URL_SET.add(f"{BASE_URL}/manga/{data['id']}")
            except Exception as e:
                pass

URL_LIST = list(URL_SET)
print(f"Total target URLs collected: {len(URL_LIST)}")

# IndexNow endpoints (Bing, Yandex, IndexNow master endpoint)
INDEXNOW_ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://yandex.com/indexnow"
]

payload = {
    "host": HOST,
    "key": KEY,
    "keyLocation": f"{BASE_URL}/{KEY}.txt",
    "urlList": URL_LIST
}

print("\n--- Sending IndexNow Push Signals ---")
for endpoint in INDEXNOW_ENDPOINTS:
    print(f"Submitting to {endpoint}...")
    try:
        res = requests.post(endpoint, json=payload, timeout=30)
        print(f"[{endpoint}] Status: {res.status_code}")
        if res.status_code in [200, 202]:
            print(f" Successfully pushed to {endpoint}")
        else:
            print(f" Response: {res.text}")
    except Exception as e:
        print(f" Failed to connect to {endpoint}: {e}")

# Search Engine Sitemap Pings
print("\n--- Sending Sitemap Ping Crawling Signals ---")
sitemap_url = f"{BASE_URL}/sitemap.xml"
ping_targets = [
    ("Google", f"https://www.google.com/ping?sitemap={sitemap_url}"),
    ("Bing / Yahoo / Copilot", f"https://www.bing.com/ping?sitemap={sitemap_url}")
]

for engine, ping_url in ping_targets:
    try:
        res = requests.get(ping_url, timeout=15)
        print(f"Pinged {engine} ({ping_url}) -> Status: {res.status_code}")
    except Exception as e:
        print(f"Failed to ping {engine}: {e}")

print("\nAll indexing signals dispatched successfully!")
