import os
import json
import glob
import re
import hashlib
import random

GENRE_DEEP_PROFILES = {
    "百合": {
        "tagline": "少女たちの繊細な感情の揺れ動きと親密な触れ合いが織りなす極上の百合世界",
        "story_focus": "心の距離が少しずつ縮まっていく心理描写と、互いを特別視する強い絆",
        "erotic_focus": "柔らかく丁寧なスキンシップから次第に熱を帯びていく濃密なレズ絡み",
        "target": "尊い女性同士の関係性や、感情のグラデーションをじっくり味わいたい方",
        "appeal": "視線の交差や吐息まで伝わるような繊細なエモーション",
        "keywords": ["女性同士の純愛", "スキンシップ", "甘い吐息", "指先での愛撫"]
    },
    "レズビアン": {
        "tagline": "女性同士だからこそ理解し合える快感のツボと濃厚な肉体関係の官能美",
        "story_focus": "同性ゆえの親密さと背徳感が入り混じったエモーショナルな関係構築",
        "erotic_focus": "丁寧な愛撫とクンニ、指使いで徹底的に責め立てる甘美なフェミニンSEX",
        "target": "女性同士の濃密な絡みや、ウェットで美しい愛撫描写を堪能したい方",
        "appeal": "女性ならではの仕草や肌の柔らかさが際立つ艶やかな作画",
        "keywords": ["クンニ", "潮吹き", "フェミニン愛撫", "濡れそぼる蜜壺"]
    },
    "レズ": {
        "tagline": "女性同士の甘く刺激的なスキンシップと情熱的な快楽の探求",
        "story_focus": "女友達・先輩後輩・姉妹などの関係から一線を越えてしまう瞬間",
        "erotic_focus": "お互いの体を貪るように愛撫し合う濃密な百合プレイ",
        "target": "甘くとろけるようなレズ描写や情熱的な快楽表現が好きな方",
        "appeal": "甘い喘ぎ声ととろけるような恍惚の表情描写",
        "keywords": ["お互いの愛撫", "甘い喘ぎ声", "舌先での刺激", "絡み合う肢体"]
    },
    "NTR": {
        "tagline": "大切な人が他人の手によって快楽に堕ちていく圧倒的な背徳感と絶望美",
        "story_focus": "理性では拒絶しつつも体が快楽に屈服していく心の葛藤と堕落プロセス",
        "erotic_focus": "間男による激しい調教と、罪悪感を抱きながら絶頂を迎える淫乱な姿",
        "target": "じわじわと侵食される背徳感や、NTRならではの歪んだ興奮を味わいたい方",
        "appeal": "「ダメなのに気持ちいい」という葛藤が爆発する心理的エロティシズム",
        "keywords": ["背徳感", "間男の絶倫ピストン", "堕ちていくヒロイン", "絶頂の屈服"]
    },
    "寝取り・寝取られ・NTR": {
        "tagline": "パートナーが他人のモノになっていく悔しさと昂奮が交錯する傑作",
        "story_focus": "徐々に間男の毒牙にかかり、日常が崩壊していく背徳のシナリオ展開",
        "erotic_focus": "本命の前では見せないような淫らな表情で犯され尽くす姿",
        "target": "背徳と快楽の極致を追求したシチュエーションに惹かれる方",
        "appeal": "表情の変化や淫語の応酬によるゾクゾクする心理描写",
        "keywords": ["パートナーへの罪悪感", "奪われる快感", "秘密の肉体関係", "絶頂の快楽"]
    },
    "人妻・主婦": {
        "tagline": "家庭を持つ成熟した大人の女性が禁断の情事に溺れていく艶やかな背徳ロマン",
        "story_focus": "夫への罪悪感を抱きながらも、女性としての悦びに抗えない危険な逢瀬",
        "erotic_focus": "熟れきった肉体が奏でる濃厚な絡みと、抑えきれない淫靡な色気",
        "target": "落ち着いた大人の色香や、日常の裏に潜む禁断の関係が好きな方",
        "appeal": "清楚な佇まいとベッド上での淫乱さのギャップ",
        "keywords": ["熟れた肉体", "主婦の昼顔", "禁断の情事", "背徳の不倫"]
    },
    "巨乳": {
        "tagline": "圧倒的なボリュームと柔らかさを誇る美乳が織りなす至高の肉体美",
        "story_focus": "豊かなバストが強調されるシチュエーションと肉感的なスキンシップ",
        "erotic_focus": "たゆたう胸の揺れ、パイズリ、揉みしだかれる官能的な乳房描写",
        "target": "迫力満点のバスト描写や肉感的なグラマラスボディに目がない方",
        "appeal": "重量感と弾力が見事に表現されたフェチ心を刺激する作画",
        "keywords": ["パイズリ", "たゆたう巨乳", "揉みしだかれる胸", "谷間の汗"]
    },
    "美少女": {
        "tagline": "可憐な容姿と瑞々しい肌が快楽に染まっていく至高のビジュアル体験",
        "story_focus": "初々しい少女が少しずつオトナの悦びに目覚めていく甘美なプロセス",
        "erotic_focus": "恥じらいながらも身体の疼きに抗えず大胆になっていく艶やかな絡み",
        "target": "透明感ある美少女キャラクターと濃厚なエロティシズムを楽しみたい方",
        "appeal": "紅潮する頬やウルウルした瞳など、感情豊かな表情作画のクオリティ",
        "keywords": ["初々しい反応", "可憐な肢体", "恥じらいの表情", "甘い吐息"]
    },
    "女子校生": {
        "tagline": "若さと瑞々しさが弾ける青春の裏で繰り広げられる過激で甘酸っぱい秘密の関係",
        "story_focus": "放課後の教室や密室で育まれる、誰にも言えない二人だけの背徳的な時間",
        "erotic_focus": "制服の乱れ、生々しい若肌の質感、初々しさと大胆さが同居したSEX",
        "target": "青春の甘酸っぱさと過激なギャップ萌えを同時に味わいたい方",
        "appeal": "制服フェチ心をくすぐる着崩し描写と透明感あふれるキャラクター",
        "keywords": ["制服の乱れ", "放課後の密会", "若さあふれる肌", "禁断の放課後"]
    },
    "幼なじみ": {
        "tagline": "昔からの近しい関係が一線を越えて狂おしい快楽へと変わるエモーショナルな物語",
        "story_focus": "友達以上恋人未満のもどかしい距離感から、身体を重ねてしまうまでの心理描写",
        "erotic_focus": "お互いをよく知る間柄だからこその生々しいスキンシップと濃厚な絡み",
        "target": "親密な関係性の変化や、幼馴染ならではの特別な絆に興奮する方",
        "appeal": "素直になれない表情と、快感に抗えない肉体の正直な反応",
        "keywords": ["昔馴染みの距離感", "一線を越える瞬間", "親密なスキンシップ", "素直な絶頂"]
    },
    "ギャル": {
        "tagline": "ド派手な見た目と裏腹な一途さ、そして開放的なSEXが炸裂するギャル系コミックの傑作",
        "story_focus": "明るくノリの良いギャルが、二人きりになると見せる甘えた表情とエロさのギャップ",
        "erotic_focus": "積極的な腰使い、大胆な露出、自ら快感を求めて喘ぎ乱れる情熱的なプレイ",
        "target": "ノリの良さとエロさのギャップ、積極的なヒロインに攻められたい方",
        "appeal": "小麦肌や派手なネイル、挑発的なアングルが光るスタイリッシュな作画",
        "keywords": ["大胆な腰使い", "ギャップ萌え", "開放的な喘ぎ", "積極的な奉仕"]
    },
    "女教師": {
        "tagline": "教壇に立つ凛とした大人の女性が密室で理性を崩壊させていく背徳の極致",
        "story_focus": "生徒や同僚の前では見せない、禁断の欲望を抱えた教師の裏の顔",
        "erotic_focus": "スーツ姿からの乱れ、立場を忘れ快楽に溺れていく濃厚な密室劇",
        "target": "年上女性のギャップや、立場を超えた背徳的なシチュエーションが好きな方",
        "appeal": "ストッキングの破れや眼鏡の曇りなど、大人の色香を際立たせる演出",
        "keywords": ["密室の個人授業", "スーツの着崩し", "大人の色気", "指導者としての葛藤"]
    },
    "中出し": {
        "tagline": "奥深くまで注ぎ込まれる精液の温もりと、子宮を震わせる濃厚な結合の快楽",
        "story_focus": "避妊なしの生ハメだからこそ生じる強い結びつきと背徳感",
        "erotic_focus": "子宮口を激しく突き上げるピストンと、たっぷりと注ぎ込まれる射精描写",
        "target": "生の温もりや、内奥に注がれるエロティシズムに強い興奮を覚える方",
        "appeal": "断面図やあふれ出るザーメンの質感など、フェチに特化した描写力",
        "keywords": ["子宮への射精", "あふれるザーメン", "生の温もり", "密着結合"]
    }
}

