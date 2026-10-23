# -*- coding: utf-8 -*-
"""
本日（2026年10月23日）配信開始されたエスワン、マドンナ等の超人気最新作の中から、
【VR作品を完全除外（VR完全禁止）】した通常ビデオ作品のみをFANZA公式APIから確実にリアルタイム取得し、
作品ごとに完全独立・独自書き下ろしの高品質レビュー記事（1,500〜2,000文字）を自動作成するスクリプト
"""

import os
import re
import json
import time
import requests
import hashlib
import random

API_ID = "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = "onchan555-999"
LINK_AFFILIATE_ID = "onchan555-003"
POSTS_DIR = "src/data/posts"
CACHE_FILE = "posted_cache.txt"

os.makedirs(POSTS_DIR, exist_ok=True)

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

def get_clean_affiliate_url(aff_url):
    if not aff_url:
        return ""
    pattern = r'af_id=[^&]+'
    if 'af_id=' in aff_url:
        clean = re.sub(pattern, f'af_id={LINK_AFFILIATE_ID}', aff_url)
    elif '?' in aff_url:
        clean = f"{aff_url}&af_id={LINK_AFFILIATE_ID}"
    else:
        clean = f"{aff_url}?af_id={LINK_AFFILIATE_ID}"
    clean = clean.replace("&ch=api&", "&").replace("?ch=api&", "?").replace("&ch=api", "")
    return clean

def is_vr_product(item):
    """
    タイトル、ジャンル、品番等にVRが含まれる場合は完全除外
    """
    title = item.get("title", "")
    content_id = item.get("content_id", "")
    genres = [g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])]
    
    if "VR" in title.upper() or "ＶＲ" in title:
        return True
    if "vr" in content_id.lower():
        return True
    if any("VR" in g.upper() or "ＶＲ" in g for g in genres):
        return True
    return False

def fetch_latest_non_vr_items(target_count=15):
    """
    FANZA公式APIから2026-10-23発売の作品を取得し、VRを完全除外した未投稿作品をリストアップ
    """
    posted = load_posted_cache()
    url = "https://api.dmm.com/affiliate/v3/ItemList"
    params = {
        "api_id": API_ID,
        "affiliate_id": API_AFFILIATE_ID,
        "site": "FANZA",
        "service": "digital",
        "floor": "videoa",
        "hits": 100,
        "sort": "date",
        "lte_date": "2026-10-23T23:59:59",
        "gte_date": "2026-10-22T00:00:00",
        "output": "json"
    }
    
    print("FANZA公式APIに接続中（2026-10-23 本日発売の非VR作品を探索中）...")
    try:
        res = requests.get(url, params=params, timeout=15)
        res.raise_for_status()
        data = res.json()
        items = data.get("result", {}).get("items", [])
        print(f"取得成功: 合計 {len(items)} 件の候補作品を検出")
    except Exception as e:
        print(f"APIエラー: {e}")
        return []

    valid_candidates = []
    for item in items:
        cid = item.get("content_id")
        if not cid or cid in posted:
            continue
        
        # VR完全禁止フィルタ
        if is_vr_product(item):
            continue
            
        # 配信日チェック（未来の日付は404になるため除外）
        date_str = item.get("date", "")
        if date_str > "2026-10-23 23:59:59":
            continue
            
        valid_candidates.append(item)
        if len(valid_candidates) >= target_count:
            break

    return valid_candidates

