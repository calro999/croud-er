import os
import re
import json
import time
import requests
import hashlib

API_ID = "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = "onchan555-999"
LINK_AFFILIATE_ID = "onchan555-003"
POSTS_DIR = "src/data/posts"
CACHE_FILE = "posted_cache.txt"

def load_posted_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return set(line.strip() for line in f if line.strip())
    return set()

def save_to_cache(content_id):
    with open(CACHE_FILE, "a", encoding="utf-8") as f:
        f.write(f"{content_id}\n")

def generate_hinban(content_id):
    if not content_id:
        return ""
    s = content_id.lower()
    s = re.sub(r'^(h_\d+|h_|\d+)', '', s)
    match = re.match(r'^([a-z]+)(\d+)', s)
    if match:
        alphabetic = match.group(1).upper()
        numeric = match.group(2)
        clean_num = numeric.lstrip('0') or '0'
        formatted_standard = f"{alphabetic}-{numeric}"
        if clean_num != numeric:
            return f"{alphabetic}-{clean_num} ({formatted_standard})"
        return formatted_standard
    return content_id.upper()

def fetch_fanza_items():
    url = "https://api.dmm.com/affiliate/v3/ItemList"
    keywords = ["デビュー", "新人", "VR", ""]
    
    unique_items = {}
    cache = load_posted_cache()

    for kw in keywords:
        print(f"Fetching keyword: '{kw}'...", flush=True)
        params = {
            "api_id": API_ID,
            "affiliate_id": API_AFFILIATE_ID,
            "site": "FANZA",
            "service": "digital",
            "floor": "videoa",
            "gte_date": "2026-09-01T00:00:00",
            "lte_date": "2026-09-26T23:59:59",
            "sort": "rank" if kw == "" else "date",
            "hits": 20,
            "output": "json"
        }
        if kw:
            params["keyword"] = kw

        try:
            res = requests.get(url, params=params, timeout=8)
            if res.status_code == 200:
                data = res.json()
                items = data.get("result", {}).get("items", [])
                print(f" -> Found {len(items)} items", flush=True)
                for item in items:
                    cid = item.get("content_id")
                    if cid and cid not in cache and cid not in unique_items:
                        post_file = os.path.join(POSTS_DIR, f"{cid}.json")
                        if not os.path.exists(post_file):
                            unique_items[cid] = item
            else:
                print(f" -> API responded with status {res.status_code}", flush=True)
        except Exception as e:
            print(f" -> Error: {e}", flush=True)

    return list(unique_items.values())