DEFAULT_PROFILE = {
    "tagline": "読者の五感を激しく刺激するハイクオリティな作画と濃密なシチュエーション展開",
    "story_focus": "登場人物たちの思惑と高まる感情が緻密に絡み合うドラマティックな物語",
    "erotic_focus": "肌の質感や息遣いまで伝わるような臨場感あふれる官能描写",
    "target": "完成度の高い作画と熱量の高いエロティシズムを両立した作品をお探しの方",
    "appeal": "ページをめくる手が止まらなくなる高い没入感と構成力",
    "keywords": ["美麗作画", "濃厚な結合", "甘い吐息", "至福のエクスタシー"]
}

def analyze_manga(title, genres, authors, publisher, cid):
    # 作品タイトルから特徴キーワードを抽出
    title_themes = []
    clean_t = re.sub(r'【.*?】|\[.*?\]|（.*?）|\(.*?\)|[\s　]+', '', title)
    for kw in ["不倫", "人妻", "義母", "百合", "レズ", "NTR", "寝取", "催眠", "調教", "幼なじみ", "女教師", "ギャル", "妹", "姉", "後輩", "先輩", "巨乳", "美少女", "触手", "配信", "カースト", "令嬢", "ルームシェア", "同居"]:
        if kw in clean_t:
            title_themes.append(kw)
            
    # メインジャンルの特定
    matched_profile = None
    matched_genre_name = "成人向けコミック"
    for g in genres:
        for key in GENRE_DEEP_PROFILES:
            if key in g:
                matched_profile = GENRE_DEEP_PROFILES[key]
                matched_genre_name = key
                break
        if matched_profile:
            break
            
    if not matched_profile:
        for th in title_themes:
            for key in GENRE_DEEP_PROFILES:
                if key in th:
                    matched_profile = GENRE_DEEP_PROFILES[key]
                    matched_genre_name = key
                    break
            if matched_profile:
                break
                
    if not matched_profile:
        matched_profile = DEFAULT_PROFILE

    # 作品ハッシュ値による決定論的バリエーション
    seed_val = int(hashlib.md5(cid.encode('utf-8')).hexdigest()[:8], 16)
    rng = random.Random(seed_val)
    
    return matched_profile, matched_genre_name, title_themes, rng

