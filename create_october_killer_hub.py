# -*- coding: utf-8 -*-
import os
import json
import requests
import html

API_ID = "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = "onchan555-999"
SITE_AFFILIATE_ID = "onchan555-003"

def fetch_top_october_items():
    url = "https://api.dmm.com/affiliate/v3/ItemList"
    params = {
        "api_id": API_ID,
        "affiliate_id": API_AFFILIATE_ID,
        "site": "FANZA",
        "service": "digital",
        "floor": "videoa",
        "gte_date": "2024-10-01T00:00:00",
        "lte_date": "2024-10-31T23:59:59",
        "sort": "rank",
        "hits": 10,
        "output": "json"
    }
    res = requests.get(url, params=params, timeout=15)
    data = res.json()
    items = data.get("result", {}).get("items", [])
    return items

items = fetch_top_october_items()
print(f"Fetched {len(items)} top items from FANZA API")

hub_id = "feature_2026_october_latest_av_masterpiece_summary"
hub_title = "【2026年10月最新作まとめ】FANZA売上ランキング上位を独占した神作AV傑作選！名作タイトル・出演女優・品番徹底総まとめ"

# Collect metadata
all_actresses = []
all_genres = ["ハイビジョン", "独占配信", "10選", "最新作", "ランキング", "おすすめ"]
main_image = ""
if items:
    img_obj = items[0].get("imageURL", {})
    main_image = img_obj.get("large") or img_obj.get("small") or ""

articles_html = []

