# -*- coding: utf-8 -*-
"""
FANZAキラー特集生成スクリプト v44
- 徹底的にAI臭さを排したプロの編集長視点の超高密度レビュー
- 3000文字以上の圧倒的ボリュームとSEO・GEO・LLM完全最適化
- 都度FANZA APIを叩いて最新かつ購買率の極めて高い人気作品データを取得
- 内部リンクおよび適切なAPI画像・アフィリエイトリンクの埋め込み
"""

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
        res = requests.get(url, params=params)
        data = res.json()
        items = data.get("result", {}).get("items", [])
        return items
    except Exception as e:
        print(f"FANZA API Error for keyword '{keyword}': {e}")
        return []

def main():
    print("=== FANZA API連携 3大キラー特集記事自動生成 (v44) 開始 ===")
    
    themes = [
        {
            "id": "feature_tower_mansion_ntr_confinement_2026",
            "title": "【タワーマンション監禁NTR】夫の目の前で犯される背徳の高級ラウンジ・極上人妻調教おすすめ神作ランキングTOP5【2026年最新】",
            "hinban": "feature_tower_mansion_ntr_confinement_2026",
            "keyword": "タワーマンション 人妻 NTR",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "genres": ["タワーマンション", "NTR", "人妻", "監禁", "高級", "背徳", "寝取られ", "高級ラウンジ"]
        },
        {
            "id": "feature_office_overtime_secret_sex_2026",
            "title": "【終電逃しの深夜オフィス密着】上司と2人きりの残業隠れで理性が崩壊する極上ハメ狂いおすすめ神作ランキングTOP5【2026年最新】",
            "hinban": "feature_office_overtime_secret_sex_2026",
            "keyword": "オフィス 残業 密着",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "genres": ["オフィス", "残業", "OL", "上司", "密室", "背徳", "社内恋愛", "パンスト"]
        },
        {
            "id": "feature_vr_immersive_oil_massage_2026",
            "title": "【VR没入感・極上オイルマッサージ】全身ヌルヌル密着で理性粉砕される痙攣トランス絶頂おすすめ神作ランキングTOP5【2026年最新】",
            "hinban": "feature_vr_immersive_oil_massage_2026",
            "keyword": "オイルマッサージ VR 没入感",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "genres": ["VR", "オイルマッサージ", "ヌルヌル", "密着", "トランス", "絶頂", "痙攣", "エステ"]
        }
    ]

    posts_dir = "/Users/calro/Downloads/blogger-er/src/data/posts"
    os.makedirs(posts_dir, exist_ok=True)

    for theme in themes:
        print(f"\n--- テーマ生成中: {theme['title']} ---")
        items = fetch_fanza_items(theme["keyword"], hits=5)
        print(f"API取得作品数: {len(items)}")

        formatted_items = []
        for idx, item in enumerate(items, 1):
            cid = item.get("content_id")
            title = item.get("title")
            affiliate_url = item.get("affiliateURL") or item.get("URL")
            prices = item.get("prices", {})
            price = prices.get("price") or "3,980円"
            
            image_url = ""
            image_info = item.get("imageURL", {})
            if isinstance(image_info, dict):
                image_url = image_info.get("large") or image_info.get("list") or ""
            
            actresses = [a.get("name") for a in item.get("iteminfo", {}).get("actress", [])]
            maker = item.get("iteminfo", {}).get("maker", [{}])[0].get("name", "有名メーカー")

            formatted_items.append({
                "cid": cid,
                "rank": idx,
                "title": title,
                "affiliate_url": affiliate_url,
                "price": price,
                "image_url": image_url,
                "actresses": actresses,
                "maker": maker
            })

        html_content = f"""
<div class="space-y-8 text-slate-200">
  <div class="bg-gradient-to-r from-rose-950/80 via-slate-900 to-slate-900 border border-rose-500/30 rounded-3xl p-6 md:p-10 shadow-2xl">
    <div class="inline-flex items-center gap-2 bg-rose-500/20 text-rose-300 px-4 py-1.5 rounded-full text-xs font-bold mb-4">
      <span>🔥 FANZA API直結・最新厳選ランキング</span>
      <span>•</span>
      <span>2026年最新トレンド</span>
    </div>
    <h1 class="text-2xl md:text-4xl font-black text-white tracking-tight leading-snug mb-4">
      {theme['title']}
    </h1>
    <p class="text-sm md:text-base text-slate-300 leading-relaxed">
      成人向けエンターテインメント市場において、最もユーザーの購買意欲を刺激し、リピート率・満足度が極めて高い「{theme['keyword']}」をテーマに、FANZA公式APIからリアルタイムで厳選された至高の傑作TOP5を徹底解剖します。単なるアダルト動画の紹介にとどまらず、心理描写のリアリティ、女優の演技力、カメラワークの臨場感、そして脳科学적・フェティシズム的観点からなぜこの作品群がこれほどまでに支持を集めるのかをプロの視点で徹底解説。今夜あなたが生涯の満足を得るための決定版ガイドです。
    </p>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-4">
    <h2 class="text-xl font-bold text-white flex items-center gap-2">
      <span class="text-rose-500">📌</span> 本特集で取り上げるシチュエーションの魅力と購買ポイント
    </h2>
    <p class="text-sm md:text-base text-slate-300 leading-relaxed">
      現代のLLMやAI検索、検索エンジンの高精度化に伴い、ユーザーが真に求める情報は「ありきたりなキーワードの羅列」ではなく、「なぜそのシチュエーションが興奮を生むのか」という深い文脈とリアリティです。当サイトでは、FANZA APIの最新ランキングデータを基に、実際に数千・数万のユーザーが購入し絶賛した作品のみを厳選。背徳感、スリル、そして極限の密着が生み出す官能のドラマを余すところなくお届けします。
    </p>
    <div class="flex flex-wrap gap-2 pt-2">
"""
        for g in theme["genres"]:
            html_content += f'      <span class="bg-slate-800 border border-slate-700 text-rose-300 px-3 py-1 rounded-full text-xs font-semibold">#{g}</span>\n'

        html_content += f"""
    </div>
  </div>

  <div class="space-y-12">
"""

        for item in formatted_items:
            html_content += f"""
    <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-6">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-800 pb-4">
        <div class="flex items-center gap-3">
          <span class="flex items-center justify-center w-10 h-10 rounded-2xl bg-gradient-to-br from-rose-500 to-pink-600 text-white font-black text-lg shadow-lg">
            {item['rank']}
          </span>
          <div>
            <span class="text-xs font-bold text-rose-400 uppercase tracking-wider">{item['maker']}</span>
            <div class="text-xs text-slate-400">品番/CID: {item['cid']}</div>
          </div>
        </div>
        <div class="inline-flex items-center gap-2 bg-slate-800 px-4 py-2 rounded-2xl text-sm font-bold text-amber-400">
          <span>💰 価格: {item['price']}</span>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
        <div class="lg:col-span-5">
          <div class="relative rounded-2xl overflow-hidden border border-slate-700 shadow-2xl group">
            <img src="{item['image_url']}" alt="{item['title']}" class="w-full h-auto object-cover transform group-hover:scale-105 transition duration-500" />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition duration-300 flex items-end p-4">
              <span class="text-xs text-white font-medium">FANZA公式高画質サンプル画像</span>
            </div>
          </div>
        </div>
        
        <div class="lg:col-span-7 space-y-4">
          <h3 class="text-lg md:text-xl font-bold text-white leading-snug hover:text-rose-400 transition">
            {item['title']}
          </h3>
          
          <div class="flex flex-wrap gap-1.5">
"""
            for act in item["actresses"]:
                html_content += f'            <span class="bg-rose-950/50 border border-rose-800/50 text-rose-200 px-2.5 py-0.5 rounded-lg text-xs font-medium">出演: {act}</span>\n'

            html_content += f"""
          </div>

          <p class="text-sm text-slate-300 leading-relaxed">
            【プロ編集長による作品インプレッション】本作は、{theme['keyword']}ジャンルにおける金字塔的作品です。緻密に練られたシチュエーション設定はもちろんのこと、女優の息遣いから微細な表情の変化まで余すところなく捉えたカメラワークが圧巻。視聴者の没入感を限界まで高め、何度繰り返しても色褪せない極上のカタルシスを提供してくれます。
          </p>

          <div class="pt-2">
            <a href="{item['affiliate_url']}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center gap-2 w-full md:w-auto px-6 py-3.5 bg-gradient-to-r from-rose-600 to-pink-600 hover:from-rose-500 hover:to-pink-500 text-white font-bold rounded-2xl shadow-lg transform hover:-translate-y-0.5 transition duration-200 text-sm">
              <span>🚀 FANZAで今すぐ詳細を見る（サンプル動画・高画質配信）</span>
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
            </a>
          </div>
        </div>
      </div>
    </div>
"""

        html_content += f"""
  </div>

  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-6">
    <h3 class="text-xl font-bold text-white">💡 関連記事・内部リンクによるさらなる深掘り</h3>
    <p class="text-sm text-slate-300 leading-relaxed">
      当サイトでは、本特集の他にも厳選された数々のプレミアム特集記事を公開しています。あなたの好みにぴったりのシチュエーションを見つけて、最高のエンターテインメント体験をお楽しみください。
    </p>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <a href="/posts/feature_sauna_rovryu_trans_infinity_sex_ranking_2026" class="block bg-slate-800/60 hover:bg-slate-800 border border-slate-700/60 p-4 rounded-2xl transition">
        <div class="text-xs text-rose-400 font-bold mb-1">🔥 人気急上昇特集</div>
        <div class="text-sm font-bold text-white">サウナ・ロウリュ後のトランス状態で行われる限界密着インフィニティSEX特集</div>
      </a>
      <a href="/posts/feature_matching_app" class="block bg-slate-800/60 hover:bg-slate-800 border border-slate-700/60 p-4 rounded-2xl transition">
        <div class="text-xs text-rose-400 font-bold mb-1">💬 定番人気特集</div>
        <div class="text-sm font-bold text-white">マッチングアプリで出会った清楚系お姉さんの裏の顔と密室ハメ狂い特集</div>
      </a>
    </div>
  </div>
</div>
"""

        main_image = formatted_items[0]["image_url"] if formatted_items and formatted_items[0]["image_url"] else ""
        first_aff_url = formatted_items[0]["affiliate_url"] if formatted_items and formatted_items[0]["affiliate_url"] else "https://www.dmm.co.jp/"

        post_data = {
            "id": theme["id"],
            "hinban": theme["hinban"],
            "title": theme["title"],
            "date": theme["date"],
            "genres": theme["genres"],
            "image": main_image,
            "affiliate_url": first_aff_url,
            "price": "3,980円~",
            "maker": "FANZA特選プレミアム",
            "review": html_content,
            "sample_images": [item["image_url"] for item in formatted_items if item["image_url"]]
        }

        file_path = os.path.join(posts_dir, f"{theme['id']}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(post_data, f, ensure_ascii=False, indent=2)
        print(f"保存完了: {file_path}")

    print("=== 全3記事の生成が完了しました ===")

if __name__ == "__main__":
    main()
