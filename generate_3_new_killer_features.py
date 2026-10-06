# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・新規キラー特集3記事自動生成スクリプト
1. 【同棲生活・甘々イチャラブ・彼女感特化】
   『【本物の彼女のような多幸感】FANZA「同棲生活・甘々イチャラブ」おすすめ神作ランキングTOP5！疲れた心を全力で癒やす至高の恋人感覚・密着ラブラブ作品選【2026年最新】』
2. 【本格コスプレ・再現度MAX・ヒロイン特化】
   『【二次元の理想を完全具現化】FANZA「本格コスプレ・ヒロイン特化」おすすめ神作ランキングTOP5！超絶クオリティ衣装と美少女キャストが魅せる至高のファンタジー作品選【2026年最新】』
3. 【大型新人デビュー・圧倒的透明感・清楚系美少女特化】
   『【息をのむ美貌と初々しい恥じらい】FANZA「大型新人デビュー・圧倒的透明感の美少女」おすすめ神作ランキングTOP5！注目の超新星が魅せる純情可憐な傑作選【2026年最新】』
"""

import os
import re
import json
import time
import urllib.parse
import requests

API_ID = "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = "onchan555-999"
LINK_AFFILIATE_ID = "onchan555-003"
OUTPUT_DIR = "src/data/posts"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open("src/lib/slugs.json", "r", encoding="utf-8") as f:
    slugs_data = json.load(f)
actress_slugs = slugs_data.get("actresses", {})
genre_slugs = slugs_data.get("genres", {})

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

# 作品別の完全オリジナル・濃密レビュー辞書
INDIVIDUAL_REVIEWS = {
    # 記事1: 同棲・甘々イチャラブ
    "1start00581": """<h2>『リアルにものすごく近い同棲生活！最高にエッチで可愛い神木麗が彼女になってハメまくり！ 神木麗』詳細レビュー</h2>
<p>圧倒的な美貌と柔らかなボディラインで不動の人気を誇る神木麗が、「交際1年目のリアルな同棲彼女」を演じきった多幸感MAXの傑作です。朝起きた瞬間のおはようキスから、休日のリビングでの無防備なじゃれ合い、そして夜のベッドでとろけるような甘い交わりまで、男性が夢見る「理想の同棲生活」が完璧な解像度で描き出されています。</p>

<h3>見どころ：彼女感溢れる飾らない笑顔と生活感たっぷりのイチャつき</h3>
<p>大きめの部屋着Tシャツから覗く白い太ももや、すっぴん風のナチュラルメイクで寄り添ってくる神木麗の破壊力は言葉を失うレベルです。「ねえ、まだ寝るの？」「ちょっとこっち来てぎゅーってして」と甘えてくる声のトーンが生々しく、本物の彼女と暮らしているかのような強烈な錯覚に襲われます。台本を感じさせない自然体のキスとハグに、日々のストレスが完全に消し去られます。</p>

<h3>実用ポイント：全身密着で愛を確かめ合うスロー＆ディープなピストン</h3>
<p>お互いの温もりを確かめ合うように、胸と胸を密着させてじっくりと腰を重ねる正常位や対面座位。神木麗が首筋に腕を回し、耳元で愛らしい吐息を漏らしながら「好き…もっと奥まで入れて…」と懇願するシーンは実用度満点です。激しいピストンではなく、情感たっぷりにじわじわと高まっていく絶頂は、賢者タイムの虚無感とは無縁の圧倒的な幸福感をもたらします。</p>""",

    "sone00991": """<h2>『最強ヒロインが彼女になって毎日ヌイてくれるイチャラブ半同棲 瀬戸環奈』詳細レビュー</h2>
<p>純真無垢な美少女フェイスと驚異のメリハリボディを兼ね備えた瀬戸環奈が、大好きな彼氏のために甲斐甲斐しく尽くし、毎日欠かさず射精のお世話をしてくれる半同棲ドリーム作。仕事でボロボロになって帰宅した彼氏を玄関で抱きしめ、お風呂でもベッドでもとことん甘やかしてくれる包容力に男性ホルモンが激しく刺激されます。</p>

<h3>見どころ：疲れた彼氏を労る献身的なお風呂イチャラブ</h3>
<p>「今日もお仕事お疲れさま！一緒にお風呂入ろ？」と笑顔で迎え入れてくれる瀬戸環奈。湯船の中で身体を洗いっこしながら、泡だらけの手で優しくペニスを包み込み、ゆっくりとストロークしてくれます。恥じらいつつも「私の前では我慢しないで全部出していいんだよ」と微笑む聖母のような眼差しに、男の理性は一瞬で溶け落ちます。</p>

<h3>実用ポイント：ベッドの上で自分から跨がって腰を振る甘えん坊騎乗位</h3>
<p>ベッドになだれ込むと、彼氏を横たわらせたまま上に跨がり、自分からゆっくりと結合部を飲み込んでいく環奈ちゃん。敏感な膣内がペニスを吸い付くように締め付け、気持ちよさに頬を染めながら「環奈の中で気持ちよくなってね…」と腰を揺らす姿は至高のエロスです。果てる瞬間まで愛の言葉を囁いてくれる極上の射精体験がここにあります。</p>""",

    "ssis00575": """<h2>『美人でスタイル抜群、更に天性の優しさを持つパーフェクトお姉さんが世界一世話焼きな彼女目線で筆おろししてくれるガチ童貞×S1美女優30日同棲ドキュメント 楓ふうあ』詳細レビュー</h2>
<p>高身長スレンダーの圧倒的プロポーションと天使の微笑みを持つ楓ふうあが、女性経験のない童貞男子と1ヶ月間リアルに同棲生活を送り、優しく包み込むように男にしてあげる前代未聞の感動的イチャラブドキュメント。ぎこちない共同生活から徐々に距離が縮まり、お互いにかけがえのない存在になっていく過程が極めてエモーショナルに描かれます。</p>

<h3>見どころ：少しずつ心の距離を縮めていくリアルな恋愛心理</h3>
<p>最初は目を合わせるだけで緊張していた童貞の彼に対し、楓ふうあは一切否定せず、優しくリードしながら手料理を振る舞い、添い寝でスキンシップを重ねていきます。「手、繋いでもいい？」「ドキドキしてるの伝わってくるよ」と優しく語りかけ、徐々に男としての自信を目覚めさせていくアプローチは全男性の涙腺と股間を同時に刺激します。</p>

