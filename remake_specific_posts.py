import os
import re
import time
import json
import requests

TARGET_IDS = [
    "cawd00998",
    "1start00153",
    "nsfs00498",
    "mmgo00019",
]

POSTS_DIR = "src/data/posts"
API_ID = "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = "onchan555-999"
LINK_AFFILIATE_ID = "onchan555-003"

def generate_hinban(content_id):
    if not content_id:
        return ""
    s = content_id.lower()
    s = re.sub(r'^(h_\d+|h_|\d+)', '', s)
    match = re.match(r'^([a-z]+)(\d+)', s)
    if match:
        alphabetic = match.group(1).upper()
        numeric = match.group(2)
        clean_num = numeric.lstrip('0')
        if not clean_num:
            clean_num = '0'
        formatted_standard = f"{alphabetic}-{numeric}"
        if clean_num != numeric:
            formatted_clean = f"{alphabetic}-{clean_num}"
            return f"{formatted_clean} ({formatted_standard})"
        return formatted_standard
    return content_id.upper()

def save_individual_post(post_data):
    os.makedirs(POSTS_DIR, exist_ok=True)
    filename = os.path.join(POSTS_DIR, f"{post_data['id']}.json")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f"Saved: {filename}")

def fetch_item_by_id(content_id):
    url = "https://api.dmm.com/affiliate/v3/ItemList"
    params = {
        "api_id": API_ID,
        "affiliate_id": API_AFFILIATE_ID,
        "site": "FANZA",
        "service": "digital",
        "floor": "videoa",
        "cid": content_id,
        "hits": 1,
        "output": "json"
    }
    print(f"Fetching: '{content_id}'")
    try:
        response = requests.get(url, params=params, timeout=15)
        if response.status_code == 200:
            data = response.json()
            items = data.get("result", {}).get("items", [])
            if items:
                return items[0]
    except Exception as e:
        print(f"Error fetching {content_id}: {e}")
    return None

def generate_seo_article(item, content_id):
    title = item.get("title", content_id)
    comment = item.get("comment", "")
    genres = ", ".join([g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])])
    actresses_list = [a.get("name", "") for a in item.get("iteminfo", {}).get("actress", [])]
    actresses = "、".join(actresses_list)

    prompt = f"""以下のアダルト映像作品の情報を元に、SEO完全特化の高品質ブログ記事HTML本文を生成してください。

【品番】: {content_id}
【作品名】: {title}
【出演者】: {actresses if actresses else "非公開"}
【あらすじ】: {comment}
【ジャンル】: {genres}

【SEO超特化・最強執筆ルール】
1. h2を3つ以上、h3を4つ以上、h4を2つ以上含める
2. 2500文字以上
3. 「{content_id}」「レビュー」「感想」「評価」「見どころ」「ネタバレ」を自然に含める
4. 必須セクション: 作品概要・見どころ・キャスト分析・シーン別レビュー（ネタバレあり）・評価表(tableタグ)・総評
5. 直接的な性描写ワードを避け、官能的で文学的な表現に変換
6. HTMLのみ出力。マークダウン禁止。

SEO最強のHTML本文のみを出力してください。"""

    system_message = "あなたはネットで絶大な支持を集めるカリスマレビュアーです。品番検索でこの記事に辿り着いた読者の検索意図に完全に応えるSEO特化記事をHTML形式で作成します。"
    models = ["openai", "openai-fast", "mistral"]

    for attempt in range(3):
        for model in models:
            try:
                print(f"  Generating with {model}...")
                response = requests.post(
                    "https://text.pollinations.ai/",
                    json={
                        "messages": [
                            {"role": "system", "content": system_message},
                            {"role": "user", "content": prompt}
                        ],
                        "model": model
                    },
                    timeout=60
                )
                if response.status_code == 200 and len(response.text.strip()) > 500:
                    result = response.text.strip()
                    if "```html" in result:
                        result = result.split("```html", 1)[1]
                    if "```" in result:
                        result = result.split("```")[0]
                    return result.strip()
            except Exception as e:
                print(f"  Error with {model}: {e}")
            time.sleep(2)
    return f"<h2>{title}</h2><p>{comment}</p>"

def main():
    print(f"--- 品番指定リメイク: {len(TARGET_IDS)}件 ---")
    for i, content_id in enumerate(TARGET_IDS):
        print(f"\n[{i+1}/{len(TARGET_IDS)}] {content_id}")
        item = fetch_item_by_id(content_id)
        if not item:
            print(f"  Not found: {content_id}")
            continue

        title = item.get("title", content_id)
        affiliate_url = item.get("affiliateURL", "")
        if "af_id=" in affiliate_url:
            affiliate_url = re.sub(r"af_id=[^&]+", f"af_id={LINK_AFFILIATE_ID}", affiliate_url)

        image_url = ""
        images = item.get("imageURL", {})
        if images:
            image_url = images.get("large") or images.get("list") or ""
        
        movie = item.get("sampleMovieURL", {})
        sample_movie_url = movie.get("size_720_480") or movie.get("size_644_414") or movie.get("size_560_360") or movie.get("size_476_306") or ""
        if sample_movie_url and "onchan555-999" in sample_movie_url:
            sample_movie_url = sample_movie_url.replace("onchan555-999", LINK_AFFILIATE_ID)


        sample_images = []
        sample_img_obj = item.get("sampleImageURL", {}).get("sample_l", {})
        if sample_img_obj:
            sample_images = sample_img_obj.get("image", [])

        print(f"  Title: {title[:60]}...")
        review_html = generate_seo_article(item, content_id)

        post_data = {
            "id": content_id,
            "hinban": generate_hinban(content_id),
            "title": title,
            "review": review_html,
            "image": image_url,
            "sample_movie_url": sample_movie_url,
            "sample_images": sample_images,
            "affiliate_url": affiliate_url,
            "genres": [g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])],
            "actresses": [a.get("name", "") for a in item.get("iteminfo", {}).get("actress", [])],
            "maker": (item.get("iteminfo", {}).get("maker", [{}]) or [{}])[0].get("name", ""),
            "date": item.get("date", time.strftime("%Y-%m-%d %H:%M:%S")),
            "labels": ["超話題作", "2026年最新", "人気", "ネタバレ"]
        }

        save_individual_post(post_data)
        time.sleep(3)

    print(f"\n--- 完了 ---")

if __name__ == "__main__":
    main()
