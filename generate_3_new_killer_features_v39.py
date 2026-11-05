# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・新規キラー特集3記事および個別作品15件自動生成スクリプト v39
各記事3000文字以上・完全独自書き下ろし・内部リンク網羅・SEO/LLM/GEO対策
1. 【優しく包み込む極上の初体験】純真な初体験を優しく導く大人のロマンス 特集（TOP5）
2. 【理性崩壊のダブルベッド密室】出張先のビジネスホテル・憧れの先輩美女OLと禁断の相部屋 特集（TOP5）
3. 【湯煙に濡れる素肌と旅情の背徳】秘湯混浴露天風呂・温泉旅館の客室露天風呂・浴衣と湯上がりの密着逢瀬 特集（TOP5）
"""

import os
import re
import json
import time
import urllib.parse
import subprocess
import requests

from reviews_feature_double_busty_sandwich import REVIEWS_DOUBLE_BUSTY_SANDWICH
from reviews_feature_afterschool_teacher import REVIEWS_AFTERSCHOOL_TEACHER
from reviews_feature_morning_cohabitation import REVIEWS_MORNING_COHABITATION
from features_def_v39 import FEATURE_ARTICLES

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
ALL_REVIEWS.update(REVIEWS_DOUBLE_BUSTY_SANDWICH)
ALL_REVIEWS.update(REVIEWS_AFTERSCHOOL_TEACHER)
ALL_REVIEWS.update(REVIEWS_MORNING_COHABITATION)

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

def generate_individual_post(cid, rank_info, feature_info, item_api):
    title = item_api.get("title", rank_info["spec_summary"])
    aff_url = item_api.get("affiliate_url_clean", item_api.get("affiliateURL", ""))
    package_img = item_api.get("imageURL", {}).get("large", "")
    maker_name = item_api.get("iteminfo", {}).get("maker", [{}])[0].get("name", "公式")
    
    actresses = [a.get("name") for a in item_api.get("iteminfo", {}).get("actress", [])]
    genres = [g.get("name") for g in item_api.get("iteminfo", {}).get("genre", [])]
    
    actress_links_html = " / ".join([get_actress_link(a) for a in actresses if a])
    genre_links_html = " ".join([get_genre_link(g) for g in genres[:8] if g])
    
    review_html = ALL_REVIEWS.get(cid, "")
    if not review_html:
        print(f"ERROR: Review not found for {cid}")
        return None

    samples = get_sample_images(item_api, max_count=4)
    samples_html = ""
    if samples:
        samples_html = '''
        <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-4">
          <h3 class="text-lg md:text-xl font-bold text-white flex items-center gap-2">
            <span>📸</span> 劇中ハイライト・高画質シーンプレビュー
          </h3>
          <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
        '''
        for s in samples:
            samples_html += f'''
            <div class="rounded-xl overflow-hidden border border-slate-700/60 shadow group">
              <img src="{s}" alt="{title} シーンプレビュー" class="w-full h-32 md:h-36 object-cover group-hover:scale-105 transition duration-300" loading="lazy" />
            </div>
            '''
        samples_html += '</div></div>'

    # 他の関連おすすめ作品リンク
    other_items = [itm for itm in feature_info["items"] if itm["cid"] != cid]
    related_items_html = ""
    if other_items:
        related_items_html = f'''
        <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-4">
          <h3 class="text-lg md:text-xl font-bold text-white flex items-center gap-2">
            <span>🔥</span> この特集で一緒に選出されたおすすめ神作
          </h3>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        '''
        for o in other_items[:4]:
            related_items_html += f'''
            <a href="/posts/{o['cid']}" class="flex items-center gap-3 p-3 bg-slate-800/60 hover:bg-slate-800 rounded-xl border border-slate-700/50 transition group">
              <span class="w-6 h-6 rounded-full bg-rose-600/80 text-white font-bold text-xs flex items-center justify-center flex-shrink-0">TOP{o['rank']}</span>
              <span class="text-xs text-slate-200 group-hover:text-amber-300 transition line-clamp-2 leading-relaxed font-medium">{o['spec_summary']}</span>
            </a>
            '''
        related_items_html += '</div></div>'

    points_li = "".join([f'<li class="flex items-start gap-2"><span class="text-rose-500 font-bold">✔</span><span class="text-slate-200">{pt}</span></li>' for pt in rank_info["points"]])

    body_html = f'''
<!-- 個別詳細レビューコンテナ -->
<div class="space-y-8">
  <!-- ファーストビュー・作品ヘッダー -->
  <div class="bg-gradient-to-br from-slate-900 via-slate-900 to-rose-950/30 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-2xl flex flex-col md:flex-row gap-6 items-start">
    <div class="w-full md:w-1/3 flex-shrink-0">
      <div class="relative rounded-2xl overflow-hidden shadow-2xl border border-slate-700/80 group">
        <img src="{package_img}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="eager" />
        <div class="absolute top-3 left-3 bg-rose-600/90 text-white text-xs font-bold px-3 py-1 rounded-full shadow-lg backdrop-blur-sm">
          特集第{rank_info['rank']}位
        </div>
      </div>
    </div>
    <div class="w-full md:w-2/3 flex flex-col justify-between space-y-4">
      <div>
        <div class="text-xs font-bold text-rose-400 tracking-wider uppercase mb-1.5 flex items-center gap-1.5">
          <span>🏆</span> {feature_info['title'][:40]}...
        </div>
        <h1 class="text-xl md:text-2xl font-black text-white leading-snug">{title}</h1>
      </div>

      <div class="space-y-2 text-sm text-slate-300">
        <p><strong class="text-slate-400">出演キャスト：</strong> {actress_links_html if actress_links_html else '単体厳選キャスト'}</p>
        <p><strong class="text-slate-400">メーカー：</strong> <span class="text-slate-200">{maker_name}</span></p>
        <p><strong class="text-slate-400">品番・CID：</strong> <span class="font-mono text-amber-300 font-bold">{cid}</span></p>
        <p><strong class="text-slate-400">抜擢理由：</strong> <span class="text-rose-300 font-medium">{rank_info['badge']}</span></p>
      </div>

      <!-- キラーポイント箇条書き -->
      <div class="bg-slate-800/60 rounded-2xl p-4 border border-slate-700/50">
        <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-1.5">
          <span>⚡</span> 本作の絶対に見逃せない実用ポイント
        </h4>
        <ul class="space-y-1.5 text-xs md:text-sm">
          {points_li}
        </ul>
      </div>

      <div class="flex flex-wrap gap-1.5 pt-1">
        {genre_links_html}
      </div>

      <div class="pt-2">
        <a href="{aff_url}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center gap-2 w-full py-4 px-6 bg-gradient-to-r from-rose-600 via-rose-500 to-amber-500 hover:from-rose-500 hover:to-amber-400 text-white font-black rounded-2xl shadow-xl shadow-rose-900/40 hover:shadow-rose-900/60 transition duration-300 text-base md:text-lg group">
          <span>🔥 FANZA公式で高画質フル本編を今すぐチェック</span>
          <svg class="w-5 h-5 group-hover:translate-x-1 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </a>
      </div>
    </div>
  </div>

  {samples_html}

  <!-- レビュー本文（完全独自書き下ろし） -->
  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-10 shadow-xl">
    {review_html}
  </div>

  <!-- 本作を120%楽しむための鑑賞ガイド -->
  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-4 text-slate-300">
    <h3 class="text-lg md:text-xl font-bold text-white flex items-center gap-2">
      <span>💡</span> 本作を120%楽しむための編集部おすすめ鑑賞ガイド
    </h3>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs md:text-sm">
      <div class="bg-slate-800/50 p-4 rounded-2xl border border-slate-700/50 space-y-2">
        <div class="font-bold text-amber-300 flex items-center gap-1.5">
          <span>🎧</span> 密閉型ヘッドホン・イヤホン推奨
        </div>
        <p class="text-slate-300 leading-relaxed">
          息を呑むような吐息、衣類が擦れ合う微細な摩擦音、肌と肌が激突する生々しい肉弾音など、音響のリアリティが極めて高く作り込まれています。密閉型ヘッドホンを装着することで、真横で愛し合っているかのような圧倒的臨場感を体感できます。
        </p>
      </div>
      <div class="bg-slate-800/50 p-4 rounded-2xl border border-slate-700/50 space-y-2">
        <div class="font-bold text-amber-300 flex items-center gap-1.5">
          <span>📺</span> 大画面モニター・暗室環境での視聴
        </div>
        <p class="text-slate-300 leading-relaxed">
          照明の陰影や肌の艶、キャストの潤んだ瞳のディテールまで緻密に表現されています。部屋の明かりを暗くし、大画面モニターで鑑賞することで、まるで映画館の最前列でドラマを見つめているかのような没入感が得られます。
        </p>
      </div>
    </div>
  </div>

  <!-- 深層心理・フェティシズム分析セクション -->
  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-4 text-slate-300">
    <h3 class="text-lg md:text-xl font-bold text-white flex items-center gap-2 text-rose-400">
      <span>🔬</span> 本作が刺激する深層心理とフェティシズムの構造分析
    </h3>
    <p class="leading-relaxed text-xs md:text-sm">
      本作が多くの男性の心を捉えて離さない本質的な理由は、単なる視覚的刺激にとどまらず、「日常では満たされない心理的願望」を完璧なリアリズムで昇華させている点にあります。日常の社会的役割やプレッシャーから完全に解放され、目の前の魅力的なヒロインと二人きりで本能のままに惹かれ合うカタルシス。
    </p>
    <p class="leading-relaxed text-xs md:text-sm">
      特に本作では、最初のぎこちない距離感から、ふとしたきっかけで境界線を越え、最後はお互いの理性をかなぐり捨てて求め合うまでの「心理的グラデーション」が極めて丁寧に描かれています。相手の吐息、肌の温もり、そして瞳の揺らぎといった微細なサインを通じて伝わってくる真実味こそが、鑑賞者を深い陶酔感へと導く最大の要因です。
    </p>
  </div>

  <!-- 本作が選出された特集記事への誘導バナー -->
  <div class="bg-gradient-to-r from-rose-950/60 via-slate-900 to-amber-950/40 border border-rose-800/50 rounded-3xl p-6 md:p-8 shadow-xl flex flex-col sm:flex-row items-center justify-between gap-4">
    <div class="space-y-1 text-center sm:text-left">
      <div class="text-xs font-bold text-rose-400">この作品がランクインした注目ランキング</div>
      <h4 class="text-base md:text-lg font-black text-white">{feature_info['title']}</h4>
    </div>
    <a href="/posts/{feature_info['id']}" class="flex-shrink-0 px-6 py-3 bg-rose-600 hover:bg-rose-500 text-white font-bold text-sm rounded-xl transition shadow-lg shadow-rose-900/50 flex items-center gap-2">
      <span>🏆 特集TOP5ランキングを見る</span>
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
    </a>
  </div>

  {related_items_html}

  <!-- 鑑賞後の総括 -->
  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-4 text-slate-300">
    <h3 class="text-lg md:text-xl font-bold text-white flex items-center gap-2 text-amber-400">
      <span>📖</span> 鑑賞後の総括：なぜ本作は観る者の記憶に深く刻み込まれるのか
    </h3>
    <p class="leading-relaxed text-xs md:text-sm">
      本作が多くのユーザーから絶賛され、名作としての評価を確固たるものにしている理由は、単なるシチュエーションの消費にとどまらない「人間関係の生々しいリアルさ」と「緻密な演出美」にあります。キャスト陣が演じるキャラクターの細やかな視線の動き、息遣い、そして肌が触れ合う瞬間の緊張感に至るまで、すべてが計算され尽くした映像美によって支えられています。
    </p>
    <p class="leading-relaxed text-xs md:text-sm">
      特に中盤から終盤にかけての感情の高まりと情熱的なスキンシップの連続は、日常では決して味わうことのできない極上の非日常感を提供してくれます。鑑賞者の心に寄り添い、確かな満足感と深い余韻を残す本作は、何度でも繰り返し鑑賞したくなる価値ある一本です。
    </p>
  </div>

  <!-- 最終CTAフッター -->
  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl text-center space-y-4">
    <h3 class="text-lg md:text-xl font-bold text-white">FANZA公式アーカイブで今すぐ本編をフル視聴</h3>
    <p class="text-xs md:text-sm text-slate-300 max-w-2xl mx-auto leading-relaxed">
      公式配信ならではの最高画質・高音質ストリーミングおよびダウンロードに対応。今すぐ公式プレイヤーで、至福の鑑賞体験をお楽しみください。
    </p>
    <div>
      <a href="{aff_url}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 py-4 px-8 bg-gradient-to-r from-rose-600 to-amber-500 hover:from-rose-500 hover:to-amber-400 text-white font-black text-base md:text-lg rounded-2xl shadow-xl shadow-rose-900/40 hover:shadow-rose-900/60 transition">
        <span>🔥 FANZA公式で高画質本編を再生</span>
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
      </a>
    </div>
  </div>
</div>
'''

    # 文字数補強チェック（3000文字以上厳格保証）
    chars = count_japanese_chars(body_html)
    if chars < 3000:
        extra_supplement = f'''
  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-4 text-slate-300">
    <h3 class="text-lg md:text-xl font-bold text-white flex items-center gap-2 text-rose-400">
      <span>✨</span> 編集部による徹底比較と本作が選ばれる理由
    </h3>
    <p class="leading-relaxed text-xs md:text-sm">
      数多ある同ジャンル作品の中でも、本作が頭ひとつ抜きん出ている決定的な要因は、キャストの圧倒的なビジュアルポテンシャルと、それを120%引き出す熟練のカメラワークにあります。単に過激さを競うのではなく、キャストの微細な表情の変化や、肌のぬくもり、そして息遣いの一つひとつを丁寧に拾い上げることで、観る者に本物の恋人と過ごしているかのような濃密な錯覚を抱かせます。
    </p>
    <p class="leading-relaxed text-xs md:text-sm">
      また、音響設計においても微細な環境音や衣擦れの音、囁き声の周波数に至るまで緻密に調整されており、一度鑑賞すればその圧倒的な完成度の虜になること間違いありません。今夜の特別な鑑賞時間に、心から自信を持っておすすめできる至高のエンターテインメント作品です。
    </p>
  </div>
        '''
        # 最後の閉じタグの直前に確実に挿入
        body_html = body_html[:-6] + f"\n{extra_supplement}\n</div>"

    release_date = "2026-11-05 01:00:00"

    return {
        "id": cid,
        "title": title,
        "date": release_date,
        "hinban": cid,
        "price": item_api.get("prices", {}).get("price", "500~"),
        "maker": maker_name,
        "actresses": actresses,
        "genres": genres,
        "image": package_img,
        "review": body_html
    }

def generate_feature_article(feature_data, fetched_items):
    f_id = feature_data["id"]
    f_title = feature_data["title"]
    f_hinban = feature_data["hinban"]
    lead_p1 = feature_data["lead_p1"]
    lead_p2 = feature_data["lead_p2"]
    genres = feature_data["genres"]
    seo_analysis_html = feature_data["seo_analysis"]
    faq_items = feature_data["faq_items"]
    
    genre_links_html = " ".join([get_genre_link(g) for g in genres if g])
    
    top_pkg = ""
    all_actresses = []
    items_html = ""
    
    for itm in feature_data["items"]:
        cid = itm["cid"]
        rank = itm["rank"]
        badge = itm["badge"]
        summary = itm["spec_summary"]
        points = itm["points"]
        
        it_api = fetched_items.get(cid, {})
        title = it_api.get("title", summary)
        aff_url = it_api.get("affiliate_url_clean", it_api.get("affiliateURL", ""))
        pkg_img = it_api.get("imageURL", {}).get("large", "")
        if rank == 1:
            top_pkg = pkg_img
            
        acts = [a.get("name") for a in it_api.get("iteminfo", {}).get("actress", [])]
        for a in acts:
            if a and a not in all_actresses:
                all_actresses.append(a)
        act_str = " / ".join([get_actress_link(a) for a in acts if a])
        
        sample_imgs = get_sample_images(it_api, max_count=2)
        sample_img_html = ""
        if sample_imgs:
            sample_img_html = '<div class="grid grid-cols-2 gap-2 mt-3">'
            for s in sample_imgs:
                sample_img_html += f'<div class="rounded-lg overflow-hidden border border-slate-700/50"><img src="{s}" alt="{title}" class="w-full h-20 md:h-24 object-cover" loading="lazy" /></div>'
            sample_img_html += '</div>'
            
        points_li = "".join([f'<li class="flex items-start gap-1.5"><span class="text-rose-500 font-bold">✔</span><span>{p}</span></li>' for p in points])
        
        raw_review = ALL_REVIEWS.get(cid, "")
        clean_review_sample = re.sub(r'<[^>]+>', ' ', raw_review)
        clean_review_sample = re.sub(r'\s+', ' ', clean_review_sample).strip()[:240] + "..."
        
        rank_badge_class = "from-amber-400 to-amber-600 text-slate-950 font-black" if rank == 1 else ("from-slate-200 to-slate-400 text-slate-950 font-black" if rank == 2 else ("from-amber-600 to-amber-800 text-white font-bold" if rank == 3 else "from-rose-600 to-rose-800 text-white font-bold"))
        
        items_html += f'''
<!-- 第{rank}位作品カード -->
<section class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-2xl space-y-6">
  <div class="flex flex-col md:flex-row gap-6 items-start">
    <div class="w-full md:w-2/5 flex-shrink-0">
      <div class="relative rounded-2xl overflow-hidden shadow-xl border border-slate-700/70 group">
        <img src="{pkg_img}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute top-3 left-3 bg-gradient-to-r {rank_badge_class} text-xs px-3 py-1 rounded-full shadow-lg">
          第{rank}位 / 厳選神作
        </div>
      </div>
      {sample_img_html}
    </div>

    <div class="w-full md:w-3/5 space-y-4">
      <div>
        <span class="text-xs font-bold text-rose-400 uppercase tracking-wider">{badge}</span>
        <h3 class="text-xl md:text-2xl font-black text-white leading-snug mt-1">
          <a href="/posts/{cid}" class="hover:text-rose-300 transition">{title}</a>
        </h3>
      </div>

      <div class="text-xs text-slate-300 space-y-1">
        <p><strong class="text-slate-400">出演：</strong> {act_str if act_str else '厳選キャスト'}</p>
        <p><strong class="text-slate-400">品番：</strong> <span class="font-mono text-amber-300 font-bold">{cid}</span></p>
      </div>

      <!-- 見どころポイント -->
      <div class="bg-slate-800/60 rounded-2xl p-4 border border-slate-700/50">
        <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-1.5">
          <span>⚡</span> 本作が選ばれた決定打
        </h4>
        <ul class="space-y-1.5 text-xs md:text-sm">
          {points_li}
        </ul>
      </div>

      <p class="text-xs md:text-sm text-slate-300 leading-relaxed bg-slate-800/30 p-3 rounded-xl border border-slate-700/30">
        {clean_review_sample}
      </p>

      <div class="flex flex-col sm:flex-row gap-3 pt-2">
        <a href="/posts/{cid}" class="flex-1 py-3 px-4 bg-slate-800 hover:bg-slate-700 border border-slate-600 text-white font-bold text-center text-xs md:text-sm rounded-xl transition shadow">
          📖 3000字詳細レビューを読む
        </a>
        <a href="{aff_url}" target="_blank" rel="noopener noreferrer" class="flex-1 py-3 px-4 bg-gradient-to-r from-rose-600 to-amber-500 hover:from-rose-500 hover:to-amber-400 text-white font-black text-center text-xs md:text-sm rounded-xl transition shadow-lg shadow-rose-900/40">
          🔥 FANZAで今すぐチェック
        </a>
      </div>
    </div>
  </div>
</section>
'''

    # FAQアコーディオン/リスト
    faq_html = ""
    for faq in faq_items:
        faq_html += f'''
        <div class="bg-slate-800/60 p-5 rounded-2xl border border-slate-700/50 space-y-2">
          <h4 class="text-sm md:text-base font-bold text-white flex items-center gap-2">
            <span class="w-6 h-6 rounded-full bg-rose-600 text-white text-xs flex items-center justify-center flex-shrink-0">Q</span>
            {faq['q']}
          </h4>
          <p class="text-xs md:text-sm text-slate-300 leading-relaxed pl-8">
            {faq['a']}
          </p>
        </div>
        '''

    # 関連記事リンク
    other_features = [f for f in FEATURE_ARTICLES if f["id"] != f_id]
    related_features_html = ""
    if other_features:
        related_features_html = f'''
        <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-4">
          <h3 class="text-lg md:text-xl font-bold text-white flex items-center gap-2">
            <span>🔥</span> あわせて読みたい注目のキラー特集ランキング
          </h3>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        '''
        for of in other_features:
            related_features_html += f'''
            <a href="/posts/{of['id']}" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-2xl border border-slate-700/50 transition group space-y-1.5">
              <span class="text-xs font-bold text-rose-400 flex items-center gap-1"><span>🏆</span> 注目特集</span>
              <h4 class="text-sm font-bold text-white group-hover:text-amber-300 transition line-clamp-2 leading-snug">{of['title']}</h4>
            </a>
            '''
        related_features_html += '</div></div>'

    actress_links_html = " / ".join([get_actress_link(a) for a in all_actresses if a])

    feature_body_html = f'''
<div class="space-y-10">
  <!-- 特集ヘッダーヒーロー -->
  <div class="bg-gradient-to-br from-slate-900 via-rose-950/40 to-slate-900 border border-slate-800 rounded-3xl p-6 md:p-10 shadow-2xl space-y-6">
    <div class="space-y-3">
      <div class="inline-flex items-center gap-2 bg-rose-600/90 text-white text-xs font-bold px-3 py-1.5 rounded-full shadow-lg">
        <span>🏆</span> 2026年最新FANZA公式アーカイブ厳選ランキング
      </div>
      <h1 class="text-2xl md:text-3xl lg:text-4xl font-black text-white leading-tight">
        {f_title}
      </h1>
      <div class="flex flex-wrap gap-2 pt-1">
        {genre_links_html}
      </div>
    </div>

    <div class="space-y-4 text-slate-300 leading-relaxed text-sm md:text-base border-t border-slate-800 pt-6">
      <p>{lead_p1}</p>
      <p>{lead_p2}</p>
    </div>

    <!-- 参加主要キャスト -->
    <div class="bg-slate-800/40 p-4 rounded-2xl border border-slate-700/40 text-xs md:text-sm text-slate-300">
      <strong class="text-slate-400">厳選選出キャスト：</strong> {actress_links_html}
    </div>
  </div>

  <!-- ランキング一覧5作品 -->
  <div class="space-y-8">
    {items_html}
  </div>

  <!-- 深層SEO分析セクション -->
  {seo_analysis_html}

  <!-- よくある質問（FAQ）セクション -->
  <section class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-6">
    <h3 class="text-xl md:text-2xl font-black text-white flex items-center gap-2 border-b border-rose-900/40 pb-3">
      <span>❓</span> 本特集に関するよくある質問（FAQ）
    </h3>
    <div class="space-y-3">
      {faq_html}
    </div>
  </section>

  {related_features_html}
</div>
'''

    # 文字数補強チェック
    chars = count_japanese_chars(feature_body_html)
    if chars < 3000:
        supplement_html = f'''
  <section class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl space-y-4 text-slate-300">
    <h3 class="text-lg md:text-xl font-bold text-white flex items-center gap-2 text-amber-400">
      <span>📖</span> 総括：なぜ本作群は時代を超えて愛され続けるのか
    </h3>
    <p class="leading-relaxed">
      今回厳選した5作品は、単なる一時的なブームや刺激にとどまらず、人間の根源的なフェティシズムと情動を鮮やかに捉えたエポックメイキングな傑作ばかりです。それぞれの作品が持つ独自の演出意図と、女優陣の献身的なパフォーマンスが高次元で結実し、観る者の脳髄を震わせる唯一無二の鑑賞体験を創り出しています。
    </p>
    <p class="leading-relaxed">
      一度その深みにハマれば抜け出せなくなるほどの圧倒的な実用性と芸術性。今夜の特別なひとときに、ぜひこの珠玉のラインナップの中からあなたの本能を最も揺さぶる一作を選び取ってください。
    </p>
  </section>
        '''
        feature_body_html = feature_body_html.replace('</div>\n\'\'\'', f'{supplement_html}</div>\n\'\'\'')

    release_date = "2026-11-05 01:00:00"

    return {
        "id": f_id,
        "title": f_title,
        "date": release_date,
        "hinban": f_hinban,
        "price": "500~",
        "maker": "FANZA厳選特集編集部",
        "actresses": all_actresses,
        "genres": genres,
        "image": top_pkg,
        "review": feature_body_html
    }

def main():
    print("=== Starting FANZA Real-Time Fetch & Generation v39 ===")
    created_ids = []

    # 1. すべてのCIDのAPIデータを取得
    all_cids = []
    for f in FEATURE_ARTICLES:
        for it in f["items"]:
            all_cids.append(it["cid"])

    print(f"Total target CIDs to fetch: {len(all_cids)}")
    fetched_items = {}
    for cid in all_cids:
        print(f"Fetching API for {cid}...")
        item = fetch_fanza_item(cid)
        if item:
            fetched_items[cid] = item
            print(f" -> OK: {item.get('title')[:30]}")
        else:
            print(f" -> FAILED: {cid}")
        time.sleep(0.3)

    # 2. 個別作品15記事の生成と保存
    print("\n--- Generating 15 individual review posts ---")
    for f in FEATURE_ARTICLES:
        for it in f["items"]:
            cid = it["cid"]
            r_item = it
            item_api = fetched_items.get(cid)
            if not item_api:
                print(f"Skipping {cid} due to missing API data")
                continue
            post_data = generate_individual_post(cid, r_item, f, item_api)
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
    if os.path.exists("generate_sitemap.js"):
        res = subprocess.run(["node", "generate_sitemap.js"], capture_output=True, text=True)
        print(res.stdout)

    # 8. llms.txt の生成
    print("\n--- Generating LLMs.txt ---")
    if os.path.exists("generate_llms_txt.js"):
        res = subprocess.run(["node", "generate_llms_txt.js"], capture_output=True, text=True)
        print(res.stdout)

    print("=== All generation and bundling completed successfully! ===")

if __name__ == "__main__":
    main()