<h3>実用ポイント：優しさと情熱が溢れ出す涙の筆おろしセックス</h3>
<p>ついに迎えた筆おろしの夜、楓ふうあは彼の上に優しく覆いかぶさり、何度も優しいキスを交わしながら自分の身体へと導きます。初めての挿入に戸惑う彼を「大丈夫だよ、ゆっくり動かして…」と温かく包み込み、互いの吐息が混ざり合う濃厚な結合シーンは、他のどんな作品でも味わえない唯一無二の多幸感と濃厚な抜きやすさを誇ります。</p>""",

    "dvaj00697": """<h2>『「私でなきゃ勃起できないカラダにしてあげる」独占欲が強すぎるヤンデレ彼女に朝昼晩ヌかれ続ける16発搾精ルーティン体内精子ゼロ生活 逢沢みゆ』詳細レビュー</h2>
<p>可憐な美少女・逢沢みゆが、彼氏への愛が深すぎるあまり「他の女を絶対に考えられないように身体の精子をすべて抜き尽くす」という強烈な独占欲を発揮する、甘くて危険なヤンデレ同棲搾精作品。朝のアラーム代わりのフェラから、夜這い、休日の拘束搾精まで、1日中愛され尽くして骨抜きにされる至福の監禁系イチャラブです。</p>

<h3>見どころ：甘い笑顔の裏に隠された狂気的なまでの愛情表現</h3>
<p>「私のこと、世界で一番好きだよね？」「浮気なんか絶対させないからね♡」と囁きながら、彼氏の股間に跨がる逢沢みゆ。逃げ場のない狭いベッドの上で、両手を押さえつけられながら耳元に甘い淫語を吹き込まれる背徳感は桁違いです。彼氏を独占したいという狂おしい愛情が、最高レベルのエロティシズムへと昇華されています。</p>

<h3>実用ポイント：休む暇を与えない朝昼晩16発の追撃ピストン</h3>
<p>一度射精してもペニスを膣内から抜かず、「まだまだ出せるでしょ？私の愛、全部受け止めて！」と腰をグラインドさせ続ける逢沢みゆ。射精後の超敏感になった亀頭を子宮口でグリグリと刺激され、連続で精液を吸い上げられる快感地獄は、ドM本能を持つ男性の射精ボタンを連打すること間違いありません。</p>""",

    "midv00140": """<h2>『ヤリまくり一泊二日の温泉旅行で本能のままオマ○コ性交 石川澪』詳細レビュー</h2>
<p>圧倒的透明感と国民的妹キャラとして絶大な支持を集める石川澪と、誰にも邪魔されない温泉旅館で過ごす濃厚イチャラブ旅行記。客室露天風呂での密着洗体から、浴衣をはだけさせて畳の上で貪り合う濃密セックスまで、付き合いたての一番燃え上がっている時期のカップルの熱量が画面越しにダイレクトに伝わってきます。</p>

<h3>見どころ：温泉の熱気で上気した白肌と無防備な浴衣姿</h3>
<p>湯上がりのほんのりピンク色に染まった肌に、ゆるく帯を締めただけの浴衣姿で現れる石川澪。「お風呂気持ちよかったね…ちょっとのぼせちゃったかも」と畳の上に寝転がり、太ももを露出させる無防備な仕草に男の欲望は即座に限界突破します。照れ笑いを浮かべながら自分から胸元を開いて見せてくる初々しさがたまりません。</p>

<h3>実用ポイント：畳の上で浴衣をめくり上げて貪る本能の交尾</h3>
<p>帯を解いて露わになった華奢な身体を抱き寄せ、畳の上できしむ音を響かせながら幾度も繰り返される生交尾。石川澪が小刻みに腰を震わせ、「ああっ、そこすごい…もっと強くして！」と普段の清純なイメージをかなぐり捨てて快楽に溺れていく姿は圧巻です。旅情の開放感とプライベート感満載の生々しい喘ぎ声が最高潮の興奮へと導きます。</p>""",

    # 記事2: 本格コスプレ・ヒロイン特化
    "ssis00984": """<h2>『最高主観でコスプレ彩花に大量フェラチオ顔射 河北彩花』詳細レビュー</h2>
<p>圧倒的な気品とトップクラスの美貌を誇る「現代AV界の女王」河北彩花（河北彩伽）が、ファン垂涎の多彩なコスプレ衣装に身を包み、完全主観（POV）目線で奉仕してくれる至高の夢企画。完璧な美顔がすぐ目の前まで迫り、衣装ごとのキャラクターになりきりながら濃厚なフェラチオと顔射を受け止めてくれる贅沢すぎる1本です。</p>

<h3>見どころ：完璧な美少女によるハイクオリティな変幻自在コスプレ</h3>
<p>清楚なナース服から小悪魔なバニーガール、艶やかなチャイナドレスまで、河北彩花の抜群のプロポーションがそれぞれの衣装を究極の次元へと引き上げています。普段のクールな美貌とは一味違う、コスプレならではの茶目っ気と大胆な露出に視線が釘付けになります。衣装越しに強調されるバストやヒップのラインがフェティシズムを激しく刺激します。</p>

<h3>実用ポイント：ゼロ距離で見つめられながらの濃密フェラと大量顔射</h3>
<p>カメラの目の前に顔を寄せ、上目遣いでペニスを根元まで咥え込む河北彩花。舌先で亀頭を転がし、ジュポジュポと生々しい水音を響かせながら見つめてくる主観アングルは、まるで本当に自分が目の前で奉仕されているかのような錯覚をもたらします。フィニッシュでその陶器のような美顔一面に白濁液をぶち撒ける瞬間は、全男性の征服欲を極限まで満たしてくれます。</p>""",

    "ssni00963": """<h2>『日本一のSEXコスプレイヤー 三上悠亜』詳細レビュー</h2>
<p>国民的アイドルから世界的トップセクシー女優へと登り詰めたレジェンド・三上悠亜が、アニメ・ゲーム・ファンタジーの世界からそのまま飛び出してきたかのような超絶ビジュアルで魅了する本格コスプレの金字塔。衣装の細部に至るまで妥協なく作り込まれた世界観の中で、完璧な二次元ヒロインが淫らに乱れていく背徳のファンタジーです。</p>

<h3>見どころ：アイドル時代を凌駕する圧巻の二次元ヒロイン再現度</h3>
<p>金髪ツインテールの魔法少女や、タイトなスーツに身を包んだ女戦士、純白のシスター衣装など、三上悠亜の圧倒的な華と表現力によって、二次元の妄想が完璧な実写となって目の前に現れます。「こんなヒロインに犯されたい」「このキャラとエッチなことがしたい」という男の長年の妄想を120%具現化してくれた奇跡の作品です。</p>

<h3>実用ポイント：豪華衣装を着崩しながらの激しい結合とアヘ顔絶頂</h3>
<p>重厚な衣装のスカートをたくし上げ、パンツをずらしてむき出しになった秘部へと直接肉棒を突き刺すコントラスト。清楚で高潔なヒロインが、ピストンが進むにつれて白目を剥き、よだれを垂らしながら快楽に屈していく表情の変化は鳥肌モノの興奮を誘います。二次元好きも実写好きも問答無用で昇天させる至高の映像美です。</p>""",

    "mida00180": """<h2>『デビュー5周年記念企画！チキチキ小野六花31変化～！1ヶ月分の日替わり31コスプレ4時間31変化SPECIAL 小野六花』詳細レビュー</h2>
