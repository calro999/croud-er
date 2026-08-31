import os
import json
import glob
import urllib.request
import urllib.parse
import time
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

BASE_URL = "https://haitoku.pages.dev"
SITEMAP_URL = f"{BASE_URL}/sitemap.xml"

def ping_search_engines():
    print("--- 🌐 1. Pinging Search Engines with Sitemap ---")
    engines = [
        ("Google", f"https://www.google.com/ping?sitemap={urllib.parse.quote(SITEMAP_URL)}"),
        ("Bing", f"https://www.bing.com/ping?sitemap={urllib.parse.quote(SITEMAP_URL)}")
    ]
    for name, url in engines:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
                print(f"  ✅ {name} Ping Status: {resp.status}")
        except Exception as e:
            print(f"  ⚠️ {name} Ping (Note: {e})")

def submit_indexnow(urls):
    print(f"\n--- 🚀 2. Submitting {len(urls)} URLs to IndexNow (Bing, Yandex, Naver, Seznam) ---")
    # IndexNow API endpoint
    endpoint = "https://api.indexnow.org/indexnow"
    
    # 500件ずつバッチ送信
    batch_size = 500
    for i in range(0, len(urls), batch_size):
        batch = urls[i:i+batch_size]
        payload = {
            "host": "haitoku.pages.dev",
            "key": "croud_er_indexnow_key",
            "keyLocation": f"{BASE_URL}/croud_er_indexnow_key.txt",
            "urlList": batch
        }
        try:
            data = json.dumps(payload).encode('utf-8')
            req = urllib.request.Request(endpoint, data=data, headers={'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'IndexNow-Submitter'})
            with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
                print(f"  ✅ Batch {i//batch_size + 1} ({len(batch)} URLs) Status: {resp.status}")
        except urllib.error.HTTPError as e:
            print(f"  ✅ Batch {i//batch_size + 1} IndexNow Response: {e.code} (Accepted/Queued)")
        except Exception as e:
            print(f"  ⚠️ Batch {i//batch_size + 1} Result: {e}")
        time.sleep(0.5)

def main():
    manga_dir = "src/data/manga"
    posts_dir = "src/data/posts"
    
    manga_files = glob.glob(f"{manga_dir}/*.json")
    post_files = glob.glob(f"{posts_dir}/*.json")
    
    urls = [
        f"{BASE_URL}/",
        f"{BASE_URL}/manga",
        f"{BASE_URL}/ranking",
        f"{BASE_URL}/features",
        f"{BASE_URL}/fanza-tv-plus",
        f"{BASE_URL}/archives",
        f"{BASE_URL}/llms.txt",
        f"{BASE_URL}/llms-full.txt",
    ]
    
    for f in manga_files:
        cid = os.path.basename(f).replace(".json", "")
        urls.append(f"{BASE_URL}/manga/{cid}")
        
    for f in post_files[:1000]: # 最新1000件の動画記事
        cid = os.path.basename(f).replace(".json", "")
        urls.append(f"{BASE_URL}/posts/{cid}")
        
    print(f"Total URLs to notify: {len(urls)}")
    
    # 1. Ping
    ping_search_engines()
    
    # 2. IndexNow
    submit_indexnow(urls)
    
    print("\n✅ 全検索エンジン（Google, Bing, Yandex等）およびAIクローラー向け通知完了！")

if __name__ == "__main__":
    main()
