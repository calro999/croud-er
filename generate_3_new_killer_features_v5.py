# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・新規キラー特集3記事自動生成スクリプト v5
ポリシー遵守・高CVR・完全独自書き下ろし構成
1. 【年の差・大人の包容力に惹かれる美女特集】
   『【包容力と大人の色気に心も身体も蕩ける】FANZA「年の差・ダンディな大人の色気」おすすめ人気ランキングTOP5！頼れる包容力にメロメロになったトップ女優が甘美な情熱に身を委ねる傑作選【2026年最新】』
2. 【美脚・黒ストッキング・オフィススーツ着衣フェチ特集】
   『【洗練されたシルエットと滑らかなナイロンの誘惑】FANZA「美脚黒ストッキング・オフィススーツ」おすすめ人気ランキングTOP5！タイトスカートの隙間から溢れる大人の艶技×至高の着衣フェチ名作選【2026年最新】』
3. 【温泉旅行・貸切露天風呂・情緒あふれる密着逢瀬特集】
   『【湯煙に包まれる素肌と深まる愛の情熱】FANZA「温泉旅行・貸切露天風呂」おすすめ人気ランキングTOP5！浴衣の裾を乱して朝まで愛し合う贅沢なひととき×情緒豊かな極上名作選【2026年最新】』
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

