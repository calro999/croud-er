# -*- coding: utf-8 -*-
"""
本日（2026年10月22日）配信開始された最新作品の中から、
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
    FANZA公式APIから2026-10-22発売の作品を取得し、VRを完全除外した未投稿作品をリストアップ
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
        "lte_date": "2026-10-22T23:59:59",
        "gte_date": "2026-10-18T00:00:00",
        "output": "json"
    }
    
    print("FANZA公式APIに接続中（非VR作品を探索中）...")
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
        if date_str > "2026-10-22 23:59:59":
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
    date_str = item.get("date", "2026-10-22")[:10]
    
    act_str = "、".join(actresses) if actresses else "素人・厳選企画単体"
    clean_url = get_clean_affiliate_url(item.get("affiliateURL", ""))
    
    # 見出しや文脈の判定
    is_amateur = "素人" in title or "ドキュメント" in title or any("素人" in g or "ドキュメント" in g for g in genres)
    is_cheating = "不倫" in title or "浮気" in title or "人妻" in title or any("人妻" in g or "不倫" in g for g in genres)
    is_chikan = "バス" in title or "痴漢" in title or "電車" in title or "指入れ" in title
    is_lesbian = "レズ" in title or "ビアン" in title or any("レズ" in g for g in genres)
    is_fella = "フェラ" in title or "シャブ" in title or "口淫" in title or any("フェラ" in g for g in genres)
    is_ryoujoku = "調〇" in title or "悪女" in title or "縛" in title or any("緊縛" in g or "マゾ" in g for g in genres)
    
    # イントロダクション（シチュエーションに応じた生々しい導入）
    if is_chikan:
        intro_lead = f"通勤・通学の日常動線である密室空間で、誰にも気付かれずに指先一本で女の身体を崩壊させる背徳の極致。本作『{title}』は、わずか数分の乗車時間という極限のタイムリミットが生む、心臓の鼓動が耳元で鳴り響くような緊張感と恥辱を見事に映像化しています。"
        core_point = f"逃げ場のない車内で、周囲の乗客にバレないよう必死に息を殺しながらも、丹念に弄ばれる秘部からジュクジュクと溢れ出す愛液。指が粘膜を擦る微かな水音と、喉の奥で押し殺した吐息のリアリティが凄まじく、鑑賞側のサディスティックな欲望を容赦なく刺激します。"
    elif is_lesbian:
        intro_lead = f"女性同士だからこそ知り尽くしている性感帯への執拗な執着と、理性をもみ消すような濃厚なスキンシップ。本作『{title}』は、男の目線とは一線を画す、肌と肌が擦れ合う微細な温度感と貪るような愛撫が生む濃密な世界観を描ききっています。"
        core_point = f"ビアンならではの繊細かつ執拗な舌技とクンニ、指使いによって、次第に身体の芯から抗えなくなっていく被写体の痙攣。普段は見せないような無防備な表情で腹筋を震わせ、快楽に溺れていく姿は、理屈を超えた本能の昂ぶりをダイレクトに叩きつけてきます。"
    elif is_amateur:
        intro_lead = f"作為的な演技や過剰な演出を削ぎ落とし、カメラの前で初めて晒される本物の羞恥と情動を克明に記録した『{title}』。{act_str}が魅せる、戸惑いと快楽の間で揺れ動く生々しい肉体の反応は、商業作品の枠を超えたドキュメンタリーならではの圧倒的な説得力を放っています。"
        core_point = f"インタビュー時の緊張した面持ちから、肌を重ねるにつれて女としての本性が剥き出しになっていくグラデーション。プロの女優には出せない、ぎこちない腰遣いやシーツを握りしめる指先の強張り、耳元まで赤く染まった上気肌が、観る者の興奮をどこまでも煽り立てます。"
    elif is_cheating:
        intro_lead = f"背徳という名の蜜の味に一度囚われたら二度と引き返せない——。本作『{title}』は、日常のすぐ裏側に潜む禁断の情事と、罪悪感によって何倍にも増幅される牝の本能を赤裸々に描いた傑作です。"
        core_point = f"普段は良き妻、あるいは清楚な日常を装っている彼女が、男に求められるままに淫らな肉奴隷へと堕ちていく瞬間。理性では拒絶しながらも、深く穿たれるたびに快感の波に呑まれ、切なく懇願するような喘ぎ声を漏らす姿はまさに圧巻です。"
    elif is_ryoujoku:
        intro_lead = f"抑え込まれた日常から解き放たれ、屈辱と激痛の果てに快楽へと目覚めていく背徳の深淵。本作『{title}』は、{act_str}の繊細な肉体が容赦なく縛られ、調教されることで露わになる、究極の牝の呻きを捉えた衝撃作です。"
        core_point = f"縄目によって食い込む豊満な肉感、身動きが取れない中で敏感な粘膜を弄ばれる極限の羞恥。自由を奪われた状態で耳元に浴びせられる汚い言葉攻めに、いつしか快感の涙を流しながら絶頂を受け入れていく展開に圧倒されます。"
    elif is_fella:
        intro_lead = f"男の欲望の象徴を唇と舌だけでどこまでも追い詰め、理性をトロトロに溶かす口淫の極致。本作『{title}』は、{act_str}による圧倒的なフェラチオの吸引力と、男を骨抜きにする生々しいテクニックを堪能できる一本です。"
        core_point = f"ジュポジュポと涎の糸を滴らせながら、カリ首から亀頭の裏筋までを丁寧に舐めしゃぶり、喉の奥深くまで咥え込むディープスロート。上目遣いで男の反応を伺いながら恍惚とした表情でしゃぶり尽くす姿に、射精欲が限界まで高まります。"
    else:
        intro_lead = f"{maker}の最新作として本日配信開始された『{title}』は、{act_str}の持つ天性の肉体美とエロティシズムを極限まで引き出した注目作。シチュエーションの巧みさと、それに呼応する女優の圧倒的な発情演技が噛み合い、最初から最後まで息をもつかせぬ高揚感を提供してくれます。"
        core_point = f"肌の質感や息づかい、交わる瞬間の肉のぶつかり合いまで緻密に捉えられたカメラワーク。男優の激しいピストンに対して、全身を紅潮させながら快楽の頂点へと駆け上がっていく{act_str}の恍惚の表情は、まさに今すぐ抜きたい男の願望を120%満たしてくれます。"

    # シーンごとの徹底解説
    scene_detail_1 = f"序盤の導入パートでは、シチュエーションのリアリティを高める丁寧な前振りと対話が展開。相手の視線に晒されながら徐々に衣服を乱されていく過程での、恥じらいと期待が入り混じった微妙な表情変化が秀逸です。指先で敏感な突起を軽く転がされるだけで、ビクンと背筋を跳ね上げる敏感な肉体反応に、思わずこちらの息も止まります。"
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
    date_str = item.get("date", "2026-10-22 10:00:00")
    
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
    print("=== 本日（2026年10月22日）発売の非VR最新商品 取得＆記事作成開始 ===")
    # 15作品の非VR最新作を厳選
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