<p>天真爛漫な笑顔と抜群の美少女感でファンを虜にし続ける小野六花が、デビュー5周年を記念してなんと驚異の「31種類の日替わりコスプレ」に挑戦した超特大ボリューム作品。制服、体操服、スク水、メイド、チアガール、婦警、ナースなど、男が愛するあらゆるフェチコスチュームが4時間にわたってノンストップで繰り広げられます。</p>

<h3>見どころ：4時間31変化！あらゆるシチュエーションを網羅した圧倒的満足度</h3>
<p>「今日はどんな格好でご奉仕しようかな？」と、次から次へと異なる衣装で登場する小野六花。衣装が変わるたびにシチュエーションやキャラクター設定も変化し、まるで31本の異なる作品を連続で観ているかのような贅沢な感覚に浸れます。小野六花のコロコロ変わる愛らしい表情と、衣装ごとに見せる無邪気なエロスが満載です。</p>

<h3>実用ポイント：1本で一生抜ける！多彩なアングルと尽くし系セックス</h3>
<p>コスプレごとのショートストーリーから濃厚な本番セックスまで、抜きどころが隙間なく敷き詰められています。バックで美尻を突き出すポーズや、衣装を着たまま跨がってくる騎乗位など、多彩な体位で小野六花の柔肌を堪能可能。その日の気分に合わせて好きなチャプターを選んで即抜きできる、一家に一本常備すべき永久保存版の神作です。</p>""",

    "dass00765": """<h2>『MカップむっつりドMお嬢様 御堂前桃華のラブラブ変態調教アルバム 実写版 美園和花』詳細レビュー</h2>
<p>規格外のMカップ超爆乳を誇る美園和花が、大人気同人コミックのドM巨乳ヒロイン「御堂前桃華」を驚異のシンクロ率で実写化した話題作。普段はお淑やかな令嬢でありながら、裏では極小の露出衣装やボンデージに身を包み、大好きなご主人様に調教されることを夢見るむっつりスケベな生態が生々しく描かれます。</p>

<h3>見どころ：重力を無視したMカップ神乳と忠実すぎる二次元再現</h3>
<p>原作コミックの過激な衣装やポージングを、美園和花の圧倒的な肉体美で見事に再現。胸元が大きくくり抜かれた特注衣装からこぼれ落ちそうな超巨乳が、歩くたびにボヨンボヨンと大きく揺れる様は圧巻の一言です。恥ずかしそうに頬を染めながら「私を好きにしてください…」と懇願するドMお嬢様の姿に征服欲が刺激されます。</p>

<h3>実用ポイント：超重量級のパイズリと肉弾ボディを揺らす濃厚ピストン</h3>
<p>両手で抱えきれないほどの巨大なバストでペニスを挟み込み、ローションをたっぷり塗って行われるパイズリはまさに極楽浄土。さらに四つん這いにさせて背後から突っ込むと、肉厚なヒップと巨大な胸が激しく波打ち、視覚的にも快感的にも男の限界を軽々と突破させます。同人ファンのみならず巨乳マニアも必見の傑作です。</p>""",

    "ssni00478": """<h2>『極小セクシーコスで美乳・美尻がいつでもチラリ！ 過激オプション満載！押せばヤレる美少女チラリフレ店 架乃ゆら』詳細レビュー</h2>
<p>守ってあげたくなるような華奢な美少女・架乃ゆらが、布面積が極端に少ないマイクロビキニや過激なセクシーコスチュームで接客してくれるリフレ店を舞台にした妄想爆発作。少し動くだけで胸やお尻が丸見えになってしまうきわどい衣装で密着マッサージを受け、欲望を抑えきれなくなった客と本番になだれ込む展開が最高にエロティックです。</p>

<h3>見どころ：布面積限界の極小衣装から溢れる華奢なスレンダー美</h3>
<p>透け感のあるレース衣装や、紐だけで繋がったような超ミニコスプレを身にまとう架乃ゆら。透明感あふれる美白肌と、小ぶりながら形の良い美乳、引き締まったウエストのコントラストが芸術的です。「お客様、どこ見てるんですか…？」と戸惑いながらも、次第に過激なリクエストを受け入れていく過程にゾクゾクします。</p>

<h3>実用ポイント：密着オイルマッサージからなし崩し的に始まる生ハメ</h3>
<p>ぬるぬるのオイルを全身に塗りたくり、肌と肌を滑らせながら行われる密着プレイ。極小コスプレ越しに伝わる温もりに我慢できず、衣装をめくってそのまま挿入してしまう背徳の瞬間は抜きやすさ抜群です。架乃ゆらが小動物のように身をすくめながら可愛い嬌声を上げてイッてしまう姿は保護欲とサディズムを同時に満たします。</p>""",

    # 記事3: 大型新人デビュー・清楚美少女特化
    "midv00202": """<h2>『超新星 新人専属 五芭 AVdebut 10年に1度のビンカン現る。 五芭』詳細レビュー</h2>
<p>デビューと同時にAV界を震撼させ、レビュー160件超の爆発的ヒットを記録した「10年に1人の逸材」五芭の衝撃的デビュー作。清楚で大人しそうな黒髪美少女の見た目とは裏腹に、身体の隅々まで神経が通い詰めた超絶敏感体質で、少し触れられただけでビクビクと全身を跳ね上げて喘ぎ狂う奇跡のリアクションが収められています。</p>

<h3>見どころ：触れられただけで潮を吹き痙攣する本物のビンカンボディ</h3>
<p>問診や簡単な愛撫の段階から、吐息を荒げて太ももを震わせる五芭。指先でクリトリスを優しく撫でられただけで、腰を大きく浮かせてシーツを濡らしてしまうほどの超高感度です。「触られただけで変な気持ちになっちゃう…」と涙目になりながら恥じらう表情は、演技では絶対に再現できない本物の生々しさに満ちています。</p>

<h3>実用ポイント：初めての男根挿入で未知の快楽に白目を剥く本気アクメ</h3>
<p>いざ本番となり、硬く反り返ったペニスが窄まった処女孔へと押し込まれた瞬間、五芭の身体は弓なりに反り返り、声にならない絶叫を上げます。奥を突かれるたびに膣内がギューッと肉棒を締め付け、快楽の波に抗えず何度も連続絶頂へと達していく姿は、デビュー作にしか存在し得ない神がかったエロティシズムの頂点です。</p>""",

    "midv00513": """<h2>『新人 現役女子大生 専属 Hカップ 一心えりか AV Debut！ 一心えりか』詳細レビュー</h2>
