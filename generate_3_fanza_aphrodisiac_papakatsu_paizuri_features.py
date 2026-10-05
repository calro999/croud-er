# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・超大型キラー特集3記事自動生成スクリプト
1. 【媚薬・キメセク・理性崩壊ガンギマリ発情特化】
   『【理性崩壊の肉欲痙攣】FANZA「媚薬・キメセク・ガンギマリ発情」おすすめ神作ランキングTOP5！清楚美女が超強力媚薬で白目を剥いて腰を振り乱す限界潮吹き交尾AV選【2026年最新】』
2. 【パパ活女子・お手当増額生中出し＆プライド崩壊調教特化】
   『【お金の魔力でプライド崩壊】FANZA「パパ活女子・お手当増額生中出し」おすすめ神作ランキングTOP5！小遣い稼ぎの生意気美少女がお手当に負けて生ハメ種付けを受け入れる屈辱快楽AV選【2026年最新】』
3. 【極上パイズリ・巨乳挟まれ窒息射精特化】
   『【神乳に埋もれて昇天】FANZA「極上パイズリ・巨乳挟まれ窒息射精」おすすめ神作ランキングTOP5！たわわな爆乳の谷間に包まれて精子を一滴残らず搾り取られる夢の母性＆快楽AV選【2026年最新】』
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