def generate_deep_article_html(item):
    title = item.get("title", "")
    cid = item.get("content_id", "")
    hinban = generate_hinban(cid)
    
    iteminfo = item.get("iteminfo", {})
    actresses = [a.get("name") for a in iteminfo.get("actress", [])]
    genres = [g.get("name") for g in iteminfo.get("genre", [])]
    maker = iteminfo.get("maker", [{}])[0].get("name", "") if iteminfo.get("maker") else ""
    label = iteminfo.get("label", [{}])[0].get("name", "") if iteminfo.get("label") else ""
    director = iteminfo.get("director", [{}])[0].get("name", "") if iteminfo.get("director") else ""
    series = iteminfo.get("series", [{}])[0].get("name", "") if iteminfo.get("series") else ""
    
    raw_desc = item.get("comment", "") or item.get("description", "")
    clean_desc = re.sub(r'<[^>]*>', '', raw_desc).strip()
    
    actress_name = "・".join(actresses) if actresses else "注目キャスト"
    main_actress = actresses[0] if actresses else ""
    
    sample_images = []
    if "sampleImageURL" in item and "sample_l" in item["sampleImageURL"]:
        sample_images = item["sampleImageURL"]["sample_l"].get("image", [])
    
    seed = int(hashlib.md5(cid.encode('utf-8')).hexdigest()[:8], 16)
    score_ero = round(4.6 + (seed % 5) * 0.1, 1)
    score_visual = round(4.7 + ((seed >> 2) % 4) * 0.1, 1)
    score_story = round(4.3 + ((seed >> 4) % 6) * 0.1, 1)

    is_debut = any(k in title for k in ["デビュー", "DEBUT", "新人", "初撮り"]) or any(k in genres for k in ["新人", "デビュー"])
    is_vr = "VR" in title or "VR" in genres

    html_parts = []

    # 1. 導入部
    html_parts.append(f"""
<div class="space-y-6">
  <div class="bg-gradient-to-r from-rose-500/10 via-purple-500/10 to-transparent border-l-4 border-rose-500 p-5 rounded-r-2xl">
    <span class="text-[11px] font-black tracking-widest text-rose-600 uppercase">
      {('🌟 2026年9月 最注目大型新人デビュー速報' if is_debut else ('🥽 2026年9月 超高画質VR最新作レビュー' if is_vr else '🔥 2026年9月最新リリース 話題作徹底レビュー'))}
    </span>
    <h2 class="text-lg md:text-xl font-black text-slate-900 mt-1 leading-snug">
      『{title}』【{hinban}】の見どころ・抜けるポイントを忖度なし解説
    </h2>
    <p class="text-xs md:text-sm text-slate-700 leading-relaxed mt-2">
      {f"2026年9月、AV界に激震を走らせる注目の{actress_name}最新作が登場。" if main_actress else "2026年9月リリースの注目最新作。"}
      {clean_desc[:120] if clean_desc else "FANZA公式ランキングでも上位に急浮上している話題の1本です。"}
    </p>
  </div>
""")

    # 2. 公式スペック・基本情報テーブル
    html_parts.append(f"""
  <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
    <h3 class="text-sm font-black text-slate-900 border-b border-slate-100 pb-2 mb-3 flex items-center gap-2">
      <span>📋</span><span>作品基本スペック＆配信情報</span>
    </h3>
    <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 text-xs">
      <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-100">
        <span class="block text-[10px] text-slate-400 font-bold">品番</span>
        <span class="font-black text-rose-600">{hinban}</span>
      </div>
      <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-100">
        <span class="block text-[10px] text-slate-400 font-bold">出演女優</span>
        <span class="font-black text-slate-800">{actress_name}</span>
      </div>
      <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-100">
        <span class="block text-[10px] text-slate-400 font-bold">メーカー</span>
        <span class="font-bold text-slate-700">{maker or "公式メーカー"}</span>
      </div>
      {f'''<div class="bg-slate-50 p-2.5 rounded-xl border border-slate-100">
        <span class="block text-[10px] text-slate-400 font-bold">レーベル</span>
        <span class="font-bold text-slate-700">{label}</span>
      </div>''' if label else ''}
      {f'''<div class="bg-slate-50 p-2.5 rounded-xl border border-slate-100">
        <span class="block text-[10px] text-slate-400 font-bold">監督</span>
        <span class="font-bold text-slate-700">{director}</span>
      </div>''' if director else ''}
      <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-100">
        <span class="block text-[10px] text-slate-400 font-bold">配信開始日</span>
        <span class="font-bold text-slate-700">{item.get("date", "").split(" ")[0]}</span>
      </div>
    </div>
  </div>
""")

    # 3. 本作のあらすじ・シチュエーション
    if clean_desc:
        html_parts.append(f"""
  <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm space-y-3">
    <h3 class="text-base font-black text-slate-900 border-b border-slate-100 pb-2">
      📖 公式あらすじ・シチュエーション詳細
    </h3>
    <p class="text-xs md:text-sm text-slate-600 leading-relaxed whitespace-pre-line">
      {clean_desc}
    </p>
  </div>
""")

    # 4. サンプル画像ギャラリー
    if sample_images and len(sample_images) > 0:
        img_tags = "".join([
            f'<div class="rounded-xl overflow-hidden shadow-sm border border-slate-100 bg-slate-100 aspect-video relative"><img src="{img_url}" alt="{title} サンプルシーン" class="w-full h-full object-cover hover:scale-105 transition duration-300" loading="lazy" /></div>'
            for img_url in sample_images[:6]
        ])
        html_parts.append(f"""
  <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm space-y-4">
    <h3 class="text-base font-black text-slate-900 border-b border-slate-100 pb-2 flex items-center justify-between">
      <span>📸 厳選サンプルシーンプレビュー</span>
      <span class="text-[10px] text-slate-400 font-bold">※FANZA公式高画質カット</span>
    </h3>
    <div class="grid grid-cols-2 sm:grid-cols-3 gap-3">
      {img_tags}
    </div>
  </div>
""")

    # 5. 編集部スコア判定＆総括
    html_parts.append(f"""
  <div class="bg-gradient-to-br from-slate-900 to-slate-950 text-white rounded-2xl p-6 shadow-lg border border-slate-800 space-y-4">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
      <h3 class="text-base font-black text-amber-400 flex items-center gap-2">
        <span>⭐</span><span>背徳の深夜書斎 編集部スコア判定</span>
      </h3>
      <span class="text-[10px] bg-rose-600 text-white font-black px-2.5 py-0.5 rounded-full">殿堂入り推奨</span>
    </div>

    <div class="grid grid-cols-3 gap-3 text-center">
      <div class="bg-white/5 border border-white/10 rounded-xl p-3">
        <span class="block text-[10px] text-slate-400 font-bold">エロ度・実用性</span>
        <span class="text-2xl font-black text-rose-400">{score_ero}</span><span class="text-xs text-slate-500">/5.0</span>
      </div>
      <div class="bg-white/5 border border-white/10 rounded-xl p-3">
        <span class="block text-[10px] text-slate-400 font-bold">ルックス・体型</span>
        <span class="text-2xl font-black text-amber-400">{score_visual}</span><span class="text-xs text-slate-500">/5.0</span>
      </div>
      <div class="bg-white/5 border border-white/10 rounded-xl p-3">
        <span class="block text-[10px] text-slate-400 font-bold">没入感・演出</span>
        <span class="text-2xl font-black text-indigo-400">{score_story}</span><span class="text-xs text-slate-500">/5.0</span>
      </div>
    </div>

    <div class="pt-2 text-xs md:text-sm text-slate-300 leading-relaxed space-y-2">
      <p>
        <b>【総括レビュー】</b>：
        {f"本作の最大の強みは、{main_actress}の圧倒的な表情変化とリアルな吐息の生々しさです。" if main_actress else "本作の最大の強みは、徹底的に作り込まれたシチュエーションとカメラアングルの秀逸さです。"}
        {f"特に中盤から終盤にかけての濃厚な絡みは、単なる台本通りではない本気度の高いリアクションが連続し、最後まで集中して没頭できる仕上がりとなっています。" if not is_vr else "VRならではの超至近距離アングルにより、息遣いや肌の質感まで目の前にあるかのような圧倒的臨場感を味わえます。"}
      </p>
    </div>
  </div>
</div>
""")

    review_html = "\n".join(html_parts)

    aff_url = item.get("affiliateURL", "")
    if aff_url and LINK_AFFILIATE_ID:
        aff_url = re.sub(r'af_id=[^&]+', f'af_id={LINK_AFFILIATE_ID}', aff_url)

    image_url = item.get("imageURL", {}).get("large", "") if "imageURL" in item else ""

    post_data = {
        "id": cid,
        "hinban": hinban,
        "title": title,
        "review": review_html,
        "image": image_url,
        "sample_images": sample_images,
        "sample_movie_url": item.get("sampleMovieURL", {}).get("size_720_480", "") if "sampleMovieURL" in item else "",
        "affiliate_url": aff_url,
        "genres": genres,
        "actresses": actresses,
        "directors": [director] if director else [],
        "maker": maker,
        "price": item.get("prices", {}).get("price", "300~") if "prices" in item else "300~",
        "date": item.get("date", "2026-09-25 00:00:00"),
        "labels": [g for g in genres[:4]]
    }

    return post_data

def main():
    print("=== Fetching latest Sept 2026 releases & rookie debut works ===", flush=True)
    items = fetch_fanza_items()
    print(f"Total candidate items fetched: {len(items)}", flush=True)

    created_count = 0
    os.makedirs(POSTS_DIR, exist_ok=True)

    for item in items:
        cid = item.get("content_id")
        if not cid:
            continue

        target_file = os.path.join(POSTS_DIR, f"{cid}.json")
        if os.path.exists(target_file):
            continue

        post_data = generate_deep_article_html(item)
        with open(target_file, "w", encoding="utf-8") as f:
            json.dump(post_data, f, ensure_ascii=False, indent=2)

        save_to_cache(cid)
        created_count += 1
        print(f"[{created_count}] Created: {cid} | {post_data['title'][:40]}", flush=True)

    print(f"=== Successfully created {created_count} high quality latest release posts ===", flush=True)

if __name__ == "__main__":
    main()
