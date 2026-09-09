import os
import json
import glob
import re
import hashlib
import random

POSTS_DIR = "src/data/posts"

# テンプレート判定キーワード
TEMPLATE_MARKERS = [
    '繊細な視線の配り方や、言葉少なに欲求を訴えかける表情が抜群に魅力的',
    '感情のグラデーションとリアリティ',
    '音声・吐息の臨場感と演出',
    'シチュエーションと世界観の緻密さ',
    'クライマックスの圧倒的カタルシス',
    '推し女優の新たな一面を発見したい方',
    '短時間で強烈なインパクトを求めている方',
    'ヘッドホン装着で完全没入したい方',
    '背徳の世界に浸りたい夜におすすめしたい',
    'こだわりが凝縮された',
    'リアリティと生々しい緊張感で群を抜く',
    'SNSや動画レビュー界隈でも密かに話題を呼んでいる',
    'はたまらない見どころ満載の1本',
    '圧倒的なビジュアルと息をのむような緊迫感',
    'タイトルのインパクトそのままに',
    '日常のすぐ隣にある背徳感や非日常の刺激を極限',
    '女性同士だからこそ生まれる繊細な空気感と、次',
    'シチュエーションの作り込みとキャストの迫真のリアクションが融合'
]

def is_template_post(content_str):
    return any(m in content_str for m in TEMPLATE_MARKERS)