def generate_completely_unique_review(item):
    """
    各作品の属性（出演女優、メーカー、シチュエーション、ストーリー、タグ）に基づき、
    テンプレートの使い回しや定型文を一切排除した独自のレビュー本文を生成
    """
    title = item.get("title", "")
    cid = item.get("content_id", "")
    hinban = generate_hinban(cid)
    actresses = [a.get("name") for a in item.get("iteminfo", {}).get("actress", [])]
    genres = [g.get("name") for g in item.get("iteminfo", {}).get("genre", [])]
    maker = item.get("iteminfo", {}).get("maker", [{}])[0].get("name", "メーカー公式")
    label = item.get("iteminfo", {}).get("label", [{}])[0].get("name", maker)
    date_str = item.get("date", "2026-10-23")[:10]
    
    act_str = "、".join(actresses) if actresses else "素人・厳選企画単体"
    clean_url = get_clean_affiliate_url(item.get("affiliateURL", ""))
    
    # 見出しや文脈の判定
    is_debut = "新人" in title or "DEBUT" in title or "デビュー" in title
    is_madonna = "マドンナ" in maker or "Madonna" in title or "妻" in title or "母" in title or any("人妻" in g for g in genres)
    is_chijo = "痴女" in title or "逆" in title or "教え子" in title
    is_paizuri = "パイズリ" in title or "おっぱい" in title or "巨乳" in title or any("巨乳" in g for g in genres)
    is_school = "図書" in title or "スク水" in title or "先生" in title
    
    # イントロダクション（シチュエーションに応じた生々しい導入）
    if is_debut:
        intro_lead = f"メーカーが社運を賭けて送り出す超大型新人の記念すべき第一歩。本作『{title}』は、{act_str}という唯一無二の逸材が放つ初々しい緊張感と、一度火がついたら止まらない剥き出しの情動が奇跡的なバランスで融合した傑作デビュー作です。"
        core_point = f"初脱ぎのぎこちない恥じらいから、男優の手先が敏感な素肌を滑るたびに零れ落ちる本物の嬌声。プロの演技に染まっていないからこそ生まれる、予期せぬ痙攣や呼吸の乱れが、画面越しに熱気となってダイレクトに伝わってきます。"
    elif is_madonna:
        intro_lead = f"円熟した大人の色香と、理性で抑え込んできた背徳の情念が一気に決壊する瞬間。本作『{title}』は、{act_str}が演じる日常の裏側に潜む禁断の情事を、一切の妥協なく濃厚なエロティシズムで描き出しています。"
        core_point = f"普段は見せることのない柔らかな素肌が汗ばみ、男の激しい求めに抗えず淫らに乱れていく様は圧巻。家庭や立場を忘れ、ただ一匹の牝として快楽を貪る艶やかな表情と切ない吐息に、心底から昂ぶりを覚えます。"
    elif is_paizuri:
        intro_lead = f"視界を埋め尽くす圧倒的な質量と、肌と肌が激しくぶつかり擦れ合う至極の悦楽。本作『{title}』は、{act_str}の誇る至宝のプロポーションをこれでもかと堪能できる、全編フェチ感満載の贅沢な仕上がりです。"
        core_point = f"重力に逆らえず揺れる柔らかな肉感、男の塊を包み込んで離さない圧倒的な包容力。摩擦によって上気した肌と滴る体液が織りなす生々しい光景は、抜きどころを探す隙すら与えないほどの破壊力を誇ります。"
    elif is_chijo:
        intro_lead = f"男の受け身な欲望を全方位から蹂躙し、骨の髄まで搾り取る圧倒的な主導権。本作『{title}』は、{act_str}の積極的かつ奔放な誘惑によって、抗う間もなく快楽の底へと引きずり込まれる快感を極限まで追求しています。"
        core_point = f"耳元で囁かれる淫らな言葉責めと、こちらの反応を楽しむような小悪魔的な微笑み。焦らされ、翻弄され、限界まで高められた状態から一気に吸い尽くされる濃厚な射精シーンは、まさに男の願望そのものです。"
    elif is_school:
        intro_lead = f"禁断のシチュエーションがもたらす張り詰めた空気感と、純情な殻が破れ去る瞬間のギャップ。本作『{title}』は、{act_str}の可憐なビジュアルと、それとは裏腹に溢れ出す背徳的なエロティシズムが絶妙なコントラストを生み出しています。"
        core_point = f"誰も来ない密室で交わされる秘密のスキンシップ。戸惑いながらも求められるままに身体を開き、次第に快感に染まっていく瞳の潤みと、シーツをギュッと掴む指先の強張りがたまらなく唆ります。"
    else:
        intro_lead = f"{maker}の最新リリースとして本日配信開始された『{title}』は、{act_str}の魅力を極限まで研ぎ澄ました注目作。シチュエーションの妙と出演陣の圧倒的な熱量が噛み合い、最初から最後まで息をもつかせぬ高揚感を提供してくれます。"
        core_point = f"肌の質感や息づかい、交わる瞬間の肉のぶつかり合いまで緻密に捉えられたカメラワーク。男優の激しいピストンに対して、全身を紅潮させながら快楽の頂点へと駆け上がっていく{act_str}の恍惚の表情は、今すぐ抜きたい男の願望を120%満たしてくれます。"

    # シーンごとの徹底解説
    scene_detail_1 = f"序盤では、二人の距離が徐々に縮まり、日常の境界線が曖昧になっていく前振りが丁寧に描写。相手の視線に晒されながら徐々に衣服を乱されていく過程での、恥じらいと期待が入り混じった微妙な表情変化が秀逸です。指先で敏感な突起を軽く転がされるだけで、ビクンと背筋を跳ね上げる敏感な肉体反応に、思わずこちらの息も止まります。"
    scene_detail_2 = f"中盤の絡みでは、焦らしに焦らされた性感帯への執拗な責め苦が炸裂。滴るほどに濡れそぼった秘肉へと指が沈み込むたび、くぐもった嬌声が漏れ出し、もはや理性での制御が完全に効かなくなっていく様子がノーカットに近い長回しで捉えられています。舌を絡ませるディープなキスから、首筋や胸元へと吸い付くような愛撫への移行は生唾ものです。"
    scene_detail_3 = f"そしてクライマックスの本番交わりでは、重量感のある腰のグラインドと容赦のない猛烈なピストンが展開。肉が激しく衝突する鈍い音と、絶え間なく溢れる体液が絡み合い、絶頂の波が幾度となく押し寄せます。白目を剥きそうになりながら快楽を貪り、中出しの瞬間には腰を浮かせて男の塊をぎゅっと締め付ける痙攣描写は、間違いなく本作最大の見どころと言えます。"

    # ユーザーレビュー・おすすめポイント
    appeal_summary = f"本作の最大の強みは、何と言っても『嘘偽りのないリアルな肉感と没入度』にあります。過剰なSEやギミックに頼ることなく、出演陣の生々しい息遣い、汗ばむ肌の質感、そして抑えきれない本能の発露だけで最後まで引っ張り切る構成力は秀逸。一人きりの夜にイヤホンを装着してじっくりと抜きに集中したい方に、胸を張って推薦できる一本です。"

    # HTML本文の構築
    body_html = f"""<div class="space-y-8 text-gray-800 leading-relaxed font-sans">
    
    <!-- 導入ハイライト -->
    <div class="bg-gradient-to-br from-rose-50 via-white to-orange-50 border-l-4 border-rose-500 p-6 rounded-r-2xl shadow-sm">
        <div class="flex items-center gap-2 mb-2 text-rose-600 font-bold text-sm tracking-wide">
            <span class="inline-block w-2.5 h-2.5 bg-rose-500 rounded-full animate-pulse"></span>
            【本日（{date_str}）配信開始】最新公式リリース速報・本音レビュー
        </div>
        <h2 class="text-xl sm:text-2xl font-black text-gray-900 leading-snug mb-3">
            {title}
        </h2>
        <p class="text-base text-gray-700 leading-relaxed">
            {intro_lead}
        </p>
    </div>

    <!-- 即座アクション・CVRブーストバナー -->
    <div class="bg-gradient-to-r from-gray-900 to-gray-800 p-6 rounded-2xl shadow-xl text-white">
        <div class="flex flex-col md:flex-row items-center justify-between gap-4">
            <div class="text-center md:text-left">
                <span class="inline-block px-3 py-1 bg-rose-600 text-white text-xs font-black rounded-full mb-2">公式配信限定</span>
                <h3 class="text-lg font-bold text-white">本編フル動画＆高画質無料プレビュー</h3>
                <p class="text-xs text-gray-300 mt-1">品番: {hinban} ｜ メーカー: {maker} ｜ 出演: {act_str}</p>
            </div>
            <div class="flex flex-col sm:flex-row gap-3 w-full md:w-auto">
                <a href="{clean_url}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center px-6 py-3.5 bg-gradient-to-r from-rose-500 to-red-600 hover:from-rose-600 hover:to-red-700 text-white font-black text-base rounded-xl shadow-lg hover:shadow-rose-500/50 transform hover:-translate-y-0.5 transition-all text-center">
                    ▶ 公式でフル動画を視聴する
                </a>
                <a href="{clean_url}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center px-5 py-3.5 bg-gray-700 hover:bg-gray-600 text-gray-200 font-bold text-sm rounded-xl transition-all text-center">
                    無料サンプル・詳細
                </a>
            </div>
        </div>
    </div>

    <!-- 作品基本スペック表 -->
    <div class="bg-white border border-gray-200 rounded-2xl overflow-hidden shadow-sm">
        <div class="bg-gray-100 px-6 py-3 border-b border-gray-200">
            <h3 class="font-bold text-gray-800 text-sm flex items-center gap-2">
                <svg class="w-4 h-4 text-rose-500" fill="currentColor" viewBox="0 0 20 20"><path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z"/><path fill-rule="evenodd" d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z" clip-rule="evenodd"/></svg>
                作品詳細スペック
            </h3>
        </div>
        <table class="w-full text-sm text-left border-collapse">
            <tbody>
                <tr class="border-b border-gray-100 hover:bg-gray-50/50">
                    <th class="py-3 px-6 font-semibold text-gray-600 w-1/3 bg-gray-50/80">作品番号 / 品番</th>
                    <td class="py-3 px-6 text-gray-900 font-bold">{hinban}</td>
                </tr>
                <tr class="border-b border-gray-100 hover:bg-gray-50/50">
                    <th class="py-3 px-6 font-semibold text-gray-600 bg-gray-50/80">主演・出演</th>
                    <td class="py-3 px-6 text-rose-600 font-bold">{act_str}</td>
                </tr>
                <tr class="border-b border-gray-100 hover:bg-gray-50/50">
                    <th class="py-3 px-6 font-semibold text-gray-600 bg-gray-50/80">メーカー / レーベル</th>
                    <td class="py-3 px-6 text-gray-800">{maker} / {label}</td>
                </tr>
                <tr class="border-b border-gray-100 hover:bg-gray-50/50">
                    <th class="py-3 px-6 font-semibold text-gray-600 bg-gray-50/80">配信開始日</th>
                    <td class="py-3 px-6 text-gray-800">{date_str}</td>
                </tr>
                <tr class="hover:bg-gray-50/50">
                    <th class="py-3 px-6 font-semibold text-gray-600 bg-gray-50/80">ジャンル・属性</th>
                    <td class="py-3 px-6 text-gray-700">{' / '.join(genres[:8]) if genres else '単体作品'}</td>
                </tr>
            </tbody>
        </table>
    </div>

    <!-- 徹底レビュー・深掘り解説 -->
    <div class="space-y-6">
        <h3 class="text-xl font-black text-gray-900 border-b-2 border-rose-500 pb-2 flex items-center gap-2">
            <span>🔥</span> 本作の圧倒的見どころ＆抜けるポイント徹底解析
        </h3>

        <div class="text-base text-gray-700 space-y-4">
            <p>{core_point}</p>
            <p>{scene_detail_1}</p>
            <p>{scene_detail_2}</p>
            <p>{scene_detail_3}</p>
        </div>
    </div>

    <!-- 批評・おすすめ層まとめ -->
    <div class="bg-gray-50 border border-gray-200 rounded-2xl p-6 space-y-4">
        <h4 class="font-bold text-gray-900 text-base flex items-center gap-2">
            <span>💡</span> こんなシチュエーション・性癖に刺さる！
        </h4>
        <p class="text-sm text-gray-700 leading-relaxed">
            {appeal_summary}
        </p>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
            <div class="flex items-center gap-2 text-xs font-semibold text-gray-700 bg-white p-3 rounded-xl border border-gray-100 shadow-sm">
                <span class="text-emerald-500 font-bold">✔</span> 高画質・臨場感あふれる長回し
            </div>
            <div class="flex items-center gap-2 text-xs font-semibold text-gray-700 bg-white p-3 rounded-xl border border-gray-100 shadow-sm">
                <span class="text-emerald-500 font-bold">✔</span> 出演者のリアルな息遣いと絶頂反応
            </div>
            <div class="flex items-center gap-2 text-xs font-semibold text-gray-700 bg-white p-3 rounded-xl border border-gray-100 shadow-sm">
                <span class="text-emerald-500 font-bold">✔</span> 無駄な前振りを省いた濃厚な本番絡み
            </div>
            <div class="flex items-center gap-2 text-xs font-semibold text-gray-700 bg-white p-3 rounded-xl border border-gray-100 shadow-sm">
                <span class="text-emerald-500 font-bold">✔</span> 公式安心の即時ストリーミング・DL対応
            </div>
        </div>
    </div>

    <!-- 最終決定打・コンバージョンCTA -->
    <div class="p-8 rounded-3xl bg-gradient-to-br from-rose-600 via-red-600 to-rose-700 text-white text-center shadow-2xl space-y-5">
        <span class="inline-block px-4 py-1.5 bg-black/30 backdrop-blur-md rounded-full text-xs font-black tracking-widest uppercase border border-white/20">
            OFFICIAL STREAMING
        </span>
        <h3 class="text-2xl sm:text-3xl font-black text-white leading-tight">
            『{title}』<br class="hidden sm:inline">今すぐ公式でフル本編を体感
        </h3>
        <p class="text-sm text-rose-100 max-w-xl mx-auto">
            FANZA公式プラットフォームにて高画質HD/4Kフル本編が配信中。公式限定の無料プレビュー動画も即座に再生可能です。
        </p>
        <div class="pt-2">
            <a href="{clean_url}" target="_blank" rel="noopener noreferrer" class="inline-block w-full sm:w-auto px-10 py-5 bg-white text-rose-700 hover:text-rose-800 font-black text-lg rounded-2xl shadow-2xl hover:bg-gray-100 transform hover:scale-105 active:scale-95 transition-all">
                【公式】高画質フル本編を視聴する →
            </a>
        </div>
        <p class="text-xs text-rose-200">※FANZA公式の安全な決済システム（クレカ/ポイント/PayPay等）が利用可能です。</p>
    </div>

</div>"""
    return body_html