<p>現役女子大生としてS1専属デビューを果たし、レビュー約150件という驚異的な支持を集めた一心えりか。あどけなさが残る人懐っこい笑顔と、服の上からでも一目でわかる大迫力のHカップ天然美巨乳という、世の男性の理想をそのまま形にしたようなド直球の王道美少女です。</p>

<h3>見どころ：服を脱いだ瞬間に現れる奇跡のHカップ天然美乳</h3>
<p>普段着の清楚なワンピースを脱ぎ捨てた瞬間、重みでたわわに揺れる純白のHカップバストが露わになります。作り物ではない柔らかさと弾力を兼ね備えた神乳に、誰もが息を呑むこと必至です。自分の大きな胸にコンプレックスを抱きつつも、褒められると嬉しそうに照れ笑いを浮かべる素朴なキャラクターが愛おしさを倍増させます。</p>

<h3>実用ポイント：大迫力のパイズリ挟み撃ちと揺れる胸を見つめながらの正常位</h3>
<p>両手で抱えるのもやっとの豊満な胸にペニスを挟み込まれ、温かい谷間で擦り上げられるパイズリの快感は言葉になりません。さらにベッドで激しく突かれるたびに、真っ白な巨乳が激しく波打ち、カメラに向かって快楽に歪んだアヘ顔を晒すシーンは実用性抜群。初々しさとドスケベな肉体美が完璧に融合した名作です。</p>""",

    "midv00484": """<h2>『新人 まだ‘可愛くなる方法’を知らない未完成原石AVデビュー 三浜唯』詳細レビュー</h2>
<p>地方から上京してきたばかりの飾らない純朴さと、洗練される前の圧倒的な素材の良さを持つ「奇跡の未完成原石」三浜唯の記念すべきファースト作。垢抜けないショートカットに少しぎこちない笑顔、そしてまだ自分の美しさに気づいていない無防備な少女が、大人の快楽の扉をこじ開けられていくドキュメンタリータッチのエロスです。</p>

<h3>見どころ：地方出身の素朴な女の子がカメラの前で晒す生々しい恥じらい</h3>
<p>「本当に私でいいんでしょうか…」と不安そうにインタビューに答える三浜唯。撮影が進むにつれて緊張がほぐれ、時折見せる無邪気な笑顔の破壊力は凄まじいものがあります。素人感満載のぎこちない手つきで男の身体に触れる姿や、キスをされた瞬間にきゅっと目を瞑るピュアな反応に胸が締め付けられます。</p>

<h3>実用ポイント：開発されていくたびに色気を増していく原石の覚醒</h3>
<p>初めて経験する本格的な責めに、戸惑いながらも身体が正直に熱を帯びていく三浜唯。膣奥を深く突かれると、幼い口元から「あっ…ああっ…！」と本気の嬌声が漏れ出し、次第に自分から腰を動かして快感を求め始める覚醒シーンは必見です。何色にも染まっていない純白の少女が女へと変わる瞬間を特等席で目撃できます。</p>""",

    "mudr00200": """<h2>『絶頂を知った日、私は大人になった 天然少女 無垢専属 AV DEBUT 日向ひかげ』詳細レビュー</h2>
<p>透き通るような白い肌と憂いを帯びた瞳が印象的な文学少女系美少女・日向ひかげ（琥珀やや）が、無垢レーベル専属として鮮烈なデビューを飾った名作。これまで本当のオーガズムを知らなかったという彼女が、丁寧に時間をかけて全身を愛撫され、生まれて初めての強烈な絶頂に震える姿を叙情的な映像美で描き出しています。</p>

<h3>見どころ：静寂の中で際立つ吐息と繊細な身体の震え</h3>
<p>どこか儚げな雰囲気を纏った日向ひかげが、静かな部屋の中で一枚ずつ衣服を脱ぎ捨てていく序盤から独特の緊張感が漂います。耳元で囁かれる言葉に耳を赤らめ、乳首をつままれるたびに小さくビクッと跳ねる身体の反応が極めて生々しく、見ている側の五感を研ぎ澄まさせます。</p>

<h3>実用ポイント：初めての絶頂で涙を流しながら痙攣する奇跡の瞬間</h3>
<p>ゆっくりと丁寧にピストンを繰り返されるうちに、日向ひかげの表情が次第に恍惚へと溶けていきます。人生で初めて訪れた深いオーガズムに、驚きと快感が入り混じった涙を瞳に浮かべ、指先をぎゅっと握りしめて震えるシーンはまさに芸術的エロス。単なる性交を超えた、心と身体が完全に解き放たれる感動的な射精を約束します。</p>""",

    "mida00817": """<h2>『新人 隠れ巨乳Fカップ専属 風見渚月 AV Debut！ 風見渚月』詳細レビュー</h2>
<p>清楚なOL風の端正な顔立ちと知的な佇まいを持ちながら、服の下には極上のFカップ美乳を隠し持っていた「ギャップの極み」風見渚月のデビュー作。真面目で礼儀正しい女性が、密室でじっくりと下半身を暴かれ、隠していたスケベな本性を惜しげもなく露わにしていくカタルシスが存分に味わえる一本です。</p>

<h3>見どころ：清楚系キャリア美女の服の下に隠された豊満なFカップ</h3>
<p>スーツ姿の凛とした姿から一転、ブラジャーを外すと現れる形の整った弾力あるFカップバスト。肌のキメが細かく、ほんのりピンク色の乳首が男の視線を釘付けにします。「恥ずかしいです…そんなに見ないでください」と言いながらも、興奮で乳首を硬く尖らせていくギャップに興奮を禁じ得ません。</p>

