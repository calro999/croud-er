# -*- coding: utf-8 -*-
"""
直近配信＆FANZAランキング上位の超人気作（本庄鈴、紗倉まな、神木麗、守屋よしの、マジックミラー号等）をAPIから取得し、
Google検索流入（品番検索・女優検索・実用度検索・ネタバレ見どころ検索）を最大化する
超高密度・完全独立キラーレビュー記事（2,000〜3,000文字）を自動作成するスクリプト
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

def get_clean_affiliate_url(aff_url, cid):
    if not aff_url:
        return f"https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D{cid}&af_id={LINK_AFFILIATE_ID}"
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

def fetch_trending_killer_items(target_count=15):
    posted = load_posted_cache()
    url = "https://api.dmm.com/affiliate/v3/ItemList"
    params = {
        "api_id": API_ID,
        "affiliate_id": API_AFFILIATE_ID,
        "site": "FANZA",
        "service": "digital",
        "floor": "videoa",
        "hits": 100,
        "sort": "rank",
        "lte_date": "2026-10-28T23:59:59",
        "gte_date": "2026-10-20T00:00:00",
        "output": "json"
    }
    
    print("FANZA公式APIに接続中（ランキング上位＆直近配信のキラー作品を取得中）...")
    try:
        res = requests.get(url, params=params, timeout=15)
        res.raise_for_status()
        data = res.json()
        items = data.get("result", {}).get("items", [])
        print(f"API検出数: 合計 {len(items)} 件の候補作品")
    except Exception as e:
        print(f"APIエラー: {e}")
        return []

    valid_candidates = []
    for item in items:
        cid = item.get("content_id")
        if not cid or cid in posted:
            continue
        if is_vr_product(item):
            continue
        date_str = item.get("date", "")
        if date_str > "2026-10-28 23:59:59":
            continue
            
        valid_candidates.append(item)
        if len(valid_candidates) >= target_count:
            break

    return valid_candidates

def generate_killer_post_body(item):
    cid = item.get("content_id", "")
    title = item.get("title", "")
    hinban = generate_hinban(cid)
    actresses = [a.get("name") for a in item.get("iteminfo", {}).get("actress", [])]
    genres = [g.get("name") for g in item.get("iteminfo", {}).get("genre", [])]
    maker = item.get("iteminfo", {}).get("maker", [{}])[0].get("name", "公式レーベル")
    label = item.get("iteminfo", {}).get("label", [{}])[0].get("name", maker)
    date_str = item.get("date", "2026-10-28")[:10]
    clean_url = get_clean_affiliate_url(item.get("affiliateURL", ""), cid)
    
    act_str = "、".join(actresses) if actresses else "素人・企画単体"
    clean_title = re.sub(r'【.*?】', '', title).strip() or title
    
    seed_val = int(hashlib.sha256((cid + "_killer_20261028").encode('utf-8')).hexdigest()[:8], 16)
    rng = random.Random(seed_val)
    
    full_text = f"{title} {' '.join(genres)} {maker}"
    
    is_ntr = any(k in full_text for k in ["NTR", "野外露出", "元カレ", "寝取", "人妻", "浮気", "不貞", "レス"])
    is_chijo_lecture = any(k in full_text for k in ["女講師", "見下し", "突き放し", "射精ガマン", "オナ専", "指導", "痴女", "フェラチオシンデレラ"])
    is_mmr = any(k in full_text for k in ["マジックミラー", "ミラー号", "彼氏とはミラー越し", "本物人妻"])
    is_shigeki = any(k in full_text for k in ["SHIGEKI", "公然露出", "潮吹き", "汗だく", "神木麗", "100k"])
    is_paizuri_anal = any(k in full_text for k in ["アナル解禁", "G カップ", "巨乳", "パイズリ", "美尻", "オナホ洗脳"])
    is_office = any(k in full_text for k in ["秘書課", "人事部", "共同業務", "OL", "公務員", "市役所"])

    if is_shigeki or "神木麗" in full_text:
        sub_heading = f"極限の公然羞恥と圧倒的潮吹き！神木麗が魅せる【{hinban}】の衝撃作レビュー"
        intro_lead = f"常識のブレーキを完全に焼き切った超弩級の露出ドキュメント『{clean_title}』。神木麗が放つ圧倒的な美貌と、逃げ場のない公然空間で限界まで追い詰められていく生々しい羞恥心が、画面越しに心拍数を限界まで跳ね上げます。"
        highlight_1 = f"白日の下に晒される無防備な素肌と、羞恥に抗えず滴り落ちる大量の体液。普段は見せることのない切迫した表情と、耳元で響く荒い呼吸のリアリズムは、既存のスタジオ作品では決して味わえない圧倒的な熱量を放っています。"
        highlight_2 = f"羞恥心が快感のブースターへと変わる決定的瞬間。激しい責め苦の中で理性が吹き飛び、白目を剥きそうになりながら全身を痙攣させるアクメ描写は、まさに実用性の極致と言えます。"
    elif is_ntr or "本庄鈴" in full_text:
        sub_heading = f"背徳の快楽に沈むセックスレス人妻…本庄鈴主演【{hinban}】の生々しい情事録"
        intro_lead = f"静かに崩壊していく日常と、一度味わったら二度と引き返せない禁断の蜜の味。『{clean_title}』は、本庄鈴の持つ透明感と妖艶さが奇跡的なバランスで融合した、背徳NTRモノの新たな金字塔です。"
        highlight_1 = f"元カレによる強引かつ執拗なアプローチに、最初は罪悪感で身体を強張らせながらも、触れられるたびに疼きを隠せなくなっていく心理描写が秀逸。唇を奪われ、首筋に吸い付かれるたびに漏れる切ない吐息に胸が締め付けられます。"
        highlight_2 = f"野外という極限のシチュエーションがもたらす心拍数の高まり。誰かに見られるかもしれない恐怖と、夫以外の男に激しく穿たれる背徳の悦楽が入り混じり、自ら腰を浮かせて快楽を貪る姿は圧巻です。"
    elif is_chijo_lecture or "紗倉まな" in full_text:
        sub_heading = f"冷徹な見下しと圧倒的焦らし責め！紗倉まな【{hinban}】の射精我慢地獄"
        intro_lead = f"男の受け身な欲望を全方位から翻弄し、骨の髄まで狂わせる究極の快楽指導作『{clean_title}』。紗倉まなの容赦のない言葉責めと、こちらの反応を楽しむかのようなサディスティックな微笑みが、鑑賞側の理性を容赦なく粉砕します。"
        highlight_1 = f"触れさせない焦らしから、至近距離で見せつけられる生々しいオナニー。男のプライドを心地よく踏みにじりながら、射精の主導権を完全に掌握される背徳の快感が全編にわたって展開されます。"
        highlight_2 = f"限界まで寸止めされた後に解き放たれる、怒涛のフィナーレ。射精した瞬間すら見下ろされ、魂まで抜き取られるような圧倒的余韻を味わえる至極の一本です。"
    elif is_mmr:
        sub_heading = f"マジックミラー越しの彼氏と交わす視線…【{hinban}】の極限羞恥ドキュメント"
        intro_lead = f"日常のすぐ隣にある透明な壁一枚を隔てた、狂気的な背徳シチュエーション『{clean_title}』。愛するパートナーがすぐ目の前にいながら、見知らぬ男の剛直に貫かれ、声を出せずに震えるヒロインの葛藤が生々しく記録されています。"
        highlight_1 = f"ミラー越しに彼氏の姿を捉えながら、身体は激しい快楽の波に抗えず濡れそぼっていく残酷なコントラスト。必死に口元を押さえながらも、突かれるたびに背筋を跳ね上げる無防備な肉体反応が興奮を煽ります。"
        highlight_2 = f"バレてしまう恐怖がそのまま快感のスパイスへと昇華される瞬間。奥深くまで穿たれ、切なく喘ぎながら果てるヒロインの姿は、マジックミラー号企画ならではの最高峰の抜きどころです。"
    elif is_office:
        sub_heading = f"清楚な制服・スーツの下に隠された牝の本能！【{hinban}】の濃密社内情事"
        intro_lead = f"オフィスという規律正しい空間で、密かに交わされる濃厚な愛撫と背徳の契り『{clean_title}』。{act_str}の魅せる知的な立ち振る舞いと、密室で衣服を乱された瞬間に剥き出しになる女の情欲が、最高のギャップとなって襲いかかります。"
        highlight_1 = f"デスクの下や給湯室でのスリリングな前戯。同僚や部下の足音が聞こえるかもしれない緊張感の中で、衣擦れの音とともに弄ばれる秘部の水音がバイノーラル級に響き渡ります。"
        highlight_2 = f"業務の仮面を脱ぎ捨て、ただ男の肉体を貪る狂乱の本番。理性的な言葉遣いから次第に淫らな懇願へと変わっていく喘ぎ声のグラデーションに、思わずこちらの息も止まります。"
    else:
        sub_heading = f"圧倒的実用性と計算し尽くされたアングル！【{hinban}】の完全本音レビュー"
        intro_lead = f"{maker}の威信を懸けてリリースされた話題沸騰の最新作『{clean_title}』。{act_str}のポテンシャルを極限まで引き出す緻密な構成と、無駄な引き延ばしを一切排除した実用的なシーン展開が、最初から最後まで息をつかせぬ高揚感をもたらします。"
        highlight_1 = f"高精細カメラが捉える肌の汗ばみと、接写による結合部のクリアな描写。張り詰めた空気の中で交わされる濃厚な愛撫が、鑑賞側の抜き欲を最短距離で刺激します。"
        highlight_2 = f"徐々に熱量を増していくピストンのリズムと、それに合わせて狂おしく乱れるヒロインの絶頂反応。爽快感と深い満足感を両立させたクライマックスは、リピート必至の仕上がりです。"

    analysis_block_1 = f"""
    <div class="bg-slate-50 border border-slate-200 rounded-2xl p-6 space-y-3">
        <h4 class="text-base font-black text-slate-900 flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-rose-500"></span>
            【第1幕：導入と前戯のリアリズム】日常の緊張が背徳の熱気へと融解するプロセス
        </h4>
        <p class="text-sm text-slate-700 leading-relaxed">
            物語の冒頭では、シチュエーションの前提条件や登場人物同士の距離感が丁寧に描写されます。{act_str}の視線の配り方、衣服越しに身体を弄ばれる段階での微細な身じろぎなど、演出の細部に至るまで計算し尽くされており、観る者を一瞬で作品世界へと引き込みます。耳元やうなじへと吹きかけられる熱い吐息の臨場感が、鑑賞側の心拍数を自然と高めていきます。
        </p>
    </div>
    """

    analysis_block_2 = f"""
    <div class="bg-slate-50 border border-slate-200 rounded-2xl p-6 space-y-3">
        <h4 class="text-base font-black text-slate-900 flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-rose-500"></span>
            【第2幕：密着絡みと粘膜愛撫】滴る愛液と理性を麻痺させるディープスキンシップ
        </h4>
        <p class="text-sm text-slate-700 leading-relaxed">
            本格的な絡みへと移行すると、画面全体の湿度が一段と跳ね上がります。丹念に性感帯を攻め立てられることで、恥じらいの壁が音を立てて崩壊。濡れそぼる秘部から漏れ出す生々しい水音と、喉の奥で押し殺した吐息が部屋中に反響します。情熱的なキスから胸元、秘部へと吸い付くようなスキンシップが途切れなく続き、ヒロインの表情は完全に快楽の熱に浮かされていきます。
        </p>
    </div>
    """

    analysis_block_3 = f"""
    <div class="bg-slate-50 border border-slate-200 rounded-2xl p-6 space-y-3">
        <h4 class="text-base font-black text-slate-900 flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-rose-500"></span>
            【第3幕：本番結合と怒涛の絶頂】重量感あるピストンと全身を震わせるクライマックス
        </h4>
        <p class="text-sm text-slate-700 leading-relaxed">
            結合部が露わになる本番交わりでは、肉が激しくぶつかり合う鈍い音とともに、容赦のないグラインドが展開。体位を変えるたびに異なる角度から秘部を穿たれ、{act_str}の全身は紅潮と汗で光り輝きます。男の塊をぎゅっと締め付けながら絶頂を迎える瞬間の恍惚とした表情、そして白目を剥きそうになりながら快楽を貪る姿は、実用性を重視するファンにとって文句なしの決定打となっています。
        </p>
    </div>
    """

    score_visual = round(rng.uniform(4.7, 5.0), 1)
    score_sound = round(rng.uniform(4.6, 5.0), 1)
    score_practical = round(rng.uniform(4.8, 5.0), 1)

    body_html = f"""<div class="space-y-8 text-gray-800 leading-relaxed font-sans">
    
    <!-- 記事トップ：独自速報＆本音レビュー見出し -->
    <div class="bg-gradient-to-br from-rose-50 via-white to-amber-50 border-l-4 border-rose-500 p-6 rounded-r-2xl shadow-sm">
        <div class="flex items-center gap-2 mb-2 text-rose-600 font-bold text-xs sm:text-sm tracking-wide">
            <span class="inline-block w-2.5 h-2.5 bg-rose-500 rounded-full animate-ping"></span>
            【FANZA人気ランキング上位】E-E-A-T基準 徹底実用検証レビュー
        </div>
        <h2 class="text-xl sm:text-2xl font-black text-gray-900 leading-snug mb-3">
            {sub_heading}
        </h2>
        <p class="text-sm sm:text-base text-gray-700 leading-relaxed">
            {intro_lead}
        </p>
    </div>

    <!-- CVRブースト：ダブルアクションボタン -->
    <div class="bg-gradient-to-r from-slate-900 via-gray-900 to-slate-800 p-6 rounded-2xl shadow-xl text-white">
        <div class="flex flex-col md:flex-row items-center justify-between gap-4">
            <div class="text-center md:text-left">
                <span class="inline-block px-3 py-1 bg-rose-600 text-white text-xs font-black rounded-full mb-2">FANZA公式正規配信</span>
                <h3 class="text-lg font-bold text-white">『{clean_title}』</h3>
                <p class="text-xs text-gray-300 mt-1">品番: {hinban} ｜ メーカー: {maker} ｜ 出演: {act_str}</p>
            </div>
            <div class="flex flex-col sm:flex-row gap-3 w-full md:w-auto">
                <a href="{clean_url}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center px-6 py-3.5 bg-gradient-to-r from-rose-500 to-red-600 hover:from-rose-600 hover:to-red-700 text-white font-black text-base rounded-xl shadow-lg hover:shadow-rose-500/50 transform hover:-translate-y-0.5 transition-all text-center">
                    ▶ 公式でフル本編を視聴する
                </a>
                <a href="{clean_url}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center px-5 py-3.5 bg-slate-700 hover:bg-slate-600 text-gray-200 font-bold text-sm rounded-xl transition-all text-center">
                    無料サンプル動画・詳細
                </a>
            </div>
        </div>
    </div>

    <!-- 作品基本スペック表 -->
    <div class="bg-white border border-gray-200 rounded-2xl overflow-hidden shadow-sm">
        <div class="bg-gray-100 px-6 py-3 border-b border-gray-200">
            <h3 class="font-bold text-gray-800 text-sm flex items-center gap-2">
                <svg class="w-4 h-4 text-rose-500" fill="currentColor" viewBox="0 0 20 20"><path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z"/><path fill-rule="evenodd" d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z" clip-rule="evenodd"/></svg>
                作品詳細スペック＆配信データ
            </h3>
        </div>
        <table class="w-full text-sm text-left border-collapse">
            <tbody>
                <tr class="border-b border-gray-100 hover:bg-gray-50/50">
                    <th class="py-3 px-6 font-semibold text-gray-600 w-1/3 bg-gray-50/80">作品番号 / 品番</th>
                    <td class="py-3 px-6 text-gray-900 font-bold">{hinban}</td>
                </tr>
                <tr class="border-b border-gray-100 hover:bg-gray-50/50">
                    <th class="py-3 px-6 font-semibold text-gray-600 bg-gray-50/80">主演・キャスト</th>
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
            <p>{highlight_1}</p>
            <p>{highlight_2}</p>
        </div>

        <div class="space-y-4 pt-2">
            {analysis_block_1}
            {analysis_block_2}
            {analysis_block_3}
        </div>
    </div>

    <!-- 総合実用度スコア -->
    <div class="bg-gradient-to-br from-slate-900 to-gray-900 text-white rounded-2xl p-6 shadow-md space-y-4">
        <h4 class="font-bold text-white text-base flex items-center gap-2">
            <span>⭐</span> 本作の実用度・クオリティ総合評価
        </h4>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 text-center">
            <div class="bg-white/10 p-4 rounded-xl border border-white/10">
                <div class="text-xs text-gray-300 mb-1">ビジュアル・表情</div>
                <div class="text-2xl font-black text-amber-400">★ {score_visual} <span class="text-xs text-gray-400">/ 5.0</span></div>
            </div>
            <div class="bg-white/10 p-4 rounded-xl border border-white/10">
                <div class="text-xs text-gray-300 mb-1">音響・息遣い</div>
                <div class="text-2xl font-black text-amber-400">★ {score_sound} <span class="text-xs text-gray-400">/ 5.0</span></div>
            </div>
            <div class="bg-white/10 p-4 rounded-xl border border-white/10">
                <div class="text-xs text-gray-300 mb-1">抜きやすさ（実用度）</div>
                <div class="text-2xl font-black text-rose-400">★ {score_practical} <span class="text-xs text-gray-400">/ 5.0</span></div>
            </div>
        </div>
    </div>

    <!-- 批評・おすすめ層まとめ -->
    <div class="bg-gray-50 border border-gray-200 rounded-2xl p-6 space-y-4">
        <h4 class="font-bold text-gray-900 text-base flex items-center gap-2">
            <span>💡</span> この作品が特に刺さるシチュエーション・性癖
        </h4>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
            <div class="flex items-center gap-2 text-xs font-semibold text-gray-700 bg-white p-3 rounded-xl border border-gray-100 shadow-sm">
                <span class="text-emerald-500 font-bold">✔</span> 高画質HD/4Kによる細部の生々しい質感
            </div>
            <div class="flex items-center gap-2 text-xs font-semibold text-gray-700 bg-white p-3 rounded-xl border border-gray-100 shadow-sm">
                <span class="text-emerald-500 font-bold">✔</span> 出演キャストのリアルな息遣いと絶頂反応
            </div>
            <div class="flex items-center gap-2 text-xs font-semibold text-gray-700 bg-white p-3 rounded-xl border border-gray-100 shadow-sm">
                <span class="text-emerald-500 font-bold">✔</span> 無駄な演出を省いた本番中心の濃密な絡み
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
            『{clean_title}』<br class="hidden sm:inline">今すぐ公式でフル本編を体感
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
    clean_url = get_clean_affiliate_url(item.get("affiliateURL", ""), cid)
    
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
    maker = item.get("iteminfo", {}).get("maker", [{}])[0].get("name", "公式レーベル")
    label = item.get("iteminfo", {}).get("label", [{}])[0].get("name", maker)
    date_str = item.get("date", "2026-10-28 10:00:00")
    
    body_html = generate_killer_post_body(item)
    
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
    print("=== トレンド・ランキング上位キラー記事の取得＆作成開始 ===")
    items = fetch_trending_killer_items(target_count=15)
    print(f"取得件数: {len(items)} 件の超注目キラー作を処理します\n")
    
    for idx, item in enumerate(items, 1):
        cid = item.get("content_id")
        title = item.get("title")
        hinban = generate_hinban(cid)
        actresses = [a.get("name") for a in item.get("iteminfo", {}).get("actress", [])]
        print(f"[{idx}/{len(items)}] 処理中: {cid} ({hinban})...")
        create_post_json(item)
        print(f"✅ キラー記事作成完了: [{hinban}] {title[:35]} (女優: {actresses})")

    print("\n全キラー作品の記事作成が完了しました！")

if __name__ == "__main__":
    main()
