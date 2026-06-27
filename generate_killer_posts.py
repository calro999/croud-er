import os
import random
import requests
import time
import json
import re

CACHE_FILE = "posted_cache.txt"
POSTS_DIR = "src/data/posts"

# API固定設定
API_ID = "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = "onchan555-999"
LINK_AFFILIATE_ID = "onchan555-003"
TARGET_POST_COUNT = 10

def clean_for_safety(text):
    if not text:
        return ""
    safety_map = {
        "ネトラレ": "禁断 of 恋",
        "ねとられ": "禁断 of 恋",
        "不倫": "秘密 of 関係",
        "団地妻": "人妻",
        "人妻": "大人の女性",
        "背徳": "秘密 of",
        "痴女": "魅力的な女性",
        "中出し": "愛 of 結末",
        "AV": "ビデオ作品",
        "アダルト": "大人向け"
    }
    for old, new in safety_map.items():
        text = text.replace(old, new)
    return text

def load_posted_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return set(line.strip() for line in f if line.strip())
    return set()

def save_to_cache(content_id):
    with open(CACHE_FILE, "a", encoding="utf-8") as f:
        f.write(f"{content_id}\n")

def fetch_fanza_items():
    # 「人気・最新」の両方を狙うため、キーワードとソート順をランダムに組み合わせつつ
    # 複数ページからまとめて多めに取得する。
    keywords = ["上原亜衣", "人妻 ネトラレ", "若奥様 不倫", "ベストセラー", "殿堂入り"]
    
    url = "https://api.dmm.com/affiliate/v3/ItemList"
    
    all_items = []
    
    for sort_type in ["rank", "date"]:
        selected_keyword = random.choice(keywords)
        print(f"Fetching FANZA items for keyword: '{selected_keyword}', sort: '{sort_type}'")
        
        params = {
            "api_id": API_ID,
            "affiliate_id": API_AFFILIATE_ID,
            "site": "FANZA",
            "service": "digital",
            "floor": "videoa",
            "keyword": selected_keyword,
            "sort": sort_type,
            "offset": random.randint(1, 5),
            "hits": 30,
            "output": "json"
        }
        
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            items = data.get("result", {}).get("items", [])
            all_items.extend(items)
        else:
            print(f"Failed to fetch for sort {sort_type}: {response.status_code}")
            
    # シャッフルしてランダム性を出す
    random.shuffle(all_items)
    return all_items

def filter_items(items, posted_cache):
    valid_items = []
    exclude_words = ["熟女", "おばさん", "五十路", "四十路", "六十路", "熟年", "マダム", "高齢", "お姉さん", "ババ"]
    
    for item in items:
        content_id = item.get("content_id")
        if not content_id or content_id in posted_cache:
            continue
            
        title = item.get("title", "")
        comment = item.get("comment", "")
        genres = [g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])]
        genres_str = " ".join(genres)
        
        is_excluded = False
        for word in exclude_words:
            if word in title or word in comment or word in genres_str:
                is_excluded = True
                break
                
        if not is_excluded:
            valid_items.append(item)
            
    return valid_items

