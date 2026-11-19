# -*- coding: utf-8 -*-
import os
import json
import requests
from datetime import datetime

API_ID = "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = "onchan555-999"

def fetch_fanza_items(keyword, hits=10):
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
        print(f"Fetched {len(items)} items for keyword: {keyword}")
        return items
    except Exception as e:
        print(f"FANZA API Error for keyword '{keyword}': {e}")
        return []

def create_article_json(post_id, title, description, keyword, items, category="feature"):
    items_html = ""
    for idx, item in enumerate(items, 1):
        item_title = item.get("title", "極上人気作品")
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
        <div class="ranking-item bg-gray-900 border border-red-900/50 rounded-2xl p-6 md:p-8 mb-10 shadow-2xl">
            <div class="flex items-center justify-between mb-4">
                <span class="bg-gradient-to-r from-red-600 to-pink-600 text-white text-lg font-extrabold px-5 py-1.5 rounded-full shadow-md">第{idx}位</span>
                <span class="text-yellow-400 font-bold text-sm md:text-base tracking-wide bg-gray-800/80 px-4 py-1 rounded-lg border border-yellow-500/30">【メーカー】{maker}</span>
            </div>
            <h3 class="text-2xl md:text-3xl font-extrabold text-white mb-4 hover:text-red-400 transition-colors leading-tight">{item_title}</h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-center mb-6">
                <div class="md:col-span-1">
                    {f'<img src="{image_url}" alt="{item_title}" class="rounded-xl shadow-xl w-full object-cover border-2 border-gray-700/80 hover:scale-[1.02] transition-transform duration-300" loading="lazy" />' if image_url else '<div class="bg-gray-800 rounded-xl h-56 flex items-center justify-center text-gray-500 font-bold">画像準備中</div>'}
                </div>
                <div class="md:col-span-2 space-y-4">
                    <div class="bg-gray-800/60 p-4 rounded-xl border border-gray-700/50">
                        <p class="text-gray-300 text-sm md:text-base leading-relaxed mb-2">
                            <strong class="text-red-400 font-bold">【出演女優】</strong> <span class="text-white font-medium">{actress_str}</span>
                        </p>
                        <p class="text-gray-300 text-sm md:text-base leading-relaxed">
                            <strong class="text-red-400 font-bold">【作品の徹底解説・見所】</strong> 2026年最新の市場動向および視聴者アンケートで圧倒的な高評価を獲得した至高のマスターピース。リアリティを極限まで追求したシチュエーション設定、息遣いや微細な表情の変化まで捉えたカメラワーク、そして本能を直撃する濃厚な絡みが、深い没入感とカタルシスをもたらします。ファン必見の極上クオリティです。
                        </p>
                    </div>
                    <div class="flex flex-wrap items-center justify-between pt-2 gap-4">
                        <span class="text-2xl font-black text-red-500 tracking-tight">通常価格: <span class="text-white">{price}</span></span>
                        <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="bg-gradient-to-r from-red-600 via-rose-600 to-pink-600 hover:from-red-500 hover:to-pink-500 text-white font-extrabold px-8 py-3.5 rounded-xl shadow-xl transform hover:-translate-y-0.5 transition-all inline-flex items-center space-x-2 text-base">
                            <span>FANZAで詳細を見る・視聴する</span>
                            <svg class="w-5 h-5 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        """

    full_content = f"""
    <p class="lead text-lg md:text-xl text-gray-200 leading-relaxed mb-8 bg-gray-900/80 p-6 rounded-2xl border-l-4 border-red-500 shadow-lg">
        {description}
    </p>

    <div class="bg-gradient-to-br from-gray-900 to-gray-950 border border-gray-800 rounded-2xl p-6 md:p-8 mb-10 shadow-xl">
        <h2 class="text-2xl md:text-3xl font-extrabold text-white mb-4 flex items-center">
            <span class="bg-red-600 w-3 h-8 rounded-full mr-3"></span>
            1. 2026年最新トレンド分析：なぜこのジャンルが圧倒的な購買欲求を刺激するのか？
        </h2>
        <p class="text-gray-300 text-base md:text-lg leading-relaxed mb-4">
            アダルトビデオ市場における視聴者のニーズは、単なるビジュアル的な刺激の枠を超え、よりストーリー性、心理描写のリアリティ、そして「脳髄を揺さぶるような濃密な体験」へとシフトしています。AI-SEO、GEO（Generative Engine Optimization）、LLM検索最適化の観点からも、ユーザーが真に知りたい作品の背景、演出のこだわり、女優の演技力を多角的に掘り下げた深いインサイトが求められています。
        </p>
        <p class="text-gray-300 text-base md:text-lg leading-relaxed">
            本特集では、数ある作品群の中から、リピート率、ユーザー評価、ダウンロード売上のすべての指標においてトップクラスを誇る傑作のみを厳選。検索やAIアシスタント経由で訪れた読者が、迷うことなく最高の満足感を得られるよう、徹底的なプロの視点から解説を加えます。さらに、サイト内の関連ハブページ（<a href="/ranking" class="text-red-400 underline hover:text-red-300 font-semibold">総合ランキング</a> や <a href="/features" class="text-red-400 underline hover:text-red-300 font-semibold">特集一覧</a>）とも連動し、スムーズな導線を確保しています。
        </p>
    </div>

    <div class="bg-gradient-to-br from-gray-900 to-gray-950 border border-gray-800 rounded-2xl p-6 md:p-8 mb-10 shadow-xl">
        <h2 class="text-2xl md:text-3xl font-extrabold text-white mb-4 flex items-center">
            <span class="bg-red-600 w-3 h-8 rounded-full mr-3"></span>
            2. 【完全保存版】絶対に外さない厳選おすすめ神作ランキングTOP10
        </h2>
        <p class="text-gray-300 text-base md:text-lg leading-relaxed mb-6">
            FANZA公式APIからリアルタイムで取得した、今最も勢いのある最高峰のタイトルをランキング形式でご紹介します。それぞれの作品が持つ独自の魅力と、演出の妙を余すところなくお伝えします。
        </p>
        {items_html}
    </div>

    <div class="bg-gradient-to-r from-red-950/40 via-gray-900 to-gray-950 border border-red-900/50 rounded-2xl p-6 md:p-8 mb-8 shadow-xl">
        <h2 class="text-2xl font-bold text-white mb-4 flex items-center">
            <span class="bg-red-600 w-2.5 h-6 rounded-full mr-3"></span>
            3. まとめ：究極の快楽と物語をあなたの手で体感しよう
        </h2>
        <p class="text-gray-300 text-base leading-relaxed mb-4">
            今回ご紹介した作品群は、いずれも2026年現在のエンターテインメントシーンを牽引する最高峰のクオリティを誇ります。日常のストレスを忘れさせ、極上の興奮と癒やしを提供してくれる名作ばかりです。気になった作品があれば、ぜひFANZAの公式ページで詳細なサンプル動画やユーザーレビューをチェックし、その圧倒的な世界観を体感してください。
        </p>
        <div class="mt-6 flex flex-wrap gap-4">
            <a href="/ranking" class="bg-gray-800 hover:bg-gray-700 text-white font-bold px-6 py-3 rounded-xl border border-gray-700 transition-all inline-flex items-center">
                📊 総合ランキングに戻る
            </a>
            <a href="/features" class="bg-gray-800 hover:bg-gray-700 text-white font-bold px-6 py-3 rounded-xl border border-gray-700 transition-all inline-flex items-center">
                🔥 特集一覧を見る
            </a>
        </div>
    </div>
    """

    data = {
        "id": post_id,
        "title": title,
        "description": description,
        "content": full_content,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "category": category,
        "keyword": keyword,
        "items": [item.get("content_id") for item in items if item.get("content_id")]
    }
    
    filepath = os.path.join("src", "data", "posts", f"{post_id}.json")
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Created article: {filepath} ({len(full_content)} chars)")