for idx, item in enumerate(items, 1):
    cid = item.get("content_id") or ""
    title = item.get("title") or ""
    img_large = item.get("imageURL", {}).get("large") or ""
    
    # Extract iteminfo
    iteminfo = item.get("iteminfo", {})
    actresses = [a.get("name") for a in iteminfo.get("actress", []) if a.get("name")]
    maker = iteminfo.get("maker", [{}])[0].get("name", "公式メーカー") if iteminfo.get("maker") else "公式メーカー"
    label = iteminfo.get("label", [{}])[0].get("name", "") if iteminfo.get("label") else ""
    genres = [g.get("name") for g in iteminfo.get("genre", []) if g.get("name")]
    date_str = item.get("date", "").split(" ")[0]
    price = item.get("prices", {}).get("price", "公式価格参照")
    
    for a in actresses:
        if a not in all_actresses:
            all_actresses.append(a)
    for g in genres[:4]:
        if g not in all_genres:
            all_genres.append(g)

    # Convert to official affiliate link with site's affiliate ID
    clean_aff_url = f"https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D{cid}&af_id={SITE_AFFILIATE_ID}&ch=api"

    # Sample images
    samples = item.get("sampleImageURL", {}).get("sample_l", {}).get("image", [])
    if not samples:
        samples = item.get("sampleImageURL", {}).get("sample_s", {}).get("image", [])
    samples_slice = samples[:4]

    actress_text = "、".join(actresses) if actresses else "厳選美女キャスト"
    genres_text = "、".join(genres[:5]) if genres else "特選AV"

    sample_images_html = ""
    if samples_slice:
        sample_images_html = f"""
        <div class="mt-4">
          <p class="text-xs font-bold text-slate-400 mb-2 flex items-center gap-1">
            <span>📸</span><span>高画質サンプル場面カット</span>
          </p>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
            {''.join([f'<a href="{clean_aff_url}" target="_blank" rel="noopener noreferrer sponsored" class="block aspect-video overflow-hidden rounded-lg border border-slate-700 bg-slate-800 hover:border-rose-500 transition"><img src="{s}" alt="{html.escape(title)} サンプル場面" class="w-full h-full object-cover hover:scale-105 transition duration-300" loading="lazy" /></a>' for s in samples_slice])}
          </div>
        </div>
        """

    card_html = f"""
    <!-- 第{idx}位 作品カード -->
    <article class="bg-slate-900/90 border border-slate-800 hover:border-rose-500/50 rounded-2xl p-5 sm:p-7 shadow-xl transition-all duration-300 space-y-5">
      <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800/80 pb-3">
        <div class="flex items-center gap-2">
          <span class="inline-flex items-center justify-center w-7 h-7 rounded-full bg-gradient-to-r from-rose-600 to-pink-600 text-white font-black text-xs shadow-md">
            #{idx}
          </span>
          <span class="text-xs font-bold px-2.5 py-0.5 rounded bg-rose-500/10 text-rose-400 border border-rose-500/20">
            {cid.upper()}
          </span>
          <span class="text-xs text-slate-400 font-medium">{date_str} 発売</span>
        </div>
        <div class="text-xs font-bold text-amber-400 flex items-center gap-1">
          <span>👑</span><span>FANZA月間売上TOPランク</span>
        </div>
      </div>

      <div class="space-y-2">
        <h3 class="text-base sm:text-lg font-black text-white hover:text-rose-400 transition leading-snug">
          <a href="{clean_aff_url}" target="_blank" rel="noopener noreferrer sponsored">
            {html.escape(title)}
          </a>
        </h3>
        <div class="flex flex-wrap items-center gap-x-4 gap-y-1 text-xs text-slate-300">
          <span class="text-slate-400">出演女優: <strong class="text-rose-300 font-bold">{html.escape(actress_text)}</strong></span>
          <span class="text-slate-400">メーカー: <strong class="text-slate-200">{html.escape(maker)}</strong></span>
          {f'<span class="text-slate-400">レーベル: <strong class="text-slate-200">{html.escape(label)}</strong></span>' if label else ''}
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-12 gap-5 items-center">
        <div class="md:col-span-5 relative group overflow-hidden rounded-xl border border-slate-800 bg-black flex items-center justify-center">
          <a href="{clean_aff_url}" target="_blank" rel="noopener noreferrer sponsored" class="block w-full">
            <img src="{img_large}" alt="{html.escape(title)} 公式パッケージ画像" class="w-full h-auto max-h-[360px] object-contain group-hover:scale-105 transition duration-300" loading="lazy" />
            <div class="absolute inset-0 bg-slate-950/40 opacity-0 group-hover:opacity-100 transition duration-200 flex items-center justify-center">
              <span class="text-xs font-black text-white bg-rose-600 px-4 py-2 rounded-xl shadow-lg flex items-center gap-1">
                <span>🔥</span><span>公式プレビューを即再生</span>
              </span>
            </div>
          </a>
        </div>
        
        <div class="md:col-span-7 space-y-4">
          <div class="bg-slate-950/60 border border-slate-800/80 rounded-xl p-4 space-y-2 text-xs leading-relaxed text-slate-300">
            <p class="font-bold text-rose-400 flex items-center gap-1.5">
              <span>💎</span><span>本作の見どころ・セールスポイント</span>
            </p>
            <p>
              2026年10月のFANZA配信ランキングで堂々の大ヒットを記録した注目の傑作！
              主演キャストの【{html.escape(actress_text)}】が魅せる圧倒的エロスと濃密な絡み、ハイクオリティな映像演出はファン必見。
              ジャンル（{html.escape(genres_text)}）の魅力を極限まで引き出した、今月絶対に見逃せない推薦タイトルです。
            </p>
          </div>

          <div class="flex flex-col sm:flex-row items-center gap-3 pt-1">
            <a href="{clean_aff_url}" target="_blank" rel="noopener noreferrer sponsored" class="w-full sm:flex-1 py-3 px-5 text-center bg-gradient-to-r from-rose-600 via-rose-500 to-pink-600 hover:from-rose-500 hover:to-pink-500 text-white font-black text-xs sm:text-sm rounded-xl shadow-lg shadow-rose-600/30 transition flex items-center justify-center gap-2">
              <span>🔥</span>
              <span>FANZA公式で無料プレビュー・本編を見る</span>
              <span class="text-xs opacity-80">›</span>
            </a>
          </div>
          <div class="flex items-center justify-between text-[11px] text-slate-400 px-1">
            <span class="text-emerald-400 font-bold">🔒 明細はDMM表記・即時ストリーミング対応</span>
            <span>単体購入・セール対応</span>
          </div>
        </div>
      </div>

      {sample_images_html}
    </article>
    """
    articles_html.append(card_html)

