# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・超大型キラー特集3記事自動生成スクリプト
1. 【母乳・搾乳・授乳手コキ＆甘やかし母性特化】
   『【母乳滴る極上搾精】FANZA「母乳・授乳手コキ＆甘やかし母性」おすすめ神作ランキングTOP5！たわわに張った乳房から吹き出す甘いミルクを飲み干しながら精子を搾り取られる至福の母性昇天AV選【2026年最新】』
2. 【逆レイプ・連続強制搾精・腰振り騎乗位特化】
   『【男が犯される極限快楽】FANZA「逆レイプ・連続強制搾精・腰振り騎乗位」おすすめ神作ランキングTOP5！肉食美女に拘束され射精後も逃げ場ゼロで金玉が空になるまで搾り取られるドM昇天AV選【2026年最新】』
3. 【初アナル解禁・お尻開発＆2穴同時特化】
   『【禁断の初アナル解禁】FANZA「初アナル解禁・お尻開発＆2穴同時」おすすめ神作ランキングTOP5！清楚美女が未知の快感に悶絶し腰を跳ね上げて連続絶頂する至高のお尻快楽AV選【2026年最新】』
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
    # 記事1: 母乳・授乳・母性甘やかし
    "sone00201": """<h2>『姉はヤンママ授乳中 in 実家 ランク1位総なめの超人気同人！業界屈指の肉感ボディ人気女優！初めての母乳噴出 小宵こなん』詳細レビュー</h2>
<p>圧倒的な肉感グラマラスボディで不動のトップ人気を誇る小宵こなんが、産後ヤンママ姉として実家に里帰りし、弟である主人公に溢れ出る母乳を飲ませながら濃厚な肉欲に溺れるメガヒット作。同人CG原作の傑作シチュエーションを完全実写化した本作は、小宵こなんのむちむちとした太もも、張りのある爆乳、そして本能剥き出しの母性フェロモンが炸裂する至高の1本です。</p>

<h3>見どころ：服の隙間から滲み出る母乳と無防備な胸元</h3>
<p>赤ん坊に母乳をあげている最中に遭遇してしまう背徳の瞬間。胸元をはだけさせ、ピンク色の張った乳首から滴る白いミルクを目の前にした時の興奮は言葉を失うレベルです。「あんたも…飲んでみる？」と悪戯っぽく笑いながら弟を誘惑するこなんちゃんの艶めかしい瞳に、男の理性は一瞬で崩壊します。</p>

<h3>実用ポイント：母乳まみれのパイズリと子宮直撃生交尾</h3>
<p>温かな母乳を胸全体に擦り付け、ローション代わりにペニスを挟み込んでしごき上げる極上パイズリ。さらに「弟の精子でまた孕んじゃう…！」と啼きながら腰を打ち付けてくる濃厚中出しピストンは、実用度・射精圧ともに満点を叩き出します。</p>""",

    "ebwh00365": """<h2>『おっとり優しい兄嫁さんに「母乳飲ませて」とお願いしてみたら…。 柏木ふみか』詳細レビュー</h2>
<p>癒やし系オーラ全開の美人兄嫁・柏木ふみかが、義弟からの甘えん坊なおねだりを断りきれず、禁断の母乳授乳から禁忌の肉体関係へと堕ちていく背徳ドラマ。ふんわりとした柔らかい笑顔と、豊かな胸から溢れ出る母乳の温もりが、鑑賞者の疲れた心と下半身を極限まで包み込みます。</p>

<h3>見どころ：恥じらいながらも母性で受け入れる兄嫁の包容力</h3>
<p>「こんなこと…義弟くんにしちゃダメなのに…」と頬を染めながらも、ゴクゴクと胸に吸い付く男の頭を優しく撫でてあげる柏木ふみか。母性本能をくすぐられて次第に吐息を熱くし、自ら乳首を口元へと押し当ててくる姿に男の独占欲と甘えたい欲求が全開になります。</p>

<h3>実用ポイント：母乳で濡れ光る乳房を揉みしだきながらの正常位</h3>
<p>胸から溢れる母乳を全身に浴びせかけながら、兄に隠れて交わる密着ピストン。兄嫁の柔らかいお腹に男の腰がぶつかり、絶頂の瞬間に「いっぱい出して…」と耳元で囁かれるカタルシスは悶絶必至です。</p>""",

    "snos00372": """<h2>『母性溢れる優し～いお姉ちゃんがおっぱいチューチューちんちんヌキヌキ甘やかしてくれる世界一気持ちいい授乳手コキ 小日向みゆう』詳細レビュー</h2>
<p>ロリフェイスに超弩級のグラマラスボディを誇る小日向みゆうが、全肯定の聖母姉ちゃんとなって弟を全方位から甘やかしてくれるバブみ＆搾精の最高峰。日常のストレスで限界の男をベッドに寝かせ、至福の授乳と超絶技巧の手コキで骨抜きにしてくれます。</p>

<h3>見どころ：赤ちゃん言葉とおっぱいチューチューのダブル攻め</h3>
<p>「よしよし、いい子だねぇ…おっぱいちゅっちゅして元気出そうね」と甘く囁きながら、ふっくら柔らかな巨乳を顔面に押し付けてくるみゆうちゃん。口いっぱいに広がるおっぱいの感触と、耳元で響く囁き声の臨場感は全男子の脳をトロトロに溶かします。</p>

<h3>実用ポイント：緩急自在の授乳手コキによる大量射精</h3>
<p>胸を吸わせながら、下半身ではオイルをたっぷり馴染ませた手で亀頭をじっくり刺激。射精直前には「全部出していいよぉ、お姉ちゃんが受け止めてあげる」と包み込まれ、勢いよく発射される精液を笑顔で見届けてくれる癒やしの極みです。</p>""",

    "dass00945": """<h2>『いっぱいチュウチュウしてね？魅惑的エロ乳輪を押しつけ国宝Iカップ授乳手コキを施してくれるチソポ大好きお姉さん 彩月七緒』詳細レビュー</h2>
<p>国宝級の天然Iカップ美巨乳と妖艶な色香で男性を虜にする彩月七緒が、エロすぎる大きな乳輪を惜しげもなく密着させ、授乳プレイと神業手コキで男の精液を一滴残らず吸い出す特化作。圧巻のボリューム感を誇るバストの迫力は画面越しでも息を呑むほどです。</p>

<h3>見どころ：魅惑の大きめ乳輪と重力無視の肉感バスト</h3>
<p>至近距離で迫る彩月七緒のIカップ乳房。少し茶色がかったエロティックな乳輪を男の唇に押し付け、「ほら、もっと強く吸ってぇ」と催促してくる淫靡な表情は破壊力抜群。視覚的なフェティシズムの最高峰を味わえます。</p>

<h3>実用ポイント：手コキと胸挟み撃ちの同時昇天コンボ</h3>
<p>豊満すぎるバストの谷間にペニスを埋め込み、さらに先端を滑らかな指先で弄ぶ二重責め。逃げ場のない快楽の波に呑まれ、乳房の間へ大量の白濁液をブチ撒ける瞬間は、巨乳・授乳好きにとって至高のエクスタシーです。</p>""",

    "rmer00052": """<h2>『ベロチュウは、母乳味。 水谷梨明日』詳細レビュー</h2>
<p>透明感溢れる美少女・水谷梨明日が、分泌される母乳を口に含み、濃厚なベロキスを通じて男と体液を分かち合う超濃厚フェティシズム作。滴るミルクと絡み合う唾液の生々しい水音が、視聴覚をダイレクトに直撃して男の興奮を最高潮へと導きます。</p>

<h3>見どころ：母乳を口移しされる生々しいディープキス</h3>
<p>張った乳房を自ら揉みしだき、口いっぱいに溜めた母乳を男の口の中へと流し込む水谷梨明日。舌が絡み合い、互いの唾液と母乳が混ざり合って口端から溢れ落ちるシーンは、背徳的フェチの極致と言える映像美とエロスを誇ります。</p>

<h3>実用ポイント：母乳まみれの体液交尾と白濁フィニッシュ</h3>
<p>胸からも口からも母乳を滴らせたまま、濡れそぼる秘部へ激しく突き入れる本番セックス。水谷梨明日が恍惚とした表情でイキ乱れ、最後は胸元と口元へ精子をぶち撒ける濃厚フィニッシュは実用派必見です。</p>""",

    # 記事2: 逆レイプ・連続強制搾精
    "midv00093": """<h2>『「もう吹いてるってばぁ！」深田えいみの逆ナン逆レ●プ痴女ドキュメント 拘束され身動き出来ず、いきなり馬乗り逆レイプ！ 深田えいみ』詳細レビュー</h2>
<p>AV界のレジェンド痴女・深田えいみが、街で見かけた男をホテルに連れ込み、ベッドに手足を拘束して一方的に犯し尽くす伝説の逆レイプドキュメント。男側の意思を完全に無視して跨がり、射精してヘトヘトになっても腰を止めずに連続で精子を搾り取るドS痴女の極致です。</p>

<h3>見どころ：拘束されて抗えない男を見下ろす肉食の笑み</h3>
<p>手足を固定され、ビクビクと反応するペニスを前に「美味しそう…全部吸い取ってあげるね」と妖しく微笑む深田えいみ。強引に口で吸い尽くされ、そのままズブズブと奥深くまで飲み込まれる瞬間の男の情けない喘ぎと、えいみのサディスティックな歓喜が最高にソソります。</p>

<h3>実用ポイント：射精直後も腰を振り続ける強制連射ピストン</h3>
<p>ドピュドピュと膣内に精液を吐き出して「もう出ない…」と懇願する男に対し、「まだまだ！もっと出せるでしょ！」と容赦なく腰をグラインドさせる深田えいみ。敏感すぎる亀頭を締め上げられ、情けなくビクビクと2発目、3発目を搾り取られる快感は悶絶必至です。</p>""",

    "masm00001": """<h2>『くそ生意気なメスガキの姪っ子に大人の俺が「ざこざこざぁ～こ」と罵られて屈服！逆レ搾精されてM堕ちした叔父の僕 松本いちか』詳細レビュー</h2>
<p>小悪魔メスガキ演技の第一人者・松本いちかが、年の離れた叔父を「ざぁ～こ♡早漏チ○ポ♡」と挑発し尽くし、上から跨がって完全に快楽で服従させる逆転搾精のメガヒット作。華奢で小さな身体からは想像もつかないドSな腰使いで、男の尊厳を粉々に粉砕します。</p>

<h3>見どころ：見下し罵倒と容赦ないスローグラインド</h3>
<p>ベッドに押し倒され、上に乗ったいちかちゃんから至近距離でバカにされ続ける至福の屈辱。「大人のくせにこんなのでイキそうになってるの？ざぁこ♡」と囁かれながら、ツボを正確に抉るような腰振りを食らうと、男の理性は瞬時に白旗を上げます。</p>

<h3>実用ポイント：早漏暴発からの強制追撃騎乗位</h3>
<p>我慢できずにあっけなく中出ししてしまった叔父に対し、「えー、もう出しちゃったの？でも抜かないもんねー！」とさらに激しく腰を動かして2回戦に突入。M男ならずとも射精が止まらなくなる超危険な実用作です。</p>""",

    "achj00094": """<h2>『「男は一切動くな。」腰振り痴女が全てを支配する、究極の騎乗位 愛弓りょう』詳細レビュー</h2>
<p>圧倒的な美貌と妖艶なフェロモンを放つ美熟女・愛弓りょうが、男に一切の身動きを禁じ、己の腰振りテクニックだけで男を天国へと送り届ける究極の騎乗位特化作。熟練の女性だけが持ち得る圧巻の締め付けと、緩急自在のグラインドが男の精力を根こそぎ奪い去ります。</p>

<h3>見どころ：完璧な美ボディで見下ろしてくる絶対女王の貫禄</h3>
<p>「あなたは私の腰の動きだけを感じていればいいの…」と冷徹かつ艶やかに告げる愛弓りょう。男の胸に両手を当てて抑え込み、汗を光らせながら腰を縦・横・円を描くように動かしてくる姿は、息を呑むほどの美しさとエロスを誇ります。</p>

<h3>実用ポイント：ツボを外さない極上グラインドと搾り取り</h3>
<p>亀頭の裏筋を的確に刺激する腰使いに、男は腰を浮かせて悶絶。射精の瞬間にはぎゅっと膣奥を収縮させて精液を一滴も漏らさず搾り取る締め付けは、まさに神の領域です。</p>""",

    "jur00752": """<h2>『『はぁはぁ…私が満足するまで、何回イッても終わらせないわよ。』 エアコン修理に来た可愛い青年に超強力媚薬を飲ませて馬乗り逆レイプ中出し さつき芽衣』詳細レビュー</h2>
<p>豊満な肉感ボディと危険な色気を放つ人妻・さつき芽衣が、自宅に修理に来た純朴な青年作業員に媚薬を盛り、身動きの取れなくなった男をベッドに押し倒して跨がり続ける密室逆レイプ作。日常の隙間に潜む狂気と肉欲の暴走がたまらなく刺激的です。</p>

<h3>見どころ：媚薬で身体が動かない男を貪る肉食人妻</h3>
<p>薬で脱力し、下半身だけがビンビンに勃起した青年の作業着を脱がせるさつき芽衣。「若い子のチ○ポってこんなに元気なのね…」と瞳をギラつかせ、涎を垂らしながらペニスに跨がる姿はリアルな狂気とエロスに満ちています。</p>

<h3>実用ポイント：重量感あふれるヒップの杭打ちピストン</h3>
<p>むっちりとした重みのあるお尻を青年の股間に打ち付け、自らアヘ顔を晒してイキ狂うさつき芽衣。青年が喘ぎながら何度も中出ししても、満足するまで腰を止めないド迫力の連続性交は圧巻です。</p>""",

    "cjod00380": """<h2>『僕をダメにするド痴女ナース 寝込みを襲われぐっちょり涎ベロキス＆杭打ちピストン中出しでチ○ポバカになるまで搾り取られた入院生活 藤森里穂』詳細レビュー</h2>
<p>ド痴女役で右に出る者のいない藤森里穂が、入院患者のベッドに夜な夜な忍び込み、点滴で動けない男を夜這い逆レイプして徹底的にザーメンを搾取する病棟エロス。ぐっちょりと音を立てるディープキスと、容赦ない杭打ちピストンのコンボで男を快楽漬けにします。</p>

<h3>見どころ：ナース服をめくり上げて跨がる夜這い侵入</h3>
<p>消灯後の薄暗い病室で、寝ている患者の布団をめくり、勃起したペニスを即座に咥え込む藤森里穂。白衣をはだけさせて豊満な胸と下腹部を押し当ててくる臨場感に、背徳の心拍数が跳ね上がります。</p>

<h3>実用ポイント：涎まみれのベロキスと激震杭打ちピストン</h3>
<p>男の口を自分の舌で塞ぎ、喘ぎ声を封じ込めながら下半身で激しい杭打ちピストンを連発。「入院中なんだから、全部私に出して元気になって？」と淫語を浴びせながらの連続搾精は実用度無限大です。</p>""",

    # 記事3: 初アナル解禁・2穴同時
    "miab00284": """<h2>『花狩まい アナル解禁！』詳細レビュー</h2>
<p>愛くるしいルックスと抜群のスタイルで大人気の専属女優・花狩まいが、ついに禁断の肛門処女を捧げた伝説のアナル解禁ドキュメント。痛みに怯えながらも、丁寧な前戯とお尻開発によって未知の快楽に目覚め、最後はアナルアクメで腰をビクビク跳ね上げる姿は全ファン必見です。</p>

<h3>見どころ：お尻を広げられて羞恥に染まる初々しい表情</h3>
<p>カメラの前でピンク色の肛門を露わにし、ローションを塗り込まれて指でほぐされていく花狩まい。「恥ずかしい…」と手で顔を覆いながらも、窄まりが徐々に開いていく様子が超高画質で克明に記録されています。</p>

<h3>実用ポイント：太い男根が菊座を押し広げて進入する瞬間</h3>
<p>先端がアナルにめり込み、ズブズブと根元まで飲み込まれた瞬間、花狩まいの瞳からポロリと涙が零れ落ちます。そして激しいピストンとともに痛みが歓喜の絶頂へと変わり、お尻を締め付けてヨガる姿は抜きの極致です。</p>""",

    "mism00185": """<h2>『アナル解禁AVデビュー！ しとやかに…しなやかに…肛門マゾアクメ 中条鈴華』詳細レビュー</h2>
<p>上品でしとやかな美貌を持つ中条鈴華が、AVデビュー作にしてまさかのアナル解禁を果たすという前代未聞の衝撃作。清楚なお嬢様風の美女が、アナルを犯されることで眠っていた超ドMの淫乱本能を呼び覚まされるドラマチックな展開に引き込まれます。</p>

<h3>見どころ：清楚美女がアナルを貫かれて白目を剥くギャップ</h3>
<p>静かな語り口から一転、肛門に硬いペニスを挿入された瞬間に「あぁっ…！お尻が裂けちゃう…！」と激しく身悶えする中条鈴華。細い腰をくねらせ、次第にお尻の快感に抗えなくなっていく表情の変化がたまらなく淫靡です。</p>

<h3>実用ポイント：アナルからの連続潮吹き＆絶叫痙攣</h3>
<p>前方の秘部には一切触れていないにもかかわらず、アナルへの深突きピストンだけで何度も潮を吹き出し、手足を硬直させてイキ狂う姿は圧巻。本物のアナルマゾだけが見せる至高の官能絵巻です。</p>""",

    "cemd00885": """<h2>『1本限りのアナルSEX復活！ 泉りおん ～これで見納め！？～撮影中にアナルSEXを交渉してみた～』詳細レビュー</h2>
<p>伝説のアナルクイーン・泉りおんが、現場での突然の交渉によって奇跡的に1本限りのお尻解禁に応じたプレミアム作。熟練のテクニックと超人的な肛門感度を誇る彼女が、男根をすんなりと飲み込み、極上の締め付けでお尻交尾を披露してくれます。</p>

<h3>見どころ：プロの矜持を感じさせる極上のアナルご奉仕</h3>
<p>交渉成立後、自ら四つん這いになってお尻を突き出し、アナルを広げて見せる泉りおん。ペニスが吸い込まれるように進入し、全く苦痛を感じさせずに微笑みながらお尻を振る姿は、まさにアナル界の至宝です。</p>

<h3>実用ポイント：奥深くまで抉られる激アナルピストンと中出し</h3>
<p>バックから容赦なくアナル最深部を打ち据える剛棒。泉りおんは舌を出し、アヘ顔を晒しながら「アナル気持ちいいぃ！」と絶叫。最後は肛門の奥深くに白濁液をドピュドピュと流し込まれる完璧なフィニッシュです。</p>""",

    "cemd00741": """<h2>『1本限りのアナルSEX復活！ 森沢かな ～これで見納め！？～撮影中にアナルSEXを交渉してみた～』詳細レビュー</h2>
<p>完璧な美貌と妖艶なフェロモンを誇るトップ女優・森沢かなが、撮影現場の熱気の中で突如アナル解禁を承諾した奇跡のドキュメント。美しく引き締まった極上のヒップラインと、狭い肛門が極太男根を飲み込んでいくコントラストが男の本能を狂わせます。</p>

<h3>見どころ：恥じらいと興奮が入り混じる大人のアナル交渉</h3>
<p>「えっ、本当にお尻でするの…？」と戸惑いを見せながらも、下半身の疼きに勝てずに承諾してしまう森沢かな。大人の色香漂う美女が、お尻の穴をカメラに向けられて赤面する姿は興奮度MAXです。</p>

<h3>実用ポイント：美尻を叩きつけるような激しいアナルバック</h3>
<p>形の良い美尻を背後から激しく突かれ、肉がぶつかり合う音を響かせながらヨガる森沢かな。肛門がひくひくと収縮し、男のペニスを締め上げる圧巻の快感は、美熟女・アナルフェチの射精中枢を直撃します。</p>""",

    "mism00106": """<h2>『アナル解禁！2穴ファック解禁！本格緊縛解禁！浣腸解禁！ 最上さゆき』詳細レビュー</h2>
<p>異常なまでのM感度を誇る最上さゆきが、アナル、2穴同時、緊縛、浣腸のすべてを一挙に解禁した伝説のハードコア作。全身を縄で縛り上げられ、前後の穴を同時に貫かれて限界アクメを連発する姿は、AV史に残る壮絶な美しさとエロスを誇ります。</p>

<h3>見どころ：2穴同時挿入で逃げ場を失った極限の快楽</h3>
<p>前方の膣と後方のアナルの両方に極太ペニスが突き刺さり、同時に激しくピストンされる2穴ファック。身動きが取れない中で、二つの穴を激しく拡張された最上さゆきが、涎を垂らしながら白目を剥く姿は圧巻の一言です。</p>

<h3>実用ポイント：緊縛拘束下での前後同時射精フィニッシュ</h3>
<p>限界まで責め抜かれた後、前後の穴から同時に大量の精液を注ぎ込まれる圧巻のクライマックス。マゾヒズムの極限に達した彼女の痙攣する身体と蕩けきった表情は、他では決して味わえない究極の実用度を誇ります。</p>"""
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
        
    act_str = "・".join(acts) if acts else "人気女優"
    
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
# 記事1: 母乳・授乳手コキ＆甘やかし母性 特化
# ==============================================================================
def generate_article_lactation():
    print("=== Generating Article 1: 母乳・授乳手コキ＆甘やかし母性特化 ===")
    cids = ["sone00201", "ebwh00365", "snos00372", "dass00945", "rmer00052"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["母乳", "授乳手コキ", "母性", "パイズリ", "甘やかし", "殿堂入り"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 1 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-amber-950/40 via-slate-900 to-slate-950 border border-amber-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-amber-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-amber-500/20 text-amber-300 border border-amber-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">LACTATION & MATERNAL ECSTASY SPECIAL</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月05日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【母乳滴る極上搾精】FANZA「母乳・授乳手コキ＆甘やかし母性」おすすめ神作ランキングTOP5！たわわに張った乳房から吹き出す甘いミルクを飲み干しながら精子を搾り取られる至福の母性昇天AV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    男なら誰もが心の奥底に秘めている「限界まで甘やかされたい」「優しいお姉さんや人妻の胸に抱かれて全てを肯定されたい」という原初の願望。そんな究極の癒やしと本能的エロティシズムが融合した奇跡のジャンル、それが「母乳・授乳手コキ・母性搾精モノ」です。日々のプレッシャーや孤独で疲れ切った男性の心と身体を、温かな母乳と包容力抜群のバストが全方位から優しく包み込みます。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    パンパンに張りつめた乳房のピンク色に透き通る乳首から、ピュッと勢いよく吹き出す白い母乳。それを口いっぱいに吸いながら、下半身では手や太ももで丁寧にペニスをしごかれ、「よしよし、いっぱいたまってたね…全部出してスッキリしようね」と耳元で囁かれる至福の体験は、他のどんなハードプレイでも味わえない圧倒的な幸福感と濃密な射精快感をもたらします。母乳の滴る肌の滑らかさと、甘い香りに包まれたベッドでの交尾はまさに極楽浄土です。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、同人原作の実写化で記録的メガヒットを飛ばした小宵こなんのヤンママ里帰り授乳作から、柏木ふみかの優しいおっとり兄嫁母乳プレイ、小日向みゆうの全肯定バブみ授乳手コキ、彩月七緒の国宝Iカップ大乳輪授乳、水谷梨明日の母乳口移しベロキスまで、母性と実用度の頂点を極めた【母乳・授乳神作TOP5】を徹底比較・レビューします。
  </p>
</div>

<!-- 選び方の基準 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-amber-400">🍼</span> 母乳・授乳手コキ作品で至福の昇天を迎える3大チェックポイント
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-amber-300 mb-2">① 母乳の噴出量と滴る生々しいシズル感</h4>
      <p class="text-slate-300 leading-relaxed">ただ胸を揉むだけでなく、乳首をつまんだ瞬間にピュッとミルクが噴き出す視覚的インパクトや、胸元を白く染めるシズル感が抜きどころを左右します。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-amber-300 mb-2">② 全肯定してくれる聖母のような甘やかし音声</h4>
      <p class="text-slate-300 leading-relaxed">「いっぱい飲んでね」「いい子いい子」など、男のプライドを解きほぐす優しい囁きやバブみ溢れるセリフ回しが射精圧を何倍にも引き上げます。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-amber-300 mb-2">③ 母乳を潤滑油にしたパイズリ＆生交尾</h4>
      <p class="text-slate-300 leading-relaxed">噴き出た温かい母乳をローション代わりにペニスへ塗りたくり、胸で挟んで擦り上げるパイズリや、体液まみれで子宮に注ぎ込む生中出しの結合度が極上です。</p>
    </div>
  </div>
</div>

<!-- 目次 -->
<div class="my-8 bg-slate-900/60 border border-slate-800 rounded-2xl p-5 shadow-inner">
  <h4 class="text-sm font-bold text-slate-300 mb-3 flex items-center gap-2">
    <span>📑</span> 目次：おすすめランキングTOP5
  </h4>
  <ul class="space-y-2 text-xs md:text-sm text-amber-400/90 font-medium">
    <li><a href="#rank-1" class="hover:underline flex items-center justify-between"><span>第1位：姉はヤンママ授乳中 in 実家（小宵こなん）</span><span class="text-slate-500 text-xs">同人原作の金字塔</span></a></li>
    <li><a href="#rank-2" class="hover:underline flex items-center justify-between"><span>第2位：おっとり優しい兄嫁さんに「母乳飲ませて」とお願いしてみたら…（柏木ふみか）</span><span class="text-slate-500 text-xs">背徳の親族授乳</span></a></li>
    <li><a href="#rank-3" class="hover:underline flex items-center justify-between"><span>第3位：母性溢れる優し～いお姉ちゃんがおっぱいチューチュー（小日向みゆう）</span><span class="text-slate-500 text-xs">究極の全肯定バブみ</span></a></li>
    <li><a href="#rank-4" class="hover:underline flex items-center justify-between"><span>第4位：いっぱいチュウチュウしてね？魅惑的エロ乳輪Iカップ（彩月七緒）</span><span class="text-slate-500 text-xs">国宝級の乳輪フェチ</span></a></li>
    <li><a href="#rank-5" class="hover:underline flex items-center justify-between"><span>第5位：ベロチュウは、母乳味。（水谷梨明日）</span><span class="text-slate-500 text-xs">濃厚口移し体液交尾</span></a></li>
  </ul>
</div>"""
    html_parts.append(intro_html)

    # 各作品の詳細レビュー
    reviews_detail = [
        # 第1位: 小宵こなん
        """<div id="rank-1" class="my-10 bg-slate-900 border-2 border-amber-500/40 rounded-2xl p-6 md:p-8 shadow-2xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-3">
      <span class="bg-gradient-to-r from-amber-500 to-yellow-400 text-slate-950 text-sm md:text-base font-black px-4 py-1 rounded-full shadow-lg">第1位（殿堂入り）</span>
      <h3 class="text-lg md:text-2xl font-black text-white">姉はヤンママ授乳中 in 実家 小宵こなん</h3>
    </div>
    <div class="text-xs text-slate-400">品番：SONE-00201 / 出演：""" + get_actress_link("小宵こなん") + """</div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <div class="space-y-4">
      <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dsone00201%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="block group relative overflow-hidden rounded-xl border border-slate-700">
        <img src="https://pics.dmm.co.jp/digital/video/sone00201/sone00201pl.jpg" alt="姉はヤンママ授乳中 in 実家 小宵こなん" class="w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-4">
          <span class="text-white text-xs font-bold bg-rose-600/90 px-3 py-1 rounded-full">FANZA公式で作品詳細を見る →</span>
        </div>
      </a>
      <div class="flex flex-wrap gap-2">
        """ + get_genre_link("母乳") + " " + get_genre_link("授乳手コキ") + " " + get_genre_link("巨乳") + " " + get_genre_link("人妻") + " " + get_genre_link("中出し") + """
      </div>
    </div>
    <div class="space-y-4 text-xs md:text-sm text-slate-300 leading-relaxed">
      <p class="font-bold text-amber-200">【解説・作品の魅力】</p>
      <p>同人CG界で圧倒的な売上を記録した伝説のタイトルを、業界屈指のグラマラスボディを誇る小宵こなんが奇跡の完全実写化。里帰り出産で実家に戻ってきたヤンママの姉が、人妻の色香と溢れ出す母乳を武器に弟を誘惑する傑作です。無防備に開かれた胸元から覗くパンパンに張った乳房と、少し悪戯っぽい笑みで弟を見つめる表情の破壊力は他の追随を許しません。</p>
      <p>赤ん坊を寝かしつけた後、薄暗い和室で始まるふたりだけの秘密の授乳タイム。「弟の分もいっぱい出ちゃうなぁ…」と呟きながら、母乳でツヤツヤに濡れた乳首を口元へ押し当ててくるシーンは、男の甘えたい本能を限界まで刺激します。</p>
      <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
        <p class="text-amber-300 font-bold mb-1">🔥 絶対に抜ける神シーン・実用ポイント</p>
        <p class="text-slate-300">母乳で滑らかになった胸の谷間にペニスをすっぽり挟み込まれる濃厚パイズリから、弟の肉棒に跨がって自ら腰を打ち付ける激しい騎乗位。胸が大きく上下に揺れるたびにミルクが飛び散り、「弟の種でまた孕んじゃう！」と啼き叫びながら迎える中出しフィニッシュは実用度120%です。</p>
      </div>
      <div class="pt-2">
        <a href="/posts/sone00201" class="text-xs text-amber-400 hover:text-amber-300 underline font-bold">👉 作品個別ページ（サンプル画像・詳細レビュー）を見る</a>
      </div>
    </div>
  </div>

  <div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-6">
    <img src="https://pics.dmm.co.jp/digital/video/sone00201/sone00201-1.jpg" alt="サンプル画像1" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/sone00201/sone00201-2.jpg" alt="サンプル画像2" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/sone00201/sone00201-3.jpg" alt="サンプル画像3" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/sone00201/sone00201-4.jpg" alt="サンプル画像4" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
  </div>

  <div class="text-center">
    <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dsone00201%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-2 bg-gradient-to-r from-amber-500 via-rose-500 to-amber-500 hover:opacity-95 text-white font-black text-sm md:text-base px-8 py-4 rounded-xl shadow-xl transition transform hover:scale-105">
      <span>今すぐFANZA公式で『姉はヤンママ授乳中』をフル視聴する</span>
      <span>🚀</span>
    </a>
  </div>
</div>""",

        # 第2位: 柏木ふみか
        """<div id="rank-2" class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-3">
      <span class="bg-slate-700 text-amber-300 text-sm md:text-base font-black px-4 py-1 rounded-full">第2位</span>
      <h3 class="text-lg md:text-2xl font-black text-white">おっとり優しい兄嫁さんに「母乳飲ませて」とお願いしてみたら… 柏木ふみか</h3>
    </div>
    <div class="text-xs text-slate-400">品番：EBWH-00365 / 出演：""" + get_actress_link("柏木ふみか") + """</div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <div class="space-y-4">
      <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Debwh00365%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="block group relative overflow-hidden rounded-xl border border-slate-700">
        <img src="https://pics.dmm.co.jp/digital/video/ebwh00365/ebwh00365pl.jpg" alt="おっとり優しい兄嫁さんに「母乳飲ませて」とお願いしてみたら… 柏木ふみか" class="w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-4">
          <span class="text-white text-xs font-bold bg-rose-600/90 px-3 py-1 rounded-full">FANZA公式で作品詳細を見る →</span>
        </div>
      </a>
      <div class="flex flex-wrap gap-2">
        """ + get_genre_link("母乳") + " " + get_genre_link("兄嫁") + " " + get_genre_link("人妻") + " " + get_genre_link("パイズリ") + " " + get_genre_link("中出し") + """
      </div>
    </div>
    <div class="space-y-4 text-xs md:text-sm text-slate-300 leading-relaxed">
      <p class="font-bold text-amber-200">【解説・作品の魅力】</p>
      <p>おっとりとして誰にでも優しい理想の兄嫁・柏木ふみかが、義弟からの無茶な甘えを断りきれず、禁忌の母乳授乳を受け入れてしまう背徳ドラマの最高峰。ふんわりとした柔らかい癒やしの笑顔と、服の上からでもはっきりとわかる豊満バストの存在感が男の背徳感を極限まで高めます。</p>
      <p>「義弟くんに母乳をあげるなんて変だよ…」と困惑しながらも、夢中になって胸に吸い付く義弟の頭をそっと撫でてしまう母性本能。次第に乳首への刺激で下腹部を疼かせ、瞳を潤ませながら自ら衣服を脱ぎ捨てていく心理変化が実に艶やかです。</p>
      <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
        <p class="text-amber-300 font-bold mb-1">🔥 絶対に抜ける神シーン・実用ポイント</p>
        <p class="text-slate-300">母乳を胸全体に伸ばしながら、義弟のペニスを優しく包み込む柏木ふみか。兄に隠れて行われるベッドでの正常位では、母乳で白く濡れた乳房を激しく揉みしだかれ、涙目で「兄さんには内緒だよ…」と中出しを受け入れる姿が最高に抜けます。</p>
      </div>
      <div class="pt-2">
        <a href="/posts/ebwh00365" class="text-xs text-amber-400 hover:text-amber-300 underline font-bold">👉 作品個別ページ（サンプル画像・詳細レビュー）を見る</a>
      </div>
    </div>
  </div>

  <div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-6">
    <img src="https://pics.dmm.co.jp/digital/video/ebwh00365/ebwh00365-1.jpg" alt="サンプル画像1" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/ebwh00365/ebwh00365-2.jpg" alt="サンプル画像2" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/ebwh00365/ebwh00365-3.jpg" alt="サンプル画像3" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/ebwh00365/ebwh00365-4.jpg" alt="サンプル画像4" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
  </div>

  <div class="text-center">
    <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Debwh00365%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-2 bg-slate-800 hover:bg-slate-700 text-amber-300 border border-amber-500/40 font-bold text-sm md:text-base px-8 py-3.5 rounded-xl shadow-lg transition">
      <span>FANZA公式で『おっとり優しい兄嫁さんに母乳飲ませて』を見る →</span>
    </a>
  </div>
</div>""",

        # 第3位: 小日向みゆう
        """<div id="rank-3" class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-3">
      <span class="bg-slate-700 text-amber-300 text-sm md:text-base font-black px-4 py-1 rounded-full">第3位</span>
      <h3 class="text-lg md:text-2xl font-black text-white">母性溢れる優し～いお姉ちゃんがおっぱいチューチュー 小日向みゆう</h3>
    </div>
    <div class="text-xs text-slate-400">品番：SNOS-00372 / 出演：""" + get_actress_link("小日向みゆう（清原みゆう）") + """</div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <div class="space-y-4">
      <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dsnos00372%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="block group relative overflow-hidden rounded-xl border border-slate-700">
        <img src="https://pics.dmm.co.jp/digital/video/snos00372/snos00372pl.jpg" alt="小日向みゆう 授乳手コキ" class="w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-4">
          <span class="text-white text-xs font-bold bg-rose-600/90 px-3 py-1 rounded-full">FANZA公式で作品詳細を見る →</span>
        </div>
      </a>
      <div class="flex flex-wrap gap-2">
        """ + get_genre_link("授乳手コキ") + " " + get_genre_link("姉") + " " + get_genre_link("甘やかし") + " " + get_genre_link("巨乳") + " " + get_genre_link("手コキ") + """
      </div>
    </div>
    <div class="space-y-4 text-xs md:text-sm text-slate-300 leading-relaxed">
      <p class="font-bold text-amber-200">【解説・作品の魅力】</p>
      <p>究極の童顔フェイスと弾力溢れる超ド級バストを持つ小日向みゆうが、疲れ果てた男を全て肯定して包み込んでくれる聖母シチュエーションの最高傑作。ベッドに横たわる男の上に優しく覆いかぶさり、甘い言葉を絶え間なく囁きながら授乳と手コキを施してくれます。</p>
      <p>「今日も頑張ったね、よしよし…」と頭を撫でられながら、柔らかな胸を顔全体に押し付けられる多幸感。赤ん坊のように無心でおっぱいを吸いながら、下半身を極上テクニックで責め立てられると、日頃のストレスや悩みが完全に吹き飛びます。</p>
      <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
        <p class="text-amber-300 font-bold mb-1">🔥 絶対に抜ける神シーン・実用ポイント</p>
        <p class="text-slate-300">胸を吸わせながら行うスローテンポの手コキから、クライマックスにかけての神速ストローク。小日向みゆうの優しい笑顔に見守られながら、「いっぱい出していいよぉ」と手のひらに大量の精液を受け止めてもらう瞬間はまさに極楽浄土です。</p>
      </div>
      <div class="pt-2">
        <a href="/posts/snos00372" class="text-xs text-amber-400 hover:text-amber-300 underline font-bold">👉 作品個別ページ（サンプル画像・詳細レビュー）を見る</a>
      </div>
    </div>
  </div>

  <div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-6">
    <img src="https://pics.dmm.co.jp/digital/video/snos00372/snos00372-1.jpg" alt="サンプル画像1" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/snos00372/snos00372-2.jpg" alt="サンプル画像2" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/snos00372/snos00372-3.jpg" alt="サンプル画像3" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/snos00372/snos00372-4.jpg" alt="サンプル画像4" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
  </div>

  <div class="text-center">
    <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dsnos00372%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-2 bg-slate-800 hover:bg-slate-700 text-amber-300 border border-amber-500/40 font-bold text-sm md:text-base px-8 py-3.5 rounded-xl shadow-lg transition">
      <span>FANZA公式で『小日向みゆう 授乳手コキ』を見る →</span>
    </a>
  </div>
</div>""",

        # 第4位: 彩月七緒
        """<div id="rank-4" class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-3">
      <span class="bg-slate-700 text-amber-300 text-sm md:text-base font-black px-4 py-1 rounded-full">第4位</span>
      <h3 class="text-lg md:text-2xl font-black text-white">国宝Iカップ授乳手コキ 彩月七緒</h3>
    </div>
    <div class="text-xs text-slate-400">品番：DASS-00945 / 出演：""" + get_actress_link("彩月七緒") + """</div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <div class="space-y-4">
      <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Ddass00945%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="block group relative overflow-hidden rounded-xl border border-slate-700">
        <img src="https://pics.dmm.co.jp/digital/video/dass00945/dass00945pl.jpg" alt="彩月七緒 国宝Iカップ授乳手コキ" class="w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-4">
          <span class="text-white text-xs font-bold bg-rose-600/90 px-3 py-1 rounded-full">FANZA公式で作品詳細を見る →</span>
        </div>
      </a>
      <div class="flex flex-wrap gap-2">
        """ + get_genre_link("巨乳") + " " + get_genre_link("授乳手コキ") + " " + get_genre_link("乳輪") + " " + get_genre_link("フェティッシュ") + " " + get_genre_link("手コキ") + """
      </div>
    </div>
    <div class="space-y-4 text-xs md:text-sm text-slate-300 leading-relaxed">
      <p class="font-bold text-amber-200">【解説・作品の魅力】</p>
      <p>圧巻の天然Iカップバストとフェロモン全開の妖艶ボディを誇る彩月七緒が、エロティックな大きな乳輪を男の顔面に押し当てて骨抜きにするフェチ特化の快作。その重量感ある胸の迫力は画面越しでも圧倒的で、乳輪フェチ・巨乳フェチなら一瞬で昇天する魔力を持っています。</p>
      <p>至近距離で見つめられながら、「いっぱいチューチューしてね？」と肉厚な乳首を口元へ押し込まれる贅沢。吸い付くたびに彩月七緒の甘い吐息が耳元をくすぐり、視覚と聴覚のダブル責めで興奮が限界突破します。</p>
      <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
        <p class="text-amber-300 font-bold mb-1">🔥 絶対に抜ける神シーン・実用ポイント</p>
        <p class="text-slate-300">巨大なIカップでペニスをすっぽり包み込みながら、両手で巧みに竿をしごき上げる二重奏パイズリ＆手コキ。暴発寸前の肉棒から吹き出す大量のザーメンを、胸の谷間と手のひらいっぱいに受け止めるフィニッシュは必見です。</p>
      </div>
      <div class="pt-2">
        <a href="/posts/dass00945" class="text-xs text-amber-400 hover:text-amber-300 underline font-bold">👉 作品個別ページ（サンプル画像・詳細レビュー）を見る</a>
      </div>
    </div>
  </div>

  <div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-6">
    <img src="https://pics.dmm.co.jp/digital/video/dass00945/dass00945-1.jpg" alt="サンプル画像1" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/dass00945/dass00945-2.jpg" alt="サンプル画像2" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/dass00945/dass00945-3.jpg" alt="サンプル画像3" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/dass00945/dass00945-4.jpg" alt="サンプル画像4" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
  </div>

  <div class="text-center">
    <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Ddass00945%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-2 bg-slate-800 hover:bg-slate-700 text-amber-300 border border-amber-500/40 font-bold text-sm md:text-base px-8 py-3.5 rounded-xl shadow-lg transition">
      <span>FANZA公式で『彩月七緒 国宝Iカップ授乳手コキ』を見る →</span>
    </a>
  </div>
</div>""",

        # 第5位: 水谷梨明日
        """<div id="rank-5" class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-3">
      <span class="bg-slate-700 text-amber-300 text-sm md:text-base font-black px-4 py-1 rounded-full">第5位</span>
      <h3 class="text-lg md:text-2xl font-black text-white">ベロチュウは、母乳味。 水谷梨明日</h3>
    </div>
    <div class="text-xs text-slate-400">品番：RMER-00052 / 出演：""" + get_actress_link("水谷梨明日") + """</div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <div class="space-y-4">
      <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Drmer00052%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="block group relative overflow-hidden rounded-xl border border-slate-700">
        <img src="https://pics.dmm.co.jp/digital/video/rmer00052/rmer00052pl.jpg" alt="ベロチュウは、母乳味。 水谷梨明日" class="w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-4">
          <span class="text-white text-xs font-bold bg-rose-600/90 px-3 py-1 rounded-full">FANZA公式で作品詳細を見る →</span>
        </div>
      </a>
      <div class="flex flex-wrap gap-2">
        """ + get_genre_link("母乳") + " " + get_genre_link("キス・ベロキス") + " " + get_genre_link("美少女") + " " + get_genre_link("中出し") + " " + get_genre_link("美乳") + """
      </div>
    </div>
    <div class="space-y-4 text-xs md:text-sm text-slate-300 leading-relaxed">
      <p class="font-bold text-amber-200">【解説・作品の魅力】</p>
      <p>瑞々しい透明感と整った顔立ちが魅力の水谷梨明日が、母乳を口に含んで舌を絡め合わせるディープキスに挑んだ異色のフェチ名作。互いの唾液と母乳が混ざり合って口元から垂れ落ちる生々しい描写は、背徳感とエロティシズムの極致です。</p>
      <p>自らの乳房を揉んでミルクを口内に溜め、それを男の口へと流し込む水谷梨明日。喉を鳴らしながら飲み干す男を見つめる恍惚の表情が、見る者の射精中枢を容赦なく刺激します。</p>
      <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
        <p class="text-amber-300 font-bold mb-1">🔥 絶対に抜ける神シーン・実用ポイント</p>
        <p class="text-slate-300">母乳の味に酔いしれながら交わす濃厚なピストン。舌を吸われながら膣奥を激しく突かれ、水谷梨明日が白目を剥いてアクメに達する結合シーンは必見。体液のリアルな音が響き渡る濃密な抜きどころです。</p>
      </div>
      <div class="pt-2">
        <a href="/posts/rmer00052" class="text-xs text-amber-400 hover:text-amber-300 underline font-bold">👉 作品個別ページ（サンプル画像・詳細レビュー）を見る</a>
      </div>
    </div>
  </div>

  <div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-6">
    <img src="https://pics.dmm.co.jp/digital/video/rmer00052/rmer00052-1.jpg" alt="サンプル画像1" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/rmer00052/rmer00052-2.jpg" alt="サンプル画像2" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/rmer00052/rmer00052-3.jpg" alt="サンプル画像3" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/rmer00052/rmer00052-4.jpg" alt="サンプル画像4" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
  </div>

  <div class="text-center">
    <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Drmer00052%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-2 bg-slate-800 hover:bg-slate-700 text-amber-300 border border-amber-500/40 font-bold text-sm md:text-base px-8 py-3.5 rounded-xl shadow-lg transition">
      <span>FANZA公式で『ベロチュウは、母乳味。』を見る →</span>
    </a>
  </div>
</div>"""
    ]
    html_parts.extend(reviews_detail)

    # 比較まとめテーブル ＆ 内部リンク ＆ FAQ
    table_and_links = """<!-- スペック比較テーブル -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl overflow-hidden">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>📊</span> おすすめ母乳・授乳手コキ神作5選 徹底スペック比較表
  </h3>
  <div class="overflow-x-auto">
    <table class="w-full text-xs md:text-sm text-left text-slate-300">
      <thead class="bg-slate-800 text-amber-300 border-b border-slate-700 uppercase">
        <tr>
          <th class="py-3 px-4">順位 / タイトル</th>
          <th class="py-3 px-4">主演女優</th>
          <th class="py-3 px-4">母性・バブみ度</th>
          <th class="py-3 px-4">実用度・射精圧</th>
          <th class="py-3 px-4">公式リンク</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800">
        <tr class="hover:bg-slate-800/40">
          <td class="py-3 px-4 font-bold text-white">第1位 姉はヤンママ授乳中 in 実家</td>
          <td class="py-3 px-4">""" + get_actress_link("小宵こなん") + """</td>
          <td class="py-3 px-4 text-amber-400">★★★★★（神作）</td>
          <td class="py-3 px-4 text-rose-400">★★★★★（限界突破）</td>
          <td class="py-3 px-4"><a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dsone00201%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="text-amber-400 underline font-bold">FANZAで確認</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="py-3 px-4 font-bold text-white">第2位 おっとり優しい兄嫁さんに母乳飲ませて</td>
          <td class="py-3 px-4">""" + get_actress_link("柏木ふみか") + """</td>
          <td class="py-3 px-4 text-amber-400">★★★★★（聖母）</td>
          <td class="py-3 px-4 text-rose-400">★★★★☆（超濃厚）</td>
          <td class="py-3 px-4"><a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Debwh00365%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="text-amber-400 underline font-bold">FANZAで確認</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="py-3 px-4 font-bold text-white">第3位 お姉ちゃんがおっぱいチューチュー</td>
          <td class="py-3 px-4">""" + get_actress_link("小日向みゆう（清原みゆう）") + """</td>
          <td class="py-3 px-4 text-amber-400">★★★★★（全肯定）</td>
          <td class="py-3 px-4 text-rose-400">★★★★☆（極楽手コキ）</td>
          <td class="py-3 px-4"><a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dsnos00372%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="text-amber-400 underline font-bold">FANZAで確認</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="py-3 px-4 font-bold text-white">第4位 国宝Iカップ授乳手コキ</td>
          <td class="py-3 px-4">""" + get_actress_link("彩月七緒") + """</td>
          <td class="py-3 px-4 text-amber-400">★★★★☆（巨乳包容）</td>
          <td class="py-3 px-4 text-rose-400">★★★★★（大乳輪迫力）</td>
          <td class="py-3 px-4"><a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Ddass00945%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="text-amber-400 underline font-bold">FANZAで確認</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="py-3 px-4 font-bold text-white">第5位 ベロチュウは、母乳味。</td>
          <td class="py-3 px-4">""" + get_actress_link("水谷梨明日") + """</td>
          <td class="py-3 px-4 text-amber-400">★★★★☆（甘口フェチ）</td>
          <td class="py-3 px-4 text-rose-400">★★★★☆（生体液興奮）</td>
          <td class="py-3 px-4"><a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Drmer00052%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="text-amber-400 underline font-bold">FANZAで確認</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- 関連特集への内部リンク -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>🔗</span> あわせて読みたい！おすすめキラー特集記事
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs md:text-sm">
    <a href="/posts/feature_fanza_titfuck_paizuri_huge_breasts_suffocation_ranking_2026" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-amber-500/50 transition block">
      <div class="font-bold text-amber-300 mb-1">【神乳に埋もれて昇天】極上パイズリ・巨乳挟まれ窒息射精ランキングTOP5</div>
      <p class="text-slate-400 line-clamp-2">たわわな爆乳の谷間に包まれて精子を一滴残らず搾り取られる夢の母性＆快楽AV選！</p>
    </a>
    <a href="/posts/feature_fanza_aphrodisiac_drugged_ecstasy_spasm_ranking_2026" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-rose-500/50 transition block">
      <div class="font-bold text-rose-300 mb-1">【理性崩壊の肉欲痙攣】媚薬・キメセク・ガンギマリ発情おすすめ神作TOP5</div>
      <p class="text-slate-400 line-clamp-2">清楚美女が超強力媚薬で白目を剥いて腰を振り乱す限界潮吹き交尾AV選！</p>
    </a>
  </div>
</div>

<!-- よくある質問（FAQ） -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>❓</span> 母乳・授乳手コキAVに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-4 text-xs md:text-sm">
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-amber-300 mb-2">Q1. 母乳AVの魅力・一番の抜きどころはどこですか？</h4>
      <p class="text-slate-300 leading-relaxed">ただのセックスとは異なり、男性の「全肯定されたい」「甘えたい」という根源的欲求を満たしながら、視覚的な白い母乳の噴出と体温を感じる生々しい接触が味わえる点です。</p>
    </div>
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-amber-300 mb-2">Q2. 初めて母乳モノを見るならどの作品がおすすめですか？</h4>
      <p class="text-slate-300 leading-relaxed">第1位の小宵こなん主演作（SONE-00201）が圧倒的におすすめです。同人人気作の実写化でストーリー性、女優の美貌と肉体、母乳のクオリティすべてが最高水準です。</p>
    </div>
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-amber-300 mb-2">Q3. 手コキでの癒やしを最優先したい場合は？</h4>
      <p class="text-slate-300 leading-relaxed">第3位の小日向みゆう主演作（SNOS-00372）です。聖母のような笑顔と優しい囁きで、包み込まれるような極楽昇天を体験できます。</p>
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
                "name": "FANZA「母乳・授乳手コキ＆甘やかし母性」おすすめ神作ランキングTOP5",
                "description": "たわわに張った乳房から吹き出す甘いミルクを飲み干しながら精子を搾り取られる至福の母性昇天AV選【2026年最新】",
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
                        "name": "母乳AVの魅力・一番の抜きどころはどこですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "男性の全肯定されたい願望を満たしながら、視覚的な白い母乳の噴出と体温を感じる生々しい接触が味わえる点です。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "初めて母乳モノを見るならどの作品がおすすめですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第1位の小宵こなん主演作（SONE-00201）が圧倒的におすすめです。ストーリー性、女優の美貌、母乳のクオリティすべてが最高水準です。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "手コキでの癒やしを最優先したい場合は？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第3位の小日向みゆう主演作（SNOS-00372）です。聖母のような笑顔と優しい囁きで包み込まれるような極楽昇天を体験できます。"
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
        "id": "feature_fanza_lactation_breastfeeding_maternal_creampie_ranking_2026",
        "title": "【母乳滴る極上搾精】FANZA「母乳・授乳手コキ＆甘やかし母性」おすすめ神作ランキングTOP5！たわわに張った乳房から吹き出す甘いミルクを飲み干しながら精子を搾り取られる至福の母性昇天AV選【2026年最新】",
        "date": "2026-10-05 06:10:00",
        "hinban": "LACTATION-MATERNAL-CREAMPIE-2026",
        "price": "300~",
        "maker": "FANZA公式セレクション",
        "actresses": ["小宵こなん", "柏木ふみか", "小日向みゆう（清原みゆう）", "彩月七緒", "水谷梨明日"],
        "genres": ["母乳", "授乳手コキ", "母性", "パイズリ", "甘やかし", "巨乳", "中出し", "特集", "殿堂入り"],
        "image": cover_image,
        "review": full_html
    }

    file_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f" -> Successfully saved Article 1 ({char_count} chars) to {file_path}")


