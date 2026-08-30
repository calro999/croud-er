import os
import re
import json
import time
import requests

API_ID = "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = "onchan555-999"
LINK_AFFILIATE_ID = "onchan555-003"
ACTRESS_DATA_DIR = "src/data/actresses"
POSTS_DIR = "src/data/posts"

os.makedirs(ACTRESS_DATA_DIR, exist_ok=True)

def fetch_actress_profile(name):
    """FANZA ActressSearch APIから女優の公式プロフィールを取得"""
    url = "https://api.dmm.com/affiliate/v3/ActressSearch"
    params = {
        "api_id": API_ID,
        "affiliate_id": API_AFFILIATE_ID,
        "keyword": name,
        "output": "json"
    }
    try:
        res = requests.get(url, params=params, timeout=15)
        if res.status_code == 200:
            data = res.json()
            actresses = data.get("result", {}).get("actress", [])
            for act in actresses:
                if act.get("name") == name or name in act.get("name", ""):
                    return act
            if actresses:
                return actresses[0]
    except Exception as e:
        print(f"Error fetching actress profile for {name}: {e}")
    return None

def fetch_actress_works(actress_id, actress_name):
    """FANZA ItemList APIから女優の出演全作品・監督名・価格情報を取得"""
    url = "https://api.dmm.com/affiliate/v3/ItemList"
    params = {
        "api_id": API_ID,
        "affiliate_id": API_AFFILIATE_ID,
        "site": "FANZA",
        "service": "digital",
        "floor": "videoa",
        "article": "actress",
        "article_id": actress_id,
        "sort": "rank",
        "hits": 30,
        "output": "json"
    }
    try:
        res = requests.get(url, params=params, timeout=15)
        if res.status_code == 200:
            data = res.json()
            items = data.get("result", {}).get("items", [])
            return items
    except Exception as e:
        print(f"Error fetching works for {actress_name} (ID: {actress_id}): {e}")
    
    # 女優IDでヒットしない場合はキーワード検索でフォールバック
    try:
        params = {
            "api_id": API_ID,
            "affiliate_id": API_AFFILIATE_ID,
            "site": "FANZA",
            "service": "digital",
            "floor": "videoa",
            "keyword": actress_name,
            "sort": "rank",
            "hits": 30,
            "output": "json"
        }
        res = requests.get(url, params=params, timeout=15)
        if res.status_code == 200:
            data = res.json()
            return data.get("result", {}).get("items", [])
    except Exception as e:
        print(f"Fallback keyword search error for {actress_name}: {e}")
    return []

def extract_directors_and_works(items):
    """作品群から監督名・作品リストを構造化抽出"""
    works_list = []
    director_counts = {}

    for item in items:
        content_id = item.get("content_id")
        title = item.get("title", "")
        date = item.get("date", "")
        
        # アフィリエイトURL置換
        affiliate_url = item.get("affiliateURL", "")
        if "af_id=" in affiliate_url:
            affiliate_url = re.sub(r"af_id=[^&]+", f"af_id={LINK_AFFILIATE_ID}", affiliate_url)
            
        images = item.get("imageURL", {})
        image_url = images.get("large") or images.get("list") or ""
        
        # 監督名
        directors = [d.get("name") for d in item.get("iteminfo", {}).get("director", []) if d.get("name")]
        for d in directors:
            director_counts[d] = director_counts.get(d, 0) + 1
            
        # メーカー名
        makers = [m.get("name") for m in item.get("iteminfo", {}).get("maker", []) if m.get("name")]
        maker = makers[0] if makers else ""
        
        # ジャンル
        genres = [g.get("name") for g in item.get("iteminfo", {}).get("genre", []) if g.get("name")]
        
        # 価格情報
        prices = item.get("prices", {})
        price_str = prices.get("price", "300~")

        works_list.append({
            "id": content_id,
            "title": title,
            "date": date,
            "image": image_url,
            "affiliate_url": affiliate_url,
            "directors": directors,
            "maker": maker,
            "genres": genres,
            "price": price_str
        })

    # 監督ランキング順
    top_directors = sorted(director_counts.items(), key=lambda x: x[1], reverse=True)
    return works_list, [d[0] for d in top_directors]

def generate_actress_wiki_data():
    """全記事から女優一覧を抽出し、FANZA APIから最新公式データを取得・保存"""
    print("=== Starting FANZA Actress Wiki Data Generation ===")
    
    actress_set = set()
    if os.path.exists(POSTS_DIR):
        for f in os.listdir(POSTS_DIR):
            if f.endswith(".json"):
                try:
                    with open(os.path.join(POSTS_DIR, f), "r", encoding="utf-8") as fp:
                        data = json.load(fp)
                        for a in data.get("actresses", []):
                            if a and len(a.strip()) > 0:
                                actress_set.add(a.strip())
                except:
                    pass

    print(f"Found {len(actress_set)} unique actresses in existing posts.")

    for actress_name in sorted(actress_set):
        target_path = os.path.join(ACTRESS_DATA_DIR, f"{actress_name}.json")
        print(f"\n[Processing Actress] {actress_name}")
        
        # FANZA ActressSearch API
        profile = fetch_actress_profile(actress_name)
        actress_id = profile.get("id") if profile else None
        
        # FANZA ItemList API
        items = fetch_actress_works(actress_id, actress_name)
        works, directors = extract_directors_and_works(items)
        
        # 公式画像URL（大・小）
        image_large = ""
        image_small = ""
        if profile and profile.get("imageURL"):
            image_large = profile["imageURL"].get("large", "")
            image_small = profile["imageURL"].get("small", "")
            
        # アフィリエイトURL
        actress_affiliate_url = f"https://al.fanza.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fsearch%2F-%2F%3Fsearchstr%3D{requests.utils.quote(actress_name)}%2F&af_id={LINK_AFFILIATE_ID}"

        wiki_data = {
            "name": actress_name,
            "ruby": profile.get("ruby", "") if profile else "",
            "fanza_id": actress_id,
            "bust": profile.get("bust") if profile else None,
            "cup": profile.get("cup") if profile else None,
            "waist": profile.get("waist") if profile else None,
            "hip": profile.get("hip") if profile else None,
            "height": profile.get("height") if profile else None,
            "birthday": profile.get("birthday") if profile else None,
            "blood_type": profile.get("blood_type") if profile else None,
            "hobby": profile.get("hobby") if profile else None,
            "prefectures": profile.get("prefectures") if profile else None,
            "image_large": image_large,
            "image_small": image_small,
            "affiliate_url": actress_affiliate_url,
            "directors": directors,
            "works_count": len(works),
            "works": works,
            "updated_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        with open(target_path, "w", encoding="utf-8") as out_f:
            json.dump(wiki_data, out_f, ensure_ascii=False, indent=2)
            
        print(f"Saved: {target_path} (Profile: {'Found' if profile else 'Not Found'}, Works: {len(works)}, Directors: {len(directors)})")
        time.sleep(0.3)

    print("\n=== Completed FANZA Actress Wiki Data Generation ===")

if __name__ == "__main__":
    generate_actress_wiki_data()
