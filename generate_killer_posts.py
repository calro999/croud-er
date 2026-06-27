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
    # SEOを極限まで意識し、今すぐアクセスが増える強烈なバズワードやトレンドワードを狙う
    keywords = ["2026年最新", "独占配信", "話題沸騰", "絶対抜ける", "SNSで話題", "超人気", "ベストセラー", "殿堂入り"]
    
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

    prompt = f"""以下の大人向け映像作品の情報を基にして、指定のSEO超特化・最強執筆ルールに従ってブログ記事のHTML本文（レビュー文）を生成してください。

【作品名】: {safe_title}
【あらすじ】: {safe_comment}
【ジャンル】: {safe_genres}

【SEO超特化・最強執筆ルール】
1. ペルソナ: ネットで絶大な支持を集める「大人の背徳ドラマ専門」のカリスマレビュアー。
2. 検索意図の充足と見出し構成: 読者が検索しそうな関連キーワード（「感想」「レビュー」「評判」「見どころ」など）を意識し、必ず <h2> や <h3> タグを使って論理的で魅力的な見出し階層を作ってください。
3. キャッチーな導入: 冒頭で「これは今すぐ見るべき！」「SNSで話題沸騰のヤバい作品」といった強烈なフックを入れて読者の離脱を防いでください。
4. 推しポイントの熱弁: マニア目線で「ここがスゴイ！」というポイントを激熱で語り、共起語（関連ワード）を自然に散りばめてSEO評価を高めてください。
5. 表現の防壁: 直接的な性描写（ポルノワード）を完全に避け、官能的で妄想を刺激する文学的表現に変換してください。
6. 出力フォーマット: HTML（<h2>, <h3>, <p>, <strong>, <ul>, <li>）のみを出力し、マークダウンのコードブロック（```html等）は一切使用しないでください。

それでは、SEO最強のHTML本文のみを出力してください。
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
            
    return """<h2>【殿堂入り確実】この展開はヤバすぎる…！今すぐ見るべき超話題作</h2>
<p>日常のすぐ裏側に潜むスリリングな関係を描いた、本能を揺さぶる傑作が登場しました。</p>
<h3>マニアも納得の圧倒的なクオリティ</h3>
<p><strong>「日常が静かに、しかし劇的に崩壊していく感覚」</strong>をじっくりと味わえる本作。俳優陣の演技力はもちろん、シチュエーションの作り込みが段違いです。SNSや各レビューサイトでも「これは絶対に抜ける」「一度見たら忘れられない」と絶賛の嵐となっています。</p>
<h3>絶対に一度は見ておくべき究極のシチュエーション</h3>
<p>単なる映像作品の枠を超え、あなたの妄想を極限まで刺激すること間違いなし。まだ見ていない方は、ぜひこの機会に究極のシチュエーションをお楽しみください。</p>"""

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
            "title": f"【2026年最新・超話題作】 {title}",
            "review": review_html,
            "image": image_url,
            "sample_images": sample_images,
            "affiliate_url": affiliate_url,
            "genres": [g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])],
            "actresses": [a.get("name", "") for a in item.get("iteminfo", {}).get("actress", [])],
            "maker": item.get("iteminfo", {}).get("maker", [{}])[0].get("name", ""),
            "date": item.get("date", time.strftime("%Y-%m-%d %H:%M:%S")),
            "labels": ["超話題作", "2026年最新", "最強コンテンツ", "絶対抜ける", "SNSで話題", "人気"]
        }
        
        save_individual_post(post_data)
        save_to_cache(content_id)
        
        generated_count += 1
        time.sleep(2) # API/LLMへの負荷軽減
        
    print(f"--- Generated {generated_count} killer posts ---")

if __name__ == "__main__":
    main()
