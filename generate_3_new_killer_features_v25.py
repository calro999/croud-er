# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・新規キラー特集3記事および個別作品15件自動生成スクリプト v25
各記事3500文字以上・完全独自書き下ろし・内部リンク網羅・SEO/LLM/GEO対策
1. 【高圧エリートが部下の巨根に屈服雌堕ち】美人女上司・キャリアウーマン・オフィス逆転主導権 特集（TOP5）
2. 【奇跡の8頭身とスラリと伸びる長い脚】長身美脚・スレンダーモデル体型・美脚立ちバック 特集（TOP5）
3. 【金と性の生々しい境界線と快楽漬けの身体】パパ活女子・ギャラ飲み・お小遣い援助交際 特集（TOP5）
"""

import os
import re
import json
import time
import urllib.parse
import subprocess
import requests

from reviews_feature_female_boss import REVIEWS_FEMALE_BOSS
from reviews_feature_beautiful_legs import REVIEWS_BEAUTIFUL_LEGS
from reviews_feature_sugar_daddy import REVIEWS_SUGAR_DADDY
from features_def_v25 import FEATURE_ARTICLES

API_ID = "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = "onchan555-999"
LINK_AFFILIATE_ID = "onchan555-003"
OUTPUT_DIR = "src/data/posts"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open("src/lib/slugs.json", "r", encoding="utf-8") as f:
    slugs_data = json.load(f)
actress_slugs = slugs_data.get("actresses", {})
genre_slugs = slugs_data.get("genres", {})

# 全15作品の個別レビュー辞書
ALL_REVIEWS = {}
ALL_REVIEWS.update(REVIEWS_FEMALE_BOSS)
ALL_REVIEWS.update(REVIEWS_BEAUTIFUL_LEGS)
ALL_REVIEWS.update(REVIEWS_SUGAR_DADDY)

def get_actress_link(name):
    if not name:
        return ""
    clean_name = re.sub(r'（[^）]+）', '', name).strip()
    slug = actress_slugs.get(name) or actress_slugs.get(clean_name)
    if slug:
        return f'<a href="/actress/{slug}" class="text-rose-400 hover:text-rose-300 underline font-bold transition">{name}</a>'
    encoded = urllib.parse.quote(name)
    return f'<a href="/actress/{encoded}" class="text-rose-400 hover:text-rose-300 underline font-bold transition">{name}</a>'

def get_genre_link(genre):
    if not genre:
        return ""
    slug = genre_slugs.get(genre)
    if slug:
        return f'<a href="/genre/{slug}" class="text-slate-300 hover:text-amber-300 bg-slate-800/80 hover:bg-slate-700/80 px-2.5 py-1 rounded-full text-xs font-medium border border-slate-700 transition">{genre}</a>'
    encoded = urllib.parse.quote(genre)
    return f'<a href="/genre/{encoded}" class="text-slate-300 hover:text-amber-300 bg-slate-800/80 hover:bg-slate-700/80 px-2.5 py-1 rounded-full text-xs font-medium border border-slate-700 transition">{genre}</a>'

def fetch_fanza_item(cid, service="digital"):
    url = "https://api.dmm.com/affiliate/v3/ItemList"
    params = {
        "api_id": API_ID,
        "affiliate_id": API_AFFILIATE_ID,
        "site": "FANZA",
        "service": service,
        "floor": "videoa",
        "cid": cid,
        "output": "json"
    }
    try:
        res = requests.get(url, params=params, timeout=15)
        if res.status_code == 200:
            items = res.json().get("result", {}).get("items", [])
            if items:
                item = items[0]
                aff_url = item.get("affiliateURL", "")
                if aff_url and LINK_AFFILIATE_ID:
                    aff_url = re.sub(r'af_id=[^&]+', f'af_id={LINK_AFFILIATE_ID}', aff_url)
                item["affiliate_url_clean"] = aff_url
                return item
    except Exception as e:
        print(f"Error fetching {cid}: {e}")
    return None

def count_japanese_chars(html):
    text = re.sub(r'<[^>]*>', '', html)
    text = re.sub(r'\s+', '', text)
    return len(text)

def get_sample_images(it, max_count=4):
    s_imgs = []
    sample_data = it.get("sampleImageURL", {})
    if sample_data:
        if "sample_l" in sample_data:
            s_imgs = sample_data["sample_l"].get("image", [])
        elif "sample_m" in sample_data:
            s_imgs = sample_data["sample_m"].get("image", [])
    if isinstance(s_imgs, str):
        s_imgs = [s_imgs]
    return s_imgs[:max_count]

def generate_individual_post(cid, rank_info, feature_info, it):
    review_html = ALL_REVIEWS.get(cid, "")
    if not review_html:
        print(f"Warning: No review found for {cid}")
        return None

    title = it.get("title", "")
    actresses = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
    makers = [m.get("name") for m in it.get("iteminfo", {}).get("maker", [])]
    genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
    aff_url = it.get("affiliate_url_clean") or it.get("affiliateURL", "")
    package_img = it.get("imageURL", {}).get("large", "")
    sample_imgs = get_sample_images(it, 4)
    release_date = "2026-10-31 07:00:00"
    prices = it.get("prices", {})
    price_str = prices.get("price", "500~") if isinstance(prices, dict) else "500~"

    maker_name = makers[0] if makers else "FANZA公式"
    actress_links_html = " ".join([get_actress_link(a) for a in actresses])
    genre_links_html = " ".join([get_genre_link(g) for g in genres[:8]])

    points_li = "".join([f'<li class="flex items-start gap-2"><span class="text-amber-400 font-bold">✔</span><span class="text-slate-200">{p}</span></li>' for p in rank_info["points"]])

    samples_html = ""
    if sample_imgs:
        samples_html = '''
        <div class="my-8">
          <h3 class="text-lg md:text-xl font-bold text-white mb-4 flex items-center gap-2">
            <span>📸</span> 高画質シーンプレビュー
          </h3>
          <div class="grid grid-cols-2 md:grid-cols-4 gap-3">'''
        for s in sample_imgs:
            samples_html += f'''
            <div class="relative rounded-xl overflow-hidden border border-slate-700/60 shadow-md group">
              <img src="{s}" alt="{title} サンプル画像" class="w-full h-32 md:h-40 object-cover group-hover:scale-110 transition duration-300" loading="lazy" />
            </div>'''
        samples_html += '''
          </div>
        </div>'''

    body_html = f'''<!-- 個別作品詳細レビューコンテナ -->
<div class="space-y-6">
  <!-- パッケージ＆基本情報カード -->
  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-2xl flex flex-col md:flex-row gap-6 items-center md:items-start">
    <div class="w-full md:w-1/3 flex-shrink-0">
      <div class="relative rounded-2xl overflow-hidden shadow-xl border border-slate-700/50 group">
        <img src="{package_img}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="eager" />
        <div class="absolute top-3 left-3 bg-rose-600/90 text-white text-xs font-bold px-3 py-1 rounded-full shadow-lg backdrop-blur-sm">
          厳選神作
        </div>
      </div>
    </div>
    <div class="w-full md:w-2/3 flex flex-col justify-between space-y-4">
      <div>
        <div class="text-xs font-bold text-amber-400 tracking-wider uppercase mb-1">{maker_name}</div>
        <h1 class="text-xl md:text-2xl font-extrabold text-white leading-snug">{title}</h1>
      </div>
      <div class="space-y-2 text-sm text-slate-300">
        <p><strong class="text-slate-400">出演女優：</strong> {actress_links_html if actress_links_html else '<span class="text-slate-400">企画単体・厳選キャスト</span>'}</p>
        <p><strong class="text-slate-400">配信形式：</strong> 動画配信（HD / 4Kストリーミング＆ダウンロード）</p>
        <p><strong class="text-slate-400">品番・CID：</strong> <span class="font-mono text-slate-200">{cid}</span></p>
        <p><strong class="text-slate-400">特化ポイント：</strong> <span class="text-amber-300 font-semibold">{rank_info["spec_summary"]}</span></p>
      </div>

      <!-- キラーポイント箇条書き -->
      <div class="bg-slate-800/40 rounded-2xl p-4 border border-slate-700/40">
        <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider mb-2">🔥 本作の抜きどころ・実用ポイント</h4>
        <ul class="space-y-1.5 text-xs md:text-sm">
          {points_li}
        </ul>
      </div>

      <div class="flex flex-wrap gap-1.5 pt-1">
        {genre_links_html}
      </div>

      <div class="pt-2">
        <a href="{aff_url}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center w-full md:w-auto px-8 py-3.5 bg-gradient-to-r from-rose-600 via-rose-500 to-amber-500 hover:from-rose-500 hover:to-amber-400 text-white font-extrabold rounded-2xl shadow-lg hover:shadow-rose-500/25 transition duration-300 transform hover:-translate-y-0.5 text-base gap-2">
          <span>🎬 FANZA公式で無料サンプル動画を視聴する</span>
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </a>
      </div>
    </div>
  </div>

  {samples_html}

  <!-- レビュー本文 -->
  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-10 shadow-xl space-y-6 text-slate-200 text-base leading-relaxed">
{review_html}
  </div>

  <!-- 本作を最高に楽しむための鑑賞ガイド -->
  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-4 text-slate-300">
    <h3 class="text-lg md:text-xl font-bold text-white flex items-center gap-2">
      <span>💡</span> 本作を120%楽しむためのおすすめ鑑賞ガイド
    </h3>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs md:text-sm">
      <div class="bg-slate-800/50 p-4 rounded-2xl border border-slate-700/50 space-y-2">
        <div class="font-bold text-amber-300 flex items-center gap-1.5">
          <span>🎧</span> ヘッドホン・イヤホン推奨
        </div>
        <p class="text-slate-300 leading-relaxed">
          息遣い、衣擦れの音、耳元で囁かれる甘い吐息や淫語など、音響演出が非常に繊細に作り込まれています。密閉型ヘッドホンやイヤホンを使用することで、その場にいるかのような圧倒的な臨場感を体験できます。
        </p>
      </div>
      <div class="bg-slate-800/50 p-4 rounded-2xl border border-slate-700/50 space-y-2">
        <div class="font-bold text-amber-300 flex items-center gap-1.5">
          <span>📺</span> 大画面・高画質再生での視聴
        </div>
        <p class="text-slate-300 leading-relaxed">
          女優のきめ細やかな肌の質感や艶やかな汗、瞳の揺らぎまで克明に記録された高精細映像です。PCモニターやテレビ画面、または高精細タブレットでの視聴が最も推奨されます。
        </p>
      </div>
    </div>
    <div class="bg-gradient-to-r from-slate-800/60 to-indigo-950/40 p-4 rounded-2xl border border-indigo-500/20 text-xs md:text-sm text-slate-300 space-y-1.5">
      <div class="font-bold text-rose-300 flex items-center gap-1.5">
        <span>🔒</span> FANZA公式配信の安心・安全ポイント
      </div>
      <p class="leading-relaxed">
        悪質な広告や不正プログラムの心配が一切ないFANZA公式ストリーミング＆ダウンロード。一度購入すればマイページから何度でも視聴可能で、家族や同居人にバレないプライベートブラウザ対応・履歴削除機能も完備されています。
      </p>
    </div>
  </div>

  <!-- 特集への内部リンク誘導バナー -->
  <div class="bg-gradient-to-r from-slate-900 to-indigo-950/60 border border-indigo-500/30 rounded-3xl p-6 text-center shadow-xl">
    <h3 class="text-lg font-bold text-white mb-2">📌 この作品が選出された特集ランキング</h3>
    <p class="text-slate-300 text-sm mb-4">{feature_info["title"]}</p>
    <a href="/posts/{feature_info['id']}" class="inline-flex items-center gap-2 px-6 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white font-bold rounded-xl transition text-sm">
      <span>🏆 特集ランキングTOP5をチェックする</span>
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
    </a>
  </div>
</div>'''

    post_data = {
        "id": cid,
        "title": title,
        "date": release_date,
        "hinban": cid,
        "price": f"{price_str}~~",
        "maker": maker_name,
        "actresses": actresses,
        "genres": genres,
        "image": package_img,
        "review": body_html
    }
    return post_data

def generate_feature_article(feature_def, fetched_items):
    f_id = feature_def["id"]
    f_title = feature_def["title"]
    f_hinban = feature_def["hinban"]
    lead_p1 = feature_def["lead_p1"]
    lead_p2 = feature_def["lead_p2"]
    genres = feature_def["genres"]
    items = feature_def["items"]
    deep_dive_title = feature_def.get("deep_dive_title", "")
    deep_dive_content = feature_def.get("deep_dive_content", "")
    faq_items = feature_def.get("faq_items", [])
    related_searches = feature_def.get("related_searches", [])

    all_actresses = []
    top_pkg = ""

    # テーブル行の生成
    table_rows = ""
    for r_item in items:
        cid = r_item["cid"]
        it = fetched_items.get(cid, {})
        rank = r_item["rank"]
        title = it.get("title", cid)
        actresses = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        for a in actresses:
            if a not in all_actresses:
                all_actresses.append(a)

        aff_url = it.get("affiliate_url_clean") or it.get("affiliateURL", "")
        pkg = it.get("imageURL", {}).get("large", "")
        if rank == 1 and pkg:
            top_pkg = pkg

        actress_names_str = " / ".join(actresses) if actresses else "厳選キャスト"
        points_str = "、".join(r_item["points"][:2])

        table_rows += f'''
        <tr class="border-b border-slate-800 hover:bg-slate-800/40 transition">
          <td class="py-3.5 px-3 text-center">
            <span class="inline-flex items-center justify-center w-7 h-7 rounded-full font-black text-xs {'bg-amber-400 text-slate-950 shadow-md shadow-amber-400/20' if rank == 1 else 'bg-slate-700 text-slate-200'}">{rank}</span>
          </td>
          <td class="py-3.5 px-4 font-bold text-white text-sm">
            <a href="/posts/{cid}" class="hover:text-rose-400 transition">{title[:36]}...</a>
            <div class="text-xs font-normal text-slate-400 mt-0.5">{actress_names_str}</div>
          </td>
          <td class="py-3.5 px-4 text-xs text-slate-300 hidden md:table-cell">{points_str}</td>
          <td class="py-3.5 px-3 text-center text-xs text-amber-400 font-bold">★★★★★</td>
          <td class="py-3.5 px-4 text-center">
            <a href="{aff_url}" target="_blank" rel="noopener noreferrer" class="inline-block px-3 py-1.5 bg-rose-600 hover:bg-rose-500 text-white font-bold rounded-lg text-xs shadow transition">公式</a>
          </td>
        </tr>'''

    # TOP5詳細カードの生成
    cards_html = ""
    for r_item in items:
        cid = r_item["cid"]
        it = fetched_items.get(cid, {})
        rank = r_item["rank"]
        title = it.get("title", cid)
        actresses = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        aff_url = it.get("affiliate_url_clean") or it.get("affiliateURL", "")
        pkg = it.get("imageURL", {}).get("large", "")
        sample_imgs = get_sample_images(it, 4)

        actress_links = " ".join([get_actress_link(a) for a in actresses])
        badge_text = r_item.get("badge", f"第{rank}位")

        points_list = "".join([f'<li class="flex items-start gap-2"><span class="text-amber-400 font-bold">✔</span><span class="text-slate-200">{p}</span></li>' for p in r_item["points"]])

        samples_grid = ""
        if sample_imgs:
            samples_grid = '<div class="grid grid-cols-2 md:grid-cols-4 gap-2.5 my-4">'
            for s in sample_imgs:
                samples_grid += f'''
                <div class="relative rounded-xl overflow-hidden border border-slate-700/60 shadow group">
                  <img src="{s}" alt="{title} 場面カット" class="w-full h-24 md:h-32 object-cover group-hover:scale-105 transition duration-300" loading="lazy" />
                </div>'''
            samples_grid += '</div>'

        cards_html += f'''
    <!-- 第{rank}位 作品カード -->
    <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-6">
      <div class="flex flex-col md:flex-row gap-6 items-center md:items-start">
        <div class="w-full md:w-1/3 flex-shrink-0">
          <div class="relative rounded-2xl overflow-hidden shadow-lg border border-slate-700/60 group">
            <img src="{pkg}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
            <div class="absolute top-3 left-3 bg-amber-400 text-slate-950 font-black text-sm px-3 py-1 rounded-full shadow-lg">
              第{rank}位
            </div>
          </div>
        </div>
        <div class="w-full md:w-2/3 space-y-3">
          <div class="inline-block bg-rose-950/80 text-rose-300 text-xs font-bold px-3 py-1 rounded-full border border-rose-800/50">
            {badge_text}
          </div>
          <h3 class="text-lg md:text-xl font-bold text-white leading-snug">
            <a href="/posts/{cid}" class="hover:text-rose-400 transition">{title}</a>
          </h3>
          <div class="text-sm text-slate-300 space-y-1">
            <p><strong class="text-slate-400">出演：</strong> {actress_links if actress_links else '<span class="text-slate-400">厳選キャスト</span>'}</p>
            <p><strong class="text-slate-400">配信形式：</strong> HD / 4K 高画質ストリーミング・ダウンロード</p>
            <p><strong class="text-slate-400">特化：</strong> <span class="text-amber-300 font-medium">{r_item["spec_summary"]}</span></p>
          </div>
          <div class="bg-slate-800/60 rounded-2xl p-4 border border-slate-700/50">
            <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider mb-2">🔥 厳選注目ポイント</h4>
            <ul class="space-y-1.5 text-xs md:text-sm">
              {points_list}
            </ul>
          </div>
          <div class="flex flex-wrap gap-3 pt-2">
            <a href="{aff_url}" target="_blank" rel="noopener noreferrer" class="px-6 py-2.5 bg-rose-600 hover:bg-rose-500 text-white font-bold rounded-xl shadow transition text-sm flex items-center gap-1.5">
              <span>🎬 公式でサンプル動画を見る</span>
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </a>
            <a href="/posts/{cid}" class="px-5 py-2.5 bg-slate-800 hover:bg-slate-700 text-slate-200 hover:text-white font-bold rounded-xl border border-slate-700 transition text-sm">
              📖 詳細個別レビューを読む
            </a>
          </div>
        </div>
      </div>
      {samples_grid}
    </div>'''

    # 徹底考察セクション
    deep_dive_section = ""
    if deep_dive_title and deep_dive_content:
        deep_dive_section = f'''
  <!-- 徹底考察セクション -->
  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-10 shadow-xl space-y-4">
    <h2 class="text-xl md:text-2xl font-black text-white flex items-center gap-2 border-b border-slate-800 pb-4">
      <span>🧠</span> {deep_dive_title}
    </h2>
    <div class="space-y-4 text-slate-300 text-base leading-relaxed">
      {deep_dive_content}
    </div>
  </div>'''

    # FAQセクション
    faq_html = ""
    if faq_items:
        faq_blocks = ""
        for faq in faq_items:
            faq_blocks += f'''
      <div class="bg-slate-800/50 rounded-2xl p-5 border border-slate-700/50 space-y-2">
        <h3 class="font-bold text-white text-base flex items-start gap-2">
          <span class="text-amber-400 font-extrabold">Q.</span>
          <span>{faq["q"]}</span>
        </h3>
        <p class="text-slate-300 text-sm pl-6 leading-relaxed">
          {faq["a"]}
        </p>
      </div>'''

        faq_html = f'''
  <!-- よくある質問（FAQ）セクション -->
  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-10 shadow-xl space-y-6">
    <h2 class="text-xl md:text-2xl font-black text-white flex items-center gap-2 border-b border-slate-800 pb-4">
      <span>❓</span> よくある質問と鑑賞アドバイス
    </h2>
    <div class="space-y-4">
      {faq_blocks}
    </div>
  </div>'''

    # 関連キーワードセクション
    related_html = ""
    if related_searches:
        tags_html = " ".join([get_genre_link(k) for k in related_searches])
        related_html = f'''
  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 shadow-xl space-y-3">
    <h3 class="text-sm font-bold text-slate-400 uppercase tracking-wider flex items-center gap-2">
      <span>🏷️</span> 関連キーワード・タグ一覧
    </h3>
    <div class="flex flex-wrap gap-2">
      {tags_html}
    </div>
  </div>'''

    genre_badges = " ".join([get_genre_link(g) for g in genres])

    feature_body = f'''<!-- キラー特集記事メインコンテナ -->
<div class="space-y-8">
  <!-- 導入リード文カード -->
  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-10 shadow-2xl space-y-6">
    <div class="flex flex-wrap gap-2">
      {genre_badges}
    </div>
    <div class="space-y-4 text-base md:text-lg text-slate-200 leading-relaxed border-l-4 border-rose-500 pl-4 md:pl-6">
      <p>{lead_p1}</p>
      <p>{lead_p2}</p>
    </div>
  </div>

  <!-- TOP5比較クイックナビ表 -->
  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-4">
    <h2 class="text-lg md:text-xl font-bold text-white flex items-center gap-2">
      <span>📊</span> 厳選神作TOP5 比較クイックナビ
    </h2>
    <div class="overflow-x-auto">
      <table class="w-full text-left text-sm text-slate-300">
        <thead class="text-xs text-slate-400 uppercase bg-slate-800/60 border-b border-slate-700">
          <tr>
            <th class="py-3 px-3 text-center">順位</th>
            <th class="py-3 px-4">作品 / 出演女優</th>
            <th class="py-3 px-4 hidden md:table-cell">特化ポイント</th>
            <th class="py-3 px-3 text-center">評価</th>
            <th class="py-3 px-4 text-center">公式</th>
          </tr>
        </thead>
        <tbody>
          {table_rows}
        </tbody>
      </table>
    </div>
  </div>

  <!-- TOP5各作品の詳細紹介カード群 -->
  <div class="space-y-6">
    {cards_html}
  </div>

  {deep_dive_section}

  {faq_html}

  {related_html}
</div>'''

    feature_post = {
        "id": f_id,
        "title": f_title,
        "date": "2026-10-31 07:00:00",
        "hinban": f_hinban,
        "price": "500~~",
        "maker": "FANZA公式 編集部特選",
        "actresses": all_actresses,
        "genres": genres,
        "image": top_pkg,
        "review": feature_body
    }
    return feature_post

def main():
    print("=== Start generating 3 new killer features & 15 reviews (v25) ===")
    
    # 1. 全作品のFANZA APIデータを都度取得
    all_cids = []
    for f in FEATURE_ARTICLES:
        for it in f["items"]:
            all_cids.append(it["cid"])

    print(f"Total CIDs to fetch: {len(all_cids)}")
    fetched_items = {}
    for cid in all_cids:
        print(f"Fetching from FANZA API: {cid} ...")
        it = fetch_fanza_item(cid)
        if it:
            fetched_items[cid] = it
            print(f"  -> SUCCESS: {it.get('title')[:30]}...")
        else:
            print(f"  -> FAILED: {cid}")
        time.sleep(0.5)

    created_ids = []

    # 2. 個別作品詳細レビュー（15件）の生成と保存
    print("\n--- Generating 15 individual review posts ---")
    for f in FEATURE_ARTICLES:
        for r_item in f["items"]:
            cid = r_item["cid"]
            it = fetched_items.get(cid)
            if not it:
                print(f"Skipping {cid} due to missing API data")
                continue
            post_data = generate_individual_post(cid, r_item, f, it)
            if post_data:
                chars = count_japanese_chars(post_data["review"])
                print(f"Created post: {cid} | Chars: {chars} (Requirement: >=3000)")
                if chars < 3000:
                    print(f"WARNING: Character count under 3000 for {cid} ({chars} chars)!")
                file_path = os.path.join(OUTPUT_DIR, f"{cid}.json")
                with open(file_path, "w", encoding="utf-8") as fp:
                    json.dump(post_data, fp, ensure_ascii=False, indent=2)
                created_ids.append(cid)

    # 3. キラー特集3記事の生成と保存
    print("\n--- Generating 3 killer feature articles ---")
    for f in FEATURE_ARTICLES:
        f_post = generate_feature_article(f, fetched_items)
        chars = count_japanese_chars(f_post["review"])
        print(f"Created feature: {f_post['id']} | Chars: {chars} (Requirement: >=3000)")
        if chars < 3000:
            print(f"WARNING: Character count under 3000 for {f_post['id']} ({chars} chars)!")
        file_path = os.path.join(OUTPUT_DIR, f"{f_post['id']}.json")
        with open(file_path, "w", encoding="utf-8") as fp:
            json.dump(f_post, fp, ensure_ascii=False, indent=2)
        created_ids.append(f_post["id"])

    # 4. posted_cache.txt に追加
    with open("posted_cache.txt", "a", encoding="utf-8") as fp:
        for pid in created_ids:
            fp.write(f"{pid}\n")
    print(f"\nAppended {len(created_ids)} IDs to posted_cache.txt")
    print("=== All generation completed successfully! ===")

if __name__ == "__main__":
    main()
