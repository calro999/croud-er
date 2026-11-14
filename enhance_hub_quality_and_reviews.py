# -*- coding: utf-8 -*-
import os
import json
import re
import html

POSTS_DIR = os.path.join("src", "data", "posts")
hubs = [
    ("feature_2026_11_latest_av_masterpiece_summary", "総合新作AV"),
    ("feature_2026_11_mature_wife_masterpiece_summary", "人妻・熟女"),
    ("feature_2026_11_busty_beauty_masterpiece_summary", "巨乳・爆乳"),
    ("feature_2026_11_single_actress_masterpiece_summary", "単体専属・美少女"),
    ("feature_2026_11_amateur_pickup_masterpiece_summary", "素人・ハメ撮り"),
    ("feature_2026_11_lesbian_yuri_masterpiece_summary", "レズ・百合"),
    ("feature_2026_11_manga_comic_masterpiece_summary", "成人コミック・新作漫画")
]

CATCH_TEMPLATES = {
    "人妻・熟女": [
        "背徳の蜜壺…理性を捨てて喘ぎ乱れる艶やかな隣の人妻",
        "禁断の密会劇！若者を貪り尽くす熟れた肉体と危険なフェロモン",
        "夫には絶対に見せられない…恥じらいと快楽に悶絶する極上若妻",
        "潤んだ瞳と滴る愛液…家庭を忘れて貪り合う濃密中出しSEX",
        "豊満な柔肌が揺れる！年下男に跨がり狂乱騎乗位でイキ崩れる未亡人"
    ],
    "巨乳・爆乳": [
        "視界を埋め尽くす神乳！圧倒的肉感と弾力で攻め立てるパイズリ地獄",
        "揺れ狂う極上バスト！激しいピストンで波打つ肉体美に射精不可避",
        "たわわに実った極上果実！顔面を包み込む密着フェラと至福の快楽",
        "ブラから溢れる圧倒的質量！汗ばむ谷間に挟まれて理性が溶け出す",
        "重量級の巨乳が跳ねる！息を呑むエロスと迫力のハメ狂いピストン"
    ],
    "単体専属・美少女": [
        "息を呑む圧倒的透明感…トップ単体女優が魅せる本気のメス堕ちSEX",
        "至高の美少女が快感に蕩ける！滴る愛液と生々しい吐息に大興奮",
        "可憐な素顔が淫らに歪む…専属クオリティの極上フェラ＆濃密ピストン",
        "完全撮り下ろし専属作！美しすぎる肢体が快楽の絶頂で震え上がる",
        "見つめ合って深々と挿入…切なさとエロスが交錯する最高純度の中出し"
    ],
    "素人・ハメ撮り": [
        "カメラの前で露わになる本性！素人娘が生々しく喘ぎ乱れるリアル交尾",
        "ナンパから即ホテルへ直行！警戒心を解いて潮吹きアクメに沈む生ハメ",
        "ネットで知り合った神ボディ素人！恥じらいながらもチンポを求める生中出し",
        "完全密着プライベート個室！プロにはない素朴な反応とガチイキの連続",
        "カメラを忘れて腰を振る！本気で気持ち良くなってしまった素人美女の絶頂顔"
    ],
    "レズ・百合": [
        "舌先が絡み合う濃密接吻…美女二人が貪り合う至極のレズビアン快楽",
        "濡れそぼる秘部を愛撫し合う…女同士だからこそ届く最深部の絶頂責め",
        "貝合わせで滴る蜜液！指先と舌で互いを極限までイカせ合う百合の極み",
        "柔らかな肌と肌が密着…甘い吐息と痙攣が止まらない濃厚レズセックス",
        "理性を奪うクンニ地獄！快感に涙を流しながら絶頂を重ねる極上美女"
    ],
    "成人コミック・新作漫画": [
        "美麗な筆致で描かれる極上エロス！背徳と快楽の限界を突破する神作",
        "圧倒的な画力と生々しい肉感描写！読めば確実に抜ける今月の大注目作",
        "フェチズムが暴走する超濃密シチュエーション！ページをめくる手が止まらない",
        "表情の歪みと愛液の描写が凄まじい…同人界隈を震撼させる最高峰の快楽劇",
        "圧倒的ボリュームと抜きどころの連続！一度読んだら忘れられない至高の傑作"
    ],
    "総合新作AV": [
        "今月絶対に見逃せない大ヒット作！ハイクオリティな演出と極上の絡み",
        "売上・話題性ともに独占！トップ女優と名門メーカーが放つ本気の傑作",
        "圧倒的臨場感で脳を揺さぶる！高画質映像で楽しむ至福のピストン劇",
        "ファン絶賛の濃厚エロス！息遣いまで伝わるリアルな快楽ドキュメント",
        "今月のFANZAランキングを席巻！最初から最後まで抜けるシーンの連続"
    ]
}