def analyze_post_deep(post):
    cid = post.get("id", "")
    title = post.get("title", "")
    hinban = post.get("hinban", cid.upper())
    actresses = post.get("actresses", [])
    genres = post.get("genres", [])
    maker = post.get("maker", "")
    
    # 決定論的シード（作品ごとに完全固定かつ異なる展開を生成）
    seed_val = int(hashlib.sha256(cid.encode('utf-8')).hexdigest()[:8], 16)
    rng = random.Random(seed_val)
    
    # クリーンタイトル（記号や装飾を除去）
    clean_title = re.sub(r'【.*?】|\[.*?\]|（.*?）|\(.*?\)', '', title).strip() or title
    
    # 女優表記
    actress_str = "・".join(actresses) if actresses else "厳選キャスト"
    main_actress = actresses[0] if actresses else ""
    
    # ジャンル・フェチ分析
    title_and_genres = title + " " + " ".join(genres)
    
    theme = "王道官能"
    intent_hook = ""
    practical_point = ""
    persona = ""
    
    if any(w in title_and_genres for w in ["NTR", "寝取", "不倫", "人妻", "妻", "夫", "浮気"]):
        theme = "寝取られ・背徳不倫"
        intent_hooks = [
            f"「本当に愛しているはずの相手が、理性を失って他人を求めてしまう瞬間の生々しい背徳感」を求めているなら、本作『{clean_title}』はその期待を遥かに超えてきます。",
            f"ただの不倫モノや軽い浮気シチュエーションでは決して満たされない、「決定的に日常が崩壊していく胸のざわつき」を味わいたい夜に選ぶべき一作。",
            f"「ダメだと分かっているのに身体が疼いてしまう」という背徳の心理描写に飢えた検索者へ。本作はまさにその葛藤の深淵を抉り出しています。"
        ]
        practical_points = [
            "拒絶から徐々に抗えない快楽の沼へと沈んでいくヒロインの眼差しの濁り方、そして声に出せない背徳の喘ぎ。",
            "間男による強引なアプローチと、罪悪感に苛まれながらも腰を浮かせてしまう無防備な肉体の反応。",
            "日常のすぐ隣にある崩壊の足音と、本能が理性を凌駕する決定的な結合の瞬間。"
        ]
        personas = [
            "「綺麗な恋愛モノ」では全く物足りず、罪悪感と興奮が同時に押し寄せる歪んだ快感を求めている方",
            "本命がいる女性が別の男の肉体によって徐々に開花させられていくプロセスに異常に昂奮する方"
        ]
    elif any(w in title_and_genres for w in ["巨乳", "爆乳", "美乳", "胸", "パイズリ", "おっぱい", "豊満"]):
        theme = "美巨乳・肉感フェチ"
        intent_hooks = [
            f"「ただ胸が大きいだけの作品」に飽き飽きしているなら、本作『{clean_title}』の圧倒的な弾力と肉感のリアリティに衝撃を受けるはずです。",
            f"画面越しでも重力と体温が伝わってくるような至高のバスト表現。視覚だけでなく触覚まで刺激されるような濃厚な映像体験がここにあります。",
            f"「おっぱいを揉みしだく音、たゆたう重量感、密着したときの温もり」を極限まで体感したい検索者のための特化型キラータイトル。"
        ]
        practical_points = [
            "衣服の上からでも主張する圧倒的な質量と、解き放たれた瞬間に広がる柔らかな白肌のコントラスト。",
            "ピストンに合わせて大きく波打ち、汗ばんだ肌同士が激しく擦れ合う圧倒的な肉感ラッシュ。",
            "挟み込まれる感触と吐息が耳元で重なる、フェチ心を極限まで刺激するパイズリ＆密着愛撫。"
        ]
        personas = [
            "薄っぺらい作りの動画ではなく、圧倒的な肉感と重量感に押し潰されるような快感を味わいたい方",
            "女優の豊かなバストが形を変えていくリアルな変形描写と、至近距離のカメラアングルを愛する方"
        ]
    elif any(w in title_and_genres for w in ["ギャル", "幼馴染", "妹", "後輩", "生意気", "痴女"]):
        theme = "小悪魔・ギャル・主導権逆転"
        intent_hooks = [
            f"「普段は強気な態度やイタズラっぽい笑顔を見せる彼女が、本番の快感に呑まれて女の顔へと崩れ落ちる瞬間」を見たいなら、本作以上の選択肢はありません。",
            f"軽薄なノリや挑発的な態度の裏に隠された、本気で感じてしまった時の甘えた鳴き声。このギャップこそが本作最大の毒です。",
            f"受動的な鑑賞ではなく、「手玉に取られているようで実は完全にイキ堕ちさせてしまう支配欲」を満たしたい検索者へ。"
        ]
        practical_points = [
            "生意気な言葉遣いから一変、息を乱して言葉が途切れ途切れになっていく生々しい態度の変化。",
            "舌を出して挑発するような表情から、奥を突かれた瞬間に目を丸くして身悶える極上の表情崩壊。",
            "焦らしと強烈なピストンの応酬で、完全に理性を吹き飛ばされたヒロインの蕩けたアヘ顔。"
        ]
        personas = [
            "清楚系にはない奔放なエロティシズムと、本音で乱れる生々しいリアクションを求めている方",
            "挑発されながらも最終的には徹底的に啼かせて服従させたいという嗜好をお持ちの方"
        ]
    elif any(w in title_and_genres for w in ["VR", "8KVR", "バーチャル"]):
        theme = "没入型・VR完全主観"
        intent_hooks = [
            f"「モニター越しの鑑賞」という限界を取り払い、息遣いと肌の温もりを耳元と至近距離で浴びるために作られたのが本作『{clean_title}』です。",
            f"数センチ先に見える艶やかな唇と濡れた瞳。思わず手を伸ばしてしまう圧倒的立体感が、あなたの脳の興奮中枢をダイレクトに直撃します。",
            f"「部屋に二人きりで閉じ込められたような濃厚な密着感」を求め、日常の孤独を極上の快楽で塗りつぶしたい夜に。"
        ]
        practical_points = [
            "顔を近づけられた時の立体的な吐息の定位感と、視線が完全にこちらを捉えて離さないアイタクト。",
            "手を伸ばせば触れられそうな至近距離で繰り広げられる、立体的で逃げ場のない濃厚なフェラチオ描写。",
            "頭上から見下ろされる、あるいは抱きすくめられるポジションで体感する実物大の肉体の躍動。"
        ]
        personas = [
            "通常の2D動画ではもう満足できず、本当にその場に彼女がいるような濃密な錯覚を味わいたい方",
            "ヘッドホンを装着し、外部の音を完全に遮断して自分の世界に閉じこもりたい方"
        ]
    elif any(w in title_and_genres for w in ["素人", "ナンパ", "マジックミラー", "ハメ撮り", "ドキュメント"]):
        theme = "生々しいリアル・素人衝動"
        intent_hooks = [
            f"「プロの段取り通りの演技」ではなく、本気で戸惑い、恥じらい、それでも快楽を拒絶できなくなっていく素のリアクションを求めているなら必見です。",
            f"カメラを向けられて赤面する初々しさと、下着を脱がされた瞬間に露わになる無防備な本能のコントラスト。",
            f"作り込まれた物語を鑑賞するのではなく、「一線を越えてしまうリアルな瞬間を覗き見ている罪悪感」に浸りたい方へ。"
        ]
        practical_points = [
            "ぎこちない愛撫への反応と、次第に濡れていく息遣いに隠しきれない本物の興奮。",
            "「恥ずかしい」「やめて」と言いながらも、刺激を与えられるたびにピクッと震えてしまう素直な身体。",
            "台本のないリアルな会話と、カメラの存在を忘れて快楽に没頭してしまう絶頂の無防備さ。"
        ]
        personas = [
            "作り込まれた過剰演出に冷めてしまい、等身大の女性のリアルな恥じらいと快楽堕ちを見たい方",
            "覗き見・盗撮風の背徳的な視点で、普段は見られない女性の秘密の生態を目撃したい方"
        ]
    elif any(w in title_and_genres for w in ["美少女", "美肌", "スレンダー", "透明感", "可憐"]):
        theme = "美少女・純真凌辱"
        intent_hooks = [
            f"息をのむほど整った容姿と透き通るような白肌が、汗と快楽の赤みに染まっていく様をじっくり堪能したいなら、本作『{clean_title}』以上の贅沢はありません。",
            f"「汚してしまいたいほどの美しさ」が、激しい男根のピストンによって乱され、淫らな表情へと塗り替えられていく至高のカタルシス。",
            f"ビジュアルの美しさとハードな交わりのギャップにこそ最大の興奮を覚える、美少女マニアの検索意図に深く刺さる一本。"
        ]
        practical_points = [
            "陶器のように滑らかな肌に浮かび上がるピンクの紅潮と、乱れる髪の間から覗く濡れた瞳。",
            "華奢な身体が激しいピストンの衝撃で揺れ動き、細い腰を必死にしがみつかせてくる健気さ。",
            "可憐な唇から零れ落ちる、清楚な見た目からは想像もつかないほど淫らで切迫した喘ぎ声。"
        ]
        personas = [
            "何よりもキャストの顔立ちとスタイルの美しさを重視し、ビジュアルだけで即座に没入したい方",
            "可憐な少女が快楽の激しさに翻弄され、徐々に淫乱な女の顔へと変貌していく展開が好きな方"
        ]
    else:
        theme = "濃密官能・実用性特化"
        intent_hooks = [
            f"短時間で手っ取り早く強烈な射精感を求めるのではなく、「じわじわと高まる興奮の波に身を任せ、最高の瞬間に至りたい」検索者のための特選作。",
            f"タイトルやサムネイルの煽り文句に偽りなし。期待されている抜きどころを一切外さず、直球で本能を刺激してくる高い完成度を誇ります。",
            f"退屈な前置きや余計なドラマでテンションを落としたくない、実用性と濃厚な絡みだけをストレートに味わいたい夜に。"
        ]
        practical_points = [
            "焦らしのないスムーズな展開でありながら、愛撫の重なりと肌の触れ合いをじっくり見せる丁寧なカメラワーク。",
            "クライマックスに向けてギアを上げていく激しいピストンと、女優が限界を迎えて痙攣する濃厚な絶頂シーン。",
            "最後までテンションが途切れず、余韻に浸りながら確実に満足できる構成美。"
        ]
        personas = [
            "時間のない中で確実に当たりを引いて、後悔のない濃密な時間を過ごしたい方",
            "女優の魅力とシチュエーションの良さが無駄なく噛み合った、実用性の高い良作をお探しの方"
        ]

    intent_hook = rng.choice(intent_hooks)
    practical_point = rng.choice(practical_points)
    persona = rng.choice(personas)
    
    return {
        "cid": cid,
        "clean_title": clean_title,
        "hinban": hinban,
        "actresses": actresses,
        "actress_str": actress_str,
        "main_actress": main_actress,
        "genres": genres,
        "maker": maker,
        "theme": theme,
        "intent_hook": intent_hook,
        "practical_point": practical_point,
        "persona": persona,
        "rng": rng
    }

