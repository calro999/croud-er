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
                        <strong class="text-red-400">【作品の魅力・見どころ】</strong> 2026年最新の市場トレンドを完全に反映した最高峰のクオリティ。細やかな表情の変化から圧倒的な熱量まで、視聴者の期待を裏切らない濃厚な絡みとリアリティ溢れる演出が絶賛されている神作です。
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
        1. 2026年最新トレンド：なぜこのジャンルが圧倒的な支持とリピートを集めるのか？
    </h2>
    <p class="text-gray-300 leading-relaxed mb-4">
        近年のアダルト動画市場において、単なる誇張された演出ではなく「日常のすぐ隣にあるリアリティ」や「隠された衝動が暴走する瞬間」を描いた作品群が驚異的な人気を誇っています。本特集では、視聴者からの評価が特に高く、何度も見返したくなるような至高の作品群を徹底的に分析・厳選しました。
    </p>

    <h2 class="text-2xl font-bold text-red-400 border-l-4 border-red-500 pl-4 my-8">
        2. 【徹底比較】絶対に外さない厳選おすすめ神作ランキングTOP5
    </h2>
    <p class="text-gray-300 leading-relaxed mb-6">
        FANZA公式APIからリアルタイムで取得した、今最も売れている最高峰の作品群をランキング形式で詳しく解説します。
    </p>

    {items_html}

    <h2 class="text-2xl font-bold text-red-400 border-l-4 border-red-500 pl-4 my-8">
        3. 最大限に楽しむための視聴環境とデバイス選びのコツ
    </h2>
    <p class="text-gray-300 leading-relaxed mb-4">
        高画質・高音質ストリーミングや大画面デバイス、VRヘッドセット等を活用することで、作品への没入感を何倍にも高めることができます。ご自身の環境に合わせた最適な視聴方法で、至福のひとときを存分にお楽しみください。
    </p>

    <h2 class="text-2xl font-bold text-red-400 border-l-4 border-red-500 pl-4 my-8">
        4. よくあるご質問（FAQ）
    </h2>
    <div class="space-y-4 text-gray-300 mb-8">
        <div class="bg-gray-800 p-4 rounded-xl border border-gray-700">
            <h3 class="font-bold text-white mb-2">Q. 紹介されている作品はすぐに視聴できますか？</h3>
            <p class="text-sm">A. はい。すべての作品はFANZAのデジタル配信に対応しており、購入後即座に高画質でストリーミング・ダウンロード視聴が可能です。</p>
        </div>
        <div class="bg-gray-800 p-4 rounded-xl border border-gray-700">
            <h3 class="font-bold text-white mb-2">Q. スマホやタブレットでも快適に再生できますか？</h3>
            <p class="text-sm">A. はい。専用アプリやブラウザからスマートフォン、タブレット、PCなどあらゆるデバイスでスムーズにご視聴いただけます。</p>
        </div>
    </div>

    <div class="mt-12 pt-6 border-t border-gray-800 text-sm text-gray-400">
        <p><strong>関連おすすめ特集・内部リンク誘導：</strong></p>
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
            "id": "feature_uraaka_joshi_nama_pako_2026",
            "title": "【裏アカ女子・個人撮影の生ハメ解禁】フォロワー急増中の人気素人がカメラの前で見せるリアルな淫乱淫語・とろける中出しドキュメントおすすめ神作ランキングTOP5【2026年最新】",
            "keyword": "素人",
            "description": "SNSや裏アカウントで密かに話題を集めるリアルな一般女性・素人娘たちのリアルな生態を捉えた個人撮影ドキュメント。加工なしの生々しい色気と、カメラの前で徐々に理性が崩壊していく瞬間を収めた、今最も売れている神作トップ5を徹底解説します。",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "genres": ["素人", "裏アカ", "個人撮影", "中出し", "生ハメ", "リアル", "淫乱", "ドキュメント"]
        },
        {
            "id": "feature_luxury_celebrity_wife_affair_2026",
            "title": "【高級住宅街のセレブ若妻・昼顔不倫】旦那が留守の豪邸で欲求不満を爆発させる濃厚フェラ＆激ピストン快楽漬けおすすめ神作ランキングTOP5【2026年最新】",
            "keyword": "人妻",
            "description": "高級住宅街に暮らす上品で気品あふれるセレブ若妻たちが、夫の留守中に禁断の情事に溺れる背徳の不倫ドラマ。満たされない日々の裏に隠された激しい性欲と、濃厚な愛液にまみれて喘ぐ姿を余すところなく捉えた至高の作品群をご紹介します。",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "genres": ["人妻", "セレブ", "不倫", "昼顔", "高級住宅街", "背徳", "濃厚", "フェラ"]
        },
        {
            "id": "feature_slender_bikini_athlete_2026",
            "title": "【スレンダー美脚アスリート・密着指導】引き締まった極上ボディを徹底的に開発される淫らなパーソナルトレーニングおすすめ神作ランキングTOP5【2026年最新】",
            "keyword": "美脚",
            "description": "鍛え上げられたスレンダーな美脚とキュッと引き締まった極上ボディを持つアスリート・モデル系美女に対する密着マンツーマントレーニング。プライベートジムの密室で、限界まで追い詰められ快感に屈していく背徳のストーリー作品を厳選解説。",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "genres": ["美脚", "スレンダー", "アスリート", "トレーニング", "密着", "ジム", "開発", "快楽"]
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