<h3>実用ポイント：理性のタガが外れて乱れ狂う大人のオンナの濃密交尾</h3>
<p>真面目な顔が快楽によって次第にメスの顔へと崩れていく過程が見事に捉えられています。激しいピストンに合わせて豊満な胸が波打ち、奥を突かれるたびに切なげに眉をひそめて喘ぐ風見渚月。大人の色香と初々しい恥じらいが同居する極上のベッドシーンは、落ち着いた大人の女性が好きなユーザーにとって最高の抜きどころです。</p>"""
}

# 3記事のメタ情報
ARTICLES = [
    {
        "id": "feature_fanza_cohabitation_sweet_girlfriend_lovelove_ranking_2026",
        "title": "【本物の彼女のような多幸感】FANZA「同棲生活・甘々イチャラブ」おすすめ神作ランキングTOP5！疲れた心を全力で癒やす至高の恋人感覚・密着ラブラブ作品選【2026年最新】",
        "hinban": "COHABITATION-LOVELOVE-GIRLFRIEND-2026",
        "cids": ["1start00581", "sone00991", "ssis00575", "dvaj00697", "midv00140"],
        "hero_tag": "COHABITATION & SWEET LOVE SPECIAL",
        "genres": ["同棲", "イチャラブ", "彼女", "美少女", "癒やし", "主観", "密着", "特集", "殿堂入り"],
        "lead_p1": "日々の仕事や人間関係で疲れ果てた現代の男性が、今もっとも求めている究極のジャンル――それが「同棲生活・甘々イチャラブ」です。過激なプレイや暴力的なシチュエーションではなく、本物の彼女と暮らしているかのような温もり、朝起きた瞬間のおはようキス、そして夜のベッドで全身を密着させて愛を確かめ合う時間。画面の向こうから伝わってくる圧倒的な「多幸感」が、冷えた心を芯から温めてくれます。",
        "lead_p2": "「今日もお疲れさま」「ぎゅーってして？」と甘えてくる愛らしい表情や、台本を感じさせない自然体のハグとキス。射精した後も虚しさを感じるどころか、心がじわっと満たされて優しい眠りにつけるのがイチャラブ同棲作品の最大の魅力です。疲れた男を全力で肯定し、世界で一番大切にされている感覚を味わえる至福の体験がここにあります。",
        "lead_p3": "本記事では、神木麗がリアルな交際1年目彼女を演じる超大作から、瀬戸環奈の毎日射精お世話半同棲、楓ふうあの奇跡の30日童貞同棲ドキュメント、逢沢みゆの独占欲ヤンデレ搾精、そして石川澪との濃密温泉旅行まで、恋人感と癒やしを極めた【同棲イチャラブ神作TOP5】を徹底レビューします！",
        "points": [
            ("① 生活感あふれる無防備な部屋着とすっぴん風メイク", "大きめのTシャツ一枚やショートパンツ姿でリビングを歩き回る彼女の無防備さ。飾らない素の笑顔と仕草が本物の共同生活のリアリティを生み出します。"),
            ("② ゼロ距離でのスキンシップと甘い囁き", "ハグ、腕枕、耳元への吐息混じりの囁き。「好きだよ」「ずっと一緒にいようね」と愛を囁かれながらの交わりが最高の癒やしをもたらします。"),
            ("③ 射精後も余韻を楽しめる多幸感とアフターケア", "ピストンが終わった後も体を離さず、優しく抱きしめ合ってキスを交わす至福のひととき。賢者タイムの虚無感を完全に払拭してくれます。")
        ],
        "table_headers": ["順位・タイトル", "主演女優", "同棲シチュエーション", "癒やし・幸福度", "詳細"],
        "faqs": [
            ("Q1. 同棲・イチャラブ作品の一番の魅力は何ですか？", "まるで本当に可愛い彼女と同棲しているかのような圧倒的な没入感と、射精後も心が満たされる多幸感です。過激さよりも愛情やスキンシップを重視したい夜に最適です。"),
            ("Q2. 初めて観るならどの作品がおすすめですか？", "第1位の神木麗主演作（1START-581）です。交際1年目のカップルの空気感が極めてリアルに再現されており、自然体の甘えっぷりに誰もがノックアウトされます。"),
            ("Q3. 癒やしだけでなく射精の実用性も高い作品はありますか？", "第4位の逢沢みゆ主演作（DVAJ-697）や第2位の瀬戸環奈主演作（SONE-991）がおすすめです。甘い同棲生活の中に濃厚な射精管理や騎乗位搾精が盛り込まれており、実用度も抜群です。")
        ],
        "related": [
            ("/posts/feature_fanza_missed_last_train_roomwear_sleepover_ranking_2026", "【終電逃しから始まる部屋着の誘惑】同僚・後輩女子宅へのお泊まりTOP5", "普段は見せない無防備な部屋着姿と密室のドキドキ感に理性が崩壊する名作選！"),
            ("/posts/feature_fanza_childhood_friend_sleepover_first_night_ranking_2026", "【幼馴染とお泊まり初夜】長年の友達関係が一線を越える甘酸っぱい交尾TOP5", "昔からの幼馴染と二人きりの夜に素直になって体を重ね合う胸キュンAV選！"),
            ("/posts/feature_fanza_subjective_pov_whispering_masturbation_support_ranking_2026", "【脳がトロける射精快楽】完全主観・耳元囁きオナサポ＆極上射精管理TOP5", "イヤホン必須！ゼロ距離の吐息と優しい淫語で脳幹まで痺れさせる主観特化選！"),
            ("/posts/feature_fanza_teasing_sister_devilish_seduction_ranking_2026", "【お兄ちゃん限定の特権】小悪魔妹・甘えん坊義妹の禁断誘惑TOP5", "生意気にからかってきながらも最後はお兄ちゃんに甘えてくる至高の妹エロス！")
        ]
    },
    {
        "id": "feature_fanza_cosplay_anime_heroine_reproduction_ranking_2026",
        "title": "【二次元の理想を完全具現化】FANZA「本格コスプレ・ヒロイン特化」おすすめ神作ランキングTOP5！超絶クオリティ衣装と美少女キャストが魅せる至高のファンタジー作品選【2026年最新】",
        "hinban": "COSPLAY-ANIME-HEROINE-2026",
        "cids": ["ssis00984", "ssni00963", "mida00180", "dass00765", "ssni00478"],
        "hero_tag": "COSPLAY & HEROINE SPECIAL",
        "genres": ["コスプレ", "美少女", "フェチ", "制服", "主観", "同人実写化", "特集", "殿堂入り"],
        "lead_p1": "アニメやゲーム、マンガの画面越しに憧れた「あの美少女ヒロインとエッチなことがしたい」という男の永遠の夢を叶えてくれるジャンル、それが「本格コスプレ・ヒロイン特化」です。単に衣装を着るだけにとどまらず、ウィッグ、メイク、衣装の質感、そしてキャラクターの口調や仕草に至るまで徹底的にこだわり抜かれた世界観は、見る者を一瞬で二次元と三次元が融合した官能の世界へと引きずり込みます。",
        "lead_p2": "完璧な衣装を着崩し、恥じらいながらも大胆に晒される白い素肌。高潔なヒロインや勝気な女戦士が、肉棒を突き立てられるにつれて白目を剥いて快楽に溺れていく姿は、通常の作品では絶対に味わえない極上の背徳感と征服欲をもたらします。二次元オタクはもちろん、フェチズムを刺激されたい全ての男性にとっての桃源郷です。",
        "lead_p3": "本記事では、当代随一の美貌を誇る河北彩花の完全主観コスプレ奉仕から、伝説の三上悠亜による神がかった二次元ヒロイン再現、小野六花の4時間31変化特大ボリューム作、美園和花のMカップ神乳コミック実写化、そして架乃ゆらの極小セクシーコスリフレまで、コスプレエロの最高峰を極めた【コスプレ神作TOP5】を徹底レビューします！",
        "points": [
            ("① 衣装のディテールとキャラクター再現へのこだわり", "ウィッグのセットや衣装の縫製、装飾品に至るまで妥協のないハイクオリティな造形。二次元の理想がそのまま実体化したような圧倒的説得力を生み出します。"),
            ("② 高潔なヒロインが快楽に堕ちていく背徳のカタルシス", "誇り高きキャラクターが、ピストンを重ねられるうちに理性を失い、淫らなアヘ顔で快感をねだるようになるギャップが最大の抜きどころです。"),
            ("③ 衣装を着たままの着崩し・チラリズムフェティシズム", "全裸になるのではなく、スカートをめくったり胸元をはだけさせたりする着衣エロス。布地と生肌のコントラストが男のフェチ本能を激しく刺激します。")
        ],
        "table_headers": ["順位・タイトル", "主演女優", "コスプレ属性・見どころ", "再現度・実用度", "詳細"],
        "faqs": [
            ("Q1. コスプレAVの醍醐味は何ですか？", "アニメやゲームの理想のヒロインが、現実の超美少女キャストによって目の前で動いて乱れてくれるという究極の妄想具現化です。衣装を着崩しての生々しい交尾は格別の背徳感があります。"),
            ("Q2. 1本で色々なコスプレを楽しみたい場合は？", "第3位の小野六花主演作（MIDA-180）が圧倒的におすすめです。4時間で31種類もの衣装が次々に登場するため、どんなフェチにも確実に刺さるシーンが見つかります。"),
            ("Q3. 主観（POV）でコスプレ美女に尽くされたいなら？", "第1位の河北彩花主演作（SSIS-984）一択です。現代最高峰の美貌を持つ河北彩花が至近距離でコスプレ姿のまま奉仕してくれる映像は、生涯の宝物になるクオリティです。")
        ],
        "related": [
            ("/posts/feature_fanza_vr_8k_ultra_immersive_best_ranking", "【8K圧倒的没入感】FANZA VR動画おすすめ殿堂入り神作TOP5", "手が届きそうな距離で美女が迫る！VRゴーグルで体感する究極の立体交尾！"),
            ("/posts/feature_fanza_pov_subjective_immersion_masterpiece_ranking", "【極上の密着・耳元吐息】FANZA「主観・POV」おすすめ殿堂入り神作TOP5", "画面の向こうの美女と完全に目が合う！主観アングルで脳がバグる傑作選！"),
            ("/posts/feature_fanza_pantyhose_slender_legs_ol_fetish_ranking", "【美脚・パンスト・黒タイツの誘惑】美脚パンスト・スーツOL傑作選", "破いたストッキングの隙間から肉棒をねじ込む至高のフェチズム特化AV！"),
            ("/posts/feature_fanza_doujin_cg_manga_high_rating_masterpieces", "【FANZA同人】超高評価CG集・同人コミックおすすめ名作選", "二次元の極上エロス！美麗なイラストと圧倒的シチュエーションの同人傑作！")
        ]
    },
    {
        "id": "feature_fanza_debut_newcomer_pure_beautiful_girl_ranking_2026",
        "title": "【息をのむ美貌と初々しい恥じらい】FANZA「大型新人デビュー・圧倒的透明感の美少女」おすすめ神作ランキングTOP5！注目の超新星が魅せる純情可憐な傑作選【2026年最新】",
        "hinban": "NEWCOMER-DEBUT-PURE-BEAUTY-2026",
        "cids": ["midv00202", "midv00513", "midv00484", "mudr00200", "mida00817"],
        "hero_tag": "NEW DEBUT & PURE BEAUTY SPECIAL",
        "genres": ["新人", "デビュー", "美少女", "清楚", "巨乳", "敏感", "単体作品", "特集", "殿堂入り"],
        "lead_p1": "数あるAVのジャンルの中で、時代や流行を問わず常に年間売上の頂点に君臨し続ける絶対の王道――それが「大型新人デビュー作」です。まだ業界の空気に染まっていない本物の恥じらい、カメラの前で初めて服を脱ぐときの緊張した面持ち、そして未知の快楽に触れて身体を震わせる初々しい反応。それら全てが、デビュー作という限られた一度きりの瞬間にしか記録できない奇跡の輝きを放ちます。",
        "lead_p2": "「本当に私でいいんでしょうか…」と不安げに語っていた少女が、ひとたび肉棒を受け入れると、抑えきれないメスの本能を開花させて艶やかな表情へと変貌していくカタルシス。作られた演技や予定調和が一切通用しない、ドキュメンタリーのような生々しい快楽の目覚めに、男の胸の高鳴りと下半身の衝動は最高潮に達します。",
        "lead_p3": "本記事では、デビュー作で異例のレビュー160件超を叩き出した五芭の超高感度ビンカン作から、現役女子大生・一心えりかの奇跡のHカップ、三浜唯の垢抜けない未完成原石の輝き、日向ひかげが無垢レーベルで見せた涙の初絶頂、そして風見渚月の隠れ巨乳Fカップまで、絶対に見逃せない【大型新人デビュー神作TOP5】を徹底レビューします！",
        "points": [
            ("① 演技ゼロ！カメラの前で初めて見せる本物の恥じらい", "プロの女優には出せない、ぎこちない仕草と照れ笑い。緊張で強張った表情が徐々に緩んでいく過程に強烈なリアリティが宿ります。"),
            ("② 未知の快楽に身体が勝手に反応してしまう敏感さ", "愛撫されるたびにビクビクと全身を震わせ、声にならない吐息を漏らす生々しい反応。身体が快感を覚えていく覚醒の瞬間が最大のハイライトです。"),
            ("③ 一生に一度しか撮れない「初々しさ」という究極の価値", "キャリアを重ねれば洗練されていくからこそ、デビュー作にしかない純朴さとぎこちなさは永遠の輝きを放ちます。即買いしても絶対に後悔しません。")
        ],
        "table_headers": ["順位・タイトル", "主演女優", "新人属性・チャームポイント", "初々しさ・衝撃度", "詳細"],
        "faqs": [
            ("Q1. 新人デビュー作がこれほど人気な理由は何ですか？", "計算された演技が一切ない「本物の恥じらい」と「リアルな快楽の目覚め」を体感できるからです。初めて大人の快楽を知って乱れていく姿は、全ジャンル中で最も興奮を誘います。"),
            ("Q2. 最も衝撃的なデビュー作を1本選ぶなら？", "第1位の五芭主演作（MIDV-202`五芭 AVdebut 10年に1度のビンカン現る。`）です。レビュー160件超が証明する通り、少し触れられただけで潮を吹き痙攣する高感度ボディはまさに歴史的傑作です。"),
            ("Q3. 巨乳系の新人でおすすめはありますか？", "第2位の一心えりか主演作（MIDV-513）です。服を脱いだ瞬間に現れる天然Hカップのド迫力バストと愛らしい女子大生の笑顔のギャップは破壊力抜群です。")
        ],
        "related": [
            ("/posts/feature_fanza_top_exclusive_actresses_ranking_masterpiece", "【2026年最新】FANZAで今もっとも抜ける「単体専属トップ女優」最強ランキング", "トップ女優たちの代表作を一挙集結！絶対にハズさない最高峰の単体AV選！"),
            ("/posts/feature_fanza_college_girl_gap_corruption_ranking", "【清楚女子大生の裏の顔】普段はおとなしいJDが快楽に溺れるギャップ作品TOP5", "真面目そうに見えて実は性欲旺盛な女子大生の生々しいエロスを徹底解剖！"),
            ("/posts/feature_fanza_first_anal_deflowering_ranking_2026", "【桃色処女孔が開く背徳と歓喜】人気単体女優の初アナル解禁神作TOP5", "未開の秘孔が初めて貫かれる痛悦の瞬間！美少女たちの限界アナル開発選！"),
            ("/posts/feature_fanza_creampie_breeding_deep_ejaculation_ranking", "【子宮に直接注ぎ込む背徳】濃厚種付け生中出しおすすめ神作TOP5", "ゴムなし生交尾の温もりと、奥深くに白濁液をドクドク注ぎ込まれる本能の交わり！")
        ]
    }
]

def main():
    print("=== STARTING GENERATION OF 3 NEW KILLER FEATURES ===")
    
    for art in ARTICLES:
        art_id = art["id"]
        art_title = art["title"]
        print(f"\nProcessing feature: {art_title}")
        
        items_data = []
        for rank_idx, cid in enumerate(art["cids"], 1):
            print(f" -> Fetching FANZA API for CID: {cid} (Rank {rank_idx})...", flush=True)
            it = fetch_fanza_item(cid)
            if not it:
                print(f"    WARNING: Failed to fetch {cid} via API!")
                continue
            it["rank"] = rank_idx
            items_data.append(it)
            time.sleep(0.3)
            
            # 個別作品JSONも最新情報で生成・更新（内部リンクを完璧に繋げるため）
            individual_path = os.path.join(OUTPUT_DIR, f"{cid}.json")
            iteminfo = it.get("iteminfo", {})
            actresses_list = [a.get("name") for a in iteminfo.get("actress", [])]
            genres_list = [g.get("name") for g in iteminfo.get("genre", [])]
            maker_name = iteminfo.get("maker", [{}])[0].get("name", "") if iteminfo.get("maker") else ""
            label_name = iteminfo.get("label", [{}])[0].get("name", "") if iteminfo.get("label") else ""
            
            ind_review = INDIVIDUAL_REVIEWS.get(cid, f"<p>{it.get('title')}</p>")
            ind_post = {
                "id": cid,
                "title": it.get("title"),
                "date": it.get("date", "2026-10-06 00:00:00"),
                "hinban": it.get("content_id", "").upper(),
                "price": str(it.get("prices", {}).get("price", "500~")),
                "maker": maker_name,
                "actresses": actresses_list,
                "genres": genres_list,
                "labels": [label_name] if label_name else [],
                "image": it.get("imageURL", {}).get("large", ""),
                "affiliate_url": it.get("affiliate_url_clean", it.get("affiliateURL", "")),
                "review": ind_review,
                "sample_images": get_sample_images(it, 10)
            }
            with open(individual_path, "w", encoding="utf-8") as f:
                json.dump(ind_post, f, ensure_ascii=False, indent=2)
            print(f"    Saved individual post JSON: {individual_path}")

        # 特集記事のHTML本文を構築
        hero_img = items_data[0].get("imageURL", {}).get("large", "") if items_data else ""
        
        # 女優一覧とジャンル一覧
        all_actresses = []
        for it in items_data:
            acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
            for a in acts:
                if a and a not in all_actresses:
                    all_actresses.append(a)
                    
        review_html_parts = []
        
        # ヒーロー導入部
        review_html_parts.append(f"""<div class="my-8 bg-gradient-to-br from-indigo-950/40 via-slate-900 to-slate-950 border border-indigo-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-indigo-500/20 text-indigo-300 border border-indigo-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">{art['hero_tag']}</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月06日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    {art_title}
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    {art['lead_p1']}
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    {art['lead_p2']}
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    {art['lead_p3']}
  </p>
