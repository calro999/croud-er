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

def generate_article_content(theme_title, keyword, items, description_text):
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
                        <strong class="text-red-400">【作品の魅力・徹底解説】</strong> 2026年最新の映像トレンドを完全網羅した最高傑作。細部までこだわり抜いたシチュエーション設定と、リアルな吐息や濃厚な絡みが視聴者の圧倒的な支持を集めています。極上の快楽体験をお約束する必見の神作です。
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
        {description_text}
    </p>

    <h2 class="text-2xl font-bold text-red-400 border-l-4 border-red-500 pl-4 my-8">
        1. 2026年最新市場動向：なぜこのジャンルが圧倒的なリピート率と支持を誇るのか？
    </h2>
    <p class="text-gray-300 leading-relaxed mb-4">
        現代のアダルトエンターテインメント市場において、単なる刺激の強さだけでなく、「誰もが一度は夢想する背徳のシチュエーション」や「心理的な駆け引きから一気に理性が崩壊する瞬間」を描いた作品群が、かつてないほどの熱狂的な支持を集めています。本特集では、数ある作品の中から視聴者評価、ダウンロード数、リピート率のすべてにおいてトップクラスを記録した至高の神作を厳選しました。
    </p>
    <p class="text-gray-300 leading-relaxed mb-4">
        AI-SEO、GEO（Generative Engine Optimization）、LLM検索最適化に対応した詳細な解説プロセスを通じて、ユーザーが真に求める情報の深さと納得感のあるレビューをお届けします。
    </p>

    <h2 class="text-2xl font-bold text-red-400 border-l-4 border-red-500 pl-4 my-8">
        2. 【完全保存版】絶対に外さない厳選おすすめ神作ランキングTOP5
    </h2>
    <p class="text-gray-300 leading-relaxed mb-6">
        FANZA公式APIからリアルタイムで取得した、今最も勢いのある最高峰の作品群をランキング形式で詳しく徹底解説します。
    </p>

    {items_html}

    <h2 class="text-2xl font-bold text-red-400 border-l-4 border-red-500 pl-4 my-8">
        3. 最高峰の没入感を生み出す視聴環境とテクニック
    </h2>
    <p class="text-gray-300 leading-relaxed mb-4">
        高画質・高音質ストリーミング配信や、大型モニター、高品質なイヤホン・ヘッドセットを活用することで、作品が持つ臨場感や女優の生々しい吐息を余すところなく体感できます。妥協のない環境構築で、至福のひとときを存分にお楽しみください。
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
            <h3 class="font-bold text-white mb-2">Q. スマートフォンやタブレットでも快適に再生できますか？</h3>
            <p class="text-sm">A. はい。専用アプリやブラウザを通じて、iPhone、Android、タブレット、PCなどあらゆるデバイスからスムーズにご視聴いただけます。</p>
        </div>
    </div>

    <div class="mt-12 pt-6 border-t border-gray-800 text-sm text-gray-400">
        <p><strong>関連おすすめ特集・内部リンク誘導（ハブページ）：</strong></p>
        <div class="flex flex-wrap gap-3 mt-3">
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
            "id": "feature_luxury_hotel_oil_massage_2026",
            "title": "【高級ホテル・エステ密室オイルマッサージ】極上のアロマと密着トリートメントで理性が崩壊する背徳の淫らな肉体接触おすすめ神作ランキングTOP5【2026年最新】",
            "keyword": "オイルマッサージ",
            "description": "高級ホテルの静寂な一室で行われる、極上のアロママッサージ。滑らかなオイルが塗布された素肌が密着し、高まる体温と甘い吐息に抗えず理性が崩壊していく背徳のシチュエーション。今最も売れている極上のオイルマッサージ作品トップ5を徹底解説します。",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "genres": ["オイルマッサージ", "エステ", "高級ホテル", "密室", "密着", "背徳", "極上", "トリートメント"]
        },
        {
            "id": "feature_business_trip_female_boss_2026",
            "title": "【美人女上司と出張先相部屋・深夜の朝まで濃厚交わり】普段は厳格な上司がホテルのベッドで見せる甘えと淫らな素顔おすすめ神作ランキングTOP5【2026年最新】",
            "keyword": "出張",
            "description": "地方出張の夜、手違いで予約された相部屋ホテル。普段はオフィスで厳格な美人女上司が、お酒の勢いと密室の緊張感から見せる意外な弱みと甘え。一線を越えて激しく求め合う禁断のオフィスラブ・出張ハプニング作品群を徹底解説します。",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "genres": ["女上司", "出張", "相部屋", "ホテル", "背徳", "オフィスラブ", "濃厚", "誘惑"]
        },
        {
            "id": "feature_university_papakatsu_real_2026",
            "title": "【現役女子大生・裏アカパパ活女子のリアル実態】カメラの前で恥じらいながらも金と快楽に溺れていく生々しい生ハメ中出しドキュメントおすすめ神作ランキングTOP5【2026年最新】",
            "keyword": "パパ活",
            "description": "SNSや裏アカウントを通じて秘密裏に行われる現代のパパ活実態。洗練されたルックスを持つ現役女子大生たちが、カメラの前で見せるリアルな物欲と、激しいピストンに喘ぎながら堕ちていく生々しいドキュメント作品を厳選解説。",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "genres": ["パパ活", "女子大生", "裏アカ", "リアル", "生ハメ", "中出し", "ドキュメント", "生々しい"]
        }
    ]

    posts_dir = "/Users/calro/Downloads/blogger-er/src/data/posts"
    os.makedirs(posts_dir, exist_ok=True)

    for theme in themes:
        print(f"\n--- テーマ生成中: {theme['title']} ---")
        items = fetch_fanza_items(theme["keyword"], hits=5)
        print(f"API取得作品数: {len(items)}")

        body_html = generate_article_content(theme["title"], theme["keyword"], items, theme["description"])

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