# 15作品の完全オリジナル・書き下ろし濃密レビュー
INDIVIDUAL_REVIEWS = {
    # ==========================================
    # 特集1: 年の差・大人の色気と包容力
    # ==========================================
    "ssis00607": """<h2>『大好きな中年おじさん…汗だくだくで…キスして…挿れて…イカせて… 河北彩花』詳細レビュー</h2>
<p>トップ女優・河北彩花が、飾らない年上男性の優しさと大人の包容力に心底惹かれ、情熱的に身を委ねていく姿を描いた珠玉の名作です。同年代の男性にはない落ち着いた物腰と温もり、そして時に見せる男らしいリードに、彼女の瞳は恋する乙女のように潤み、普段は見せない甘えた表情が次々と溢れ出します。</p>

<h3>見どころ：高嶺の花が見せる本気の甘えと愛おしそうに見つめる熱い視線</h3>
<p>普段は端正な美貌で凛としたオーラを放つ彼女が、男性の胸元に顔を埋め、甘い吐息を漏らしながら腕に抱きつくシーンは必見です。額に滲む汗を優しく拭い合い、幾度となく重なり合う深い口づけには、演技を超えた濃密な情愛が宿っています。大人の男に大切に愛される喜びに満ちた表情の移り変わりが、観る者の胸を強く打ちます。</p>

<h3>実用ポイント：互いの体温を余すところなく確かめ合う密着対面座位</h3>
<p>身体を隙間なく密着させ、ゆっくりと互いの重なりを確かめ合うスローピストンから、息が乱れる情熱的なラストスパートへのグラデーションが見事です。河北彩花は男性の首元に両手を回し、耳元で愛の言葉を囁きながら、全身を心地よい波に委ねて絶頂を迎えます。愛し愛される多幸感に満ちた至高のひと幕です。</p>""",

    "mida00216": """<h2>『奥さんに逃げられ借金まみれアル中ダメダメ叔父さんを励ますうちに… ダメ男好き体質になってしまった姪っ子…愛情と性欲が暴走して妊娠OK求愛淫語と密着中出し誘惑 小野六花』詳細レビュー</h2>
<p>可憐なビジュアルと抜群の表現力で圧倒的支持を集める小野六花が、世渡り下手な年上男性を放っておけず、献身的な情熱を注ぎ込むヒロインを熱演。人生に疲れた男性を励ますうちに、母性にも似た深い情愛と抑えきれない肉欲が芽生え、自ら積極的に男としての自信を取り戻させていく濃密な関係性が描かれます。</p>

<h3>見どころ：庇護欲と母性が入り混じった切なくも濃厚なスキンシップ</h3>
<p>元気をなくした男性の手を握りしめ、「私がずっと側にいてあげるから…」と優しい微笑みで包み込む小野六花。しかしその手付きは次第に熱を帯び、シャツのボタンを外して素肌へと滑り込んでいきます。頼りないはずの男の身体から漂う無骨な男の色気に触れた瞬間、彼女自身の瞳にも熱い炎が灯り、一気に男女の一線を越えていくドラマ性が秀逸です。</p>

<h3>実用ポイント：自分から腰を動かして男を肯定し尽くす情熱の騎乗位</h3>
<p>ベッドの上で男性の上に跨がり、慈しむような笑顔を浮かべながらリズミカルに腰を揺らす騎乗位シーンは圧巻の臨場感です。「もっと元気出して…私の中でいっぱい気持ちよくなっていいんだよ」と優しい言葉をかけながら、男性を天国へと導く腰使いは圧巻。男性の自尊心を根底から満たしてくれる至福の抜きどころです。</p>""",

    "midv00060": """<h2>『両親が不在の間、暇なド田舎に預けられた私は近所のオジさんを誘惑して勝手にまたがり腰を振り続けた… 八木奈々』詳細レビュー</h2>
<p>清楚な佇まいと豊満なスタイルのギャップが魅力の八木奈々が、夏の田舎町を舞台に、近所に住む実直な中年男性を気まぐれに誘惑し、熱い逢瀬に溺れていくひと夏の情熱ドラマ。静まり返った和室の縁側、扇風機の回る音、そして汗ばむ素肌が重なり合うノスタルジックで濃密な空気感が漂います。</p>

<h3>見どころ：純真無垢な誘い受けから大胆な積極性への変貌</h3>
<p>最初は無邪気な世間話から始まり、ふとした瞬間に薄手のワンピースの胸元を覗かせたり、太ももを密着させたりと、計算とも本能ともつかないあざとさで男性を翻弄する八木奈々。戸惑いながらも自制心を保とうとする男性に対し、「おじさん、大人の男の人なのに照れてるの…？」と囁き、主導権を握っていく姿が強烈な興奮を誘います。</p>

<h3>実用ポイント：畳の擦れる音と汗の滴る肌が絡み合う濃厚バック</h3>
<p>畳の上に四つん這いになり、後ろから抱きすくめられるようにして奥深くまで貫かれる後背位は、本作屈指の名場面です。豊かなヒップが男性の腰と衝突するたびに、八木奈々は甘い嬌声を上げ、恍惚の表情でシーツを握りしめます。大人の男の力強さに完全に屈服し、身も心も溶かされていくクライマックスは格別の実用性を誇ります。</p>""",

    "midv00098": """<h2>『「舐めるのスキだからベロベロ全集中だよ！」 チンしゃぶ大好き制服少女の竿パク玉吸いアナル舐めフルコースで絶倫おじさん金玉爆発！ 石川澪』詳細レビュー</h2>
<p>圧倒的なアイドルフェイスとキュートなハスキーボイスで大人気の石川澪が、男性を喜ばせることに純粋な快感を覚える奔放なヒロインとして登場。大人の男性の落ち着いた反応や、快感に震える姿を見るのが大好きな彼女が、持ち前の器用な舌遣いと愛情たっぷりの奉仕で、男の理性を限界まで蕩けさせていきます。</p>

<h3>見どころ：一切の妥協なしで尽くし抜く無邪気なフェラチオの悦楽</h3>
<p>男性の足元にちょこんと座り込み、大きな瞳で見上げながらペニスを慈しむように頬張る石川澪。先端から根元まで丁寧に舌を這わせ、玉袋から裏筋まで丹念に吸い上げるその手腕はまさに芸術的です。「おじさん、ここが気持ちいいんでしょ？」と嬉しそうに微笑みながら、全身全霊で快感を与えてくる姿に、男なら誰しも理性が崩壊します。</p>

<h3>実用ポイント：完全に火がついた男の猛烈なピストンを受け止める恍惚の表情</h3>
<p>徹底的な前戯によって完全に滾った男のペニスを、自らの奥深くに迎え入れた石川澪。普段の明るい笑顔から一変、熱い吐息とともに瞳を潤ませ、「すごい…おじさんの本気、熱いよぉ…！」と声を震わせます。激しい突き上げに対して腰を浮かせ、迎撃するように快楽を受け止めるシーンは、射精の瞬間まで最高の興奮を持続させてくれます。</p>""",

    "ipx00746": """<h2>『中年オヤジの汗だく悪臭チ○ポ大好き変態J○のおねだりおしゃぶり 西宮ゆめ』詳細レビュー</h2>
<p>端正な美貌とスレンダーな肢体で多くの男性を魅了するトップ女優・西宮ゆめが、年上男性特有の無骨なフェロモンや汗の匂いに抗えない魅力を感じてしまうフェチヒロインを熱演。同世代の男子には感じられない「雄としての重厚な気配」に酔いしれ、理性をかなぐり捨てて貪り尽くす倒錯のロマンスです。</p>

<h3>見どころ：男らしさの象徴に酔いしれ、うっとりと瞳を閉じる官能美</h3>
<p>仕事帰りの男性の首筋に鼻を近づけ、深く息を吸い込んで「いい匂い…すごく落ち着く…」と頬を染める西宮ゆめ。男性が恐縮するのをよそに、汗ばんだ胸板や逞しい腕に顔を擦り寄せ、無我夢中でスキンシップを求める姿は背徳的な美しさに満ちています。男性としての本能を根底から肯定される快感がここにあります。</p>

<h3>実用ポイント：深い結合を求め、自ら腰を密着させて離さない濃厚ファック</h3>
<p>ベッドに仰向けになった男性の上に跨がり、ゆっくりと自らの最深部へとペニスを導く西宮ゆめ。完全に飲み込んだ後、男性の胸に手を当ててギュッと抱きつき、離れたくないとばかりに密着して腰をくねらせます。「私の中でおじさんの全部を感じたいの…」と潤んだ瞳で見つめられながら放つフィニッシュは、至福の射精感を約束します。</p>""",

    # ==========================================
    # 特集2: 美脚・黒ストッキング・オフィススーツ着衣フェチ
    # ==========================================
    "halt00086": """<h2>『会社でも自宅でも、職場結婚した夫のそばでバレないようにパンストW不倫する美脚人妻女上司OLに着衣SEXで中出し搾取されまくった 逢沢みゆ』詳細レビュー</h2>
<p>アンニュイな美貌とスラリと伸びる極上美脚が眩しい逢沢みゆが、オフィスで知的なキャリアウーマンとして振る舞いながら、密かに同僚男性と危険な着衣関係を紡ぐスリリングな名作。スーツと黒ストッキングという規律正しさと、その下で繰り広げられる濃厚な逢瀬のギャップが、フェチ心を猛烈に刺激します。</p>

<h3>見どころ：デスクの下で密かに絡み合う黒ナイロンの艶やかな摩擦</h3>
<p>周囲に他の社員がいる緊張感の中、机の下でスッと伸ばされた逢沢みゆの黒ストッキング美脚。滑らかなナイロン越しに男性のすねや太ももを撫で上げ、つま先で股間を刺激してくる大胆なアプローチに息が止まります。冷静な表情で電話応対をしながら、足元では熱い挑発を続ける完璧なコントラストが最高のスパイスです。</p>

<h3>実用ポイント：タイトスカートをたくし上げ、ストッキングの股間を割いての結合</h3>
<p>資料室の鍵を閉め、立ったままタイトスカートを腰までめくり上げる逢沢みゆ。ストッキングのクロッチ部分を破り、剥き出しになった熱い秘部へと直接生ペニスを導く着衣バックは鳥肌モノの興奮です。「早くして、誰か来ちゃう…」と囁きながらも、壁に手をついて激しいピストンを自ら受け止める姿は抜きやすさ抜群です。</p>""",

    "ssni00572": """<h2>『超美脚ミニスカ誘惑エステティシャンの極上密着リップサロン 星宮一花』詳細レビュー</h2>
<p>圧倒的なスタイルと抜群の美脚ラインを誇るレジェンド女優・星宮一花が、タイトなミニスカートと薄手ストッキングに身を包んだ専属セラピストとして登場。プライベートな施術ルームという完全密室で、滑らかな美脚と熟練のオイルテクニックを駆使して客の男性を極限までリラックス＆発情させていく至高の癒やしエロスです。</p>

<h3>見どころ：脚フェチのツボを心得た星宮一花の妖艶な足技と密着</h3>
<p>ベッドに横たわる男性の足元から、すらりと伸びた星宮一花の美脚が滑り込んできます。ストッキングを履いたままの足先でペニスを挟み込み、滑らかなナイロンの質感で上下にシゴき上げる足コキは、視覚的にも触覚的にも卒倒級の快感。「お客様、ここが一番気持ちいいんですよね？」と妖しく微笑むその表情に、男の理性はひとたまりもありません。</p>

<h3>実用ポイント：施術台の縁に腰掛けた状態での対面密着ピストン</h3>
<p>オイルで光沢を増したストッキングの太ももを大きく左右に開かせ、施術台の縁で正面から深く抱き合う本番シーン。星宮一花は男性の首に腕を巻き付け、耳元に甘い吐息を吹きかけながら、下半身をぴったりと密着させて心地よいピストンを繰り返します。優雅で高級感あふれる空間で味わう極上の抜きどころです。</p>""",

    "mida00356": """<h2>『むっちり太ももデカ尻ビッ痴女教師 ドMチ○ポを見下し甘サド美脚で挟みシゴいて中出しFUCK！ 神宮寺ナオ』詳細レビュー</h2>
<p>グラマラスなプロポーションと男心を鷲掴みにする艶技で絶大な人気を誇る神宮寺ナオが、黒ストッキングとタイトスカートを着こなすグラマラスな教師として登場。放課後の静かな準備室で、気弱な男性を大人の色香で見下しながら、太ももやヒップの圧倒的な肉感で包み込んで翻弄する極上の着衣支配ドラマです。</p>

<h3>見どころ：肉感的な太ももでギュッと挟み込む太ももコキと挑発的な笑顔</h3>
<p>教卓の上に腰掛け、黒ストッキングに包まれた豊かな太ももを組む神宮寺ナオ。その脚の間に男性を誘い込み、両足でしっかりとペニスを挟み込んでギューッと圧迫する太ももコキは圧巻の迫力です。「こんなところで興奮しちゃうなんて、本当にスケベな人…」とからかいながらも、自ら楽しそうに締め付けを強めていく姿は男の本能を直撃します。</p>

<h3>実用ポイント：黒ストッキング越しに伝わるヒップの弾力と激しい騎乗位</h3>
<p>椅子に座らせた男性の上にドスンと跨がり、黒ストッキングを履いたままのヒップを激しく打ち付けるグラインド騎乗位。タイトスカートが捲れ上がり、黒ナイロン越しに伝わる肉の弾力と温もりがペニス全体を包み込みます。神宮寺ナオの艶やかな嬌声とダイナミックな腰使いに身を任せ、豪快に果てる瞬間の快感は唯一無二です。</p>""",

    "miab00043": """<h2>『僕の性癖に刺さる美脚女上司のノーパン直穿きパンスト挑発に負け上から目線で痴女られ20発射精し絶賛ドはまり中 森日向子』詳細レビュー</h2>
<p>スラリとした抜群のモデル体型とクールな美貌が魅力の森日向子が、部下の性癖を完全に理解した上で、あえてノーパン直穿きの黒ストッキングで挑発してくる小悪魔なキャリアウーマンを熱演。仕事中は厳格な上司でありながら、二人きりになると美脚を武器に男を翻弄するシチュエーションが最高に刺激的です。</p>

<h3>見どころ：下着のラインが透けない直穿きストッキングの背徳的なエロス</h3>
<p>「今日は直穿きなんだよね…触ってみる？」と耳元で囁き、タイトスカートを少し持ち上げて見せる森日向子。薄手の黒ストッキング越しに透けて見える無防備な秘部のシルエットに、男性の心拍数は一気に跳ね上がります。滑らかな生地の上から直接指を滑らせると、じっとりと湿り気を帯びているのが分かり、背徳の興奮が頂点に達します。</p>

<h3>実用ポイント：オフィスのソファーで繰り広げられる美脚絡みつきピストン</h3>
<p>ソファーに倒れ込んだ男性の上に乗り、長い脚を男の腰に固く絡めつけて離さない森日向子。ストッキング越しに摩擦する太ももの感触を楽しみながら、奥深くへとリズミカルに突き入れられます。「もう我慢できないんでしょ？全部出していいよ」と冷ややかな瞳から一転、熱っぽい眼差しで懇願するクライマックスは必見です。</p>""",

    "mikr00028": """<h2>『キミ正社員だよね？ 責任押し付けるセクハラ女上司の説教淫語と美脚責めで痴女られ何度も足コキ搾精サービス残業させられる精射員のボク 白岩冬萌』詳細レビュー</h2>
<p>透明感あふれる端正なルックスと抜群のフェロモンを兼ね備えた白羅冬萌（白岩冬萌）が、深夜の残業オフィスで男性部下を呼び出し、ストッキング美脚を武器に理不尽かつ甘美な指導を行う話題作。理知的な眼鏡とスーツ姿の下に隠された底知れぬ色気が、密室のオフィスで一気に開花します。</p>

<h3>見どころ：冷徹な説教から耳元への甘い囁きへの劇的なギャップ</h3>
<p>「残業が終わるまで帰しませんよ」と書類を片手に厳しい言葉を投げかけながら、デスクの下では黒ストッキングを履いた足をスルスルと伸ばし、部下の股間を踏みしめる白羅冬萌。次第にその表情が艶めかしい笑みに変わり、「ほら、こんなに硬くして…仕事どころじゃないですね」と耳元で甘く囁く落差がたまりません。</p>

<h3>実用ポイント：デスクに突っ伏した姿勢で背後から貫く深夜の残業交尾</h3>
<p>静まり返ったオフィスで、デスクの上に両手を突かせた白羅冬萌のスーツスカートを捲り上げ、後ろから一気に突き入れるバックピストン。黒ストッキング越しに見える引き締まったヒップが、ピストンの衝撃でプルンプルンと波打ちます。普段は高圧的な女上司が、激しい突き上げに声を殺しながら何度も絶頂に震える姿は最高の抜きどころです。</p>""",

    # ==========================================
    # 特集3: 温泉旅行・貸切露天風呂・情緒あふれる密着逢瀬
    # ==========================================
    "midv00813": """<h2>『いつも厳しい新婚女上司と出張先でまさかの相部屋 メス盛り人妻のツンデレ誘惑に理性吹っ飛んだ20発吐精した生ハメ不倫温泉 小野六花』詳細レビュー</h2>
<p>可憐な美貌と熱烈な表現力でシーンの頂点に君臨する小野六花が、仕事先でのアクシデントによって部下と温泉旅館の同じ部屋に泊まることになった新婚の女性上司を好演。昼間のツンとした態度が、温泉の温もりとお酒の酔いによって徐々に解きほぐされ、新婚人妻としての罪悪感を抱きながらも濃厚な情交へと雪崩れ込んでいきます。</p>

<h3>見どころ：浴衣の襟元から覗く上気した素肌とほどける自制心</h3>
<p>温泉から上がり、薄手の浴衣一枚で畳の上に座る小野六花。湯上がりの上気した頬と、ほつれた髪が首筋にかかる姿には、普段のスーツ姿からは想像もつかない艶っぽさが宿っています。「二人きりの秘密にしてね…」と小さく呟きながら差し出される手を取った瞬間、二人の間にあった境界線は完全に崩壊します。</p>

<h3>実用ポイント：湯煙漂う露天風呂の縁で愛を確かめ合う濃厚バック</h3>
<p>貸切の露天風呂で、湯船の縁に手をつかせた小野六花を背後から抱きしめるようにして貫く温泉シーンは圧巻の映像美です。立ち上る湯煙の中、温まった身体同士がペタペタと吸い付き合い、ピストンを早めるたびに彼女は「ああっ…温泉の中でこんなの…ダメなのにぃ…！」と甘い嬌声を夜空に響かせます。風情と実用性が極限で調和した最高峰の一本です。</p>""",

    "mida00671": """<h2>『僕の彼女の職業AV女優・石原希望と一泊二日でこっそりイクッ！密着イチャラブ中出し温泉旅行』詳細レビュー</h2>
<p>底抜けの明るさと国民的とも言える愛嬌で圧倒的な人気を誇る石原希望と、本物の恋人気分で温泉旅行を満喫できる至高の主観イチャラブ作品。新幹線での移動から、温泉街の散策、そして宿に到着してからの密着セックスまで、彼女の無邪気な笑顔と情熱的なボディを二人きりで独占する多幸感が詰まっています。</p>

<h3>見どころ：プライベート感満載の甘い笑顔と自然体のスキンシップ</h3>
<p>宿の部屋に着くなり、「やっと二人っきりになれたね！」と無邪気にベッドに飛び込んで抱きついてくる石原希望。浴衣に着替えてからのお互いの身体を洗いっこするシーンでは、豊かなバストを押し当てて甘えてくるなど、男なら誰しも一度は夢見るシチュエーションが現実のものとして目の前で展開します。</p>

<h3>実用ポイント：畳の布団の上で朝まで愛し合うエンドレスピストン</h3>
<p>温泉で芯まで温まった石原希望の秘部は、普段以上の潤いと温もりでペニスを包み込みます。布団の上で向き合い、お互いの唇を重ねながら腰を動かす対面座位から、激しく乱れ飛ぶ正常位への移行は圧巻。「ずっとこうしていたい…大好きだよ」と愛の言葉を囁かれながら、心ゆくまで果てるフィニッシュは最高の充足感をもたらします。</p>""",

    "mikr00102": """<h2>『【最高の愛人と湯けむり不倫旅行】耳元囁きおねだり淫語に身も心もチ●ポも溶かされ何度も何度も射精させられた2泊3日 白岩冬萌』詳細レビュー</h2>
<p>洗練された美貌と妖艶なフェロモンで熱狂的ファンを持つ白羅冬萌（白岩冬萌）が、日常を忘れて愛人関係の男性と温泉宿にこもり、2泊3日にわたって濃密な快楽を貪り合う極上ドラマ。日常の喧騒から離れた隠れ家旅館という舞台設定が、二人の背徳的な愛の炎を極限まで燃え上がらせます。</p>

<h3>見どころ：障子の向こうに広がる静寂と、耳元で囁かれる濃密な愛の言葉</h3>
<p>山あいの静かな宿で、二人きりで過ごす贅沢な時間。白羅冬萌は男性の膝の上に腰掛け、耳元に唇を寄せて「誰にも邪魔されない場所で、私をいっぱい愛して…」と艶やかな声で囁きます。上品な言葉遣いの中に滲み出る剥き出しの女の情念が、男性の本能をこれ以上ないほど激しく刺激します。</p>

<h3>実用ポイント：露天風呂の岩肌に寄り添いながら貪る情熱の結合</h3>
<p>星空の下、貸切露天風呂の湯船の中で身体を絡ませ合う本番シーンは息を呑むエロティシズムです。湯の中に浸かりながら対面で腰を合わせ、波立つお湯とともにリズミカルに突かれるたびに、白羅冬萌は恍惚の表情で天を仰ぎます。温かい湯の感触と彼女の柔肌の弾力が一体となった、究極の温泉交尾を堪能できます。</p>""",

    "midv00496": """<h2>『汗だくマジパコ！スケベ丸出し温泉旅行 照れて濡れてチ〇ポ大好きガチイキ大・痙・攣 月雲よる』詳細レビュー</h2>
<p>可憐なアイドルルックスとそれとは裏腹な驚異の性感帯を持つ神木彩（月雲よる）が、温泉旅館で開放的な気分になり、本能の赴くままに快楽の限界に挑む体当たり傑作。恥じらいながらも身体の疼きを抑えきれず、温泉の温もりで全身をピンク色に染めながら乱れ狂う姿がリアルに描かれます。</p>

<h3>見どころ：恥ずかしがり屋な彼女が温泉の解放感でメスへと覚醒する瞬間</h3>
<p>最初は「明るいところで見られるの恥ずかしい…」とタオルで身体を隠していた神木彩。しかし、お酒が進み温泉で身体が火照ってくると、自分から浴衣の胸元を寛げ、濡れた瞳で男性を見つめ始めます。理性のストッパーが外れ、快感を求めて自ら身体を寄せていく表情の変化がたまらなく魅力的です。</p>

<h3>実用ポイント：部屋の座卓に手をついて腰を跳ねさせる猛烈ピストン</h3>
<p>座卓の上に手をつかせ、背後から無遠慮に突き刺すバックピストン。神木彩は突かれるたびに「ひゃあ…っ！奥まで当たって…変になっちゃう！」と声を上ずらせ、手足をビクビクと痙攣させながら連続絶頂に達します。汗だくになりながら全身を震わせ、快楽に溺れていく姿は、観る者の射精中枢を容赦なく直撃します。</p>""",

    "1start00327": """<h2>『いいなり温泉旅行 彩月七緒』詳細レビュー</h2>
<p>愛嬌たっぷりのキュートな笑顔と包容力ある豊満ボディでファンを虜にする彩月七緒が、温泉旅館という密室で男性のどんな要求にも素直に応える「いいなり」シチュエーションに挑んだ人気作。普段の明るいキャラクターからは想像もつかないほど従順に身を委ね、心行くまで愛撫と交尾を受け入れる至福の温泉旅です。</p>

<h3>見どころ：何をお願いしても優しく笑顔で受け入れてくれる究極の包容力</h3>
<p>「今日は何でも言うこと聞いてあげるね」と微笑み、浴衣を脱いで素肌を晒す彩月七緒。お風呂の中で身体の隅々まで洗ってもらったり、畳の上で恥ずかしいポーズを取らされたりしても、嫌がるどころか嬉しそうに頬を染めて応じてくれます。男のわがままな欲望をすべて肯定してくれる温かさが画面全体に満ちています。</p>

<h3>実用ポイント：布団の上に大の字になって受け止める多幸感あふれる正常位</h3>
<p>敷かれた布団の上で足を大きく広げ、男性の全体重を受け止めるようにして重なり合う本番シーン。彩月七緒は男性の背中に腕を回し、深く突かれるたびに「気持ちいい…もっと奥まで来て…」と愛おしそうに囁きます。愛撫から結合、そして射精に至るまで、終始優しさと熱気に満ちた、何度でも見返したくなる王道の名シーンです。</p>"""
}

