# -*- coding: utf-8 -*-
import os
import json
import requests
import html
from datetime import datetime

API_ID = "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = "onchan555-999"
SITE_AFFILIATE_ID = "onchan555-003"
POSTS_DIR = os.path.join("src", "data", "posts")
HUB_ID = "feature_2026_november_latest_av_masterpiece_summary"
HUB_FILE = os.path.join(POSTS_DIR, f"{HUB_ID}.json")

def fetch_latest_november_items(hits=5):
    url = "https://api.dmm.com/affiliate/v3/ItemList"
    params = {
        "api_id": API_ID,
        "affiliate_id": API_AFFILIATE_ID,
        "site": "FANZA",
        "service": "digital",
        "floor": "videoa",
        "sort": "date",
        "hits": hits,
        "output": "json"
    }
    res = requests.get(url, params=params, timeout=15)
    data = res.json()
    items = data.get("result", {}).get("items", [])
    if not items:
        # Fallback to recent top items
        params.pop("sort")
        params["sort"] = "rank"
        res = requests.get(url, params=params, timeout=15)
        data = res.json()
        items = data.get("result", {}).get("items", [])
    return items

def build_card_html(item, idx):
    cid = item.get("content_id") or ""
    title = item.get("title") or ""
    img_large = item.get("imageURL", {}).get("large") or ""
    iteminfo = item.get("iteminfo", {})
    actresses = [a.get("name") for a in iteminfo.get("actress", []) if a.get("name")]
    maker = iteminfo.get("maker", [{}])[0].get("name", "公式メーカー") if iteminfo.get("maker") else "公式メーカー"
    label = iteminfo.get("label", [{}])[0].get("name", "") if iteminfo.get("label") else ""
    genres = [g.get("name") for g in iteminfo.get("genre", []) if g.get("name")]
    date_str = item.get("date", "").split(" ")[0]
    
    clean_aff_url = f"https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D{cid}&af_id={SITE_AFFILIATE_ID}&ch=api"
    
    samples = item.get("sampleImageURL", {}).get("sample_l", {}).get("image", [])
    if not samples:
        samples = item.get("sampleImageURL", {}).get("sample_s", {}).get("image", [])
    samples_slice = samples[:4]

    actress_text = "、".join(actresses) if actresses else "人気女優・特選キャスト"
    genres_text = "、".join(genres[:5]) if genres else "新作AV"

    sample_images_html = ""
    if samples_slice:
        sample_images_html = f"""
        <div class="mt-4">
          <p class="text-xs font-bold text-slate-400 mb-2 flex items-center gap-1">
            <span>📸</span><span>高画質サンプル場面カット</span>
          </p>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
            {''.join([f'<a href="{clean_aff_url}" target="_blank" rel="noopener noreferrer sponsored" class="block aspect-video overflow-hidden rounded-lg border border-slate-700 bg-slate-800 hover:border-rose-500 transition"><img src="{s}" alt="{html.escape(title)} サンプル" class="w-full h-full object-cover hover:scale-105 transition duration-300" loading="lazy" /></a>' for s in samples_slice])}
          </div>
        </div>
        """

    return f"""
    <!-- 新作追加カード: {cid.upper()} -->
    <article class="bg-slate-900/90 border border-slate-800 hover:border-rose-500/50 rounded-2xl p-5 sm:p-7 shadow-xl transition-all duration-300 space-y-5">
      <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800/80 pb-3">
        <div class="flex items-center gap-2">
          <span class="inline-flex items-center justify-center w-7 h-7 rounded-full bg-gradient-to-r from-rose-600 to-pink-600 text-white font-black text-xs shadow-md">
            #{idx}
          </span>
          <span class="text-xs font-bold px-2.5 py-0.5 rounded bg-rose-500/10 text-rose-400 border border-rose-500/20">
            {cid.upper()}
          </span>
          <span class="text-xs text-slate-400 font-medium">{date_str} 配信</span>
        </div>
        <div class="text-xs font-bold text-rose-400 flex items-center gap-1">
          <span>🔥</span><span>2026年11月 最新リリース速報</span>
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
              <span>💎</span><span>本作の見どころ・レビューポイント</span>
            </p>
            <p>
              今月リリースされた最新注目タイトル！【{html.escape(actress_text)}】の圧倒的な存在感と濃密な絡み、高画質映像による臨場感は必見。
              ジャンル（{html.escape(genres_text)}）のファンなら絶対に押さえておきたい最新傑作です。
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

def init_or_update_hub():
    items = fetch_latest_november_items(hits=10)
    print(f"Fetched {len(items)} items for November hub")
    
    cards_html = [build_card_html(item, idx + 1) for idx, item in enumerate(items)]
    
    all_actresses = []
    for item in items:
        for a in item.get("iteminfo", {}).get("actress", []):
            name = a.get("name")
            if name and name not in all_actresses:
                all_actresses.append(name)

    main_image = items[0].get("imageURL", {}).get("large") if items else ""
    first_cid = items[0].get("content_id") if items else ""
    
    hub_title = "【2026年11月最新作まとめ】FANZA話題の新作AV毎日更新速報！名作タイトル・品番・出演女優徹底まとめ"

    hub_content = f"""<!-- キラー特集コンテナ -->