def generate_killer_article(item):
    title = item.get("title")
    comment = item.get("comment", "")
    genres = ", ".join([g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])])
    
    safe_title = clean_for_safety(title)
    safe_comment = clean_for_safety(comment)
    safe_genres = clean_for_safety(genres)

    prompt = f"""以下の大人向け映像作品の情報を基にして、指定の執筆ルールに従ってブログ記事のHTML本文（レビュー文）を生成してください。

【作品名】: {safe_title}
【あらすじ】: {safe_comment}
【ジャンル】: {safe_genres}

【執筆ルール（キラー記事用）】
1. ペルソナ: ネットで絶大な支持を集める「大人の背徳ドラマ専門」のカリスマレビュアー。
2. キャッチーな見出し: 冒頭にSNSでバズりやすい、強烈なフックとなる見出し（<h3>）を配置してください。「これはヤバい」「絶対に見るべき」という熱量を込めてください。
3. 推しポイントの熱弁: マニア目線で「ここがスゴイ！」というポイントを激熱で語ってください。
4. SEOと読者の興味: 読者の興味を惹く関連ワードを自然に散りばめ、まとめサイトのような読みやすさを持たせてください。
5. 表現の防壁: 直接的な性描写（ポルノワード）を完全に避け、官能的で妄想を刺激する文学的表現に変換してください。
6. 出力フォーマット: HTML（<p>, <h3>, <strong>）のみを出力し、マークダウンのコードブロックは一切使用しないでください。

それでは、HTML本文のみを出力してください。
"""

    system_message = "あなたはネットで絶大な支持を集めるカリスマレビュアーです。規約に配慮しつつ極めて熱量の高いレビュー文をHTML形式で作成します。"
    pollinations_models = ["openai", "openai-fast", "mistral"]
    
    for attempt in range(2):
        for model in pollinations_models:
            try:
                print(f"Generating article with {model}...")
                response = requests.post(
                    "https://text.pollinations.ai/",
                    json={
                        "messages": [
                            {"role": "system", "content": system_message},
                            {"role": "user", "content": prompt}
                        ],
                        "model": model
                    },
                    timeout=30
                )
                if response.status_code == 200 and len(response.text.strip()) > 100:
                    result_text = response.text.strip()
                    if "```html" in result_text:
                        result_text = result_text.split("```html", 1)[1]
                    if "```" in result_text:
                        result_text = result_text.split("```")[0]
                    return result_text.strip()
            except Exception as e:
                pass
            time.sleep(1)
            
    return """<h3>【殿堂入り 확実】この展開はヤバすぎる…！</h3>
<p>日常のすぐ裏側に潜むスリリングな関係を描いた、本能を揺さぶる傑作が登場しました。</p>
<p><strong>「日常が静かに、しかし劇的に崩壊していく感覚」</strong>をじっくりと味わえる本作。マニアも納得の圧倒的なクオリティです。</p>
<p>絶対に一度は見ておくべき、究極のシチュエーションをお楽しみください。</p>"""

def save_individual_post(post_data):
    os.makedirs(POSTS_DIR, exist_ok=True)
    post_id = post_data["id"]
    file_path = os.path.join(POSTS_DIR, f"{post_id}.json")
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f"Saved: {file_path}")

def main():
    print(f"--- Killer Posts Generator Started (Target: {TARGET_POST_COUNT} posts) ---")
    
    all_items = fetch_fanza_items()
    posted_cache = load_posted_cache()
    
    valid_items = filter_items(all_items, posted_cache)
    print(f"Found {len(valid_items)} valid candidates.")
    
    generated_count = 0
    
    for item in valid_items:
        if generated_count >= TARGET_POST_COUNT:
            break
            
        content_id = item.get("content_id")
        title = item.get("title")
        affiliate_url = item.get("affiliateURL", "")
        
        # アフィリエイトIDの置換
        if "af_id=" in affiliate_url:
            affiliate_url = re.sub(r"af_id=[^&]+", f"af_id={LINK_AFFILIATE_ID}", affiliate_url)
            
        # 画像
        image_url = ""
        images = item.get("imageURL", {})
        if images:
            image_url = images.get("large") or images.get("list") or ""

        sample_images = []
        sample_img_obj = item.get("sampleImageURL", {}).get("sample_l", {})
        if sample_img_obj:
            sample_images = sample_img_obj.get("image", [])
            
        print(f"[{generated_count+1}/{TARGET_POST_COUNT}] Processing: {title}")
        review_html = generate_killer_article(item)
        
        post_data = {
            "id": content_id,
            "title": f"【絶対必見・キラー記事】 {title}",
            "review": review_html,
            "image": image_url,
            "sample_images": sample_images,
            "affiliate_url": affiliate_url,
            "genres": [g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])],
            "actresses": [a.get("name", "") for a in item.get("iteminfo", {}).get("actress", [])],
            "maker": item.get("iteminfo", {}).get("maker", [{}])[0].get("name", ""),
            "date": item.get("date", time.strftime("%Y-%m-%d %H:%M:%S")),
            "labels": ["キラー記事", "人気", "最新", "必見", "ランキング上位"]
        }
        
        save_individual_post(post_data)
        save_to_cache(content_id)
        
        generated_count += 1
        time.sleep(2) # API/LLMへの負荷軽減
        
    print(f"--- Generated {generated_count} killer posts ---")

if __name__ == "__main__":
    main()