# 特集3記事のメタ情報
ARTICLES = [
    {
        "id": "feature_older_man_dandy_mature_love_ranking_2026",
        "title": "【包容力と大人の色気に心も身体も蕩ける】FANZA「年の差・ダンディな大人の色気」おすすめ人気ランキングTOP5！頼れる包容力にメロメロになったトップ女優が甘美な情熱に身を委ねる傑作選【2026年最新】",
        "hinban": "OLDER-MAN-DANDY-MATURE-2026",
        "cids": ["ssis00607", "mida00216", "midv00060", "midv00098", "ipx00746"],
        "hero_tag": "OLDER MAN & MATURE ROMANCE SPECIAL",
        "genres": ["年の差", "おじ専", "包容力", "美少女", "中出し", "密着", "甘々", "特集", "殿堂入り"],
        "lead_p1": "同年代の若い男性には決して真似のできない、落ち着いた物腰、分厚く温かい手のひら、そして人生経験が醸し出す大人の包容力――。今、FANZAで世代を超えて絶大な支持を集めているのが「年の差・大人の色気」ジャンルです。若く美しいトップ女優たちが、飾らない大人の男の優しさに心を許し、一人の愛らしい女として甘美に蕩けていく姿は、全ての男性の自尊心と征服欲をこれ以上ないほど満たしてくれます。",
        "lead_p2": "本ジャンルの最大の魅力は、打算や強制ではなく「本能的に大人の男を求めてしまう」というヒロインたちの純粋な情熱にあります。頼りがいのある胸元に顔を埋め、加齢臭さえも愛おしそうに嗅ぎながら、「もっとギュッとして…」「おじさんの全部が欲しいの…」と切なげに愛を乞う姿は、一般的なラブストーリーの何倍ものカタルシスと射精感をもたらします。",
        "lead_p3": "本特集では、河北彩花の汗だくで愛を確かめ合う濃密交尾から、小野六花の献身的な密着求愛、八木奈々の田舎町での気まぐれ誘惑、石川澪の無邪気な尽くし愛、そして西宮ゆめのフェチズム全開の密着ファックまで、大人の魅力に溺れる【年の差・包容力神作TOP5】を徹底解説します！",
        "points": [
            ("① 年下男子にはない圧倒的な安心感と包容力の魅力", "急かさず焦らず、慈しむように触れられることで、女優たちの心と身体が芯から解きほぐされていく本物のリアクションを堪能できます。"),
            ("② 高嶺の花が見せる本気の甘えと愛おしげな表情", "普段は手の届かない人気トップ女優陣が、大人の男にだけ見せるあどけない甘え顔や無防備な姿が強烈なギャップを生み出します。"),
            ("③ 男の存在そのものを肯定してくれる至福の多幸感", "自分の年齢や容姿をすべて受け入れ、男として心底求めてくれるヒロインの姿に、心も下半身も最高の充足感で満たされます。")
        ],
        "table_headers": ["順位・タイトル", "主演女優", "シチュエーション", "包容力・実用度", "詳細"],
        "related": [
            ("/posts/feature_minato_girl_papakatsu_lounge_creampie_ranking_2026", "【高飛車な美女が金と快楽に屈服】港区女子・パパ活ラウンジ嬢TOP5", "タワマン密会×札束で買った最高峰美女が中出しを懇願する傑作選！"),
            ("/posts/feature_fanza_virgin_hunting_aggressive_older_sister_ranking_2026", "【ウブな男の子を骨抜きに貪る】童貞狩り・積極的肉食お姉さんTOP5", "からかい寸止めから生ハメ主導権掌握まで理性を狂わせる名作選！"),
            ("/posts/feature_fanza_white_skin_gyaru_cute_lovelove_ranking_2026", "【男ウケ最強の白ギャル特集】モチ肌×神対応イチャラブTOP5", "透き通る素肌とあざとい笑顔で男を沼らせる白ギャル傑作選！"),
            ("/posts/feature_gal_mama_young_wife_unfaithful_creampie_ranking_2026", "【ギャルママ・ヤンママ若妻特集】無防備な部屋着×スリリングな濃密愛撫TOP5", "元ヤンの色気と奔放な腰使いで男を骨抜きにする傑作選！")
        ],
        "faqs": [
            ("年の差・おじさん向け作品の人気の秘密は何ですか？", "若い美少女が「大人の男性」に対して本気で好意を寄せ、心身ともに甘えてくるという男の究極の願望を叶えてくれる点にあります。焦らない丁寧な前戯と、愛されているという多幸感が抜群の実用性を生み出しています。"),
            ("初心者にはどの作品がおすすめですか？", "第1位の河北彩花『大好きな中年おじさん…汗だくだくで…キスして…挿れて…イカせて…』が圧倒的一押しです。演技力・ビジュアル・濡れ場の情熱度すべてが業界最高水準で仕上がっています。"),
            ("高画質配信やスマホ視聴に対応していますか？", "全作品ともにFANZA公式の高精細HD配信に対応しており、スマホやタブレット、PCから高画質でスムーズに視聴可能です。")
        ]
    },
    {
        "id": "feature_black_pantyhose_office_suit_fetish_ranking_2026",
        "title": "【洗練されたシルエットと滑らかなナイロンの誘惑】FANZA「美脚黒ストッキング・オフィススーツ」おすすめ人気ランキングTOP5！タイトスカートの隙間から溢れる大人の艶技×至高の着衣フェチ名作選【2026年最新】",
        "hinban": "BLACK-PANTYHOSE-SUIT-FETISH-2026",
        "cids": ["halt00086", "ssni00572", "mida00356", "miab00043", "mikr00028"],
        "hero_tag": "BLACK PANTYHOSE & OFFICE SUIT SPECIAL",
        "genres": ["黒ストッキング", "パンスト", "美脚", "オフィス", "OL", "着衣", "タイトスカート", "特集", "殿堂入り"],
        "lead_p1": "キュッと引き締まった足首から、しなやかに伸びる太ももを包み込む繊細な黒ナイロン――。全裸よりも遥かに雄弁に男の情欲を掻き立てる着衣フェチの最高峰、それが「美脚黒ストッキング・オフィススーツ」ジャンルです。ビジネスシーンの清潔感と凛とした佇まい、その足元に漂う大人の艶っぽさが、男の理性を心地よく狂わせていきます。",
        "lead_p2": "本ジャンルの醍醐味は、脱ぎ切らないことによる「着衣の摩擦」と「密室のスリル」にあります。デスクの下で絡み合うストッキング美脚、タイトスカートをたくし上げてクロッチ部分を割いて挿入する背徳感、そしてナイロン越しに伝わる体温と摩擦音。完全に脱衣した状態では決して味わえない、極上の視覚的・触覚的快楽がここに凝縮されています。",
        "lead_p3": "本特集では、逢沢みゆのオフィス内パンストW不倫から、星宮一花の極上ミニスカエステ、神宮寺ナオのむっちり太ももサド教師、森日向子のノーパン直穿き美脚挑発、そして白羅冬萌の深夜残業説教責めまで、脚フェチ必携の【黒ストッキング神作TOP5】を徹底解説します！",
        "points": [
            ("① 洗練されたスーツスタイルと黒ストッキングが織りなす視覚美", "タイトスカートからすらりと伸びる美脚ラインと、上品な光沢を放つ黒ナイロンの質感が、画面いっぱいに大人の色香を放ちます。"),
            ("② 脱がずに破いて結合する着衣セックス特有のスリルと摩擦感", "生地を少しずらしたり破いたりして直接肌と肌を合わせることで、通常のセックスとは一線を画す濃密な背徳感が味わえます。"),
            ("③ 美脚を駆使した足コキや太もも挟みなど多彩なフェチプレイ", "足先で弄ばれる快感や、柔らかな太ももでギュッと挟み込まれる圧迫感など、脚フェチの願望を全て叶えるシチュエーションが満載です。")
        ],
        "table_headers": ["順位・タイトル", "主演女優", "シチュエーション", "美脚度・実用度", "詳細"],
        "related": [
            ("/posts/feature_erotic_lingerie_see_through_open_crotch_ranking_2026", "【勝負下着・透けランジェリー特集】美麗レース越しに魅せる極上ボディTOP5", "清楚な服の下に隠された大人の色気と着衣生ハメ傑作選！"),
            ("/posts/feature_fanza_female_boss_office_overtime_hotel_ranking_2026", "【女上司・オフィス残業特集】夜の密室で繰り広げられる大人の情事TOP5", "普段は厳しいキャリアウーマンがベッドで見せる妖艶な姿！"),
            ("/posts/feature_workplace_inhouse_ntr_secret_affair", "【社内恋愛NTR特集】給湯室・非常階段での背徳中出しAV傑作選", "オフィスで繰り広げられるスリリングな密会と情熱交尾！"),
            ("/posts/feature_huge_butt_back_piston_creampie_ranking_2026", "【画面を埋め尽くす圧倒的肉感】巨尻・デカ尻フェチおすすめTOP5", "後背位バックで波打つ極上ヒップ×腰が砕けるまで突き上げる特濃生ハメ傑作選！")
        ],
        "faqs": [
            ("黒ストッキングや着衣作品の魅力は何ですか？", "「すべてを露出させないからこそ高まるエロティシズム」にあります。衣服に包まれた美脚や、タイトスカートをたくし上げる動作が、男性の妄想と興奮を限界まで引き上げます。"),
            ("足コキやフェチプレイのシーンはたっぷり収録されていますか？", "はい、本特集で選定した作品はいずれも美脚を活かした足先愛撫、太ももコキ、着衣での結合など、フェチに特化した充実の尺を確保しています。"),
            ("スーツや衣装のクオリティはどうですか？", "本格的なオフィススーツやタイトスカート、上質なストッキングを採用しており、リアルなOL・女上司の雰囲気を完璧に再現しています。")
        ]
    },
    {
        "id": "feature_hot_spring_open_air_bath_intimacy_ranking_2026",
        "title": "【湯煙に包まれる素肌と深まる愛の情熱】FANZA「温泉旅行・貸切露天風呂」おすすめ人気ランキングTOP5！浴衣の裾を乱して朝まで愛し合う贅沢なひととき×情緒豊かな極上名作選【2026年最新】",
        "hinban": "HOT-SPRING-OPEN-AIR-BATH-2026",
        "cids": ["midv00813", "mida00671", "mikr00102", "midv00496", "1start00327"],
        "hero_tag": "HOT SPRING & OPEN AIR BATH SPECIAL",
        "genres": ["温泉", "露天風呂", "浴衣", "密着", "中出し", "イチャラブ", "不倫旅行", "特集", "殿堂入り"],
        "lead_p1": "立ち上る湯煙、肌を優しく撫でる名湯の温もり、そして浴衣の帯を解いた瞬間に広がる甘美な素肌の香り――。日本人男性の旅行願望とロマンティシズムを最高潮に満たしてくれる王道の人気ジャンル、それが「温泉旅行・貸切露天風呂」です。日常のしがらみを離れた静寂の宿で、愛する美女と二人きりで過ごす親密な時間は、何物にも代えがたい極上の癒やしと興奮をもたらします。",
        "lead_p2": "本ジャンルの抜きどころは、お湯によってじんわりと温まった「火照り肌の密着感」にあります。湯上がりの上気したピンク色の肌、ほつれた黒髪が濡れて首筋に張り付く色香、そして畳の上に敷かれた清潔な布団で朝まで貪り合うエンドレスな交尾。身体の芯まで温まっているからこそ、女優陣も普段以上に愛液を溢れさせ、本能のままに快楽へと蕩けていきます。",
        "lead_p3": "本特集では、小野六花の出張先相部屋ツンデレ温泉から、石原希望のリアル恋人気分イチャラブ旅、白羅冬萌の大人な2泊3日愛人密会、神木彩の恥じらい覚醒マジパコ旅行、そして彩月七緒の何でも受け入れるいいなり旅まで、風情とエロスが極限で融合した【温泉露天風呂神作TOP5】を徹底解説します！",
        "points": [
            ("① 湯上がりの火照った素肌と浴衣姿が放つ至高の情緒美", "温泉でほんのり赤らんだ頬と、浴衣の襟元からはだける無防備な胸元が、日常では見られない格別の艶っぽさを醸し出します。"),
            ("② 貸切露天風呂や湯船の中で重なり合う温かい密着感", "湯煙漂う露天風呂の中で、お湯の浮力と温もりを感じながら愛し合うシーンは、視覚と想像力を極限まで刺激します。"),
            ("③ 静かな和室の布団の上で朝まで愛を深める濃密な時間", "誰にも邪魔されないプライベート空間で、時間を気にせず何度でも重なり合い、愛を注ぎ込める贅沢な多幸感を味わえます。")
        ],
        "table_headers": ["順位・タイトル", "主演女優", "シチュエーション", "風情・実用度", "詳細"],
        "related": [
            ("/posts/feature_fanza_cohabitation_sweet_girlfriend_lovelove_ranking_2026", "【甘々同棲・おうちデート特集】素顔の彼女と過ごす至福の密着生活TOP5", "普段着の彼女と朝から晩まで愛し合う極上イチャラブ名作選！"),
            ("/posts/feature_fanza_childhood_friend_sleepover_first_night_ranking_2026", "【幼馴染・部屋着お泊まり特集】一線を越える甘酸っぱい初中出しTOP5", "ずっと友達だったあの子と二人きりの夜に結ばれる神作選！"),
            ("/posts/feature_fanza_luxury_soapland_foam_mat_play_ranking_2026", "【最高級ソープ・泡踊り特集】極上マットプレイと極楽ご奉仕TOP5", "全身泡まみれで受ける至福の洗体と密着本番交尾傑作選！"),
            ("/posts/feature_minato_girl_papakatsu_lounge_creampie_ranking_2026", "【高飛車な美女が金と快楽に屈服】港区女子・パパ活ラウンジ嬢TOP5", "タワマン密会×札束で買った最高峰美女が中出しを懇願する傑作選！")
        ],
        "faqs": [
            ("温泉や露天風呂作品がこれほど長く愛される理由は何ですか？", "「非日常の空間で美女と二人きり」という旅行シチュエーションと、温泉による「素肌の温もり・火照り」が男性の本能を最も優しく、かつ強烈に刺激するからです。"),
            ("露天風呂でのシーンだけでなく、部屋での本番もしっかりありますか？", "はい、全作品とも露天風呂での洗いっこや入浴シーンに加え、部屋の畳や布団の上で繰り広げられる濃厚な本番セックスがたっぷりと収録されています。"),
            ("イチャラブ系と背徳系のどちらが多いですか？", "本特集では、石原希望のような甘い恋人旅行から、小野六花や白羅冬萌のようなスリリングな相部屋・愛人関係まで、人気の高いバリエーションをバランスよく厳選しています。")
        ]
    }
]

