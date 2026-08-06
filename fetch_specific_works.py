def generate_article_with_llm_text(prompt, system_message):
    import requests, os
    
    # 1. Gemini API (最優先)
    gemini_key = os.environ.get("GEMINI_API_KEY")
    if gemini_key:
        for model_name in ["gemini-2.0-flash", "gemini-2.5-flash", "gemini-1.5-flash"]:
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={gemini_key}"
                payload = {
                    "contents": [{"parts": [{"text": f"{system_message}\n\n{prompt}"}]}],
                    "generationConfig": {"temperature": 0.8, "maxOutputTokens": 2048}
                }
                if "2.5" in model_name:
                    payload["generationConfig"]["thinkingConfig"] = {"thinkingBudget": 0}
                res = requests.post(url, json=payload, timeout=30)
                if res.status_code == 200:
                    candidate = res.json().get("candidates", [{}])[0]
                    parts = candidate.get("content", {}).get("parts", [])
                    text = "".join(p.get("text", "") for p in parts if p.get("text")).strip()
                    if len(text) > 50:
                        text = text.replace("```html", "").replace("```", "").strip()
                        return text
            except Exception as e:
                print(f"Gemini error ({model_name}): {e}")

    # 2. Groq API
    groq_key = os.environ.get("GROQ_API_KEY")
    if groq_key:
        for model_name in ["llama-3.3-70b-versatile", "llama3-70b-8192"]:
            try:
                headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
                payload = {
                    "model": model_name,
                    "messages": [{"role": "system", "content": system_message}, {"role": "user", "content": prompt}],
                    "temperature": 0.8,
                    "max_tokens": 2048
                }
                res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload, timeout=30)
                if res.status_code == 200:
                    text = res.json()["choices"][0]["message"]["content"].strip()
                    if len(text) > 50:
                        text = text.replace("```html", "").replace("```", "").strip()
                        return text
            except Exception as e:
                print(f"Groq error ({model_name}): {e}")

    # 3. OpenRouter API
    openrouter_key = os.environ.get("OPENROUTER_API_KEY")
    if openrouter_key:
        for model_name in ["google/gemma-3-27b-it:free", "mistralai/mistral-nemo:free"]:
            try:
                headers = {
                    "Authorization": f"Bearer {openrouter_key}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://github.com",
                    "X-Title": "AutoPoster"
                }
                payload = {
                    "model": model_name,
                    "messages": [{"role": "system", "content": system_message}, {"role": "user", "content": prompt}],
                    "temperature": 0.8,
                    "max_tokens": 2048
                }
                res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload, timeout=30)
                if res.status_code == 200:
                    text = res.json()["choices"][0]["message"]["content"].strip()
                    if len(text) > 50:
                        text = text.replace("```html", "").replace("```", "").strip()
                        return text
            except Exception as e:
                print(f"OpenRouter error ({model_name}): {e}")

    # 4. GitHub Models API (PAT)
    gh_token = os.environ.get("GH_TOKEN")
    if gh_token and not gh_token.startswith("ghs_"):
        for model_name in ["gpt-4o-mini", "gpt-4o"]:
            try:
                headers = {"Authorization": f"Bearer {gh_token}", "Content-Type": "application/json"}
                payload = {
                    "model": model_name,
                    "messages": [{"role": "system", "content": system_message}, {"role": "user", "content": prompt}],
                    "temperature": 0.8,
                    "max_tokens": 2048
                }
                res = requests.post("https://models.inference.ai.azure.com/chat/completions", headers=headers, json=payload, timeout=30)
                if res.status_code == 200:
                    text = res.json()["choices"][0]["message"]["content"].strip()
                    if len(text) > 50:
                        text = text.replace("```html", "").replace("```", "").strip()
                        return text
            except Exception as e:
                print(f"GitHub Models error ({model_name}): {e}")

    return None


import os
import time
import json
import re
import urllib.parse
import requests

POSTS_DIR = "src/data/posts"
CACHE_FILE = "posted_cache.txt"

def load_posted_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return set(line.strip() for line in f if line.strip())
    return set()

def save_to_cache(content_id):
    with open(CACHE_FILE, "a", encoding="utf-8") as f:
        f.write(f"{content_id}\n")

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