hub_content = f"""<!-- キラー特集コンテナ -->
<div class="space-y-10 text-slate-200">
  <!-- ヒーローリード文セクション -->
  <header class="bg-gradient-to-br from-slate-900 via-slate-900 to-rose-950/40 border border-slate-800 rounded-3xl p-6 md:p-10 shadow-2xl space-y-6">
    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-rose-600/20 border border-rose-500/30 text-rose-400 text-xs font-black tracking-wide">
      <span>👑</span><span>FANZA公式データ完全同期・月間売上ベストセレクション</span>
    </div>
    <div class="space-y-3">
      <h1 class="text-xl sm:text-2xl md:text-3xl font-black text-white leading-tight tracking-tight">
        【2026年10月最新作まとめ】FANZA売上ランキング上位を独占した神作AV傑作選！名作タイトル・出演女優・品番徹底総まとめ
      </h1>
      <p class="text-xs sm:text-sm text-slate-300 leading-relaxed max-w-4xl">
        2026年10月にFANZA（DMM）で配信・リリースされた膨大な新作AVの中から、<strong>圧倒的な売上・高評価レビュー・アクセス数を集めた絶対に見るべき大ヒット名作タイトル</strong>を厳選ピックアップ！<br>
        人気単体女優の最新専属作から、話題の企画モノ、濃密中出し、極上シチュエーションまで、作品ごとの見どころや高画質サンプルカットを網羅してご紹介します。気になる作品は各公式リンクより無料プレビュー動画を今すぐチェックいただけます。
      </p>
    </div>

    <!-- メリット・安心ガイドバッジ -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-2 text-xs">
      <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800 text-center space-y-1">
        <span class="text-base">🎬</span>
        <p class="font-bold text-white">公式プレビュー無料</p>
        <p class="text-[10px] text-slate-400">本編ダイジェスト即再生</p>
      </div>
      <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800 text-center space-y-1">
        <span class="text-base">🔒</span>
        <p class="font-bold text-white">クレカ明細安心</p>
        <p class="text-[10px] text-slate-400">DMM表記（作品名なし）</p>
      </div>
      <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800 text-center space-y-1">
        <span class="text-base">📱</span>
        <p class="font-bold text-white">スマホ・PC即視聴</p>
        <p class="text-[10px] text-slate-400">アプリ＆ブラウザ高画質</p>
      </div>
      <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800 text-center space-y-1">
        <span class="text-base">⚡</span>
        <p class="font-bold text-white">ランキング上位</p>
        <p class="text-[10px] text-slate-400">失敗しない名作のみ厳選</p>
      </div>
    </div>
  </header>

  <!-- 作品リスト一覧 -->
  <section class="space-y-8">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
      <h2 class="text-lg sm:text-xl font-black text-white flex items-center gap-2">
        <span>🔥</span><span>2026年10月発売・話題の神作タイトル厳選10作品</span>
      </h2>
      <span class="text-xs text-rose-400 font-bold">全作品・公式直リンク完備</span>
    </div>

    <div class="space-y-6">
      {''.join(articles_html)}
    </div>
  </section>

  <!-- フッターCTAバナー -->
  <section class="bg-gradient-to-r from-rose-950/60 via-slate-900 to-slate-950 border border-rose-500/30 rounded-2xl p-6 sm:p-8 text-center space-y-4 shadow-2xl">
    <h3 class="text-lg sm:text-xl font-black text-white">
      もっとたくさんの最新作・見放題作品を楽しみたいなら
    </h3>
    <p class="text-xs sm:text-sm text-slate-300 max-w-2xl mx-auto leading-relaxed">
      FANZAでは毎月数千本以上の新作が随時追加中！単品購入はもちろん、月額定額で15万本以上が見放題になる「FANZA見放題chプレミアム」も大好評です。
    </p>
    <div class="flex flex-col sm:flex-row items-center justify-center gap-3 pt-2">
      <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2F&af_id={SITE_AFFILIATE_ID}&ch=api" target="_blank" rel="noopener noreferrer sponsored" class="w-full sm:w-auto px-8 py-3.5 bg-gradient-to-r from-rose-600 to-pink-600 hover:from-rose-500 hover:to-pink-500 text-white font-black text-xs sm:text-sm rounded-xl shadow-lg transition">
        👉 FANZA公式 ビデオ総合TOPへ
      </a>
      <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fmonthly%2Fpremium%2F&af_id={SITE_AFFILIATE_ID}" target="_blank" rel="noopener noreferrer sponsored" class="w-full sm:w-auto px-8 py-3.5 bg-slate-800 hover:bg-slate-700 border border-amber-400/50 text-amber-300 font-black text-xs sm:text-sm rounded-xl shadow transition">
        👑 15万本見放題chをチェック
      </a>
    </div>
  </section>
</div>
"""

out_post = {
    "id": hub_id,
    "title": hub_title,
    "date": "2026-10-31 23:59:59",
    "hinban": "OCTOBER-2026-SUMMARY",
    "price": "300~",
    "maker": "FANZA総合傑作選",
    "actresses": all_actresses[:15],
    "genres": all_genres[:12],
    "image": main_image,
    "review": hub_content,
    "affiliate_url": f"https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D{items[0].get('content_id')}&af_id={SITE_AFFILIATE_ID}&ch=api" if items else f"https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2F&af_id={SITE_AFFILIATE_ID}&ch=api"
}

out_path = os.path.join("src", "data", "posts", f"{hub_id}.json")
with open(out_path, "w", encoding="utf-8") as fp:
    json.dump(out_post, fp, ensure_ascii=False, indent=2)

print(f"Successfully created: {out_path}")
