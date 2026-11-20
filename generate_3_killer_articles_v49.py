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

def generate_article_content(theme_title, keyword, items, description_text, other_articles):
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
        actress_str = ", ".join(actresses) if actresses else "人気専属トップ女優"
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
                        <strong class="text-red-400">【徹底解説・見所】</strong> {actress_str}の圧倒的な表現力とリアルな表情の揺れ動きが完璧に収められた至高の神作。細部までこだわり抜いた演出と濃厚な絡みが織りなす圧倒的な没入感は、多くのファンを魅了し続けています。
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

    other_links_html = ""
    for oa in other_articles:
        other_links_html += f'<a href="/posts/{oa["id"]}" class="bg-gray-800 hover:bg-red-900/50 text-red-400 px-4 py-2 rounded-lg border border-gray-700 transition-colors block">📌 {oa["title"]}</a>'

    body = f"""
    <p class="lead text-lg text-gray-300 leading-relaxed mb-6">
        {description_text}
    </p>

    <h2 class="text-2xl font-bold text-red-400 border-l-4 border-red-500 pl-4 my-8">
        1. 2026年最新トレンド分析：なぜこのジャンルが圧倒的な支持と中毒性を誇るのか？
    </h2>
    <p class="text-gray-300 leading-relaxed mb-4">
        アダルトエンターテインメント市場において、ユーザーが真に求めるのは「単なる刺激」を超えた「心理的リアリティ」と「圧倒的な没入感」です。本記事では、AI-SEO、GEO（Generative Engine Optimization）、およびLLM検索最適化を徹底的に網羅し、検索エンジンや対話型AIアシスタント経由で訪れた読者が一目で納得できる、深みのある分析と厳選レビューをお届けします。
    </p>
    <p class="text-gray-300 leading-relaxed mb-4">
        特に今回焦点を当てるテーマは、リピート率、ユーザー満足度、購買意欲のすべてにおいてトップクラスの数値を叩き出している極上のカテゴリーです。妥協のない映像美と、女優たちの魂の熱演が生み出す極上の時間を余すところなく紐解きます。
    </p>

    <h2 class="text-2xl font-bold text-red-400 border-l-4 border-red-500 pl-4 my-8">
        2. 【厳選】絶対に外さない最高峰おすすめ神作ランキングTOP5
    </h2>
    <p class="text-gray-300 leading-relaxed mb-6">
        FANZA公式APIからリアルタイムで取得したデータをもとに、今最も勢いのある最高傑作をランキング形式で詳しく解説します。
    </p>

    {items_html}

    <h2 class="text-2xl font-bold text-red-400 border-l-4 border-red-500 pl-4 my-8">
        3. 最高峰の視聴環境構築と満足度を最大化するテクニック
    </h2>
    <p class="text-gray-300 leading-relaxed mb-4">
        作品が持つ魅力を100%味わい尽くすためには、視聴する環境のアップデートが不可欠です。高画質・高音質ストリーミングの活用や、大画面モニター、高品質なヘッドホンを用いることで、女優の吐息や細かな表情の機微まで生々しく体感することができます。
    </p>

    <h2 class="text-2xl font-bold text-red-400 border-l-4 border-red-500 pl-4 my-8">
        4. よくあるご質問（FAQ）
    </h2>
    <div class="space-y-4 text-gray-300 mb-8">
        <div class="bg-gray-800 p-4 rounded-xl border border-gray-700">
            <h3 class="font-bold text-white mb-2">Q. 紹介されている作品はすぐに視聴可能ですか？</h3>
            <p class="text-sm">A. はい。すべての作品はFANZAのデジタル配信に対応しており、購入後即座に高画質ストリーミングおよびダウンロード視聴が可能です。</p>
        </div>
        <div class="bg-gray-800 p-4 rounded-xl border border-gray-700">
            <h3 class="font-bold text-white mb-2">Q. スマートフォンやPCでも快適に楽しめますか？</h3>
            <p class="text-sm">A. はい。iPhone、Android、PC、タブレットなどあらゆるデバイスから専用アプリやブラウザでスムーズにご視聴いただけます。</p>
        </div>
    </div>

    <div class="mt-12 pt-6 border-t border-gray-800 text-sm text-gray-400">
        <p class="font-bold text-white mb-3">🔗 関連おすすめ特集記事（内部リンク）</p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 mb-6">
            {other_links_html}
        </div>
        <p class="font-bold text-white mb-3">📂 サイト内ハブ・総合案内</p>
        <div class="flex flex-wrap gap-3">
            <a href="/features" class="bg-gray-800 hover:bg-red-900/50 text-red-400 px-4 py-2 rounded-lg border border-gray-700 transition-colors">🔥 特集記事一覧に戻る</a>
            <a href="/ranking" class="bg-gray-800 hover:bg-red-900/50 text-red-400 px-4 py-2 rounded-lg border border-gray-700 transition-colors">🏆 最新ランキングを見る</a>
            <a href="/genre" class="bg-gray-800 hover:bg-red-900/50 text-red-400 px-4 py-2 rounded-lg border border-gray-700 transition-colors">📂 ジャンル別作品一覧</a>
        </div>
    </div>
    """
    return body