def fetch_fanza_item_by_keyword(keyword):
    api_id = os.environ.get("FANZA_API_ID", "z5dC9ZkXkE0YcW8QcZ4G") # フォールバックとして仮のIDを使用しないよう注意だが、本番では環境変数を利用する
    affiliate_id = os.environ.get("FANZA_AFFILIATE_ID", "onchan555-003")
    
    url = "https://api.dmm.com/affiliate/v3/ItemList"
    params = {
        "api_id": api_id,
        "affiliate_id": affiliate_id,
        "site": "FANZA",
        "service": "digital",
        "floor": "videoa",
        "keyword": keyword,
        "hits": 10,
        "output": "json"
    }

    print(f"Searching FANZA API for keyword: {keyword}")
    try:
        response = requests.get(url, params=params, timeout=15)
        if response.status_code != 200:
            print(f"API Error: {response.status_code}")
            return None
        data = response.json()
        items = data.get("result", {}).get("items", [])
        if items:
            return items[0] # 一番最初に見つかったものを返す
    except Exception as e:
        print(f"Request error: {e}")
    return None

def generate_article_with_llm(item):
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

【執筆ルール】
1. ペルソナ: ネットで絶大な支持を集める「秘密の恋愛・大人の背徳ドラマ専門」のカリスマ熱血レビュアー。圧倒的な文章の熱量で語ってください。
2. 感情的なキャッチコピー: 冒頭に作品の「禁断のシチュエーションのヤバさ」を突いた見出し（<h2> または <h3>）を配置してください。
3. マニア目線の心理描写: 公式のあらすじをなぞるのではない、ストーリー・心理・情景の推しポイントを熱量MAXで書いてください。
4. SEO対策とAIO対策: 「見どころ」「ユーザーの口コミ・評価風レビュー」「Q&A」などを構造化して書き、検索ユーザーの疑問に答える形（結論ファースト）で記載してください。
5. GEO対策・体験的価値: どのようなシチュエーションでこの作品を視聴すべきか（「週末の深夜、1人きりの部屋で高画質・独占配信で見るべき」など）を記載してください。
6. 表現の防壁: 直接的な性描写を避け、官能的で文学的表現に変換してください。
7. 【最重要】出力フォーマット: HTMLタグ（<p>, <h2>, <h3>, <ul>, <li>など）のみで出力し、マークダウンのコードブロック記法（```html や ``` など）は「絶対に」出力しないでください。余計なメタ情報は一切不要です。HTML本体のみを直接出力してください。

それでは、HTML本文のみを出力してください。
"""

    system_message = "あなたはSEOとAI-SEOを極めたカリスマ熱血レビュアーです。マークダウン記法を一切使用せず、純粋なHTMLのみを出力します。"

    print("Warning: LLM generation failed.")
    return "<p>レビューの生成に失敗しました。</p>"

def save_individual_post(post_data):
    os.makedirs(POSTS_DIR, exist_ok=True)
    post_id = post_data["id"]
    file_path = os.path.join(POSTS_DIR, f"{post_id}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f"Successfully saved: {file_path}")

def process_keyword(keyword):
    item = fetch_fanza_item_by_keyword(keyword)
    if not item:
        print(f"Failed to find item for keyword: {keyword}")
        return False

    content_id = item.get("content_id")
    title = item.get("title")
    affiliate_url = item.get("affiliateURL", "")
    
    if affiliate_url:
        affiliate_url = affiliate_url.replace("af_id=onchan555-999", "af_id=onchan555-003")

    image_url = ""
    images = item.get("imageURL", {})
    if images:
        image_url = images.get("large") or images.get("list") or ""
    
    movie = item.get("sampleMovieURL", {})
    sample_movie_url = movie.get("size_720_480") or movie.get("size_644_414") or ""

    sample_images = []
    sample_img_obj = item.get("sampleImageURL", {}).get("sample_l", {})
    if sample_img_obj:
        sample_images = sample_img_obj.get("image", [])

    review_html = generate_article_with_llm(item)

    post_data = {
        "id": content_id,
        "hinban": generate_hinban(content_id),
        "title": f"【超ド級の背徳感】 {title}",
        "review": review_html,
        "image": image_url,
        "sample_movie_url": sample_movie_url,
        "sample_images": sample_images,
        "affiliate_url": affiliate_url,
        "genres": [g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])],
        "actresses": [a.get("name", "") for a in item.get("iteminfo", {}).get("actress", [])],
        "maker": item.get("iteminfo", {}).get("maker", [{}])[0].get("name", ""),
        "date": item.get("date", time.strftime("%Y-%m-%d %H:%M:%S")),
        "labels": ["FANZA新作", "厳選レビュー"]
    }

    save_individual_post(post_data)
    save_to_cache(content_id)
    return True

if __name__ == "__main__":
    keywords = [
        "経験浅い外出し約束の19歳大学生の膣奥にお約束の中出し2回決行",
        "人妻快感柔肌悶え濡れる背徳性感恥帯"
    ]
    for kw in keywords:
        process_keyword(kw)
        time.sleep(2)