def fetch_fanza_item(cid, service="digital", floor="videoa"):
    url = "https://api.dmm.com/affiliate/v3/ItemList"
    params = {
        "api_id": API_ID,
        "affiliate_id": API_AFFILIATE_ID,
        "site": "FANZA",
        "service": service,
        "floor": floor,
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

INDIVIDUAL_REVIEWS = {
    "waaa00270": """<h2>『強化合宿中に陸上女子が悪徳コーチに媚薬を盛られて汗だくキメセク大絶頂 末広純』詳細レビュー</h2>
<p>健康美溢れるアスリート・末広純が、信頼する悪徳コーチに媚薬を飲まされ、合宿所で体液まみれの肉欲に沈む衝撃作。陸上仕込みのしなやかな美脚と引き締まった腹筋が、薬の熱でピンク色に染まり、汗を散らしながら快楽の波に呑まれていく姿は圧巻です。</p>

<h3>見どころ：拒絶から自発的な中出し懇願への転落プロセス</h3>
<p>最初はコーチの手を払い除けようとしていた彼女が、下腹部の疼きに抗えなくなり、自らユニフォームを脱ぎ捨てて男根を欲するまでの生々しい心理・肉体変化が見事に描き出されています。瞳が潤み、涎を垂らしながらペニスにしがみつく姿に背徳感が爆発します。</p>

<h3>実用ポイント：激震の連続潮吹き痙攣と荒々しい交尾</h3>
<p>最深部を抉るような激しいピストンが始まると、シーツを水浸しにするほどの激しい潮吹きが連発。全身を弓なりに反らせて白目を剥く極限アクメは、鑑賞者の射精中枢を瞬時にノックアウトする圧倒的な実用度を誇ります。</p>""",

    "midv00314": """<h2>『巨漢部員たちに媚薬を盛られた女子マネージャーが愛液・潮・汗だくアクメ キメセク合宿レ×プ乱交 小野六花』詳細レビュー</h2>
<p>圧倒的な清純派トップ女優・小野六花が、夏合宿中に巨漢部員たちの罠にかかり、媚薬で完全に理性を壊されて輪姦されるメガヒット作。普段は部員を優しくサポートしていた可憐な女子マネージャーが、薬効によって淫乱メス豚へと変貌するギャップが凄まじい破壊力を持ちます。</p>

<h3>見どころ：群がる男根を貪り食うアヘ顔アクメ</h3>
<p>媚薬入りドリンクを飲まされた六花は、全身の火照りに耐えきれず、自ら股間を押さえてよがり始めます。突き出された何本ものペニスに涎を垂らしてしゃぶりつき、次々と挿入される激ピストンに歓喜の悲鳴を上げ続ける姿はまさに圧巻です。</p>

<h3>実用ポイント：交代で注ぎ込まれる濃厚種付けピストン</h3>
<p>次々に男が入れ替わり、容赦なく膣内に精液を注ぎ込まれてもなお「もっと奥まで突いてぇ！」と腰を振る六花の姿は実用度120％。純情少女が肉欲の極限に達するカタルシスを余すところなく味わえます。</p>""",

    "miaa00680": """<h2>『スレンダー連れ子を媚薬オイル調教 体液（涎・愛液・潮）噴出イキまくり肉便器堕ち 東條なつ』詳細レビュー</h2>
<p>モデル級の美貌とスレンダー美ボディを誇る東條なつが、義父の手によって媚薬オイルで全身を調教され、体液垂れ流しの快楽人形へと作り変えられる傑作。反抗的な態度をとっていた美少女が、肌から浸透する薬の力で次第に雌の顔になっていく過程が艶やかに描かれます。</p>

<h3>見どころ：オイルに濡れる美肌と痙攣する腰つき</h3>
<p>乳首や秘部に丹念に塗り込まれる媚薬オイル。指先で愛撫されるたびに背中を跳ね上げ、東條なつの透き通るような白い肌がピンクに染まります。スレンダーな肢体がビクビクと震え、自ら快楽を求めて腰をくねらせるシーンはフェティシズムの極致です。</p>

<h3>実用ポイント：感度激増アソコへの深突き生ハメ</h3>
<p>完全に感度が狂った肉穴にペニスをズブズブと押し込むと、東條なつは涙目で「お父さん…そこ凄い…！」とすがりつきます。子宮口を激しくノックされるたびに噴き出す愛液と潮の臨場感は、見る者を一瞬で絶頂へと導きます。</p>""",

    "mida00527": """<h2>『笑わない少女が悪徳エステに騙されて…媚薬オイルで恥部をほぐされ崩壊失禁アクメ 快楽マッサージ沼に堕ちた無表情美少女 望月円』詳細レビュー</h2>
<p>クールな眼差しとミステリアスな魅力を持つ望月円が、無料体験のエステで悪徳施術師に特製媚薬オイルを塗りたくられ、恥部を執拗に攻められて失禁アクメに溺れる名作。感情を表に出さなかった美少女が快楽で崩壊していく過程が男の本能を直撃します。</p>

<h3>見どころ：無表情の崩壊と恥じらいの喪失</h3>
<p>「くすぐったいだけです…」と強がっていた彼女が、熱を帯びた媚薬オイルの浸透とともに荒い息を吐き始めます。目元を紅潮させ、恥部をまさぐられるたびに小さく漏れ出る甘い喘ぎ声のギャップがたまりません。</p>

<h3>実用ポイント：我慢しきれず漏れ出る大量失禁と貪り交尾</h3>
<p>極限まで高まった快感に耐えきれず、ついに恥じらいを捨てて大量失禁＆潮吹きのアクメへ到達。その後、施術師のペニスを自ら求めて跨がり、無我夢中で腰を振る望月円の姿は、実用派ファン垂涎の抜きどころです。</p>""",

    "homa00162": """<h2>『SNSで拾った家出少女を媚薬キメセク漬け 絶倫チ○ポが満足するまで中出しできる肉便器に仕上げた 日向由奈』詳細レビュー</h2>
<p>リアルな危うさと愛らしさを漂わせる日向由奈が、家出中に怪しい男に拾われ、密室で媚薬を与えられ続けて快楽漬けにされる調教サスペンス作。現代の闇とエロスが生々しく交錯し、独特の緊張感と背徳感を醸し出しています。</p>

<h3>見どころ：薬効でフワフワとトリップする無防備ボディ</h3>
<p>水に溶かされた媚薬を飲み干した由奈は、数十分後には下半身の強烈な疼きに悶え始めます。焦点の合わない瞳で男を見つめ、身体を擦り寄せてくる姿は、男の保護欲と支配欲を限界まで煽り立てます。</p>

<h3>実用ポイント：朝から晩まで注ぎ込まれる容赦なき中出し</h3>
<p>媚薬が効き続ける中、男の逞しいチ○ポを何度も何度も奥深くまで挿入される由奈。完全に服従し、「もっと出して…」と種付けをねだるアヘ顔は実用度抜群。背徳感にまみれた濃厚プレイを堪能できます。</p>""",

    "1stars00693": """<h2>『パパ活で絶倫おじさんとホテルで一日中滅茶苦茶に中出しされています。 青空ひかり』詳細レビュー</h2>
<p>トップアイドル級の美貌と愛嬌を誇る青空ひかりが、小遣い稼ぎで始めたパパ活で絶倫オジサンと遭遇し、高級ホテルで一日中休む間もなく生中出しされ続ける大ヒット作。パパ活女子の気軽なノリが、圧倒的な肉欲の嵐に巻き込まれていく展開が最高にエロティックです。</p>

<h3>見どころ：逃げ場のない密室で削られるプライド</h3>
<p>「買い物行くから早くして」と言っていたひかりちゃんが、おじさんの太く逞しいペニスに貫かれた途端、声にならない喘ぎ声を漏らします。何発出しても衰えないおじさんの精力に圧倒され、次第にベッドの上でぐったりと快楽に身を委ねていく姿がソソります。</p>

<h3>実用ポイント：体位を変えながら繰り返される濃厚種付け</h3>
<p>正常位で奥深くまで突き入れられ、バックで美尻を叩きつけられ、対面座位で密着しながら子宮に注ぎ込まれる大量の精液。青空ひかりの可愛い顔が快感に蕩け、完全にメスの顔になっていく様は、全男子必見の神シーンです。</p>""",

    "fpre00124": """<h2>『パパを夢中にさせる港区女子の密着ベロ舐めテクニック 長身巨乳美女らんの場合 菊乃らん』詳細レビュー</h2>
<p>スラリとした高身長と豊かな美巨乳を兼ね備えた港区美女・菊乃らんが、金持ちパパを骨抜きにする極上のおねだりテクニックと密着愛撫を繰り広げる作品。洗練された大人の色香と、ベッドで見せる淫らな本性のコントラストが抜群です。</p>

<h3>見どころ：全身を溶かす長い舌の密着ベロ舐め</h3>
<p>耳元への甘い囁きから始まり、首筋、胸元、そして股間へと舌を這わせていく菊乃らん。男の弱点を熟知した巧みな舌使いと、豊満な胸を押し当ててくるスキンシップは、鑑賞者の理性を一瞬で溶かします。</p>

<h3>実用ポイント：パパを喜ばせる極上騎乗位と生ハメ</h3>
<p>ベッドに押し倒したパパの上に跨がり、自慢の美巨乳を揺らしながら腰をくねらせる菊乃らん。快楽が高まるにつれて余裕の表情が消え、「パパのおちんぽ気持ちいい…！」と本気でイキ狂う姿は圧巻の実用度を誇ります。</p>""",

    "ebod00845": """<h2>『激むちHcup卑猥ボディどすけべ制服女子のパパ活バイトはレベチ 香坂紗梨』詳細レビュー</h2>
<p>重量感あふれる天然Hカップと豊満な肉感ボディを持つ香坂紗梨が、制服姿でパパ活のアルバイトに精を出す肉弾エロス満載の作品。制服のボタンを押し広げるような巨乳と、短いスカートから覗くむっちり太ももが男の本能を刺激します。</p>

<h3>見どころ：爆乳パイズリと惜しげもない肉体密着</h3>
<p>初対面のおじさんに対しても物怖じせず、自慢のHカップでペニスをすっぽり挟み込む香坂紗梨。柔らかく温かな胸の感触と、上目遣いで微笑みかけてくる無邪気なエロさがたまらなく魅力的です。</p>

<h3>実用ポイント：肉がぶつかり合う激しいバックピストン</h3>
<p>四つん這いにさせてむっちりしたお尻を背後から激しく突くバックシーンは迫力満点。肉と肉が衝突する生々しい音とともに、たわわな胸が激しく波打ちます。生中出しの快感に酔いしれる姿は巨乳好き必見です。</p>""",

    "mkmp00656": """<h2>『乳首が弱点のパパ活女子を強●チクイキ。オジを馬鹿にする塩対応な女子校生が執拗な乳首責めで屈服させられイキ狂う 柏木こなつ』詳細レビュー</h2>
<p>生意気なツンツン態度が可愛い柏木こなつが、オジサンを見下す塩対応パパ活女子を演じる屈服快楽モノ。ホテルに入ってもスマホを見ながら冷たくあしらっていた彼女が、超敏感な乳首を執拗に攻められてプライドを砕かれていきます。</p>

<h3>見どころ：塩対応からのチクイキ絶叫ギャップ</h3>
<p>服の上から、そして直接コリコリと弄ばれる乳首。最初は「やめてよ」と嫌がっていたこなつが、次第に呼吸を荒げ、乳首を吸われるだけで背中を反らせて喘ぎ始める変化が最高に興奮を誘います。</p>

<h3>実用ポイント：涙目で快楽に屈服する中出し交尾</h3>
<p>乳首責めで何度もイカされた彼女は、完全に抵抗力を失ってオジサンの逞しいペニスを受け入れます。「何でも言うこと聞くから…！」とすがりつきながら中出しされる姿は、男の征服欲を極限まで満たしてくれます。</p>""",

    "mdbk00358": """<h2>『絶対領域のチラリズムでギンギンになったチ●ポを美脚エロテクで射精に導く美女パパ活OL 森日向子 都月るいさ Nia』詳細レビュー</h2>
<p>抜群のプロポーションを誇る森日向子、都月るいさ、Niaの3大美女が、裏のパパ活でオジサンたちを美脚エロテクニックで翻弄する超豪華作。タイトスカートとストッキングの隙間から覗く絶対領域が男の視線を釘付けにします。</p>

<h3>見どころ：3者3様の美脚責めと濃厚密着プレイ</h3>
<p>ストッキング越しの足コキや、太ももでペニスを挟み込む巧みな愛撫。オフィスライクな衣装を身に纏った美女たちが、至近距離で囁きながら男の精力を根こそぎ奪い取ろうとする姿は目の保養そのものです。</p>

<h3>実用ポイント：美脚に囲まれて迎える連続射精</h3>
<p>限界まで勃起させられた後、それぞれの美女たちと繰り広げる濃厚なピストン運動。しなやかな生足に絡みつかれながら、奥深くまで突き刺して果てる瞬間は、美脚フェチにとって至高の快楽をもたらします。</p>""",

    "sone00912": """<h2>『最強ヒロインのパイズリ挟射 瀬戸環奈』詳細レビュー</h2>
<p>神がかった美貌と透明感を誇るトップ女優・瀬戸環奈が、パーフェクトな極上バストで男のペニスを挟み込み、丁寧にしごき上げるパイズリ特化の最高峰傑作。吸い込まれそうな瞳と、柔らかく温かな胸の感触が融合した奇跡の1本です。</p>

<h3>見どころ：両手で寄せ集められる美乳と上目遣い</h3>
<p>ローションを馴染ませた豊かな胸でペニスを包み込み、先端をチラリと覗かせながら擦り上げる瀬戸環奈。至近距離から「環奈のおっぱいでイッて…？」と囁かれる破壊力は、男の理性を瞬時に焼き切ります。</p>

<h3>実用ポイント：胸の谷間へのダイレクト射精と追撃搾精</h3>
<p>我慢できずに勢いよく発射された精液を、谷間いっぱいに受け止めながら最後まで優しく搾り取ってくれるフィニッシュ。美少女フェチも巨乳好きも大満足間違いなしの実用度100%作品です。</p>""",

    "mide00634": """<h2>『30本のチ○ポを抜きまくるパイズリ大乱交 水卜さくら』詳細レビュー</h2>
<p>究極の童顔フェイスと爆発的Gカップを併せ持つ水卜さくらが、次々と押し寄せる男たちのペニスをひたすらパイズリだけで射精させ続ける伝説の企画モノ。小さく華奢な体躯に実った豊満バストが縦横無尽に揺れ動きます。</p>

<h3>見どころ：嫌な顔一つせず男根を包み込む聖母の包容力</h3>
<p>何本もの逞しいペニスが迫る中、笑顔で愛おしそうにおっぱいで迎え入れるさくらちゃん。たわわな胸の弾力と滑らかな肌触りで、男たちを次々と昇天させていく姿はまさに圧巻です。</p>

<h3>実用ポイント：胸元が精子で真っ白に染まる連続発射</h3>
<p>休む間もなく繰り返される胸元への大量射精。谷間や首筋まで白濁液まみれになりながらも、次の男棒を挟んでしごき続ける姿は実用度MAX。爆乳パイズリの歴史に残る金字塔です。</p>""",

    "ssni00347": """<h2>『世話焼き職業女子の献身的な超密着おっぱい尽くし 夢乃あいか』詳細レビュー</h2>
<p>爆乳界の絶対的女王・夢乃あいかが、看護師や家政婦などの世話焼き女子に扮し、服の上からでも溢れ出るド迫力バストを全身で密着させて男を癒やし尽くす大人気作。圧倒的な母性と包容力に包まれる夢のような体験が味わえます。</p>

<h3>見どころ：顔が埋もれるほどの豊満バスト密着</h3>
<p>ベッドに横たわる男の上に乗り、巨大な胸を顔や身体に押し当ててくる夢乃あいか。息が詰まるほどの柔らかさと、甘い香りに包まれる至福の時間は、日頃の疲れを一瞬で消し去ってくれます。</p>

<h3>実用ポイント：すっぽり包み込まれる極上パイズリ</h3>
<p>ペニスが完全に見えなくなるほど豊かな胸で覆い隠し、優しくリズミカルに擦り上げるパイズリ。「いっぱい出していいんだよ…」と囁かれながら昇天を迎えるカタルシスは別格です。</p>""",

    "pppe00071": """<h2>『一度射精してもおっぱい密着挟み撃ちで追撃丁寧にヌイてくれる W巨乳回春エステ 蜜美杏 百永さりな』詳細レビュー</h2>
<p>圧巻のダイナマイトボディを誇る蜜美杏と百永さりなという、巨乳界の二大巨頭が同時に施術を担当する夢の回春エステ作。左右から巨大なバストで同時に挟み撃ちにされる贅沢極まりないシチュエーションです。</p>

<h3>見どころ：W爆乳サンドイッチによる窒息寸前プレイ</h3>
<p>男のペニスを二人の巨大な胸で挟み込み、互いの肌を擦り合わせながら責め立てるWパイズリ。前からも横からも押し寄せる圧倒的な肉感に、男の理性は一瞬で崩壊します。</p>

<h3>実用ポイント：賢者タイムを許さない連続追撃搾精</h3>
<p>1発目を射精してぐったりしたペニスに対しても、二人は微笑みながらおっぱい責めを継続。敏感になった先端を柔らかく包み込み、2発目、3発目と精子を吸い出していく破壊力は悶絶必至です。</p>""",

    "mide00839": """<h2>『彼女のお姉ちゃんにノーブラ巨乳でこっそり誘惑されちゃったボク 中山ふみか』詳細レビュー</h2>
<p>重量級の迫力美乳と妖艶な色香を持つ中山ふみかが、妹の留守中に彼女の部屋で彼氏をノーブラ部屋着で誘惑する背徳の名作。薄い生地からくっきりと浮かぶ胸の丸みと、耳元への囁きが男の本能を狂わせます。</p>

<h3>見どころ：ノーブラ胸チラからの略奪アプローチ</h3>
<p>妹には内緒という密室のスリルの中、無防備に胸元をはだけさせて男のペニスに触れてくる中山ふみか。豊満な胸で肉棒を挟み込み、妖しく微笑みながら腰を寄せてくる姿は背徳の極みです。</p>

<h3>実用ポイント：重量感あふれるパイズリとそのまま跨がり騎乗位</h3>
<p>ずっしりとした重みのあるバストで上下にしごき上げられた後、我慢できずに自ら跨がって肉棒を奥深くまで飲み込むふみか。胸を激しく揺らしながらイキ乱れるシーンは巨乳好き必見の破壊力です。</p>"""
}

def generate_individual_post_if_needed(it, special_labels=None):
    cid = it.get("content_id")
    if not cid:
        return
    file_path = os.path.join(OUTPUT_DIR, f"{cid}.json")
    if os.path.exists(file_path):
        return
    
    title = it.get("title", "")
    acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
    genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
    maker = it.get("iteminfo", {}).get("maker", [{}])[0].get("name", "")
    price = it.get("prices", {}).get("price", "300~")
    date_str = it.get("date", "2024-01-01 10:00:00")
    img = it.get("imageURL", {}).get("large", "")
    aff_url = it.get("affiliate_url_clean", "")
    sample_movie = f"https://www.dmm.com/litevideo/-/part/=/cid={cid}/size=720_480/affi_id={LINK_AFFILIATE_ID}/"
    
    samples = []
    s_data = it.get("sampleImageURL", {})
    if "sample_l" in s_data:
        samples = s_data["sample_l"].get("image", [])
    elif "sample_m" in s_data:
        samples = s_data["sample_m"].get("image", [])
    if isinstance(samples, str):
        samples = [samples]
        
    act_str = "・".join(acts) if acts else "トップ女優"
    
    review_html = INDIVIDUAL_REVIEWS.get(cid)
    if not review_html:
        review_html = f"""<h2>『{title}』詳細レビュー・作品の見どころ</h2>
<p>本作は、{act_str}が渾身の熱演を見せ、作品の世界観と圧倒的な官能エロティシズムが最高潮に達した傑作です。</p>
<h3>主演キャスト（{act_str}）の熱演と見どころ</h3>
<p>{act_str}が見せる生々しい表情と、快楽に蕩けていく視線の移り変わりは圧巻。肌が擦れ合うたびに漏れ出る熱い吐息と、欲望を抑えきれずに震える肉体のリアルさが画面越しにダイレクトに伝わります。</p>
<h3>実用ポイント・結合と絶頂の臨場感</h3>
<p>クライマックスで繰り広げられる濃厚なピストン運動と、奥深くまで突き刺さる結合描写は破壊力抜群。反響する水音と喘ぎ声が五感を強く刺激し、一瞬で限界射精へと導いてくれます。</p>
<h3>総評・おすすめの鑑賞スタイル</h3>
<p>設定の緻密さとエロスの爆発力が高次元で調和した必見作。じっくりと腰を据えて没入したい夜に自信を持っておすすめできる一本です。</p>"""

    data = {
        "id": cid,
        "hinban": f"{cid.upper()}",
        "title": title,
        "review": review_html,
        "image": img,
        "sample_movie_url": sample_movie,
        "sample_images": samples[:20],
        "affiliate_url": aff_url,
        "genres": genres[:10],
        "actresses": acts,
        "directors": [],
        "maker": maker,
        "price": price,
        "date": date_str,
        "labels": special_labels or ["殿堂入り", "話題作", "おすすめ"]
    }
    with open(file_path, "w", encoding="utf-8") as out_f:
        json.dump(data, out_f, ensure_ascii=False, indent=2)
    print(f" -> Generated individual post: {cid}")


# ==============================================================================
# 記事1: 媚薬・キメセク・理性崩壊ガンギマリ発情 特化
# ==============================================================================
def generate_article_aphrodisiac():
    print("=== Generating Article 1: 媚薬・キメセク・理性崩壊ガンギマリ発情特化 ===")
    cids = ["waaa00270", "midv00314", "miaa00680", "mida00527", "homa00162"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["媚薬", "キメセク", "ガンギマリ", "潮吹き", "痙攣", "殿堂入り"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 1 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-rose-950/40 via-slate-900 to-slate-950 border border-rose-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-rose-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-rose-500/20 text-rose-300 border border-rose-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">APHRODISIAC ECSTASY SPECIAL</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月05日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【理性崩壊の肉欲痙攣】FANZA「媚薬・キメセク・ガンギマリ発情」おすすめ神作ランキングTOP5！清楚美女が超強力媚薬で白目を剥いて腰を振り乱す限界潮吹き交尾AV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    普段は凛とした表情を崩さない清楚な美少女や、プライド高く男を寄せ付けない美女。そんな高嶺の花が、一口飲まされた超強力媚薬によって体温を急上昇させ、下腹部の疼きに耐えきれず理性も羞恥心もすべて焼き切られてしまったら――。男の破壊的欲望とサディスティックな征服欲を極限まで満たす禁断のジャンル、それが「媚薬・キメセク発情モノ」です。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    毛穴という毛穴から吹き出す汗、火照りきって紅潮した肌、そして焦点の合わないトロンとした瞳。触れられただけでビクンと背中を跳ね上げ、自ら股間を押し付けて「お願い…早く挿れて…頭がおかしくなっちゃう！」と涎を垂らしながら懇願してくる姿は、全AVジャンルの中でも抜きん出た破壊的な中毒性を誇ります。普段との落差が大きければ大きいほど、媚薬で完全にメス豚化してしまった瞬間の射精快感は桁違いです。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、末広純が合宿先で悪徳コーチに媚薬を盛られて汗だく潮吹き痙攣する伝説作から、小野六花の女子マネージャー媚薬乱交、東條なつの媚薬オイル調教肉便器堕ち、望月円の無表情美少女が崩壊失禁アクメに溺れるエステ罠、日向由奈の家出少女キメセク漬けまで、実用度・狂乱度ともに頂点を極めた【媚薬キメセク神作TOP5】を徹底解説します。
  </p>
</div>

<!-- 選び方の基準 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-rose-400">🧪</span> 媚薬・キメセクモノで脳が溶けるほどの射精を迎える3大チェックポイント
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-rose-300 mb-2">① 拒絶から発情へ…理性が溶け落ちるグラデーション</h4>
      <p class="text-slate-300 leading-relaxed">「何か変な薬入れたの…？やめて！」と抵抗していた瞳が、徐々に潤んでトロ顔へと崩れ落ち、自ら指を秘部に突っ込んで愛液を掻き回し始める変貌プロセスこそが最大の醍醐味です。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-rose-300 mb-2">② 汗・涎・愛液・潮…体液まみれの肉体痙攣</h4>
      <p class="text-slate-300 leading-relaxed">薬効で全身の神経が極限まで過敏化し、亀頭が子宮口に触れただけでビクビクと全身を硬直させて噴水のような潮吹きを連発する生々しい肉体反応が興奮を沸点まで押し上げます。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-rose-300 mb-2">③ プライド崩壊！ガンギマリ中出し懇願</h4>
      <p class="text-slate-300 leading-relaxed">羞恥心を完全に喪失し、白目を剥いて舌を出しながら「中に出してぇ！種付けしてぇ！」と叫び散らすアヘ顔アクメ。男の征服欲が120%満たされる最高の瞬間です。</p>
    </div>
  </div>
</div>"""
    html_parts.append(intro_html)

    reviews_data = {
        "waaa00270": {
            "desc": """<h4>【作品解説・見どころ】末広純が魅せる鬼気迫る狂乱アクメ！悪徳コーチに媚薬を盛られた合宿の悪夢</h4>
<p>スラリと伸びた美脚と引き締まったしなやかな筋肉美を誇る陸上美女・末広純が、信頼していた悪徳コーチに超強力媚薬をドリンクに混入され、汗だくの肉欲地獄へと叩き落とされる戦慄の傑作。薬が回り始めた彼女は、息を荒げながら太ももを擦り合わせ、次第にコーチの男根を欲して自らユニフォームを脱ぎ捨てます。健康的なアスリート美女の誇りが、抗えない薬の熱によって無残にも解け去っていく過程が凄まじい緊迫感を生み出しています。</p>
<h4>【実用ポイント】全身汗だくの連続潮吹き痙攣と休みなき狂乱ピストン</h4>
<p>ペニスが膣内にめり込んだ瞬間、末広純は絶叫とともに背中を弓なりに反らせ、ベッド一面を水浸しにするほどの激しい潮吹きを炸裂させます。コーチに腰を掴まれ、獣のような荒いピストンで最深部を抉られるたびに、白目を剥きかけて痙攣を繰り返す肉体の生々しさは圧巻。汗と愛液でドロドロになりながら、何度も何度も射精を要求してくる姿は、鑑賞者の理性を一瞬で粉砕します。</p>""",
            "rating": "★★★★★ 5.0 / 5.0",
            "service_score": "ガンギマリ度: 100% | 潮吹き痙攣度: 100% | 実用性: 100%"
        },
        "midv00314": {
            "desc": """<h4>【作品解説・見どころ】小野六花の美少女マネージャーが媚薬乱交で堕ちる！巨漢部員たちによる輪姦交尾</h4>
<p>圧倒的透明感と国民的妹のような愛らしさで不動の人気を誇る小野六花が、夏合宿中に巨漢部員たちの罠にかかり、媚薬漬けにされて輪姦される衝撃作。普段は部員たちを甲斐甲斐しく支えていた健気な彼女が、媚薬入りのスポーツドリンクを口にした途端、全身がピンク色に染まり、自ら股間を押さえてよがり始めます。普段の清純なイメージとの強烈なギャップが、男の征服欲を激しく刺激します。</p>
<h4>【実用ポイント】次々と群がる男根をしゃぶり尽くし、中出しをねだるアヘ顔</h4>
<p>完全に理性を奪われた六花は、次々と突き出される巨根に群がり、涎を垂らしながら夢中で貪りしゃぶりつきます。交代で挿入される激ピストンに対し、嫌がるどころか腰を浮かせて奥深くへと迎え入れ、「もっと…もっと奥まで突いてぇ！」と叫び声を上げてイキ狂う姿は壮絶の極み。純情美少女が肉便器として覚醒する瞬間の抜きやすさは別格です。</p>""",
            "rating": "★★★★★ 4.9 / 5.0",
            "service_score": "背徳輪姦度: 100% | 理性崩壊度: 99% | 実用性: 100%"
        },
        "miaa00680": {
            "desc": """<h4>【作品解説・見どころ】東條なつのスレンダー美ボディが媚薬オイルで覚醒！義父の調教に堕ちる連れ子</h4>
<p>モデル級の極上プロポーションと透き通るような白肌を持つ東條なつが、義理の父親に媚薬成分入りの特製アロマオイルで全身をマッサージされ、体液垂れ流しの快楽人形へと作り変えられる背徳作。最初は反抗的な態度で睨みつけていた彼女が、乳首や秘部にオイルを塗り込まれるにつれて息遣いが荒くなり、ビクビクと腰を揺らし始めます。スレンダーな肢体が快楽の激震に打ち震える様は息を呑むエロティシズムです。</p>
<h4>【実用ポイント】涎・愛液・潮の三重奏！感度300倍の肉穴に沈む生チ○ポ</h4>
<p>媚薬オイルが皮膚から浸透し、指先でクリトリスを転がされただけで噴水のように潮を吹き出す東條なつ。もはや義父への憎しみは消え失せ、「お父さん…そこ気持ちいい…壊れちゃう…！」とすがりつく姿は男のサディズムを限界まで満たします。奥深くまで生ハメされ、子宮口を激しくノックされるたびに口から涎を垂らして昇天する濃密シーンは必見です。</p>""",
            "rating": "★★★★★ 4.9 / 5.0",
            "service_score": "オイル調教度: 100% | スレンダー肉感: 99% | 実用性: 99%"
        },
        "mida00527": {
            "desc": """<h4>【作品解説・見どころ】望月円のクールな無表情が崩壊！悪徳エステの媚薬オイルで失禁アクメ沼へ</h4>
<p>何を考えているか読めないミステリアスな美貌とクールな眼差しが魅力の望月円が、無料体験と称する悪徳エステサロンに誘い込まれ、極悪媚薬オイルで無理やりイカされまくる問題作。「痛いマッサージは嫌なんですけど…」と淡々と話していた少女が、施術師の巧みな指使いと熱い媚薬オイルの浸透によって、徐々に目元を潤ませていきます。表情を崩さなかったクールビューティーが快楽に耐えかねて悶える姿は最高にソソります。</p>
<h4>【実用ポイント】恥じらいを忘れさせる猛烈な愛撫と連続中出しの破壊力</h4>
<p>薬効によって下腹部が燃え盛るように熱くなり、秘部を念入りに捏ね回された望月円は、ついに我慢の限界を迎えて大量失禁＆潮吹きのアクメへ到達。「やだ…出ちゃう…止まらない…！」と泣き叫びながら、施術師の逞しいペニスに跨がり、自ら夢中で腰を振る様は圧巻。無表情美少女が完全なド淫乱へと変貌する奇跡のドラマです。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "ギャップ崩壊度: 100% | 失禁潮吹き度: 98% | 実用性: 98%"
        },
        "homa00162": {
            "desc": """<h4>【作品解説・見どころ】日向由奈の家出少女を拾ってキメセク漬け！絶倫チ○ポで飼い慣らす肉便器化記録</h4>
<p>どこか影のある美少女・日向由奈が、家出して途方に暮れていたところを怪しい男に拾われ、部屋に閉じ込められて媚薬を飲まされ続ける狂気の調教モノ。行く当てのない彼女は、男に差し出された水を疑いもせずに飲み干し、数十分後には下半身の猛烈な疼きにのたうち回ることになります。現代的な闇を感じさせるリアルな設定と、日向由奈の鬼気迫る喘ぎが男の下半身を直撃します。</p>
<h4>【実用ポイント】昼夜を問わず繰り返される生中出しと完全服従の快楽漬け</h4>
<p>媚薬が切れる前に次の薬を与えられ、常に頭がフワフワとトリップした状態でチ○ポを挿れられ続ける由奈。「もうこれなしじゃ生きられない…」と男の腰にしがみつき、精液を欲して自分からアソコを開いて見せるシーンは実用度の塊です。完全に調教されきった少女の膣内に熱い種付けを繰り返す背徳感に、思わず腰が砕けます。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "監禁調教度: 99% | キメセク中毒性: 99% | 実用性: 98%"
        }
    }

    for idx, it in enumerate(items):
        cid = it.get("content_id")
        title = it.get("title")
        aff_url = it.get("affiliate_url_clean")
        large_img = it.get("imageURL", {}).get("large", "")
        acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        act_html = " ".join([get_actress_link(a) for a in acts])
        genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        genre_html = " ".join([get_genre_link(g) for g in genres[:6]])
        sample_imgs = get_sample_images(it, 4)
        c_data = reviews_data.get(cid, {})

        sample_imgs_html = ""
        if sample_imgs:
            img_tags = "".join([f'<img src="{sim}" alt="{title} サンプル{s_idx+1}" class="w-full h-28 object-cover rounded-lg border border-slate-700/80 hover:scale-105 transition transform duration-300" loading="lazy" />' for s_idx, sim in enumerate(sample_imgs)])
            sample_imgs_html = f'<div class="grid grid-cols-2 md:grid-cols-4 gap-2 my-4">{img_tags}</div>'

        item_block = f"""
<div class="my-10 bg-slate-900/90 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-2xl relative">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-2">
      <span class="bg-rose-600 text-white font-black text-sm px-3 py-1 rounded-lg">第{idx+1}位</span>
      <span class="text-xs text-slate-400 font-mono tracking-wider">品番: {cid.upper()}</span>
    </div>
    <div class="text-amber-400 font-black text-sm tracking-wide">{c_data.get('rating', '★★★★★ 5.0 / 5.0')}</div>
  </div>

  <h3 class="text-xl md:text-2xl font-black text-white leading-snug mb-4 hover:text-rose-400 transition">
    <a href="{aff_url}" target="_blank" rel="nofollow noopener">{title}</a>
  </h3>

  <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-start">
    <div class="md:col-span-5">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block group overflow-hidden rounded-xl border border-slate-700/80 shadow-lg relative">
        <img src="{large_img}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition duration-300 flex items-end p-4">
          <span class="bg-rose-600 text-white font-bold text-xs px-3 py-1.5 rounded-full shadow-lg">FANZA公式で今すぐ無料サンプル再生 ▶</span>
        </div>
      </a>
      <div class="mt-3 text-xs bg-slate-800/60 p-2.5 rounded-lg border border-slate-700/50 text-slate-300">
        <div class="mb-1"><span class="text-slate-400">主演女優:</span> {act_html or "人気トップキャスト"}</div>
        <div><span class="text-slate-400">スペック評価:</span> <span class="text-rose-300 font-medium">{c_data.get('service_score', '実用度特化')}</span></div>
      </div>
    </div>

    <div class="md:col-span-7 space-y-4 text-slate-300 text-sm md:text-base leading-relaxed">
      {c_data.get('desc', '')}
      
      <div class="pt-2">
        <div class="text-xs text-slate-400 mb-2 font-medium">関連ジャンルタグ:</div>
        <div class="flex flex-wrap gap-1.5">{genre_html}</div>
      </div>
    </div>
  </div>

  {sample_imgs_html}

  <div class="mt-6 flex flex-col sm:flex-row items-center justify-between gap-4 bg-slate-950/80 p-4 rounded-xl border border-slate-800">
    <div class="text-xs text-slate-400">
      高画質ストリーミング／ダウンロード対応・スマホ即時視聴可能
    </div>
    <div class="flex items-center gap-3 w-full sm:w-auto">
      <a href="/posts/{cid}" class="text-center px-4 py-2.5 rounded-xl border border-slate-700 text-slate-300 hover:text-white hover:bg-slate-800 text-xs font-bold transition w-1/2 sm:w-auto">
        詳細個別レビューを見る
      </a>
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="text-center bg-gradient-to-r from-rose-600 to-pink-600 hover:from-rose-500 hover:to-pink-500 text-white text-sm font-black px-6 py-2.5 rounded-xl shadow-lg shadow-rose-900/40 hover:shadow-rose-800/60 transition transform hover:-translate-y-0.5 w-1/2 sm:w-auto">
        FANZA公式で今すぐ本編を見る ▶
      </a>
    </div>
  </div>
</div>"""
        html_parts.append(item_block)

    # 比較まとめテーブル & 関連特集リンク
    table_and_links = f"""
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-rose-400">📊</span> 【徹底比較】媚薬・キメセク神作TOP5 スペック一覧表
  </h3>
  <div class="overflow-x-auto">
    <table class="w-full text-left text-xs md:text-sm text-slate-300">
      <thead class="bg-slate-800/80 text-slate-200">
        <tr>
          <th class="p-3">順位</th>
          <th class="p-3">作品タイトル</th>
          <th class="p-3">主演キャスト</th>
          <th class="p-3">特化属性</th>
          <th class="p-3">実用評価</th>
          <th class="p-3 text-center">公式リンク</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800">
        <tr class="hover:bg-slate-800/40 transition">
          <td class="p-3 font-bold text-rose-400">第1位</td>
          <td class="p-3 font-medium text-white">{items[0].get('title')[:32]}...</td>
          <td class="p-3">末広純</td>
          <td class="p-3">合宿媚薬・汗だく潮吹き痙攣</td>
          <td class="p-3 text-amber-400">★★★★★ 5.0</td>
          <td class="p-3 text-center"><a href="{items[0].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-rose-400 hover:underline font-bold">作品を見る</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40 transition">
          <td class="p-3 font-bold text-rose-400">第2位</td>
          <td class="p-3 font-medium text-white">{items[1].get('title')[:32]}...</td>
          <td class="p-3">小野六花</td>
          <td class="p-3">マネージャー媚薬乱交輪姦</td>
          <td class="p-3 text-amber-400">★★★★★ 4.9</td>
          <td class="p-3 text-center"><a href="{items[1].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-rose-400 hover:underline font-bold">作品を見る</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40 transition">
          <td class="p-3 font-bold text-rose-400">第3位</td>
          <td class="p-3 font-medium text-white">{items[2].get('title')[:32]}...</td>
          <td class="p-3">東條なつ</td>
          <td class="p-3">媚薬オイル・体液噴出肉便器</td>
          <td class="p-3 text-amber-400">★★★★★ 4.9</td>
          <td class="p-3 text-center"><a href="{items[2].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-rose-400 hover:underline font-bold">作品を見る</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40 transition">
          <td class="p-3 font-bold text-rose-400">第4位</td>
          <td class="p-3 font-medium text-white">{items[3].get('title')[:32]}...</td>
          <td class="p-3">望月円</td>
          <td class="p-3">悪徳エステ・無表情崩壊失禁</td>
          <td class="p-3 text-amber-400">★★★★★ 4.8</td>
          <td class="p-3 text-center"><a href="{items[3].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-rose-400 hover:underline font-bold">作品を見る</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40 transition">
          <td class="p-3 font-bold text-rose-400">第5位</td>
          <td class="p-3 font-medium text-white">{items[4].get('title')[:32]}...</td>
          <td class="p-3">日向由奈</td>
          <td class="p-3">家出少女・キメセク漬け服従</td>
          <td class="p-3 text-amber-400">★★★★★ 4.8</td>
          <td class="p-3 text-center"><a href="{items[4].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-rose-400 hover:underline font-bold">作品を見る</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- 内部リンク：あわせて読みたい関連特集 -->
<div class="my-10 bg-slate-900/60 border border-slate-800 rounded-2xl p-6 md:p-8">
  <h3 class="text-lg font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-rose-400">🔥</span> あわせてチェックしたい！背徳・快楽特化の人気特集
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-sm">
    <a href="/posts/feature_fanza_endure_super_technique_raw_creampie_ranking_2026" class="p-3.5 bg-slate-800/80 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-rose-500/50 transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-rose-300 font-medium">【凄テク我慢・生中出し特化】耐え抜いたらご褒美生中出しAV厳選</span>
      <span class="text-rose-400 group-hover:translate-x-1 transition">→</span>
    </a>
    <a href="/posts/feature_fanza_missed_last_train_roomwear_sleepover_ranking_2026" class="p-3.5 bg-slate-800/80 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-rose-500/50 transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-rose-300 font-medium">【終電逃し・無防備部屋着特化】すっぴんノーブラ生中出しAV厳選</span>
      <span class="text-rose-400 group-hover:translate-x-1 transition">→</span>
    </a>
    <a href="/posts/feature_fanza_childhood_friend_sleepover_first_night_ranking_2026" class="p-3.5 bg-slate-800/80 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-rose-500/50 transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-rose-300 font-medium">【幼馴染・お泊まり実家帰省特化】昔の面影と大人の色気背徳中出し選</span>
      <span class="text-rose-400 group-hover:translate-x-1 transition">→</span>
    </a>
    <a href="/posts/feature_fanza_common_sense_alteration_hypnosis_ranking" class="p-3.5 bg-slate-800/80 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-rose-500/50 transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-rose-300 font-medium">【常識改変・催眠洗脳特化】無自覚にハメ狂う絶対服従AV厳選</span>
      <span class="text-rose-400 group-hover:translate-x-1 transition">→</span>
    </a>
  </div>
</div>

<!-- よくある質問 (FAQ) -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8">
  <h3 class="text-xl font-bold text-white mb-6 flex items-center gap-2">
    <span class="text-rose-400">❓</span> 媚薬・キメセクAVに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-4 text-sm md:text-base">
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-rose-300 mb-2">Q1. 媚薬・キメセク作品の最大の魅力は何ですか？</h4>
      <p class="text-slate-300 leading-relaxed">普段は絶対に乱れない清楚な美女や高飛車な女性が、理性を完全に奪われて自ら腰を振り乱し、快楽に屈服して中出しを懇願する圧倒的な「ギャップ」と「背徳感」です。</p>
    </div>
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-rose-300 mb-2">Q2. 一番激しい潮吹きや痙攣を楽しみたいならどの作品がおすすめですか？</h4>
      <p class="text-slate-300 leading-relaxed">第1位の末広純主演作（WAAA-270）が圧倒的です。アスリート美女の引き締まった肉体が汗と愛液まみれになり、限界を超えた連続アクメでベッドを水浸しにする狂気の実用度を誇ります。</p>
    </div>
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-rose-300 mb-2">Q3. 初心者でも引かずに楽しめますか？</h4>
      <p class="text-slate-300 leading-relaxed">はい。第2位の小野六花や第3位の東條なつのように、シチュエーションとしてのストーリー性がしっかりしており、映像美とエロスが絶妙に融合した名作から入ると没入しやすくおすすめです。</p>
    </div>
  </div>
</div>"""
    html_parts.append(table_and_links)

    # JSON-LD Schema
    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "ItemList",
                "name": "FANZA「媚薬・キメセク・ガンギマリ発情」おすすめ神作ランキングTOP5",
                "description": "清楚美女が超強力媚薬で白目を剥いて腰を振り乱す限界潮吹き交尾AVおすすめランキングTOP5【2026年最新】",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": idx + 1,
                        "name": it.get('title'),
                        "url": it.get('affiliate_url_clean')
                    } for idx, it in enumerate(items)
                ]
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": "媚薬・キメセクAVの最大の魅力は何ですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "普段は絶対に乱れない清楚な美女が理性を完全に奪われて自ら腰を振り乱し、快楽に屈服して中出しを懇願する圧倒的なギャップと背徳感です。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "一番激しい潮吹きや痙攣を楽しみたいならどの作品がおすすめですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第1位の末広純主演作（WAAA-270）が圧倒的です。引き締まった肉体が汗と愛液まみれになり限界を超えた連続アクメを披露します。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "初心者でも引かずに楽しめますか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "はい、小野六花や東條なつのようにストーリー性と映像美が優れた名作から入ると存分に楽しめます。"
                        }
                    }
                ]
            }
        ]
    }
    json_ld_script = f'<script type="application/ld+json">\n{json.dumps(json_ld, ensure_ascii=False, indent=2)}\n</script>'
    html_parts.append(json_ld_script)

    full_html = "\n\n".join(html_parts)
    char_count = count_japanese_chars(full_html)
    print(f"Article 1 character count: {char_count} chars")
    if char_count < 3000:
        raise Exception(f"Article 1 is under 3000 chars: {char_count}")

    post_data = {
        "id": "feature_fanza_aphrodisiac_drugged_ecstasy_spasm_ranking_2026",
        "title": "【理性崩壊の肉欲痙攣】FANZA「媚薬・キメセク・ガンギマリ発情」おすすめ神作ランキングTOP5！清楚美女が超強力媚薬で白目を剥いて腰を振り乱す限界潮吹き交尾AV選【2026年最新】",
        "date": "2026-10-05 02:00:00",
        "hinban": "APHRODISIAC-ECSTASY-SPASM-2026",
        "price": "300~",
        "maker": "FANZA公式セレクション",
        "actresses": ["末広純", "小野六花", "東條なつ", "望月円", "日向由奈"],
        "genres": ["媚薬", "キメセク", "ガンギマリ", "潮吹き", "痙攣", "悪堕ち", "理性崩壊", "生中出し", "特集", "殿堂入り"],
        "image": cover_image,
        "review": full_html
    }

    file_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f" -> Successfully saved Article 1 ({char_count} chars) to {file_path}")


# ==============================================================================
# 記事2: パパ活女子・お手当増額生中出し＆プライド崩壊調教 特化
# ==============================================================================
def generate_article_papakatsu():
    print("=== Generating Article 2: パパ活女子・お手当増額生中出し＆プライド崩壊調教特化 ===")
    cids = ["1stars00693", "fpre00124", "ebod00845", "mkmp00656", "mdbk00358"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["パパ活", "お手当", "生中出し", "港区女子", "屈服", "殿堂入り"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 2 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-amber-950/40 via-slate-900 to-slate-950 border border-amber-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-amber-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-amber-500/20 text-amber-300 border border-amber-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">SUGAR DADDY SWEET SUBMISSION SPECIAL</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月05日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【お金の魔力でプライド崩壊】FANZA「パパ活女子・お手当増額生中出し」おすすめ神作ランキングTOP5！小遣い稼ぎの生意気美少女がお手当に負けて生ハメ種付けを受け入れる屈辱快楽AV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    ブランド品や贅沢な生活のために、年の離れたオジサンから「お手当」をもらって割り切った関係を築く現代のパパ活女子たち。最初のうちは「ご飯食べるだけで3万ね」「ホテルは無理だから」と生意気な態度でオジサンを見下していた今どき美少女が、札束の厚みと絶倫ピストンの快感に抗えず、少しずつプライドを削り落とされていく――。これほど男の征服欲と優越感を掻き立てるシチュエーションはありません。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    「今日ゴムないんだけど…お手当あと10万上乗せするから生でいい？」「えっ…10万？…じゃあ中には出さないでね」という口約束から始まる密室の攻防。一度生のチンポを受け入れてしまえば、若い膣内はおじさんの硬く逞しい肉棒に貪り尽くされ、「ダメ…生気持ちよすぎる…おじさんのおちんぽ凄い…！」とプライドをかなぐり捨てて啼き乱れます。最後はお金を握りしめながら、子宮の奥深くまで注ぎ込まれる熱い精液に痙攣するしかありません。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、青空ひかりが絶倫パパに一日中ホテルで滅茶苦茶に中出しされる金字塔から、菊乃らんの港区女子ベロ舐め調教、香坂紗梨のHカップ爆乳制服P活、柏木こなつの塩対応パパ活チクイキ屈服、森日向子らの美脚OLパパ活まで、リアルな現代フェチと屈辱快楽の頂点を極めた【パパ活神作TOP5】を徹底特集します。
  </p>
</div>

<!-- 選び方の基準 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-amber-400">💵</span> パパ活モノで最高の征服感と快楽を貪るための3大チェックポイント
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-amber-300 mb-2">① 生意気・塩対応からの屈服グラデーション</h4>
      <p class="text-slate-300 leading-relaxed">最初はスマホをいじりながら適当に愛想笑いしていた小娘が、札束を目の前に積まれ、肉棒を押し込まれた途端にメスの顔へと崩れ落ちる落差が最高の抜きどころです。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-amber-300 mb-2">② お手当増額交渉とナマ解禁の駆け引き</h4>
      <p class="text-slate-300 leading-relaxed">「生ハメならプラス5万」「中出しならプラス10万」とお金に目が眩んでハードルを下げていき、最終的に肉欲の快楽に呑まれて自ら種付けを懇願する展開が興奮を倍増させます。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-amber-300 mb-2">③ オジサンに一日中貪り尽くされる濃厚連射</h4>
      <p class="text-slate-300 leading-relaxed">ホテルの密室に缶詰めにされ、朝から晩まで体力尽きるまで何度も膣内に射精され続ける圧倒的な種付けピストンこそが、実用派ファンの射精中枢を狂わせます。</p>
    </div>
  </div>
</div>"""
    html_parts.append(intro_html)

    reviews_data = {
        "1stars00693": {
            "desc": """<h4>【作品解説・見どころ】青空ひかりの歴史的メガヒット！絶倫おじさんにホテルで一日中中出しされる金字塔</h4>
<p>圧倒的なアイドル級フェイスと透明感を併せ持つ青空ひかりが、小遣い稼ぎのパパ活で出会った絶倫オジサンに高級ホテルへ連れ込まれ、文字通り一日中休むことなく生中出しされまくる伝説の名作。「短時間でサクッと終わらせて買い物行こう」と高を括っていたひかりちゃんが、オジサンの底知れない精力と太いペニスに圧倒され、次第にベッドから逃げられなくなっていきます。</p>
<h4>【実用ポイント】逃げ場のないベッドで繰り返される濃厚種付けの嵐</h4>
<p>ゴムを外された生の亀頭が膣奥を貫くたびに、青空ひかりの大きな瞳から涙がこぼれ、しかしアソコは愛液でグショグショに濡れそぼります。1発目を出されてもオジサンのチ○ポは萎えず、バック、正常位、対面座位と体位を変えながら容赦なく注ぎ込まれる大量の白濁液。何発も中出しされてアヘ顔で痙攣する青空ひかりの姿は、実用度120％の歴史的傑作です。</p>""",
            "rating": "★★★★★ 5.0 / 5.0",
            "service_score": "パパ活屈服度: 100% | 連射中出し度: 100% | 実用性: 100%"
        },
        "fpre00124": {
            "desc": """<h4>【作品解説・見どころ】菊乃らんの長身巨乳スタイル！パパを骨抜きにする港区女子の濃厚ベロ舐めテク</h4>
<p>高身長スラリとした美脚と豊かな美巨乳を誇る港区美女・菊乃らんが、金持ちパパを虜にする極上エロテクニックを披露する超実力派作品。高級ラウンジやバーで男の自尊心をくすぐる会話を繰り広げた後、スイートルームで始まる濃密な愛撫タイム。長い舌を器用に使って男の耳元、首筋、そして股間へと這わせていく密着ベロ舐めは、見る者すべての脳を溶かします。</p>
<h4>【実用ポイント】金目当てのはずが我を忘れて跨がる極上騎乗位</h4>
<p>パパをお手玉のように転がしていたはずの菊乃らんが、逞しい肉棒に貫かれた瞬間、女の野生を取り戻して自ら激しく腰を上下させます。豊満な胸が波打ち、滴る汗が肌を光らせながら「パパのおちんちん、凄く気持ちいい…」と甘く喘ぐ姿は、男のプライドを最高峰まで満たしてくれる極上体験です。</p>""",
            "rating": "★★★★★ 4.9 / 5.0",
            "service_score": "港区女子度: 100% | ベロ舐めテク: 99% | 実用性: 99%"
        },
        "ebod00845": {
            "desc": """<h4>【作品解説・見どころ】香坂紗梨のド迫力Hカップ肉弾戦！どすけべ制服女子のパパ活バイト</h4>
<p>たわわに実ったHカップの天然巨乳とむっちりとした魅惑のボディラインを持つ香坂紗梨が、制服姿でパパ活に励むハイレベル作品。ボタンが弾けそうなほど張ち切れんばかりの胸元と、短いスカートから覗く柔らかな太もも。お金を受け取った彼女は、初対面のオジサンに対しても物怖じせず、むっちりした肉体を惜しげもなく密着させてきます。</p>
<h4>【実用ポイント】爆乳パイズリと肉感ヒップへのバックピストン</h4>
<p>男の股間を巨大なバストで挟み込む極上パイズリから始まり、四つん這いにさせてむっちりしたお尻を背後から突き崩すバック交尾へ。肉と肉がぶつかり合う激しい破裂音とともに、香坂紗梨の豊かな肉体が波打ちます。生ハメの快感に酔いしれて中出しを許してしまう瞬間、男の興奮は最高潮へと達します。</p>""",
            "rating": "★★★★★ 4.9 / 5.0",
            "service_score": "Hカップ肉感度: 100% | 制服フェチ度: 99% | 実用性: 99%"
        },
        "mkmp00656": {
            "desc": """<h4>【作品解説・見どころ】柏木こなつの塩対応が生意気！乳首弱点パパ活女子の強制チクイキ屈服</h4>
<p>小生意気な表情とキュートなルックスの柏木こなつが、オジサンを完全に金づる扱いする塩対応パパ活女子を熱演。ホテルに入っても冷めた態度で「早く終わらせてよね」と見下してくる彼女に対し、オジサンが目をつけたのは彼女の隠れた弱点・超敏感な乳首でした。執拗に乳首をコリコリと弄ばれ、吸い上げられるうちに、生意気な態度は一変します。</p>
<h4>【実用ポイント】プライド完全崩壊！チクイキ連発からの痙攣アクメ</h4>
<p>「やだ…そこ触らないで…あっ、あぁぁっ！」と乳首を責められるだけで腰をビクンビクンと跳ね上げ、自ら潮を吹いてイキ狂う柏木こなつ。塩対応だったはずの少女が、快楽に屈服して「ごめんなさい…何でも言うこと聞くから…！」と涙目で懇願してくるカタルシスは悶絶必至の快感です。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "塩対応屈服度: 100% | チクイキ敏感度: 98% | 実用性: 98%"
        },
        "mdbk00358": {
            "desc": """<h4>【作品解説・見どころ】森日向子・都月るいさ・Nia！美脚パパ活OLたちの絶対領域エロテク</h4>
<p>抜群のプロポーションを誇る森日向子、都月るいさ、Niaの3大美女が、副業感覚でパパ活に手を染める現役OLを演じる超豪華作。タイトスカートにストッキング、スリットから覗く絶対領域でオジサンの視線を釘付けにします。職場で溜まったストレスを発散するかのように、オジサンのチンポを美脚で挟み、手練手管のテクニックで翻弄してきます。</p>
<h4>【実用ポイント】3人それぞれの美脚責めと濃厚射精搾り取り</h4>
<p>ストッキング越しの足コキや密着フェラチオで限界まで勃起させられた後、オフィス調の個室で生ハメ交尾へ。美女たちが代わる代わる腰を振り、オジサンの精力を根こそぎ吸い取るような濃厚ピストンを繰り広げます。美脚フェチ・OL好きにはたまらない贅沢極まりない実用作です。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "美脚ストッキング: 100% | 豪華キャスト度: 98% | 実用性: 98%"
        }
    }

    for idx, it in enumerate(items):
        cid = it.get("content_id")
        title = it.get("title")
        aff_url = it.get("affiliate_url_clean")
        large_img = it.get("imageURL", {}).get("large", "")
        acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        act_html = " ".join([get_actress_link(a) for a in acts])
        genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        genre_html = " ".join([get_genre_link(g) for g in genres[:6]])
        sample_imgs = get_sample_images(it, 4)
        c_data = reviews_data.get(cid, {})

        sample_imgs_html = ""
        if sample_imgs:
            img_tags = "".join([f'<img src="{sim}" alt="{title} サンプル{s_idx+1}" class="w-full h-28 object-cover rounded-lg border border-slate-700/80 hover:scale-105 transition transform duration-300" loading="lazy" />' for s_idx, sim in enumerate(sample_imgs)])
            sample_imgs_html = f'<div class="grid grid-cols-2 md:grid-cols-4 gap-2 my-4">{img_tags}</div>'

        item_block = f"""
<div class="my-10 bg-slate-900/90 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-2xl relative">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-2">
      <span class="bg-amber-600 text-white font-black text-sm px-3 py-1 rounded-lg">第{idx+1}位</span>
      <span class="text-xs text-slate-400 font-mono tracking-wider">品番: {cid.upper()}</span>
    </div>
    <div class="text-amber-400 font-black text-sm tracking-wide">{c_data.get('rating', '★★★★★ 5.0 / 5.0')}</div>
  </div>

  <h3 class="text-xl md:text-2xl font-black text-white leading-snug mb-4 hover:text-amber-400 transition">
    <a href="{aff_url}" target="_blank" rel="nofollow noopener">{title}</a>
  </h3>

  <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-start">
    <div class="md:col-span-5">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block group overflow-hidden rounded-xl border border-slate-700/80 shadow-lg relative">
        <img src="{large_img}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition duration-300 flex items-end p-4">
          <span class="bg-amber-600 text-white font-bold text-xs px-3 py-1.5 rounded-full shadow-lg">FANZA公式で今すぐ無料サンプル再生 ▶</span>
        </div>
      </a>
      <div class="mt-3 text-xs bg-slate-800/60 p-2.5 rounded-lg border border-slate-700/50 text-slate-300">
        <div class="mb-1"><span class="text-slate-400">主演女優:</span> {act_html or "人気トップキャスト"}</div>
        <div><span class="text-slate-400">スペック評価:</span> <span class="text-amber-300 font-medium">{c_data.get('service_score', '実用度特化')}</span></div>
      </div>
    </div>

    <div class="md:col-span-7 space-y-4 text-slate-300 text-sm md:text-base leading-relaxed">
      {c_data.get('desc', '')}
      
      <div class="pt-2">
        <div class="text-xs text-slate-400 mb-2 font-medium">関連ジャンルタグ:</div>
        <div class="flex flex-wrap gap-1.5">{genre_html}</div>
      </div>
    </div>
  </div>

  {sample_imgs_html}

  <div class="mt-6 flex flex-col sm:flex-row items-center justify-between gap-4 bg-slate-950/80 p-4 rounded-xl border border-slate-800">
    <div class="text-xs text-slate-400">
      高画質ストリーミング／ダウンロード対応・スマホ即時視聴可能
    </div>
    <div class="flex items-center gap-3 w-full sm:w-auto">
      <a href="/posts/{cid}" class="text-center px-4 py-2.5 rounded-xl border border-slate-700 text-slate-300 hover:text-white hover:bg-slate-800 text-xs font-bold transition w-1/2 sm:w-auto">
        詳細個別レビューを見る
      </a>
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="text-center bg-gradient-to-r from-amber-600 to-orange-600 hover:from-amber-500 hover:to-orange-500 text-white text-sm font-black px-6 py-2.5 rounded-xl shadow-lg shadow-amber-900/40 hover:shadow-amber-800/60 transition transform hover:-translate-y-0.5 w-1/2 sm:w-auto">
        FANZA公式で今すぐ本編を見る ▶
      </a>
    </div>
  </div>
</div>"""
        html_parts.append(item_block)

    # 比較まとめテーブル & 関連特集リンク
    table_and_links = f"""
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-amber-400">📊</span> 【徹底比較】パパ活女子・お手当屈服神作TOP5 スペック一覧表
  </h3>
  <div class="overflow-x-auto">
    <table class="w-full text-left text-xs md:text-sm text-slate-300">
      <thead class="bg-slate-800/80 text-slate-200">
        <tr>
          <th class="p-3">順位</th>
          <th class="p-3">作品タイトル</th>
          <th class="p-3">主演キャスト</th>
          <th class="p-3">特化属性</th>
          <th class="p-3">実用評価</th>
          <th class="p-3 text-center">公式リンク</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800">
        <tr class="hover:bg-slate-800/40 transition">
          <td class="p-3 font-bold text-amber-400">第1位</td>
          <td class="p-3 font-medium text-white">{items[0].get('title')[:32]}...</td>
          <td class="p-3">青空ひかり</td>
          <td class="p-3">絶倫パパ・一日中ホテル缶詰め中出し</td>
          <td class="p-3 text-amber-400">★★★★★ 5.0</td>
          <td class="p-3 text-center"><a href="{items[0].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-amber-400 hover:underline font-bold">作品を見る</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40 transition">
          <td class="p-3 font-bold text-amber-400">第2位</td>
          <td class="p-3 font-medium text-white">{items[1].get('title')[:32]}...</td>
          <td class="p-3">菊乃らん</td>
          <td class="p-3">港区女子・長身巨乳ベロ舐めテク</td>
          <td class="p-3 text-amber-400">★★★★★ 4.9</td>
          <td class="p-3 text-center"><a href="{items[1].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-amber-400 hover:underline font-bold">作品を見る</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40 transition">
          <td class="p-3 font-bold text-amber-400">第3位</td>
          <td class="p-3 font-medium text-white">{items[2].get('title')[:32]}...</td>
          <td class="p-3">香坂紗梨</td>
          <td class="p-3">Hカップ爆乳制服・肉弾パイズリ</td>
          <td class="p-3 text-amber-400">★★★★★ 4.9</td>
          <td class="p-3 text-center"><a href="{items[2].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-amber-400 hover:underline font-bold">作品を見る</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40 transition">
          <td class="p-3 font-bold text-amber-400">第4位</td>
          <td class="p-3 font-medium text-white">{items[3].get('title')[:32]}...</td>
          <td class="p-3">柏木こなつ</td>
          <td class="p-3">塩対応パパ活・乳首攻めチクイキ屈服</td>
          <td class="p-3 text-amber-400">★★★★★ 4.8</td>
          <td class="p-3 text-center"><a href="{items[3].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-amber-400 hover:underline font-bold">作品を見る</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40 transition">
          <td class="p-3 font-bold text-amber-400">第5位</td>
          <td class="p-3 font-medium text-white">{items[4].get('title')[:32]}...</td>
          <td class="p-3">森日向子 ほか</td>
          <td class="p-3">美脚OLパパ活・ストッキング搾精</td>
          <td class="p-3 text-amber-400">★★★★★ 4.8</td>
          <td class="p-3 text-center"><a href="{items[4].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-amber-400 hover:underline font-bold">作品を見る</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- 内部リンク：あわせて読みたい関連特集 -->
<div class="my-10 bg-slate-900/60 border border-slate-800 rounded-2xl p-6 md:p-8">
  <h3 class="text-lg font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-amber-400">🔥</span> あわせてチェックしたい！征服・背徳特化の人気特集
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-sm">
    <a href="/posts/feature_fanza_missed_last_train_roomwear_sleepover_ranking_2026" class="p-3.5 bg-slate-800/80 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-amber-500/50 transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-amber-300 font-medium">【終電逃し・無防備部屋着特化】すっぴんノーブラ生中出しAV厳選</span>
      <span class="text-amber-400 group-hover:translate-x-1 transition">→</span>
    </a>
    <a href="/posts/feature_fanza_home_tutor_private_lesson_seduction_ranking_2026" class="p-3.5 bg-slate-800/80 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-amber-500/50 transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-amber-300 font-medium">【美人家庭教師・個別指導特化】密室勉強部屋での背徳生ハメ選</span>
      <span class="text-amber-400 group-hover:translate-x-1 transition">→</span>
    </a>
    <a href="/posts/feature_fanza_cabin_attendant_flight_hotel_ranking_2026" class="p-3.5 bg-slate-800/80 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-amber-500/50 transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-amber-300 font-medium">【美脚CA・フライト先密会特化】制服美女をホテルでハメ狂うAV選</span>
      <span class="text-amber-400 group-hover:translate-x-1 transition">→</span>
    </a>
    <a href="/posts/feature_fanza_black_gyaru_raw_creampie_ranking_2026" class="p-3.5 bg-slate-800/80 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-amber-500/50 transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-amber-300 font-medium">【黒ギャル・生中出し特化】肉食ビッチ美女を種付け屈服させるAV選</span>
      <span class="text-amber-400 group-hover:translate-x-1 transition">→</span>
    </a>
  </div>
</div>

<!-- よくある質問 (FAQ) -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8">
  <h3 class="text-xl font-bold text-white mb-6 flex items-center gap-2">
    <span class="text-amber-400">❓</span> パパ活・お手当中出しAVに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-4 text-sm md:text-base">
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-amber-300 mb-2">Q1. パパ活モノの一番の興奮ポイントは何ですか？</h4>
      <p class="text-slate-300 leading-relaxed">お金を媒介にしたリアルな上下関係と、最初は舐めた態度をとっていた美少女がお手当増額に釣られて生ハメを受け入れ、最終的に肉欲で喘ぎ狂う征服感です。</p>
    </div>
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-amber-300 mb-2">Q2. 一番抜け度が高くて中出しが濃厚な作品はどれですか？</h4>
      <p class="text-slate-300 leading-relaxed">第1位の青空ひかり主演作（1STARS-693）です。ホテルで一日中絶倫ピストンを受け続け、何発も中出しされて徐々にトロ顔になっていく過程は全男子必見です。</p>
    </div>
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-amber-300 mb-2">Q3. スタイル抜群の美女が見たい場合は？</h4>
      <p class="text-slate-300 leading-relaxed">長身巨乳の菊乃らん（第2位）や、むっちりHカップの香坂紗梨（第3位）がおすすめです。圧倒的な肉体美でおじさんを弄ぶ姿が最高にソソります。</p>
    </div>
  </div>
</div>"""
    html_parts.append(table_and_links)

    # JSON-LD Schema
    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "ItemList",
                "name": "FANZA「パパ活女子・お手当増額生中出し」おすすめ神作ランキングTOP5",
                "description": "小遣い稼ぎの生意気美少女がお手当に負けて生ハメ種付けを受け入れる屈辱快楽AVおすすめランキングTOP5【2026年最新】",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": idx + 1,
                        "name": it.get('title'),
                        "url": it.get('affiliate_url_clean')
                    } for idx, it in enumerate(items)
                ]
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": "パパ活モノの一番の興奮ポイントは何ですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "お金を媒介にしたリアルな上下関係と、最初は舐めた態度をとっていた美少女がお手当に釣られて生ハメを受け入れ、最終的に肉欲で喘ぎ狂う征服感です。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "一番抜け度が高くて中出しが濃厚な作品はどれですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第1位の青空ひかり主演作（1STARS-693）です。ホテルで一日中絶倫ピストンを受け続け何発も中出しされる過程は必見です。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "スタイル抜群の美女が見たい場合は？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "長身巨乳の菊乃らんや、むっちりHカップの香坂紗梨がおすすめです。"
                        }
                    }
                ]
            }
        ]
    }
    json_ld_script = f'<script type="application/ld+json">\n{json.dumps(json_ld, ensure_ascii=False, indent=2)}\n</script>'
    html_parts.append(json_ld_script)

    full_html = "\n\n".join(html_parts)
    char_count = count_japanese_chars(full_html)
    print(f"Article 2 character count: {char_count} chars")
    if char_count < 3000:
        raise Exception(f"Article 2 is under 3000 chars: {char_count}")

    post_data = {
        "id": "feature_fanza_sugar_daddy_allowance_raw_creampie_ranking_2026",
        "title": "【お金の魔力でプライド崩壊】FANZA「パパ活女子・お手当増額生中出し」おすすめ神作ランキングTOP5！小遣い稼ぎの生意気美少女がお手当に負けて生ハメ種付けを受け入れる屈辱快楽AV選【2026年最新】",
        "date": "2026-10-05 02:10:00",
        "hinban": "SUGAR-DADDY-ALLOWANCE-CREAMPIE-2026",
        "price": "300~",
        "maker": "FANZA公式セレクション",
        "actresses": ["青空ひかり", "菊乃らん", "香坂紗梨", "柏木こなつ", "森日向子"],
        "genres": ["パパ活", "お手当", "生中出し", "港区女子", "女子大生", "屈服", "制服", "買収", "特集", "殿堂入り"],
        "image": cover_image,
        "review": full_html
    }

    file_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f" -> Successfully saved Article 2 ({char_count} chars) to {file_path}")