def main():
    themes = [
        {
            "id": "feature_busty_dynamite_paizuri_2026",
            "title": "【爆乳・極上パイズリ特化】圧倒的なボリュームと柔らかさを誇る巨乳美女たちの骨抜き密着ピストンおすすめ神作ランキングTOP5【2026年最新】",
            "keyword": "爆乳 パイズリ",
            "description": "男性の夢をすべて詰め込んだ究極の爆乳・パイズリ特化特集。圧倒的なバストのボリュームと吸い付くような柔らかさ、そして激しい密着ピストンで理性が完全に崩壊する神作トップ5を徹底解説。",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "genres": ["爆乳", "パイズリ", "巨乳", "豊満", "密着", "ピストン", "極上", "フェチ"]
        },
        {
            "id": "feature_amateur_raw_creampie_nanpa_2026",
            "title": "【素人ナンパ・生ハメリアルドキュメント】街頭のリアルな美女たちがカメラの前で本能を解放する禁断の生中出しおすすめ神作ランキングTOP5【2026年最新】",
            "keyword": "素人 ナンパ",
            "description": "仕込みなしのリアルな素人ナンパ＆ドキュメント作品群。普段は清楚な一般女性たちが、カメラの前で徐々に本能を剥き出しにし、濃厚な生ハメ・中出しに溺れていく背徳のドキュメンタリーを徹底解説。",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "genres": ["素人", "ナンパ", "生ハメ", "中出し", "ドキュメント", "リアル", "密着", "ハメ撮り"]
        },
        {
            "id": "feature_uraaka_offpako_secret_encounter_2026",
            "title": "【裏アカ女子・オフパコ秘密の逢瀬】SNSの裏アカウントで繋がった現代的リアル美女たちの淫らな密会おすすめ神作ランキングTOP5【2026年最新】",
            "keyword": "裏アカ オフパコ",
            "description": "現代の恋愛・性事情を象徴する裏アカウント女子・オフパコ文化にスポットを当てた最新トレンド特集。SNSで知り合ったリアルな美女たちが、ホテルの一室で見せる大胆すぎる淫らな姿と濃厚な絡みを徹底解説。",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "genres": ["裏アカ", "オフパコ", "SNS", "密会", "現代", "リアル", "ホテル", "濃厚"]
        }
    ]

    posts_dir = "/Users/calro/Downloads/blogger-er/src/data/posts"
    os.makedirs(posts_dir, exist_ok=True)

    # Prepare metadata list for cross-linking
    other_list = [{"id": t["id"], "title": t["title"]} for t in themes]

    for i, theme in enumerate(themes):
        print(f"\n--- テーマ生成中 ({i+1}/3): {theme['title']} ---")
        items = fetch_fanza_items(theme["keyword"], hits=5)
        print(f"API取得作品数: {len(items)}")

        # Exclude current article from cross-links
        current_others = [o for o in other_list if o["id"] != theme["id"]]

        body_html = generate_article_content(theme["title"], theme["keyword"], items, theme["description"], current_others)

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
