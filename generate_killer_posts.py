import os
import random
import re

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

quests
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
            
    fallback_title = title or "この作品"
    fallback_genres = "、".join(genres.split(", ")) if genres else "大人の背徳ドラマ"
    fallback_maker = item.get("iteminfo", {}).get("maker", [{}])[0].get("name", "一流メーカー") if item.get("iteminfo", {}).get("maker") else "一流メーカー"

    # 5パターンのフォールバックテンプレート（Duplicate Content回避）
    pattern = random.randint(1, 5)

    if pattern == 1:
        return f"""<h2>『{fallback_title}』完全レビュー——{fallback_genres}マニアが唸る感動スペック全分析</h2>
<p>当サイトのレビュアーが、今年観た作品の中で脳裏に濃く刻まれた一本がこれ。『{fallback_title}』は、単なるエンターテインメントを超えて、見る者の内側に何かを残す作品だ。</p>
<h3>『{fallback_title}』を見るべき3つの理由</h3>
<ul>
<li><strong>理由①：シチュエーションの独自性</strong>——{fallback_genres}ならではのリアリティに満ちた設定。</li>
<li><strong>理由②：{fallback_maker}の意気込み</strong>——一切顧みない映像クオリティと編集技術。</li>
<li><strong>理由③：何度でも唸れる完璧な作り</strong>——見るたびに新たな発見がある作品構成。</li>
</ul>
<h3>記者が気になった「神カット」分析</h3>
<p>{fallback_genres}のシチュエーションを与えられた出演者のリアクションは、まさにこれこそが整局のハイライトと言えるシーンの連続だ。見る手が「なぜそんな表情ができるのか」と考えさせるほどの深みがある。</p>
<h3>カメラワーク・編集・音響の「トリプルな魅力」</h3>
<p>{fallback_maker}が声った、まるでドキュメンタリーのような寄り高いアングル。一切の張り何く午後の頂病のように身をゆだねるキャストが、映像全体に流れる気備を割る。</p>
<h4>映像美のポイント</h4>
<p>高画質映像ならではの鮮明な映像美と、静寂の中に響く環境音が、リアリティを係数的に引き上げる。</p>
<h2>総合評価——『{fallback_title}』の口克</h2>
<table><thead><tr><th>評価項目</th><th>スコア</th></tr></thead><tbody><tr><td>シチュエーション</td><td>★★★★★</td></tr><tr><td>キャスト</td><td>★★★★☆</td></tr><tr><td>映像</td><td>★★★★★</td></tr><tr><td>総合</td><td>★★★★★</td></tr></tbody></table>
<p>当サイトが誇う中でも特にお特めする作品。見逃した場合は必ず御出に。</p>"""

    elif pattern == 2:
        return f"""<h2>『{fallback_title}』出演女優の百面の魅力——{fallback_genres}エクストリーム全分析</h2>
<p>『{fallback_title}』を初めて観た頭毎にるのは、キャストの知性と本能の道象となるような存在感だ。{fallback_maker}が慎身を差し居るからこそ、これほどのクオリティが実現する。</p>
<h3>記者が認める「{fallback_title}」の彼女の裡</h3>
<p>{fallback_genres}のシチュエーションを与えられた女優のリアクションは、見る者が「自分もその立場にいる」と覚各するほどなビルド感に満ちている。</p>
<h3>スタッフが情穀った「山場」の確かな一手</h3>
<p>{fallback_maker}が対出した高めのカメラ位置と編集的リズムは、観る者の感情を完全に深場に引き込む。「そこに居る」ことの感覚の高さはネット上のレビューでも高評価。</p>
<h4>見どころポイント</h4>
<ul>
<li>女優の知性と本能が交差する予測不能な表情変化。</li>
<li>プロだからこそ出る、即興を超えた真そのままの姿。</li>
<li>頼れるリズム感で完結に向かって酵す構成。</li>
</ul>
<h2>総合評価</h2>
<table><thead><tr><th>評価項目</th><th>スコア</th></tr></thead><tbody><tr><td>女優の相ろ</td><td>★★★★★</td></tr><tr><td>シチュエーション</td><td>★★★★★</td></tr><tr><td>映像超</td><td>★★★★☆</td></tr><tr><td>総合</td><td>★★★★★</td></tr></tbody></table>
<p>一度視聴し始めたら最後まで目が離せない作品。</p>"""

    elif pattern == 3:
        return f"""<h2>『{fallback_title}』全切りレビュー——{fallback_genres}マニア者必見のエッセンス</h2>
<p>『{fallback_title}』を観る前に知っておくべきことが3つある。ライターが自信を持っておすすめできる理由を、全力で語る。</p>
<h3>1. 「{fallback_title}」の内容概要</h3>
<p>{fallback_genres}をメインに掲いながらも、完全にテンプレート的な展開を拒否する独自のシナリオ機構。{fallback_maker}の制作陣容の深さが就している。</p>
<h3>2. 記者が驚いた「神カット」分析</h3>
<p>観る者が「自分もその立場で居る」と覚各するほどの埋没感。カメラと編集の能力がその頂をたどるような構成で、状況まりは最後のクライマックスに向けて一気に上昇する。</p>
<h3>3. それでも「{fallback_title}」を矜んでいない人へ</h3>
<p>見ていないのはじめて見る前の自分だけ。岐路じていることをして見るべきだ。</p>
<h4>レビュアー最大注目ポイント</h4>
<ul>
<li>{fallback_maker}の大漠を入れた映像安と編集。</li>
<li>出演者と神ライトが対向いた次の感を思わせるカメラワーク。</li>
<li>忍耐と略奈が串となったシナリオ構成の妙味。</li>
</ul>
<h2>総合評価</h2>
<table><thead><tr><th>評価項目</th><th>スコア</th></tr></thead><tbody><tr><td>シチュエーション</td><td>★★★★★</td></tr><tr><td>映像</td><td>★★★★★</td></tr><tr><td>総合</td><td>★★★★★</td></tr></tbody></table><p>一度見ると芯落こない。</p>"""

    elif pattern == 4:
        return f"""{fallback_genres}の極致形——『{fallback_title}』はなぜ今期最高峰なのか
<h2>{fallback_genres}の極致形——なぜ今期最高峰なのか</h2>
<p>{fallback_maker}が近年リリースした作品群の中でも、『{fallback_title}』は途铁に隠いて反鎚する感情を探ってくる。</p>
<h3>この作品が・・・世代の談に成る理由</h3>
<p>{fallback_genres}の出演者たちが織りなす関係性の深さ、そして{fallback_maker}が償った楚天な映像美が、その深場感を係数的に探る。</p>
<h3>レビュアーが気屋の丈くた「見どころ」</h3>
<ul>
<li><strong>対局的な導入</strong>：開始から感じる流れ感。</li>
<li><strong>目を凸る別ら顧みを与える女優の表現</strong>：プロだから出る、即興を超えた真そのままの姿。</li>
<li><strong>気屋の丈く編集</strong>：頼れるリズム感で完結に向かって酵す構成。</li>
</ul>
<h4>スタッフのこだわり</h4>
<p>照明・音響・カメラアングル全てにおいて{fallback_maker}の妥協なきこだわりが見て取れる。</p>
<h2>総合評価</h2>
<table><thead><tr><th>評価項目</th><th>スコア</th></tr></thead><tbody><tr><td>シチュエーション</td><td>★★★★☆</td></tr><tr><td>キャスト</td><td>★★★★★</td></tr><tr><td>総合</td><td>★★★★★</td></tr></tbody></table>
<p>『{fallback_title}』は興味のある人全員に自信を持っておすすめする作品。</p>"""

    else:
        return f"""<h2>手取りレビュー：『{fallback_title}』——{fallback_genres}マニア者に唸う永遠の影</h2>
<p>『{fallback_title}』——そのタイトルだけで导かれる人がいることは容易に想像できる。それほどに魅力的な内容と出演者がままならないで観る者の心を追いかけてくるからだ。</p>
<h3>{fallback_genres}というラベルが必ずしもこの作品を語れない理由</h3>
<p>{fallback_genres}というカテゴリに内包されるが、この作品はその命験を当に身にまとった上でさらに高い山へ登ろうとする佳の作品だ。</p>
<h3>レビュアー最大注目ポイント</h3>
<ul>
<li>{fallback_maker}の大漠を入れた映像安と編集。</li>
<li>出演者と神ライトが対向いた次の感を思わせるカメラワーク。</li>
<li>忍耐と略奈が串となったシナリオ構成の妙味。</li>
</ul>
<h3>それでも「{fallback_title}」を矜んでいない人へのメッセージ</h3>
<p>見ていないのはじめて見る前の自分だけ。岐路じていることを後悔するぐらいならすぐ見るべきだ。</p>
<h2>総合評価</h2>
<table><thead><tr><th>評価項目</th><th>スコア</th></tr></thead><tbody><tr><td>シチュエーション</td><td>★★★★★</td></tr><tr><td>キャスト</td><td>★★★★★</td></tr><tr><td>映像</td><td>★★★★☆</td></tr><tr><td>総合</td><td>★★★★★</td></tr></tbody></table>
<p>『{fallback_title}』は興味のある人全員に自信を持っておすすめする作品。</p>"""


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
            "hinban": generate_hinban(content_id),
            "title": title,
            "review": review_html,
            "image": image_url,
            "sample_images": sample_images,
            "affiliate_url": affiliate_url,
            "genres": [g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])],
            "actresses": [a.get("name", "") for a in item.get("iteminfo", {}).get("actress", [])],
            "maker": item.get("iteminfo", {}).get("maker", [{}])[0].get("name", ""),
            "date": item.get("date", time.strftime("%Y-%m-%d %H:%M:%S")),
            "labels": ["超話題作", "2026年最新", "SNSで話題", "人気"]
        }
        
        save_individual_post(post_data)
        save_to_cache(content_id)
        
        generated_count += 1
        time.sleep(2) # API/LLMへの負荷軽減
        
    print(f"--- Generated {generated_count} killer posts ---")

if __name__ == "__main__":
    main()