# ==============================================================================
# 記事3: 極上パイズリ・巨乳挟まれ窒息射精 特化
# ==============================================================================
def generate_article_paizuri():
    print("=== Generating Article 3: 極上パイズリ・巨乳挟まれ窒息射精特化 ===")
    cids = ["sone00912", "mide00634", "ssni00347", "pppe00071", "mide00839"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["パイズリ", "巨乳", "爆乳", "挟射", "窒息", "殿堂入り"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 3 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-pink-950/40 via-slate-900 to-slate-950 border border-pink-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-pink-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-pink-500/20 text-pink-300 border border-pink-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">TITFUCK BREASTS SUFFOCATION SPECIAL</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月05日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【神乳に埋もれて昇天】FANZA「極上パイズリ・巨乳挟まれ窒息射精」おすすめ神作ランキングTOP5！たわわな爆乳の谷間に包まれて精子を一滴残らず搾り取られる夢の母性＆快楽AV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    男たるもの、誰もが一度は夢見る究極の楽園――それが「美女の巨大な胸に顔を埋め、柔らかな谷間に肉棒を挟まれて射精すること」。母性あふれる温もりと、手コキやフェラチオをも凌駕する極上の密着圧力。摩擦熱とローションの滑らかさが融合し、先端を擦り上げられるたびに脳髄が痺れるような快楽が押し寄せる「パイズリ」は、全世代の男性にとって永遠の聖域です。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    両手でたわわな胸を寄せ集め、亀頭を包み込んで上目遣いで見つめてくる美女。息苦しいほどの爆乳に顔を押し付けられ、甘い香りに包まれながら「おっぱい気持ちいい？全部出していいんだよ…」と耳元で囁かれた瞬間、男の射精我慢リミッターは完全に崩壊します。溢れ出た白濁液が胸元や鎖骨を白く汚し、それでもなお優しくしごき上げられる追撃の快感は、まさに男にとっての極楽浄土です。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、S1最強ヒロイン瀬戸環奈による神がかったパイズリ挟射から、水卜さくらが30本のチンポを抜きまくる伝説のパイズリ大乱交、夢乃あいかの献身的超密着おっぱい尽くし、蜜美杏＆百永さりなのW爆乳挟み撃ち回春エステ、そして中山ふみかのノーブラ巨乳誘惑まで、実用度・母性・破壊力のすべてを兼ね備えた【パイズリ神作TOP5】を徹底解説します。
  </p>
</div>

<!-- 選び方の基準 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-pink-400">🍈</span> 極上パイズリで至高の昇天を迎えるための3大チェックポイント
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-pink-300 mb-2">① おっぱいの肉感・弾力と谷間の密着圧</h4>
      <p class="text-slate-300 leading-relaxed">単に胸が大きいだけでなく、ペニスをすっぽりと隙間なく包み込める柔らかさと、キュッと締め上げる筋力・テクニックがあるかどうかが快感を大きく左右します。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-pink-300 mb-2">② 上目遣いの視線と耳元への甘い囁き</h4>
      <p class="text-slate-300 leading-relaxed">「いっぱい溜まってるの？」「おっぱいにビュルビュル出して？」と、胸を上下させながら慈愛と淫らさが入り混じった瞳で見つめてくる心理的プレイが射精欲を刺激します。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-pink-300 mb-2">③ 射精瞬間の胸元ぶっかけと追撃搾精</h4>
      <p class="text-slate-300 leading-relaxed">我慢できずに谷間から勢いよく発射された精子を、嫌がることなく胸元いっぱいに浴び、さらに残さず丁寧に搾り取ってくれるフィニッシュの満足度が抜群です。</p>
    </div>
  </div>
</div>"""
    html_parts.append(intro_html)

    reviews_data = {
        "sone00912": {
            "desc": """<h4>【作品解説・見どころ】瀬戸環奈の最強ヒロイン美乳！神業パイズリ挟射で男を骨抜きにする傑作</h4>
<p>パーフェクトな美貌と透明感を誇るトップ女優・瀬戸環奈が、自慢の極上バストをフル活用して男のペニスを弄び尽くすS1の超人気作。美しく形の整った豊かな胸を両手で寄せ集め、先端から根元まで丁寧にペニスを包み込む姿はまさに眼福の極み。ローションをたっぷり馴染ませた胸の谷間でシャコシャコと擦り上げられる快感に、男の腰は思わず浮き上がってしまいます。</p>
<h4>【実用ポイント】至近距離の上目遣いと谷間へのダイレクト射精</h4>
<p>瀬戸環奈の吸い込まれそうな瞳で見つめられ、「環奈のおっぱいでイッて…？」とおねだりされる破壊力は凄まじいものがあります。息を呑むような美しさと生々しい摩擦熱が融合し、絶頂の瞬間には谷間の最深部から勢いよく精液が飛び散ります。美少女フェチも巨乳好きも一網打尽にする必見の1本です。</p>""",
            "rating": "★★★★★ 5.0 / 5.0",
            "service_score": "ビジュアル完成度: 100% | 挟射テクニック: 100% | 実用性: 100%"
        },
        "mide00634": {
            "desc": """<h4>【作品解説・見どころ】水卜さくらの伝説的快挙！30本のチンポを抜きまくるパイズリ大乱交</h4>
<p>究極のロリフェイスと爆発的Gカップを併せ持つ水卜さくらが、次々と押し寄せる男たちのペニスをひたすらパイズリだけで射精させ続ける伝説的企画モノ。小さく可憐な体躯に不釣り合いなほどの豊満バストが、激しい動きに合わせて縦横無尽に揺れ動きます。男たちの逞しい肉棒を、嫌な顔一つせず愛おしそうに胸で抱きかかえる姿は聖母そのものです。</p>
<h4>【実用ポイント】休む間もなく繰り返される胸元発射と精子まみれのおっぱい</h4>
<p>何本ものチンポが次々に胸の谷間に沈み込み、連続で白濁液を噴射していく様は圧巻のひと言。胸元、谷間、そしてさくらちゃんの首筋までが精子で真っ白に染まりながらも、笑顔で次の男棒を迎え入れる献身っぷりは実用度MAX。爆乳パイズリの歴史に残る金字塔です。</p>""",
            "rating": "★★★★★ 4.9 / 5.0",
            "service_score": "パイズリ耐久度: 100% | 精子まみれ度: 100% | 実用性: 100%"
        },
        "ssni00347": {
            "desc": """<h4>【作品解説・見どころ】夢乃あいかの超密着おっぱい尽くし！世話焼き職業女子の献身的搾精</h4>
<p>爆乳界の絶対的女王・夢乃あいかが、看護師や家政婦など様々な世話焼き職業女子に扮し、豊満すぎる胸を惜しみなく密着させて男を癒やし尽くす大人気作。服の上からでも隠しきれない圧倒的ボリュームのバストが、男の顔や体に押し付けられるシーンは窒息寸前の至福感。彼女特有の温かな笑顔と包容力に、日頃のストレスが一瞬で消し飛びます。</p>
<h4>【実用ポイント】柔らかな弾力に包まれて精力を根こそぎ奪われる快感</h4>
<p>ベッドに仰向けになった男の上に乗っかり、豊かな胸でペニスをすっぽり覆い隠して擦り上げるパイズリは、他の追随を許さない極上の柔らかさ。「いっぱい出して楽になってね…」と囁かれながら、胸の温もりに包まれて果てる瞬間は、男の本能が完全に昇天する至高の瞬間です。</p>""",
            "rating": "★★★★★ 4.9 / 5.0",
            "service_score": "母性包容力: 100% | 爆乳弾力度: 99% | 実用性: 99%"
        },
        "pppe00071": {
            "desc": """<h4>【作品解説・見どころ】蜜美杏＆百永さりなのW爆乳サンドイッチ！回春エステの挟み撃ち搾精</h4>
<p>圧巻のダイナマイトボディを誇る蜜美杏と百永さりなという、巨乳ファン垂涎の2大美女が同時に施術を担当する夢の回春エステ作。施術台に寝かされた男の左右から、巨大なバストが同時に押し当てられる「Wパイズリ挟み撃ち」はまさに男の妄想の極致。逃げ場のない爆乳の壁に挟まれ、前からも横からも責め立てられます。</p>
<h4>【実用ポイント】一度射精しても止まらない！2つの神乳による追撃パイズリ</h4>
<p>1発目を射精してぐったりしたペニスに対しても、二人は優しく微笑みながら「まだまだ出せるよね？」とおっぱい責めを再開。敏感になった亀頭をふんわりと包み込み、2発目、3発目と容赦なく精子を吸い出していく破壊力は、パイズリ好きなら一度は体験しておくべき極限の実用度です。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "W爆乳迫力度: 100% | 追撃搾精度: 98% | 実用性: 98%"
        },
        "mide00839": {
            "desc": """<h4>【作品解説・見どころ】中山ふみかのノーブラ巨乳誘惑！彼女の部屋でお姉ちゃんに略奪される夜</h4>
<p>重量級のド迫力バストと蠱惑的な肉体美を持つ中山ふみかが、妹の留守中に彼女の彼氏をノーブラ部屋着で誘惑する禁断のシチュエーション。薄い部屋着からくっきりと浮かぶ豊かな胸の丸み、胸元をはだけさせて「妹には内緒にしてあげるから…」と耳元で囁く妖艶なアプローチに、男の股間は瞬時に鋼のように硬くなります。</p>
<h4>【実用ポイント】重量感あふれるおっぱいパイズリとそのまま跨がり騎乗位へ</h4>
<p>中山ふみかのずっしりと重い美巨乳でペニスを挟み込み、上下にスライドさせながら見つめてくる表情は背徳感の極み。我慢できずに射精寸前まで追い込まれた後、自ら跨がって肉棒を飲み込み、胸を揺らしながら激しくイキ狂うクライマックスは、巨乳・パイズリ好きの脳汁を限界まで噴出させます。</p>""",
            "rating": "★★★★★ 4.8 / 5.0",
            "service_score": "ノーブラ誘惑度: 100% | 重量感パイズリ: 98% | 実用性: 98%"
        }
    }

    for idx, it in enumerate(items):
        cid = it.get("content_id")
        title = it.get("title")
        aff_url = it.get("affiliate_url_clean")
        large_img = it.get("imageURL", {}).get("large", "")
        acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        act_html = " ".join([get_actress_link(a) for a in acts])
        genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        genre_html = " ".join([get_genre_link(g) for g in genres[:6]])
        sample_imgs = get_sample_images(it, 4)
        c_data = reviews_data.get(cid, {})

        sample_imgs_html = ""
        if sample_imgs:
            img_tags = "".join([f'<img src="{sim}" alt="{title} サンプル{s_idx+1}" class="w-full h-28 object-cover rounded-lg border border-slate-700/80 hover:scale-105 transition transform duration-300" loading="lazy" />' for s_idx, sim in enumerate(sample_imgs)])
            sample_imgs_html = f'<div class="grid grid-cols-2 md:grid-cols-4 gap-2 my-4">{img_tags}</div>'

        item_block = f"""
<div class="my-10 bg-slate-900/90 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-2xl relative">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-2">
      <span class="bg-pink-600 text-white font-black text-sm px-3 py-1 rounded-lg">第{idx+1}位</span>
      <span class="text-xs text-slate-400 font-mono tracking-wider">品番: {cid.upper()}</span>
    </div>
    <div class="text-amber-400 font-black text-sm tracking-wide">{c_data.get('rating', '★★★★★ 5.0 / 5.0')}</div>
  </div>

  <h3 class="text-xl md:text-2xl font-black text-white leading-snug mb-4 hover:text-pink-400 transition">
    <a href="{aff_url}" target="_blank" rel="nofollow noopener">{title}</a>
  </h3>

  <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-start">
    <div class="md:col-span-5">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block group overflow-hidden rounded-xl border border-slate-700/80 shadow-lg relative">
        <img src="{large_img}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition duration-300 flex items-end p-4">
          <span class="bg-pink-600 text-white font-bold text-xs px-3 py-1.5 rounded-full shadow-lg">FANZA公式で今すぐ無料サンプル再生 ▶</span>
        </div>
      </a>
      <div class="mt-3 text-xs bg-slate-800/60 p-2.5 rounded-lg border border-slate-700/50 text-slate-300">
        <div class="mb-1"><span class="text-slate-400">主演女優:</span> {act_html or "人気トップキャスト"}</div>
        <div><span class="text-slate-400">スペック評価:</span> <span class="text-pink-300 font-medium">{c_data.get('service_score', '実用度特化')}</span></div>
      </div>
    </div>

    <div class="md:col-span-7 space-y-4 text-slate-300 text-sm md:text-base leading-relaxed">
      {c_data.get('desc', '')}
      
      <div class="pt-2">
        <div class="text-xs text-slate-400 mb-2 font-medium">関連ジャンルタグ:</div>
        <div class="flex flex-wrap gap-1.5">{genre_html}</div>
      </div>
    </div>
  </div>

  {sample_imgs_html}

  <div class="mt-6 flex flex-col sm:flex-row items-center justify-between gap-4 bg-slate-950/80 p-4 rounded-xl border border-slate-800">
    <div class="text-xs text-slate-400">
      高画質ストリーミング／ダウンロード対応・スマホ即時視聴可能
    </div>
    <div class="flex items-center gap-3 w-full sm:w-auto">
      <a href="/posts/{cid}" class="text-center px-4 py-2.5 rounded-xl border border-slate-700 text-slate-300 hover:text-white hover:bg-slate-800 text-xs font-bold transition w-1/2 sm:w-auto">
        詳細個別レビューを見る
      </a>
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="text-center bg-gradient-to-r from-pink-600 to-rose-600 hover:from-pink-500 hover:to-rose-500 text-white text-sm font-black px-6 py-2.5 rounded-xl shadow-lg shadow-pink-900/40 hover:shadow-pink-800/60 transition transform hover:-translate-y-0.5 w-1/2 sm:w-auto">
        FANZA公式で今すぐ本編を見る ▶
      </a>
    </div>
  </div>
</div>"""
        html_parts.append(item_block)

    # 比較まとめテーブル & 関連特集リンク
    table_and_links = f"""
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-pink-400">📊</span> 【徹底比較】極上パイズリ・挟射神作TOP5 スペック一覧表
  </h3>
  <div class="overflow-x-auto">
    <table class="w-full text-left text-xs md:text-sm text-slate-300">
      <thead class="bg-slate-800/80 text-slate-200">
        <tr>
          <th class="p-3">順位</th>
          <th class="p-3">作品タイトル</th>
          <th class="p-3">主演キャスト</th>
          <th class="p-3">特化属性</th>
          <th class="p-3">実用評価</th>
          <th class="p-3 text-center">公式リンク</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800">
        <tr class="hover:bg-slate-800/40 transition">
          <td class="p-3 font-bold text-pink-400">第1位</td>
          <td class="p-3 font-medium text-white">{items[0].get('title')[:32]}...</td>
          <td class="p-3">瀬戸環奈</td>
          <td class="p-3">S1最強ヒロイン・美乳密着挟射</td>
          <td class="p-3 text-amber-400">★★★★★ 5.0</td>
          <td class="p-3 text-center"><a href="{items[0].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-pink-400 hover:underline font-bold">作品を見る</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40 transition">
          <td class="p-3 font-bold text-pink-400">第2位</td>
          <td class="p-3 font-medium text-white">{items[1].get('title')[:32]}...</td>
          <td class="p-3">水卜さくら</td>
          <td class="p-3">Gカップ爆乳・30本連続パイズリ乱交</td>
          <td class="p-3 text-amber-400">★★★★★ 4.9</td>
          <td class="p-3 text-center"><a href="{items[1].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-pink-400 hover:underline font-bold">作品を見る</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40 transition">
          <td class="p-3 font-bold text-pink-400">第3位</td>
          <td class="p-3 font-medium text-white">{items[2].get('title')[:32]}...</td>
          <td class="p-3">夢乃あいか</td>
          <td class="p-3">母性爆発・世話焼き超密着おっぱい尽くし</td>
          <td class="p-3 text-amber-400">★★★★★ 4.9</td>
          <td class="p-3 text-center"><a href="{items[2].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-pink-400 hover:underline font-bold">作品を見る</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40 transition">
          <td class="p-3 font-bold text-pink-400">第4位</td>
          <td class="p-3 font-medium text-white">{items[3].get('title')[:32]}...</td>
          <td class="p-3">蜜美杏・百永さりな</td>
          <td class="p-3">W爆乳サンドイッチ・追撃回春エステ</td>
          <td class="p-3 text-amber-400">★★★★★ 4.8</td>
          <td class="p-3 text-center"><a href="{items[3].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-pink-400 hover:underline font-bold">作品を見る</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40 transition">
          <td class="p-3 font-bold text-pink-400">第5位</td>
          <td class="p-3 font-medium text-white">{items[4].get('title')[:32]}...</td>
          <td class="p-3">中山ふみか</td>
          <td class="p-3">ノーブラ巨乳誘惑・重量級略奪交尾</td>
          <td class="p-3 text-amber-400">★★★★★ 4.8</td>
          <td class="p-3 text-center"><a href="{items[4].get('affiliate_url_clean')}" target="_blank" rel="nofollow noopener" class="text-pink-400 hover:underline font-bold">作品を見る</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- 内部リンク：あわせて読みたい関連特集 -->
<div class="my-10 bg-slate-900/60 border border-slate-800 rounded-2xl p-6 md:p-8">
  <h3 class="text-lg font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-pink-400">🔥</span> あわせてチェックしたい！巨乳・射精管理特化の人気特集
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-sm">
    <a href="/posts/feature_fanza_endure_super_technique_raw_creampie_ranking_2026" class="p-3.5 bg-slate-800/80 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-pink-500/50 transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-pink-300 font-medium">【凄テク我慢・生中出し特化】耐え抜いたらご褒美生中出しAV厳選</span>
      <span class="text-pink-400 group-hover:translate-x-1 transition">→</span>
    </a>
    <a href="/posts/feature_fanza_busty_huge_tits_masterpieces_ranking" class="p-3.5 bg-slate-800/80 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-pink-500/50 transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-pink-300 font-medium">【爆乳・巨乳名作特化】揺れる巨大バストの圧倒的迫力AV厳選</span>
      <span class="text-pink-400 group-hover:translate-x-1 transition">→</span>
    </a>
    <a href="/posts/feature_fanza_vacuum_blowjob_deep_throat_ranking" class="p-3.5 bg-slate-800/80 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-pink-500/50 transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-pink-300 font-medium">【バキュームフェラ・深喉特化】極上口淫で吸い尽くされるAV選</span>
      <span class="text-pink-400 group-hover:translate-x-1 transition">→</span>
    </a>
    <a href="/posts/feature_fanza_luxury_soapland_foam_mat_play_ranking_2026" class="p-3.5 bg-slate-800/80 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-pink-500/50 transition flex items-center justify-between group">
      <span class="text-slate-200 group-hover:text-pink-300 font-medium">【高級ソープ・泡踊り特化】極上マットプレイと生中出し奉仕AV選</span>
      <span class="text-pink-400 group-hover:translate-x-1 transition">→</span>
    </a>
  </div>
</div>

<!-- よくある質問 (FAQ) -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8">
  <h3 class="text-xl font-bold text-white mb-6 flex items-center gap-2">
    <span class="text-pink-400">❓</span> パイズリ・巨乳挟射AVに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-4 text-sm md:text-base">
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-pink-300 mb-2">Q1. パイズリ作品の醍醐味は何ですか？</h4>
      <p class="text-slate-300 leading-relaxed">視覚的な圧倒的豊満バストの迫力、ローションと肌が擦れ合う生々しい水音、そして谷間に包まれて精子を解き放つ至高の母性と快楽です。</p>
    </div>
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-pink-300 mb-2">Q2. 一番美しくて抜けるパイズリ作品はどれですか？</h4>
      <p class="text-slate-300 leading-relaxed">第1位の瀬戸環奈主演作（SONE-912）です。圧倒的なルックスの美女が至近距離で見つめながら丁寧に挟んでしごいてくれる姿は全男子の夢です。</p>
    </div>
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-pink-300 mb-2">Q3. ひたすらパイズリ射精だけを連続で見たい場合は？</h4>
      <p class="text-slate-300 leading-relaxed">第2位の水卜さくら主演作（MIDE-634）がおすすめです。30本のペニスをひたすら胸だけで射精させる圧巻の企画です。</p>
    </div>
  </div>
</div>"""
    html_parts.append(table_and_links)

    # JSON-LD Schema
    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "ItemList",
                "name": "FANZA「極上パイズリ・巨乳挟まれ窒息射精」おすすめ神作ランキングTOP5",
                "description": "たわわな爆乳の谷間に包まれて精子を一滴残らず搾り取られる夢の母性＆快楽AVおすすめランキングTOP5【2026年最新】",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": idx + 1,
                        "name": it.get('title'),
                        "url": it.get('affiliate_url_clean')
                    } for idx, it in enumerate(items)
                ]
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": "パイズリ作品の醍醐味は何ですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "視覚的な圧倒的豊満バストの迫力、ローションと肌が擦れ合う生々しい水音、そして谷間に包まれて精子を解き放つ至高の母性と快楽です。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "一番美しくて抜けるパイズリ作品はどれですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第1位の瀬戸環奈主演作（SONE-912）です。圧倒的なルックスの美女が至近距離で見つめながら丁寧に挟んでしごいてくれます。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "ひたすらパイズリ射精だけを連続で見たい場合は？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第2位の水卜さくら主演作（MIDE-634）がおすすめです。30本のペニスをひたすら胸だけで射精させる圧巻の企画です。"
                        }
                    }
                ]
            }
        ]
    }
    json_ld_script = f'<script type="application/ld+json">\n{json.dumps(json_ld, ensure_ascii=False, indent=2)}\n</script>'
    html_parts.append(json_ld_script)

    full_html = "\n\n".join(html_parts)
    char_count = count_japanese_chars(full_html)
    print(f"Article 3 character count: {char_count} chars")
    if char_count < 3000:
        raise Exception(f"Article 3 is under 3000 chars: {char_count}")

    post_data = {
        "id": "feature_fanza_titfuck_paizuri_huge_breasts_suffocation_ranking_2026",
        "title": "【神乳に埋もれて昇天】FANZA「極上パイズリ・巨乳挟まれ窒息射精」おすすめ神作ランキングTOP5！たわわな爆乳の谷間に包まれて精子を一滴残らず搾り取られる夢の母性＆快楽AV選【2026年最新】",
        "date": "2026-10-05 02:20:00",
        "hinban": "TITFUCK-PAIZURI-SUFFOCATION-2026",
        "price": "300~",
        "maker": "FANZA公式セレクション",
        "actresses": ["瀬戸環奈", "水卜さくら", "夢乃あいか", "蜜美杏", "中山ふみか"],
        "genres": ["パイズリ", "巨乳", "爆乳", "挟射", "窒息", "回春エステ", "射精管理", "搾精", "特集", "殿堂入り"],
        "image": cover_image,
        "review": full_html
    }

    file_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f" -> Successfully saved Article 3 ({char_count} chars) to {file_path}")


def main():
    print("==================================================")
    print("FANZA公式APIリアルタイム取得・超大型キラー特集3記事自動生成開始")
    print("==================================================")
    generate_article_aphrodisiac()
    print("--------------------------------------------------")
    generate_article_papakatsu()
    print("--------------------------------------------------")
    generate_article_paizuri()
    print("==================================================")
    print("3記事すべての生成が正常に完了しました！")
    print("==================================================")

if __name__ == "__main__":
    main()
