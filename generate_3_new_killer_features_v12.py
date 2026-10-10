# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・新規キラー特集3記事および個別作品15件自動生成スクリプト v12
各記事3000文字以上・完全独自書き下ろし・内部リンク網羅・SEO/LLM/GEO対策
1. 同窓会・初恋の元カノ人妻・再会不倫特集
2. ナース・白衣の天使・夜勤病棟の秘密看護特集
3. 小悪魔後輩・あざと生意気女子社員の逆誘惑特集
"""

import os
import re
import json
import time
import urllib.parse
import requests

from reviews_feature_reunion import REVIEWS_PART1
from reviews_feature_nurse import REVIEWS_PART2
from reviews_feature_junior import REVIEWS_PART3
from features_def_v12 import FEATURE_ARTICLES

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
ALL_REVIEWS.update(REVIEWS_PART1)
ALL_REVIEWS.update(REVIEWS_PART2)
ALL_REVIEWS.update(REVIEWS_PART3)

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

def main():
    print("=== STARTING GENERATION FOR 3 KILLER FEATURES & 15 INDIVIDUAL POSTS (v12) ===")
    
    # 1. 15作品の個別記事作成
    print("\n--- Phase 1: Generating 15 Individual Posts with >3,000 Chars ---")
    
    individual_success = 0
    feature_success = 0

    for art in FEATURE_ARTICLES:
        print(f"\nProcessing feature items for: {art['title'][:40]}...")
        for it_def in art["items"]:
            cid = it_def["cid"]
            print(f" -> Fetching FANZA API for CID: {cid}...")
            it = fetch_fanza_item(cid)
            if not it:
                print(f" [ERROR] Could not fetch data for CID: {cid}")
                continue
            
            title = it.get("title", "")
            img_l = it.get("imageURL", {}).get("large", "")
            aff_url = it.get("affiliate_url_clean") or it.get("affiliateURL", "")
            actresses = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
            genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
            maker = it.get("iteminfo", {}).get("maker", [{}])[0].get("name", "FANZA")
            price = it.get("prices", {}).get("price", "500~")
            samples = get_sample_images(it, 4)
            
            actress_links_html = " ".join([get_actress_link(a) for a in actresses])
            genre_links_html = " ".join([get_genre_link(g) for g in genres[:8]])
            
            points_list = "".join([f'<li class="flex items-start gap-2"><span class="text-amber-400 font-bold">✔</span><span class="text-slate-200">{p}</span></li>' for p in it_def["points"]])
            
            sample_gallery_html = ""
            if samples:
                gallery_cards = []
                for idx, s_url in enumerate(samples):
                    gallery_cards.append(f"""    <div class="relative rounded-2xl overflow-hidden bg-slate-800 border border-slate-700/60 shadow group">
      <img src="{s_url}" alt="{title} シーン画像{idx+1}" class="w-full h-auto object-cover transform group-hover:scale-105 transition duration-300" loading="lazy" />
      <div class="absolute bottom-2 left-2 bg-black/70 backdrop-blur-md px-2 py-0.5 rounded text-[10px] text-slate-300">プレビュー #{idx+1}</div>
    </div>""")
                sample_gallery_html = f"""<div class="my-8">
  <h3 class="text-lg md:text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>📸</span> 高画質シーンプレビュー
  </h3>
  <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
{''.join(gallery_cards)}
  </div>
</div>"""

            review_body = ALL_REVIEWS.get(cid, f"<p>{title}の超濃密レビューです。</p>")
            
            individual_html = f"""<!-- 個別作品詳細レビューコンテナ -->
