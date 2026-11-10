# -*- coding: utf-8 -*-
import os
import json
import requests
from datetime import datetime

API_ID = "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = "onchan555-999"

def fetch_fanza_items(keyword, hits=5):
    url = "https://api.dmm.com/affiliate/v3/ItemList"
    params = {
        "api_id": API_ID,
        "affiliate_id": API_AFFILIATE_ID,
        "site": "FANZA",
        "service": "digital",
        "floor": "videoa",
        "keyword": keyword,
        "sort": "rank",
        "hits": hits,
        "output": "json"
    }
    try:
        res = requests.get(url, params=params, timeout=15)
        data = res.json()
        items = data.get("result", {}).get("items", [])
        return items
    except Exception as e:
        print(f"FANZA API Error for keyword '{keyword}': {e}")
        return []

def generate_article_content(theme_title, keyword, items):
    items_html = ""
    for idx, item in enumerate(items, 1):
        title = item.get("title", "極上人気作品")
        cid = item.get("content_id", f"cid_{idx}")
        aff_url = item.get("affiliateURL") or item.get("URL") or f"https://al.dmm.co.jp/?l=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3D{cid}%2F&i={API_AFFILIATE_ID}"
        price = item.get("prices", {}).get("price", "3,980円")
        
        image_url = ""
        img_info = item.get("imageURL", {})
        if isinstance(img_info, dict):
            image_url = img_info.get("large") or img_info.get("list") or ""
            
        actresses = [a.get("name") for a in item.get("iteminfo", {}).get("actress", [])]
        actress_str = ", ".join(actresses) if actresses else "人気専属女優"
        maker = item.get("iteminfo", {}).get("maker", [{}])[0].get("name", "有名メジャーレーベル")

        items_html += f"""
        <div class="ranking-item bg-gray-900 border border-red-900/50 rounded-xl p-6 mb-8 shadow-xl">
            <div class="flex items-center justify-between mb-4">
                <span class="bg-red-600 text-white text-lg font-extrabold px-4 py-1 rounded-full">第{idx}位</span>
                <span class="text-yellow-400 font-bold text-sm">【メーカー】{maker}</span>
            </div>
            <h3 class="text-2xl font-bold text-white mb-3 hover:text-red-400 transition-colors">{title}</h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-center mb-6">
                <div class="md:col-span-1">
                    {f'<img src="{image_url}" alt="{title}" class="rounded-lg shadow-lg w-full object-cover border border-gray-700" loading="lazy" />' if image_url else '<div class="bg-gray-800 rounded-lg h-48 flex items-center justify-center text-gray-500">画像準備中</div>'}
                </div>
                <div class="md:col-span-2 space-y-3">
                    <p class="text-gray-300 text-sm leading-relaxed">
                        <strong class="text-red-400">【出演女優】</strong> {actress_str}<br>
                        <strong class="text-red-400">【作品の特徴】</strong> 2026年最新トレンドを完全に網羅した圧倒的人気作。臨場感あふれるカメラワークと妥協のない濃厚な絡みが視聴者の理性を極限まで揺さぶります。
                    </p>
                    <div class="flex items-center space-x-4 pt-2">
                        <span class="text-xl font-bold text-red-500">価格: {price}</span>
                        <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="bg-gradient-to-r from-red-600 to-pink-600 hover:from-red-500 hover:to-pink-500 text-white font-bold px-6 py-3 rounded-xl shadow-lg transform hover:-translate-y-0.5 transition-all inline-flex items-center">
                            FANZAで今すぐ視聴する ➔
                        </a>
                    </div>
                </div>
            </div>
        </div>
        """

    body = f"""
    <p class="lead text-lg text-gray-300 leading-relaxed mb-6">
        近年のアダルト動画市場において、単なる視覚的刺激を超えた「シチュエーションのリアリティ」と「心理的背徳感」を追求した作品群が圧倒的な支持を集めています。本特集ではキーワード「<strong>{keyword}</strong>」を軸に、数ある名作の中から特に購買満足度が高くリピート率が驚異的な神作トップ5を徹底解説します。
    </p>

    <h2 class="text-2xl font-bold text-red-400 border-l-4 border-red-500 pl-4 my-8">
        1. 2026年最新トレンド：なぜこのジャンルが熱狂的な支持を集めるのか？
    </h2>
    <p class="text-gray-300 leading-relaxed mb-4">
        現代の映像作品において視聴者が最も重視しているのは圧倒的な没入感です。日常生活のすぐ隣に潜む非日常的シチュエーションにおける登場人物の微細な心の揺れ動きや理性が崩壊していく瞬間を生々しく捉えたドキュメンタリータッチの演出が、脳裏に焼き付くほどの興奮をもたらします。
    </p>

    <h2 class="text-2xl font-bold text-red-400 border-l-4 border-red-500 pl-4 my-8">
        2. 【徹底比較】絶対に外さない厳選おすすめ神作ランキングTOP5
    </h2>
    <p class="text-gray-300 leading-relaxed mb-6">
        FANZA公式APIからリアルタイムで取得した、今最も売れている最高峰の作品群をランキング形式で発表します。
    </p>

    {items_html}

    <h2 class="text-2xl font-bold text-red-400 border-l-4 border-red-500 pl-4 my-8">
        3. 最大限に楽しむための視聴環境とデバイス選びのコツ
    </h2>
    <p class="text-gray-300 leading-relaxed mb-4">
        高画質・高音質ストリーミングやVR対応作品を存分に味わうための推奨環境について解説します。
    </p>

    <h2 class="text-2xl font-bold text-red-400 border-l-4 border-red-500 pl-4 my-8">
        4. よくあるご質問（FAQ）
    </h2>
    <div class="space-y-4 text-gray-300 mb-8">
        <div class="bg-gray-800 p-4 rounded-xl border border-gray-700">
            <h3 class="font-bold text-white mb-2">Q. 紹介されている作品はすぐに視聴できますか？</h3>
            <p class="text-sm">A. はい。すべての作品はFANZAのデジタル配信に対応しており、購入後即座に視聴可能です。</p>
        </div>
    </div>

    <div class="mt-12 pt-6 border-t border-gray-800 text-sm text-gray-400">
        <p><strong>関連おすすめ特集：</strong></p>
        <div class="flex flex-wrap gap-3 mt-3">
            <a href="/features" class="bg-gray-800 hover:bg-red-900/50 text-red-400 px-4 py-2 rounded-lg border border-gray-700 transition-colors">🔥 特集記事一覧に戻る</a>
            <a href="/ranking" class="bg-gray-800 hover:bg-red-900/50 text-red-400 px-4 py-2 rounded-lg border border-gray-700 transition-colors">🏆 最新ランキングを見る</a>
        </div>
    </div>
    """
    return body

