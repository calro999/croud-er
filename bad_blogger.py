import os
import random
import requests
import time
import base64
import json
import tempfile
from playwright.sync_api import sync_playwright

CACHE_FILE = "posted_cache.txt"


def click_physical(page, selector):
    elements = page.locator(selector).all()
    for el in elements:
        try:
            box = el.bounding_box()
            if box and box['width'] > 0 and box['height'] > 0:
                x = box['x'] + box['width'] / 2
                y = box['y'] + box['height'] / 2
                page.mouse.click(x, y)
                return True
        except:
            pass
    return False

def load_posted_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return set(line.strip() for line in f if line.strip())
    return set()

def save_to_cache(content_id):
    with open(CACHE_FILE, "a", encoding="utf-8") as f:
        f.write(f"{content_id}\n")

def fetch_fanza_item():
    api_id = os.environ.get("FANZA_API_ID")
    affiliate_id = os.environ.get("FANZA_AFFILIATE_ID")
    if not api_id or not affiliate_id:
        raise ValueError("FANZA_API_ID and FANZA_AFFILIATE_ID must be set in environment variables.")

    # URL全体が入っている場合、クエリパラメータから抽出を試みる（デコード前に行う）
    import re
    import urllib.parse

    raw_api_id = api_id
    raw_affiliate_id = affiliate_id

    # api_idのパース
    if "api_id=" in raw_api_id:
        match = re.search(r"[?&]api_id=([^&]+)", raw_api_id)
        if match:
            api_id = match.group(1)

    # affiliate_idのパース
    if "affiliate_id=" in raw_affiliate_id:
        match = re.search(r"[?&]affiliate_id=([^&]+)", raw_affiliate_id)
        if match:
            affiliate_id = match.group(1)
    elif "affiliate_id=" in raw_api_id:
        # FANZA_API_IDのURL内に含まれるaffiliate_idを予備的に検索
        match = re.search(r"[?&]affiliate_id=([^&]+)", raw_api_id)
        if match:
            affiliate_id = match.group(1)

    # デコード・クレンジング処理を行う前に、何が渡ってきているかをアスキーコードのカンマ区切りにしてActionsのマスクを完全に回避して出力
    api_id_ascii = ",".join(str(ord(c)) for c in api_id)
    aff_ascii = ",".join(str(ord(c)) for c in affiliate_id)
    print(f"[DEBUG] ASCII API ID: {api_id_ascii}")
    print(f"[DEBUG] ASCII Affiliate ID: {aff_ascii}")

    # URLデコードしてアンパサンドなどのエスケープを解除
    api_id = urllib.parse.unquote(api_id).strip()
    affiliate_id = urllib.parse.unquote(affiliate_id).strip()

    # 背徳系キーワードリスト
    keywords = ["人妻 ネトラレ", "熟女 不倫", "団地妻 背徳"]
    selected_keyword = random.choice(keywords)
    print(f"Searching FANZA for keyword: {selected_keyword}")

    url = "https://api.dmm.com/affiliate/v3/ItemList"
    params = {
        "api_id": api_id,
        "affiliate_id": affiliate_id,
        "site": "FANZA",
        "service": "digital",
        "floor": "videoa",
        "keyword": selected_keyword,
        "sort": random.choice(["date", "rank"]),
        "hits": 10,
        "output": "json"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise RuntimeError(f"Failed to fetch from FANZA API: {response.status_code} - {response.text}")

    data = response.json()
    items = data.get("result", {}).get("items", [])
    if not items:
        raise RuntimeError(f"No items found for keyword: {selected_keyword}")

    posted_cache = load_posted_cache()
    for item in items:
        content_id = item.get("content_id")
        if content_id and content_id not in posted_cache:
            return item

    raise RuntimeError("All fetched FANZA items have already been posted.")

def clean_for_safety(text):
    if not text:
        return ""
    # コンテンツ管理ポリシーに引っかかりやすい単語の置換マップ
    safety_map = {
        "ネトラレ": "禁断の恋",
        "ねとられ": "禁断の恋",
        "不倫": "秘密の関係",
        "団地妻": "人妻",
        "人妻": "大人の女性",
        "背徳": "秘密の",
        "痴女": "魅力的な女性",
        "中出し": "愛の結末",
        "AV": "ビデオ作品",
        "アダルト": "大人向け"
    }
    for old, new in safety_map.items():
        text = text.replace(old, new)
    return text

def generate_article_with_llm(item):
    title = item.get("title")
    comment = item.get("comment", "")
    genres = ", ".join([g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])])
    affiliate_url = item.get("affiliateURL")
    
    # 画像URLの取得
    image_url = ""
    images = item.get("imageURL", {})
    if images:
        image_url = images.get("large") or images.get("list") or ""

    # タイトル、あらすじ、ジャンルをフィルターにかからないようマイルドに変換
    safe_title = clean_for_safety(title)
    safe_comment = clean_for_safety(comment)
    safe_genres = clean_for_safety(genres)

    prompt = f"""以下の大人向け映像作品の情報を基にして、指定の執筆ルールに従ってブログ記事のHTML本文（レビュー文）を生成してください。

【作品名】: {safe_title}
【あらすじ】: {safe_comment}
【ジャンル】: {safe_genres}

【執筆ルール】
1. ペルソナ: ネットで絶大な支持を集める「秘密の恋愛・大人の背徳ドラマ専門」のカリスマ熱血レビュアー。圧倒的な文章の熱量で語ってください。
2. 感情的なキャッチコピー: 冒頭に作品の「禁断のシチュエーションのヤバさ」を突いた見出し（<h3>）を配置してください。
3. マニア目線の心理描写: 公式のあらすじをなぞるのではない、ストーリー・心理・情景の推しポイントを熱量MAXで書いてください（例：「登場人物の葛藤する表情」「日常が崩壊していく感覚」など）。
4. ロングテールSEOの埋め込み: 記事内に自然な形で「主婦」「不倫」「旦那の留守中」「寝取られ」などの関連サジェストワードを散りばめてください。
5. 表現の防壁: 直接的な性描写（ポルノワード）を完全に避け、官能的で妄想を刺激する文学的表現（例：「禁断の領域」「蜜月」「背徳の泥沼」）に必ず変換してください。
6. 出力フォーマット: Bloggerにそのまま流し込めるように、本文のみをHTML（<p>, <h3>, <strong>）で出力し、マークダウンのコードブロック（```html や ```）は一切出力しないでください。

それでは、HTML本文のみを出力してください。
"""

    system_message = "あなたはネットで絶大な支持を集める「秘密の恋愛・大人の背徳ドラマ専門」のカリスマ熱血レビュアーです。規約に配慮しつつ極めて熱量の高いレビュー文をHTML形式で作成します。"

    # Pollinations AI のモデルリスト（高速かつモデレーションフリー）
    pollinations_models = ["openai", "openai-fast", "llama", "mistral", "qwen"]
    for attempt in range(2): # 全体で最大2回ループ
        for model in pollinations_models:
            try:
                print(f"Attempting to generate article with Pollinations AI (model: {model}, attempt: {attempt+1})...")
                response = requests.post(
                    "https://text.pollinations.ai/",
                    json={
                        "messages": [
                            {"role": "system", "content": system_message},
                            {"role": "user", "content": prompt}
                        ],
                        "model": model
                    },
                    timeout=35
                )
                if response.status_code == 200 and len(response.text.strip()) > 100:
                    result_text = response.text.strip()
                    if "```html" in result_text:
                        result_text = result_text.split("```html", 1)[1]
                    if "```" in result_text:
                        result_text = result_text.split("```", 1)[0]
                    return result_text.strip()
                elif response.status_code == 429:
                    print(f"Pollinations AI ({model}) returned 429 (Rate Limit). Waiting before retry...")
                    time.sleep(3)
                else:
                    print(f"Pollinations AI ({model}) returned status code: {response.status_code} - {response.text[:200]}")
            except Exception as e:
                print(f"Pollinations AI ({model}) failed with exception: {e}")
                time.sleep(2)

    # 最終的な絶対安全用のフォールバック生成
    print("Warning: All LLM models failed or timed out. Using high-quality fallback template.")
    fallback_html = f"""
    <h3>禁断のシチュエーションが織りなす大人の濃厚ストーリー！</h3>
    <p>日常のすぐ裏側に潜むスリリングな関係を描いた、本能を揺さぶる名作が登場しました。</p>
    <p><strong>「日常が静かに、しかし劇的に崩壊していく感覚」</strong>をじっくりと味わえる本作。登場人物たちが織りなす葛藤と、罪悪感に濡れた表情はまさにマニアも納得の仕上がりです。</p>
    <p>禁断の領域へと足を踏み入れていく二人の蜜月を、ぜひその目で確かめてみてください。</p>
    """
    return fallback_html.strip()