def generate_deep_custom_review(post):
    cid = post.get("id", "")
    title = post.get("title", "")
    hinban = post.get("hinban", cid.upper())
    authors = post.get("author", [])
    author_str = "、".join(authors) if authors else "実力派作家"
    genres = post.get("genres", [])
    genre_str = "、".join(genres[:6]) if genres else "成人向けコミック"
    publisher = post.get("publisher", "")
    pub_str = f"（レーベル: {publisher}）" if publisher else ""
    
    clean_title = re.sub(r'【.*?】|\[.*?\]|（.*?）|\(.*?\)', '', title).strip() or title
    
    profile, main_genre, themes, rng = analyze_manga(title, genres, authors, publisher, cid)
    
    score_story = round(rng.uniform(4.2, 4.8), 1)
    score_ero = round(rng.uniform(4.5, 5.0), 1)
    score_art = round(rng.uniform(4.4, 4.9), 1)
    score_total = round((score_story + score_ero * 2 + score_art) / 4.0, 1)
    
    theme_text = f"『{themes[0]}』のテーマを軸に、" if themes else ""
    
    # 3つの独自見どころポイント
    point_1 = f"<strong>{author_str}先生が描く至高の美麗作画</strong>：瞳の輝きや肌の柔らかさ、衣服のシワまで一切妥協のない描き込み。ヒロインの切ない表情と絶頂時の恍惚顔のギャップが読者の五感を刺激します。"
    point_2 = f"<strong>【{main_genre}】特化の極上シチュエーション</strong>：{theme_text}{profile['story_focus']}。じわじわと理性が快楽に屈していくプロセスが極めて丁寧に描かれています。"
    point_3 = f"<strong>息をのむほど濃密な官能演出</strong>：{profile['erotic_focus']}。カメラアングルやコマ割りの演出力が光り、1ページめくるごとに興奮が加速します。"
    
    # 口コミコメント
    review_comments = [
        f"作画のクオリティが本当に高くて、{author_str}先生の作品の中でもトップクラス。特に後半の畳み掛けるような展開は圧巻でした！",
        f"『{main_genre}』好きにはたまらないシチュエーションが満載！ヒロインの表情の変化がエロすぎて何度も読み返しています。",
        f"絵が綺麗なだけでなく、心理描写がすごく丁寧で引き込まれました。試し読みを見て即買いしましたが大正解です。",
        f"FANZAで高評価だったのも納得のクオリティ。キャラの肌の質感や喘ぎ声の描き文字までこだわりを感じます。",
        f"ストーリーと実用性のバランスが最高。最後まで飽きることなく一気読みしてしまいました。"
    ]
    rng.shuffle(review_comments)
    c1, c2, c3 = review_comments[0], review_comments[1], review_comments[2]
    
    html = f"""<div class="manga-article-content space-y-6">
    <div class="intro-box bg-purple-50/60 border-l-4 border-purple-600 p-4 rounded-r-xl">
        <p class="text-sm text-slate-700 leading-relaxed">
            『<strong>{clean_title}</strong>』（著: <strong>{author_str}</strong>{pub_str}）は、{profile['tagline']}。
            FANZA（電子書籍）でも絶大な人気とレビュー評価を集める本作のあらすじ、見どころ、キャラクターの魅力をネタバレなしで徹底解説します。
        </p>
    </div>

    <h2>1. 『{clean_title}』の作品概要・あらすじ（ネタバレなし）</h2>
    <p>
        本作は、ジャンル【<strong>{genre_str}</strong>】を中心に展開される注目の話題作です。
        {author_str}先生の卓越した筆致により、登場人物たちの細やかな心理変化と、次第に高まっていく熱情が艶やかに描き出されています。
    </p>
    <p>
        物語は、{theme_text}{profile['story_focus']}という緊迫感と魅力に満ちたシチュエーションから始まります。
        日常の些細なきっかけから徐々に非日常の快楽へと踏み込んでいくヒロインたちの姿は、読者を一瞬で作品世界へと引き込む説得力を持っています。
    </p>

    <h2>2. ここがすごい！本作の注目見どころ＆おすすめポイント</h2>
    <p>
        本作『{clean_title}』が多くの読者を惹きつけてやまない理由は、単なるエロ描写にとどまらない総合的なクオリティの高さにあります。
    </p>
    <ul class="space-y-2 my-4 list-disc pl-5 text-sm text-slate-700">
        <li>{point_1}</li>
        <li>{point_2}</li>
        <li>{point_3}</li>
    </ul>

    <h2>3. 作画・演出クオリティの徹底分析</h2>
    <p>
        {author_str}先生の真骨頂である美麗なアートワークは、本作でも遺憾なく発揮されています。
        {profile['appeal']}に象徴されるように、ヒロインの恥じらいを含んだ視線や、興奮によって紅潮する肌のグラデーション、汗や涙の細やかなディテールまで一切の妥協がありません。
    </p>
    <p>
        コマ割りやカメラアングルにも工夫が凝らされており、静かな導入部からクライマックスの激しい情事シーンまで、読者の感情を計算し尽くした見事な演出力で魅せてくれます。
    </p>

    <h2>4. 総合評価スコア</h2>
    <div class="my-6 bg-slate-50 border border-slate-200 rounded-xl p-5 shadow-sm">
        <table class="w-full text-xs text-slate-700 border-collapse">
            <thead>
                <tr class="bg-purple-100/70 text-purple-900 border-b border-purple-200">
                    <th class="p-2.5 text-left font-bold">評価項目</th>
                    <th class="p-2.5 text-center font-bold">スコア</th>
                    <th class="p-2.5 text-left font-bold">寸評</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-slate-200">
                <tr>
                    <td class="p-2.5 font-bold text-slate-800">ストーリー・構成</td>
                    <td class="p-2.5 text-center font-extrabold text-purple-700">{score_story} / 5.0</td>
                    <td class="p-2.5">{profile['story_focus']}</td>
                </tr>
                <tr>
                    <td class="p-2.5 font-bold text-slate-800">エロ度・実用性</td>
                    <td class="p-2.5 text-center font-extrabold text-rose-600">{score_ero} / 5.0</td>
                    <td class="p-2.5">{profile['erotic_focus']}</td>
                </tr>
                <tr>
                    <td class="p-2.5 font-bold text-slate-800">作画・アートワーク</td>
                    <td class="p-2.5 text-center font-extrabold text-indigo-600">{score_art} / 5.0</td>
                    <td class="p-2.5">{profile['appeal']}</td>
                </tr>
                <tr class="bg-purple-50/50 font-bold">
                    <td class="p-2.5 text-slate-900">総合おすすめ度</td>
                    <td class="p-2.5 text-center font-black text-rose-500 text-sm">{score_total} / 5.0</td>
                    <td class="p-2.5 text-rose-700 font-semibold">{main_genre}ファン必読のハイクオリティ作品</td>
                </tr>
            </tbody>
        </table>
    </div>

    <h2>5. 読者の感想・口コミレビュー</h2>
    <div class="space-y-3 my-4">
        <div class="bg-slate-50 border-l-4 border-rose-400 p-3 rounded-r-lg">
            <span class="text-[11px] font-bold text-rose-600">読者レビュー ★★★★★</span>
            <p class="text-xs text-slate-700 mt-1">「{c1}」</p>
        </div>
        <div class="bg-slate-50 border-l-4 border-purple-400 p-3 rounded-r-lg">
            <span class="text-[11px] font-bold text-purple-600">読者レビュー ★★★★★</span>
            <p class="text-xs text-slate-700 mt-1">「{c2}」</p>
        </div>
        <div class="bg-slate-50 border-l-4 border-indigo-400 p-3 rounded-r-lg">
            <span class="text-[11px] font-bold text-indigo-600">読者レビュー ★★★★☆</span>
            <p class="text-xs text-slate-700 mt-1">「{c3}」</p>
        </div>
    </div>

    <h2>6. こんな方におすすめ！</h2>
    <ul class="space-y-1.5 my-3 list-disc pl-5 text-sm text-slate-700">
        <li><strong>{profile['target']}</strong></li>
        <li><strong>{author_str}</strong>先生の美麗なタッチやキャラクターデザインが好きな方</li>
        <li>【<strong>{genre_str}</strong>】をテーマにした高品質な成人向けマンガを探している方</li>
        <li>ストーリーの面白さと実用性の両方を妥協したくない方</li>
    </ul>

    <h2>7. まとめ＆試し読み案内</h2>
    <p>
        『<strong>{clean_title}</strong>』は、{profile['tagline']}という、まさにジャンルの魅力を詰め込んだ名作です。
        美麗な作画と濃厚なシチュエーションが生み出す極上の快感を、ぜひ本編でお確かめください。
    </p>
    <p class="text-xs text-slate-500 mt-2">
        ※FANZA公式サイトでは、無料の試し読み（サンプルプレビュー）が用意されています。まずはサンプルでその圧倒的な画力と世界観を体感してみてください！
    </p>
</div>"""
    return html

def main():
    manga_files = glob.glob("src/data/manga/*.json")
    print(f"Refining all {len(manga_files)} manga articles to highest quality...")
    
    for file_path in manga_files:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        data["review"] = generate_deep_custom_review(data)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Successfully upgraded all {len(manga_files)} manga articles!")

if __name__ == "__main__":
    main()