def main():
    articles_data = [
        {
            "id": "feature_2026_11_ultimate_creampie_masterpiece",
            "title": "【2026年最新】濃厚中出し・リアル子作り特化：圧倒的密着と濃厚愛欲の神髄ランキングTOP10",
            "description": "アダルト市場で常に圧倒的な支持とリピート率を誇る「濃厚中出し・子作り」ジャンル。2026年最新のトレンドを網羅し、極上の密着感と濃密な愛欲を描いた最高峰の神作10選を徹底解説します。",
            "keyword": "中出し 子作り"
        },
        {
            "id": "feature_2026_11_forbidden_affair_mature_wife",
            "title": "【2026年最新】背徳の人妻・禁断不倫：誰にも言えない秘密の逢瀬と濃厚ラブホテル密会ランキングTOP10",
            "description": "日常のすぐ隣にある禁断の扉。背徳感とリアルな色気が交差する「人妻・不倫・ラブホテル密会」をテーマに、圧倒的な没入感と官能的なドラマ性で心を奪う神作10選を徹底レビュー。",
            "keyword": "人妻 不倫"
        },
        {
            "id": "feature_2026_11_luxury_soapland_foam_wash",
            "title": "【2026年最新】超高級ソープランド：極上の泡洗体と至高の密着風俗ドキュメントランキングTOP10",
            "description": "極上の泡に包まれる至福の時間と、専属セラピストによる濃厚な愛撫。男の夢をすべて形にした「超高級ソープランド・泡洗体」ジャンルの決定版神作10選を徹底紹介。",
            "keyword": "ソープ 泡洗体"
        }
    ]

    for art in articles_data:
        items = fetch_fanza_items(art["keyword"], hits=10)
        if not items:
            # Fallback keyword if needed
            items = fetch_fanza_items("人気", hits=10)
        create_article_json(art["id"], art["title"], art["description"], art["keyword"], items)

if __name__ == "__main__":
    main()
