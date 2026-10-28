# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・新規キラー特集3記事および個別作品15件自動生成スクリプト v17
各記事3500文字以上・完全独自書き下ろし・内部リンク網羅・SEO/LLM/GEO対策
1. 満員電車・密着痴漢・通勤ラッシュ背徳特集
2. 高級ソープランド・泡姫マットプレイ＆密着洗体特集
3. PTA役員・保護者会不倫・昼下がり密会特集
"""

import os
import re
import json
import time
import urllib.parse
import requests

from reviews_feature_densha import REVIEWS_DENSHA
from reviews_feature_soapland import REVIEWS_SOAPLAND
from reviews_feature_pta import REVIEWS_PTA
from features_def_v17 import FEATURE_ARTICLES

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
ALL_REVIEWS.update(REVIEWS_DENSHA)
ALL_REVIEWS.update(REVIEWS_SOAPLAND)
ALL_REVIEWS.update(REVIEWS_PTA)

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
    release_date = "2026-10-28 22:00:00"
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
        <p><strong class="text-slate-400">出演女優：</strong> {actress_links_html if actress_links_html else '<span class="text-slate-400">企画単体・素人キャスト</span>'}</p>
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
    faqs = feature_def.get("faqs", [])
    related = feature_def.get("related", [])

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

        act_text = "企画単体"
        if actresses:
            act_text = ", ".join(actresses[:2])

        table_rows += f'''
        <tr class="border-b border-slate-800/80 hover:bg-slate-800/40 transition">
          <td class="py-3 px-3 text-center font-extrabold text-amber-400">{rank}位</td>
          <td class="py-3 px-4 font-medium text-slate-200">
            <a href="/posts/{cid}" class="hover:text-rose-400 transition underline underline-offset-2 font-bold">{title}</a>
            <div class="text-xs text-slate-400 mt-0.5">出演：{act_text}</div>
          </td>
          <td class="py-3 px-4 text-xs text-slate-300 hidden md:table-cell">{r_item["spec_summary"]}</td>
          <td class="py-3 px-3 text-center text-rose-400 font-bold text-xs">★★★★★</td>
          <td class="py-3 px-4 text-center">
            <a href="{aff_url}" target="_blank" rel="noopener noreferrer" class="inline-block px-3 py-1 bg-rose-600 hover:bg-rose-500 text-white text-xs font-bold rounded-lg transition whitespace-nowrap shadow-sm">公式詳細</a>
          </td>
        </tr>'''

    # 各作品紹介カード群
    cards_html = ""
    for r_item in items:
        cid = r_item["cid"]
        it = fetched_items.get(cid, {})
        rank = r_item["rank"]
        title = it.get("title", cid)
        badge = r_item["badge"]
        actresses = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        makers = [m.get("name") for m in it.get("iteminfo", {}).get("maker", [])]
        maker_name = makers[0] if makers else "FANZA公式"
        aff_url = it.get("affiliate_url_clean") or it.get("affiliateURL", "")
        pkg = it.get("imageURL", {}).get("large", "")
        sample_imgs = get_sample_images(it, 3)

        actress_links = " ".join([get_actress_link(a) for a in actresses])
        points_li = "".join([f'<li class="flex items-start gap-2"><span class="text-amber-400 font-bold">✔</span><span class="text-slate-200">{p}</span></li>' for p in r_item["points"]])

        samples_card_html = ""
        if sample_imgs:
            samples_card_html = '<div class="grid grid-cols-3 gap-2 mt-4">'
            for s in sample_imgs:
                samples_card_html += f'<div class="rounded-lg overflow-hidden border border-slate-700/50"><img src="{s}" alt="サンプル画像" class="w-full h-24 object-cover" loading="lazy" /></div>'
            samples_card_html += '</div>'

        medal = "🥇" if rank == 1 else ("🥈" if rank == 2 else ("🥉" if rank == 3 else f"第{rank}位"))

        cards_html += f'''
    <!-- 第{rank}位カード -->
    <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-6">
      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 border-b border-slate-800 pb-4">
        <div class="flex items-center gap-3">
          <span class="text-2xl md:text-3xl font-black text-amber-400">{medal}</span>
          <span class="text-xs md:text-sm font-bold px-3 py-1 bg-rose-600/20 text-rose-400 border border-rose-500/30 rounded-full">{badge}</span>
        </div>
        <div class="text-xs font-mono text-slate-400">CID: {cid} / {maker_name}</div>
      </div>

      <div class="flex flex-col md:flex-row gap-6 items-center md:items-start">
        <div class="w-full md:w-2/5 flex-shrink-0">
          <div class="relative rounded-2xl overflow-hidden shadow-lg border border-slate-700/60 group">
            <img src="{pkg}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
          </div>
          {samples_card_html}
        </div>
        <div class="w-full md:w-3/5 space-y-4">
          <h2 class="text-xl md:text-2xl font-bold text-white leading-snug">
            <a href="/posts/{cid}" class="hover:text-rose-400 transition">{title}</a>
          </h2>
          <div class="text-xs md:text-sm text-slate-300 space-y-1">
            <p><strong class="text-slate-400">主演：</strong> {actress_links if actress_links else '<span class="text-slate-400">企画単体</span>'}</p>
            <p><strong class="text-slate-400">特化ポイント：</strong> <span class="text-amber-300 font-semibold">{r_item["spec_summary"]}</span></p>
          </div>

          <div class="bg-slate-800/40 rounded-2xl p-4 border border-slate-700/40">
            <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider mb-2">🔥 厳選抜けるポイント・見どころ</h4>
            <ul class="space-y-1.5 text-xs md:text-sm">
              {points_li}
            </ul>
          </div>

          <div class="pt-2 flex flex-col sm:flex-row gap-3">
            <a href="/posts/{cid}" class="inline-flex items-center justify-center px-5 py-2.5 bg-slate-800 hover:bg-slate-700 text-slate-200 hover:text-white font-bold rounded-xl transition text-sm border border-slate-700 gap-1.5">
              <span>📖 単体詳細レビューを読む</span>
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </a>
            <a href="{aff_url}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center px-6 py-2.5 bg-gradient-to-r from-rose-600 to-amber-500 hover:from-rose-500 hover:to-amber-400 text-white font-extrabold rounded-xl shadow-lg transition text-sm gap-1.5">
              <span>🎬 FANZA公式で無料サンプルを視聴</span>
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </a>
          </div>
        </div>
      </div>
    </div>'''

    # 深掘り解説コラム
    deep_dive_section = ""
    if deep_dive_title and deep_dive_content:
        deep_dive_section = f'''
  <!-- 深掘り解説コラム -->
  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-10 shadow-xl space-y-6 my-8">
    <div class="inline-flex items-center gap-2 px-3 py-1 bg-amber-500/10 border border-amber-500/20 rounded-full text-amber-400 text-xs font-bold">
      <span>💡</span> 特集徹底深掘りコラム
    </div>
    <h3 class="text-xl md:text-2xl font-extrabold text-white">
      {deep_dive_title}
    </h3>
    {deep_dive_content}
  </div>'''

    # FAQ
    faq_html = ""
    if faqs:
        f_items = ""
        for faq in faqs:
            f_items += f'''
            <div class="bg-slate-800/40 rounded-2xl p-5 border border-slate-700/40 space-y-2">
              <h4 class="text-amber-400 font-bold text-sm md:text-base flex items-start gap-2">
                <span class="bg-amber-400/20 text-amber-300 text-xs px-2 py-0.5 rounded font-black">Q</span>
                <span>{faq['q']}</span>
              </h4>
              <p class="text-slate-300 text-xs md:text-sm leading-relaxed pl-6">
                {faq['a']}
              </p>
            </div>'''
        faq_html = f'''
        <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-4 my-8">
          <h3 class="text-xl font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-3">
            <span>❓</span> よくある質問と実用度ガイド
          </h3>
          <div class="space-y-3 pt-2">
            {f_items}
          </div>
        </div>'''

    # 関連特集リンク
    related_html = ""
    if related:
        rel_cards = ""
        for r in related:
            rel_cards += f'''
            <a href="{r['url']}" class="bg-slate-800/40 hover:bg-slate-800/80 border border-slate-700/50 hover:border-rose-500/50 rounded-2xl p-5 transition group flex flex-col justify-between">
              <div>
                <h4 class="text-white group-hover:text-rose-400 font-bold text-base mb-2 transition leading-snug">{r['title']}</h4>
                <p class="text-slate-400 text-xs leading-relaxed">{r['desc']}</p>
              </div>
              <div class="mt-4 text-xs text-rose-400 font-bold flex items-center gap-1 group-hover:translate-x-1 transition">
                <span>記事を読む</span>
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
              </div>
            </a>'''
        related_html = f'''
        <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-4 my-8">
          <h3 class="text-xl font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-3">
            <span>✨</span> あわせて読みたい関連キラー特集
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4 pt-2">
            {rel_cards}
          </div>
        </div>'''

    feature_body = f'''<!-- 特集記事コンテナ -->
<div class="space-y-8">
  <!-- ヘッダー導入 -->
  <div class="bg-gradient-to-br from-slate-900 via-slate-900 to-indigo-950 border border-slate-800 rounded-3xl p-6 md:p-10 shadow-2xl space-y-6">
    <div class="inline-flex items-center gap-2 px-3.5 py-1 bg-rose-600/20 border border-rose-500/40 rounded-full text-rose-300 text-xs font-extrabold uppercase tracking-wider">
      <span>🔥</span> FANZA公式連携・2026年最新キラー特集
    </div>
    <h1 class="text-2xl md:text-4xl font-extrabold text-white leading-tight tracking-tight">
      {f_title}
    </h1>
    <div class="space-y-4 text-slate-300 text-base md:text-lg leading-relaxed pt-2 border-t border-slate-800/80">
      <p>{lead_p1}</p>
      <p>{lead_p2}</p>
    </div>
  </div>

  <!-- ランキング比較表 -->
  <div class="my-8 overflow-x-auto rounded-2xl border border-slate-800 bg-slate-900/60 shadow-xl">
    <table class="w-full text-left border-collapse">
      <thead>
        <tr class="bg-slate-800/80 text-xs font-bold text-slate-300 uppercase tracking-wider border-b border-slate-700">
          <th class="py-3 px-3 text-center w-14">順位</th>
          <th class="py-3 px-4">作品 / 主演</th>
          <th class="py-3 px-4 hidden md:table-cell">特化ポイント</th>
          <th class="py-3 px-3 text-center w-24">評価</th>
          <th class="py-3 px-4 text-center w-20">公式</th>
        </tr>
      </thead>
      <tbody>
        {table_rows}
      </tbody>
    </table>
  </div>

  <!-- 各作品紹介カード群 -->
  <div class="space-y-10 my-8">
    {cards_html}
  </div>

  {deep_dive_section}
  {faq_html}
  {related_html}
</div>'''

    post_data = {
        "id": f_id,
        "title": f_title,
        "date": "2026-10-28 22:00:00",
        "hinban": f_hinban,
        "price": "500~",
        "maker": "FANZA公式厳選特集",
        "actresses": all_actresses,
        "genres": genres,
        "image": top_pkg,
        "review": feature_body
    }
    return post_data

def main():
    print("=== Start Generating Killer Features v17 ===")
    
    all_cids = []
    for f in FEATURE_ARTICLES:
        for it in f["items"]:
            all_cids.append(it["cid"])
    
    print(f"Total CIDs to fetch: {len(all_cids)}")
    fetched_data = {}
    for cid in all_cids:
        print(f"Fetching from FANZA API: {cid}...")
        item = fetch_fanza_item(cid)
        if item:
            fetched_data[cid] = item
            print(f"  OK: {item.get('title', '')[:30]}")
        else:
            print(f"  FAILED: {cid}")
        time.sleep(0.5)

    generated_posts = []

    # 1. 個別作品15件の生成
    for f in FEATURE_ARTICLES:
        for r_item in f["items"]:
            cid = r_item["cid"]
            it = fetched_data.get(cid)
            if not it:
                print(f"Skip post {cid} due to missing data")
                continue
            post = generate_individual_post(cid, r_item, f, it)
            if post:
                out_path = os.path.join(OUTPUT_DIR, f"{cid}.json")
                with open(out_path, "w", encoding="utf-8") as out_f:
                    json.dump(post, out_f, ensure_ascii=False, indent=2)
                generated_posts.append(post)
                char_count = count_japanese_chars(post["review"])
                print(f"Generated Post: {cid} ({char_count} chars)")

    # 2. キラー特集3記事の生成
    for f in FEATURE_ARTICLES:
        f_post = generate_feature_article(f, fetched_data)
        out_path = os.path.join(OUTPUT_DIR, f"{f_post['id']}.json")
        with open(out_path, "w", encoding="utf-8") as out_f:
            json.dump(f_post, out_f, ensure_ascii=False, indent=2)
        generated_posts.append(f_post)
        char_count = count_japanese_chars(f_post["review"])
        print(f"Generated Feature: {f_post['id']} ({char_count} chars)")

    # posted_cache.txtの更新
    with open("posted_cache.txt", "a", encoding="utf-8") as f:
        for cid in all_cids:
            f.write(f"{cid}\n")

    print(f"\nAll Done! Successfully generated {len(generated_posts)} articles.")

if __name__ == "__main__":
    main()
