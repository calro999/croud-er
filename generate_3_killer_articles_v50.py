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
        <div class="ranking-item bg-gray-900 border border-red-900/60 rounded-xl p-6 mb-8 shadow-2xl">
            <div class="flex items-center justify-between mb-4">
                <span class="bg-gradient-to-r from-red-600 to-pink-600 text-white text-lg font-extrabold px-4 py-1.5 rounded-full shadow-md">第{idx}位</span>
                <span class="text-yellow-400 font-bold text-sm bg-gray-800 px-3 py-1 rounded-md border border-gray-700">【メーカー】{maker}</span>
            </div>
            <h3 class="text-2xl font-bold text-white mb-4 hover:text-red-400 transition-colors leading-snug">{title}</h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-center mb-6">
                <div class="md:col-span-1">
                    {f'<img src="{image_url}" alt="{title}" class="rounded-lg shadow-lg w-full object-cover border border-gray-700" loading="lazy" />' if image_url else '<div class="bg-gray-800 rounded-lg h-48 flex items-center justify-center text-gray-500">画像準備中</div>'}
                </div>
                <div class="md:col-span-2 space-y-3">
                    <p class="text-gray-300 text-base leading-relaxed">
                        <strong class="text-red-400 font-semibold">【出演女優】</strong> {actress_str}<br><br>
                        <strong class="text-red-400 font-semibold">【徹底解説・見所】</strong> {actress_str}の圧倒的な表現力とリアルな表情の揺れ動きが完璧に収められた至高の神作。細部までこだわり抜いた演出と濃厚な絡みが織りなす圧倒的な没入感は、多くのファンを魅了し続けています。心理描写のリアリティと官能的な映像美が最高潮に達する瞬間をぜひご堪能ください。
                    </p>
                    <div class="flex flex-wrap items-center justify-between pt-4 border-t border-gray-800">
                        <span class="text-xl font-extrabold text-red-500 mb-2 md:mb-0">参考価格: {price}</span>
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
        other_links_html += f'<a href="/posts/{oa["id"]}" class="bg-gray-800 hover:bg-red-900/40 text-red-400 px-4 py-3 rounded-xl border border-gray-700 transition-all block font-medium shadow-sm">📌 {oa["title"]}</a>'

    body = f"""
    <div class="post-content-inner space-y-8 text-gray-200 text-lg leading-relaxed">
        <p class="lead text-xl text-gray-100 font-medium leading-relaxed bg-gray-900/80 p-6 rounded-2xl border border-red-900/40 shadow-inner">
            {description_text}
        </p>

        <section class="space-y-4">
            <h2 class="text-3xl font-bold text-red-400 border-l-4 border-red-500 pl-4 py-1">
                1. 2026年最新トレンド分析：なぜこのジャンルが圧倒的な支持と中毒性を誇るのか？
            </h2>
            <p class="text-gray-300 leading-relaxed">
                アダルトエンターテインメント市場において、ユーザーが真に求めるのは「単なる一時的な刺激」を超えた「心理的リアリティ」と「圧倒的な没入感」です。本記事では、高度なAI-SEO、GEO（Generative Engine Optimization）、およびLLM検索最適化を徹底的に網羅し、検索エンジンや対話型AIアシスタント経由で訪れた読者が一目で納得できる、深みのある分析と厳選レビューをお届けします。
            </p>
            <p class="text-gray-300 leading-relaxed">
                特に今回焦点を当てるカテゴリーは、リピート率、ユーザー満足度、購買意欲のすべてにおいてトップクラスの数値を叩き出している極上のジャンルです。妥協のない映像美と、女優たちの魂の熱演が生み出す極上の時間を余すところなく紐解きます。
            </p>
        </section>

        <section class="space-y-6">
            <h2 class="text-3xl font-bold text-red-400 border-l-4 border-red-500 pl-4 py-1">
                2. 【厳選】絶対に外さない最高峰おすすめ神作ランキングTOP5
            </h2>
            <p class="text-gray-300 leading-relaxed">
                FANZA公式APIからリアルタイムで取得したデータをもとに、今最も勢いのある最高傑作をランキング形式で詳しく解説します。それぞれの作品が持つ独自の魅力や、見逃せないハイライトを余すところなくお伝えします。
            </p>

            {items_html}
        </section>

        <section class="space-y-4">
            <h2 class="text-3xl font-bold text-red-400 border-l-4 border-red-500 pl-4 py-1">
                3. 最高峰の視聴環境構築と満足度を最大化するテクニック
            </h2>
            <p class="text-gray-300 leading-relaxed">
                作品が持つ魅力を100%味わい尽くすためには、視聴する環境のアップデートが不可欠です。高画質・高音質ストリーミングの活用や、大画面モニター、高品質なヘッドホンを用いることで、女優の吐息や細かな表情の機微まで生々しく体感することができます。さらに、ナイトタイムのプライベートな空間を演出することで、極上の没入感を味わうことが可能です。
            </p>
        </section>

        <section class="space-y-4">
            <h2 class="text-3xl font-bold text-red-400 border-l-4 border-red-500 pl-4 py-1">
                4. よくあるご質問（FAQ）
            </h2>
            <div class="space-y-4 text-gray-300">
                <div class="bg-gray-900 p-5 rounded-xl border border-gray-800 shadow-md">
                    <h3 class="font-bold text-white text-lg mb-2">Q. 紹介されている作品はすぐに視聴可能ですか？</h3>
                    <p class="text-sm leading-relaxed">A. はい。すべての作品はFANZAのデジタル配信に対応しており、購入後即座に高画質ストリーミングおよびダウンロード視聴が可能です。</p>
                </div>
                <div class="bg-gray-900 p-5 rounded-xl border border-gray-800 shadow-md">
                    <h3 class="font-bold text-white text-lg mb-2">Q. スマートフォンやPCでも快適に楽しめますか？</h3>
                    <p class="text-sm leading-relaxed">A. はい。iPhone、Android、PC、タブレットなどあらゆるデバイスから専用アプリやブラウザでスムーズにご視聴いただけます。</p>
                </div>
            </div>
        </section>

        <div class="mt-16 pt-8 border-t border-gray-800 space-y-6">
            <div>
                <p class="font-bold text-white text-lg mb-4 flex items-center">
                    <span class="mr-2">🔗</span> 関連おすすめ特集記事（内部リンク）
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {other_links_html}
                </div>
            </div>

            <div class="pt-4">
                <p class="font-bold text-white text-lg mb-4 flex items-center">
                    <span class="mr-2">📂</span> サイト内ハブ・総合案内
                </p>
                <div class="flex flex-wrap gap-3">
                    <a href="/features" class="bg-gray-800 hover:bg-red-900/50 text-red-400 px-5 py-3 rounded-xl border border-gray-700 transition-all font-medium shadow-sm">🔥 特集記事一覧に戻る</a>
                    <a href="/ranking" class="bg-gray-800 hover:bg-red-900/50 text-red-400 px-5 py-3 rounded-xl border border-gray-700 transition-all font-medium shadow-sm">🏆 最新ランキングを見る</a>
                    <a href="/genre" class="bg-gray-800 hover:bg-red-900/50 text-red-400 px-5 py-3 rounded-xl border border-gray-700 transition-all font-medium shadow-sm">📂 ジャンル別作品一覧</a>
                </div>
            </div>
        </div>
    </div>
    """
    return body

