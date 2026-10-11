# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・新規キラー特集3記事および個別作品15件自動生成スクリプト v14
各記事3000文字以上・完全独自書き下ろし・内部リンク網羅・SEO/LLM/GEO対策
1. 女教師・放課後の背徳指導と禁断愛特集
2. 温泉旅行・客室露天風呂と浴衣の情事特集
3. 幼馴染・十数年ぶりの再会と執着交尾特集
"""

import os
import re
import json
import time
import urllib.parse
import requests

from reviews_feature_teacher import REVIEWS_PART1
from reviews_feature_onsen import REVIEWS_PART2
from reviews_feature_childhood import REVIEWS_PART3
from features_def_v14 import FEATURE_ARTICLES

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
    release_date = it.get("date", "2026-10-11 12:00:00")

    actress_name = actresses[0] if actresses else "人気女優"
    maker_name = makers[0] if makers else "FANZA独占"
    actress_links_html = " ".join([get_actress_link(a) for a in actresses])
    genre_links_html = " ".join([get_genre_link(g) for g in genres[:8]])

    feature_link_html = f'''
    <div class="my-8 p-5 bg-gradient-to-r from-rose-950/60 via-slate-900 to-amber-950/40 border border-rose-500/30 rounded-2xl shadow-xl">
        <div class="flex items-center gap-2 text-rose-400 font-bold text-sm mb-2">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-rose-500 animate-pulse"></span>
            特集ランキング第{rank_info['rank']}位選出作品
        </div>
        <p class="text-slate-200 text-sm leading-relaxed mb-3">
            本作は、当サイトの厳選特集記事「<a href="/posts/{feature_info['id']}" class="text-amber-400 hover:text-amber-300 font-bold underline decoration-amber-500/50">{feature_info['title']}</a>」において、堂々の第{rank_info['rank']}位にランクインした屈指の名作です。
        </p>
        <a href="/posts/{feature_info['id']}" class="inline-flex items-center gap-1.5 text-xs text-rose-300 hover:text-rose-200 font-semibold bg-rose-900/40 hover:bg-rose-800/50 px-3 py-1.5 rounded-lg border border-rose-700/50 transition">
            特集ランキングの全編をチェックする →
        </a>
    </div>
    '''

    samples_html = ""
    if sample_imgs:
        samples_html = '<div class="my-8"><h3 class="text-lg font-bold text-slate-200 mb-4 border-l-4 border-rose-500 pl-3">公式高画質サンプルシーン（タップで拡大プレビュー）</h3><div class="grid grid-cols-2 gap-3 sm:gap-4">'
        for idx, simg in enumerate(sample_imgs, 1):
            samples_html += f'''
            <div class="relative group rounded-xl overflow-hidden bg-slate-950 border border-slate-800 shadow-lg">
                <img src="{simg}" alt="{title} 公式サンプルシーン {idx}" class="w-full h-auto object-cover transform group-hover:scale-105 transition duration-300" loading="lazy" />
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex items-end p-2.5">
                    <span class="text-xs text-rose-300 font-medium font-sans">ハイビジョン公式シーン {idx}</span>
                </div>
            </div>
            '''
        samples_html += '</div></div>'

    cta_top = f'''
    <div class="my-8 text-center bg-slate-900/90 border border-rose-500/40 rounded-2xl p-6 shadow-2xl backdrop-blur">
        <p class="text-amber-300 text-sm font-bold tracking-wider mb-2">【FANZA公式独占】高画質HD・完全ノーカット配信中</p>
        <h3 class="text-xl font-extrabold text-white mb-4 leading-snug">{title}</h3>
        <a href="{aff_url}" target="_blank" rel="noopener noreferrer nofollow" class="inline-flex items-center justify-center gap-3 px-8 py-4 bg-gradient-to-r from-rose-600 via-rose-500 to-amber-600 hover:from-rose-500 hover:to-amber-500 text-white font-extrabold text-lg rounded-xl shadow-lg hover:shadow-rose-500/50 transform hover:-translate-y-0.5 transition duration-200">
            <span>今すぐFANZA公式で作品を見る（プレビュー無料）</span>
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
        </a>
        <p class="text-xs text-slate-400 mt-2.5">※FANZA公式サイトへ安全に遷移します。無料の冒頭プレビュー動画あり。</p>
    </div>
    '''

    cta_bottom = f'''
    <div class="my-10 bg-gradient-to-b from-slate-900 to-slate-950 border border-rose-500/30 rounded-2xl p-6 sm:p-8 text-center shadow-2xl">
        <span class="px-3 py-1 bg-rose-500/20 text-rose-300 border border-rose-500/30 rounded-full text-xs font-bold tracking-wider uppercase mb-3 inline-block">Special Offer</span>
        <h3 class="text-xl sm:text-2xl font-black text-white mb-3">この至高の背徳ドラマを最高の画質で体験する</h3>
        <p class="text-slate-300 text-sm max-w-xl mx-auto mb-6 leading-relaxed">
            息遣いまで伝わる臨場感と女優の生々しいメス顔。無料サンプル動画を視聴するだけでも、その桁違いの完成度に圧倒されること間違いありません。
        </p>
        <a href="{aff_url}" target="_blank" rel="noopener noreferrer nofollow" class="inline-flex items-center justify-center gap-3 px-8 py-4 bg-gradient-to-r from-rose-600 to-amber-600 hover:from-rose-500 hover:to-amber-500 text-white font-black text-lg rounded-xl shadow-xl hover:shadow-rose-500/50 transform hover:-translate-y-0.5 transition duration-200 w-full sm:w-auto">
            <span>FANZA公式で高画質フル本編をチェック</span>
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
        </a>
    </div>
    '''

    full_body = f"""
    <div class="article-content space-y-6 text-slate-200 leading-relaxed font-sans text-base">
        {feature_link_html}
        {cta_top}
        <div class="my-6">
            <img src="{package_img}" alt="{title} 公式パッケージ" class="w-full max-w-2xl mx-auto rounded-2xl border border-slate-800 shadow-2xl" loading="lazy" />
        </div>
        <div class="my-4 flex flex-wrap gap-2 items-center">
            <span class="text-xs text-slate-400 font-bold">出演女優:</span>
            {actress_links_html}
        </div>
        <div class="my-4 flex flex-wrap gap-2 items-center">
            <span class="text-xs text-slate-400 font-bold">ジャンル:</span>
            {genre_links_html}
        </div>
        <div class="prose prose-invert max-w-none my-8 leading-loose space-y-6">
            {review_html}
        </div>
        {samples_html}
        {cta_bottom}
    </div>
    """

    char_cnt = count_japanese_chars(full_body)

    post_data = {
        "id": cid,
        "title": f"【公式詳細レビュー】{title}（{actress_name}主演・見どころ徹底解説）",
        "date": release_date,
        "actresses": actresses,
        "maker": maker_name,
        "genres": genres,
        "url": aff_url,
        "image": package_img,
        "sample_images": sample_imgs,
        "body": full_body,
        "character_count": char_cnt,
        "is_feature": False,
        "related_feature_id": feature_info["id"]
    }
    return post_data

def generate_feature_article(feature_def, fetched_items):
    f_id = feature_def["id"]
    f_title = feature_def["title"]
    items = feature_def["items"]
    lead_p1 = feature_def["lead_p1"]
    lead_p2 = feature_def["lead_p2"]
    genres = feature_def["genres"]
    faqs = feature_def.get("faqs", [])
    related = feature_def.get("related", [])

    table_rows = ""
    ranking_sections = ""

    for rank_item in items:
        cid = rank_item["cid"]
        rank = rank_item["rank"]
        badge = rank_item["badge"]
        spec_summary = rank_item["spec_summary"]
        points = rank_item["points"]
        it = fetched_items.get(cid, {})

        it_title = it.get("title", "")
        actresses = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        actress_name = actresses[0] if actresses else ""
        actress_link = get_actress_link(actress_name)
        makers = [m.get("name") for m in it.get("iteminfo", {}).get("maker", [])]
        maker_name = makers[0] if makers else ""
        pkg_img = it.get("imageURL", {}).get("large", "")
        aff_url = it.get("affiliate_url_clean") or it.get("affiliateURL", "")
        sample_imgs = get_sample_images(it, 4)

        table_rows += f"""
        <tr class="border-b border-slate-800 hover:bg-slate-800/40 transition">
            <td class="py-4 px-3 text-center">
                <span class="inline-flex items-center justify-center w-8 h-8 rounded-full font-black text-sm {'bg-amber-500 text-slate-950 font-black shadow-lg shadow-amber-500/30' if rank == 1 else 'bg-rose-600 text-white shadow-md' if rank == 2 else 'bg-slate-700 text-amber-300' if rank == 3 else 'bg-slate-800 text-slate-400'}">
                    {rank}
                </span>
            </td>
            <td class="py-4 px-3">
                <div class="font-bold text-white text-sm hover:text-amber-300 transition mb-1">
                    <a href="/posts/{cid}">{it_title}</a>
                </div>
                <div class="text-xs text-rose-400 font-semibold">{actress_link} <span class="text-slate-500 ml-1">/ {maker_name}</span></div>
            </td>
            <td class="py-4 px-3 text-xs text-slate-300 leading-snug hidden md:table-cell">
                {spec_summary}
            </td>
            <td class="py-4 px-3 text-center">
                <span class="text-amber-400 font-bold text-sm">{'★★★★★' if rank <= 2 else '★★★★☆'}</span>
            </td>
            <td class="py-4 px-3 text-center whitespace-nowrap">
                <a href="{aff_url}" target="_blank" rel="noopener noreferrer nofollow" class="inline-block px-3 py-1.5 bg-gradient-to-r from-rose-600 to-amber-600 hover:from-rose-500 hover:to-amber-500 text-white font-bold text-xs rounded-lg shadow transition">
                    公式視聴
                </a>
            </td>
        </tr>
        """

        points_html = "".join([f'<li class="flex items-start gap-2 text-slate-300 text-sm leading-relaxed"><span class="text-amber-400 font-bold mt-0.5">✔</span><span>{p}</span></li>' for p in points])

        item_samples_html = ""
        if sample_imgs:
            item_samples_html = '<div class="grid grid-cols-2 gap-2 mt-4">'
            for sidx, simg in enumerate(sample_imgs, 1):
                item_samples_html += f'<img src="{simg}" alt="{it_title} シーン {sidx}" class="w-full h-auto object-cover rounded-lg border border-slate-800 shadow" loading="lazy" />'
            item_samples_html += '</div>'

        ranking_sections += f"""
        <section id="rank-{rank}" class="my-12 p-6 sm:p-8 bg-slate-900/90 border border-slate-800 rounded-3xl shadow-2xl relative overflow-hidden">
            <div class="absolute -right-12 -top-12 w-40 h-40 bg-rose-600/10 rounded-full blur-3xl pointer-events-none"></div>
            
            <div class="flex items-center gap-3 mb-4 flex-wrap">
                <span class="inline-flex items-center justify-center px-4 py-1.5 rounded-full font-black text-sm {'bg-amber-400 text-slate-950 shadow-lg shadow-amber-400/40' if rank == 1 else 'bg-rose-600 text-white shadow-md' if rank == 2 else 'bg-slate-700 text-amber-300' if rank == 3 else 'bg-slate-800 text-slate-300'}">
                    第{rank}位
                </span>
                <span class="text-xs font-bold px-3 py-1 bg-rose-950/80 border border-rose-500/40 text-rose-300 rounded-full">
                    {badge}
                </span>
            </div>

            <h3 class="text-xl sm:text-2xl font-black text-white leading-snug mb-3">
                <a href="/posts/{cid}" class="hover:text-amber-300 transition">{it_title}</a>
            </h3>

            <div class="flex items-center gap-4 text-xs text-slate-400 mb-6 pb-4 border-b border-slate-800 flex-wrap">
                <div>主演女優: {actress_link}</div>
                <div>レーベル: <span class="text-slate-300 font-semibold">{maker_name}</span></div>
                <div>品番: <span class="text-slate-300 font-mono">{cid.upper()}</span></div>
                <div>個別解説: <a href="/posts/{cid}" class="text-amber-400 hover:text-amber-300 underline font-bold">完全書き下ろし詳細レビューを読む →</a></div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
                <div class="lg:col-span-5">
                    <a href="{aff_url}" target="_blank" rel="noopener noreferrer nofollow" class="block relative group overflow-hidden rounded-2xl border border-slate-700 shadow-xl">
                        <img src="{pkg_img}" alt="{it_title} パッケージ画像" class="w-full h-auto object-cover transform group-hover:scale-105 transition duration-300" loading="lazy" />
                        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex items-end p-4">
                            <span class="text-xs text-amber-300 font-bold">FANZA公式でプレビューを見る →</span>
                        </div>
                    </a>
                    {item_samples_html}
                </div>

                <div class="lg:col-span-7 space-y-4">
                    <div class="p-4 bg-slate-950/80 rounded-2xl border border-slate-800">
                        <h4 class="text-sm font-bold text-amber-300 mb-2.5 flex items-center gap-1.5">
                            <span>✦</span> 本作が選出された理由・決定的一撃
                        </h4>
                        <p class="text-slate-300 text-sm leading-relaxed mb-4">
                            {spec_summary}
                        </p>
                        <h5 class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">注目ポイント & 見どころハイライト</h5>
                        <ul class="space-y-2">
                            {points_html}
                        </ul>
                    </div>

                    <div class="pt-2">
                        <a href="{aff_url}" target="_blank" rel="noopener noreferrer nofollow" class="inline-flex items-center justify-center gap-2 w-full py-4 bg-gradient-to-r from-rose-600 via-rose-500 to-amber-600 hover:from-rose-500 hover:to-amber-500 text-white font-extrabold text-base rounded-xl shadow-lg hover:shadow-rose-500/50 transform hover:-translate-y-0.5 transition duration-200">
                            <span>第{rank}位：FANZA公式で高画質フル本編を視聴</span>
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                        </a>
                        <div class="text-center mt-2">
                            <a href="/posts/{cid}" class="text-xs text-slate-400 hover:text-amber-300 underline transition">
                                本作の約4,000文字に及ぶ個別詳細解説・見どころ詳細はこちら →
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """

    faqs_html = ""
    if faqs:
        faqs_html = """
        <div class="my-12 p-6 sm:p-8 bg-slate-900/60 border border-slate-800 rounded-3xl shadow-xl">
            <h3 class="text-xl font-black text-white mb-6 border-l-4 border-amber-400 pl-3">
                【よくある質問】このジャンルに関するQ&Aと選び方のコツ
            </h3>
            <div class="space-y-4">
        """
        for q, a in faqs:
            faqs_html += f"""
            <div class="p-4 bg-slate-950/70 rounded-2xl border border-slate-800/80">
                <h4 class="font-bold text-amber-300 text-sm mb-2 flex items-center gap-2">
                    <span class="inline-block w-5 h-5 rounded-full bg-amber-400/20 text-amber-300 text-xs text-center leading-5 font-bold">Q</span>
                    {q}
                </h4>
                <p class="text-slate-300 text-sm leading-relaxed pl-7">
                    {a}
                </p>
            </div>
            """
        faqs_html += "</div></div>"

    related_html = ""
    if related:
        related_html = """
        <div class="my-12 p-6 sm:p-8 bg-slate-900/80 border border-slate-800 rounded-3xl shadow-xl">
            <h3 class="text-xl font-black text-white mb-6 border-l-4 border-rose-500 pl-3">
                あわせて読みたい！おすすめの背徳特集・人気ジャンルランキング
            </h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        """
        for rurl, rtitle, rdesc in related:
            related_html += f"""
            <a href="{rurl}" class="p-4 bg-slate-950/80 hover:bg-slate-800/60 border border-slate-800 hover:border-rose-500/50 rounded-2xl transition group block">
                <h4 class="font-bold text-white group-hover:text-amber-300 text-sm mb-1.5 transition leading-snug">
                    {rtitle}
                </h4>
                <p class="text-xs text-slate-400 leading-relaxed line-clamp-2">
                    {rdesc}
                </p>
            </a>
            """
        related_html += "</div></div>"

    genre_tags_html = " ".join([get_genre_link(g) for g in genres])

    full_body = f"""
    <div class="article-content space-y-8 text-slate-200 leading-relaxed font-sans text-base">
        <!-- 導入リード文 -->
        <div class="p-6 sm:p-8 bg-gradient-to-br from-slate-900 via-slate-950 to-slate-900 border border-slate-800 rounded-3xl shadow-2xl">
            <div class="flex flex-wrap gap-2 mb-4">
                {genre_tags_html}
            </div>
            <p class="text-slate-200 text-base sm:text-lg leading-relaxed mb-4">
                {lead_p1}
            </p>
            <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
                {lead_p2}
            </p>
        </div>

        <!-- 比較ランキングまとめテーブル -->
        <div class="my-8 overflow-hidden rounded-2xl border border-slate-800 bg-slate-950/80 shadow-2xl">
            <div class="p-4 bg-slate-900 border-b border-slate-800 font-bold text-amber-300 text-sm flex items-center justify-between">
                <span>【一目でわかる】厳選TOP5 スペック比較一覧表</span>
                <span class="text-xs text-slate-400 font-normal">※横スクロールで詳細確認可能</span>
            </div>
            <div class="overflow-x-auto">
                <table class="w-full text-left border-collapse min-w-[640px]">
                    <thead>
                        <tr class="border-b border-slate-800 bg-slate-900/60 text-slate-400 text-xs font-semibold">
                            <th class="py-3 px-3 text-center">順位</th>
                            <th class="py-3 px-3">作品タイトル / 主演</th>
                            <th class="py-3 px-3 hidden md:table-cell">特化ポイント</th>
                            <th class="py-3 px-3 text-center">おすすめ度</th>
                            <th class="py-3 px-3 text-center">公式</th>
                        </tr>
                    </thead>
                    <tbody>
                        {table_rows}
                    </tbody>
                </table>
            </div>
        </div>

        <!-- 各作品の徹底解説セクション -->
        <div class="space-y-6">
            {ranking_sections}
        </div>

        <!-- FAQセクション -->
        {faqs_html}

        <!-- 内部回遊レコメンド -->
        {related_html}
    </div>
    """

    char_cnt = count_japanese_chars(full_body)

    first_item = items[0]
    top_cid = first_item["cid"]
    top_it = fetched_items.get(top_cid, {})
    top_pkg = top_it.get("imageURL", {}).get("large", "")
    top_aff = top_it.get("affiliate_url_clean") or top_it.get("affiliateURL", "")
    top_actresses = [a.get("name") for a in top_it.get("iteminfo", {}).get("actress", [])]

    feature_post_data = {
        "id": f_id,
        "title": f_title,
        "date": "2026-10-11 12:00:00",
        "actresses": top_actresses,
        "maker": "FANZAキラー特集",
        "genres": genres,
        "url": top_aff,
        "image": top_pkg,
        "sample_images": get_sample_images(top_it, 4),
        "body": full_body,
        "character_count": char_cnt,
        "is_feature": True,
        "ranking_cids": [x["cid"] for x in items]
    }
    return feature_post_data

def main():
    print("=== Start Generating Killer Features v14 ===")
    
    # 全15作品のメタデータをFANZA APIから取得
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
                print(f"Generated Post: {cid} ({post['character_count']} chars)")

    # 2. キラー特集3記事の生成
    for f in FEATURE_ARTICLES:
        f_post = generate_feature_article(f, fetched_data)
        out_path = os.path.join(OUTPUT_DIR, f"{f_post['id']}.json")
        with open(out_path, "w", encoding="utf-8") as out_f:
            json.dump(f_post, out_f, ensure_ascii=False, indent=2)
        generated_posts.append(f_post)
        print(f"Generated Feature: {f_post['id']} ({f_post['character_count']} chars)")

    # posted_cache.txtの更新
    with open("posted_cache.txt", "a", encoding="utf-8") as f:
        for cid in all_cids:
            f.write(f"{cid}\n")

    print(f"\nAll Done! Successfully generated {len(generated_posts)} articles.")

if __name__ == "__main__":
    main()