<div class="space-y-6">
  <!-- パッケージ＆基本情報カード -->
  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-2xl flex flex-col md:flex-row gap-6 items-center md:items-start">
    <div class="w-full md:w-1/3 flex-shrink-0">
      <div class="relative rounded-2xl overflow-hidden shadow-xl border border-slate-700/50 group">
        <img src="{img_l}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="eager" />
        <div class="absolute top-3 left-3 bg-rose-600/90 text-white text-xs font-bold px-3 py-1 rounded-full shadow-lg backdrop-blur-sm">
          厳選神作
        </div>
      </div>
    </div>
    <div class="w-full md:w-2/3 flex flex-col justify-between space-y-4">
      <div>
        <div class="text-xs font-bold text-amber-400 tracking-wider uppercase mb-1">{maker}</div>
        <h1 class="text-xl md:text-2xl font-extrabold text-white leading-snug">{title}</h1>
      </div>
      <div class="space-y-2 text-sm text-slate-300">
        <p><strong class="text-slate-400">出演女優：</strong> {actress_links_html or '単体・企画女優'}</p>
        <p><strong class="text-slate-400">配信形式：</strong> 動画配信（HD / 4Kストリーミング＆ダウンロード）</p>
        <p><strong class="text-slate-400">品番・CID：</strong> <span class="font-mono text-slate-200">{cid}</span></p>
        <p><strong class="text-slate-400">特化ポイント：</strong> <span class="text-amber-300 font-semibold">{it_def['spec_summary']}</span></p>
      </div>

      <!-- キラーポイント箇条書き -->
      <div class="bg-slate-800/40 rounded-2xl p-4 border border-slate-700/40">
        <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider mb-2">🔥 本作の抜きどころ・実用ポイント</h4>
        <ul class="space-y-1.5 text-xs md:text-sm">
{points_list}
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

  <!-- シーン画像ギャラリー -->
  {sample_gallery_html}

  <!-- 本文詳細レビュー -->
  <div class="bg-slate-900/90 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl text-slate-200 leading-relaxed space-y-6 prose prose-invert max-w-none">
    {review_body}
  </div>

  <!-- 特集への逆リンクバナー -->
  <div class="bg-gradient-to-r from-slate-900 to-indigo-950/60 border border-indigo-500/30 rounded-3xl p-6 text-center shadow-xl">
    <h3 class="text-lg font-bold text-white mb-2">📌 この作品が選出された特集ランキング</h3>
    <p class="text-slate-300 text-sm mb-4">{art['title']}</p>
    <a href="/posts/{art['id']}" class="inline-flex items-center gap-2 px-6 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white font-bold rounded-xl transition text-sm">
      <span>🏆 特集ランキングTOP5をチェックする</span>
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
    </a>
  </div>