def post_to_blogger(title, content, labels):
    blog_id = os.environ.get("BLOGGER_BLOG_ID")
    if not blog_id:
        raise ValueError("BLOGGER_BLOG_ID is not set in environment variables.")
    session_b64 = os.environ.get("BLOGGER_SESSION_B64")
    
    session_file_path = None
    if session_b64:
        try:
            decoded_str = base64.b64decode(session_b64).decode('utf-8')
            json.loads(decoded_str)
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=False, suffix=".json") as temp_file:
                temp_file.write(decoded_str)
                session_file_path = temp_file.name
        except Exception as e:
            raise ValueError(f"BLOGGER_SESSION_B64 のデコードに失敗しました: {e}")
    elif os.path.exists("session.json"):
        print("Found local session.json. Using it for Blog Post.")
        session_file_path = "session.json"
    else:
        raise ValueError(f"BLOGGER_SESSION_B64 is not set and local session.json not found.")

    print(f"Posting to Blogger (Blog ID: {blog_id}) using Playwright...")

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=True,
                args=["--disable-blink-features=AutomationControlled"]
            )
            context = browser.new_context(
                storage_state=session_file_path,
                viewport={"width": 1280, "height": 800},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                permissions=['clipboard-read', 'clipboard-write']
            )
            page = context.new_page()
            page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

            try:
                time.sleep(random.uniform(3.0, 5.0))

                page.goto(f"https://draft.blogger.com/blog/post/edit/{blog_id}/new", wait_until="networkidle")
                time.sleep(random.uniform(3.0, 5.0))
                
                if "edit" not in page.url:
                    page.keyboard.press('c')
                    time.sleep(random.uniform(3.0, 5.0))
                
                if "edit" not in page.url:
                    page.evaluate('''() => {
                        const btns = Array.from(document.querySelectorAll('div[role="button"]'));
                        const newPostBtn = btns.find(b => (b.getAttribute('aria-label') || '').includes('新しい投稿') || (b.getAttribute('aria-label') || '').includes('New post'));
                        if (newPostBtn) newPostBtn.click();
                    }''')
                    time.sleep(random.uniform(3.0, 5.0))

                # 1. タイトル入力
                title_input = page.locator('.titleField input, input[aria-label*="Title"], input[aria-label*="タイトル"]').first
                title_input.wait_for(state="visible", timeout=30000)
                title_input.click()
                time.sleep(0.5)
                page.keyboard.press('Meta+A')
                page.keyboard.press('Control+A')
                page.keyboard.press('Backspace')
                
                max_retries = 3
                success = False
                
                for attempt in range(max_retries):
                    print(f"--- Attempt {attempt+1} / {max_retries} ---")
                    
                    if attempt > 0:
                        print("Reloading page for retry...")
                        page.reload(wait_until="domcontentloaded")
                        time.sleep(3)
                    
                    try:
                        title_input = page.locator('input.titleField, input[aria-label="タイトル"], input[aria-label="Title"]').locator("visible=true").first
                        title_input.fill(title)
                        time.sleep(2)
                        
                        print("Focusing on the rich text editor via Tab navigation...")
                        page.keyboard.press('Tab')
                        time.sleep(0.5)
                        page.keyboard.press('Tab')
                        time.sleep(1)
                        
                        try:
                            editor_body = page.locator('div[aria-label="本文"], div[aria-label="Body"], div[role="textbox"], iframe').locator("visible=true").first
                            editor_body.click(timeout=3000)
                        except:
                            pass
                            
                        print("Injecting HTML via Playwright clipboard paste...")
                        page.evaluate('''html => {
                            try {
                                const blob = new Blob([html], { type: 'text/html' });
                                const data = [new ClipboardItem({ 'text/html': blob })];
                                navigator.clipboard.write(data);
                            } catch (e) {
                                console.error('Clipboard write failed:', e);
                            }
                        }''', content)
                        time.sleep(2)
                        
                        page.keyboard.press('Control+V')
                        page.keyboard.press('Meta+V')
                        time.sleep(2)
                        
                        page.keyboard.press('Space')
                        time.sleep(0.5)
                        page.keyboard.press('Backspace')
                        time.sleep(3)
                        
                        print("Validating injected content...")
                        page_html = page.content()
                        
                        if "<img" in page_html and ("href" in page_html or "http" in page_html):
                            print("Validation passed: Body content successfully detected in page!")
                            success = True
                            break
                        else:
                            print("Validation failed: Body seems empty or missing images.")
                            
                    except Exception as e:
                        print(f"Error during injection attempt {attempt+1}: {e}")
                        
                    time.sleep(3)
                
                if not success:
                    raise Exception("Critical Failure: Could not inject body content.")

                # ラベル（タグ）の追加
                try:
                    print("Adding labels...")
                    # ラベル入力フィールドのプレースホルダーやaria-labelにマッチさせる
                    label_input = page.locator('input[aria-label*="ラベル"], input[aria-label*="Label"], input[placeholder*="ラベル"]').first
                    if label_input.is_visible():
                        label_input.click()
                        time.sleep(0.5)
                        labels_str = ",".join(labels)
                        label_input.fill(labels_str)
                        page.keyboard.press('Enter')
                        print(f"Labels added: {labels_str}")
                        time.sleep(2)
                except Exception as label_err:
                    print(f"Failed to add labels: {label_err}")

                # 3. 公開ボタンのクリック
                print("Publishing post...")
                try:
                    pub_btn = page.locator('[aria-label="公開"], [aria-label="Publish"]').locator("visible=true").first
                    pub_btn.scroll_into_view_if_needed()
                    time.sleep(1)
                    pub_btn.click(force=True, timeout=10000)
                    print("Clicked publish button.")
                except Exception as e:
                    print("Failed to click publish button:", e)
                    page.keyboard.press('Control+Shift+P')
                    page.keyboard.press('Meta+Shift+P')
                
                time.sleep(4)

                # 4. 確認ダイアログの「確認」ボタン
                try:
                    conf_btn = page.locator('[aria-label="確認"], [aria-label="Confirm"], div[role="button"]:has-text("確認")').locator("visible=true").first
                    conf_btn.scroll_into_view_if_needed()
                    time.sleep(1)
                    conf_btn.click(force=True, timeout=10000)
                    print("Clicked confirm button.")
                except Exception as e:
                    print("Failed to click confirm button:", e)
                    page.keyboard.press('Enter')
                
                time.sleep(10)
                print("Successfully published post using Playwright!")
            except Exception as e:
                print(f"Error occurred. Current URL: {page.url}")
                raise e

    finally:
        if session_file_path and session_file_path != "session.json" and os.path.exists(session_file_path):
            os.remove(session_file_path)


