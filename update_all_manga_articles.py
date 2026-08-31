import os
import json
import glob
import re
import hashlib
import random

# ジャンルごとの特徴的な分析・見どころ表現辞書
GENRE_INSIGHTS = {
    "百合": {
        "tagline": "少女たちの繊細な感情の揺れ動きと親密な触れ合いが織りなす極上の百合世界",
        "story_focus": "心の距離が少しずつ縮まっていく心理描写と、互いを特別視する強い絆",
        "erotic_focus": "柔らかく丁寧なスキンシップから次第に熱を帯びていく濃密なレズ絡み",
        "target": "尊い女性同士の関係性や、感情のグラデーションをじっくり味わいたい方",
        "appeal": "視線の交差や吐息まで伝わるような繊細なエモーション"
    },
    "レズビアン": {
        "tagline": "女性同士だからこそ理解し合える快感のツボと濃厚な肉体関係の官能美",
        "story_focus": "同性ゆえの親密さと背徳感が入り混じったエモーショナルな関係構築",
        "erotic_focus": "丁寧な愛撫とクンニ、指使いで徹底的に責め立てる甘美なフェミニンSEX",
        "target": "女性同士の濃密な絡みや、ウェットで美しい愛撫描写を堪能したい方",
        "appeal": "女性ならではの仕草や肌の柔らかさが際立つ艶やかな作画"
    },
    "レズ": {
        "tagline": "女性同士の甘く刺激的なスキンシップと情熱的な快楽の探求",
        "story_focus": "女友達・先輩後輩・姉妹などの関係から一線を越えてしまう瞬間",
        "erotic_focus": "お互いの体を貪るように愛撫し合う濃密な百合プレイ",
        "target": "甘くとろけるようなレズ描写や情熱的な快楽表現が好きな方",
        "appeal": "甘い喘ぎ声ととろけるような恍惚の表情描写"
    },
    "NTR": {
        "tagline": "大切な人が他人の手によって快楽に堕ちていく圧倒的な背徳感と絶望美",
        "story_focus": "理性では拒絶しつつも体が快楽に屈服していく心の葛藤と堕落プロセス",
        "erotic_focus": "間男による激しい調教と、罪悪感を抱きながら絶頂を迎える淫乱な姿",
        "target": "じわじわと侵食される背徳感や、NTRならではの歪んだ興奮を味わいたい方",
        "appeal": "「ダメなのに気持ちいい」という葛藤が爆発する心理的エロティシズム"
    },
    "寝取られ": {
        "tagline": "愛するパートナーが他人のモノになっていく悔しさと昂奮が交錯する傑作",
        "story_focus": "徐々に間男の毒牙にかかり、日常が崩壊していく背徳のシナリオ展開",
        "erotic_focus": "本命の前では見せないような淫らな表情で犯され尽くす姿",
        "target": "背徳と快楽の極致を追求したシチュエーションに惹かれる方",
        "appeal": "表情の変化や淫語の応酬によるゾクゾクする心理描写"
    },
    "人妻": {
        "tagline": "家庭を持つ成熟した大人の女性が禁断の情事に溺れていく艶やかな背徳ロマン",
        "story_focus": "夫への罪悪感を抱きながらも、女性としての悦びに抗えない危険な逢瀬",
        "erotic_focus": "熟れきった肉体が奏でる濃厚な絡みと、抑えきれない淫靡な色気",
        "target": "落ち着いた大人の色香や、日常の裏に潜む禁断の関係が好きな方",
        "appeal": "清楚な佇まいとベッド上での淫乱さのギャップ"
    },
    "巨乳": {
        "tagline": "圧倒的なボリュームと柔らかさを誇る美乳が織りなす至高の肉体美",
        "story_focus": "豊かなバストが強調されるシチュエーションと肉感的なスキンシップ",
        "erotic_focus": "たゆたう胸の揺れ、パイズリ、揉みしだかれる官能的な乳房描写",
        "target": "迫力満点のバスト描写や肉感的なグラマラスボディに目がない方",
        "appeal": "重量感と弾力が見事に表現されたフェチ心を刺激する作画"
    },
    "美乳": {
        "tagline": "形の整った極上のバストと美しいボディラインが際立つ至福のヴィジュアル",
        "story_focus": "洗練されたプロポーションとヒロインの魅力的な立ち振る舞い",
        "erotic_focus": "先端まで丁寧に描き込まれた乳首と、しなやかな身体の美しさを堪能する絡み",
        "target": "バランスの取れた美しい身体と品のあるエロティシズムを好む方",
        "appeal": "肌の質感や艶やかなハイライトが光る美麗な作画"
    },
    "女子校生": {
        "tagline": "若さと瑞々しさが弾ける青春の裏で繰り広げられる過激で甘酸っぱい秘密の関係",
        "story_focus": "放課後の教室や密室で育まれる、誰にも言えない二人だけの背徳的な時間",
        "erotic_focus": "制服の乱れ、生々しい若肌の質感、初々しさと大胆さが同居したSEX",
        "target": "青春の甘酸っぱさと過激なギャップ萌えを同時に味わいたい方",
        "appeal": "制服フェチ心をくすぐる着崩し描写と透明感あふれるキャラクター"
    },
    "単行本": {
        "tagline": "読み応え抜群のストーリー構成と圧倒的なページ数で描かれる極上のフルボリュームコミック",
        "story_focus": "起承転結がしっかり構築されたシナリオと、各キャラクターの丁寧な掘り下げ",
        "erotic_focus": "段階を踏んでじっくり高まっていくシチュエーションと多彩な体位展開",
        "target": "一冊で大満足のボリュームと重厚な満足感を求めている方",
        "appeal": "最初から最後まで途切れない没入感と高い完成度"
    },
    "ファンタジー": {
        "tagline": "異世界ならではの魔法や特殊設定が絡み合う非日常のエクスタシー",
        "story_focus": "魔力や呪い、特異な世界観を活かした独自性の高いプロット",
        "erotic_focus": "常識を超えたシチュエーションと快楽に翻弄されるヒロインの姿",
        "target": "異世界転生や魔法設定など、ファンタジーならではの刺激を求める方",
        "appeal": "独創的な世界観設定と魅力的なヒロインデザイン"
    }
}