</div>""")

        # 選び方チェックポイント
        review_html_parts.append(f"""<!-- 選び方の基準 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-indigo-400">✨</span> 本ジャンルで最高の満足度を得るための3大チェックポイント
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-indigo-300 mb-2">{art['points'][0][0]}</h4>
      <p class="text-slate-300 leading-relaxed">{art['points'][0][1]}</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-indigo-300 mb-2">{art['points'][1][0]}</h4>
      <p class="text-slate-300 leading-relaxed">{art['points'][1][1]}</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-indigo-300 mb-2">{art['points'][2][0]}</h4>
      <p class="text-slate-300 leading-relaxed">{art['points'][2][1]}</p>
    </div>
  </div>
</div>""")

        # 目次
        toc_items = []
        for it in items_data:
            r = it["rank"]
            t = it.get("title", "")
            cid = it.get("content_id", "")
            acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
            act_str = f"（{'・'.join(acts)}）" if acts else ""
            toc_items.append(f'<li><a href="#rank-{r}" class="hover:underline flex items-center justify-between"><span>第{r}位：{t[:35]}…{act_str}</span><span class="text-slate-500 text-xs">詳細へ ↓</span></a></li>')
            
        review_html_parts.append(f"""<!-- 目次 -->
<div class="my-8 bg-slate-900/60 border border-slate-800 rounded-2xl p-5 shadow-inner">
  <h4 class="text-sm font-bold text-slate-300 mb-3 flex items-center gap-2">
    <span>📑</span> 目次：おすすめランキングTOP5
  </h4>
  <ul class="space-y-2 text-xs md:text-sm text-indigo-400/90 font-medium">
    {''.join(toc_items)}
  </ul>
