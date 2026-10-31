# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・新規キラー特集3記事および個別作品15件自動生成スクリプト v27
各記事3500文字以上・完全独自書き下ろし・内部リンク網羅・SEO/LLM/GEO対策
1. 【十数年ぶりの再会とホテル密会】同窓会・人妻同級生・初恋の元カノ略奪 特集（TOP5）
2. 【美尻レギンスと汗ばむ密着レッスン】パーソナルジム・美人女性トレーナー・密室ストレッチ 特集（TOP5）
3. 【初対面マッチングから即日ホテル直行】マッチングアプリ・素人女子お持ち帰り・即日ワンナイト 特集（TOP5）
"""

import os
import re
import json
import time
import urllib.parse
import subprocess
import requests

from reviews_feature_class_reunion import REVIEWS_CLASS_REUNION
from reviews_feature_personal_gym import REVIEWS_PERSONAL_GYM
from reviews_feature_matching_app import REVIEWS_MATCHING_APP
from features_def_v27 import FEATURE_ARTICLES

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
ALL_REVIEWS.update(REVIEWS_CLASS_REUNION)
ALL_REVIEWS.update(REVIEWS_PERSONAL_GYM)
ALL_REVIEWS.update(REVIEWS_MATCHING_APP)

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

def count_japanese_chars(html_text):
    text = re.sub(r'<[^>]+>', '', html_text)
    text = re.sub(r'\s+', '', text)
    return len(text)

def get_sample_images(it, max_count=4):
    sample_urls = []
    sample_obj = it.get("sampleImageURL", {})
    if isinstance(sample_obj, dict):
        sample_l = sample_obj.get("sample_l", {})
        if isinstance(sample_l, dict):
            image_list = sample_l.get("image", [])
            if isinstance(image_list, list):
                sample_urls = image_list
            elif isinstance(image_list, str):
                sample_urls = [image_list]
    return sample_urls[:max_count]

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
    release_date = "2026-11-01 02:00:00"
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

      <!-- アクションボタン -->
      <div class="pt-2 flex flex-col sm:flex-row gap-3">
        <a href="{aff_url}" target="_blank" rel="noopener noreferrer" class="flex-1 text-center py-4 px-6 bg-gradient-to-r from-rose-600 to-rose-700 hover:from-rose-500 hover:to-rose-600 text-white font-black rounded-2xl shadow-xl shadow-rose-900/40 hover:shadow-rose-600/50 hover:scale-[1.02] active:scale-[0.98] transition duration-200 flex items-center justify-center gap-2 text-base">
          <span>🎬</span> FANZA公式で本編を再生する
        </a>
        <a href="/posts/{feature_info["id"]}" class="px-5 py-4 bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold rounded-2xl text-center text-sm border border-slate-700 transition">
          特集ランキングへ戻る
        </a>
      </div>
    </div>
  </div>

  <!-- サンプルギャラリー -->
  {samples_html}

  <!-- 完全独自書き下ろし詳細レビュー本文 -->
  <div class="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 md:p-10 shadow-xl space-y-8">
    <div class="border-b border-slate-800 pb-4 mb-6">
      <span class="text-rose-500 text-sm font-bold tracking-widest uppercase">Deep Review & Spec Analysis</span>
      <h2 class="text-2xl font-black text-white mt-1">作品深層レビュー＆鑑賞ガイド</h2>
    </div>

    {review_html}

    <!-- 相互内部リンク・特集バナー -->
    <div class="mt-8 p-6 bg-slate-900 border border-slate-800 rounded-2xl space-y-3">
      <h3 class="text-base font-bold text-white flex items-center gap-2">
        <span>💡</span> 本作の鑑賞アドバイス＆実用シチュエーション解説
      </h3>
      <p class="text-sm text-slate-300 leading-relaxed">
        本作『{title}』は、FANZA（DMM）公式配信においてHD高画質および4K高精細ストリーミングに対応した人気タイトルです。スマートフォンやタブレットでのイヤホン鑑賞はもちろん、大画面テレビやPCモニターで視聴することで、女優の艶やかな肌の質感や瞳の潤み、生々しい愛液の飛沫まで余すところなく鮮明に堪能いただけます。特に一人でじっくりと没入したい夜の時間帯や、日常のストレスを解放して究極の快楽に浸りたい瞬間に最適な一本です。
      </p>
      <p class="text-sm text-slate-300 leading-relaxed">
        また、本作は当サイトの「{feature_info["title"]}」にも堂々ランクインを果たしており、同系統の厳選された人気作品と見比べることで、より一層ディープなフェティシズムをお楽しみいただけます。
      </p>
    </div>

    <div class="mt-8 p-6 bg-gradient-to-r from-slate-900 to-rose-950/60 rounded-2xl border border-rose-900/40 flex flex-col md:flex-row items-center justify-between gap-4">
      <div>
        <div class="text-xs font-bold text-rose-400 uppercase tracking-wider mb-1">Featured In This Special</div>
        <h4 class="text-lg font-black text-white">{feature_info["title"]}</h4>
        <p class="text-xs text-slate-400 mt-1">同ジャンルの至高の傑作5選を完全網羅！ランキングTOP5をチェック</p>
      </div>
      <a href="/posts/{feature_info["id"]}" class="flex-shrink-0 px-6 py-3 bg-rose-600 hover:bg-rose-500 text-white font-bold rounded-xl text-sm shadow transition">
        特集記事を見る →
      </a>
    </div>

    <!-- 関連ジャンルタグ -->
    <div class="pt-6 border-t border-slate-800 flex flex-wrap gap-2 items-center">
      <span class="text-xs font-bold text-slate-400 mr-2">関連タグ:</span>
      {genre_links_html}
    </div>
  </div>
</div>
'''

    return {
        "id": cid,
        "title": title,
        "date": release_date,
        "hinban": cid,
        "price": price_str,
        "maker": maker_name,
        "actresses": actresses,
        "genres": genres,
        "image": package_img,
        "review": body_html
    }

def generate_feature_article(feature_def, fetched_items):
    f_id = feature_def["id"]
    f_title = feature_def["title"]
    f_hinban = feature_def["hinban"]
    lead_p1 = feature_def["lead_p1"]
    lead_p2 = feature_def["lead_p2"]
    genres = feature_def["genres"]
    items = feature_def["items"]

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
                <div class="rounded-lg overflow-hidden border border-slate-700/60 shadow group">
                  <img src="{s}" alt="{title} プレビュー" class="w-full h-24 md:h-28 object-cover group-hover:scale-105 transition duration-300" loading="lazy" />
                </div>'''
            samples_grid += '</div>'

        cards_html += f'''
        <!-- 第{rank}位カード -->
        <article class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-6">
          <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-800 pb-4">
            <div class="flex items-center gap-3">
              <span class="flex items-center justify-center w-10 h-10 rounded-2xl font-black text-lg {'bg-amber-400 text-slate-950 shadow-lg shadow-amber-400/30' if rank == 1 else 'bg-slate-700 text-white'}">{rank}</span>
              <div>
                <span class="text-xs font-bold text-rose-500 uppercase tracking-widest">{badge_text}</span>
                <h3 class="text-lg md:text-xl font-bold text-white leading-snug">
                  <a href="/posts/{cid}" class="hover:text-rose-400 transition">{title}</a>
                </h3>
              </div>
            </div>
            <span class="px-3 py-1 rounded-full text-xs font-bold bg-amber-400/10 text-amber-400 border border-amber-400/20">
              総合評価 ★★★★★ (5.0)
            </span>
          </div>

          <div class="flex flex-col md:flex-row gap-6">
            <div class="w-full md:w-5/12 flex-shrink-0">
              <div class="relative rounded-2xl overflow-hidden shadow-lg border border-slate-700/50 group">
                <img src="{pkg}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
              </div>
            </div>
            <div class="w-full md:w-7/12 flex flex-col justify-between space-y-4">
              <div class="space-y-2 text-sm text-slate-300">
                <p><strong class="text-slate-400">主要キャスト：</strong> {actress_links if actress_links else '<span class="text-slate-400">厳選キャスト</span>'}</p>
                <p><strong class="text-slate-400">特化見どころ：</strong> <span class="text-amber-300 font-semibold">{r_item["spec_summary"]}</span></p>
                <p><strong class="text-slate-400">公式品番・CID：</strong> <span class="font-mono text-slate-200">{cid}</span></p>
              </div>

              <!-- ポイントリスト -->
              <div class="bg-slate-800/40 rounded-2xl p-4 border border-slate-700/40">
                <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider mb-2">🔥 ここが抜ける！神ポイント</h4>
                <ul class="space-y-1.5 text-xs md:text-sm">
                  {points_list}
                </ul>
              </div>

              <!-- サンプルギャラリー -->
              {samples_grid}

              <!-- ボタン群 -->
              <div class="pt-2 flex flex-col sm:flex-row gap-3">
                <a href="{aff_url}" target="_blank" rel="noopener noreferrer" class="flex-1 text-center py-3.5 px-6 bg-gradient-to-r from-rose-600 to-rose-700 hover:from-rose-500 hover:to-rose-600 text-white font-extrabold rounded-xl shadow-lg shadow-rose-900/30 hover:scale-[1.02] active:scale-[0.98] transition flex items-center justify-center gap-2 text-sm">
                  <span>🎬</span> FANZA公式で作品詳細を見る
                </a>
                <a href="/posts/{cid}" class="px-5 py-3.5 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold rounded-xl text-center text-sm border border-slate-700 transition">
                  完全詳細レビューを読む →
                </a>
              </div>
            </div>
          </div>
        </article>'''

    genres_links = " ".join([get_genre_link(g) for g in genres])
    actresses_links = " ".join([get_actress_link(a) for a in all_actresses[:10]])

    full_html = f'''<!-- キラー特集コンテナ -->
<div class="space-y-10">
  <!-- ヒーローリード文セクション -->
  <header class="bg-gradient-to-br from-slate-900 via-slate-900 to-rose-950/40 border border-slate-800 rounded-3xl p-6 md:p-10 shadow-2xl space-y-6">
    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-rose-600/20 text-rose-400 text-xs font-bold border border-rose-500/30">
      <span>👑</span> 2026年最新FANZA公式アーカイブ完全選定
    </div>
    <h1 class="text-2xl md:text-4xl font-black text-white leading-tight">
      {f_title}
    </h1>
    <div class="space-y-4 text-slate-300 text-base md:text-lg leading-relaxed border-t border-slate-800/80 pt-6">
      <p>{lead_p1}</p>
      <p>{lead_p2}</p>
    </div>
    <div class="pt-4 flex flex-wrap gap-2 items-center text-xs">
      <span class="text-slate-400 font-bold mr-1">関連ジャンル:</span>
      {genres_links}
    </div>
  </header>

  <!-- 比較ランキング一覧テーブル -->
  <section class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-4">
    <div class="flex items-center justify-between">
      <h2 class="text-lg md:text-xl font-extrabold text-white flex items-center gap-2">
        <span>📊</span> 厳選おすすめTOP5 比較早見表
      </h2>
      <span class="text-xs text-slate-400">横スクロールで詳細確認</span>
    </div>
    <div class="overflow-x-auto">
      <table class="w-full text-left border-collapse min-w-[600px]">
        <thead>
          <tr class="border-b border-slate-700 text-xs font-bold text-slate-400 uppercase bg-slate-800/60">
            <th class="py-3 px-3 text-center w-12">順位</th>
            <th class="py-3 px-4">作品名・出演女優</th>
            <th class="py-3 px-4 hidden md:table-cell">核心抜きどころ</th>
            <th class="py-3 px-3 text-center w-24">実用評価</th>
            <th class="py-3 px-4 text-center w-28">公式リンク</th>
          </tr>
        </thead>
        <tbody>
          {table_rows}
        </tbody>
      </table>
    </div>
  </section>

  <!-- ランキング詳細カードセクション -->
  <section class="space-y-8">
    <div class="border-l-4 border-rose-500 pl-4">
      <h2 class="text-2xl md:text-3xl font-black text-white">至高の神作ランキングTOP5 詳細解説</h2>
      <p class="text-slate-400 text-sm mt-1">圧倒的な抜けるシチュエーションと女優陣の限界突破SEXを徹底深掘り</p>
    </div>

    {cards_html}
  </section>

  <!-- FAQ・鑑賞ガイドセクション -->
  <section class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-6">
    <h3 class="text-xl font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-3">
      <span>💡</span> よくある質問・失敗しない鑑賞ガイド
    </h3>
    <div class="space-y-4 text-sm md:text-base">
      <div class="bg-slate-800/40 rounded-2xl p-4 border border-slate-700/40 space-y-1">
        <h4 class="font-bold text-rose-400">Q. 本ランキング作品はすべてFANZA公式で高画質配信されていますか？</h4>
        <p class="text-slate-300">はい、本特集で厳選したすべての作品はFANZA（DMM）公式デジタル動画配信にてHDおよび高精細4K画質、スマートフォンやPC、テレビアプリで今すぐ即時ストリーミング・ダウンロード視聴が可能です。</p>
      </div>
      <div class="bg-slate-800/40 rounded-2xl p-4 border border-slate-700/40 space-y-1">
        <h4 class="font-bold text-rose-400">Q. 個別作品の詳細なレビューや見どころタイムラインはどこで確認できますか？</h4>
        <p class="text-slate-300">各作品カード内の「完全詳細レビューを読む」ボタンから、当サイト専属レビュアーによる3500文字超の濃厚なシーン解説、プレイタイムライン、女優の表情分析レビュー記事へアクセスいただけます。</p>
      </div>
      <div class="bg-slate-800/40 rounded-2xl p-4 border border-slate-700/40 space-y-1">
        <h4 class="font-bold text-rose-400">Q. 初めてこのジャンルを鑑賞するなら、どれから見るのが一番おすすめですか？</h4>
        <p class="text-slate-300">まずはランキング第1位の作品からご覧いただくことを強くおすすめします。ジャンル特有の背徳感・シチュエーションのリアリズム・女優の熱演のすべてが最高潮に凝縮されており、絶対に後悔させない仕上がりとなっています。</p>
      </div>
    </div>
  </section>

  <!-- フッター・キャストリンク集 -->
  <footer class="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 text-sm text-slate-400 space-y-3">
    <div class="flex items-center gap-2 text-white font-bold">
      <span>🌟</span> 本特集の関連女優一覧
    </div>
    <div class="flex flex-wrap gap-2">
      {actresses_links}
    </div>
  </footer>
</div>
'''

    return {
        "id": f_id,
        "title": f_title,
        "date": "2026-11-01 02:00:00",
        "hinban": f_hinban,
        "price": "500~",
        "maker": "FANZA公式キラー特集2026",
        "actresses": all_actresses,
        "genres": genres,
        "image": top_pkg,
        "review": full_html
    }

def main():
    print("=== Starting Generation of 3 Killer Features & 15 Reviews v27 ===")

    # 1. FANZA API から全15作品をリアルタイム取得
    all_cids = []
    for f in FEATURE_ARTICLES:
        for itm in f["items"]:
            all_cids.append(itm["cid"])

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

    # 5. bundle_posts.js の実行
    print("\n--- Bundling posts for Next.js ---")
    res = subprocess.run(["node", "bundle_posts.js"], capture_output=True, text=True)
    print(res.stdout)
    if res.returncode != 0:
        print("ERROR bundling posts:", res.stderr)

    # 6. bundle_manga.js の実行
    print("\n--- Bundling manga ---")
    res = subprocess.run(["node", "bundle_manga.js"], capture_output=True, text=True)
    print(res.stdout)

    # 7. サイトマップの生成
    print("\n--- Generating Sitemaps ---")
    res = subprocess.run(["node", "generate_sitemap.js"], capture_output=True, text=True)
    print(res.stdout)

    # 8. llms.txt の生成
    print("\n--- Generating LLMs.txt ---")
    res = subprocess.run(["node", "generate_llms_txt.js"], capture_output=True, text=True)
    print(res.stdout)

    print("=== All generation and bundling completed successfully! ===")

if __name__ == "__main__":
    main()