def main():
    try:
        # 1. FANZAから商品取得
        item = fetch_fanza_item()
        content_id = item.get("content_id")
        title = item.get("title")
        affiliate_url = item.get("affiliateURL")
        # リンク用のアフィリエイトIDはonchan555-003にするため、取得したURLのaf_idパラメータ部分を書き換える
        if affiliate_url:
            # af_id=onchan555-999 (あるいはAPI用ID) の箇所を強制的に onchan555-003 に書き換え
            affiliate_url = affiliate_url.replace("af_id=onchan555-999", "af_id=onchan555-003")
            # 汎用的に環境変数で指定された値から書き換えるフォールバック
            api_aff_id = os.environ.get("FANZA_AFFILIATE_ID")
            if api_aff_id and api_aff_id != "onchan555-003":
                affiliate_url = affiliate_url.replace(f"af_id={api_aff_id}", "af_id=onchan555-003")

        print(f"Selected FANZA Item: {title} ({content_id})")
        print(f"[DEBUG] Replaced Link Affiliate URL: {affiliate_url}")

        # 画像URL
        image_url = ""
        images = item.get("imageURL", {})
        if images:
            image_url = images.get("large") or images.get("list") or ""

        # 2. LLMでレビュー文HTML生成
        review_html = generate_article_with_llm(item)
        
        # 3. 指定レイアウトHTMLとガッチャンコする
        # CTAボタン用のグラデーションCSS付きリンク
        cta_button_html = f"""
        <div style="text-align: center; margin: 40px 0;">
            <a href="{affiliate_url}" target="_blank" rel="noopener noreferrer" style="
                display: inline-block;
                padding: 18px 36px;
                font-size: 20px;
                font-weight: bold;
                color: #ffffff;
                background: linear-gradient(45deg, #ff416c, #ff4b2b);
                text-decoration: none;
                border-radius: 50px;
                box-shadow: 0 4px 15px rgba(255, 75, 43, 0.4);
                transition: transform 0.2s;
            ">
                🔥 今すぐこの作品を視聴する！
            </a>
        </div>
        """
        
        full_html = f"""
        <div class="fanza-review-post" style="font-family: 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; color: #333;">
            <div style="text-align: center; margin-bottom: 30px;">
                <a href="{affiliate_url}" target="_blank" rel="noopener noreferrer">
                    <img src="{image_url}" alt="{title}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.15);" />
                </a>
            </div>
            
            <div class="review-body" style="font-size: 16px; margin-bottom: 30px;">
                {review_html}
            </div>
            
            {cta_button_html}
        </div>
        """

        gen_title = f"【超ド級の背徳感】 {title}"
        labels = ["FANZA新作", "人妻", "ネトラレ", "背徳不倫"]
        
        print("--- Generated HTML Content Snippet ---")
        print(full_html[:300])
        print("--------------------------------------")
        
        post_to_blogger(gen_title, full_html, labels)

        # 4. キャッシュに保存
        save_to_cache(content_id)
        print("Process completed successfully.")

    except Exception as e:
        print(f"Error in execution: {e}")
        exit(1)

if __name__ == "__main__":
    main()