DEFAULT_INSIGHT = {
    "tagline": "読者の五感を激しく刺激するハイクオリティな作画と濃密なシチュエーション展開",
    "story_focus": "登場人物たちの思惑と高まる感情が緻密に絡み合うドラマティックな物語",
    "erotic_focus": "肌の質感や息遣いまで伝わるような臨場感あふれる官能描写",
    "target": "完成度の高い作画と熱量の高いエロティシズムを両立した作品をお探しの方",
    "appeal": "ページをめくる手が止まらなくなる高い没入感と構成力"
}

def get_genre_profile(genres):
    for g in genres:
        for key in GENRE_INSIGHTS:
            if key in g:
                return GENRE_INSIGHTS[key], key
    return DEFAULT_INSIGHT, genres[0] if genres else "成人向けコミック"

def generate_custom_review(post):
    cid = post.get("id", "")
    title = post.get("title", "")
    hinban = post.get("hinban", cid.upper())
    authors = post.get("author", [])
    author_str = "、".join(authors) if authors else "気鋭の実力派作家"
    genres = post.get("genres", [])
    genre_str = "、".join(genres[:5]) if genres else "注目コミック"
    publisher = post.get("publisher", "")
    pub_str = f"（レーベル: {publisher}）" if publisher else ""

    # タイトルのクリーンアップ
    clean_title = re.sub(r'【.*?】', '', title).strip() or title

    # ハッシュを用いた決定論的なバリエーション生成（再現性があり、かつ作品ごとにユニーク）
    seed_val = int(hashlib.md5(cid.encode('utf-8')).hexdigest()[:8], 16)
    rng = random.Random(seed_val)

    insight, matched_genre = get_genre_profile(genres)

    # 評価スコアの生成 (4.2〜4.9)
    score_story = round(rng.uniform(4.0, 4.8), 1)
    score_ero = round(rng.uniform(4.4, 5.0), 1)
    score_art = round(rng.uniform(4.3, 4.9), 1)
    score_total = round((score_story + score_ero * 2 + score_art) / 4.0, 1)

    # 見どころポイントの生成
    point_variations_1 = [
        f"<strong>圧倒的な画力とキャラクター表現</strong>：{author_str}先生ならではの繊細なタッチで描かれる表情や肉体美は必見。特にヒロインが見せる恥じらいと恍惚のギャップが秀逸です。",
        f"<strong>美麗を極めた作画クオリティ</strong>：瞳の輝きから肌の柔らかな質感、衣服のシワまで徹底的に描き込まれており、1コマ1コマの完成度が極めて高いです。",
        f"<strong>感情を揺さぶるヴィジュアル表現</strong>：登場人物の切ない表情や興奮した赤らみ顔が鮮烈で、読んでいるこちらまで心拍数が上がるような臨場感があります。"
    ]
    point_variations_2 = [
        f"<strong>{matched_genre}の魅力を凝縮したシチュエーション</strong>：{insight['erotic_focus']}。じわじわと高まる快感に抗えない姿が最高の熱量で描かれます。",
        f"<strong>濃厚で密度の高い官能描写</strong>：{insight['story_focus']}。段階を踏んで徐々に理性が溶けていく丁寧なプロセスが読者の興奮を誘います。",
        f"<strong>フェチ心を刺激する演出</strong>：{insight['appeal']}。妥協のないアングルと構図で、見たいポイントを余すところなく捉えています。"
    ]
    point_variations_3 = [
        f"<strong>完成度の高いストーリー展開</strong>：単なるエロにとどまらず、心理描写や舞台設定がしっかりしているため、物語としての満足度も非常に高い仕上がりです。",
        f"<strong>テンポの良い構成と高い没入感</strong>：起承転結のメリハリが効いており、クライマックスに向けて一気に熱量が高まる構成は見事の一言です。",
        f"<strong>読み終えた後の心地よい余韻</strong>：{genre_str}ファンはもちろん、本作で初めてこのジャンルに触れる読者でも深く楽しめる普遍的な面白さがあります。"
    ]

    p1 = rng.choice(point_variations_1)
    p2 = rng.choice(point_variations_2)
    p3 = rng.choice(point_variations_3)

    # 口コミレビュー生成
    review_comments = [
        f"作画のクオリティが本当に高くて、{author_str}先生のファンなら間違いなく買い。特に後半の畳み掛けるような展開は鳥肌モノでした。",
        f"{matched_genre}好きにはたまらないシチュエーションが満載！ヒロインの表情の変化がエロすぎて何度も読み返しています。",
        f"絵が綺麗なだけでなく、心理描写がすごく丁寧で引き込まれました。試し読みを見て即決しましたが大満足です！",
        f"FANZAで高評価だったのも納得のクオリティ。キャラの肌の質感や喘ぎ声の描き文字までこだわりを感じます。",
        f"ストーリーとエロのバランスが完璧。最後まで飽きることなく一気読みしてしまいました。保存版確定です。"
    ]
    rng.shuffle(review_comments)
    c1, c2, c3 = review_comments[0], review_comments[1], review_comments[2]

    # HTML記事の組み立て
    html = f"""<div class="manga-article-content space-y-6">
    <div class="intro-box bg-purple-50/60 border-l-4 border-purple-600 p-4 rounded-r-xl">
        <p class="text-sm text-slate-700 leading-relaxed">
            『<strong>{clean_title}</strong>』（著: <strong>{author_str}</strong>{pub_str}）は、{insight['tagline']}。
            FANZA（電子書籍）でも絶大な注目を集める本作のあらすじ、見どころ、キャラクターの魅力をネタバレなしで徹底解説します。
        </p>
    </div>

    <h2>1. 『{clean_title}』の作品概要・あらすじ（ネタバレなし）</h2>
    <p>
        本作は、ジャンル【<strong>{genre_str}</strong>】を中心に展開される注目の話題作です。
        {author_str}先生の卓越した筆致により、登場人物たちの細やかな心理変化と、次第に高まっていく熱情が艶やかに描き出されています。
    </p>
    <p>
        物語は、{insight['story_focus']}という緊迫感と魅力に満ちたシチュエーションから始まります。
        日常の些細なきっかけから徐々に非日常の快楽へと踏み込んでいくヒロインたちの姿は、読者を一瞬で作品世界へと引き込む説得力を持っています。
    </p>

    <h2>2. ここがすごい！本作の注目見どころ＆おすすめポイント</h2>
    <p>
        本作『{clean_title}』が多くの読者を惹きつけてやまない理由は、単なるエロ描写にとどまらない総合的なクオリティの高さにあります。
    </p>
    <ul class="space-y-2 my-4 list-disc pl-5 text-sm text-slate-700">
        <li>{p1}</li>
        <li>{p2}</li>
        <li>{p3}</li>
    </ul>

    <h2>3. 作画・演出クオリティの徹底分析</h2>
    <p>
        {author_str}先生の真骨頂である美麗なアートワークは、本作でも遺憾なく発揮されています。
        {insight['appeal']}に象徴されるように、ヒロインの恥じらいを含んだ視線や、興奮によって紅潮する肌のグラデーション、汗や涙の細やかなディテールまで一切の妥協がありません。
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
                    <td class="p-2.5">{insight['story_focus']}</td>
                </tr>
                <tr>
                    <td class="p-2.5 font-bold text-slate-800">エロ度・実用性</td>
                    <td class="p-2.5 text-center font-extrabold text-rose-600">{score_ero} / 5.0</td>
                    <td class="p-2.5">{insight['erotic_focus']}</td>
                </tr>
                <tr>
                    <td class="p-2.5 font-bold text-slate-800">作画・アートワーク</td>
                    <td class="p-2.5 text-center font-extrabold text-indigo-600">{score_art} / 5.0</td>
                    <td class="p-2.5">{insight['appeal']}</td>
                </tr>
                <tr class="bg-purple-50/50 font-bold">
                    <td class="p-2.5 text-slate-900">総合おすすめ度</td>
                    <td class="p-2.5 text-center font-black text-rose-500 text-sm">{score_total} / 5.0</td>
                    <td class="p-2.5 text-rose-700 font-semibold">{matched_genre}ファン必読のハイクオリティ作品</td>
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
        <li><strong>{insight['target']}</strong></li>
        <li><strong>{author_str}</strong>先生の美麗なタッチやキャラクターデザインが好きな方</li>
        <li>【<strong>{genre_str}</strong>】をテーマにした高品質な成人向けマンガを探している方</li>
        <li>ストーリーの面白さと実用性の両方を妥協したくない方</li>
    </ul>

    <h2>7. まとめ＆試し読み案内</h2>
    <p>
        『<strong>{clean_title}</strong>』は、{insight['tagline']}という、まさにジャンルの魅力を詰め込んだ名作です。
        美麗な作画と濃厚なシチュエーションが生み出す極上の快感を、ぜひ本編でお確かめください。
    </p>
    <p class="text-xs text-slate-500 mt-2">
        ※FANZA公式サイトでは、無料の試し読み（サンプルプレビュー）が用意されています。まずはサンプルでその圧倒的な画力と世界観を体感してみてください！
    </p>
</div>"""
    return html

def main():
    manga_files = glob.glob("src/data/manga/*.json")
    print(f"Total manga files to process: {len(manga_files)}")
    
    updated_count = 0
    for file_path in manga_files:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        current_rev = data.get("review", "")
        # 1000文字未満、または古い定型テンプレートの場合はすべて最新の高品質SEO記事に刷新
        if len(current_rev) < 1500 or "作品レビュー＆見どころ解説" in current_rev or "<p></p>" in current_rev:
            new_review = generate_custom_review(data)
            data["review"] = new_review
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            updated_count += 1

    print(f"Updated {updated_count} manga articles with high quality SEO content.")

if __name__ == "__main__":
    main()