</div>"""

            c_count = count_japanese_chars(individual_html)
            print(f"    -> [Post {cid}] Char count: {c_count} chars (Requirement >= 3000)")
            if c_count < 3000:
                print(f"    [WARNING] Char count below 3000 for {cid}: {c_count}")

            post_json = {
                "id": cid,
                "title": title,
                "date": it.get("date", "2026-10-10 12:00:00"),
                "hinban": cid,
                "price": str(price),
                "maker": maker,
                "actresses": actresses,
                "genres": genres,
                "image": img_l,
                "review": individual_html
            }

            file_path = os.path.join(OUTPUT_DIR, f"{cid}.json")
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(post_json, f, ensure_ascii=False, indent=2)
            print(f"    -> Saved post: {file_path}")
            individual_success += 1

    # 2. 3大特集記事の作成
    print("\n--- Phase 2: Generating 3 Killer Feature Articles with >8,000 Chars ---")
    
    for art_idx, art in enumerate(FEATURE_ARTICLES, 1):
        art_id = art["id"]
        art_title = art["title"]
        print(f"\n==========================================")
        print(f"[{art_idx}/3] Building Feature Article: {art_title[:50]}...")
        print(f"==========================================")

        items_data = []
        for it_def in art["items"]:
            cid = it_def["cid"]
            print(f" -> Fetching data for feature item: {cid}...")
            it = fetch_fanza_item(cid)
            if it:
                it["spec_summary"] = it_def["spec_summary"]
                it["badge"] = it_def["badge"]
                it["points"] = it_def["points"]
                it["rank"] = it_def["rank"]
                it["review_body"] = ALL_REVIEWS.get(cid, "")
                items_data.append(it)
            time.sleep(0.3)

        if not items_data:
            print(f" [ERROR] No items found for feature {art_id}")
            continue

        lead_p1 = art["lead_p1"]
        lead_p2 = art["lead_p2"]

        # 比較テーブル作成
        table_rows = []
        for it in items_data:
            cid = it.get("content_id", "")
            title = it.get("title", "")
            actresses = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
            act_str = ", ".join(actresses) if actresses else "単体女優"
            aff_url = it.get("affiliate_url_clean") or it.get("affiliateURL", "")
            img_s = it.get("imageURL", {}).get("small") or it.get("imageURL", {}).get("large", "")
            
            table_rows.append(f"""          <tr class="border-b border-slate-800 hover:bg-slate-800/50 transition">
            <td class="py-4 px-3 text-center">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-full bg-gradient-to-br from-amber-500 to-rose-600 text-white font-extrabold text-sm shadow">
                {it['rank']}
              </span>
            </td>
            <td class="py-4 px-3">
              <div class="flex items-center gap-3">
                <img src="{img_s}" alt="{title}" class="w-14 h-19 object-cover rounded shadow border border-slate-700/60 flex-shrink-0" loading="lazy" />
                <div>
                  <a href="/posts/{cid}" class="text-white hover:text-rose-400 font-bold text-xs md:text-sm line-clamp-2 transition leading-tight">
                    {title}
                  </a>
                  <div class="text-[11px] text-rose-300 mt-1 font-semibold">{act_str}</div>
                </div>
              </div>
            </td>
            <td class="py-4 px-3 text-xs text-slate-300 hidden md:table-cell">
              {it['spec_summary']}
            </td>
            <td class="py-4 px-3 text-center">
              <span class="text-amber-400 font-extrabold text-xs md:text-sm">★★★★★</span>
              <div class="text-[10px] text-slate-400">殿堂認定</div>
            </td>
            <td class="py-4 px-3 text-center">
              <a href="{aff_url}" target="_blank" rel="noopener noreferrer" class="inline-block px-3 py-1.5 bg-rose-600 hover:bg-rose-500 text-white text-xs font-bold rounded-lg shadow transition whitespace-nowrap">
                公式視聴
              </a>
            </td>
          </tr>""")

        comparison_table_html = f"""<div class="my-10 bg-slate-900 border border-slate-800 rounded-3xl p-4 md:p-6 shadow-2xl">
  <h3 class="text-lg md:text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>📊</span> 厳選TOP5 スペック＆抜きどころ徹底比較表
  </h3>
  <div class="overflow-x-auto">
    <table class="w-full text-left text-sm text-slate-300">
      <thead class="text-xs uppercase bg-slate-800/80 text-amber-400 border-b border-slate-700">
        <tr>
          <th class="py-3 px-3 text-center">順位</th>
          <th class="py-3 px-3">作品タイトル / 主演</th>
          <th class="py-3 px-3 hidden md:table-cell">特化ポイント</th>
          <th class="py-3 px-3 text-center">おすすめ度</th>
          <th class="py-3 px-3 text-center">詳細</th>
        </tr>
      </thead>
      <tbody>
{''.join(table_rows)}
      </tbody>
    </table>
  </div>