def main():
    themes = [
        {
            "id": "feature_neighbor_wife_ntr_secret_2026",
            "title": "【人妻・寝取り特化】隣人の美熟女・人妻との背徳の密会と理性が崩壊するNTR中出しおすすめ神作ランキングTOP5【2026年最新】",
            "keyword": "人妻 寝取り NTR",
            "description": "日常のすぐ隣に潜む甘美な背徳感。隣家の美しい人妻や若奥様と秘密裏に交わす禁断の密会から、理性が音を立てて崩壊していくNTR・中出しの極致を描いたおすすめ神作トップ5を徹底解説。",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "genres": ["人妻", "寝取り", "NTR", "熟女", "近親相姦", "背徳", "密会", "中出し"]
        },
        {
            "id": "feature_schoolgirl_cosplay_uniform_2026",
            "title": "【制服・現役女子校生コスプレ特化】甘酸っぱい青春の狂宴と恥じらいの濃厚ピストンおすすめ神作ランキングTOP5【2026年最新】",
            "keyword": "制服 女子校生 コスプレ",
            "description": "誰もが一度は憧れる青春の甘酸っぱさと、背徳的なエロスが融合した制服・女子校生コスプレ特化特集。純朴なルックスとは裏腹に、激しい密着ピストンに溺れていく圧倒的興奮の神作トップ5を徹底解説。",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "genres": ["制服", "女子校生", "コスプレ", "学生", "ピストン", "青春", "純愛", "フェチ"]
        },
        {
            "id": "feature_amateur_hamedori_real_document_2026",
            "title": "【素人・ハメ撮りリアルドキュメント特化】カメラの前で恥じらいながらも快楽に溺れていく禁断の生中出しおすすめ神作ランキングTOP5【2026年最新】",
            "keyword": "ハメ撮り 素人",
            "description": "作り込まれていない圧倒的なリアリティと生々しい熱気がたまらない素人ハメ撮りドキュメント特化特集。カメラの前で徐々に理性を失い、快楽に身を委ねていく一般女性たちの生々しい姿を描いた神作トップ5を徹底解説。",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "genres": ["素人", "ハメ撮り", "リアル", "ドキュメント", "中出し", "生ハメ", "密着", "プライベート"]
        }
    ]

    posts_dir = "/Users/calro/Downloads/blogger-er/src/data/posts"
    os.makedirs(posts_dir, exist_ok=True)

    other_list = [{"id": t["id"], "title": t["title"]} for t in themes]

    for i, theme in enumerate(themes):
        print(f"\n--- テーマ生成中 ({i+1}/3): {theme['title']} ---")
        items = fetch_fanza_items(theme["keyword"], hits=5)
        print(f"API取得作品数: {len(items)}")

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
