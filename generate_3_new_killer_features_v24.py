# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・新規キラー特集3記事および個別作品15件自動生成スクリプト v24
各記事3500文字以上・完全独自書き下ろし・内部リンク網羅・SEO/LLM/GEO対策
1. 【桃尻が波打ちバックから突き上げる快感】美尻・巨尻・後背位特化 特集（TOP5）
2. 【初々しい素顔とベッドの乱れ咲き】現役女子大生・素人JD・キャンパス密会 特集（TOP5）
3. 【規格外の肉感と揺れる神乳に埋もれる】爆乳・超巨乳・メガパイズリ 特集（TOP5）
"""

import os
import re
import json
import time
import urllib.parse
import subprocess
import requests

from reviews_feature_hip_ass import REVIEWS_HIP_ASS
from reviews_feature_college_student import REVIEWS_COLLEGE_STUDENT
from reviews_feature_busty_dynamite import REVIEWS_BUSTY_DYNAMITE
from features_def_v24 import FEATURE_ARTICLES

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
ALL_REVIEWS.update(REVIEWS_HIP_ASS)
ALL_REVIEWS.update(REVIEWS_COLLEGE_STUDENT)
ALL_REVIEWS.update(REVIEWS_BUSTY_DYNAMITE)

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
    release_date = "2026-10-31 01:00:00"
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
            <a href="{aff_url}" target="_blank" rel="noopener noreferrer" class="inline-flex px-3 py-1.5 bg-rose-600 hover:bg-rose-500 text-white rounded-lg text-xs font-bold transition">公式</a>
          </td>
        </tr>'''

    # 個別カード群の生成
    cards_html = ""
    for r_item in items:
        cid = r_item["cid"]
        it = fetched_items.get(cid, {})
        rank = r_item["rank"]
        badge = r_item["badge"]
        points = r_item["points"]
        title = it.get("title", cid)
        actresses = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        aff_url = it.get("affiliate_url_clean") or it.get("affiliateURL", "")
        pkg = it.get("imageURL", {}).get("large", "")
        sample_imgs = get_sample_images(it, 3)

        actress_links = " ".join([get_actress_link(a) for a in actresses])
        points_li = "".join([f'<li class="flex items-start gap-2"><span class="text-amber-400 font-bold">✔</span><span class="text-slate-200">{p}</span></li>' for p in points])

        s_html = ""
        if sample_imgs:
            s_html = '<div class="grid grid-cols-3 gap-2 mt-3">'
            for s in sample_imgs:
                s_html += f'<img src="{s}" alt="{title} サンプル" class="rounded-lg object-cover h-20 md:h-24 w-full border border-slate-700/50" loading="lazy" />'
            s_html += '</div>'

        cards_html += f'''
        <!-- 作品紹介カード：第{rank}位 -->
        <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-6">
          <div class="flex flex-col md:flex-row gap-6 items-center md:items-start">
            <div class="w-full md:w-1/3 flex-shrink-0">
              <div class="relative rounded-2xl overflow-hidden shadow-lg border border-slate-700/60 group">
                <img src="{pkg}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
                <div class="absolute top-3 left-3 bg-gradient-to-r from-amber-500 to-rose-600 text-white text-xs font-black px-3 py-1 rounded-full shadow-lg">
                  第{rank}位
                </div>
              </div>
              {s_html}
            </div>
            <div class="w-full md:w-2/3 flex flex-col justify-between space-y-4">
              <div>
                <div class="inline-block px-3 py-1 bg-rose-500/10 border border-rose-500/20 rounded-full text-rose-300 text-xs font-bold mb-2">
                  {badge}
                </div>
                <h2 class="text-xl md:text-2xl font-bold text-white leading-snug">
                  <a href="/posts/{cid}" class="hover:text-rose-400 transition">{title}</a>
                </h2>
                <div class="text-xs text-slate-400 mt-2">
                  <strong>出演：</strong> {actress_links if actress_links else '厳選キャスト'}
                </div>
              </div>

              <div class="bg-slate-800/50 rounded-2xl p-4 border border-slate-700/40">
                <div class="text-xs font-bold text-amber-400 uppercase tracking-wider mb-2">💡 厳選おすすめポイント</div>
                <ul class="space-y-1.5 text-xs md:text-sm">
                  {points_li}
                </ul>
              </div>

              <div class="flex flex-col sm:flex-row gap-3 pt-2">
                <a href="/posts/{cid}" class="flex-1 inline-flex items-center justify-center px-6 py-3 bg-slate-800 hover:bg-slate-700 border border-slate-600/50 text-white font-bold rounded-xl transition text-sm gap-1.5">
                  <span>📖 個別詳細レビューを読む</span>
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                </a>
                <a href="{aff_url}" target="_blank" rel="noopener noreferrer" class="flex-1 inline-flex items-center justify-center px-6 py-3 bg-gradient-to-r from-rose-600 to-amber-500 hover:from-rose-500 hover:to-amber-400 text-white font-extrabold rounded-xl shadow-lg transition text-sm gap-1.5">
                  <span>🎬 公式で無料サンプルを見る</span>
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                </a>
              </div>
            </div>
          </div>
        </div>'''

    # 深層分析セクション
    deep_dive_section = ""
    if deep_dive_title and deep_dive_content:
        deep_dive_section = f'''
        <!-- 深層分析セクション -->
        <div class="bg-gradient-to-br from-slate-900 via-slate-900 to-indigo-950 border border-slate-800 rounded-3xl p-6 md:p-10 shadow-xl space-y-4 my-8">
          <div class="inline-flex items-center gap-2 px-3 py-1 bg-indigo-500/20 border border-indigo-500/30 rounded-full text-indigo-300 text-xs font-bold">
            <span>🧠</span> 徹底考察＆心理学的分析
          </div>
          <h2 class="text-xl md:text-2xl font-extrabold text-white">
            {deep_dive_title}
          </h2>
          {deep_dive_content}
        </div>'''

    # FAQセクション
    faq_html = ""
    if faq_items:
        faq_blocks = ""
        for item in faq_items:
            faq_blocks += f'''
            <div class="bg-slate-800/40 border border-slate-700/50 rounded-2xl p-4 md:p-5 space-y-2">
              <h3 class="text-sm md:text-base font-bold text-amber-300 flex items-start gap-2">
                <span class="text-rose-400 font-extrabold">Q.</span>
                <span>{item["q"]}</span>
              </h3>
              <p class="text-xs md:text-sm text-slate-300 leading-relaxed pl-6">
                {item["a"]}
              </p>
            </div>'''
        faq_html = f'''
        <!-- よくある質問セクション -->
        <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-10 shadow-xl space-y-6 my-8">
          <div class="flex items-center gap-2">
            <span class="text-xl">❓</span>
            <h2 class="text-xl md:text-2xl font-extrabold text-white">よくある質問（FAQ）</h2>
          </div>
          <div class="space-y-4">
            {faq_blocks}
          </div>
        </div>'''

    # 関連検索キーワード＆内部リンク
    related_html = ""
    if related_searches:
        rel_tags = " ".join([f'<span class="bg-slate-800 text-slate-300 px-3 py-1.5 rounded-full text-xs font-medium border border-slate-700/60">#{kw}</span>' for kw in related_searches])
        related_html = f'''
        <!-- 関連キーワード -->
        <div class="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 shadow-lg space-y-3 my-8">
          <h3 class="text-xs font-bold text-slate-400 uppercase tracking-wider">🏷️ 関連トピックス・検索タグ</h3>
          <div class="flex flex-wrap gap-2">
            {rel_tags}
          </div>
        </div>'''

    feature_body = f'''<!-- 特集記事コンテナ -->
<div class="space-y-8">
  <!-- 導入リード文セクション -->
  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-10 shadow-2xl space-y-4">
    <div class="inline-flex items-center gap-2 px-3.5 py-1.5 bg-rose-500/10 border border-rose-500/20 rounded-full text-rose-300 text-xs font-bold tracking-wider uppercase">
      <span>🔥</span> FANZA公式 厳選キラー特集
    </div>
    <h1 class="text-2xl md:text-3xl lg:text-4xl font-extrabold text-white leading-tight">
      {f_title}
    </h1>
    <div class="text-sm md:text-base text-slate-300 leading-relaxed space-y-3 pt-2">
      <p>{lead_p1}</p>
      <p>{lead_p2}</p>
    </div>
  </div>

  <!-- 一目でわかる厳選TOP5比較サマリー表 -->
  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl">
    <h2 class="text-lg md:text-xl font-bold text-white mb-4 flex items-center gap-2">
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
        "date": "2026-10-31 01:00:00",
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
    print("=== Start generating 3 new killer features & 15 reviews (v24) ===")
    
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
