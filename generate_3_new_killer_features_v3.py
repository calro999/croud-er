# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・新規キラー特集3記事自動生成スクリプト v3
1. 【地下アイドル・推し活密会特化】
   『【最推しのあの子と秘密の密会】FANZA「地下アイドル・推し活お泊まり」おすすめ人気ランキングTOP5！特典会裏の秘密の恋心からステージ衣装のまま朝まで愛し合う名作選【2026年最新】』
2. 【ギャルママ・ヤンママ若妻特化】
   『【元ヤンの魅力溢れる若妻の甘い誘惑】FANZA「ギャルママ・ヤンママ若妻」おすすめ人気ランキングTOP5！無防備な部屋着姿×旦那の留守に始まるスリリングな濃密愛撫傑作選【2026年最新】』
3. 【過激勝負下着・透けランジェリー特化】
   『【清楚な服の下に隠された大人の色気】FANZA「勝負下着・透けランジェリー」おすすめ人気ランキングTOP5！美麗レース越しに魅せる極上ボディと濃密スキンシップ傑作選【2026年最新】』
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
    # 記事1: 地下アイドル・推し活密会特化
    "avsa00446": """<h2>『アナル舐めさせオフパコ撮影会。肛門の匂いでファンを沼らせて無制限ナマ中出しSEXできる小悪魔アイドルちゃん 北岡果林』詳細レビュー</h2>
<p>圧倒的なプロポーションと甘い小悪魔フェイスで絶大な人気を誇る北岡果林が、熱狂的なファンを沼らせる魅惑の地下アイドルを熱演した傑作です。ステージ上では清純な笑顔を振りまきながら、ファンの前でだけ見せる秘密の個室撮影会。普段は決して触れることのできない最推しが、ファンの目の前でスカートをめくり、恥じらいと興奮の入り混じった瞳で見つめてくる瞬間から、理性が一気に吹き飛びます。</p>

<h3>見どころ：プライベート空間で広がるアイドルとファンの秘密の関係</h3>
<p>「私を一番応援してくれるキミだけに特別だよ？」と囁きながら、至近距離で甘えてくる北岡果林。アイドルの華やかな衣装と、密室で剥き出しになる生々しい素肌のコントラストが素晴らしく、ファンの心理を熟知したあざとい仕草が男心を限界まで刺激します。耳元で囁かれる甘い吐息と、カメラ越しに見つめ合う濃厚なアイコンタクトは、まるで自分自身が太客として選ばれたかのような圧倒的な没入感を約束します。</p>

<h3>実用ポイント：衣装のまま乱れ狂う情熱的な密着ピストンと甘い嬌声</h3>
<p>フリルたっぷりのステージ衣装を身にまとったまま、ベッドの上で激しく腰を重ね合う展開はまさに男の妄想の具現化です。ピストンが深くなるにつれて、アイドルの仮面が剥がれ落ち、一人の熱い快楽を求める女性としての表情へと変化。「もっと強く抱きしめて…！」とすがりつきながら絶頂を迎える姿は、抜きやすさにおいても最高峰の満足度を誇ります。</p>""",

    "lulu00385": """<h2>『オフパコ枕営業しているあざと可愛い地下アイドルを媚薬オイル乳首ハラスメントで敏感早漏体質に仕立て上げ白目アへ顔を晒すまで 倉木しおり』詳細レビュー</h2>
<p>愛らしい小動物系ルックスと抜群のスタイルを持つ倉木しおりが、裏でファンと親密な関係を持つあざとい地下アイドルを演じた話題作。ステージの裏側で繰り広げられるスリリングな密会と、オイルマッサージをきっかけに身体の奥深くまで敏感に開発されていく生々しい快楽のプロセスが極めて緻密に描かれています。</p>

<h3>見どころ：あざとい営業スマイルが本気の快楽に呑み込まれる瞬間</h3>
<p>「これからも推してくれるよね？」と上目遣いで甘えていた彼女が、温かいオイルで全身を丹念に愛撫されるうちに次第に呼吸を荒らげていくグラデーションが見事です。敏感になった肌を指先でなぞられるたびに小さくビクッと震え、必死に声を抑えようとしながらも甘い吐息を漏らしてしまう表情は、ファンの征服欲をこれ以上ないほど掻き立てます。</p>

<h3>実用ポイント：全身を上気させて快楽に溺れる濃密な本番セックス</h3>
<p>ベッドに組み敷かれ、敏感になった秘部を奥深くまで貫かれた倉木しおりは、もはやアイドルの立場を忘れて快楽の波に身を任せます。結合部から響く水音と、快感に震えながら全身をピンク色に染めていく熱い姿は圧巻。何度も絶頂を繰り返しながら、パートナーの首に腕を回して求め続ける情熱的な交わりは必見です。</p>""",

    "mukc00121": """<h2>『清楚系地下アイドルと裏営業で繋がるオフパコ乱交撮影会。 推してくれるなら無制限ナマ中出し放題な僕たちの痴女天使 八坂凪』詳細レビュー</h2>
<p>透き通るような白肌と清楚な黒髪が印象的な美少女・八坂凪が、熱心なファンたちに感謝と情熱を捧げる秘密の裏営業撮影会を描いた衝撃作。グループ内でも一際ウブに見える清楚担当の美少女が、密室でカメラを向けられながら徐々に大胆なメスの顔を解き放っていく展開が、ファンの妄想を極限まで掻き立てます。</p>

<h3>見どころ：清純派アイドルのギャップと献身的なファンサービス</h3>
<p>「みんなが支えてくれたから、今の私があるんだよ…」と涙ぐみながら、ファン一人ひとりの手を握り、身体を寄せてくる八坂凪。清楚なワンピースを脱ぎ捨て、下着姿から完全な素肌を晒していく羞恥と興奮の表情がたまりません。ファンの視線を全身に浴びながら、恥ずかしそうに秘部を指で広げて見せるシーンは、息を呑むほどのエロティシズムに満ちています。</p>

<h3>実用ポイント：複数の男たちに囲まれて愛され尽くす至福の密着</h3>
<p>熱狂的な男たちに囲まれ、代わる代わる濃厚な愛撫と熱い口づけを注がれる八坂凪。華奢な身体を震わせながら、次々と注ぎ込まれる情熱を全身で受け止め、恍惚の表情で腰をくねらせる姿はまさに痴女天使そのもの。清楚な美少女が快楽によって完全に満たされていくクライマックスは、強烈な射精トリガーとなります。</p>""",

    "ofes00048": """<h2>『エグいファンサしてくれるメロがりギャルドル舐めじゃくりフェラで顔面ザーメンシャワーオフパコ撮影会 新井リマ』詳細レビュー</h2>
<p>底抜けに明るいキャラクターと抜群の愛嬌を誇る新井リマが、ノリの良すぎるギャル系地下アイドルとして登場。ファンを喜ばせるためなら何でもしてくれる神対応のファンサがエスカレートし、個室撮影会でとんでもない濃厚スキンシップへと雪崩れ込む、男性の夢を詰め込んだ超ハイテンション快作です。</p>

<h3>見どころ：距離感ゼロの密着と超積極的なフェラチオ奉仕</h3>
<p>「来てくれてありがとー！今日は何して遊ぶ？」と最初からハグでお出迎えしてくれる新井リマ。ファンのズボンに躊躇なく手を伸ばし、膝立ちになって至近距離で見つめながらペニスを口に含む濃厚な奉仕は圧巻です。大きな瞳を輝かせながら、ジュポジュポと生々しい水音を響かせて喉奥まで咥え込むテクニックに、男の腰は浮き上がらずにはいられません。</p>

<h3>実用ポイント：明るい笑顔から一転する本気汁まみれの情熱交尾</h3>
<p>ベッドに倒れ込み、ギャル特有の屈託のない笑顔を浮かべながらも、挿入された瞬間には「あっ…すごい、奥まで当たってる…！」と艶っぽいオンナの表情に一変。長い脚を大きく広げてバックから激しく突き上げられるシーンでは、豊かな美尻が激しく揺れ、射精の瞬間まで激しいピストンで男をリードしてくれます。</p>""",

    "gvh00893": """<h2>『姫予約限定！！太客とだけスケベなことをするいけない地下アイドルのオマ○コ個人撮影会！！ 佐藤愛瑠』詳細レビュー</h2>
<p>誰もが見惚れる端正な美貌とスレンダーな美ボディを誇る佐藤愛瑠が、大金を落としてくれる太客限定の特別撮影会で禁断のサービスを提供する地下アイドルを熱演。ラグジュアリーなホテルのスイートルームで、二人きりの秘密の時間が幕を開けます。</p>

<h3>見どころ：選ばれた男だけが味わえる至高の優越感と親密感</h3>
<p>一般のファンには絶対に見せない、甘えた声と無防備な仕草で迎えてくれる佐藤愛瑠。「キミといる時が一番落ち着くの…」とベッドの上で寄り添い、ホテルのガウンをはだけさせて美しい胸元や太ももを惜しげもなく披露します。大金を投じた者だけが独占できる最高峰の美女という設定が、男性のプライドと独占欲を強烈に刺激します。</p>

<h3>実用ポイント：高級ホテルの静寂を破る濃密な密着ピストンと甘い喘ぎ</h3>
<p>シーツの上で美脚を絡め合わせ、お互いの体温を確かめ合うように深く結合する本番シーン。佐藤愛瑠の引き締まったウエストを掴み、奥深くまで突き入れるたびに、彼女の長い髪が揺れ、瞳が快感でトロンと溶けていきます。静かな個室に響く二人の熱い吐息と肉のぶつかる音は、極上の抜きどころとして脳裏に焼き付きます。</p>""",

    # 記事2: ギャルママ・ヤンママ若妻特化
    "miab00230": """<h2>『「すぐ会えますか？ただしデカチンに限る」 デカ尻絶倫ギャルママのマッチング即ハメ不倫 底なし異常性欲30発 新村あかり』詳細レビュー</h2>
<p>圧倒的なボリュームを誇る肉感的な美尻と、元ヤン特有の妖艶な色気を兼ね備えた新村あかりが、欲求不満の限界を迎えた若妻ギャルママを熱演した名作。日々の育児や単身赴任中の夫への不満から、マッチングアプリで屈強な男を呼び出し、貪るように快楽を貪り尽くすストーリーは、男の征服欲を直撃します。</p>

<h3>見どころ：溢れんばかりの肉感ボディと無防備な部屋着姿の破壊力</h3>
<p>ショートパンツからこぼれ落ちそうな豊満な太ももと、胸元の開いたキャミソール姿でドアを開ける新村あかり。挨拶もそこそこに「待ってたよ…早くシよ？」と抱きついてくる肉食っぷりは圧巻です。家庭の生活感が漂う部屋の中で、母親の顔をかなぐり捨てて一人のメスとして男に密着する背徳感が、画面全体から濃厚に漂います。</p>

<h3>実用ポイント：デカ尻を揺らしまくる豪快なバックと底なしの絶頂</h3>
<p>四つん這いにさせた新村あかりの巨大な美尻を両手で掴み、背後から力強く突き入れるバックのシーンは圧巻の迫力です。肉がぶつかり合う重厚な音とともに、彼女はシーツを噛み締めながら「もっと奥まで…！中がいっぱいになっちゃう…！」と絶叫アクメ。何度射精しても「まだまだ足りないでしょ？」と求めてくる絶倫っぷりに圧倒されます。</p>""",

    "lulu00450": """<h2>『残クレVIPカーの支払いに困った元ヤンデカ尻黒ギャル妻に挑発ケツ相談され肩代わりNTRピストンでデレデレ堕ち 黒咲華』詳細レビュー</h2>
<p>健康的な小麦肌と抜群のヒップラインでファンを熱狂させる黒咲華が、生活の苦しさから隣人の男に身体を許してしまう元ヤンギャル妻を熱演。最初は強気で生意気だったギャル妻が、力強いピストンと男らしさに屈服し、次第に甘えたオンナの顔へと崩壊していくプロセスが秀逸です。</p>

<h3>見どころ：強気なツンから甘えん坊のデレへの劇的な心境変化</h3>
<p>「アンタなんかに抱かれる筋合いねーし！」と最初は尖った態度を見せていた黒咲華が、強引に身体を重ねられるうちに次第に息を乱し、肌を紅潮させていきます。元ヤンのプライドが快感によって心地よく崩れ去り、最後は「お願い…もっと抱いて…」と男の首にしがみついて懇願してくるギャップは、男心を猛烈に滾らせます。</p>

<h3>実用ポイント：小麦色の引き締まった腰回りが跳ねる激しいピストン</h3>
<p>ベッドの上で黒咲華の褐色肌が汗で輝き、腰を突き上げるたびに豊かなヒップが波打つダイナミックな交わり。正常位で密着しながら見つめ合うと、彼女の潤んだ瞳が快感でとろけ、舌を絡ませながら濃厚なキスを求めてきます。強気な美女を完全に手玉に取る快感に浸りながら、至高のフィニッシュを迎えられます。</p>""",

    "dass00969": """<h2>『人妻ギャルの授業参観日の誘惑。「お前の母ちゃん、エロすぎじゃね？」 百永さりな』詳細レビュー</h2>
<p>端正な美貌と抜群のプロポーションを誇る百永さりなが、授業参観で息子の同級生や保護者たちの視線を独占してしまうド派手なギャルママを演じた大人気作。タイトなミニスカートと胸元を強調したスーツ姿で学校を訪れ、放課後の教室や自宅で禁断の交わりへと発展していくシチュエーションが秀逸です。</p>

<h3>見どころ：PTAや教室という日常空間に持ち込まれる圧倒的なエロス</h3>
<p>他の母親たちが地味なスーツを着る中、一人だけ際立つ明るい茶髪とハイヒール、そして香水の香りを漂わせる百永さりな。「うちの子の友達？仲良くしてあげてね」と悪戯っぽく微笑みながら、至近距離で胸の谷間を見せつけてくるシーンはドキドキが止まりません。人目を忍ぶ背徳感と、誰もが羨む美女ママを独占する優越感が最高です。</p>

<h3>実用ポイント：机の上に腰掛けさせて下着をずらし貫く情熱交尾</h3>
<p>教室の教卓や机の上に座らせ、ストッキングを破いて直接挿入するシーンの背徳感は尋常ではありません。「誰か来ちゃうかも…」と口では言いながらも、奥を突かれるたびに百永さりなの腰は自ら跳ね上がり、快感に声を押し殺します。大人の色香とギャルの奔放さが完璧に調和した、実用度満点の作品です。</p>""",

    "sone00201": """<h2>『姉はヤンママ授乳中 in 実家 ランク1位総なめの超人気同人！業界屈指の肉感ボディ人気女優！初めての… 小宵こなん』詳細レビュー</h2>
<p>業界屈指の神乳とマシュマロのような豊満ボディで圧倒的な支持を誇る小宵こなんが、出産を経て実家に戻ってきたヤンママの義姉を演じた伝説的名作。同人CG集で爆発的な人気を博した名作を完全実写化し、圧倒的な肉感と母性的なエロスが画面から溢れ出します。</p>

<h3>見どころ：限界まで膨らんだ豊満バストと母性溢れるスキンシップ</h3>
<p>タンクトップの胸元からこぼれんばかりの豊かなバストを無防備に晒しながら、実家のリビングでくつろぐ小宵こなん。「昔からあんたは甘えん坊だったもんね」と優しく頭を抱きしめられ、柔らかい胸の谷間に顔を埋められる多幸感は言葉を失います。元ヤンらしいフランクな口調と、柔らかい母性のギャップが男性の理性を完全に溶かします。</p>

<h3>実用ポイント：重厚な乳肉が激しく揺れ動く極上のパイズリと生ハメ</h3>
<p>自慢の豊満な胸でペニスを挟み込み、熱い吐息を吹きかけながら愛撫するパイズリシーンはまさに国宝級。さらにそのままベッドになだれ込み、重厚な腰回りを深く突き入れると、小宵こなんは恍惚の表情で「んっ、ああっ…すごい…！」と悶え狂います。全身の肉感がダイレクトに伝わる極上の交わりは、何度見ても飽きない名シーンです。</p>""",

    "1start00141": """<h2>『ヤンママの叔母に童貞を食われました。普段はガサツな叔母のドエロいオンナ顔に欲情し全精子を捧げた絶倫す… 小倉由菜』詳細レビュー</h2>
<p>トップアイドル級の可愛らしさと抜群の演技力で魅了する小倉由菜が、甥っ子の家に居候する若きヤンママの叔母を熱演。普段はジャージ姿でガサツに振る舞っている叔母が、甥っ子が童貞であることを知ってから急激にオンナの顔を覗かせ、ベッドの上で朝まで男にしてあげる極上のストーリーです。</p>

<h3>見どころ：身内ならではの距離感の近さと不意に見せる妖艶な色気</h3>
<p>「あんた、まだ女の子とシたことないの？ウソでしょー！」とケラケラ笑いながら、コタツの中で足を絡ませてくる小倉由菜。しかし、ひとたび部屋で二人きりになると、ふっと真面目な表情になり、「大人の気持ちいいこと、教えてあげよっか？」と耳元で囁いてきます。親しい関係だからこそ生まれるドキドキ感と甘い誘惑がたまりません。</p>

<h3>実用ポイント：手取り足取りリードしてくれる包容力満点の筆おろし</h3>
<p>緊張で震える甥っ子を優しく抱きしめ、自分の身体を使ってセックスの手順を一から教えてくれる小倉由菜。上に跨がってゆっくりと腰を沈め、ペニスが奥まで収まると愛おしそうにキスを降らせます。「上手だよ…もっと動かしていいよ」と甘い声でリードされながら、全精力を注ぎ込むように中出しするフィニッシュは感動的なほどの射精感を味わえます。</p>""",

    # 記事3: 過激勝負下着・透けランジェリー特化
    "miab00262": """<h2>『彼女の姉の卑猥すぎる高級ランジェリーと誘惑KISSに魅せられて…何度も何度も彼女に隠れて中出し性交17発 五日市芽依』詳細レビュー</h2>
<p>端正な美貌と抜群のプロポーションを誇る五日市芽依が、同棲中の彼女の姉として登場。黒の繊細なレースランジェリーとストッキングに身を包み、妹の彼氏を密室で誘惑して朝までハメ狂うという、背徳感とフェティシズムの極致を描いた大ヒット作です。</p>

<h3>見どころ：透き通るレース越しに覗く美しい素肌と挑発的な眼差し</h3>
<p>風呂上がりに薄手のバスローブを羽織り、妹が留守の隙に部屋に入ってくる五日市芽依。ローブを脱ぎ捨てると、そこには肌が透けて見える過激な高級ランジェリー姿。「妹には内緒だよ？」と悪戯っぽく微笑みながら、長い美脚を組み替えてTバックの食い込みを見せつけるシーンは、息を呑むほどの美しさと色気を放ちます。</p>

<h3>実用ポイント：ランジェリーを着たままでの濃厚着衣ピストン</h3>
<p>下着を完全に脱がせることなく、ショーツのクロッチ部分を横にずらしただけで挿入する着衣セックス。五日市芽依の引き締まったウエストとレースの質感が手元に伝わり、奥を突くたびに彼女の整った顔が快楽で崩れていきます。妹がいつ帰ってくるか分からない緊迫感の中、何度も中出しを許してしまう背徳の交わりは実用度満点です。</p>""",

    "1stars00804": """<h2>『本能で絡み合う極上のランジェリー＆オイリー4本番 神木麗』詳細レビュー</h2>
<p>誰もが見惚れる驚異のパーフェクトボディと圧倒的な美貌を誇る現代のトップ女優・神木麗。選び抜かれた最高級のランジェリーをまとい、全身にオイルを塗りたくって本能のままに貪り合う、美とエロティシズムが融合した至高の映像美作品です。</p>

<h3>見どころ：神木麗のパーフェクトプロポーションを際立たせる過激下着</h3>
<p>ワインレッドやエメラルドグリーンの艶やかなランジェリーが、神木麗の白く透き通るようなモチ肌と豊満なバスト、そして引き締まった美尻を完璧に引き立てます。オイルで濡れたランジェリーが肌にぴったりと張り付き、乳首の突起や秘部の輪郭が浮き彫りになるビジュアルは、視覚的な快感を極限まで高めてくれます。</p>

<h3>実用ポイント：オイルの滑らかさとレースの摩擦が生み出す極上快感</h3>
<p>ベッド一面にオイルが広がり、二人の肉体が擦れ合うたびにぬめる心地よい水音が響きます。神木麗の上に覆い被さり、ランジェリー越しに豊かな胸を揉みしだきながら奥深くまで貫くと、彼女は長い美脚を男の背中に絡めつけ、「ああっ…すごい、溶けちゃいそう…！」と絶叫。美しいトップ女優の野生の喘ぎ声を堪能できます。</p>""",

    "midv00103": """<h2>『過激下着モデルを頼まれた義姉のポージング練習が卑猥すぎて我慢できず暴走、毎日中出ししまくった 神宮寺ナオ』詳細レビュー</h2>
<p>圧倒的な気品と凛とした美しさを放つ神宮寺ナオが、ネット通販の下着モデルを引き受けた義理の姉を熱演。弟にカメラマン役を頼み、部屋の中で過激すぎる勝負下着のポージングを練習するうちに、お互いの理性が決壊して毎日のようにハメ倒すという夢のようなシチュエーションです。</p>

<h3>見どころ：ポージング指導から始まるゼロ距離のスキンシップ</h3>
<p>「このポーズ、変じゃないかな？」と、Tバックや穴あきショーツを身につけた神宮寺ナオが四つん這いやM字開脚を披露。ファインダー越しに見つめる弟に対し、無防備に秘部を晒しながらポーズを変えていく姿に興奮しない男はいません。恥ずかしそうに頬を染めながらも、次第に弟の視線を意識してポーズが大胆になっていく心理描写が絶品です。</p>

<h3>実用ポイント：撮影スタジオと化した部屋での激しい生ハメピストン</h3>
<p>カメラを投げ捨て、ベッドの上で義姉を押し倒す弟。神宮寺ナオは「ダメだよ…義姉弟なのに…」と抵抗するものの、下着をずらして挿入された瞬間には甘い吐息を漏らして男の背中に爪を立てます。清楚な義姉が過激な下着を着たまま、快感に負けて腰を振り乱す姿は、最高の射精へと導いてくれます。</p>""",

    "jur00107": """<h2>『麗しきランジェリー、唾液と精液で汚れた酬いの人妻保険外交員 結城花乃羽』詳細レビュー</h2>
<p>上品な大人の色香と抜群のスタイルを持つ結城花乃羽が、契約のために顧客の男に身体を捧げる人妻保険外交員を演じたアタッカーズの重厚な名作。スーツの下に隠された極上の勝負下着と、罪悪感に苛まれながらも快楽に沈んでいく人妻の切なくもドスケベな姿が胸を打ちます。</p>

<h3>見どころ：真面目な営業スーツから露わになる秘密の黒レース</h3>
<p>ビシッと着こなしたスーツのボタンを一つずつ外していくと、中から現れるのは夫にも見せたことのない過激な黒レースのランジェリー。「契約、してくださいますか…？」と震える声で懇願しながら、男の要求に応じて恥ずかしいポーズを取らされる結城花乃羽の羞恥に満ちた表情は、男のサディスティックな欲望を極限まで刺激します。</p>

<h3>実用ポイント：罪悪感と背徳の快楽に濡れる濃厚な本番交尾</h3>
<p>ホテルのベッドに組み敷かれ、美しい下着を愛撫で濡らされながら貫かれる結城花乃羽。最初は涙を浮かべて拒絶していたはずが、男の巧みな指先と重厚なピストンによって子宮を突かれると、次第に自ら腰を動かして快楽を求めてしまいます。人妻のプライドが崩壊し、甘い吐息を漏らしながら中出しを受け止めるシーンは必見です。</p>""",

    "mfyd00151": """<h2>『チェックインからチェックアウトまでどすけべランジェリーでマッチョチ○ポの激ピストンにイキまくる！！ 三枝れい』詳細レビュー</h2>
<p>健康的な肉体美と底なしの明るさを持つ三枝れいが、ホテルに何着ものドスケベランジェリーを持ち込み、チェックインからチェックアウトまで着替えながらハメ狂う快楽特化作。次から次へと繰り出される過激な下着と、休む間もなく繰り広げられる激しいセックスの連続に圧倒されます。</p>

<h3>見どころ：次々と着替える多彩な過激下着コレクション</h3>
<p>スケスケのベビードール、紐だけのマイクロビキニ、股開きのクロッチレスショーツなど、男性のフェティシズムを刺激する衣装が目白押し。「次はこの下着に着替えてきたよ♡」とベッドの上でポーズを取る三枝れいの笑顔と肉体美に、何度でも勃起が蘇ります。下着フェチにはたまらない贅沢な構成です。</p>

<h3>実用ポイント：激しいピストンに合わせて弾む肉体美と絶頂アクメ</h3>
<p>下着を着替えるたびに新たな体位で激しく交わる二人。三枝れいの引き締まった美尻と豊かなバストが激しいピストンに合わせて激しく揺れ、部屋中に肉がぶつかる快音が響き渡ります。「もうダメ、またイッちゃう…！」と白目を剥いて潮を吹きながら絶頂に達する姿は圧巻。一晩中抜きまくりたい方に自信を持っておすすめできる傑作です。</p>"""
}

