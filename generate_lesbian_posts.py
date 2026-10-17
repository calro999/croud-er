
def call_multi_llm_api(prompt, system_content="You are a helpful assistant."):
    # 1. Groq API
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

    # 2. Gemini API
    gemini_key = os.environ.get("GEMINI_API_KEY")
    if gemini_key:
        gemini_models = [
            "gemini-2.0-flash",
            "gemini-2.0-flash-lite",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
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


CACHE_FILE = "posted_cache.txt"
POSTS_DIR = "src/data/posts"

# API固定設定
API_ID = "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = "onchan555-999"
LINK_AFFILIATE_ID = "onchan555-003"
TARGET_POST_COUNT = 3

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

def generate_fake_reviews():
    score_ero = round(random.uniform(4.0, 5.0), 1)
    score_story = round(random.uniform(3.0, 4.8), 1)
    score_camera = round(random.uniform(3.5, 4.9), 1)
    
    comments_pool = [
        "マジで抜けた。今年トップクラスの当たり。",
        "女優の表情がエロすぎる…絶対リピートする。",
        "カメラワークが神。見たいところをしっかり映してくれてる。",
        "最初は期待してなかったけど、後半の展開で完全に昇天した。",
        "SNSで話題になってたから見たけど、噂以上の破壊力だったわ。",
        "このシリーズはハズレがない。今回も最高。",
        "パッケージ詐欺なし！本編の方がエロいという奇跡。",
        "何度見ても抜ける。保存版確定です。"
    ]
    
    selected_comments = random.sample(comments_pool, 3)
    
    html = f"""
<div class="mt-8 bg-slate-50 border border-slate-200 rounded-2xl p-6 shadow-sm">
    <h3 class="text-lg font-extrabold text-slate-800 mb-4 border-b border-slate-200 pb-2">⭐ ユーザーの評価・口コミ</h3>
    
    <div class="flex flex-wrap gap-4 mb-6">
        <div class="bg-white px-4 py-2 rounded-xl border border-rose-100 shadow-sm text-center flex-1 min-w-[100px]">
            <span class="block text-[10px] text-slate-500 font-bold mb-1">エロ度</span>
            <span class="text-xl font-black text-rose-500">{score_ero}</span><span class="text-sm text-slate-400">/5.0</span>
        </div>
        <div class="bg-white px-4 py-2 rounded-xl border border-rose-100 shadow-sm text-center flex-1 min-w-[100px]">
            <span class="block text-[10px] text-slate-500 font-bold mb-1">ストーリー</span>
            <span class="text-xl font-black text-rose-500">{score_story}</span><span class="text-sm text-slate-400">/5.0</span>
        </div>
        <div class="bg-white px-4 py-2 rounded-xl border border-rose-100 shadow-sm text-center flex-1 min-w-[100px]">
            <span class="block text-[10px] text-slate-500 font-bold mb-1">カメラワーク</span>
            <span class="text-xl font-black text-rose-500">{score_camera}</span><span class="text-sm text-slate-400">/5.0</span>
        </div>
    </div>

    <div class="space-y-4">
        <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm relative">
            <span class="absolute -top-3 left-4 bg-rose-500 text-white text-[9px] font-bold px-2 py-0.5 rounded-full">レビュー</span>
            <p class="text-sm text-slate-700 font-medium leading-relaxed">「{selected_comments[0]}」</p>
        </div>
        <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm relative">
            <span class="absolute -top-3 left-4 bg-rose-500 text-white text-[9px] font-bold px-2 py-0.5 rounded-full">レビュー</span>
            <p class="text-sm text-slate-700 font-medium leading-relaxed">「{selected_comments[1]}」</p>
        </div>
        <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm relative">
            <span class="absolute -top-3 left-4 bg-rose-500 text-white text-[9px] font-bold px-2 py-0.5 rounded-full">レビュー</span>
            <p class="text-sm text-slate-700 font-medium leading-relaxed">「{selected_comments[2]}」</p>
        </div>
    </div>
</div>
"""
    return html


def save_to_cache(content_id):
    with open(CACHE_FILE, "a", encoding="utf-8") as f:
        f.write(f"{content_id}\n")

def get_random_internal_links(num_links=3):
    if not os.path.exists(POSTS_DIR):
        return ""
    post_files = [f for f in os.listdir(POSTS_DIR) if f.endswith('.json')]
    if not post_files:
        return ""
    
    selected = random.sample(post_files, min(num_links, len(post_files)))
    links_html = "<h3>あわせて読みたいおすすめ記事</h3>\n<ul>\n"
    for filename in selected:
        try:
            with open(os.path.join(POSTS_DIR, filename), "r", encoding="utf-8") as f:
                data = json.load(f)
                post_id = data.get("id", "")
                post_title = data.get("title", "")
                if post_id and post_title:
                    links_html += f'<li><a href="/post/{post_id}">{post_title}</a></li>\n'
        except:
            pass
    links_html += "</ul>"
    return links_html

def fetch_fanza_items():
    # レズ・百合に特化したキーワード（確実にヒットしやすいものに絞る）
    keywords = ["レズ", "百合", "女性同士"]
    
    url = "https://api.dmm.com/affiliate/v3/ItemList"
    
    all_items = []
    
    # すべてのキーワードを試す
    for keyword in keywords:
        for sort_type in ["rank", "date"]:
            print(f"Fetching FANZA items for keyword: '{keyword}', sort: '{sort_type}'")
            
            params = {
                "api_id": API_ID,
                "affiliate_id": API_AFFILIATE_ID,
                "site": "FANZA",
                "service": "digital",
                "floor": "videoa",
                "keyword": keyword,
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

    prompt = f"""以下の大人向け映像作品の情報を基にして、SEO超特化・最強執筆ルールに従ってブログ記事のHTML本文を生成してください。

【作品名】: {safe_title}
【あらすじ】: {safe_comment}
【ジャンル】: {safe_genres}

【SEO超特化・最強執筆ルール】
1. 【長さ】: 必ず2000文字以上の底つきのある記事を書くこと。短い記事は絶対に禁止。
2. 【見出し構成】: <h2>を2つ以上、<h3>を4つ以上、<h4>を2つ以上使って論理的な見出し階層を作ること。
3. 【検索意図】: 「レビュー」「感想」「評価」「見どころ」「おすすめ」「サンプル」など読者が使う検索キーワードを自然に盛り込む。
4. 【導入フック】: 冒頭で読者を引き込む強烈なフック文を書く（「見た瞬間に後悔する」「完全に予想を裏切ってくる」など）。
5. 【独自性】: 他サイトのレビューと全く異なるライターの個性を濃く出すこと。
6. 【構成必須セクション】:
   ・作品概要（どんな内容か）
   ・見どころ分析（なぜこの作品が優れているか）
   ・キャスト分析（出演者の魅力）
   ・演出・カメラワーク（技術面の評価）
   ・評価表（tableタグで各要素をスコア付け）
   ・総評
7. 【表現の防壁】: 直接的な性描写ワードを完全に避け、官能的で文学的な表現に変換。
8. 【フォーマット】: HTMLのみ出力（h2, h3, h4, p, strong, ul, li, table, thead, tbody, tr, th, td）。マークダウンのコードブロック（```html等）は使用禁止。

SEO最強のHTML本文のみを出力してください。
"""

    system_message = "あなたはネットで絶大な支持を集める「百合・女性同士の恋愛・背徳ドラマ専門」のカリスマ熱血レビュアーです。規約に配慮しつつ極めて熱量の高いレビュー文をHTML形式で作成します。"

    article_html = call_multi_llm_api(prompt, system_message)
    if article_html:
        if "```html" in article_html:
            article_html = article_html.split("```html", 1)[1].split("```")[0]
        elif "```" in article_html:
            article_html = article_html.split("```", 1)[1].split("```")[0]
        article_html = article_html.strip()
        if len(article_html) > 200:
            return article_html

    # フォールバック処理: 固定テンプレートを廃止し、作品データに基づく完全動的レビューを生成
    fallback_title = title or "この作品"
    clean_t = re.sub(r'【.*?】', '', fallback_title).strip() or fallback_title
    fallback_genres = "、".join(genres.split(", ")) if genres else "百合・レズビアン"
    fallback_maker = item.get("iteminfo", {}).get("maker", [{}])[0].get("name", "一流メーカー") if item.get("iteminfo", {}).get("maker") else "一流メーカー"
    actresses = [a.get("name", "") for a in item.get("iteminfo", {}).get("actress", [])]
    actress_str = "・".join(actresses) if actresses else ""

    intro_hooks = [
        f"数ある百合・レズ作品の中でも、ひときわ熱い情熱と濃密な肌の重なり合いが描かれた{fallback_maker}の注目作。",
        f"女性同士だからこそ生まれる繊細な空気感と、次第に高まる熱情に息をのむ名作。",
        f"タイトルのインパクトそのままに、互いの体を貪り合う美しくも淫らな情景が広がる一本。"
    ]
    
    if actresses:
        actress_focus = f"""
<h3>出演キャスト（{actress_str}）の魅力と濃密な絡み</h3>
<p>{actress_str}が魅せる、恥じらいと情熱が混ざり合った至極の表情。肌を重ね合わせるたびに深まる吐息と熱気が、見る側の五感を刺激します。</p>
"""
    else:
        actress_focus = f"""
<h3>女性同士ならではの美しく官能的なシチュエーション</h3>
<p>本作の最大の魅力は、女性同士の繊細な心理描写と官能的な距離感の演出です。ためらいが快楽へと変わっていくプロセスが丁寧に描かれています。</p>
"""

    highlight_focus = f"""
<h3>見どころ・おすすめの視聴ポイント</h3>
<p>『{clean_t}』のハイライトは、中盤以降の止まらない愛撫と熱狂のクライマックス。{fallback_genres}の世界観を存分に味わえるハイクオリティな映像美に仕上がっています。</p>
"""

    closing_thoughts = [
        f"『{clean_t}』は、{fallback_maker}が放つ百合・レズ作品の傑作。濃厚で甘美な世界に浸りたい方に心からおすすめします。",
        f"最初から最後まで美しい映像と情熱的な展開に惹き込まれる一本。ぜひじっくりとご堪能ください。"
    ]

    selected_intro = random.choice(intro_hooks)
    selected_closing = random.choice(closing_thoughts)

    return f"""<h2>『{clean_t}』詳細レビュー・作品の見どころ</h2>
<p>{selected_intro}</p>
{actress_focus}
{highlight_focus}
<h3>総評</h3>
<p>{selected_closing}</p>"""


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
        
        movie = item.get("sampleMovieURL", {})
        sample_movie_url = movie.get("size_720_480") or movie.get("size_644_414") or movie.get("size_560_360") or movie.get("size_476_306") or ""
        if sample_movie_url and "onchan555-999" in sample_movie_url:
            sample_movie_url = sample_movie_url.replace("onchan555-999", LINK_AFFILIATE_ID)


        sample_images = []
        sample_img_obj = item.get("sampleImageURL", {}).get("sample_l", {})
        if sample_img_obj:
            sample_images = sample_img_obj.get("image", [])
            
        print(f"[{generated_count+1}/{TARGET_POST_COUNT}] Processing: {title}")
        review_html = generate_killer_article(item)
        
        fake_reviews = generate_fake_reviews()
        review_html += "\n" + fake_reviews

        internal_links = get_random_internal_links(3)
        if internal_links:
            review_html += "\n" + internal_links
        
        post_data = {
            "id": content_id,
            "hinban": generate_hinban(content_id),
            "title": title,
            "review": review_html,
            "image": image_url,
            "sample_movie_url": sample_movie_url,
            "sample_images": sample_images,
            "affiliate_url": affiliate_url,
            "genres": list(set([g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])] + ["レズ"])),
            "actresses": [a.get("name", "") for a in item.get("iteminfo", {}).get("actress", [])],
            "maker": item.get("iteminfo", {}).get("maker", [{}])[0].get("name", ""),
            "date": item.get("date", time.strftime("%Y-%m-%d %H:%M:%S")),
            "labels": ["レズ", "百合", "女性同士", "2026年最新"]
        }
        
        save_individual_post(post_data)
        save_to_cache(content_id)
        
        generated_count += 1
        time.sleep(2) # API/LLMへの負荷軽減
        
    print(f"--- Generated {generated_count} killer posts ---")

if __name__ == "__main__":
    main()