# ==============================================================================
# 記事2: 逆レイプ・連続強制搾精・腰振り騎乗位 特化
# ==============================================================================
def generate_article_reverse_rape():
    print("=== Generating Article 2: 逆レイプ・連続強制搾精・腰振り騎乗位特化 ===")
    cids = ["midv00093", "masm00001", "achj00094", "jur00752", "cjod00380"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["逆レイプ", "搾精", "騎乗位", "痴女", "拘束", "殿堂入り"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 2 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-purple-950/40 via-slate-900 to-slate-950 border border-purple-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-purple-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-purple-500/20 text-purple-300 border border-purple-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">REVERSE RAPE & FORCED SQUEEZE SPECIAL</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月05日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【男が犯される極限快楽】FANZA「逆レイプ・連続強制搾精・腰振り騎乗位」おすすめ神作ランキングTOP5！肉食美女に拘束され射精後も逃げ場ゼロで金玉が空になるまで搾り取られるドM昇天AV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    普段はリードする側の男が、抗えない状況でベッドに押し倒され、性欲旺盛な美女に主導権を完全に奪われて玩具のように犯し尽くされる――。一度ハマると二度と抜け出せなくなる禁断の快楽ジャンル、それが「逆レイプ・連続強制搾精・馬乗り騎乗位モノ」です。男のプライドを心地よく粉砕され、己の意思とは裏腹に身体が快感に屈服していく倒錯的なエクスタシーは絶大な実用度を誇ります。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    「もう出ない…勘弁して！」と涙目で懇願する男に対し、妖しい笑みを浮かべながら「まだまだ出せるでしょ？」「全部空っぽになるまで離さないから♡」と腰をグリグリと打ち付けてくる肉食美女たち。射精直後の敏感すぎる亀頭をぎゅうぎゅうと膣奥で締め上げられ、情けなく腰をビクビク跳ね上げながら2発目、3発目を強制的に搾り取られる感覚は、全男子の射精中枢を狂わせる劇薬そのものです。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、深田えいみの伝説的逆ナン拘束逆レイプ作から、松本いちかの生意気メスガキ逆レ搾精、愛弓りょうの「男は動くな」究極支配騎乗位、さつき芽衣の媚薬馬乗り逆レイプ、藤森里穂の寝込みを襲うド痴女ナース夜這いまで、ドM心と射精欲を限界まで煽り立てる【逆レイプ神作TOP5】を徹底特集します。
  </p>
</div>

<!-- 選び方の基準 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-purple-400">⛓️</span> 逆レイプ・強制搾精モノで腰が浮くほどの快感を味わう3大チェックポイント
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-purple-300 mb-2">① 逃げ場のない完全受け身・拘束シチュエーション</h4>
      <p class="text-slate-300 leading-relaxed">手足を縛られたり、上に跨がられて体重で抑え込まれるなど、男側が自力で逃げられない絶望的な状況設定が背徳感を最高潮に高めます。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-purple-300 mb-2">② 射精後も抜かずに腰を振り続ける強制追撃ピストン</h4>
      <p class="text-slate-300 leading-relaxed">一発出してぐったりしたペニスを休ませず、敏感になった亀頭をそのまま締め上げて連続発射へと追い込む容赦のなさが実用の決め手です。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-purple-300 mb-2">③ 見下ろしてくるサディスティックな笑みと淫語攻め</h4>
      <p class="text-slate-300 leading-relaxed">「情けない顔して可愛い♡」「もっと精子ちょうだい」など、上から男を見下ろしながら浴びせられる小悪魔な淫語が脳髄を直撃します。</p>
    </div>
  </div>
</div>

<!-- 目次 -->
<div class="my-8 bg-slate-900/60 border border-slate-800 rounded-2xl p-5 shadow-inner">
  <h4 class="text-sm font-bold text-slate-300 mb-3 flex items-center gap-2">
    <span>📑</span> 目次：おすすめランキングTOP5
  </h4>
  <ul class="space-y-2 text-xs md:text-sm text-purple-400/90 font-medium">
    <li><a href="#rank-1" class="hover:underline flex items-center justify-between"><span>第1位：「もう吹いてるってばぁ！」逆ナン逆レイプ（深田えいみ）</span><span class="text-slate-500 text-xs">拘束馬乗りの金字塔</span></a></li>
    <li><a href="#rank-2" class="hover:underline flex items-center justify-between"><span>第2位：メスガキ姪っ子にざこざこ罵られて逆レ搾精（松本いちか）</span><span class="text-slate-500 text-xs">小悪魔屈辱M堕ち</span></a></li>
    <li><a href="#rank-3" class="hover:underline flex items-center justify-between"><span>第3位：「男は一切動くな。」腰振り痴女が全てを支配（愛弓りょう）</span><span class="text-slate-500 text-xs">美熟女の絶対支配</span></a></li>
    <li><a href="#rank-4" class="hover:underline flex items-center justify-between"><span>第4位：青年作業員に媚薬を飲ませて馬乗り逆レイプ（さつき芽衣）</span><span class="text-slate-500 text-xs">肉食人妻の暴走</span></a></li>
    <li><a href="#rank-5" class="hover:underline flex items-center justify-between"><span>第5位：僕をダメにするド痴女ナース杭打ちピストン（藤森里穂）</span><span class="text-slate-500 text-xs">夜這い連続搾精</span></a></li>
  </ul>
</div>"""
    html_parts.append(intro_html)

    # 各作品の詳細レビュー
    reviews_detail = [
        # 第1位: 深田えいみ
        """<div id="rank-1" class="my-10 bg-slate-900 border-2 border-purple-500/40 rounded-2xl p-6 md:p-8 shadow-2xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-3">
      <span class="bg-gradient-to-r from-purple-500 to-pink-500 text-white text-sm md:text-base font-black px-4 py-1 rounded-full shadow-lg">第1位（殿堂入り）</span>
      <h3 class="text-lg md:text-2xl font-black text-white">「もう吹いてるってばぁ！」逆ナン逆レイプ 深田えいみ</h3>
    </div>
    <div class="text-xs text-slate-400">品番：MIDV-00093 / 出演：""" + get_actress_link("深田えいみ") + """</div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <div class="space-y-4">
      <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dmidv00093%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="block group relative overflow-hidden rounded-xl border border-slate-700">
        <img src="https://pics.dmm.co.jp/digital/video/midv00093/midv00093pl.jpg" alt="深田えいみ 逆ナン逆レイプ" class="w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-4">
          <span class="text-white text-xs font-bold bg-rose-600/90 px-3 py-1 rounded-full">FANZA公式で作品詳細を見る →</span>
        </div>
      </a>
      <div class="flex flex-wrap gap-2">
        """ + get_genre_link("逆レイプ") + " " + get_genre_link("痴女") + " " + get_genre_link("拘束") + " " + get_genre_link("騎乗位") + " " + get_genre_link("連続射精") + """
      </div>
    </div>
    <div class="space-y-4 text-xs md:text-sm text-slate-300 leading-relaxed">
      <p class="font-bold text-purple-200">【解説・作品の魅力】</p>
      <p>AV界きってのトップ痴女・深田えいみが、街で見つけた一般男性をラブホテルへと連れ込み、ベッドに両手両足を拘束して一方的に責め立てる伝説の逆レイプドキュメント。男側の都合や体力など一切お構いなしに、己の性欲を満たすためだけに肉棒を貪り食うサディスティックな姿は圧巻です。</p>
      <p>拘束されて身動きの取れない男を見下ろし、「私の言うこと聞いてくれるよね？」と冷たく妖しく微笑む深田えいみ。強引に覆いかぶさってペニスをズブズブと奥深くまで呑み込み、男の情けない悲鳴を聞きながら激しく腰を上下させる光景に、全男子のドM本能が覚醒します。</p>
      <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
        <p class="text-purple-300 font-bold mb-1">🔥 絶対に抜ける神シーン・実用ポイント</p>
        <p class="text-slate-300">1発目を中出しされて「もう無理、抜いて…！」と懇願する男に対し、「もう吹いてるってばぁ！でもまだまだ出すよ！」とさらに腰の回転を加速させる深田えいみ。敏感すぎる亀頭を締め上げられ、強制的に2発目・3発目を搾り取られる連続アクメは実用度無限大です。</p>
      </div>
      <div class="pt-2">
        <a href="/posts/midv00093" class="text-xs text-purple-400 hover:text-purple-300 underline font-bold">👉 作品個別ページ（サンプル画像・詳細レビュー）を見る</a>
      </div>
    </div>
  </div>

  <div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-6">
    <img src="https://pics.dmm.co.jp/digital/video/midv00093/midv00093-1.jpg" alt="サンプル画像1" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/midv00093/midv00093-2.jpg" alt="サンプル画像2" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/midv00093/midv00093-3.jpg" alt="サンプル画像3" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/midv00093/midv00093-4.jpg" alt="サンプル画像4" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
  </div>

  <div class="text-center">
    <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dmidv00093%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-2 bg-gradient-to-r from-purple-600 via-pink-600 to-purple-600 hover:opacity-95 text-white font-black text-sm md:text-base px-8 py-4 rounded-xl shadow-xl transition transform hover:scale-105">
      <span>今すぐFANZA公式で『深田えいみの逆ナン逆レイプ』をフル視聴する</span>
      <span>🚀</span>
    </a>
  </div>
</div>""",

        # 第2位: 松本いちか
        """<div id="rank-2" class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-3">
      <span class="bg-slate-700 text-purple-300 text-sm md:text-base font-black px-4 py-1 rounded-full">第2位</span>
      <h3 class="text-lg md:text-2xl font-black text-white">メスガキ姪っ子にざこざこ罵られて逆レ搾精 松本いちか</h3>
    </div>
    <div class="text-xs text-slate-400">品番：MASM-00001 / 出演：""" + get_actress_link("松本いちか") + """</div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <div class="space-y-4">
      <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dmasm00001%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="block group relative overflow-hidden rounded-xl border border-slate-700">
        <img src="https://pics.dmm.co.jp/digital/video/masm00001/masm00001pl.jpg" alt="松本いちか メスガキ逆レ搾精" class="w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 semi-transparent to-transparent flex items-end p-4">
          <span class="text-white text-xs font-bold bg-rose-600/90 px-3 py-1 rounded-full">FANZA公式で作品詳細を見る →</span>
        </div>
      </a>
      <div class="flex flex-wrap gap-2">
        """ + get_genre_link("メスガキ") + " " + get_genre_link("逆レイプ") + " " + get_genre_link("騎乗位") + " " + get_genre_link("美少女") + " " + get_genre_link("搾精") + """
      </div>
    </div>
    <div class="space-y-4 text-xs md:text-sm text-slate-300 leading-relaxed">
      <p class="font-bold text-purple-200">【解説・作品の魅力】</p>
      <p>小柄で華奢な美少女・松本いちかが、年の離れた叔父を「ざぁ～こ♡早漏チ○ポ♡」と徹底的に小馬鹿にし、上に跨がって大人を完全に快楽で服従させるメガヒット作。普段は生意気な態度をとる姪っ子が、ベッドの上で恐ろしいほどの性欲と腰使いを発揮するギャップが悶絶級です。</p>
      <p>大人のプライドをズタズタに引き裂く挑発的な目線と、耳元で囁かれる嘲笑。「おじさん、こんな子供の身体でビンビンにして恥ずかしくないの？」と言われながら、狭い膣奥でグリグリと亀頭を擦られる屈辱快楽に男は一瞬で白旗を上げます。</p>
      <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
        <p class="text-purple-300 font-bold mb-1">🔥 絶対に抜ける神シーン・実用ポイント</p>
        <p class="text-slate-300">あっけなく中出ししてしまった叔父を見下ろし、「えー、もう出ちゃったの？ざぁこ♡でも抜かないもんねー！」と腰を止めずにピストンを継続。射精後も逃げられないまま搾り取られる姿は、M男でなくとも興奮が止まりません。</p>
      </div>
      <div class="pt-2">
        <a href="/posts/masm00001" class="text-xs text-purple-400 hover:text-purple-300 underline font-bold">👉 作品個別ページ（サンプル画像・詳細レビュー）を見る</a>
      </div>
    </div>
  </div>

  <div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-6">
    <img src="https://pics.dmm.co.jp/digital/video/masm00001/masm00001-1.jpg" alt="サンプル画像1" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/masm00001/masm00001-2.jpg" alt="サンプル画像2" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/masm00001/masm00001-3.jpg" alt="サンプル画像3" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/masm00001/masm00001-4.jpg" alt="サンプル画像4" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
  </div>

  <div class="text-center">
    <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dmasm00001%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-2 bg-slate-800 hover:bg-slate-700 text-purple-300 border border-purple-500/40 font-bold text-sm md:text-base px-8 py-3.5 rounded-xl shadow-lg transition">
      <span>FANZA公式で『松本いちか メスガキ逆レ搾精』を見る →</span>
    </a>
  </div>
</div>""",

        # 第3位: 愛弓りょう
        """<div id="rank-3" class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-3">
      <span class="bg-slate-700 text-purple-300 text-sm md:text-base font-black px-4 py-1 rounded-full">第3位</span>
      <h3 class="text-lg md:text-2xl font-black text-white">「男は一切動くな。」腰振り痴女が全てを支配する、究極の騎乗位 愛弓りょう</h3>
    </div>
    <div class="text-xs text-slate-400">品番：ACHJ-00094 / 出演：""" + get_actress_link("愛弓りょう") + """</div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <div class="space-y-4">
      <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dachj00094%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="block group relative overflow-hidden rounded-xl border border-slate-700">
        <img src="https://pics.dmm.co.jp/digital/video/achj00094/achj00094pl.jpg" alt="愛弓りょう 究極の騎乗位" class="w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-4">
          <span class="text-white text-xs font-bold bg-rose-600/90 px-3 py-1 rounded-full">FANZA公式で作品詳細を見る →</span>
        </div>
      </a>
      <div class="flex flex-wrap gap-2">
        """ + get_genre_link("騎乗位") + " " + get_genre_link("痴女") + " " + get_genre_link("人妻") + " " + get_genre_link("美熟女") + " " + get_genre_link("搾精") + """
      </div>
    </div>
    <div class="space-y-4 text-xs md:text-sm text-slate-300 leading-relaxed">
      <p class="font-bold text-purple-200">【解説・作品の魅力】</p>
      <p>完璧な美貌と妖艶なフェロモンを放つ美熟女・愛弓りょうが、男に一切の動きを許さず、己の熟練した腰振りだけで男を昇天へと導く騎乗位特化作。大人のお姉さんに全てを委ね、ただ跨がられて弄ばれるだけの至福の快楽が詰まっています。</p>
      <p>「男は一切動かないで…私の腰の動きだけを感じて」と男の胸を抑え込み、ゆったりと円を描くように腰を回す愛弓りょう。汗ばんだ美ボディと艶やかな視線が男の理性を完全に溶かします。</p>
      <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
        <p class="text-purple-300 font-bold mb-1">🔥 絶対に抜ける神シーン・実用ポイント</p>
        <p class="text-slate-300">亀頭のツボを正確に抉るスローグラインドから、突如始まる激しい縦ピストン。男が腰を浮かせそうになると「動いちゃダメって言ったでしょ？」と叱られながら、膣奥で精液をすべて搾り取られる瞬間は絶頂必至です。</p>
      </div>
      <div class="pt-2">
        <a href="/posts/achj00094" class="text-xs text-purple-400 hover:text-purple-300 underline font-bold">👉 作品個別ページ（サンプル画像・詳細レビュー）を見る</a>
      </div>
    </div>
  </div>

  <div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-6">
    <img src="https://pics.dmm.co.jp/digital/video/achj00094/achj00094-1.jpg" alt="サンプル画像1" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/achj00094/achj00094-2.jpg" alt="サンプル画像2" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/achj00094/achj00094-3.jpg" alt="サンプル画像3" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/achj00094/achj00094-4.jpg" alt="サンプル画像4" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
  </div>

  <div class="text-center">
    <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dachj00094%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-2 bg-slate-800 hover:bg-slate-700 text-purple-300 border border-purple-500/40 font-bold text-sm md:text-base px-8 py-3.5 rounded-xl shadow-lg transition">
      <span>FANZA公式で『愛弓りょう 究極の騎乗位』を見る →</span>
    </a>
  </div>
</div>""",

        # 第4位: さつき芽衣
        """<div id="rank-4" class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-3">
      <span class="bg-slate-700 text-purple-300 text-sm md:text-base font-black px-4 py-1 rounded-full">第4位</span>
      <h3 class="text-lg md:text-2xl font-black text-white">青年作業員に媚薬を飲ませて馬乗り逆レイプ さつき芽衣</h3>
    </div>
    <div class="text-xs text-slate-400">品番：JUR-00752 / 出演：""" + get_actress_link("さつき芽衣") + """</div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <div class="space-y-4">
      <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Djur00752%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="block group relative overflow-hidden rounded-xl border border-slate-700">
        <img src="https://pics.dmm.co.jp/digital/video/jur00752/jur00752pl.jpg" alt="さつき芽衣 馬乗り逆レイプ" class="w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-4">
          <span class="text-white text-xs font-bold bg-rose-600/90 px-3 py-1 rounded-full">FANZA公式で作品詳細を見る →</span>
        </div>
      </a>
      <div class="flex flex-wrap gap-2">
        """ + get_genre_link("人妻") + " " + get_genre_link("逆レイプ") + " " + get_genre_link("媚薬") + " " + get_genre_link("騎乗位") + " " + get_genre_link("中出し") + """
      </div>
    </div>
    <div class="space-y-4 text-xs md:text-sm text-slate-300 leading-relaxed">
      <p class="font-bold text-purple-200">【解説・作品の魅力】</p>
      <p>肉感的なむっちりボディと濃厚なフェロモンを漂わせる人妻・さつき芽衣が、エアコン修理に来た若い作業員に媚薬を盛り、身体が動かなくなった男を密室で貪り尽くす衝撃作。男を押し倒して作業着を剥ぎ取り、若々しいペニスに跨がって貪欲に腰を振る人妻の狂乱エロスが炸裂します。</p>
      <p>「若い男の子の身体、ずっと触りたかったの…」と息を荒くしてペニスをしごき上げるさつき芽衣。青年が必死に抵抗しようとしても、媚薬の脱力感と人妻の重みで身動きが取れず、快感に沈んでいく過程が最高にエロティックです。</p>
      <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
        <p class="text-purple-300 font-bold mb-1">🔥 絶対に抜ける神シーン・実用ポイント</p>
        <p class="text-slate-300">重みのある豊満ヒップを青年の股間に打ち付け、自らアヘ顔を晒して何度もイキまくるさつき芽衣。青年が限界を迎えて中出ししても、「何回イッても終わらせないわよ」と腰を止めずに搾り取り続ける姿は圧巻の実用度を誇ります。</p>
      </div>
      <div class="pt-2">
        <a href="/posts/jur00752" class="text-xs text-purple-400 hover:text-purple-300 underline font-bold">👉 作品個別ページ（サンプル画像・詳細レビュー）を見る</a>
      </div>
    </div>
  </div>

  <div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-6">
    <img src="https://pics.dmm.co.jp/digital/video/jur00752/jur00752-1.jpg" alt="サンプル画像1" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/jur00752/jur00752-2.jpg" alt="サンプル画像2" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/jur00752/jur00752-3.jpg" alt="サンプル画像3" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/jur00752/jur00752-4.jpg" alt="サンプル画像4" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
  </div>

  <div class="text-center">
    <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Djur00752%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-2 bg-slate-800 hover:bg-slate-700 text-purple-300 border border-purple-500/40 font-bold text-sm md:text-base px-8 py-3.5 rounded-xl shadow-lg transition">
      <span>FANZA公式で『さつき芽衣 馬乗り逆レイプ』を見る →</span>
    </a>
  </div>
</div>""",

        # 第5位: 藤森里穂
        """<div id="rank-5" class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-3">
      <span class="bg-slate-700 text-purple-300 text-sm md:text-base font-black px-4 py-1 rounded-full">第5位</span>
      <h3 class="text-lg md:text-2xl font-black text-white">僕をダメにするド痴女ナース杭打ちピストン 藤森里穂</h3>
    </div>
    <div class="text-xs text-slate-400">品番：CJOD-00380 / 出演：""" + get_actress_link("藤森里穂") + """</div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <div class="space-y-4">
      <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dcjod00380%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="block group relative overflow-hidden rounded-xl border border-slate-700">
        <img src="https://pics.dmm.co.jp/digital/video/cjod00380/cjod00380pl.jpg" alt="藤森里穂 ド痴女ナース" class="w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-4">
          <span class="text-white text-xs font-bold bg-rose-600/90 px-3 py-1 rounded-full">FANZA公式で作品詳細を見る →</span>
        </div>
      </a>
      <div class="flex flex-wrap gap-2">
        """ + get_genre_link("看護婦・ナース") + " " + get_genre_link("痴女") + " " + get_genre_link("逆レイプ") + " " + get_genre_link("中出し") + " " + get_genre_link("騎乗位") + """
      </div>
    </div>
    <div class="space-y-4 text-xs md:text-sm text-slate-300 leading-relaxed">
      <p class="font-bold text-purple-200">【解説・作品の魅力】</p>
      <p>ド痴女役をやらせたら右に出る者のいない人気女優・藤森里穂が、入院患者の寝込みを夜な夜な襲い、点滴で動けない男を夜這い逆レイプしてザーメンを吸い尽くす病棟背徳の最高傑作。涎を滴らせるディープキスと容赦ない杭打ちピストンの嵐が男を骨抜きにします。</p>
      <p>「声出しちゃダメですよ…」と口元を塞ぎながら、ナース服をめくってペニスを跨ぐ藤森里穂。薄暗い病室で響く生々しい水音と、快楽に蕩けたナースの表情が男の背徳感を極限まで煽り立てます。</p>
      <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
        <p class="text-purple-300 font-bold mb-1">🔥 絶対に抜ける神シーン・実用ポイント</p>
        <p class="text-slate-300">息つく暇も与えずに繰り返される激しい杭打ち騎乗位。男がベッドの上でビクビクと絶頂しても、「患者さんの精子、全部私のもの♡」と腰を打ち付け続けて2発目・3発目の中出しを搾り取るシーンは必見です。</p>
      </div>
      <div class="pt-2">
        <a href="/posts/cjod00380" class="text-xs text-purple-400 hover:text-purple-300 underline font-bold">👉 作品個別ページ（サンプル画像・詳細レビュー）を見る</a>
      </div>
    </div>
  </div>

  <div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-6">
    <img src="https://pics.dmm.co.jp/digital/video/cjod00380/cjod00380-1.jpg" alt="サンプル画像1" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/cjod00380/cjod00380-2.jpg" alt="サンプル画像2" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/cjod00380/cjod00380-3.jpg" alt="サンプル画像3" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/cjod00380/cjod00380-4.jpg" alt="サンプル画像4" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
  </div>

  <div class="text-center">
    <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dcjod00380%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-2 bg-slate-800 hover:bg-slate-700 text-purple-300 border border-purple-500/40 font-bold text-sm md:text-base px-8 py-3.5 rounded-xl shadow-lg transition">
      <span>FANZA公式で『藤森里穂 ド痴女ナース』を見る →</span>
    </a>
  </div>
</div>"""
    ]
    html_parts.extend(reviews_detail)

    # 比較まとめテーブル ＆ 内部リンク ＆ FAQ
    table_and_links = """<!-- スペック比較テーブル -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl overflow-hidden">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>📊</span> おすすめ逆レイプ・搾精騎乗位神作5選 徹底スペック比較表
  </h3>
  <div class="overflow-x-auto">
    <table class="w-full text-xs md:text-sm text-left text-slate-300">
      <thead class="bg-slate-800 text-purple-300 border-b border-slate-700 uppercase">
        <tr>
          <th class="py-3 px-4">順位 / タイトル</th>
          <th class="py-3 px-4">主演女優</th>
          <th class="py-3 px-4">ドS・肉食度</th>
          <th class="py-3 px-4">実用度・射精圧</th>
          <th class="py-3 px-4">公式リンク</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800">
        <tr class="hover:bg-slate-800/40">
          <td class="py-3 px-4 font-bold text-white">第1位 逆ナン逆レイプ</td>
          <td class="py-3 px-4">""" + get_actress_link("深田えいみ") + """</td>
          <td class="py-3 px-4 text-purple-400">★★★★★（完全拘束）</td>
          <td class="py-3 px-4 text-rose-400">★★★★★（限界連続射精）</td>
          <td class="py-3 px-4"><a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dmidv00093%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="text-purple-400 underline font-bold">FANZAで確認</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="py-3 px-4 font-bold text-white">第2位 メスガキ姪っ子逆レ搾精</td>
          <td class="py-3 px-4">""" + get_actress_link("松本いちか") + """</td>
          <td class="py-3 px-4 text-purple-400">★★★★★（ざこ罵倒）</td>
          <td class="py-3 px-4 text-rose-400">★★★★★（M男悶絶）</td>
          <td class="py-3 px-4"><a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dmasm00001%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="text-purple-400 underline font-bold">FANZAで確認</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="py-3 px-4 font-bold text-white">第3位 「男は一切動くな。」究極の騎乗位</td>
          <td class="py-3 px-4">""" + get_actress_link("愛弓りょう") + """</td>
          <td class="py-3 px-4 text-purple-400">★★★★☆（女王支配）</td>
          <td class="py-3 px-4 text-rose-400">★★★★☆（極上グラインド）</td>
          <td class="py-3 px-4"><a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dachj00094%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="text-purple-400 underline font-bold">FANZAで確認</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="py-3 px-4 font-bold text-white">第4位 青年作業員に媚薬馬乗り逆レイプ</td>
          <td class="py-3 px-4">""" + get_actress_link("さつき芽衣") + """</td>
          <td class="py-3 px-4 text-purple-400">★★★★☆（肉食人妻）</td>
          <td class="py-3 px-4 text-rose-400">★★★★☆（杭打ち中出し）</td>
          <td class="py-3 px-4"><a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Djur00752%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="text-purple-400 underline font-bold">FANZAで確認</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="py-3 px-4 font-bold text-white">第5位 ド痴女ナース杭打ちピストン</td>
          <td class="py-3 px-4">""" + get_actress_link("藤森里穂") + """</td>
          <td class="py-3 px-4 text-purple-400">★★★★☆（夜這い痴女）</td>
          <td class="py-3 px-4 text-rose-400">★★★★☆（涎キス搾精）</td>
          <td class="py-3 px-4"><a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dcjod00380%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="text-purple-400 underline font-bold">FANZAで確認</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- 関連特集への内部リンク -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>🔗</span> あわせて読みたい！おすすめキラー特集記事
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs md:text-sm">
    <a href="/posts/feature_fanza_sugar_daddy_allowance_raw_creampie_ranking_2026" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-purple-500/50 transition block">
      <div class="font-bold text-purple-300 mb-1">【お金の魔力でプライド崩壊】パパ活女子・お手当増額生中出しランキングTOP5</div>
      <p class="text-slate-400 line-clamp-2">小遣い稼ぎの生意気美少女がお手当に負けて生ハメ種付けを受け入れる屈辱快楽AV選！</p>
    </a>
    <a href="/posts/feature_super_tech_edge_orgasm_denial_unprotected_creampie_ranking_2026" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-pink-500/50 transition block">
      <div class="font-bold text-pink-300 mb-1">【凄テク寸止め＆我慢生中出し】射精管理・極限快感ランキングTOP5</div>
      <p class="text-slate-400 line-clamp-2">寸止めで限界まで焦らされた後に解き放たれる大量射精の快感！</p>
    </a>
  </div>
</div>

<!-- よくある質問（FAQ） -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>❓</span> 逆レイプ・搾精騎乗位AVに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-4 text-xs md:text-sm">
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-purple-300 mb-2">Q1. 逆レイプ作品の最大の魅力は何ですか？</h4>
      <p class="text-slate-300 leading-relaxed">能動的に動く必要がなく、完全な受け身で美女に主導権を奪われ、射精後も逃げ場ゼロで連続搾精される倒錯したドM快楽です。</p>
    </div>
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-purple-300 mb-2">Q2. 一番ドSで容赦なく搾り取られる作品はどれですか？</h4>
      <p class="text-slate-300 leading-relaxed">第1位の深田えいみ主演作（MIDV-00093）です。ベッドに手足を拘束された状態で、男の懇願を無視して連続射精へ追い込む姿は圧巻です。</p>
    </div>
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-purple-300 mb-2">Q3. 生意気な女の子に罵られながら犯されたい場合は？</h4>
      <p class="text-slate-300 leading-relaxed">第2位の松本いちか主演作（MASM-00001）がおすすめです。「ざぁこ♡」の煽りと容赦ない腰振りでプライドを砕かれます。</p>
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
                "name": "FANZA「逆レイプ・連続強制搾精・腰振り騎乗位」おすすめ神作ランキングTOP5",
                "description": "肉食美女に拘束され射精後も逃げ場ゼロで金玉が空になるまで搾り取られるドM昇天AV選【2026年最新】",
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
                        "name": "逆レイプ作品の最大の魅力は何ですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "能動的に動く必要がなく、完全な受け身で美女に主導権を奪われ、射精後も逃げ場ゼロで連続搾精される倒錯したドM快楽です。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "一番ドSで容赦なく搾り取られる作品はどれですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第1位の深田えいみ主演作（MIDV-00093）です。手足拘束下で男の懇願を無視して連続射精へ追い込む姿は圧巻です。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "生意気な女の子に罵られながら犯されたい場合は？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第2位の松本いちか主演作（MASM-00001）がおすすめです。ざこ罵倒と容赦ない腰振りでプライドを砕かれます。"
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
        "id": "feature_fanza_reverse_rape_forced_ejaculation_cowgirl_ranking_2026",
        "title": "【男が犯される極限快楽】FANZA「逆レイプ・連続強制搾精・腰振り騎乗位」おすすめ神作ランキングTOP5！肉食美女に拘束され射精後も逃げ場ゼロで金玉が空になるまで搾り取られるドM昇天AV選【2026年最新】",
        "date": "2026-10-05 06:15:00",
        "hinban": "REVERSE-RAPE-FORCED-SQUEEZE-2026",
        "price": "300~",
        "maker": "FANZA公式セレクション",
        "actresses": ["深田えいみ", "松本いちか", "愛弓りょう", "さつき芽衣", "藤森里穂"],
        "genres": ["逆レイプ", "搾精", "騎乗位", "痴女", "拘束", "連続射精", "メスガキ", "特集", "殿堂入り"],
        "image": cover_image,
        "review": full_html
    }

    file_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f" -> Successfully saved Article 2 ({char_count} chars) to {file_path}")