</div>"""

        # 各作品の詳細カード作成
        ranking_sections = []
        for it in items_data:
            cid = it.get("content_id", "")
            title = it.get("title", "")
            img_l = it.get("imageURL", {}).get("large", "")
            aff_url = it.get("affiliate_url_clean") or it.get("affiliateURL", "")
            actresses = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
            genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
            maker = it.get("iteminfo", {}).get("maker", [{}])[0].get("name", "FANZA")
            samples = get_sample_images(it, 4)
            
            actress_links_html = " ".join([get_actress_link(a) for a in actresses])
            genre_links_html = " ".join([get_genre_link(g) for g in genres[:6]])
            points_list = "".join([f'<li class="flex items-start gap-2"><span class="text-amber-400 font-bold">✔</span><span class="text-slate-200">{p}</span></li>' for p in it["points"]])
            
            sample_gallery_html = ""
            if samples:
                gallery_cards = []
                for idx, s_url in enumerate(samples):
                    gallery_cards.append(f"""        <div class="relative rounded-xl overflow-hidden bg-slate-800 border border-slate-700/60 shadow group">
          <img src="{s_url}" alt="{title} プレビュー{idx+1}" class="w-full h-auto object-cover transform group-hover:scale-105 transition duration-300" loading="lazy" />
          <div class="absolute bottom-1.5 left-1.5 bg-black/70 backdrop-blur-md px-1.5 py-0.5 rounded text-[9px] text-slate-300">シーン #{idx+1}</div>
        </div>""")
                sample_gallery_html = f"""<div class="my-6">
  <div class="text-xs font-bold text-slate-400 mb-2">📸 本編プレビューギャラリー</div>
  <div class="grid grid-cols-2 md:grid-cols-4 gap-2.5">
{''.join(gallery_cards)}
  </div>
</div>"""

            ranking_sections.append(f"""<!-- 第{it['rank']}位: {title} -->
<div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-2xl space-y-6">
  <div class="flex flex-col md:flex-row gap-6 items-center md:items-start">
    <div class="w-full md:w-1/3 flex-shrink-0">
      <div class="relative rounded-2xl overflow-hidden shadow-2xl border border-slate-700/60 group">
        <img src="{img_l}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute top-3 left-3 bg-gradient-to-r from-amber-500 to-rose-600 text-white font-extrabold text-sm px-3.5 py-1 rounded-full shadow-lg">
          第{it['rank']}位
        </div>
      </div>
    </div>
    <div class="w-full md:w-2/3 flex flex-col justify-between space-y-4">
      <div>
        <div class="inline-block bg-rose-500/20 text-rose-300 border border-rose-500/30 text-xs font-bold px-3 py-1 rounded-full mb-2">
          {it['badge']}
        </div>
        <h3 class="text-xl md:text-2xl font-extrabold text-white leading-snug">
          <a href="/posts/{cid}" class="hover:text-rose-400 transition">{title}</a>
        </h3>
      </div>
      
      <div class="space-y-1.5 text-sm text-slate-300">
        <p><strong class="text-slate-400">主演女優：</strong> {actress_links_html or '単体女優'}</p>
        <p><strong class="text-slate-400">メーカー：</strong> <span class="text-slate-200">{maker}</span></p>
        <p><strong class="text-slate-400">品番・CID：</strong> <span class="font-mono text-slate-300">{cid}</span></p>
        <p><strong class="text-slate-400">特化ポイント：</strong> <span class="text-amber-300 font-semibold">{it['spec_summary']}</span></p>
      </div>

      <div class="bg-slate-800/40 rounded-2xl p-4 border border-slate-700/40">
        <div class="text-xs font-bold text-amber-400 uppercase tracking-wider mb-2">🔥 圧倒的抜きどころハイライト</div>
        <ul class="space-y-1.5 text-xs md:text-sm">
{points_list}
        </ul>
      </div>

      <div class="flex flex-wrap gap-1.5 pt-1">
        {genre_links_html}
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

  <!-- シーン画像ギャラリー -->
  {sample_gallery_html}

  <!-- 作品個別レビュー全文埋め込み -->
  <div class="bg-slate-950/70 border border-slate-800/80 rounded-2xl p-5 md:p-7 text-slate-300 leading-relaxed space-y-5 prose prose-invert max-w-none text-sm md:text-base">
    {it['review_body']}
  </div>
