import os

# Cloudflare Pages / Vercelなどでビルド時に静的データを生成するため、
# ビルドエラーを防ぐプレースホルダーJSONファイルをローカルに生成しておく
JSON_DB_PATH = os.path.join("public", "data", "posts.json")

def main():
    if not os.path.exists(JSON_DB_PATH):
        os.makedirs(os.path.dirname(JSON_DB_PATH), exist_ok=True)
        with open(JSON_DB_PATH, "w", encoding="utf-8") as f:
            f.write("[]")
        print("Initialized empty posts.json database.")

if __name__ == "__main__":
    main()