REVIEW_TEMPLATES = {
    "人妻・熟女": [
        "家庭や日常の枠組みから解き放たれ、一人のメスとして快楽に溺れていく心理描写と生々しい肉体美が圧巻。しっとりと濡れた秘部に深々と挿入され、背徳感に震えながら腰をくねらせるシーンは必見です。",
        "年齢を重ねるごとに増すフェロモンと、我慢できない快楽に蕩けていく表情が男の本能を刺激。控えめな態度から一転、我を忘れて淫語を漏らしながら中出しを求める姿に理性が崩壊します。"
    ],
    "巨乳・爆乳": [
        "画面いっぱいに広がる迫力のバストと、ピストンの衝撃に合わせて激しく波打つ圧倒的質量感。手や口だけでなく全身の柔肌を使って包み込むような密着愛撫は、巨乳ファンならずとも息を呑む破壊力です。",
        "ただ大きいだけでなく、張りと柔らかさを兼ね備えた極上の美乳。激しいピストンの中で汗ばみ、桃色の乳首をビンビンに尖らせながらイキ乱れるシーンの連続に射精が止まりません。"
    ],
    "単体専属・美少女": [
        "トップ単体女優ならではの卓越したビジュアルと、作品全体を包み込む贅沢なカメラワーク。男優のリードに身を委ね、徐々に羞恥心を脱ぎ捨てて本気の快楽に没入していく姿が極上のエロスを生み出しています。",
        "見つめ合う瞳、耳元で囁かれるリアルな吐息、そして絶頂時に見せる無防備な表情。単なる演技を超えた熱量とエロスが詰まっており、最初から最後まで没入感たっぷりに楽しめます。"
    ],
    "素人・ハメ撮り": [
        "演出されたAVでは決して味わえない、リアルな緊張感と生々しい反応が最大の魅力。ぎこちない手つきから徐々に快感に目覚め、本気でチ〇ポを締め付けてくるリアルな交尾に興奮が最高潮に達します。",
        "個室空間での密着から、徐々に理性が外れていくドキュメント感。カメラの前で晒されるリアルな恥じらいと、我慢できずに漏れ出る喘ぎ声が男の本能を直撃します。"
    ],
    "レズ・百合": [
        "女性特有の繊細なタッチと、貪り合うような濃密な舌使いが織りなす極上の百合世界。相手の性感帯を熟知した攻めで何度も絶頂を繰り返し、互いの愛液で全身を濡らし合う映像美に圧倒されます。",
        "視線の交わし合いから徐々に高まっていくエロスの熱量。男の介在しない二人だけの密室で、愛と快楽が完全に溶け合った極上のレズプレイは何度見ても飽きさせません。"
    ],
    "成人コミック・新作漫画": [
        "コマ割り、構図、トーンワークのすべてが読者の興奮を極限まで高めるよう計算し尽くされた傑作。キャラクターの細やかな表情の変化や、溢れ出る愛液・汗の質感描写が抜群の抜けを提供します。",
        "ストーリーの導入からクライマックスの乱れ狂いまで、読者を引き込んで離さない構成力。フェチ心をくすぐるシチュエーションが完璧に描かれており、コレクションに加える価値のある一冊です。"
    ],
    "総合新作AV": [
        "名門メーカーのこだわり抜かれた企画力と、出演キャストの圧倒的ポテンシャルが見事に融合した今月の代表作。映像のクリアさ、音響の生々しさ、そして何より絡みの濃厚さが群を抜いています。",
        "導入のシチュエーションからラストの怒涛の絶頂ラッシュまで一切の無駄がない充実の構成。今月どの作品を観るべきか迷っているなら、まず間違いなく押さえておくべきイチオシのタイトルです。"
    ]
}