</div>""")

        # TOP5 作品セクション
        for it in items_data:
            r = it["rank"]
            cid = it.get("content_id", "")
            title = it.get("title", "")
            aff_url = it.get("affiliate_url_clean", it.get("affiliateURL", ""))
            pkg_img = it.get("imageURL", {}).get("large", "")
            sample_imgs = get_sample_images(it, 4)
            
            iteminfo = it.get("iteminfo", {})
            actresses = [a.get("name") for a in iteminfo.get("actress", [])]
            genres = [g.get("name") for g in iteminfo.get("genre", [])]
            
            actress_links = " ".join([get_actress_link(a) for a in actresses if a])
            genre_badges = " ".join([get_genre_link(g) for g in genres[:5] if g])
            
            review_text = INDIVIDUAL_REVIEWS.get(cid, "")
            
            # サンプル画像ギャラリー
            sample_gallery = ""
            if sample_imgs:
                img_tags = "".join([f'<img src="{img}" alt="サンプル画像" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />' for img in sample_imgs])
                sample_gallery = f'<div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-6">{img_tags}</div>'

            border_class = "border-2 border-indigo-500/40" if r == 1 else "border border-slate-800"
            badge_class = "bg-gradient-to-r from-indigo-500 to-cyan-400 text-slate-950" if r == 1 else "bg-slate-700 text-indigo-300"
            badge_text = "第1位（殿堂入り）" if r == 1 else f"第{r}位"

            review_html_parts.append(f"""<div id="rank-{r}" class="my-10 bg-slate-900 {border_class} rounded-2xl p-6 md:p-8 shadow-2xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-3">
      <span class="{badge_class} text-sm md:text-base font-black px-4 py-1 rounded-full shadow-lg">{badge_text}</span>
      <h3 class="text-lg md:text-2xl font-black text-white">{title}</h3>
    </div>
    <div class="text-xs text-slate-400">品番：{cid.upper()} / 出演：{actress_links}</div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <div class="space-y-4">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block group relative overflow-hidden rounded-xl border border-slate-700">
        <img src="{pkg_img}" alt="{title}" class="w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-4">
          <span class="text-white text-xs font-bold bg-indigo-600/90 px-3 py-1 rounded-full">FANZA公式で作品詳細を見る →</span>
        </div>
      </a>
      <div class="flex flex-wrap gap-2">
        {genre_badges}
      </div>
    </div>
    <div class="space-y-4 text-xs md:text-sm text-slate-300 leading-relaxed">
      {review_text}
      <div class="pt-2">
        <a href="/posts/{cid}" class="text-xs text-indigo-400 hover:text-indigo-300 underline font-bold">👉 作品個別ページ（サンプル画像・詳細レビュー）を見る</a>
      </div>
    </div>
  </div>

  {sample_gallery}

  <div class="text-center">
    <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-2 bg-gradient-to-r from-indigo-500 via-purple-500 to-indigo-500 hover:opacity-95 text-white font-black text-sm md:text-base px-8 py-4 rounded-xl shadow-xl transition transform hover:scale-105">
      <span>今すぐFANZA公式で『{title[:22]}…』をフル視聴する</span>
      <span>🚀</span>
    </a>
  </div>
