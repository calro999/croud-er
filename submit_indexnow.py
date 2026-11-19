# -*- coding: utf-8 -*-
import os
import json
import requests
import datetime

KEY = "a8f6d2b3c7e491f8a2c5b7d9e0f3g1h4"
HOST = "haitoku.pages.dev"
BASE_URL = f"https://{HOST}"

URL_SET = {
    f"{BASE_URL}/",
    f"{BASE_URL}/fanza-tv-plus",
    f"{BASE_URL}/fanza-device-guide",
    f"{BASE_URL}/features",
    f"{BASE_URL}/ranking",
    f"{BASE_URL}/archives",
    f"{BASE_URL}/manga",
    f"{BASE_URL}/llms.txt",
    f"{BASE_URL}/llms-full.txt"
}

POSTS_DIR = "src/data/posts"
MANGA_DIR = "src/data/manga"

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
            except Exception:
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
            except Exception:
                pass

URL_LIST = list(URL_SET)
print(f"Total target URLs collected: {len(URL_LIST)}")

# IndexNow endpoints:
# - Bing (also powers Yahoo! / DuckDuckGo search index)
# - IndexNow master API (shared with DuckDuckGo, Seznam, Naver, etc.)
# - Yandex
INDEXNOW_ENDPOINTS = [
    ("IndexNow Master (DuckDuckGo / Copilot / Global AI)", "https://api.indexnow.org/indexnow"),
    ("Bing IndexNow (DuckDuckGo Backend & Microsoft Copilot)", "https://www.bing.com/indexnow")
]

print("\n--- Sending IndexNow Push Signals to DuckDuckGo & Global Search Crawlers ---")
CHUNK_SIZE = 10000
for i in range(0, len(URL_LIST), CHUNK_SIZE):
    chunk = URL_LIST[i:i + CHUNK_SIZE]
    print(f"Submitting chunk {i // CHUNK_SIZE + 1} ({len(chunk)} URLs)...")
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": f"{BASE_URL}/{KEY}.txt",
        "urlList": chunk
    }
    for label, endpoint in INDEXNOW_ENDPOINTS:
        try:
            res = requests.post(endpoint, json=payload, timeout=30)
            print(f"[{label}] Status: {res.status_code}")
            if res.status_code in [200, 202]:
                print(f" -> Successfully received and queued for immediate indexing!")
            else:
                print(f" -> Response: {res.text}")
        except Exception as e:
            print(f" -> Failed to connect to {endpoint}: {e}")

# Push LLM & AI Knowledge base signals
print("\n--- Pinging AI Search Engines & LLM Web Indexers ---")
sitemap_url = f"{BASE_URL}/sitemap.xml"
llms_url = f"{BASE_URL}/llms.txt"

ai_ping_targets = [
    ("Bing / DuckDuckGo / Copilot Engine", f"https://www.bing.com/ping?sitemap={sitemap_url}"),
    ("Google Search & Gemini Crawler Ping", f"https://www.google.com/ping?sitemap={sitemap_url}")
]

for engine, ping_url in ai_ping_targets:
    try:
        res = requests.get(ping_url, timeout=15)
        print(f"Pinged {engine} -> Status: {res.status_code}")
    except Exception as e:
        print(f"Failed to ping {engine}: {e}")

print("\nAll IndexNow and AI crawler indexing signals dispatched successfully!")