def clean_and_enhance():
    for hub_file, genre_key in hubs:
        path = os.path.join(POSTS_DIR, f"{hub_file}.json")
        if not os.path.exists(path):
            continue
        
        with open(path, "r", encoding="utf-8") as f:
            d = json.load(f)
        
        review = d.get("review", "")
        parts = review.split("<!-- 追加カード:")
        header_part = parts[0]
        card_parts = parts[1:]
        
        new_cards = []
        for idx, cp in enumerate(card_parts, 1):
            cid_match = re.match(r"\s*([A-Z0-9_\-]+)\s*-->", cp, re.I)
            cid = cid_match.group(1) if cid_match else f"ITEM-{idx}"
            
            author_match = re.search(r'(<span class="text-slate-400">著者・サークル: <strong class="text-rose-300 font-bold">)(.*?)(</strong></span>)', cp)
            if author_match:
                authors = [a.strip() for a in author_match.group(2).split("、")]
                if len(authors) > 3:
                    short_authors = "、".join(authors[:3]) + " ほか"
                    cp = cp.replace(author_match.group(0), f'{author_match.group(1)}{short_authors}{author_match.group(3)}')

            creator_match = re.search(r'<strong class="text-rose-300 font-bold">(.*?)</strong>', cp)
            creator_name = creator_match.group(1) if creator_match else "出演キャスト"
            
            copy_list = CATCH_TEMPLATES.get(genre_key, CATCH_TEMPLATES["総合新作AV"])
            rev_list = REVIEW_TEMPLATES.get(genre_key, REVIEW_TEMPLATES["総合新作AV"])
            
            chosen_copy = copy_list[(idx - 1) % len(copy_list)]
            if creator_name and "ほか" not in creator_name and len(creator_name) < 15:
                if "【" not in chosen_copy:
                    chosen_copy = f"【{creator_name}】{chosen_copy}"

            chosen_rev = rev_list[(idx - 1) % len(rev_list)]

            cp = re.sub(r'<p class="text-xs font-bold text-rose-400 tracking-wide">.*?</p>', f'<p class="text-xs font-bold text-rose-400 tracking-wide">{html.escape(chosen_copy)}</p>', cp)
            cp = re.sub(r'(<span>💎</span><span>見どころ＆おすすめポイント</span>\s*</p>\s*<p>).*?(</p>)', f'\\1{html.escape(chosen_rev)}\\2', cp, flags=re.DOTALL)
            cp = re.sub(r'<span class="inline-flex items-center justify-center w-7 h-7 rounded-full bg-gradient-to-r from-rose-600 to-pink-600 text-white font-black text-xs shadow-md">\s*#\d+\s*</span>', f'<span class="inline-flex items-center justify-center w-7 h-7 rounded-full bg-gradient-to-r from-rose-600 to-pink-600 text-white font-black text-xs shadow-md">#{idx}</span>', cp)

            new_cards.append(f"<!-- 追加カード: {cid} -->" + cp[cp.find("-->") + 3:])

        d["review"] = header_part + "".join(new_cards)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        print(f"[{genre_key}] Polished {len(new_cards)} cards.")

if __name__ == "__main__":
    clean_and_enhance()