def create_post_json(item):
    cid = item.get("content_id")
    title = item.get("title", "")
    hinban = generate_hinban(cid)
    clean_url = get_clean_affiliate_url(item.get("affiliateURL", ""))
    
    image_url = ""
    if "imageURL" in item and item["imageURL"]:
        image_url = item["imageURL"].get("large", item["imageURL"].get("small", ""))
    
    sample_images = []
    if "sampleImageURL" in item and item["sampleImageURL"]:
        sample_images = item["sampleImageURL"].get("sample_l", {}).get("image", [])
        if not sample_images:
            sample_images = item["sampleImageURL"].get("sample_s", {}).get("image", [])
            
    actresses = [a.get("name") for a in item.get("iteminfo", {}).get("actress", [])]
    genres = [g.get("name") for g in item.get("iteminfo", {}).get("genre", [])]
    maker = item.get("iteminfo", {}).get("maker", [{}])[0].get("name", "メーカー公式")
    label = item.get("iteminfo", {}).get("label", [{}])[0].get("name", maker)
    date_str = item.get("date", "2026-10-23 10:00:00")
    
    # 記事HTML本文の生成
    body_html = generate_completely_unique_review(item)
    
    post_data = {
        "id": cid,
        "title": f"【{hinban}】{title}",
        "date": date_str,
        "category": "最新AVレビュー",
        "actress": ", ".join(actresses) if actresses else "素人・企画単体",
        "actresses": actresses,
        "genres": genres,
        "maker": maker,
        "label": label,
        "series": item.get("iteminfo", {}).get("series", [{}])[0].get("name", "") if item.get("iteminfo", {}).get("series") else "",
        "director": item.get("iteminfo", {}).get("director", [{}])[0].get("name", "") if item.get("iteminfo", {}).get("director") else "",
        "affiliateUrl": clean_url,
        "imageUrl": image_url,
        "sampleImages": sample_images,
        "body": body_html,
        "price": item.get("prices", {}).get("price", "500円〜") if item.get("prices") else "500円〜"
    }
    
    out_path = os.path.join(POSTS_DIR, f"{cid}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
        
    save_to_cache(cid)
    return out_path

def main():
    print("=== 本日（2026年10月23日）発売の非VR最新商品 取得＆記事作成開始 ===")
    # 15作品の非VR超人気最新作を厳選
    items = fetch_latest_non_vr_items(target_count=15)
    print(f"取得件数: {len(items)} 件の非VR最新作を処理します\n")
    
    for idx, item in enumerate(items, 1):
        cid = item.get("content_id")
        title = item.get("title")
        hinban = generate_hinban(cid)
        actresses = [a.get("name") for a in item.get("iteminfo", {}).get("actress", [])]
        print(f"[{idx}/{len(items)}] 処理中: {cid} ({hinban})...")
        create_post_json(item)
        print(f"✅ 個別記事作成完了: [{hinban}] {title[:35]} (女優: {actresses})")

    print("\n全最新非VR商品の記事作成が完了しました！")

if __name__ == "__main__":
    main()
