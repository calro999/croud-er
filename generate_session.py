import os
import json
import base64
from playwright.sync_api import sync_playwright

def main():
    print("Blogger にログインしてセッションを保存します...")
    with sync_playwright() as p:
        # 自動化検知を回避するための引数を指定して起動
        browser = p.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        # webdriver検出フラグを無効化
        page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        # 1. Bloggerへのログイン
        page.goto("https://www.blogger.com/")
        print("=========================================================")
        print("ブラウザ上でGoogleアカウント（Blogger）にログインしてください。")
        print("ログイン完了後、Bloggerのダッシュボードが表示されたら、")
        print("このターミナルで Enter キーを押してください。")
        print("=========================================================")
        input("Press Enter after Blogger login...")
        
        state = context.storage_state()
        
        with open("session.json", "w") as f:
            json.dump(state, f)
            
        print("session.json を作成しました。")
        
        # Base64エンコードした文字列を直接ターミナルに出力
        session_str = json.dumps(state)
        b64_str = base64.b64encode(session_str.encode('utf-8')).decode('utf-8')
        
        print("\n================== BLOGGER_SESSION_B64 (COPY THIS) ==================")
        print(b64_str)
        print("=====================================================================\n")
        print("上記の長い文字列をすべてコピーして、GitHub Secrets of BLOGGER_SESSION_B64 に設定してください。")

        browser.close()

if __name__ == "__main__":
    main()