</div>""")

        # FAQセクション
        faq_cards = []
        faq_json_ld = []
        for q, a in art["faqs"]:
            faq_cards.append(f"""    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 md:p-6 shadow">
      <h4 class="text-base md:text-lg font-bold text-white mb-2 flex items-start gap-2">
        <span class="text-rose-500 font-black">Q.</span>
        <span>{q}</span>
      </h4>
      <p class="text-slate-300 text-sm leading-relaxed pl-6">
        <span class="text-amber-400 font-bold mr-1">A.</span>{a}
      </p>
    </div>""")
            faq_json_ld.append({
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": a
                }
            })

        faq_html = f"""<div class="my-10 space-y-4">
  <h3 class="text-lg md:text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>❓</span> よくある質問・鑑賞ガイド（FAQ）
  </h3>
{''.join(faq_cards)}
</div>
<script type="application/ld+json">
{json.dumps({
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": faq_json_ld
}, ensure_ascii=False, indent=2)}
</script>"""

        # 内部リンク（関連特集）
        related_cards = []
        for rel_url, rel_title, rel_desc in art["related"]:
            related_cards.append(f"""    <a href="{rel_url}" class="block bg-slate-900 border border-slate-800 hover:border-rose-500/50 rounded-2xl p-5 shadow-lg group transition duration-300">
      <div class="text-xs font-bold text-amber-400 mb-1">RECOMMENDED FEATURE</div>
      <h4 class="text-base font-bold text-white group-hover:text-rose-400 transition mb-2">{rel_title}</h4>
      <p class="text-xs text-slate-400 line-clamp-2">{rel_desc}</p>
    </a>""")

        related_html = f"""<div class="my-12">
  <h3 class="text-lg md:text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>🔗</span> あわせて読みたい厳選キラー特集
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
{''.join(related_cards)}
  </div>
</div>"""

        feature_html = f"""<!-- 特集記事コンテナ -->
<div class="space-y-8">
  <!-- リード文セクション -->
  <div class="bg-gradient-to-br from-slate-900 via-slate-900 to-indigo-950/40 border border-slate-800 rounded-3xl p-6 md:p-10 shadow-2xl space-y-4">
    <div class="inline-flex items-center gap-2 bg-gradient-to-r from-rose-500/20 to-amber-500/20 text-rose-300 border border-rose-500/30 text-xs font-extrabold px-3.5 py-1.5 rounded-full uppercase tracking-wider">
      <span>🏆</span> 2026年最新FANZA公式売上＆実用度データ徹底解析
    </div>
    <h1 class="text-2xl md:text-4xl font-black text-white leading-tight">
      {art_title}
    </h1>
    <div class="text-slate-300 leading-relaxed space-y-4 text-sm md:text-base pt-2">
      <p>{lead_p1}</p>
      <p>{lead_p2}</p>
    </div>
  </div>

  <!-- スペック比較テーブル -->
  {comparison_table_html}

  <!-- ランキング本体セクション -->
  <div class="space-y-10">
{''.join(ranking_sections)}
  </div>

  <!-- FAQセクション -->
  {faq_html}

  <!-- 関連記事・内部リンク -->
  {related_html}
</div>"""

        f_count = count_japanese_chars(feature_html)
        print(f" -> Feature [{art_id}] Total char count: {f_count} chars (Requirement >= 3000)")

        feature_post_json = {
            "id": art_id,
            "title": art_title,
            "date": "2026-10-10 12:00:00",
            "hinban": art["hinban"],
            "price": "500~",
            "maker": "FANZA公式厳選特集",
            "actresses": [it.get("iteminfo", {}).get("actress", [{}])[0].get("name", "") for it in items_data if it.get("iteminfo", {}).get("actress")],
            "genres": art["genres"],
            "image": items_data[0].get("imageURL", {}).get("large", ""),
            "review": feature_html
        }

        f_path = os.path.join(OUTPUT_DIR, f"{art_id}.json")
        with open(f_path, "w", encoding="utf-8") as f:
            json.dump(feature_post_json, f, ensure_ascii=False, indent=2)
        print(f" -> Saved Feature Article: {f_path}")
        feature_success += 1

    print(f"\n=== GENERATION COMPLETE: {individual_success} Individual Posts, {feature_success} Feature Articles ===")

if __name__ == "__main__":
    main()