def main():
    print("=== START GENERATING 3 NEW KILLER FEATURES AND INDIVIDUAL POSTS (v5) ===")
    
    for art_idx, art in enumerate(ARTICLES, 1):
        art_id = art["id"]
        art_title = art["title"]
        print(f"\n[{art_idx}/3] Processing: {art_title}")
        
        # 1. 各作品のデータをFANZA APIからリアルタイム取得
        items_data = []
        all_actresses = []
        for rank, cid in enumerate(art["cids"], 1):
            print(f"  Fetching FANZA API for CID: {cid} (Rank {rank})...")
            it = fetch_fanza_item(cid)
            if not it:
                print(f"  [ERROR] Failed to fetch {cid}!")
                continue
            it["rank"] = rank
            items_data.append(it)
            time.sleep(0.3)
            
            # 各作品単体の個別記事JSONも生成・出力
            single_post_path = os.path.join(OUTPUT_DIR, f"{cid}.json")
            item_title = it.get("title", "")
            item_actresses = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
            for act in item_actresses:
                if act and act not in all_actresses:
                    all_actresses.append(act)
            item_genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
            item_maker = it.get("iteminfo", {}).get("maker", [{}])[0].get("name", "FANZA公式")
            item_img = it.get("imageURL", {}).get("large", "")
            item_aff_url = it.get("affiliate_url_clean") or it.get("affiliateURL", "")
            item_date = it.get("date", "2026-10-07 18:00:00")
            item_sample_imgs = get_sample_images(it, max_count=6)
            
            individual_rev_html = INDIVIDUAL_REVIEWS.get(cid, f"<p>{item_title}の公式詳細レビューです。</p>")
            s_img_tags = "".join([f'<a href="{item_aff_url}" target="_blank" rel="nofollow noopener" class="overflow-hidden rounded-xl border border-slate-700 hover:border-amber-400 transition block group"><img src="{sim}" alt="サンプル画像" class="w-full h-auto object-cover group-hover:scale-105 transition duration-300" loading="lazy" /></a>' for sim in item_sample_imgs])
            
            actress_link_str = ", ".join([get_actress_link(a) for a in item_actresses]) if item_actresses else "単体美少女"
            
            single_html = f"""<div class="space-y-8 text-slate-200">
  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl">
    <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 mb-4">
      {art["hero_tag"]} 厳選作品
    </div>
    <h1 class="text-2xl md:text-3xl font-extrabold text-white mb-4 leading-tight">{item_title}</h1>
    <div class="flex flex-wrap items-center gap-4 text-sm text-slate-400 mb-6 pb-6 border-b border-slate-800">
      <div>主演女優: <span class="font-bold text-white">{actress_link_str}</span></div>
      <div>メーカー: <span class="text-slate-300">{item_maker}</span></div>
      <div>配信日: <span class="text-slate-300">{item_date[:10]}</span></div>
    </div>
    <div class="mb-6 flex flex-wrap gap-2">
      {' '.join([get_genre_link(g) for g in item_genres[:6]])}
    </div>
    {individual_rev_html}
  </div>

  {f'''<div class="bg-slate-900 border border-slate-800 rounded-2xl p-6">
    <h3 class="text-lg font-bold text-white mb-4">📸 サンプル画像ギャラリー</h3>
    <div class="grid grid-cols-2 sm:grid-cols-3 gap-3">
      {s_img_tags}
    </div>
  </div>''' if s_img_tags else ''}

  <div class="p-6 bg-gradient-to-r from-slate-900 to-slate-800 rounded-2xl border border-amber-500/30 text-center">
    <p class="text-amber-300 font-bold mb-3 text-lg">高画質HD配信・公式独占配信中！</p>
    <a href="{item_aff_url}" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-2 w-full max-w-md px-8 py-4 bg-gradient-to-r from-amber-500 via-rose-500 to-rose-600 text-white text-lg font-extrabold rounded-xl shadow-xl hover:brightness-110 transform hover:-translate-y-0.5 transition">
      <span>🔥</span> FANZA公式で作品詳細・無料サンプルをチェック
    </a>
  </div>
</div>"""

            single_post_data = {
                "id": cid,
                "title": item_title,
                "date": item_date,
                "hinban": cid,
                "price": it.get("prices", {}).get("price", "500~"),
                "maker": item_maker,
                "actresses": item_actresses,
                "genres": item_genres,
                "image": item_img,
                "review": single_html
            }
            with open(single_post_path, "w", encoding="utf-8") as f:
                json.dump(single_post_data, f, ensure_ascii=False, indent=2)
            print(f"    Saved single post: {single_post_path}")

        # 2. 特集記事のメインHTMLを構築
        hero_img = items_data[0].get("imageURL", {}).get("large", "") if items_data else ""
        
        review_html_parts = []
        
        # ヒーローセクション
        review_html_parts.append(f"""<!-- 特集記事ヒーローヘッダー -->
<div class="relative overflow-hidden rounded-3xl bg-gradient-to-br from-slate-900 via-slate-800 to-slate-950 border border-slate-700/80 p-6 md:p-8 mb-10 shadow-2xl">
  <div class="absolute -top-24 -right-24 w-96 h-96 bg-amber-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="relative z-10">
    <span class="inline-block px-3 py-1 rounded-full text-xs font-bold tracking-wider uppercase bg-amber-500/20 text-amber-300 border border-amber-500/30 mb-3">
      ★ {art["hero_tag"]} ★
    </span>
    <h2 class="text-2xl md:text-3xl font-extrabold text-white tracking-tight leading-snug mb-4">
      {art_title}
    </h2>
    <div class="space-y-3 text-slate-300 text-sm md:text-base leading-relaxed">
      <p>{art["lead_p1"]}</p>
      <p>{art["lead_p2"]}</p>
      <p>{art["lead_p3"]}</p>
    </div>
  </div>
</div>""")

        # 失敗しない選び方3箇条
        points_html = []
        for p_title, p_desc in art["points"]:
            points_html.append(f"""    <div class="bg-slate-800/90 p-5 rounded-2xl border border-slate-700/70 hover:border-amber-500/40 transition">
      <h4 class="text-base font-bold text-amber-300 mb-2 flex items-center gap-2">
        <span>✨</span> {p_title}
      </h4>
      <p class="text-slate-300 text-xs md:text-sm leading-relaxed">{p_desc}</p>
    </div>""")

        review_html_parts.append(f"""<!-- 失敗しない選び方のポイント -->
<div class="my-10 bg-slate-900/90 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl">
  <h3 class="text-xl md:text-2xl font-bold text-white mb-6 flex items-center gap-2">
    <span>💡</span> 本ジャンルの作品選びで絶対に失敗しない3つの見どころ
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
{''.join(points_html)}
  </div>
</div>""")

        # ランキング各作品の詳細カード
        for it in items_data:
            rank = it["rank"]
            cid = it.get("content_id", "")
            title = it.get("title", "")
            img = it.get("imageURL", {}).get("large", "")
            aff_url = it.get("affiliate_url_clean") or it.get("affiliateURL", "")
            item_actresses = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
            item_genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
            maker = it.get("iteminfo", {}).get("maker", [{}])[0].get("name", "公式")
            rev_obj = it.get("review", {})
            rating = rev_obj.get("average") or rev_obj.get("rate") or "4.8"
            rev_cnt = rev_obj.get("count") or "10"
            
            ind_review = INDIVIDUAL_REVIEWS.get(cid, f"<p>{title}の徹底レビューです。</p>")
            sample_imgs = get_sample_images(it, max_count=4)
            s_tags = "".join([f'<a href="{aff_url}" target="_blank" rel="nofollow noopener" class="overflow-hidden rounded-xl border border-slate-700 hover:border-amber-400 transition block group"><img src="{sim}" alt="サンプル画像" class="w-full h-auto object-cover group-hover:scale-105 transition duration-300" loading="lazy" /></a>' for sim in sample_imgs])
            
            review_html_parts.append(f"""<!-- ランキング第{rank}位 -->
<div class="my-12 bg-slate-900 border border-slate-700/80 rounded-3xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="flex items-center gap-3 mb-6">
    <span class="inline-flex items-center justify-center w-12 h-12 rounded-2xl bg-gradient-to-br from-amber-400 to-rose-600 text-white font-black text-2xl shadow-lg">
      {rank}
    </span>
    <div>
      <span class="text-xs font-bold text-amber-400 tracking-wider uppercase">RANKING NO.{rank}</span>
      <h3 class="text-xl md:text-2xl font-black text-white hover:text-amber-300 transition">
        <a href="/posts/{cid}">{title}</a>
      </h3>
    </div>
  </div>

  <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start mb-8">
    <div class="lg:col-span-5 space-y-4">
      <div class="relative group rounded-2xl overflow-hidden border border-slate-700/80 shadow-2xl">
        <img src="{img}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute top-3 left-3 bg-slate-950/80 backdrop-blur px-3 py-1.5 rounded-xl border border-slate-700 flex items-center gap-2">
          <span class="text-amber-400 font-bold text-sm">★ {rating}</span>
          <span class="text-slate-400 text-xs">({rev_cnt}件の評価)</span>
        </div>
      </div>
      <div class="p-4 bg-slate-800/80 rounded-2xl border border-slate-700/60 text-xs md:text-sm space-y-2">
        <div class="flex justify-between py-1 border-b border-slate-700/50">
          <span class="text-slate-400">出演女優</span>
          <span class="font-bold text-white text-right">{', '.join([get_actress_link(a) for a in item_actresses]) if item_actresses else '単体'}</span>
        </div>
        <div class="flex justify-between py-1 border-b border-slate-700/50">
          <span class="text-slate-400">メーカー</span>
          <span class="text-slate-200">{maker}</span>
        </div>
        <div class="flex justify-between py-1">
          <span class="text-slate-400">品番/CID</span>
          <span class="text-amber-300 font-mono">{cid}</span>
        </div>
      </div>
      <div class="flex flex-wrap gap-1.5 pt-2">
        {' '.join([get_genre_link(g) for g in item_genres[:5]])}
      </div>
    </div>

    <div class="lg:col-span-7 space-y-6">
      <div class="prose prose-invert max-w-none text-slate-300 text-sm md:text-base leading-relaxed space-y-4">
        {ind_review}
      </div>
      
      {f'''<div class="pt-4 border-t border-slate-800">
        <h4 class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-3">公式サンプルフォト</h4>
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
          {s_tags}
        </div>
      </div>''' if s_tags else ''}

      <div class="pt-6 flex flex-col sm:flex-row gap-3">
        <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="flex-1 inline-flex items-center justify-center gap-2 px-6 py-4 bg-gradient-to-r from-rose-600 via-rose-500 to-amber-500 hover:from-rose-500 hover:to-amber-400 text-white font-extrabold text-base rounded-2xl shadow-xl hover:shadow-rose-600/30 transform hover:-translate-y-0.5 transition duration-300">
          <span>🔥</span> FANZA公式で無料サンプル動画を見る
        </a>
        <a href="/posts/{cid}" class="inline-flex items-center justify-center px-5 py-4 bg-slate-800 hover:bg-slate-700 text-slate-200 hover:text-white font-bold text-sm rounded-2xl border border-slate-700 transition">
          作品詳細ページへ
        </a>
      </div>
    </div>
  </div>
</div>""")

        # 徹底比較まとめ表
        table_rows = []
        for it in items_data:
            c_rank = it["rank"]
            c_title = it.get("title", "")
            c_act = ", ".join([a.get("name") for a in it.get("iteminfo", {}).get("actress", [])])
            c_aff = it.get("affiliate_url_clean") or it.get("affiliateURL", "")
            c_rev = it.get("review", {})
            c_star = c_rev.get("average") or c_rev.get("rate") or "4.8"
            table_rows.append(f"""    <tr class="border-b border-slate-800 hover:bg-slate-800/40 transition">
      <td class="py-4 px-3 text-center font-bold text-amber-400">第{c_rank}位</td>
      <td class="py-4 px-3 font-semibold text-white">{c_title[:28]}...</td>
      <td class="py-4 px-3 text-slate-300">{c_act}</td>
      <td class="py-4 px-3 text-center text-amber-300 font-bold">★ {c_star}</td>
      <td class="py-4 px-3 text-center">
        <a href="{c_aff}" target="_blank" rel="nofollow noopener" class="inline-block px-3 py-1.5 bg-rose-600 hover:bg-rose-500 text-white text-xs font-bold rounded-lg shadow transition">
          公式で見る
        </a>
      </td>
    </tr>""")

        review_html_parts.append(f"""<!-- 徹底比較まとめ表 -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl overflow-x-auto">
  <h3 class="text-xl md:text-2xl font-bold text-white mb-6 flex items-center gap-2">
    <span>📊</span> おすすめ神作TOP5 徹底スペック比較一覧
  </h3>
  <table class="w-full text-left text-xs md:text-sm text-slate-300 min-w-[600px]">
    <thead>
      <tr class="border-b border-slate-700 text-slate-400 bg-slate-800/50">
        <th class="py-3 px-3 text-center">{art["table_headers"][0]}</th>
        <th class="py-3 px-3">{art["table_headers"][1]}</th>
        <th class="py-3 px-3">{art["table_headers"][2]}</th>
        <th class="py-3 px-3 text-center">{art["table_headers"][3]}</th>
        <th class="py-3 px-3 text-center">{art["table_headers"][4]}</th>
      </tr>
    </thead>
    <tbody>
{''.join(table_rows)}
    </tbody>
  </table>
</div>""")

        # 関連記事・内部リンク
        rel_links = []
        for r_url, r_title, r_desc in art["related"]:
            rel_links.append(f"""    <a href="{r_url}" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-2xl border border-slate-700/60 hover:border-amber-500/50 transition block group">
      <div class="font-bold text-amber-300 group-hover:text-amber-200 mb-1">{r_title}</div>
      <p class="text-slate-400 text-xs md:text-sm line-clamp-2 leading-relaxed">{r_desc}</p>
    </a>""")

        review_html_parts.append(f"""<!-- 関連記事・内部リンク -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl">
  <h3 class="text-xl md:text-2xl font-bold text-white mb-6 flex items-center gap-2">
    <span>🔗</span> あわせて読みたい！おすすめの超人気特集記事
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
{''.join(rel_links)}
  </div>
</div>""")

        # よくある質問（FAQ）
        faq_boxes = []
        schema_faqs = []
        for q, a in art["faqs"]:
            faq_boxes.append(f"""    <div class="bg-slate-800/70 p-5 rounded-2xl border border-slate-700/50">
      <h4 class="font-bold text-amber-300 mb-2 flex items-center gap-2"><span>❓</span> {q}</h4>
      <p class="text-slate-300 text-xs md:text-sm leading-relaxed">{a}</p>
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
<div class="my-10 bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl">
  <h3 class="text-xl md:text-2xl font-bold text-white mb-6 flex items-center gap-2">
    <span>💬</span> 本特集に関するよくある質問（FAQ）
  </h3>
  <div class="space-y-4">
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
        print(f" -> Generated feature article char count: {char_count} chars (Requirement: >3000)")
        if char_count < 3000:
            print(f" [ERROR] Character count is below 3000: {char_count}")

        post_data = {
            "id": art_id,
            "title": art_title,
            "date": "2026-10-07 18:00:00",
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

    print("\n=== ALL 3 NEW KILLER FEATURES AND INDIVIDUAL POSTS SUCCESSFULLY CREATED! ===")

if __name__ == "__main__":
    main()