<div class="space-y-10 text-slate-200">
  <header class="bg-gradient-to-br from-slate-900 via-slate-900 to-rose-950/40 border border-slate-800 rounded-3xl p-6 md:p-10 shadow-2xl space-y-6">
    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-rose-600/20 border border-rose-500/30 text-rose-400 text-xs font-black tracking-wide">
      <span>🔥</span><span>FANZA公式API自動連携・2026年11月最新作デイリー更新中</span>
    </div>
    <div class="space-y-3">
      <h1 class="text-xl sm:text-2xl md:text-3xl font-black text-white leading-tight tracking-tight">
        【2026年11月最新作まとめ】FANZA話題の新作AV毎日更新速報！名作タイトル・品番・出演女優徹底まとめ
      </h1>
      <p class="text-xs sm:text-sm text-slate-300 leading-relaxed max-w-4xl">
        2026年11月にリリースされた注目の最新作AVを毎日リアルタイムに追記・更新中！<br>
        人気メーカー（S1、MOODYZ、アイデアポケット、マドンナ、SOD等）の専属単体女優の最新作から、話題の企画物・素人系まで、<strong>絶対に見逃せない傑作タイトルを品番・出演者・サンプルカット付きで総まとめ</strong>しています。全作品、公式リンクより無料プレビュー動画が即時視聴可能です。
      </p>
    </div>

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
        <p class="font-bold text-white">毎日自動追加</p>
        <p class="text-[10px] text-slate-400">最新リリースを最速網羅</p>
      </div>
    </div>
  </header>

  <section class="space-y-8">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
      <h2 class="text-lg sm:text-xl font-black text-white flex items-center gap-2">
        <span>🔥</span><span>2026年11月 最新リリース注目タイトル一覧</span>
      </h2>
      <span class="text-xs text-rose-400 font-bold">随時新着追加中</span>
    </div>

    <!-- NOVEMBER_CARDS_START -->
    <div class="space-y-6" id="november-cards-container">
      {''.join(cards_html)}
    </div>
    <!-- NOVEMBER_CARDS_END -->
  </section>

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

    post_data = {
        "id": HUB_ID,
        "title": hub_title,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "hinban": "NOVEMBER-2026-SUMMARY",
        "price": "300~",
        "maker": "FANZA最新作速報",
        "actresses": all_actresses[:15],
        "genres": ["ハイビジョン", "独占配信", "10選", "最新作", "ランキング", "おすすめ", "単体作品"],
        "image": main_image,
        "review": hub_content,
        "affiliate_url": f"https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D{first_cid}&af_id={SITE_AFFILIATE_ID}&ch=api" if first_cid else f"https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2F&af_id={SITE_AFFILIATE_ID}&ch=api"
    }

    with open(HUB_FILE, "w", encoding="utf-8") as fp:
        json.dump(post_data, fp, ensure_ascii=False, indent=2)

    print(f"Successfully generated/updated: {HUB_FILE}")

if __name__ == "__main__":
    init_or_update_hub()