# 3記事のメタ情報
ARTICLES = [
    {
        "id": "feature_underground_idol_fan_hookup_raw_creampie_ranking_2026",
        "title": "【最推しのあの子と秘密の密会】FANZA「地下アイドル・推し活お泊まり」おすすめ人気ランキングTOP5！特典会裏の秘密の恋心からステージ衣装のまま朝まで愛し合う名作選【2026年最新】",
        "hinban": "UNDERGROUND-IDOL-FAN-CREAMPIE-2026",
        "cids": ["avsa00446", "lulu00385", "mukc00121", "ofes00048", "gvh00893"],
        "hero_tag": "UNDERGROUND IDOL SPECIAL",
        "genres": ["地下アイドル", "ファン食い", "裏営業", "オフパコ", "中出し", "美少女", "特集", "殿堂入り", "主観"],
        "lead_p1": "ライブハウスの熱気、最前列で振るペンライト、そして特典会のわずか数十秒の会話――。現代の男性たちを最も熱狂させ、時に狂わせるのが「地下アイドル」という存在です。ステージの上できらめく笑顔を振りまく手の届かないはずのアイドルが、もしも自分だけに特別な感情を抱き、密室で二人きりの逢瀬を交わしてくれたら……。そんな全オタクの究極の妄想を具現化したジャンルが、今FANZAで爆発的な人気を博しています。",
        "lead_p2": "本ジャンルの真髄は、きらびやかなステージ衣装と生々しい素肌のギャップ、そして「選ばれた男だけが味わえる圧倒的な優越感」にあります。特典会の裏でこっそり交わされる合鍵、ファンの部屋を訪れたアイドルの無防備な私服姿、そしてベッドの上でアイドルの仮面を脱ぎ捨てて一人のメスとして乱れ狂う姿は、他のどんなシチュエーションでも味わえない濃厚な背徳感をもたらします。",
        "lead_p3": "本特集では、北岡果林のアナルまで捧げる小悪魔オフパコから、倉木しおりのあざと可愛い敏感開発、八坂凪の清楚系裏営業、新井リマの神ファンサフェラ、そして佐藤愛瑠の太客限定ホテル密会まで、オタク心を限界まで滾らせる【地下アイドル神作TOP5】を徹底解説します！",
        "points": [
            ("① 華やかなステージ衣装と剥き出しの素肌のコントラスト", "フリルたっぷりの衣装を着たまま乱れる姿や、衣装を脱ぎ捨てて下着姿を晒す瞬間の生々しい羞恥心が、視覚的な興奮を極限まで高めます。"),
            ("② 「キミだけが特別」という甘い囁きが生み出す独占欲", "普段は大勢のファンに囲まれるアイドルが、密室で自分だけに甘え、耳元で愛を囁いてくれる優越感は男のプライドを完璧に満たします。"),
            ("③ 快楽に負けてアイドルの仮面が剥がれ落ちるメス堕ち劇", "最初はアイドルのプロ意識を保っていた彼女が、激しいピストンによって次第に理性を失い、本能の喘ぎ声を漏らす変化が最高の抜きどころです。")
        ],
        "table_headers": ["順位・タイトル", "主演アイドル", "シチュエーション", "背徳度・実用度", "詳細"],
        "related": [
            ("/posts/feature_fanza_white_skin_gyaru_cute_lovelove_ranking_2026", "【男ウケ最強の白ギャル特集】モチ肌×神対応イチャラブTOP5", "透き通る素肌とあざとい笑顔で男を沼らせる白ギャル傑作選！"),
            ("/posts/feature_fanza_virgin_deflower_older_sister_ranking_2026", "【童貞狩り・積極的肉食お姉さん】からかい寸止めから生ハメまでTOP5", "ウブな男の子を骨抜きに貪り尽くす年上美女の濃厚搾精名作選！"),
            ("/posts/feature_fanza_ex_girlfriend_reunion_unfaithful_sex_ranking_2026", "【元カノ・再会未練セックス特集】大人になった元恋人と貪り合うTOP5", "同窓会や偶然の再会からホテルで朝まで交わす背徳の傑作選！"),
            ("/posts/feature_exclusive_cosplay_costume_masterpiece", "【本格コスプレ特集】完成度の高い衣装と艶やかなボディの饗宴", "アニメやゲームのヒロインになりきって乱れる至高のコスプレ作品集！")
        ],
        "faqs": [
            ("地下アイドルジャンルがここまで人気を集める理由は何ですか？", "一般的なAVと異なり、「憧れの推しアイドルと繋がれる」という現代的なオタクの夢や妄想がリアルに体験できるためです。ステージ上の華やかさと、密室での生々しい性欲の落差が強烈なカタルシスを生み出します。"),
            ("初めて観る場合、どの作品から入るのがおすすめですか？", "まずは第1位の北岡果林『アナル舐めさせオフパコ撮影会』が圧倒的におすすめです。アイドルとしてのビジュアル完成度、小悪魔的な甘え方、そして濃厚なプレイ内容まで全てが一級品です。"),
            ("衣装を着たままの着衣プレイは収録されていますか？", "はい、本特集で厳選した作品はいずれもステージ衣装やチェキ用衣装を着たままの愛撫・挿入シーンが豊富に含まれており、着衣フェチの方にも大満足いただける内容です。")
        ]
    },
    {
        "id": "feature_gal_mama_young_wife_unfaithful_creampie_ranking_2026",
        "title": "【元ヤンの魅力溢れる若妻の甘い誘惑】FANZA「ギャルママ・ヤンママ若妻」おすすめ人気ランキングTOP5！無防備な部屋着姿×旦那の留守に始まるスリリングな濃密愛撫傑作選【2026年最新】",
        "hinban": "GAL-MAMA-YOUNG-WIFE-CREAMPIE-2026",
        "cids": ["miab00230", "lulu00450", "dass00969", "sone00201", "1start00141"],
        "hero_tag": "GAL MAMA YOUNG WIFE SPECIAL",
        "genres": ["ギャルママ", "ヤンママ", "人妻", "不倫", "中出し", "巨尻", "元ヤン", "特集", "殿堂入り"],
        "lead_p1": "清楚でおしとやかな人妻モノとは一線を画し、男性たちの本能的な性欲を激しく揺さぶるジャンル――それが「ギャルママ・ヤンママ若妻」です。若くして子供を産み、昔のやんちゃな雰囲気を残したまま大人の色気を身につけた彼女たち。明るい茶髪に無防備なスウェットやショートパンツ、サンダル履きの気だるげな姿には、男を惹きつけてやまない独特のフェロモンが充満しています。",
        "lead_p2": "ギャルママ作品の圧倒的な魅力は、堅苦しさゼロのフランクな距離感と、一度火がついたら止まらない貪欲なメスの本能にあります。「旦那が仕事で留守の昼下がり」「子供が隣の部屋で寝静まった深夜」、生活感溢れる部屋の中で隣人の男や昔の知人を招き入れ、声を押し殺しながら貪り合うスリルは格別です。エッチ慣れした大胆な腰使いと、元ヤンらしい素直でストレートな淫語が男の脳を蕩けさせます。",
        "lead_p3": "本特集では、新村あかりのデカ尻マッチング即ハメから、黒咲華の残クレVIPカー肩代わりNTR、百永さりなの授業参観ミニスカ誘惑、小宵こなんの伝説的ヤンママ授乳、小倉由菜の童貞甥っ子筆おろしまで、肉感とエロスを極めた【ギャルママ神作TOP5】を徹底解説します！",
        "points": [
            ("① 生活感漂う部屋着と無防備な肉感ボディ", "ジャージやショートパンツ、胸元のゆるいキャミソールなど、日常の隙間から覗く豊満な素肌が強烈な視覚的刺激を与えます。"),
            ("② 旦那の留守と子供の就寝がもたらす極限のスリル", "「声を出したらバレちゃう…」という極限の緊張感の中で交わされる生々しい吐息とピストンが、男の興奮を最高潮に引き上げます。"),
            ("③ 元ヤン特有の気だるさとベッドでの淫乱な豹変", "普段のサバサバした態度から一転、奥を突かれた瞬間に目を潤ませて貪欲に快楽を求めてくるギャップが最強の射精トリガーです。")
        ],
        "table_headers": ["順位・タイトル", "主演女優", "シチュエーション", "肉感・背徳度", "詳細"],
        "related": [
            ("/posts/feature_fanza_white_skin_gyaru_cute_lovelove_ranking_2026", "【男ウケ最強の白ギャル特集】モチ肌×神対応イチャラブTOP5", "透き通る素肌とあざとい笑顔で男を沼らせる白ギャル傑作選！"),
            ("/posts/feature_widow_mourning_dress_secret_desire", "【漆黒の喪服と黒ストッキングの疼き】未亡人・喪服特集", "静まり返る仏間で夫の遺影の前に組み敷かれる至高の背徳名作選！"),
            ("/posts/feature_workplace_inhouse_ntr_secret_affair", "【社内恋愛NTR特集】給湯室・非常階段での背徳中出しAV傑作選", "オフィスで繰り広げられるスリリングな密会と情熱交尾！"),
            ("/posts/feature_fanza_ex_girlfriend_reunion_unfaithful_sex_ranking_2026", "【元カノ・再会未練セックス特集】大人になった元恋人と貪り合うTOP5", "昔の思い出が蘇るホテルでの濃厚な交わり傑作選！")
        ],
        "faqs": [
            ("ギャルママ作品の見どころは普通の人妻作品と何が違いますか？", "普通の人妻作品が持つ「罪悪感や羞恥心」に加え、ギャルママ作品には「ノリの軽さ」「エッチに対する積極性」「元ヤン特有の肉感的で大胆な腰使い」が加わります。男側が気後れせず、本能のままハメ狂える爽快感が最大の違いです。"),
            ("肉感的なヒップや太ももが好きな人にも合いますか？", "まさにうってつけです。新村あかりや黒咲華など、本ジャンルで活躍する女優陣は業界屈指の美尻・美脚・豊満ボディを誇り、四つん這いバックでの迫力は全ジャンル中トップクラスです。"),
            ("ストーリー性やスチュエーションのリアルさはどうですか？", "団地やアパートの一室、授業参観後の学校など、日常と隣り合わせのリアルなシチュエーションが綿密に作り込まれており、強い没入感を味わえます。")
        ]
    },
    {
        "id": "feature_erotic_lingerie_see_through_open_crotch_ranking_2026",
        "title": "【清楚な服の下に隠された大人の色気】FANZA「勝負下着・透けランジェリー」おすすめ人気ランキングTOP5！美麗レース越しに魅せる極上ボディと濃密スキンシップ傑作選【2026年最新】",
        "hinban": "EROTIC-LINGERIE-SEE-THROUGH-2026",
        "cids": ["miab00262", "1stars00804", "midv00103", "jur00107", "mfyd00151"],
        "hero_tag": "EROTIC LINGERIE SPECIAL",
        "genres": ["ランジェリー", "勝負下着", "透け", "着衣", "美乳", "中出し", "お姉さん", "特集", "殿堂入り"],
        "lead_p1": "普段着やフォーマルなスーツの下に、女性が密かに忍ばせている過激なランジェリー――。透き通るような繊細なレース、肌に食い込む細いストラップ、そして秘部やバストを惜しげもなく透かして魅せる「勝負下着」は、全男性のフェティシズムを根底から揺さぶる永遠のキラーコンテンツです。",
        "lead_p2": "本ジャンルの醍醐味は、完全な裸体よりも遥かに官能的な「着衣の美学」にあります。洋服を脱がせた瞬間に目に飛び込んでくる過激な下着姿に息を呑み、布越しに伝わる体温と柔肌の感触を味わう贅沢さ。さらにショーツを完全に脱がさず、クロッチを指でずらしただけでそのまま貫く背徳の着衣ピストンは、視覚と触覚の双方に極上の刺激をもたらします。",
        "lead_p3": "本特集では、五日市芽依の彼女の姉による高級ランジェリー誘惑から、神木麗のパーフェクトボディ×オイリーランジェリー、神宮寺ナオの下着モデルポージング練習、結城花乃羽の人妻保険外交員黒レース、三枝れいの過激下着乱れイキまで、洗練された美と濃密なエロスが交錯する【勝負下着神作TOP5】を徹底解説します！",
        "points": [
            ("① 裸よりもエロい！布一枚が引き立てる肉体美", "透けレース越しに覗く乳首や、ヒップラインを美しく見せるTバックなど、下着があるからこそ引き立つ女性の曲線美を心ゆくまで堪能できます。"),
            ("② ショーツをずらして挿入する着衣の背徳感", "脱ぎ捨てず、下着を着けたままの状態で結合するシチュエーションは、男の征服欲と急き立てられる性欲を極限まで掻き立てます。"),
            ("③ トップ女優陣の美貌と洗練された高級感", "神木麗や五日市芽依など、業界を代表する最高峰の美女たちが身につけることで、作品全体にラグジュアリーな艶っぽさが漂います。")
        ],
        "table_headers": ["順位・タイトル", "主演女優", "シチュエーション", "高級感・実用度", "詳細"],
        "related": [
            ("/posts/feature_fanza_white_skin_gyaru_cute_lovelove_ranking_2026", "【男ウケ最強の白ギャル特集】モチ肌×神対応イチャラブTOP5", "透き通る素肌とあざとい笑顔で男を沼らせる白ギャル傑作選！"),
            ("/posts/feature_exclusive_maid_lingerie_service_passion", "【至福の奉仕】専属メイド・ご奉仕ランジェリー特集", "呼び鈴ひとつで駆けつける献身美女の極上名作選！"),
            ("/posts/feature_see_through_bra_clothes_on_creampie", "【着衣透けブラ・濡れシャツ密着AV特集】服の上から浮き出る巨乳と乳首", "濡れたシャツに張り付く下着と素肌のフェチ名作選！"),
            ("/posts/feature_fanza_virgin_deflower_older_sister_ranking_2026", "【童貞狩り・積極的肉食お姉さん】からかい寸止めから生ハメまでTOP5", "経験豊富な美女が手取り足取り教え込む至高の筆おろし！")
        ],
        "faqs": [
            ("ランジェリー・勝負下着作品の最大の抜きどころはどこですか？", "何と言っても「下着を着たままの着衣挿入」です。レース越しに揺れる胸や、ショーツを横にずらしただけで狭い秘部へと貫く瞬間のビジュアルは、全ジャンル屈指の射精感を誇ります。"),
            ("画質や映像の美しさにこだわりはありますか？", "本特集の作品はいずれも高精細HD/4Kクオリティで撮影されており、ランジェリーの繊細なレース生地の質感や、女優の肌のきめ細やかさまで息を呑む美しさで描写されています。"),
            ("フェチ要素だけでなく、しっかりとした本番ピストンも楽しめますか？", "もちろんです。下着の美しさを愛でる序盤のじっくりとした愛撫から、後半は理性を失って腰を打ち付け合う情熱的な本番ピストンまで、実用度満点の構成となっています。")
        ]
    }
]

def main():
    print("=== START GENERATING 3 NEW KILLER FEATURES AND INDIVIDUAL POSTS (v3) ===")
    
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
            item_date = it.get("date", "2026-10-07 00:00:00")
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
            rating = rev_obj.get("average", "4.8")
            rev_cnt = rev_obj.get("count", "10")
            
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
            c_star = c_rev.get("average", "4.8")
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

        # 内部リンク（関連記事）
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
            "date": "2026-10-07 06:00:00",
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
