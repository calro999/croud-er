# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・新規キラー特集3記事および個別作品15件自動生成スクリプト v15
各記事3000文字以上・完全独自書き下ろし・内部リンク網羅・SEO/LLM/GEO対策
1. オフィス・OL・秘密の社内情事特集
2. 高級ホテル・スイートルーム背徳密会特集
3. 魅惑のコスプレ・変身ヒロイン特集
"""

import os
import re
import json
import time
import urllib.parse
import requests

from reviews_feature_office import REVIEWS_OFFICE
from reviews_feature_hotel import REVIEWS_HOTEL
from reviews_feature_cosplay import REVIEWS_COSPLAY
from features_def_v15 import FEATURE_ARTICLES

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
ALL_REVIEWS.update(REVIEWS_OFFICE)
ALL_REVIEWS.update(REVIEWS_HOTEL)
ALL_REVIEWS.update(REVIEWS_COSPLAY)

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
    release_date = it.get("date", "2026-10-12 06:00:00")
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
          <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
        '''
        for idx, simg in enumerate(sample_imgs, 1):
            samples_html += f'''
            <div class="relative rounded-2xl overflow-hidden bg-slate-800 border border-slate-700/60 shadow group">
              <img src="{simg}" alt="{title} シーン画像{idx}" class="w-full h-auto object-cover transform group-hover:scale-105 transition duration-300" loading="lazy" />
              <div class="absolute bottom-2 left-2 bg-black/70 backdrop-blur-md px-2 py-0.5 rounded text-[10px] text-slate-300">プレビュー #{idx}</div>
            </div>
            '''
        samples_html += '</div></div>'

    feature_reverse_banner = f'''
    <div class="bg-gradient-to-r from-slate-900 to-indigo-950/60 border border-indigo-500/30 rounded-3xl p-6 text-center shadow-xl">
      <h3 class="text-lg font-bold text-white mb-2">📌 この作品が選出された特集ランキング</h3>
      <p class="text-slate-300 text-sm mb-4">{feature_info['title']}</p>
      <a href="/posts/{feature_info['id']}" class="inline-flex items-center gap-2 px-6 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white font-bold rounded-xl transition text-sm">
        <span>🏆 特集ランキングTOP5をチェックする</span>
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
      </a>
    </div>
    '''

    full_review_html = f'''<!-- 個別作品詳細レビューコンテナ -->
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
        <p><strong class="text-slate-400">出演女優：</strong> {actress_links_html}</p>
        <p><strong class="text-slate-400">配信形式：</strong> 動画配信（HD / 4Kストリーミング＆ダウンロード）</p>
        <p><strong class="text-slate-400">品番・CID：</strong> <span class="font-mono text-slate-200">{cid}</span></p>
        <p><strong class="text-slate-400">特化ポイント：</strong> <span class="text-amber-300 font-semibold">{rank_info['spec_summary']}</span></p>
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
      <div class="pt-3">
        <a href="{aff_url}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center gap-3 w-full md:w-auto px-8 py-4 bg-gradient-to-r from-rose-600 to-amber-600 hover:from-rose-500 hover:to-amber-500 text-white font-extrabold text-base rounded-2xl shadow-xl hover:shadow-rose-500/25 transition duration-300 transform hover:-translate-y-0.5">
          <span>🔥 FANZA公式サイトで本編・無料サンプル動画を視聴する</span>
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </a>
      </div>
    </div>
  </div>

  {samples_html}

  <!-- 本文詳細レビュー -->
  <div class="bg-slate-900/90 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl text-slate-200 leading-relaxed space-y-6 prose prose-invert max-w-none">
    {review_html}
  </div>

  {feature_reverse_banner}
</div>'''

    post_data = {
        "id": cid,
        "title": title,
        "date": release_date,
        "hinban": cid,
        "price": f"{price_str}~",
        "maker": maker_name,
        "actresses": actresses,
        "genres": genres,
        "image": package_img,
        "review": full_review_html
    }
    return post_data

def generate_feature_article(feature_def, fetched_items):
    f_id = feature_def["id"]
    f_title = feature_def["title"]
    f_hinban = feature_def["hinban"]
    items = feature_def["items"]
    lead_p1 = feature_def["lead_p1"]
    lead_p2 = feature_def["lead_p2"]
    genres = feature_def["genres"]
    faqs = feature_def.get("faqs", [])
    related = feature_def.get("related", [])

    all_actresses = []
    for it_info in items:
        it = fetched_items.get(it_info["cid"], {})
        for a in it.get("iteminfo", {}).get("actress", []):
            aname = a.get("name")
            if aname and aname not in all_actresses:
                all_actresses.append(aname)

    top_item = items[0]
    top_it = fetched_items.get(top_item["cid"], {})
    top_pkg = top_it.get("imageURL", {}).get("large", "")

    # 1. 比較一覧表の行
    table_rows = ""
    for r_item in items:
        cid = r_item["cid"]
        rank = r_item["rank"]
        spec_summary = r_item["spec_summary"]
        it = fetched_items.get(cid, {})
        it_title = it.get("title", "")
        acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        act_name = acts[0] if acts else ""
        aff_url = it.get("affiliate_url_clean") or it.get("affiliateURL", "")

        table_rows += f'''
        <tr class="border-b border-slate-800 hover:bg-slate-800/40 transition">
          <td class="py-4 px-3 text-center">
            <span class="inline-flex items-center justify-center w-7 h-7 rounded-full bg-amber-500/20 text-amber-300 font-extrabold text-sm border border-amber-500/30">
              {rank}
            </span>
          </td>
          <td class="py-4 px-4">
            <a href="/posts/{cid}" class="text-white hover:text-rose-400 font-bold text-sm block mb-0.5 line-clamp-1">{it_title}</a>
            <span class="text-xs text-rose-400 font-medium">主演: {act_name}</span>
          </td>
          <td class="py-4 px-4 text-xs text-slate-300 hidden md:table-cell">
            {spec_summary}
          </td>
          <td class="py-4 px-3 text-center">
            <span class="text-amber-400 text-xs font-bold">★★★★★</span>
          </td>
          <td class="py-4 px-4 text-center">
            <a href="{aff_url}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-rose-600 hover:bg-rose-500 text-white rounded-lg text-xs font-bold shadow transition">
              <span>公式</span>
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
            </a>
          </td>
        </tr>
        '''

    # 2. ランキング各カード
    cards_html = ""
    for r_item in items:
        cid = r_item["cid"]
        rank = r_item["rank"]
        badge = r_item["badge"]
        spec_summary = r_item["spec_summary"]
        points = r_item["points"]

        it = fetched_items.get(cid, {})
        it_title = it.get("title", "")
        pkg = it.get("imageURL", {}).get("large", "")
        aff_url = it.get("affiliate_url_clean") or it.get("affiliateURL", "")
        acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        act_links = " ".join([get_actress_link(a) for a in acts])
        makers = [m.get("name") for m in it.get("iteminfo", {}).get("maker", [])]
        maker_name = makers[0] if makers else "FANZA公式"
        it_genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        genre_links = " ".join([get_genre_link(g) for g in it_genres[:6]])
        sample_imgs = get_sample_images(it, 4)
        individual_review = ALL_REVIEWS.get(cid, "")

        points_li = "".join([f'<li class="flex items-start gap-2"><span class="text-amber-400 font-bold">✔</span><span class="text-slate-200">{p}</span></li>' for p in points])

        sample_grid = ""
        if sample_imgs:
            sample_grid = '<div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-2">'
            for sidx, simg in enumerate(sample_imgs, 1):
                sample_grid += f'''
                <div class="rounded-xl overflow-hidden bg-slate-800 border border-slate-700/50">
                  <img src="{simg}" alt="{it_title} プレビュー{sidx}" class="w-full h-auto object-cover" loading="lazy" />
                </div>
                '''
            sample_grid += '</div>'

        cards_html += f'''
        <!-- RANK {rank} -->
        <div class="bg-slate-900/90 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-6">
          <div class="flex flex-col md:flex-row gap-6 items-center md:items-start">
            <div class="w-full md:w-1/3 flex-shrink-0">
              <div class="relative rounded-2xl overflow-hidden shadow-xl border border-slate-700/60 group">
                <img src="{pkg}" alt="{it_title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
                <div class="absolute top-3 left-3 bg-gradient-to-r from-amber-500 to-rose-600 text-white font-extrabold text-sm px-3.5 py-1 rounded-full shadow-lg">
                  第{rank}位
                </div>
              </div>
            </div>
            <div class="w-full md:w-2/3 flex flex-col justify-between space-y-4">
              <div>
                <div class="inline-block bg-rose-500/20 text-rose-300 border border-rose-500/30 text-xs font-bold px-3 py-1 rounded-full mb-2">
                  {badge}
                </div>
                <h3 class="text-xl md:text-2xl font-extrabold text-white leading-snug">
                  <a href="/posts/{cid}" class="hover:text-rose-400 transition">{it_title}</a>
                </h3>
              </div>
              
              <div class="space-y-1.5 text-sm text-slate-300">
                <p><strong class="text-slate-400">主演女優：</strong> {act_links}</p>
                <p><strong class="text-slate-400">メーカー：</strong> <span class="text-slate-200">{maker_name}</span></p>
                <p><strong class="text-slate-400">品番・CID：</strong> <span class="font-mono text-slate-300">{cid}</span></p>
                <p><strong class="text-slate-400">特化ポイント：</strong> <span class="text-amber-300 font-semibold">{spec_summary}</span></p>
              </div>

              <div class="bg-slate-800/40 rounded-2xl p-4 border border-slate-700/40">
                <div class="text-xs font-bold text-amber-400 uppercase tracking-wider mb-2">🔥 圧倒的抜きどころハイライト</div>
                <ul class="space-y-1.5 text-xs md:text-sm">
                  {points_li}
                </ul>
              </div>

              <div class="flex flex-wrap gap-1.5 pt-1">
                {genre_links}
              </div>

              <div class="pt-3 flex flex-col sm:flex-row gap-3">
                <a href="{aff_url}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center gap-2 px-6 py-3.5 bg-gradient-to-r from-rose-600 to-amber-600 hover:from-rose-500 hover:to-amber-500 text-white font-extrabold text-sm rounded-xl shadow-lg hover:shadow-rose-500/25 transition flex-1 text-center">
                  <span>🔥 FANZA公式サイトで本編・無料サンプルを見る</span>
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                </a>
                <a href="/posts/{cid}" class="inline-flex items-center justify-center gap-2 px-5 py-3.5 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold text-sm rounded-xl border border-slate-700 transition text-center">
                  <span>📖 個別超濃密レビューを読む</span>
                </a>
              </div>
            </div>
          </div>

          {sample_grid}

          <!-- 作品詳細レビュー抜粋 -->
          <div class="bg-slate-950/60 rounded-2xl p-5 border border-slate-800 text-slate-300 text-sm leading-relaxed space-y-4">
            {individual_review}
          </div>
        </div>
        '''

    # 3. FAQセクション
    faq_html = ""
    if faqs:
        faq_items = ""
        for q, a in faqs:
            faq_items += f'''
            <div class="bg-slate-800/50 rounded-2xl p-5 border border-slate-700/40 space-y-2">
              <h4 class="text-base font-bold text-amber-300 flex items-center gap-2">
                <span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-amber-400/20 text-amber-300 text-xs font-black">Q</span>
                {q}
              </h4>
              <p class="text-slate-300 text-sm leading-relaxed pl-8">
                {a}
              </p>
            </div>
            '''
        faq_html = f'''
        <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-4 my-8">
          <h3 class="text-xl font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-3">
            <span>💡</span> このジャンルに関するよくある質問（FAQ）
          </h3>
          <div class="space-y-4 pt-2">
            {faq_items}
          </div>
        </div>
        '''

    # 4. あわせて読みたい
    related_html = ""
    if related:
        rel_cards = ""
        for rlink, rtitle, rdesc in related:
            rel_cards += f'''
            <a href="{rlink}" class="bg-slate-800/40 hover:bg-slate-800/80 border border-slate-700/50 hover:border-rose-500/50 rounded-2xl p-5 transition group flex flex-col justify-between">
              <div>
                <h4 class="text-white group-hover:text-rose-400 font-bold text-base mb-2 transition leading-snug">{rtitle}</h4>
                <p class="text-slate-400 text-xs leading-relaxed">{rdesc}</p>
              </div>
              <div class="mt-4 text-xs text-rose-400 font-bold flex items-center gap-1 group-hover:translate-x-1 transition">
                <span>記事を読む</span>
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
              </div>
            </a>
            '''
        related_html = f'''
        <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-4 my-8">
          <h3 class="text-xl font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-3">
            <span>✨</span> あわせて読みたい関連キラー特集
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4 pt-2">
            {rel_cards}
          </div>
        </div>
        '''

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

  <!-- ランキング詳細カード一覧 -->
  <div class="space-y-10 my-8">
    {cards_html}
  </div>

  {faq_html}
  {related_html}
</div>'''

    post_data = {
        "id": f_id,
        "title": f_title,
        "date": "2026-10-12 06:00:00",
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
    print("=== Start Generating Killer Features v15 ===")
    
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
