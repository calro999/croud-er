
def call_multi_llm_api(prompt, system_content="You are a helpful assistant."):
    groq_key = os.environ.get("GROQ_API_KEY")
    if groq_key:
        for model_name in ["llama-3.3-70b-versatile", "llama3-70b-8192"]:
            try:
                headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
                payload = {
                    "model": model_name,
                    "messages": [{"role": "system", "content": system_content}, {"role": "user", "content": prompt}],
                    "temperature": 0.7
                }
                res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload, timeout=30)
                if res.status_code == 200:
                    text = res.json()["choices"][0]["message"]["content"].strip()
                    if len(text) > 100:
                        return text
            except Exception as e:
                print(f"Groq API error ({model_name}): {e}")

    gemini_key = os.environ.get("GEMINI_API_KEY")
    if gemini_key:
        gemini_models = [
            "gemini-2.5-flash",
            "gemini-2.0-flash",
            "gemini-2.5-flash-lite",
            "gemini-2.0-flash-lite",
            "gemini-2.5-pro",
            "gemini-3-flash",
            "gemini-3.1-pro",
            "gemini-3.1-flash-lite",
            "gemini-3.5-flash-lite",
            "gemini-3.5-flash",
            "gemini-3.6-flash",
            "gemini-3.7-flash"
        ]
        random.shuffle(gemini_models)
        for model_name in gemini_models:
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={gemini_key}"
                payload = {
                    "contents": [{"parts": [{"text": f"{system_content}\n\n{prompt}"}]}],
                    "generationConfig": {"temperature": 0.7, "maxOutputTokens": 2048}
                }
                res = requests.post(url, json=payload, timeout=30)
                if res.status_code == 200:
                    candidate = res.json().get("candidates", [{}])[0]
                    parts = candidate.get("content", {}).get("parts", [])
                    text = "".join(p.get("text", "") for p in parts if p.get("text")).strip()
                    if len(text) > 100:
                        return text
            except Exception as e:
                print(f"Gemini API error ({model_name}): {e}")

    return None

import os
import random
import re
import time
import json
import requests

SITE = "blogger-er"
CACHE_FILE = "manga_cache.txt"
POSTS_DIR = "src/data/manga"
API_ID = "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = "onchan555-999"
LINK_AFFILIATE_ID = "onchan555-003"
TARGET_POST_COUNT = 5

# blogger-er: レズ・百合・NTR・人妻系漫画
SEARCH_KEYWORDS = ["レズ", "百合", "NTR", "人妻", "寝取られ", "女性同士"]
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
    
    # 既存の全漫画JSONファイルから正規化タイトルを収集（作品重複を永久に防止）
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
    print(f"Saved: {filename}")

def fetch_fanza_manga():
    url = "https://api.dmm.com/affiliate/v3/ItemList"
    all_items = []
    for keyword in SEARCH_KEYWORDS:
        for sort_type in ["rank", "date"]:
            params = {
                "api_id": API_ID,
                "affiliate_id": API_AFFILIATE_ID,
                "site": "FANZA",
                "service": "ebook",
                "floor": "comic",
                "keyword": keyword,
                "sort": sort_type,
                "offset": random.randint(1, 10),
                "hits": 20,
                "output": "json"
            }
            try:
                print(f"Fetching manga: '{keyword}', sort: '{sort_type}'")
                r = requests.get(url, params=params, timeout=15)
                if r.status_code == 200:
                    items = r.json().get("result", {}).get("items", [])
                    all_items.extend(items)
            except Exception as e:
                print(f"Error: {e}")
            time.sleep(0.5)
    random.shuffle(all_items)
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

from update_all_manga_articles import generate_custom_review

def generate_manga_article(item):
    title = item.get("title", "")
    comment = item.get("comment", "")
    genres = ", ".join([g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])])
    authors = "、".join([a.get("name", "") for a in item.get("iteminfo", {}).get("author", [])])
    cid = item.get("content_id", "")

    prompt = f"""以下のアダルト漫画の情報を元に、SEO完全特化の高品質ブログ記事HTML本文を生成してください。

【品番】: {cid}
【タイトル】: {title}
【作者】: {authors if authors else "不明"}
【あらすじ（公式）】: {comment}
【ジャンル】: {genres}

【SEO超特化ルール】
1. h2を3つ以上、h3を4つ以上含める
2. 2000文字以上
3. 「レビュー」「感想」「ネタバレなし」「あらすじ」「おすすめ漫画」を自然に含める
4. 必須セクション: 概要・設定紹介（ネタバレなし）/見どころ（箇条書き）/作者・画風の分析/こんな人におすすめ/評価表(table: ストーリー・エロ度・画力)
5. ネタバレは最小限にし「続きはFANZAで確認」へ誘導
6. HTMLのみ出力。マークダウン禁止。"""

    system_message = "あなたはアダルトコミック・同人漫画のレビュー専門ライターです。読者の購買意欲を掻き立てる熱量の高い記事をHTML形式で出力します。"
    res = call_multi_llm_api(prompt, system_message)
    if res:
        if "```html" in res:
            res = res.split("```html", 1)[1].split("```")[0]
        elif "```" in res:
            res = res.split("```", 1)[1].split("```")[0]
        res = res.strip()
        if len(res) > 300:
            return res

    # 独自高品質SEOエンジンによる完全生成フォールバック
    item_adapter = {
        "id": cid,
        "title": title,
        "hinban": generate_hinban(cid),
        "author": [a.get("name", "") for a in item.get("iteminfo", {}).get("author", [])],
        "genres": [g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])],
        "publisher": (item.get("iteminfo", {}).get("label", [{}]) or [{}])[0].get("name", "")
    }
    return generate_custom_review(item_adapter)

def main():
    print(f"--- Manga Generator ({SITE}) | Target: {TARGET_POST_COUNT} ---")
    posted_cache, existing_titles = load_posted_cache()
    all_items = fetch_fanza_manga()
    valid_items = filter_items(all_items, posted_cache, existing_titles)
    print(f"Found {len(valid_items)} valid manga candidates.")

    count = 0
    for item in valid_items:
        if count >= TARGET_POST_COUNT:
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

        print(f"[{count+1}/{TARGET_POST_COUNT}] {title[:60]}")
        review_html = generate_manga_article(item)

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
            "genres": [g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])],
            "author": [a.get("name", "") for a in item.get("iteminfo", {}).get("author", [])],
            "publisher": (item.get("iteminfo", {}).get("label", [{}]) or [{}])[0].get("name", ""),
            "date": item.get("date", time.strftime("%Y-%m-%d %H:%M:%S")),
            "labels": ["漫画", "アダルト漫画", "2026年最新", "おすすめ"]
        }

        save_manga_post(post_data)
        save_to_cache(cid)
        count += 1
        time.sleep(2)

    print(f"--- Generated {count} manga posts ---")

if __name__ == "__main__":
    main()