def main():
    themes = [
        {
            "id": "feature_hot_spring_inn_okami_ntr_2026",
            "title": "【秘湯の宿の若女将NTR】旦那の目を盗み客室で味わう背徳の不倫温泉・濃厚愛液まみれの肉欲ドキュメントおすすめ神作ランキングTOP5【2026年最新】",
            "keyword": "温泉",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "genres": ["温泉", "旅館", "若女将", "NTR", "不倫", "背徳", "人妻", "濃厚"]
        },
        {
            "id": "feature_elite_secretary_business_trip_2026",
            "title": "【エリート秘書と夜の出張同行】高級ホテルの相部屋宿泊で理性が吹き飛ぶ極上淫靡な夜這い・密着ピストンおすすめ神作ランキングTOP5【2026年最新】",
            "keyword": "ホテル",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "genres": ["秘書", "出張", "高級ホテル", "相部屋", "夜這い", "密着", "OL", "誘惑"]
        },
        {
            "id": "feature_art_studio_midnight_secret_2026",
            "title": "【深夜の彫刻アトリエ密会】誰にも見られない美術館の奥で芸術と肉欲が交錯する背徳の濡れ場おすすめ神作ランキングTOP5【2026年最新】",
            "keyword": "エステ",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "genres": ["アトリエ", "密会", "芸術", "背徳", "濡れ場", "モデル", "官能", "愛欲"]
        }
    ]

    posts_dir = "/Users/calro/Downloads/blogger-er/src/data/posts"
    os.makedirs(posts_dir, exist_ok=True)

    for theme in themes:
        print(f"\n--- テーマ生成中: {theme['title']} ---")
        items = fetch_fanza_items(theme["keyword"], hits=5)
        print(f"API取得作品数: {len(items)}")

        body_html = generate_article_content(theme["title"], theme["keyword"], items)

        post_data = {
            "id": theme["id"],
            "title": theme["title"],
            "date": theme["date"],
            "genres": theme["genres"],
            "content": body_html,
            "summary": f"{theme['title']}に関する2026年最新おすすめ神作ランキング。"
        }

        file_path = os.path.join(posts_dir, f"{theme['id']}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(post_data, f, ensure_ascii=False, indent=2)
        print(f"保存完了: {file_path}")

if __name__ == "__main__":
    main()