</div>""")

        # スペック比較まとめ表
        table_rows = []
        for it in items_data:
            r = it["rank"]
            t = it.get("title", "")
            cid = it.get("content_id", "")
            acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
            act_str = "・".join(acts) if acts else "注目女優"
            
            # 各ジャンルに合わせた特徴テキスト
            attr_text = f"見どころ満載（{cid.upper()}）"
            score_text = "★★★★★ (120%)" if r == 1 else "★★★★★ (110%)"
            
            table_rows.append(f"""      <tr class="hover:bg-slate-800/40">
        <td class="p-3 font-bold text-white">第{r}位：{t[:22]}…</td>
        <td class="p-3">{act_str}</td>
        <td class="p-3">{attr_text}</td>
        <td class="p-3 text-indigo-400 font-bold">{score_text}</td>
        <td class="p-3"><a href="/posts/{cid}" class="text-indigo-400 hover:underline">詳細</a></td>
      </tr>""")

        review_html_parts.append(f"""<!-- スペック比較まとめ表 -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl overflow-x-auto">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>📊</span> おすすめ神作TOP5 徹底スペック比較表
  </h3>
  <table class="w-full text-left text-xs md:text-sm text-slate-300">
    <thead class="bg-slate-800/80 text-indigo-300 uppercase font-bold border-b border-slate-700">
      <tr>
        <th class="p-3">{art['table_headers'][0]}</th>
        <th class="p-3">{art['table_headers'][1]}</th>
        <th class="p-3">{art['table_headers'][2]}</th>
        <th class="p-3">{art['table_headers'][3]}</th>
        <th class="p-3">{art['table_headers'][4]}</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-slate-800">
{''.join(table_rows)}
    </tbody>
  </table>
</div>""")

        # 内部リンク（関連記事）
        rel_links = []
        for r_url, r_title, r_desc in art["related"]:
            rel_links.append(f"""    <a href="{r_url}" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-indigo-500/50 transition block">
      <div class="font-bold text-indigo-300 mb-1">{r_title}</div>
      <p class="text-slate-400 line-clamp-2">{r_desc}</p>
    </a>""")

        review_html_parts.append(f"""<!-- 関連記事・内部リンク -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>🔗</span> あわせて読みたい！おすすめの超人気キラー特集記事
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs md:text-sm">
{''.join(rel_links)}
  </div>
</div>""")

        # よくある質問（FAQ）
        faq_boxes = []
        schema_faqs = []
        for q, a in art["faqs"]:
            faq_boxes.append(f"""    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-indigo-300 mb-2">{q}</h4>
      <p class="text-slate-300 leading-relaxed">{a}</p>
    </div>""")
            schema_faqs.append({
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": a
                }
            })

        review_html_parts.append(f"""<!-- よくある質問（FAQ） -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>❓</span> 本ジャンルに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-4 text-xs md:text-sm">
{''.join(faq_boxes)}
  </div>
</div>""")

        # Schema.org JSON-LD (ItemList + FAQPage)
        schema_items = []
        for it in items_data:
            schema_items.append({
                "@type": "ListItem",
                "position": it["rank"],
                "name": it.get("title", ""),
                "url": f"https://haitoku.pages.dev/posts/{it.get('content_id', '')}",
                "image": it.get("imageURL", {}).get("large", "")
            })
            
        json_ld_data = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "ItemList",
                    "name": art_title,
                    "description": art["lead_p1"],
                    "numberOfItems": len(schema_items),
                    "itemListElement": schema_items
                },
                {
                    "@type": "FAQPage",
                    "mainEntity": schema_faqs
                }
            ]
        }
        
        json_ld_string = json.dumps(json_ld_data, ensure_ascii=False)
        review_html_parts.append(f"""<script type="application/ld+json">
{json_ld_string}
</script>""")

        final_review_html = "\n\n".join(review_html_parts)
        char_count = count_japanese_chars(final_review_html)
        print(f" -> Generated article char count (Japanese without HTML): {char_count} chars")

        post_data = {
            "id": art_id,
            "title": art_title,
            "date": "2026-10-06 00:00:00",
            "hinban": art["hinban"],
            "price": "500~",
            "maker": "FANZA公式セレクション",
            "actresses": all_actresses,
            "genres": art["genres"],
            "image": hero_img,
            "review": final_review_html
        }

        output_path = os.path.join(OUTPUT_DIR, f"{art_id}.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(post_data, f, ensure_ascii=False, indent=2)
        print(f" -> Successfully saved feature post: {output_path}")

    print("\n=== ALL 3 NEW KILLER FEATURES AND INDIVIDUAL POSTS GENERATED! ===")

if __name__ == "__main__":
    main()