# ==============================================================================
# 記事3: 初アナル解禁・お尻開発＆2穴同時 特化
# ==============================================================================
def generate_article_anal():
    print("=== Generating Article 3: 初アナル解禁・お尻開発＆2穴同時特化 ===")
    cids = ["miab00284", "mism00185", "cemd00885", "cemd00741", "mism00106"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["アナル解禁", "アナル", "2穴", "美尻", "開発", "殿堂入り"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 3 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-rose-950/40 via-slate-900 to-slate-950 border border-rose-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-rose-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-rose-500/20 text-rose-300 border border-rose-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">FIRST ANAL DEBUT & DUAL HOLES SPECIAL</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月05日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【禁断の初アナル解禁】FANZA「初アナル解禁・お尻開発＆2穴同時」おすすめ神作ランキングTOP5！清楚美女が未知の快感に悶絶し腰を跳ね上げて連続絶頂する至高のお尻快楽AV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    美しき人気女優が、これまでのキャリアで一度も許してこなかった最後の聖域・アナル――。その硬く閉ざされた処女肛門をカメラの前で初解禁し、未知の異物感と痛みを乗り越えて至高のエクスタシーへと覚醒していく瞬間は、全AVシーンの中でも最もドラマチックで興奮を呼ぶ至高の瞬間です。男の征服欲とフェティシズムの極点、それが「初アナル解禁・お尻開発・2穴同時交尾」です。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    四つん這いにされて羞恥に頬を染めながら、ローションで丁寧にほぐされていくピンク色の小さな菊座。太い男根がズブズブと割り込んでいく瞬間に零れる涙、そして奥深くまで貫かれた瞬間に「あぁっ…！お尻なのに気持ちいい…！」と白目を剥いてアナルアクメに達する光景は、鑑賞者の理性を一瞬で焼き切ります。前方の秘部とは比べ物にならない強烈な締め付けと、前後の穴を同時に突き分ける背徳の快感は圧巻です。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、大人気専属女優・花狩まいの初アナル解禁ドキュメントから、中条鈴華の上品美女アナルAVデビュー、伝説のアナルクイーン泉りおんの奇跡の1本限定復活、美熟女森沢かなの現場交渉アナルSEX、最上さゆきの壮絶2穴緊縛アナルまで、実用度・緊張感・エロスのすべてが最高潮に達した【初アナル解禁神作TOP5】を徹底解説します。
  </p>
</div>

<!-- 選び方の基準 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-rose-400">🍑</span> 初アナル解禁作品で最高の興奮を味わう3大チェックポイント
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-rose-300 mb-2">① 丁寧なお尻開発プロセスと羞恥の表情</h4>
      <p class="text-slate-300 leading-relaxed">いきなり挿入するのではなく、指やローションでじっくりと肛門をほぐされ、恥ずかしさに顔を覆いながらも体が快感を受け入れていく前戯がソソります。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-rose-300 mb-2">② 処女肛門を極太ペニスが貫く瞬間の緊迫感</h4>
      <p class="text-slate-300 leading-relaxed">狭い菊座が押し広げられ、亀頭がめり込んでいくアップ映像と、女優が息を呑んで痛みに耐えながら快楽へと変化していくリアクションが最高の実用度を誇ります。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-rose-300 mb-2">③ アナルアクメによる連続潮吹き＆アナル中出し</h4>
      <p class="text-slate-300 leading-relaxed">アナルへの刺激だけで腰をビクビクと跳ね上げてイキ狂う姿や、直腸の奥深くに濃厚な白濁精液を注ぎ込まれる背徳のフィニッシュが圧巻です。</p>
    </div>
  </div>
</div>

<!-- 目次 -->
<div class="my-8 bg-slate-900/60 border border-slate-800 rounded-2xl p-5 shadow-inner">
  <h4 class="text-sm font-bold text-slate-300 mb-3 flex items-center gap-2">
    <span>📑</span> 目次：おすすめランキングTOP5
  </h4>
  <ul class="space-y-2 text-xs md:text-sm text-rose-400/90 font-medium">
    <li><a href="#rank-1" class="hover:underline flex items-center justify-between"><span>第1位：花狩まい アナル解禁！（花狩まい）</span><span class="text-slate-500 text-xs">専属美少女の初肛門</span></a></li>
    <li><a href="#rank-2" class="hover:underline flex items-center justify-between"><span>第2位：アナル解禁AVデビュー！ しとやかに…（中条鈴華）</span><span class="text-slate-500 text-xs">清楚お嬢様の肛門マゾ</span></a></li>
    <li><a href="#rank-3" class="hover:underline flex items-center justify-between"><span>第3位：1本限りのアナルSEX復活！（泉りおん）</span><span class="text-slate-500 text-xs">伝説クイーンの奇跡</span></a></li>
    <li><a href="#rank-4" class="hover:underline flex items-center justify-between"><span>第4位：1本限りのアナルSEX復活！（森沢かな）</span><span class="text-slate-500 text-xs">美熟女の現場交渉SEX</span></a></li>
    <li><a href="#rank-5" class="hover:underline flex items-center justify-between"><span>第5位：アナル解禁！2穴ファック本格緊縛解禁！（最上さゆき）</span><span class="text-slate-500 text-xs">前後2穴同時の狂乱</span></a></li>
  </ul>
</div>"""
    html_parts.append(intro_html)

    # 各作品の詳細レビュー
    reviews_detail = [
        # 第1位: 花狩まい
        """<div id="rank-1" class="my-10 bg-slate-900 border-2 border-rose-500/40 rounded-2xl p-6 md:p-8 shadow-2xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-3">
      <span class="bg-gradient-to-r from-rose-500 to-pink-500 text-white text-sm md:text-base font-black px-4 py-1 rounded-full shadow-lg">第1位（殿堂入り）</span>
      <h3 class="text-lg md:text-2xl font-black text-white">花狩まい アナル解禁！</h3>
    </div>
    <div class="text-xs text-slate-400">品番：MIAB-00284 / 出演：""" + get_actress_link("花狩まい") + """</div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <div class="space-y-4">
      <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dmiab00284%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="block group relative overflow-hidden rounded-xl border border-slate-700">
        <img src="https://pics.dmm.co.jp/digital/video/miab00284/miab00284pl.jpg" alt="花狩まい アナル解禁！" class="w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-4">
          <span class="text-white text-xs font-bold bg-rose-600/90 px-3 py-1 rounded-full">FANZA公式で作品詳細を見る →</span>
        </div>
      </a>
      <div class="flex flex-wrap gap-2">
        """ + get_genre_link("アナル") + " " + get_genre_link("初アナル") + " " + get_genre_link("美少女") + " " + get_genre_link("美尻") + " " + get_genre_link("潮吹き") + """
      </div>
    </div>
    <div class="space-y-4 text-xs md:text-sm text-slate-300 leading-relaxed">
      <p class="font-bold text-rose-200">【解説・作品の魅力】</p>
      <p>愛くるしいルックスと抜群のプロポーションで絶大な人気を誇る専属女優・花狩まいが、ついに未知の領域である肛門処女を捧げた記念碑的ドキュメント。誰にも犯されたことのない無垢なお尻が、カメラの前で初めて男根を受け入れる瞬間を完全収録した歴史的傑作です。</p>
      <p>初めは「本当に痛くないですか…？」と怯えていた花狩まいが、念入りなオイルマッサージとローション開発によって徐々に体の力を抜き、肛門の奥が熱く疼き始める過程が極めて克明に描かれています。恥ずかしそうに手でお尻を隠そうとする仕草が男の征服欲を限界まで煽り立てます。</p>
      <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
        <p class="text-rose-300 font-bold mb-1">🔥 絶対に抜ける神シーン・実用ポイント</p>
        <p class="text-slate-300">極太のペニスが狭い肛門を押し広げて進入する瞬間、花狩まいの瞳に浮かぶ涙と紅潮した頬。そして激しいピストンとともに痛みが甘い快感へと反転し、腰をビクビク跳ね上げてアナルアクメを連発する姿は、実用派アナルファンにとって至高の抜きどころです。</p>
      </div>
      <div class="pt-2">
        <a href="/posts/miab00284" class="text-xs text-rose-400 hover:text-rose-300 underline font-bold">👉 作品個別ページ（サンプル画像・詳細レビュー）を見る</a>
      </div>
    </div>
  </div>

  <div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-6">
    <img src="https://pics.dmm.co.jp/digital/video/miab00284/miab00284-1.jpg" alt="サンプル画像1" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/miab00284/miab00284-2.jpg" alt="サンプル画像2" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/miab00284/miab00284-3.jpg" alt="サンプル画像3" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/miab00284/miab00284-4.jpg" alt="サンプル画像4" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
  </div>

  <div class="text-center">
    <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dmiab00284%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-2 bg-gradient-to-r from-rose-500 via-pink-600 to-rose-500 hover:opacity-95 text-white font-black text-sm md:text-base px-8 py-4 rounded-xl shadow-xl transition transform hover:scale-105">
      <span>今すぐFANZA公式で『花狩まい アナル解禁！』をフル視聴する</span>
      <span>🚀</span>
    </a>
  </div>
</div>""",

        # 第2位: 中条鈴華
        """<div id="rank-2" class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-3">
      <span class="bg-slate-700 text-rose-300 text-sm md:text-base font-black px-4 py-1 rounded-full">第2位</span>
      <h3 class="text-lg md:text-2xl font-black text-white">アナル解禁AVデビュー！ しとやかに… 中条鈴華</h3>
    </div>
    <div class="text-xs text-slate-400">品番：MISM-00185 / 出演：""" + get_actress_link("中条鈴華") + """</div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <div class="space-y-4">
      <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dmism00185%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="block group relative overflow-hidden rounded-xl border border-slate-700">
        <img src="https://pics.dmm.co.jp/digital/video/mism00185/mism00185pl.jpg" alt="中条鈴華 アナル解禁AVデビュー" class="w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-4">
          <span class="text-white text-xs font-bold bg-rose-600/90 px-3 py-1 rounded-full">FANZA公式で作品詳細を見る →</span>
        </div>
      </a>
      <div class="flex flex-wrap gap-2">
        """ + get_genre_link("アナル") + " " + get_genre_link("デビュー") + " " + get_genre_link("ドM") + " " + get_genre_link("潮吹き") + " " + get_genre_link("美尻") + """
      </div>
    </div>
    <div class="space-y-4 text-xs md:text-sm text-slate-300 leading-relaxed">
      <p class="font-bold text-rose-200">【解説・作品の魅力】</p>
      <p>清楚で品格ある佇まいを持つ中条鈴華が、なんとAVデビュー作でアナル解禁を同時に果たすという異例の衝撃作。おっとりとした良家のお嬢様のような美女が、アナルを貫かれる快感によってド淫乱なマゾメスへと変貌していくカタルシスは言葉を失うレベルです。</p>
      <p>「こんなところに入れられたら、おかしくなっちゃいます…」と懇願しながらも、肛門を激しくノックされるたびに甘い喘ぎ声を漏らす中条鈴華。細くしなやかな肢体がビクンビクンと痙攣し、恥じらいを捨てて腰を突き出す姿に男の加虐心が限界まで煽られます。</p>
      <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
        <p class="text-rose-300 font-bold mb-1">🔥 絶対に抜ける神シーン・実用ポイント</p>
        <p class="text-slate-300">前方の秘部には一切触れず、アナルピストンだけで連続で大量の潮を噴き出す壮絶なアナルアクメ。白目を剥いて舌を垂らし、「お尻もっと奥まで突いてください…！」と懇願する姿は必見です。</p>
      </div>
      <div class="pt-2">
        <a href="/posts/mism00185" class="text-xs text-rose-400 hover:text-rose-300 underline font-bold">👉 作品個別ページ（サンプル画像・詳細レビュー）を見る</a>
      </div>
    </div>
  </div>

  <div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-6">
    <img src="https://pics.dmm.co.jp/digital/video/mism00185/mism00185-1.jpg" alt="サンプル画像1" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/mism00185/mism00185-2.jpg" alt="サンプル画像2" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/mism00185/mism00185-3.jpg" alt="サンプル画像3" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/mism00185/mism00185-4.jpg" alt="サンプル画像4" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
  </div>

  <div class="text-center">
    <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dmism00185%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-2 bg-slate-800 hover:bg-slate-700 text-rose-300 border border-rose-500/40 font-bold text-sm md:text-base px-8 py-3.5 rounded-xl shadow-lg transition">
      <span>FANZA公式で『中条鈴華 アナル解禁AVデビュー』を見る →</span>
    </a>
  </div>
</div>""",

        # 第3位: 泉りおん
        """<div id="rank-3" class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-3">
      <span class="bg-slate-700 text-rose-300 text-sm md:text-base font-black px-4 py-1 rounded-full">第3位</span>
      <h3 class="text-lg md:text-2xl font-black text-white">1本限りのアナルSEX復活！ 泉りおん</h3>
    </div>
    <div class="text-xs text-slate-400">品番：CEMD-00885 / 出演：""" + get_actress_link("泉りおん") + """</div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <div class="space-y-4">
      <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dcemd00885%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="block group relative overflow-hidden rounded-xl border border-slate-700">
        <img src="https://pics.dmm.co.jp/digital/video/cemd00885/cemd00885pl.jpg" alt="泉りおん アナルSEX復活" class="w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-4">
          <span class="text-white text-xs font-bold bg-rose-600/90 px-3 py-1 rounded-full">FANZA公式で作品詳細を見る →</span>
        </div>
      </a>
      <div class="flex flex-wrap gap-2">
        """ + get_genre_link("アナル") + " " + get_genre_link("中出し") + " " + get_genre_link("美乳") + " " + get_genre_link("フェティッシュ") + " " + get_genre_link("バック") + """
      </div>
    </div>
    <div class="space-y-4 text-xs md:text-sm text-slate-300 leading-relaxed">
      <p class="font-bold text-rose-200">【解説・作品の魅力】</p>
      <p>伝説のアナルクイーンとして君臨する泉りおんが、撮影現場でのリアルな交渉によって奇跡的に1本限定のアナル解禁を果たした超貴重作。アナルを知り尽くした圧倒的な肛門感度と、極太ペニスを根元まで飲み込む滑らかな受け入れテクニックは圧巻の一言です。</p>
      <p>自ら四つん這いになり、綺麗なお尻を広げてアナルを見せつける泉りおん。ペニスが吸い込まれるように進入し、痛がるどころか恍惚の笑みを浮かべて「アナル奥まで入って気持ちいい…」と腰を振る姿はアナル愛好家必見の神映像です。</p>
      <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
        <p class="text-rose-300 font-bold mb-1">🔥 絶対に抜ける神シーン・実用ポイント</p>
        <p class="text-slate-300">バックから容赦なくアナル奥深くまで打ち据える激しいピストン。泉りおんがアヘ顔を晒して啼き叫び、最後は肛門の奥深くに濃厚な白濁液をドピュドピュと流し込まれる完璧なアナル中出しフィニッシュです。</p>
      </div>
      <div class="pt-2">
        <a href="/posts/cemd00885" class="text-xs text-rose-400 hover:text-rose-300 underline font-bold">👉 作品個別ページ（サンプル画像・詳細レビュー）を見る</a>
      </div>
    </div>
  </div>

  <div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-6">
    <img src="https://pics.dmm.co.jp/digital/video/cemd00885/cemd00885-1.jpg" alt="サンプル画像1" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/cemd00885/cemd00885-2.jpg" alt="サンプル画像2" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/cemd00885/cemd00885-3.jpg" alt="サンプル画像3" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/cemd00885/cemd00885-4.jpg" alt="サンプル画像4" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
  </div>

  <div class="text-center">
    <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dcemd00885%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-2 bg-slate-800 hover:bg-slate-700 text-rose-300 border border-rose-500/40 font-bold text-sm md:text-base px-8 py-3.5 rounded-xl shadow-lg transition">
      <span>FANZA公式で『泉りおん アナルSEX復活』を見る →</span>
    </a>
  </div>
</div>""",

        # 第4位: 森沢かな
        """<div id="rank-4" class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-3">
      <span class="bg-slate-700 text-rose-300 text-sm md:text-base font-black px-4 py-1 rounded-full">第4位</span>
      <h3 class="text-lg md:text-2xl font-black text-white">1本限りのアナルSEX復活！ 森沢かな</h3>
    </div>
    <div class="text-xs text-slate-400">品番：CEMD-00741 / 出演：""" + get_actress_link("森沢かな（飯岡かなこ）") + """</div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <div class="space-y-4">
      <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dcemd00741%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="block group relative overflow-hidden rounded-xl border border-slate-700">
        <img src="https://pics.dmm.co.jp/digital/video/cemd00741/cemd00741pl.jpg" alt="森沢かな アナルSEX復活" class="w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-4">
          <span class="text-white text-xs font-bold bg-rose-600/90 px-3 py-1 rounded-full">FANZA公式で作品詳細を見る →</span>
        </div>
      </a>
      <div class="flex flex-wrap gap-2">
        """ + get_genre_link("アナル") + " " + get_genre_link("人妻") + " " + get_genre_link("美熟女") + " " + get_genre_link("美尻") + " " + get_genre_link("中出し") + """
      </div>
    </div>
    <div class="space-y-4 text-xs md:text-sm text-slate-300 leading-relaxed">
      <p class="font-bold text-rose-200">【解説・作品の魅力】</p>
      <p>完璧な美貌と引き締まった極上の美ボディを誇る森沢かなが、撮影現場の熱気の中でアナル解禁を承諾したプレミアム作品。大人の色香漂う美熟女が、恥じらいながらもお尻の穴を差し出し、太いペニスに貫かれていく背徳のコントラストが男の本能を狂わせます。</p>
      <p>「本当にお尻でするの…？」と戸惑いながらも、下半身を濡らし、アナルへの侵入に吐息を熱くする森沢かな。大人の女が見せる本気の恥じらいと、快感に負けていく姿がたまらなく淫靡です。</p>
      <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
        <p class="text-rose-300 font-bold mb-1">🔥 絶対に抜ける神シーン・実用ポイント</p>
        <p class="text-slate-300">形の整った美しいヒップを背後から激しく突かれ、肉がぶつかり合う音を響かせながらヨガる森沢かな。肛門がひくひくと収縮して男根を締め上げる圧巻の締め付けは、美熟女・アナル好きの射精中枢を直撃します。</p>
      </div>
      <div class="pt-2">
        <a href="/posts/cemd00741" class="text-xs text-rose-400 hover:text-rose-300 underline font-bold">👉 作品個別ページ（サンプル画像・詳細レビュー）を見る</a>
      </div>
    </div>
  </div>

  <div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-6">
    <img src="https://pics.dmm.co.jp/digital/video/cemd00741/cemd00741-1.jpg" alt="サンプル画像1" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/cemd00741/cemd00741-2.jpg" alt="サンプル画像2" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/cemd00741/cemd00741-3.jpg" alt="サンプル画像3" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/cemd00741/cemd00741-4.jpg" alt="サンプル画像4" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
  </div>

  <div class="text-center">
    <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dcemd00741%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-2 bg-slate-800 hover:bg-slate-700 text-rose-300 border border-rose-500/40 font-bold text-sm md:text-base px-8 py-3.5 rounded-xl shadow-lg transition">
      <span>FANZA公式で『森沢かな アナルSEX復活』を見る →</span>
    </a>
  </div>
</div>""",

        # 第5位: 最上さゆき
        """<div id="rank-5" class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-3">
      <span class="bg-slate-700 text-rose-300 text-sm md:text-base font-black px-4 py-1 rounded-full">第5位</span>
      <h3 class="text-lg md:text-2xl font-black text-white">アナル解禁！2穴ファック解禁！本格緊縛解禁！ 最上さゆき</h3>
    </div>
    <div class="text-xs text-slate-400">品番：MISM-00106 / 出演：""" + get_actress_link("最上さゆき") + """</div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <div class="space-y-4">
      <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dmism00106%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="block group relative overflow-hidden rounded-xl border border-slate-700">
        <img src="https://pics.dmm.co.jp/digital/video/mism00106/mism00106pl.jpg" alt="最上さゆき 2穴アナル解禁" class="w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-4">
          <span class="text-white text-xs font-bold bg-rose-600/90 px-3 py-1 rounded-full">FANZA公式で作品詳細を見る →</span>
        </div>
      </a>
      <div class="flex flex-wrap gap-2">
        """ + get_genre_link("アナル") + " " + get_genre_link("2穴") + " " + get_genre_link("緊縛") + " " + get_genre_link("ハードコア") + " " + get_genre_link("中出し") + """
      </div>
    </div>
    <div class="space-y-4 text-xs md:text-sm text-slate-300 leading-relaxed">
      <p class="font-bold text-rose-200">【解説・作品の魅力】</p>
      <p>並外れたマゾ感度を持つ最上さゆきが、アナル、2穴同時、本格緊縛を一挙に解禁したハードコアの極致。縄で美しく縛り上げられ、逃げ場のない状態で前後の穴を同時に貫かれる壮絶な官能美は、他では決して見られない迫力を誇ります。</p>
      <p>苦痛と快楽の狭間で喘ぎ、前と後ろの穴を同時に激しく突き分けられる最上さゆき。全身を汗で光らせ、快感の極限で痙攣する姿は、マゾヒズムを愛する全ファンの心を鷲掴みにします。</p>
      <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
        <p class="text-rose-300 font-bold mb-1">🔥 絶対に抜ける神シーン・実用ポイント</p>
        <p class="text-slate-300">二本の極太男根に前後から挟み撃ちにされ、膣とアナルの両方に同時にドピュドピュと大量射精されるクライマックス。体液まみれで完全にトリップした最上さゆきのアヘ顔は、脳を焼き切る破壊力です。</p>
      </div>
      <div class="pt-2">
        <a href="/posts/mism00106" class="text-xs text-rose-400 hover:text-rose-300 underline font-bold">👉 作品個別ページ（サンプル画像・詳細レビュー）を見る</a>
      </div>
    </div>
  </div>

  <div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-6">
    <img src="https://pics.dmm.co.jp/digital/video/mism00106/mism00106-1.jpg" alt="サンプル画像1" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/mism00106/mism00106-2.jpg" alt="サンプル画像2" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/mism00106/mism00106-3.jpg" alt="サンプル画像3" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
    <img src="https://pics.dmm.co.jp/digital/video/mism00106/mism00106-4.jpg" alt="サンプル画像4" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />
  </div>

  <div class="text-center">
    <a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dmism00106%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-2 bg-slate-800 hover:bg-slate-700 text-rose-300 border border-rose-500/40 font-bold text-sm md:text-base px-8 py-3.5 rounded-xl shadow-lg transition">
      <span>FANZA公式で『最上さゆき 2穴アナル解禁』を見る →</span>
    </a>
  </div>
</div>"""
    ]
    html_parts.extend(reviews_detail)

    # 比較まとめテーブル ＆ 内部リンク ＆ FAQ
    table_and_links = """<!-- スペック比較テーブル -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl overflow-hidden">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>📊</span> おすすめ初アナル解禁神作5選 徹底スペック比較表
  </h3>
  <div class="overflow-x-auto">
    <table class="w-full text-xs md:text-sm text-left text-slate-300">
      <thead class="bg-slate-800 text-rose-300 border-b border-slate-700 uppercase">
        <tr>
          <th class="py-3 px-4">順位 / タイトル</th>
          <th class="py-3 px-4">主演女優</th>
          <th class="py-3 px-4">お尻開発・美尻度</th>
          <th class="py-3 px-4">実用度・射精圧</th>
          <th class="py-3 px-4">公式リンク</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800">
        <tr class="hover:bg-slate-800/40">
          <td class="py-3 px-4 font-bold text-white">第1位 花狩まい アナル解禁！</td>
          <td class="py-3 px-4">""" + get_actress_link("花狩まい") + """</td>
          <td class="py-3 px-4 text-rose-400">★★★★★（完全処女肛門）</td>
          <td class="py-3 px-4 text-rose-400">★★★★★（至高の悶絶）</td>
          <td class="py-3 px-4"><a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dmiab00284%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="text-rose-400 underline font-bold">FANZAで確認</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="py-3 px-4 font-bold text-white">第2位 アナル解禁AVデビュー！</td>
          <td class="py-3 px-4">""" + get_actress_link("中条鈴華") + """</td>
          <td class="py-3 px-4 text-rose-400">★★★★★（清楚マゾ）</td>
          <td class="py-3 px-4 text-rose-400">★★★★★（アナル潮吹き）</td>
          <td class="py-3 px-4"><a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dmism00185%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="text-rose-400 underline font-bold">FANZAで確認</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="py-3 px-4 font-bold text-white">第3位 1本限りのアナルSEX復活！</td>
          <td class="py-3 px-4">""" + get_actress_link("泉りおん") + """</td>
          <td class="py-3 px-4 text-rose-400">★★★★☆（クイーン貫禄）</td>
          <td class="py-3 px-4 text-rose-400">★★★★☆（極上中出し）</td>
          <td class="py-3 px-4"><a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dcemd00885%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="text-rose-400 underline font-bold">FANZAで確認</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="py-3 px-4 font-bold text-white">第4位 1本限りのアナルSEX復活！</td>
          <td class="py-3 px-4">""" + get_actress_link("森沢かな（飯岡かなこ）") + """</td>
          <td class="py-3 px-4 text-rose-400">★★★★☆（美熟女美尻）</td>
          <td class="py-3 px-4 text-rose-400">★★★★☆（バック締め付け）</td>
          <td class="py-3 px-4"><a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dcemd00741%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="text-rose-400 underline font-bold">FANZAで確認</a></td>
        </tr>
        <tr class="hover:bg-slate-800/40">
          <td class="py-3 px-4 font-bold text-white">第5位 アナル解禁！2穴ファック本格緊縛</td>
          <td class="py-3 px-4">""" + get_actress_link("最上さゆき") + """</td>
          <td class="py-3 px-4 text-rose-400">★★★★☆（2穴同時拡張）</td>
          <td class="py-3 px-4 text-rose-400">★★★★☆（前後同時射精）</td>
          <td class="py-3 px-4"><a href="https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Fdetail%2F%3D%2Fcid%3Dmism00106%2F&af_id=onchan555-003&ch=toolbar&ch_id=link" target="_blank" rel="nofollow noopener" class="text-rose-400 underline font-bold">FANZAで確認</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- 関連特集への内部リンク -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>🔗</span> あわせて読みたい！おすすめキラー特集記事
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs md:text-sm">
    <a href="/posts/feature_fanza_titfuck_paizuri_huge_breasts_suffocation_ranking_2026" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-rose-500/50 transition block">
      <div class="font-bold text-rose-300 mb-1">【神乳に埋もれて昇天】極上パイズリ・巨乳挟まれ窒息射精ランキングTOP5</div>
      <p class="text-slate-400 line-clamp-2">たわわな爆乳の谷間に包まれて精子を一滴残らず搾り取られる夢の母性＆快楽AV選！</p>
    </a>
    <a href="/posts/feature_fanza_aphrodisiac_drugged_ecstasy_spasm_ranking_2026" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-pink-500/50 transition block">
      <div class="font-bold text-pink-300 mb-1">【理性崩壊の肉欲痙攣】媚薬・キメセク・ガンギマリ発情おすすめ神作TOP5</div>
      <p class="text-slate-400 line-clamp-2">清楚美女が超強力媚薬で白目を剥いて腰を振り乱す限界潮吹き交尾AV選！</p>
    </a>
  </div>
</div>

<!-- よくある質問（FAQ） -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>❓</span> 初アナル解禁AVに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-4 text-xs md:text-sm">
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-rose-300 mb-2">Q1. 初アナル解禁作品の一番の見どころは何ですか？</h4>
      <p class="text-slate-300 leading-relaxed">女優が未知の挿入に羞恥と緊張で怯えながらも、丁寧にほぐされて快感に目覚めていく表情のドラマチックな変化です。</p>
    </div>
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-rose-300 mb-2">Q2. 一番美少女で初々しいアナル作品はどれですか？</h4>
      <p class="text-slate-300 leading-relaxed">第1位の花狩まい主演作（MIAB-00284）です。専属人気美少女がカメラの前で初めて菊座を開いて受け入れる姿は必見です。</p>
    </div>
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-rose-300 mb-2">Q3. 激しいアナルアクメや潮吹きを見たい場合は？</h4>
      <p class="text-slate-300 leading-relaxed">第2位の中条鈴華主演作（MISM-00185）がおすすめです。清楚なお嬢様美女がアナルピストンだけで潮を吹き狂う姿は圧巻です。</p>
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
                "name": "FANZA「初アナル解禁・お尻開発＆2穴同時」おすすめ神作ランキングTOP5",
                "description": "清楚美女が未知の快感に悶絶し腰を跳ね上げて連続絶頂する至高のお尻快楽AV選【2026年最新】",
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
                        "name": "初アナル解禁作品の一番の見どころは何ですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "女優が未知の挿入に羞恥と緊張で怯えながらも、丁寧にほぐされて快感に目覚めていく表情のドラマチックな変化です。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "一番美少女で初々しいアナル作品はどれですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第1位の花狩まい主演作（MIAB-00284）です。専属人気美少女がカメラの前で初めて菊座を開いて受け入れる姿は必見です。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "激しいアナルアクメや潮吹きを見たい場合は？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第2位の中条鈴華主演作（MISM-00185）がおすすめです。清楚なお嬢様美女がアナルピストンだけで潮を吹き狂う姿は圧巻です。"
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
        "id": "feature_fanza_anal_debut_first_anal_two_holes_ranking_2026",
        "title": "【禁断の初アナル解禁】FANZA「初アナル解禁・お尻開発＆2穴同時」おすすめ神作ランキングTOP5！清楚美女が未知の快感に悶絶し腰を跳ね上げて連続絶頂する至高のお尻快楽AV選【2026年最新】",
        "date": "2026-10-05 06:20:00",
        "hinban": "FIRST-ANAL-DEBUT-DUAL-HOLES-2026",
        "price": "300~",
        "maker": "FANZA公式セレクション",
        "actresses": ["花狩まい", "中条鈴華", "泉りおん", "森沢かな（飯岡かなこ）", "最上さゆき"],
        "genres": ["アナル", "初アナル", "美尻", "開発", "2穴", "潮吹き", "中出し", "特集", "殿堂入り"],
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
    generate_article_lactation()
    print("--------------------------------------------------")
    generate_article_reverse_rape()
    print("--------------------------------------------------")
    generate_article_anal()
    print("==================================================")
    print("3記事すべての生成が正常に完了しました！")
    print("==================================================")

if __name__ == "__main__":
    main()