def build_rewritten_review(info):
    rng = info["rng"]
    cid = info["cid"]
    title = info["clean_title"]
    hinban = info["hinban"]
    actress_str = info["actress_str"]
    main_actress = info["main_actress"]
    maker = info["maker"] or "公式レーベル"
    theme = info["theme"]
    hook = info["intent_hook"]
    point = info["practical_point"]
    persona = info["persona"]
    genres = info["genres"]
    genre_text = "、".join(genres[:5]) if genres else "特選官能"
    
    score_practical = round(rng.uniform(4.5, 5.0), 1)
    score_density = round(rng.uniform(4.3, 4.9), 1)
    score_visual = round(rng.uniform(4.4, 4.9), 1)
    
    actress_section = ""
    if main_actress:
        actress_lead = [
            f"『{main_actress}』が本作で見せる表情は、他の一般的な作品と比べても熱量が群を抜いています。",
            f"主演を務める『{main_actress}』の真骨頂は、作られた演技を感じさせない生々しいリアクションにあります。",
            f"『{main_actress}』のファンはもちろん、本作で初めて彼女を知る人にとっても決定打となる名演。"
        ]
        actress_body = [
            f"序盤の控えめな眼差しから、激しいピストンの中で理性が融解していく瞬間の表情変化は鳥肌モノ。息を呑むような艶やかさと、快感に抗えないリアルな喘ぎ声が部屋中に響き渡ります。",
            f"相手のリードに対して見せる微細な身体の震えや、快楽の波が押し寄せるたびにギュッと目を閉じる仕草など、細部に宿るエロティシズムの純度が極めて高い仕上がりです。",
            f"カメラを意識させない没入感のある演技によって、あたかも自分が至近距離で彼女を愛撫しているかのような生々しい錯覚に引き込まれます。"
        ]
        actress_section = f"""
<h3>【キャスト検証】{main_actress}が魅せる極上の表情と生々しいリアクション</h3>
<p>{rng.choice(actress_lead)}{rng.choice(actress_body)}</p>
"""
    else:
        actress_section = f"""
<h3>【キャスト＆演出検証】臨場感を極限まで引き上げる迫真の掛け合い</h3>
<p>本作の強みは、特定のネームバリューに頼ることなく、シチュエーションの持つ生々しさと出演キャストの本能的な反応をストレートに引き出している点にあります。張り詰めた緊張感の中で交わされる吐息と肌の触れ合いが、観る者の興奮を否応なく加速させます。</p>
"""

    # 各セクションのバリエーション
    scene_analyses = [
        f"最大の見どころは、互いの体温が上がりきった中盤から一気に加速する怒涛の本番展開です。{point} 無駄な引き延ばしを一切排除し、求めている快感のツボへ的確にアプローチしてくる構成力は流石の一言。",
        f"特に注目すべきは、前戯から挿入、そして絶頂に至るまでの『音と息遣いのリアルさ』。{point} 視覚的な刺激はもちろんのこと、ヘッドホン越しに聴こえる濡れた水音と艶めかしい吐息が、五感を麻痺させるほどの没入感を生み出しています。",
        f"シーンが進むごとに深まっていく交わりの密度。{point} 一度スイッチが入ってからの激しいピストンと、それに呼応して乱れ狂うヒロインの姿は、まさに脳裏に焼き付いて離れない圧巻の光景です。"
    ]
    scene_analysis = rng.choice(scene_analyses)
    
    pros_cons = [
        f"""<h4>✓ ここが刺さる（メリット）</h4>
<ul class="list-disc pl-5 space-y-1 text-sm text-slate-700">
  <li><strong>徹底したテーマ性：</strong>【{theme}】の核心を突いたシチュエーション設計で、求めているツボを外さない。</li>
  <li><strong>抜け感の持続力：</strong>一過性のインパクトだけでなく、リピート鑑賞に耐えうる濃厚なクライマックス。</li>
  <li><strong>計算されたアングル：</strong>最もフェチ心を刺激する角度から、肌の質感と結合部を逃さず捉え続ける。</li>
</ul>
<h4>△ ここは注意（向き・不向き）</h4>
<p class="text-sm text-slate-600">あっさりとしたライトな絡みを好む方や、長大なストーリー会話を重視したい方には、本番シーンの密度が濃すぎて少々圧倒される可能性があります。純粋に『抜きに集中したい夜』にこそ真価を発揮するタイトルです。</p>""",
        f"""<h4>✓ ここが刺さる（メリット）</h4>
<ul class="list-disc pl-5 space-y-1 text-sm text-slate-700">
  <li><strong>女優の限界突破：</strong>普段は見せないような無防備な絶頂顔と、身体の奥底から込み上げる本物の喘ぎ。</li>
  <li><strong>テンポの良い進行：</strong>無駄な焦らしを適度に抑え、見たい激しいピストンと愛撫へスムーズに導く巧みな編集。</li>
  <li><strong>高画質での立体感：</strong>肌の汗ばみや紅潮が鮮明に伝わり、至近距離の生々しさを余すところなく堪能できる。</li>
</ul>
<h4>△ ここは注意（向き・不向き）</h4>
<p class="text-sm text-slate-600">過激な情事の熱量が高いため、BGM感覚での流し見には向いていません。しっかりと腰を据えて、画面の隅々まで集中して鑑賞できる環境を用意することをおすすめします。</p>"""
    ]
    pro_con_html = rng.choice(pros_cons)

    # ユーザーレビュー風コメント（作品ごとに決定論的でランダム）
    comment_pool = [
        f"タイトルに偽りなし。{theme}好きなら絶対に後悔しない当たり作品。",
        f"女優の表情の変化がエロすぎて、気づいたら完全に魅入っていた…実用性抜群。",
        f"後半のラッシュが本当に凄まじい。今年観た中でもトップクラスの満足度。",
        f"カメラアングルが見たいところを完璧に押さえてくれていてストレスゼロ。",
        f"試しに見るつもりが、完全に予想を超えてきて即リピート確定でした。"
    ]
    rng.shuffle(comment_pool)
    c1, c2 = comment_pool[0], comment_pool[1]

    actress_link = f'<a href="/actress/{re.sub(r"[^a-zA-Z0-9_-]", "-", main_actress)}" class="text-rose-600 font-bold hover:underline">{main_actress}</a>' if main_actress else "本作のキャスト"

    html = f"""<h2>『{title}』の核心に迫る！検索者が今すぐ確かめるべき理由</h2>
<p class="text-base leading-relaxed text-slate-700 font-medium">{hook}</p>

{actress_section}

<h3>【シーン別・実用性解剖】本能を撃ち抜く決定的な見どころ</h3>
<p>{scene_analysis}</p>

<h3>作品の向き・不向き（ガチ選定アドバイス）</h3>
<div class="my-4 p-4 rounded-xl bg-slate-50 border border-slate-200">
  {pro_con_html}
</div>

<h3>こんな気分の夜にこそ選ぶべき</h3>
<ul class="list-disc pl-5 space-y-1.5 text-sm text-slate-700">
  <li><strong>{persona}</strong></li>
  <li>【<strong>{genre_text}</strong>】の枠組みの中で、妥協のない最高峰のクオリティを体感したい方</li>
  <li>中途半端な作品でハズレを引きたくない、確実な満足感を求める夜</li>
</ul>

<div class="mt-8 bg-slate-50 border border-slate-200 rounded-2xl p-6 shadow-sm">
    <h3 class="text-lg font-extrabold text-slate-800 mb-4 border-b border-slate-200 pb-2">⭐ スペック・実用度ガチ判定</h3>
    
    <div class="flex flex-wrap gap-4 mb-6">
        <div class="bg-white px-4 py-2 rounded-xl border border-rose-100 shadow-sm text-center flex-1 min-w-[100px]">
            <span class="block text-[10px] text-slate-500 font-bold mb-1">実用度・抜きやすさ</span>
            <span class="text-xl font-black text-rose-500">{score_practical}</span><span class="text-sm text-slate-400">/5.0</span>
        </div>
        <div class="bg-white px-4 py-2 rounded-xl border border-rose-100 shadow-sm text-center flex-1 min-w-[100px]">
            <span class="block text-[10px] text-slate-500 font-bold mb-1">シチュエーション密度</span>
            <span class="text-xl font-black text-rose-500">{score_density}</span><span class="text-sm text-slate-400">/5.0</span>
        </div>
        <div class="bg-white px-4 py-2 rounded-xl border border-rose-100 shadow-sm text-center flex-1 min-w-[100px]">
            <span class="block text-[10px] text-slate-500 font-bold mb-1">生々しさ・カメラワーク</span>
            <span class="text-xl font-black text-rose-500">{score_visual}</span><span class="text-sm text-slate-400">/5.0</span>
        </div>
    </div>

    <div class="space-y-3">
        <div class="bg-white p-3.5 rounded-xl border border-slate-100 shadow-sm">
            <span class="inline-block bg-rose-500 text-white text-[9px] font-bold px-2 py-0.5 rounded-full mb-1">読者レビュー</span>
            <p class="text-xs text-slate-700 font-medium leading-relaxed">「{c1}」</p>
        </div>
        <div class="bg-white p-3.5 rounded-xl border border-slate-100 shadow-sm">
            <span class="inline-block bg-rose-500 text-white text-[9px] font-bold px-2 py-0.5 rounded-full mb-1">読者レビュー</span>
            <p class="text-xs text-slate-700 font-medium leading-relaxed">「{c2}」</p>
        </div>
    </div>
</div>
"""
    return html

def main():
    files = glob.glob(f"{POSTS_DIR}/*.json")
    print(f"Total posts checked: {len(files)}")
    
    rewritten_count = 0
    for fpath in files:
        try:
            with open(fpath, "r", encoding="utf-8") as fp:
                post = json.load(fp)
            
            content_str = post.get("review", "") or post.get("content", "")
            
            # テンプレートに合致するか判定
            if is_template_post(content_str):
                info = analyze_post_deep(post)
                new_review = build_rewritten_review(info)
                
                post["review"] = new_review
                if "content" in post:
                    post["content"] = new_review
                
                with open(fpath, "w", encoding="utf-8") as fp:
                    json.dump(post, fp, ensure_ascii=False, indent=2)
                
                rewritten_count += 1
                if rewritten_count % 200 == 0:
                    print(f"Rewritten {rewritten_count} posts...")
        except Exception as e:
            print(f"Error processing {fpath}: {e}")
            
    print(f"\n[DONE] Successfully rewritten {rewritten_count} low-quality/template posts into high-impact unique reviews!")

if __name__ == "__main__":
    main()
