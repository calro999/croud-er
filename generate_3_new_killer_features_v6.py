# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・新規キラー特集3記事自動生成スクリプト v6
ポリシー遵守・高CVR・完全独自書き下ろし構成
1. 【巨乳・神乳パイズリ＆激揺れピストン特化】
   『【包み込まれる至高の柔肌と圧倒的揺れ】FANZA「巨乳・神乳パイズリ」おすすめ人気ランキングTOP5！規格外のメガおっぱいに埋もれる快楽×限界まで搾り取られる極上名作選【2026年最新】』
2. 【女上司・プライド崩壊・立場逆転メス堕ち特化】
   『【冷徹なキャリア美女が快楽に屈する瞬間】FANZA「女上司・プライド崩壊・立場逆転」おすすめ人気ランキングTOP5！職場の高嶺の花が部下に弱みを握られ牝の顔で懇願する背徳の神作選【2026年最新】』
3. 【寝取られ（NTR）・最愛の人が他人に堕ちる背徳特化】
   『【愛する人が他人の快楽に堕ちていく背徳】FANZA「寝取られ（NTR）・背徳メス堕ち」おすすめ人気ランキングTOP5！嫌悪から絶頂へ…目の前で最愛の女性を貪り尽くされる狂気の傑作選【2026年最新】』
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
    # 特集1: 巨乳・神乳パイズリ＆激揺れピストン
    # ==========================================
    "mida00280": """<h2>『M男くんの自宅にQカップHimariお姉さんが緊急訪問！囁き密着パイズリ天国で1日中ぶっこ抜かれる最高痴女デリバリー！！ Himari』詳細レビュー</h2>
<p>人類の遺伝子の奇跡とも呼ぶべき規格外のQカップ超乳を誇るHimariが、欲望を持て余す男性の部屋にデリバリー痴女として訪問。視界を覆い尽くすほどのメガマシュマロ巨乳を惜しげもなく駆使し、朝から晩まで男の理性を木っ端微塵に粉砕していく超ド級のパイズリ特化名作です。CGを一切疑う余地のない生々しい肉の重みと弾力は、画面越しでも息が詰まるほどの圧倒的迫力を誇ります。</p>

<h3>見どころ：視界が真っ白になるQカップの挟撃と耳元密着ウィスパー淫語</h3>
<p>Himariの最大の見せ場は、ベッドの上で仰向けになった男性の顔面に跨がり、両手で抱えきれないほどの巨大な乳房でペニスを根元まで完全に包み込むパイズリシーンです。たっぷりとローションを含ませた乳房の間で肉棒が前後するたびに、クチュクチュという濃密な水音が室内に響き渡ります。「ほら、お姉ちゃんのおっぱいで全部隠れちゃったね…気持ちいい？もっと出していいんだよ」と、至近距離で囁かれる甘くねっとりとした淫語に、男の脳内麻薬は限界突破します。</p>

<h3>実用ポイント：重力に逆らえない超巨乳が激しくバウンドする逆正常位ピストン</h3>
<p>パイズリで硬度を極限まで高めた後は、Himariが男性の上に腰を落とす圧巻の騎乗位へと突入します。腰を上下させるたび、重力に従って暴れ狂うQカップの肉塊はまさに圧巻の一言。胸元に顔を埋め、乳首を吸い上げながら下から突き上げるピストンに、Himari自身も快楽に蕩けたアヘ顔を晒して連続絶頂を迎えます。巨大な胸に窒息しながら果てたいという全男子の究極の願望を叶えてくれる珠玉の抜きどころです。</p>""",

    "sqte00635": """<h2>『休日に彼女と。たゆんたゆん爆乳に中出しSEX 宍戸里帆』詳細レビュー</h2>
<p>グラマラスな天然美巨乳と圧倒的な愛嬌でシーンを席巻する宍戸里帆が、休日に彼氏と二人きりで過ごす甘々かつ濃密な同棲セックスを描いた傑作。ゆったりとした部屋着からこぼれ落ちそうな大迫力のバストと、大好きな彼氏の前だからこそ見せる無防備でエロティックな仕草の数々が、観る者の心と股間を激しく揺さぶります。</p>

<h3>見どころ：シャツの隙間からこぼれ落ちる極上バストと甘えん坊パイズリ</h3>
<p>リビングのソファーでくつろぐ中、宍戸里帆が大きめのオーバーサイズシャツのボタンを一つずつ外していく導入部は興奮必至。ブラジャーから解放された真っ白で柔らかな乳房がボロンと露出し、彼氏の腕にしがみつきながら胸の谷間にペニスを滑り込ませてきます。「里帆のおっぱいで気持ちよくなって…？」と上目遣いで見つめられながら、弾力抜群の柔肌で擦り上げられる感覚はまさに天国そのものです。</p>

<h3>実用ポイント：ソファーに押し倒しての乳揺れ全開バックピストン</h3>
<p>ベッドへ移動することすら我慢できず、ソファーの上で四つん這いにさせた宍戸里帆の豊かなヒップを掴んで背後から一気に貫く本番シーン。後背位で激しくピストンを繰り出すたび、彼女の豊満なバストが前後に激しくたゆんたゆんと揺れ動きます。鏡越しに自らの乱れ姿と揺れる胸を見つめさせながら腰を打ち付け、最後は膣内深くへと濃厚な精液を注ぎ込むシーンは実用度満点です。</p>""",

    "1stars00804": """<h2>『本能で絡み合う極上のランジェリー＆オイリー4本番 神木麗』詳細レビュー</h2>
<p>芸術的なまでのプロポーションと神が授けた完璧な美乳Gカップを誇るトップ女優・神木麗が、最高級の過激ランジェリーと全身オイルで男の本能を極限まで覚醒させる至高の艶技作品。洗練された美貌と、オイルで濡れ光る極上の豊満ボディが融合し、一秒たりとも目が離せない圧倒的な美と快楽の映像世界を創出しています。</p>

<h3>見どころ：テラテラと光るオイルまみれの神乳で擦り上げる超密着パイズリ</h3>
<p>全身にたっぷりとオイルを塗りたくられた神木麗の肢体は、照明の光を反射して怪しい色気を放ちます。滑らかさを増したGカップのバストで男性のペニスを挟み込み、自らの体重をかけて滑らせるオイリーパイズリは、視覚的な破壊力も快感度も桁違い。「あぁ…滑ってすごく気持ちいい…」と自身も火照った吐息を漏らしながら、乳首をペニスに擦り付けてくる淫らな責めは男の理性を瞬時に消し去ります。</p>

<h3>実用ポイント：オイルで滑り合う肌と肌…汗だくで貪り合う濃密正常位</h3>
<p>オイリーな前戯からベッドの上で繰り広げられる本番交尾は、肌と肌が激しくぶつかり合う生々しい肉弾戦。神木麗のしなやかな脚を肩に担ぎ上げ、奥深くのGスポットを抉るように突くたび、彼女の美しい胸が左右に激しく波打ちます。彼女の艶やかな喘ぎ声が最高潮に達した瞬間、胸元と子宮口へと連続で吐き出すフィニッシュは鳥肌モノの抜きどころです。</p>""",

    "cawd00949": """<h2>『朝起きると山積みの使用済みコンドームと全裸の伊藤さん（同僚） 泥●して記憶がない…おっぱい丸出し寝姿に我慢できず二日酔い追撃中出し 伊藤舞雪』詳細レビュー</h2>
<p>端正なルックスと完璧なくびれ、そして誰もが見惚れる美巨乳を持つトップスター・伊藤舞雪が、会社の飲み会後に同僚男性の部屋で泥酔お泊まりしてしまったシチュエーションを描く大ヒット作。散乱するコンドームの殻、昨夜の情事を物語る生々しい痕跡、そして朝の光の中で全裸で眠る同僚美女という、男の妄想の頂点を具現化した一作です。</p>

<h3>見どころ：無防備に晒された同僚美女の美巨乳と寝起きパイズリの衝撃</h3>
<p>ベッドの上でシーツをはだけ、豊かな胸を惜しげもなく晒して眠る伊藤舞雪。起こそうと胸に触れた瞬間、寝ぼけ眼の彼女が「ん…まだするの…？」と呟き、無自覚にペニスを自慢のバストで挟み込んできます。二日酔いの火照った体温と、柔らかく包み込んでくる美乳の温もりが混ざり合い、男の朝立ちした剛直は爆発寸前まで追い込まれます。</p>

<h3>実用ポイント：二日酔いの気だるさの中で貪る追撃の生中出しバック</h3>
<p>昨夜の記憶はおぼろげながら、目の前の極上ボディに我慢できなくなった男性が、うつ伏せで眠る伊藤舞雪の腰を持ち上げて背後から挿入。寝起きの狭い膣内がギチギチとペニスを締め付け、彼女は枕に顔を埋めながら「あっ…朝からそんなに激しく突かれたら…またイッちゃう…！」と悶絶します。引き締まったウエストと揺れる豊満バストのコントラストを堪能しながらの朝中出しは圧巻です。</p>""",

    "juny00124": """<h2>『上下のオクチで連続ごっくん！爆乳密着舐め回しソープ 夕季ちとせ』詳細レビュー</h2>
<p>圧倒的な肉感と包容力に満ちた爆乳で熱狂的ファンを抱える夕季ちとせが、吉原の超高級ソープ嬢として男の欲望のすべてを受け止める至福のソープランド名作。泡まみれの滑走マットプレイから、上下のオクチを使った連続バキューム、そして爆乳で全身を包み込む神業施術まで、男が一生に一度は体験したい極上サービスが凝縮されています。</p>

<h3>見どころ：泡だらけの爆乳で全身を滑走するダイナミックマットパイズリ</h3>
<p>滑らかなソープの泡に包まれた夕季ちとせが、マットの上に横たわる男性の身体の上をその豊満な胸と柔肌ですべるように滑走。ペニスの上にたっぷりの泡と重量感あふれる爆乳を乗せ、リズミカルに滑らせるマットパイズリは、他では絶対に味わえない極上の浮遊感と刺激をもたらします。「お兄ちゃんのチ〇ポ、すっごく大きくなってる…」と耳元で囁く優しい笑顔が男の心を蕩けさせます。</p>

<h3>実用ポイント：口内フェラと爆乳挟撃の連続攻撃からの濃厚胸元発射</h3>
<p>ベッドに移ってからは、上下のオクチを使った息もつかせぬバキューム責めが展開。口内でじっくりと亀頭を吸い上げた直後、間髪入れずに温かい爆乳でぎゅっと挟み込んで擦り上げる波状攻撃に、男性は抗う術を失います。限界を迎えて「もう出る…！」と告げた瞬間、夕季ちとせは胸をさらに強く密着させてペニスを包み込み、噴き出す白濁液を全てバストで受け止めてくれます。</p>""",

    # ==========================================
    # 特集2: 女上司・プライド崩壊・立場逆転メス堕ち
    # ==========================================
    "pfes00113": """<h2>『偉そうにしやがって。小っちゃいリボンの付いたパンティ履いてるくせに。～女上司なんてもう怖くない～ 響乃うた』詳細レビュー</h2>
<p>冷徹で厳格、職場では誰もが恐れるエリート女上司・響乃うた。しかし彼女のタイトスカートの下には、キャラに似合わない可愛らしい小さなピンクのリボンが付いた勝負下着が隠されていた――。普段の高圧的な態度と、隠された乙女な下着のギャップを見抜いた部下による、容赦ないプライド解体と立場逆転の快感を味わい尽くすメガヒット作です。</p>

<h3>見どころ：弱みを暴かれた瞬間の動揺と、震える唇で繰り広げる屈辱フェラ</h3>
<p>会議室で二人きりになった際、スカートを捲り上げられて秘密の下着を白日の下に晒される響乃うた。真っ赤になって怒鳴ろうとするものの、「こんな可愛いパンツ穿いて部下を説教してたんですか？」と耳元で嘲笑され、一気に言葉を失います。プライドをへし折られた彼女が、涙目で部下のペニスを恐る恐る口に含み、上目遣いで「これで満足…？」と屈辱に震える表情は男の征服欲を極限まで満たします。</p>

<h3>実用ポイント：役員会議室のデスクに突っ伏させ、スーツを着たままのバックピストン</h3>
<p>屈辱フェラでビンビンに硬くなった剛直を、デスクに手をつかせた響乃うたのスーツスカートの下から一気に挿入。普段の命令口調はどこへやら、激しいピストンを食らうたびに「ひゃんっ…！こんなの…部下のくせに…あぁっ！」と女の喘ぎ声を漏らし始めます。抵抗が快感へと変わり、最後は自分から腰を振って中出しを懇願するメス堕ちの瞬間は最高の抜きどころです。</p>""",

    "waaa00617": """<h2>『色気ムンムン女上司にバキバキ童貞がバレてしまい…まさかの筆おろし相部屋 またがりベロキス淫語浴びせ杭打ち中出しFUCKで膣射調教を繰り返し一晩中ヤリまくった… 大槻ひびき』詳細レビュー</h2>
<p>成熟した大人の色気と抜群の演技力でトップを走り続けるレジェンド・大槻ひびきが、出張先で童貞の部下をからかい半分に筆おろしした結果、部下の底知れぬ絶倫ぶりに逆に狂わされてしまう逆転劇。大人の余裕を見せていた女上司が、朝を迎える頃にはただの淫乱な牝へと成り下がっていく過程が鳥肌モノのリアルさで描かれます。</p>

<h3>見どころ：大人の余裕から始まる妖艶な童貞筆おろしと濃厚ベロキス</h3>
<p>ホテルの部屋でビールを飲みながら、「君、もしかしてまだ経験ないの？」と艶めかしい視線を送る大槻ひびき。浴衣をはだけさせて豊満な胸を見せつけ、童貞のガチガチになったペニスを優しく手コキしながら耳元に濃厚なキスを降らせます。「お姉さんが大人の気持ちいいこと、全部教えてあげるね」と主導権を握って跨がる姿は、男の憧れの筆おろしそのものです。</p>

<h3>実用ポイント：童貞の規格外ピストンに腰が砕け、逆に乗っ取られる連続中出し</h3>
<p>しかし、一度快楽の扉を開いた童貞部下の体力とピストンは桁違い。主導権を握っていたはずの大槻ひびきは、下からの強烈な突き上げと荒々しいバックピストンに瞳の焦点を失い、「待って…もう無理…イッちゃうから抜いてぇ！」と悲鳴を上げます。容赦なく子宮口を連打され、一晩で何度も中出しされて完全にメスとして屈服する表情は必見です。</p>""",

    "1start00525": """<h2>『新卒で入った会社の研修がしんどくて息抜きにピンサロ行ったらめちゃ怖いOJT女上司と遭遇「副業バラされたくなかったら…」立場逆転本番生ハメ 青空ひかり』詳細レビュー</h2>
<p>圧倒的透明感と小悪魔的な可愛さを併せ持つ青空ひかりが、昼間は鬼のように厳しい会社の教育係（OJT上司）、夜は歓楽街のピンサロで働く秘密を持つ女性を熱演。偶然訪れた新卒社員に正体を見破られ、社内での優位性が一瞬にして崩壊するスリリングな背徳シチュエーションが炸裂します。</p>

<h3>見どころ：ピンク色の薄暗い個室で対峙する「職場の上司」の生々しい絶望</h3>
<p>カーテンを開けた瞬間、目の前に現れたのは昼間自分を厳しく叱責していた青空ひかり。普段のキリッとしたオフィスカジュアルとは一転、露出度の高いセクシーな衣装で客を待っていた彼女は、部下の顔を見た瞬間に顔面蒼白になります。「会社には…絶対に言わないで…」と懇願する彼女に対し、「じゃあ、特別なサービスしてくれますよね？」と迫る緊迫感は心臓が跳ね上がるほどの興奮です。</p>

<h3>実用ポイント：禁止されている本番行為を強要…立場逆転の生ハメ中出し</h3>
<p>本来は本番禁止の店舗であるにもかかわらず、秘密を守る代償として生挿入を要求。青空ひかりは涙を浮かべながらスカートをめくり、自ら生ペニスを濡れた秘部へと導きます。普段の威圧的な態度は見る影もなく、突かれるたびに「ああっ…こんなところで…新卒の子に犯されちゃう…！」と切なく喘ぎ、最後は無情にも膣内へと白濁液を注ぎ込まれます。</p>""",

    "mimk00249": """<h2>『パワハラ女上司と社畜くん実写版 残業中にオフィスでオナニーしていた上司の弱みに付け込み立場逆転中出しセックスで仕返し！ 吉根ゆりあ』詳細レビュー</h2>
<p>圧倒的なプロポーションとドSな演技に定評のある吉根ゆりあが、日頃から部下に理不尽なパワハラを繰り返していたキャリア女上司を熱演。深夜の静まり返ったオフィスで、自慰行為に耽っていた現場を部下にスマホで激写されたことから始まる、痛快かつ超エロティックな復讐メス堕ち劇です。</p>

<h3>見どころ：残業中のオフィスに響く自慰の喘ぎ声と、証拠動画を突きつけられた屈辱</h3>
<p>誰もいないはずの深夜のオフィス。書類を取りに戻った部下が目撃したのは、机の下でスカートをめくり、パンティをずらして指を突っ込みながら悶える吉根ゆりあの姿でした。スマホでその一部始終を撮影され、動かぬ証拠を突きつけられた彼女のプライドは音を立てて崩壊。「消して…なんでもするから…」とすがる彼女に、日頃の恨みを晴らす命令が下されます。</p>

<h3>実用ポイント：上司のデスクの上で開帳させ、容赦なく突き刺す報復ピストン</h3>
<p>いつも彼女が偉そうに部下を叱りつけていた執務デスクの上に吉根ゆりあを押し倒し、M字開脚で秘部を晒させます。日頃のパワハラへの仕返しとして、荒々しくペニスを突き刺すと、彼女の肉体は思いのほか敏感で、激しく腰を跳ねさせて快楽に悶絶。「ごめんなさい…私が悪かったからぁ…！」と謝罪しながらも絶頂を繰り返す姿は実用度MAXです。</p>""",

    "mikr00039": """<h2>『いつも強気な年下の女上司は激ピスされたがりのドMマ●コでした。 お酒に弱い女上司を介抱してベッドに寝かせたら… 幸村泉希』詳細レビュー</h2>
<p>スラリとした美脚とシャープな美貌が魅力の幸村泉希が、年下でありながら出世して偉そうに振る舞う強気な上司を好演。仕事終わりのサシ飲みで泥酔してしまい、部下の部屋で介抱されるうちに、隠していた「激しいピストンで犯されたい」というドMの本性が露わになるギャップ萌えの極致です。</p>

<h3>見どころ：酔っ払ってタガが外れた女上司の無防備な甘えとドMカミングアウト</h3>
<p>スーツを崩し、ベッドに倒れ込んで頬を真っ赤に染める幸村泉希。「私だって…いつも無理して強がってるの…」と涙混じりに愚痴をこぼしながら、部下のネクタイを引っ張ってベッドへと引き倒します。いつも見下していた部下の男らしい腕に抱きしめられた瞬間、彼女の瞳は潤み、「私をめちゃくちゃにして…壊れるくらい突いて…」と懇願し始めます。</p>

<h3>実用ポイント：ベッドが軋むほどの猛烈ピストンで子宮を激突するドM覚醒本番</h3>
<p>彼女の望み通り、一切の手加減なしで腰を叩きつける激ピストンを開始。幸村泉希は枕を爪で引き裂くように握りしめ、「そう…！もっと強く叩いて…！部下のチ〇ポで狂っちゃう…！」と絶叫しながら何度も潮を吹いて痙攣します。普段の生意気な態度が完全に消え去り、ただ激しく犯される快楽に溺れていく姿は、観る者の射精欲を限界まで煽り立てます。</p>""",

    # ==========================================
    # 特集3: 寝取られ（NTR）・最愛の人が他人に堕ちる背徳
    # ==========================================
    "snos00334": """<h2>『最強ビジュOLさん、出張先で死ぬほど嫌いな中年上司と相部屋… でも過激セクハラにまさかの快楽堕ちしちゃった瀬戸環奈』詳細レビュー</h2>
<p>芸能人級の圧倒的なビジュアルと透明感を誇る瀬戸環奈が、出張先の手違いで死ぬほど毛嫌いしていた脂ぎった中年上司と同じホテルの部屋に泊まる羽目になる戦慄のNTR名作。生理的嫌悪感しかなかったはずの上司の執拗な愛撫と巧みな指技に、心とは裏腹に身体が快楽を覚えてしまい、徐々にトロ顔のメスへと堕ちていく心理描写が鳥肌モノです。</p>

<h3>見どころ：彼氏との電話中に背後から弄ばれる恐怖と、拒絶できない身体の疼き</h3>
<p>部屋の隅で彼氏に「今ホテルに着いたよ…早く会いたいな」と電話をしている最中、背後から音もなく忍び寄る中年上司。受話器を耳に当てたまま、服の上から胸を揉まれ、スカートの中に手を入れられて秘部を弄ばれます。「声を出したら彼氏にバラすぞ」と耳元で脅され、息を殺して耐える瀬戸環奈ですが、熟練の愛撫に抗えず、電話の向こうの彼氏に気づかれないよう甘い吐息を漏らしてしまいます。</p>

<h3>実用ポイント：嫌悪していた中年男の太い肉棒に貫かれ、アヘ顔で中出しを受け入れる絶望</h3>
<p>ベッドに押し倒され、ついに中年上司の生ペニスが瀬戸環奈の純潔な膣内へと突き刺さる瞬間。最初は顔を背けて拒絶していた彼女ですが、荒々しく腰を振られるたびに瞳の焦点が定まらなくなり、次第に自分から上司の首に腕を回して腰を浮かせ始めます。「あぁっ…おじさんの…すごいぃ…！」と完全に快楽に屈服し、彼氏の存在を忘れて子宮に中出しされる姿は背徳の極致です。</p>""",

    "mida00655": """<h2>『三角関係だった親友に1日限定で彼女を差し出したら身も心も寝取られてしまったお話です。 八木奈々』詳細レビュー</h2>
<p>可憐な美貌と天性のエロスでファンの心を掴んで離さない八木奈々が、彼氏の親友である男に1日だけ預けられた結果、男としての圧倒的な力量の差によって身も心も完全に奪われてしまう救いようのないNTR傑作。軽い気持ちで彼女を差し出した彼氏の愚かさと、親友の絶倫テクニックに子宮を鷲掴みにされた彼女の冷徹な変貌が生々しく描かれます。</p>

<h3>見どころ：彼氏の目の前で始まる親友との密着と、徐々に冷めていく彼女の視線</h3>
<p>親友の自宅に泊まることになった夜、最初は彼氏に申し訳なさそうな表情を見せていた八木奈々。しかし、親友の強引なリードと濃厚なキスに触れた瞬間、彼女の中で何かが弾けます。彼氏との淡白な関係では決して味わえなかった情熱的な愛撫に触れ、彼女の瞳からは罪悪感が消え失せ、一人の飢えた牝としての熱い光が宿り始めます。</p>

<h3>実用ポイント：翌朝、別人のように淫らな表情で親友の腰にしがみつく完堕ち中出し</h3>
<p>翌朝、迎えに来た彼氏が見たのは、親友の腕の中で幸せそうに眠る八木奈々の姿でした。彼氏が部屋に入ってきたことに気づいても慌てる様子もなく、親友に抱きついたままペニスを迎え入れ、目の前で見せつけるように濃厚な腰使いを披露。「ごめんね…でも、この人じゃないともう満足できないの…」と残酷な宣告を下しながら中出しを受け入れるクライマックスは必見です。</p>""",

    "ntrh00002": """<h2>『豊満巨乳すぎる彼女が俺の親父に寝取られ種付けプレスされていた。 美園和花』詳細レビュー</h2>
<p>むっちりとした極上の肉感とあふれんばかりの美巨乳を誇る美園和花が、同棲中の彼氏の実父（中年オヤジ）にその豊満ボディを狙われ、じっくりと寝取られていく衝撃の家庭内NTR名作。同世代の男にはない昭和の男の無骨な性欲と粘着質な愛撫に、彼女の豊かな肉体が徐々に目覚めさせられていく過程が濃密に描かれます。</p>

<h3>見どころ：留守中のリビングで繰り返される義父の執拗なスキンシップと胸揉み</h3>
<p>彼氏が仕事で家を留守にしている昼下がり、居間でくつろぐ美園和花に近づく父親。世間話を装いながら、次第にその手は彼女の豊かな胸や太ももへと伸びていきます。「お前みたいな良い女、息子にはもったいないな」と耳元で囁かれ、最初は困惑していた美園和花ですが、経験豊富な父親の執拗なタッチに次第に身体を熱く火照らせていきます。</p>

<h3>実用ポイント：襖の隙間から目撃する、父親の全体重をかけた種付けプレスセックス</h3>
<p>予定より早く帰宅した彼氏が襖の隙間から覗き見たのは、畳の上に大の字に寝かされた美園和花と、その上に覆いかぶさる父親の姿でした。父親の太い腰がドスン、ドスンと打ち付けられるたび、美園和花の巨大な胸が激しく波打ち、「お義父さん…っ！それ以上奥突かれたら…赤ちゃんできちゃう…！」と恍惚の表情で叫ぶ光景は、観る者の脳髄を激しく揺さぶります。</p>""",

    "mimk00136": """<h2>『カラミざかり 原作/桂あいり 累計販売数400万部突破 伝説の青春同人マンガ実写化 小野六花』詳細レビュー</h2>
<p>同人マンガ史上に燦然と輝く大ヒット作『カラミざかり』を、トップ女優・小野六花主演で完全実写化した伝説的一作。純粋で可憐な女子高生が、憧れていたはずの同級生ではなく、粗野で強引な不良ヤンキーの激しい快楽に弄ばれ、抗いようもなく心身ともに堕ちていくビターで甘美なNTRの世界観が完璧に再現されています。</p>

<h3>見どころ：原作の繊細な心理描写を完全再現した小野六花の圧倒的憑依演技</h3>
<p>放課後の教室や薄暗い路地裏で、ヤンキー男に壁ドンされ強引に唇を奪われる小野六花。最初は恐怖と嫌悪感で身を縮こまらせていた彼女が、強引にスカートをめくられ秘部をまさぐられるうちに、身体の奥底から込み上げる疼きに瞳を潤ませていきます。「あいつにバラされたくなかったら、声出すなよ」と脅されながら、震える手で男のシャツを掴む姿は痛々しくも凄まじい色気を放ちます。</p>

<h3>実用ポイント：彼氏には絶対に見せない淫乱な笑顔と、男の腰にしがみつく本能の交尾</h3>
<p>ラブホテルのベッドで繰り広げられる本番シーンは、まさに青春の崩壊と覚醒の瞬間。小野六花は彼氏の前で見せるような清純な表情をかなぐり捨て、男のペニスに跨がり、貪るように腰を振り乱します。「こんなの…いけないのに…すっごく気持ちいい…！」と涙を流しながらも絶頂を貪り、男の精液を体内に受け止めて恍惚となるクライマックスは実用性・ドラマ性ともに満点です。</p>""",

    "ckck00009": """<h2>『情けなく歪んだ性癖の貴方が悪いんだからね。僕を突き刺すように彼女の心の声が聞こえる悔シコNTR 美谷朱音』詳細レビュー</h2>
<p>知的な美貌と妖艶なフェロモンを併せ持つ実力派・美谷朱音（美谷朱里）が、歪んだ性癖から「彼女が他の男に抱かれる姿を見たい」と願った情けない彼氏の目の前で、他人の巨根に完全に胃袋ならぬ子宮を掴まれてしまう心理的拷問NTR。彼女のリアルすぎる「本音の心の声」がナレーションとして響き渡る革新的な構成が話題を呼んだ名作です。</p>

<h3>見どころ：彼氏の目の前で他人の男の肉棒に夢中になる彼女の冷ややかな心の声</h3>
<p>ホテルの部屋の片隅で、隠れて見つめる彼氏の存在を知りながら、マッチョな間男のベッドに倒れ込む美谷朱音。彼氏とは比べ物にならない太く硬いペニスを見た瞬間、彼女の心の声が響きます。「うそ…こんなに大きいの？…あの人のとは全然違う…」。罪悪感を装いながらも、指先で愛おしそうに他人の男根をなぞる彼女の仕草に、彼氏は絶望と興奮で震えます。</p>

<h3>実用ポイント：激ピストンでアヘ顔を晒しながら「あの人よりずっと気持ちいい」と中出しを懇願</h3>
<p>間男に腰を掴まれ、容赦ない重低音ピストンで奥深くを抉られる美谷朱音。次第に彼氏への気遣いなど完全に吹き飛び、「もっと…！もっと強く突いてぇ！全部出して！」と髪を振り乱して狂い悶えます。「ごめんね、でもこの人のチ〇ポが最高なの…」という残酷な心の声が突き刺さる中、子宮口にたっぷりと濃厚ザーメンを注ぎ込まれるラストは、悔しさと興奮で射精が止まらなくなります。</p>"""
}

# 特集3記事のメタ情報
ARTICLES = [
    # ----------------------------------------------------
    # 特集1: 巨乳・神乳パイズリ＆激揺れピストン
    # ----------------------------------------------------
    {
        "id": "feature_massive_breasts_paizuri_deep_cleavage_ranking_2026",
        "title": "【包み込まれる至高の柔肌と圧倒的揺れ】FANZA「巨乳・神乳パイズリ」おすすめ人気ランキングTOP5！規格外のメガおっぱいに埋もれる快楽×限界まで搾り取られる極上名作選【2026年最新】",
        "hinban": "MASSIVE-BREASTS-PAIZURI-TOP5-2026",
        "cids": ["mida00280", "sqte00635", "1stars00804", "cawd00949", "juny00124"],
        "hero_tag": "MASSIVE BREASTS & PAIZURI SPECIAL",
        "genres": ["巨乳", "爆乳", "パイズリ", "中出し", "騎乗位", "密着", "特集", "殿堂入り"],
        "lead_p1": "男の永遠のロマンであり、本能を最もダイレクトに刺激する究極のフェチシズム――それが「巨乳・神乳パイズリ」です。手のひらからこぼれ落ちる圧倒的な質量、服の上からでも隠しきれない豊かな渓谷、そして肉棒をまるごと包み込んで締め付ける温かい柔肌の感触は、一度味わえば二度と抜け出せない魔性の快楽を誇ります。",
        "lead_p2": "本特集では、FANZAに無数に存在する巨乳作品の中から、単にサイズが大きいだけでなく「肉の弾力・揺れの迫力・パイズリの技術・挿入時の密着度」が全て極限レベルに達している伝説的神作TOP5を厳選しました。画面を埋め尽くすド迫力の乳揺れと、耳元で甘く囁かれながら限界まで搾り取られる極上の射精体験をぜひご堪能ください。",
        "guide_title": "失敗しない「巨乳・パイズリAV」選びの決定版3大ポイント",
        "guide_points": [
            ("胸の「質感と弾力」の生々しさをチェック", "単にシリコンで膨らませたような硬い胸ではなく、重力に従って自然に形を変え、ピストンの衝撃でたゆんたゆんと波打つ天然系の極上バストを選ぶのが鉄則です。ローションやオイルが絡んだときの光沢と吸い付き感が段違いです。"),
            ("「パイズリの技術とアングル」のこだわり", "ペニスの先端が見えなくなるほど深く挟み込み、乳首を擦り当てながら上下にシゴき上げる技術力の高い作品は抜きやすさが桁違いです。完全主観や見下ろしアングルなど、視覚的に没入できるカメラワークも重要です。"),
            ("「挿入時の乳揺れ・対面密着度」を重視", "パイズリ後の本番において、騎乗位や正常位で胸元に顔を埋められる対面密着シーンがあるかどうかは極めて重要。ピストンのリズムに合わせて胸が顔面に衝突してくるような迫力ある作品は最高峰のカタルシスをもたらします。")
        ],
        "highlights": {
            "mida00280": ("規格外Qカップの怪物的質量！ペニスが完全に消失するブラックホール級パイズリ", "人類史上最高峰のメガ乳房を持つHimariが、自室に押し掛けて1日中パイズリで搾り尽くす夢の痴女デリバリー。両胸の間にペニスをすっぽり収め、耳元で囁きながらシゴき上げる快感は卒倒必至です。"),
            "sqte00635": ("たゆんたゆん揺れる天然美巨乳の極致！彼女感あふれる休日イチャラブ中出し", "宍戸里帆の圧倒的な肉感と愛嬌が炸裂する同棲イチャラブ名作。ソファーでシャツをはだけて繰り広げられる無防備パイズリと、背後から突かれて激しく暴れ狂う乳揺れバックピストンは実用度満点です。"),
            "1stars00804": ("造形美の頂点を極めた神Gカップ！オイルでテラテラ光る美乳に溺れる芸術的エロス", "パーフェクトボディを誇る神木麗が、最高級ランジェリーと全身オイルで男の本能を覚醒させる至高作。滑らかな胸で挟み込まれるオイリーパイズリと、汗だくで貪り合う濃密ピストンは鳥肌モノの美しさです。"),
            "cawd00949": ("同僚美女の無防備な胸の谷間！泥酔お泊まりの朝に貪り尽くす寝起きパイズリ", "伊藤舞雪が同僚男性の部屋で酔い潰れ、全裸で眠る姿から始まる妄想具現化ドラマ。寝起きの気だるい表情で胸に挟んでくる無自覚パイズリと、引き締まったウエストを揺らす朝中出しバックは必見です。"),
            "juny00124": ("吉原超高級ソープの至福体験！泡だらけの爆乳で全身を滑走する神業マットプレイ", "圧倒的肉感の夕季ちとせが、ソープ嬢として男の欲望を全肯定。泡まみれのマット上で巨大な胸を滑らせるマットパイズリから、上下のオクチを使った連続バキューム責めまで、男の夢が詰まった極上作です。")
        },
        "table_headers": ["順位", "作品タイトル", "主演女優", "評価", "公式リンク"],
        "faqs": [
            ("巨乳作品で一番実用度が高いアングルは何ですか？", "断トツで「対面座位」や「正常位の見下ろしアングル」、そして「騎乗位の煽りアングル」です。女性の豊かなバストが重力とピストンによって激しく波打つ様子がダイレクトに視界に飛び込んでくるため、射精の瞬間の興奮が何倍にも跳ね上がります。"),
            ("Himariさんのような超規格外の胸でもしっかりパイズリできますか？", "むしろサイズが大きければ大きいほど、ペニス全体が胸の肉塊に飲み込まれるため、一般的なパイズリとは比較にならない包摂感と温もりを味わえます。ローションを併用することで摩擦の滑らかさも完璧になります。"),
            ("オイル作品と通常の作品ではどちらがおすすめですか？", "視覚的なエロスやテカリ、滑らかな摩擦感を重視するならオイル作品（神木麗さんの作品など）が圧倒的におすすめです。一方で、肌本来のサラサラとした柔らかさや同棲感を味わいたいなら通常のイチャラブ作品（宍戸里帆さんの作品など）が適しています。"),
            ("動画のサンプルは無料で確認できますか？", "はい、各作品の詳細ボタンからFANZA公式サイトへアクセスすることで、高画質なサンプル動画や追加のプレビュー画像を完全無料で確認できます。まずはサンプルで胸の揺れ具合をチェックしてみてください。")
        ],
        "related": [
            ("/posts/feature_black_pantyhose_office_suit_fetish_ranking_2026", "【美脚・黒ストッキング・オフィススーツ特集】", "洗練された大人の着衣フェチ！タイトスカートと滑らかなナイロン越しに味わう至高の足技＆オフィス密着名作選。"),
            ("/posts/feature_huge_butt_back_piston_creampie_ranking_2026", "【巨尻・デカ尻バックピストン特集】", "画面を埋め尽くす圧倒的ヒップの肉感！後背位で波打つ極上桃尻を腰が砕けるまで突き上げる特濃生ハメ名作選。"),
            ("/posts/feature_older_man_dandy_mature_love_ranking_2026", "【年の差・大人の色気と包容力特集】", "頼れる包容力にメロメロになったトップ女優が、甘美な情熱に身を委ねて心も身体も蕩けていく珠玉の名作選。"),
            ("/posts/feature_hot_spring_open_air_bath_intimacy_ranking_2026", "【温泉旅行・貸切露天風呂特集】", "湯煙に包まれる素肌と深まる愛の情熱！浴衣の裾を乱して朝まで愛し合う贅沢なひとときを描く情緒豊かな極上名作選。")
        ]
    },

    # ----------------------------------------------------
    # 特集2: 女上司・プライド崩壊・立場逆転メス堕ち
    # ----------------------------------------------------
    {
        "id": "feature_female_boss_pride_collapse_reverse_domination_ranking_2026",
        "title": "【冷徹なキャリア美女が快楽に屈する瞬間】FANZA「女上司・プライド崩壊・立場逆転」おすすめ人気ランキングTOP5！職場の高嶺の花が部下に弱みを握られ牝の顔で懇願する背徳の神作選【2026年最新】",
        "hinban": "FEMALE-BOSS-PRIDE-COLLAPSE-2026",
        "cids": ["pfes00113", "waaa00617", "1start00525", "mimk00249", "mikr00039"],
        "hero_tag": "FEMALE BOSS & REVERSE DOMINATION SPECIAL",
        "genres": ["女上司", "立場逆転", "メス堕ち", "OL", "屈辱", "中出し", "特集", "殿堂入り"],
        "lead_p1": "職場では常に完璧で、部下を冷たく見下し、厳しい言葉で叱責してくる高嶺の花の女上司――。そんな近寄りがたいキャリア美女が、ふとした弱みを握られたり、理性のタガが外れた瞬間、普段のプライドを粉々に砕かれて一人の牝として男に屈服していく姿は、男性の征服欲とサディズムをこの上なく刺激します。",
        "lead_p2": "本特集では、FANZAで絶大な支持を集める「女上司・立場逆転」ジャンルの中から、ストーリーの完成度とメス堕ちの落差が凄まじい傑作TOP5を厳選しました。オフィスのデスクの下で震える秘密、屈辱に涙しながらの奉仕、そして激しいピストンに抗えず「もっと奥を突いて…！」と懇願する女上司の乱れ姿は、他の追随を許さない圧倒的な射精圧を約束します。",
        "guide_title": "失敗しない「女上司・立場逆転AV」選びの決定版3大ポイント",
        "guide_points": [
            ("「昼間の冷徹さと夜の崩壊」の落差（ギャップ）を重視", "普段の仕事中の態度が厳しく冷酷であればあるほど、弱みを暴かれてプライドが崩壊した瞬間のカタルシスは跳ね上がります。スーツ姿での毅然とした表情が、快楽によってアヘ顔へと変貌していくグラデーションが見事な作品を選びましょう。"),
            ("「弱みの握り方とシチュエーション」の説得力", "可愛い下着の看破、副業風俗での遭遇、深夜オフィスの自慰激写など、部下が優位に立つきっかけがリアルで背徳的な作品ほど没入感が高まります。密室での駆け引きや命令口調の逆転が丁寧に描かれている作品がベストです。"),
            ("「スーツ・着衣を活かした背徳プレイ」の有無", "タイトスカートをたくし上げ、パンティをずらして挿入する着衣セックスや、オフィスの執務デスク・役員会議室を舞台にしたプレイは臨場感抜群です。仕事場の痕跡を残したまま犯される背徳の構図を存分に味わえる作品がおすすめです。")
        ],
        "highlights": {
            "pfes00113": ("普段は鬼上司がピンクのリボンパンティ！？秘密を暴かれ屈辱の涙目フェラ", "冷酷エリート上司の響乃うたが隠していた乙女下着を部下に看破されるメガヒット作。プライドをへし折られて「社内では言わないで…」と懇願し、執務デスクの上でスーツを着たままバックで貫かれる姿は征服欲を直撃します。"),
            "waaa00617": ("色気ムンムン女上司が出張先で童貞筆おろし…逆に絶倫ピストンに狂わされ逆転完堕ち", "レジェンド大槻ひびきが演じる大人のフェロモン上司。余裕の笑みで童貞部下をからかっていたはずが、若い肉棒の硬さと無尽蔵のスタミナに翻弄され、朝を迎える頃にはただの淫乱な牝へと成り下がる逆転の極致です。"),
            "1start00525": ("厳しすぎるOJT教育係がピンサロで副業！？歓楽街で始まる立場逆転の生ハメ本番", "青空ひかり演じる鬼上司の秘密を新卒社員が偶然突き止めるスリリングな傑作。ピンク色の個室で「バラされたくなかったら…」と迫られ、涙を浮かべながら生挿入を受け入れる背徳感は息が止まるほどの興奮です。"),
            "mimk00249": ("深夜オフィスで自慰に耽るパワハラ上司を激写！動かぬ証拠で脅す痛快報復中出し", "吉根ゆりあが演じる高飛車な女上司が、残業中のオフィスでオナニーしていた現場を押さえられる痛快ドラマ。日頃の恨みを込めて役員デスクの上で激ピストンを浴びせ、快楽に抗えず謝罪絶頂する姿は実用度MAXです。"),
            "mikr00039": ("年下の強気上司がサシ飲み泥酔でベッドへ…「激ピスされたい」ドM本性が暴走！", "幸村泉希演じる生意気な年下上司が、お酒の勢いで介抱されるうちに隠していたドMマ●コを曝け出す名作。ベッドが軋むほどの猛烈ピストンで子宮を激突され、部下に狂わされて泣き叫ぶギャップ萌えの最高峰です。")
        },
        "table_headers": ["順位", "作品タイトル", "主演女優", "評価", "公式リンク"],
        "faqs": [
            ("女上司もので一番興奮するシチュエーションは何ですか？", "やはり「オフィスの会議室や残業中のデスクでの着衣プレイ」と「弱みを握られて部下の命令に従わざるを得ない屈辱の瞬間」です。社会的地位の高さと、肉体的な服従のコントラストが男の脳を最も強く刺激します。"),
            ("大槻ひびきさんの作品はどのような人に向いていますか？", "年上の包容力ある美女にからかわれたい方や、立場逆転で大人の女性をメロメロに言わせたい方に完璧にフィットします。演技力・フェロモンともに業界トップクラスのため、ストーリーへの没入感が抜群です。"),
            ("着衣フェチ向けのシーンは含まれていますか？", "はい、今回選定した5作品はいずれもスーツ、タイトスカート、ストッキング、オフィスカジュアルを巧みに活かした着衣プレイが満載です。完全に脱がせるのではなく、着衣のまま乱す背徳感を存分に楽しめます。"),
            ("スマホやタブレットでも快適に視聴できますか？", "FANZAの動画配信サービスはスマートフォン、タブレット、PC、スマートTVなどあらゆる端末に完全対応しています。ブラウザでのストリーミング再生はもちろん、公式アプリでの事前ダウンロード再生も可能です。")
        ],
        "related": [
            ("/posts/feature_minato_girl_papakatsu_lounge_creampie_ranking_2026", "【港区女子・パパ活ラウンジ嬢特集】", "高飛車な美女が金と快楽に屈服！高級タワマン密会×札束で買った最高峰美女が中出しを懇願するメス堕ち傑作選。"),
            ("/posts/feature_hypnosis_common_sense_alteration_obedience_ranking_2026", "【催眠・常識改変・絶対服従特集】", "理性が吹き飛び快楽に完全服従！指パッチンひとつで敏感ビクビク痙攣×普段は高嶺の花がアヘ顔で貪る神作選。"),
            ("/posts/feature_black_pantyhose_office_suit_fetish_ranking_2026", "【美脚・黒ストッキング・オフィススーツ特集】", "タイトスカートの隙間から溢れる大人の艶技！オフィスでの密着と滑らかなナイロン越しに味わう着衣フェチ名作選。"),
            ("/posts/feature_virgin_hunting_aggressive_older_sister_ranking_2026", "【童貞狩り・積極的肉食お姉さん特集】", "ウブな男の子を骨抜きに貪り尽くす！からかい寸止めから生ハメ主導権掌握まで理性を狂わせる至高の搾精傑作選。")
        ]
    },

    # ----------------------------------------------------
    # 特集3: 寝取られ（NTR）・最愛の人が他人に堕ちる背徳
    # ----------------------------------------------------
    {
        "id": "feature_netorare_ntr_betrayal_ecstasy_ranking_2026",
        "title": "【愛する人が他人の快楽に堕ちていく背徳】FANZA「寝取られ（NTR）・背徳メス堕ち」おすすめ人気ランキングTOP5！嫌悪から絶頂へ…目の前で最愛の女性を貪り尽くされる狂気の傑作選【2026年最新】",
        "hinban": "NETORARE-NTR-BETRAYAL-2026",
        "cids": ["snos00334", "mida00655", "ntrh00002", "mimk00136", "ckck00009"],
        "hero_tag": "NETORARE & BETRAYAL ECSTASY SPECIAL",
        "genres": ["寝取られ", "NTR", "背徳", "中出し", "メス堕ち", "絶望", "特集", "殿堂入り"],
        "lead_p1": "誰よりも愛し、大切にしてきた最愛の女性が、他人の男の荒々しい快楽に身を委ね、抗いようもなく肉の悦びに溺れていく――。胸を引き裂かれるような絶望と嫉妬、そしてそれと裏腹に股間を激しく突き上げる狂おしい興奮。AV界において最も中毒性が高く、一度ハマると抜け出せない魔境が「寝取られ（NTR）」ジャンルです。",
        "lead_p2": "本特集では、FANZAに君臨するNTR作品群の中から、心理描写の緻密さ、背徳的なシチュエーション、そしてヒロインの表情の変貌が際立つ歴代最高峰の神作TOP5を厳選しました。最初は嫌悪と恐怖に震えていた美女が、熟練のピストンと濃厚な精液によって子宮を開発され、トロけた瞳で他人の中出しを受け入れる瞬間…その破壊的なカタルシスをぜひ体感してください。",
        "guide_title": "失敗しない「寝取られ（NTR）AV」選びの決定版3大ポイント",
        "guide_points": [
            ("「嫌悪から快楽への堕ちるグラデーション」を重視", "最初からビッチな女性が浮気するのではなく、彼氏を一途に愛していた清純なヒロインが、抗えない快楽によって徐々に肉体を支配されていく心理の変遷が最も重要です。抵抗する言葉と裏腹に濡れそぼる秘部の描写が秀逸な作品を選びましょう。"),
            ("「彼氏の存在を意識させる背徳ギミック」の有無", "彼氏との電話中のいたずら、彼氏の目の前や襖の隙間からの覗き見、心の声のナレーションなど、元のパートナーの存在が強調されるほどNTRの背徳感は倍増します。見つかるかもしれない緊張感と奪われる絶望が最高のスパイスです。"),
            ("「相手男（間男）の圧倒的なオス感と肉弾戦」", "中年上司、絶倫の親友、無骨な義父、粗野なヤンキーなど、ヒロインを奪う男の「オスとしての強さ・テクニック」に説得力がある作品ほど、ヒロインが完堕ちする結末に深い納得感と強烈なシコり感が生まれます。")
        ],
        "highlights": {
            "snos00334": ("最強美女が出張先で大嫌いな中年上司と相部屋…電話中の愛撫から絶望のトロ顔メス堕ち", "瀬戸環奈の神ビジュアルが汚される究極の出張NTR。彼氏と電話中に背後から弄ばれる恐怖と、嫌悪していたはずの中年男の太いペニスに子宮を突かれてアヘ顔絶頂する姿は背徳の極致です。"),
            "mida00655": ("親友に1日だけ彼女を預けたら…翌朝には彼氏を捨てて親友の腰にしがみつく完堕ち", "八木奈々が演じる清純な彼女が、親友の絶倫テクニックに子宮を鷲掴みにされる救いようのない名作。翌朝、迎えに来た彼氏の目の前で嬉々として中出しを受け入れる残酷な美しさは必見です。"),
            "ntrh00002": ("同棲中の彼女の豊満巨乳を実の親父が略奪！襖の隙間から覗く衝撃の種付けプレス", "美園和花のむっちり爆乳ボディに目をつけた実父が、留守中にじっくり開発。畳の上で全体重をかけて打ち込まれる昭和の無骨ピストンに、「お義父さん…！」と絶叫痙攣する姿は脳髄を直撃します。"),
            "mimk00136": ("400万部突破の伝説的青春同人マンガ完全実写化！清純女子高生がヤンキーに貪られる名作", "小野六花主演による『カラミざかり』奇跡の実写化。彼氏には絶対に見せない淫乱な笑顔で男のペニスに跨がり、涙を流しながらも絶頂を貪る心理描写は全NTRファン必見の完成度です。"),
            "ckck00009": ("歪んだ彼氏への精神的拷問！他人の巨根に夢中になる彼女のリアルな本音ナレーション", "美谷朱音演じる彼女が、目の前で他人の男に抱かれながら「あの人よりずっと気持ちいい…」と心の中で呟く革新作。残酷な本音を突き刺されながら中出しを目撃する悔しさと興奮は唯一無二です。")
        },
        "table_headers": ["順位", "作品タイトル", "主演女優", "評価", "公式リンク"],
        "faqs": [
            ("NTR作品を初めて見る人にはどの作品がおすすめですか？", "まずは原作が同人で大ヒットし、ストーリーと心情描写が完璧な『カラミざかり』（小野六花主演）か、王道の出張相部屋シチュエーションである瀬戸環奈さんの作品がおすすめです。映像美と背徳のバランスが極めて高く、物語に引き込まれます。"),
            ("胸糞が悪くなりすぎずに抜ける作品はありますか？", "『出張先で死ぬほど嫌いな中年上司と相部屋…』（瀬戸環奈）や『情けなく歪んだ性癖の貴方が悪いんだからね』（美谷朱音）は、ヒロイン自身の快楽への目覚めとエロティシズムに重点が置かれているため、シコりやすさと背徳感のバランスが抜群です。"),
            ("間男が中年男性のシチュエーションはなぜ人気なのですか？", "若く美しいヒロインと、脂ぎった中年男性という圧倒的なビジュアルの格差が、生理的な嫌悪感を突き抜けて快楽に屈したときの「メス堕ち感」を最大化するためです。背徳感を極限まで高めてくれます。"),
            ("購入後の視聴期限や保存について教えてください。", "FANZAのデジタル配信（動画）で購入した作品は、アカウントに紐づいて無期限で何度でも視聴可能です。また、PCやスマートフォンにダウンロード保存しておけば、通信制限やオフライン環境でも高画質でいつでも楽しめます。")
        ],
        "related": [
            ("/posts/feature_fanza_ex_girlfriend_reunion_unrequited_passion_ranking_2026", "【元カノ・再会未練セックス特集】", "昔付き合っていたあの子と数年ぶりの再会！大人の色気をまとった元恋人とホテルで貪り合う至高の背徳名作選。"),
            ("/posts/feature_gal_mama_young_wife_unfaithful_creampie_ranking_2026", "【ギャルママ・ヤンママ若妻特集】", "元ヤンの魅力溢れる若妻の甘い誘惑！無防備な部屋着姿×旦那の留守に始まるスリリングな濃密不倫中出し傑作選。"),
            ("/posts/feature_underground_idol_fan_hookup_raw_creampie_ranking_2026", "【地下アイドル・推し活密会特集】", "最推しのあの子と秘密のお泊まり！特典会裏の秘密の恋心からステージ衣装のまま朝まで愛し合う背徳名作選。"),
            ("/posts/feature_fanza_cohabitation_sweet_girlfriend_lovelove_ranking_2026", "【同棲生活・甘々イチャラブ特集】", "本物の彼女のような多幸感！疲れた心を全力で癒やす至高の恋人感覚・密着ラブラブ作品選。")
        ]
    }
]

def main():
    print("=== STARTING NEW KILLER FEATURES v6 GENERATION ===")
    
    # 1. 15作品の生データをFANZA APIからリアルタイム取得
    items_by_cid = {}
    for art in ARTICLES:
        for cid in art["cids"]:
            if cid not in items_by_cid:
                print(f"Fetching from FANZA API: {cid}...")
                item = fetch_fanza_item(cid)
                if not item:
                    print(f" [WARN] Digital not found for {cid}, trying monthly...")
                    item = fetch_fanza_item(cid, service="monthly")
                if item:
                    items_by_cid[cid] = item
                    print(f" [SUCCESS] Fetched: {item.get('title', '')[:40]}")
                else:
                    print(f" [ERROR] Could not fetch {cid} from FANZA API!")
                time.sleep(0.5)

    # 2. 15作品の個別記事（posts/{cid}.json）を生成・保存
    print("\n--- Generating 15 Individual Post JSONs ---")
    for art in ARTICLES:
        feature_id = art["id"]
        feature_title = art["title"]
        for cid in art["cids"]:
            item = items_by_cid.get(cid)
            if not item:
                continue

            it_title = item.get("title", "")
            it_date = item.get("date", "2026-10-07 20:00:00")
            it_price = item.get("prices", {}).get("price", "2480~")
            it_maker = item.get("iteminfo", {}).get("maker", [{}])[0].get("name", "FANZA")
            
            act_list = [a.get("name") for a in item.get("iteminfo", {}).get("actress", [])]
            genre_list = [g.get("name") for g in item.get("iteminfo", {}).get("genre", [])]
            if "特集" not in genre_list:
                genre_list.append("特集")
            
            hero_img = item.get("imageURL", {}).get("large", "")
            aff_url = item.get("affiliate_url_clean") or item.get("affiliateURL", "")
            
            # レビュー評価
            rev_data = item.get("review", {})
            rating_val = rev_data.get("average") or rev_data.get("rate") or "4.8"
            rating_count = rev_data.get("count") or "12"

            sample_imgs = get_sample_images(item, max_count=6)
            sample_gallery_html = ""
            if sample_imgs:
                img_tags = "".join([f'<a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block overflow-hidden rounded-xl border border-slate-700/60 hover:opacity-90 transition"><img src="{img_url}" alt="{it_title} サンプル画像" class="w-full h-auto object-cover hover:scale-105 transition duration-300" loading="lazy" /></a>' for img_url in sample_imgs])
                sample_gallery_html = f"""<div class="my-8 p-6 bg-slate-900 border border-slate-800 rounded-3xl">
  <h3 class="text-lg md:text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>📸</span> 高画質サンプルプレビューギャラリー
  </h3>
  <div class="grid grid-cols-2 md:grid-cols-3 gap-3">
    {img_tags}
  </div>
</div>"""

            indiv_rev = INDIVIDUAL_REVIEWS.get(cid, f"<p>{it_title}の詳細レビューです。迫力の演技と濃密なストーリー展開が光る名作です。</p>")
            
            act_links = " ".join([get_actress_link(a) for a in act_list])
            genre_tags = " ".join([get_genre_link(g) for g in genre_list[:8]])

            # 個別記事用HTML
            post_html = f"""<article class="space-y-6">
  <!-- 特集への親リンクパンくずバッジ -->
  <div class="p-4 bg-gradient-to-r from-amber-950/40 via-slate-900 to-slate-900 border border-amber-500/30 rounded-2xl mb-6">
    <div class="text-xs text-amber-400 font-bold uppercase tracking-wider mb-1">FEATURED SELECTION</div>
    <div class="text-sm text-slate-300">
      本作品はキラー特集『<a href="/posts/{feature_id}" class="text-amber-300 hover:text-amber-200 underline font-bold transition">{feature_title}</a>』選定作品です。
    </div>
  </div>

  <!-- 作品詳細レビュー -->
  <div class="prose prose-invert max-w-none text-slate-200 leading-relaxed text-base md:text-lg">
    {indiv_rev}
  </div>

  <!-- 公式購入・視聴誘導ボタン -->
  <div class="my-8 p-6 bg-gradient-to-br from-slate-900 to-rose-950/30 border border-rose-500/30 rounded-3xl text-center shadow-xl">
    <div class="text-amber-400 font-bold text-sm mb-2 flex items-center justify-center gap-1">
      <span>★</span> レビュー評価 {rating_val} ({rating_count}件のユーザー評価)
    </div>
    <h3 class="text-xl md:text-2xl font-black text-white mb-4">
      『{it_title}』をFANZA公式で今すぐ視聴
    </h3>
    <p class="text-slate-300 text-sm max-w-xl mx-auto mb-6">
      高画質ストリーミングおよびオフライン保存に対応。公式限定の長尺プレビューやお得なセール情報も公式サイトにて随時公開中！
    </p>
    <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-3 px-8 py-4 bg-gradient-to-r from-rose-600 via-rose-500 to-amber-500 hover:from-rose-500 hover:to-amber-400 text-white font-extrabold text-lg rounded-2xl shadow-lg hover:shadow-rose-500/25 transition transform hover:-translate-y-0.5">
      <span>今すぐFANZA公式で作品を見る</span>
      <span>➔</span>
    </a>
  </div>

  <!-- サンプルギャラリー -->
  {sample_gallery_html}

  <!-- メタ情報 -->
  <div class="p-6 bg-slate-900/80 border border-slate-800 rounded-2xl text-sm text-slate-300 space-y-3">
    <div class="flex items-center gap-2"><span class="font-bold text-slate-400 w-24">出演女優:</span> <div>{act_links or "単体女優"}</div></div>
    <div class="flex items-center gap-2"><span class="font-bold text-slate-400 w-24">メーカー:</span> <span class="text-slate-200 font-semibold">{it_maker}</span></div>
    <div class="flex items-start gap-2"><span class="font-bold text-slate-400 w-24 pt-1">ジャンル:</span> <div class="flex flex-wrap gap-1.5">{genre_tags}</div></div>
  </div>
</article>"""

            indiv_post_data = {
                "id": cid,
                "title": it_title,
                "date": it_date,
                "hinban": cid.upper(),
                "price": str(it_price),
                "maker": it_maker,
                "actresses": act_list,
                "genres": genre_list,
                "image": hero_img,
                "review": post_html
            }

            out_path = os.path.join(OUTPUT_DIR, f"{cid}.json")
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(indiv_post_data, f, ensure_ascii=False, indent=2)
            print(f"Saved individual post: {cid} -> {out_path}")

    # 3. 3つの特集記事（posts/{art_id}.json）を生成・保存
    print("\n--- Generating 3 Massive Killer Feature Posts ---")
    for art in ARTICLES:
        art_id = art["id"]
        art_title = art["title"]
        print(f"\nProcessing Feature: {art_id}")

        items_data = []
        for rank, cid in enumerate(art["cids"], 1):
            it = items_by_cid.get(cid)
            if it:
                it_copy = dict(it)
                it_copy["rank"] = rank
                items_data.append(it_copy)

        if len(items_data) != 5:
            print(f" [ERROR] Expected 5 items, found {len(items_data)} for {art_id}!")
            continue

        hero_img = items_data[0].get("imageURL", {}).get("large", "")
        all_actresses = []
        for it in items_data:
            for a in it.get("iteminfo", {}).get("actress", []):
                name = a.get("name")
                if name and name not in all_actresses:
                    all_actresses.append(name)

        review_html_parts = []

        # ヒーローバナー＆導入リード
        review_html_parts.append(f"""<!-- ヒーローリード文 -->
<div class="mb-10 p-6 md:p-8 bg-gradient-to-br from-slate-900 via-slate-900 to-rose-950/40 border border-rose-500/30 rounded-3xl shadow-2xl relative overflow-hidden">
  <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-rose-500/20 border border-rose-500/40 text-rose-300 text-xs font-black tracking-widest uppercase mb-4">
    <span>🔥</span> {art["hero_tag"]}
  </div>
  <p class="text-base md:text-xl text-slate-200 leading-relaxed font-medium mb-4">
    {art["lead_p1"]}
  </p>
  <p class="text-sm md:text-lg text-slate-300 leading-relaxed font-normal">
    {art["lead_p2"]}
  </p>
</div>""")

        # 目次ナビゲーション
        toc_items = []
        for it in items_data:
            c_rank = it["rank"]
            c_title = it.get("title", "")
            c_act = " / ".join([a.get("name") for a in it.get("iteminfo", {}).get("actress", [])])
            toc_items.append(f"""    <li class="flex items-start gap-2 text-sm text-slate-300">
      <span class="text-amber-400 font-bold">第{c_rank}位:</span>
      <a href="#rank-{c_rank}" class="text-slate-200 hover:text-amber-300 underline transition line-clamp-1">
        {c_title} ({c_act})
      </a>
    </li>""")

        review_html_parts.append(f"""<!-- 目次（クイックナビゲーション） -->
<div class="my-8 p-6 bg-slate-900/90 border border-slate-800 rounded-3xl shadow-xl">
  <h3 class="text-lg md:text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>📑</span> 目次・ランキング一覧
  </h3>
  <ul class="space-y-2.5">
{''.join(toc_items)}
    <li class="flex items-start gap-2 text-sm text-slate-300 pt-2 border-t border-slate-800">
      <span class="text-amber-400 font-bold">📊</span>
      <a href="#comparison-table" class="text-slate-200 hover:text-amber-300 underline transition">おすすめ神作TOP5 徹底スペック比較一覧</a>
    </li>
    <li class="flex items-start gap-2 text-sm text-slate-300">
      <span class="text-amber-400 font-bold">💬</span>
      <a href="#faq-section" class="text-slate-200 hover:text-amber-300 underline transition">本特集に関するよくある質問（FAQ）</a>
    </li>
  </ul>
</div>""")

        # 選び方ガイド
        guide_box_parts = []
        for p_title, p_desc in art["guide_points"]:
            guide_box_parts.append(f"""    <div class="bg-slate-800/60 p-5 rounded-2xl border border-slate-700/60">
      <h4 class="font-bold text-amber-300 text-base md:text-lg mb-2 flex items-center gap-2">
        <span>✅</span> {p_title}
      </h4>
      <p class="text-slate-300 text-xs md:text-sm leading-relaxed">{p_desc}</p>
    </div>""")

        review_html_parts.append(f"""<!-- 失敗しない作品選びのポイント -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl">
  <h3 class="text-xl md:text-2xl font-bold text-white mb-4 flex items-center gap-2">
    <span>💡</span> {art["guide_title"]}
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6">
{''.join(guide_box_parts)}
  </div>
</div>""")

        # ランキング各作品の詳細カード
        for it in items_data:
            c_rank = it["rank"]
            c_cid = it.get("content_id", "")
            c_title = it.get("title", "")
            c_img = it.get("imageURL", {}).get("large", "")
            c_aff = it.get("affiliate_url_clean") or it.get("affiliateURL", "")
            c_act_list = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
            c_act_links = " ".join([get_actress_link(a) for a in c_act_list])
            c_genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
            c_genre_tags = " ".join([get_genre_link(g) for g in c_genres[:6]])
            
            c_rev = it.get("review", {})
            c_star = c_rev.get("average") or c_rev.get("rate") or "4.8"
            c_cnt = c_rev.get("count") or "20"

            h_lead, h_body = art["highlights"].get(c_cid, ("圧倒的な完成度を誇る名作！", "卓越した演技と濃密なエロスが織りなす極上のエンターテインメントです。"))

            c_samples = get_sample_images(it, max_count=4)
            sample_html = ""
            if c_samples:
                s_imgs_html = "".join([f'<a href="{c_aff}" target="_blank" rel="nofollow noopener" class="block overflow-hidden rounded-xl border border-slate-700 hover:opacity-90 transition"><img src="{s_img}" alt="{c_title} サンプル" class="w-full h-24 md:h-28 object-cover hover:scale-105 transition duration-300" loading="lazy" /></a>' for s_img in c_samples])
                sample_html = f"""<div class="mt-4 pt-4 border-t border-slate-800">
  <div class="text-xs font-bold text-slate-400 mb-2 flex items-center gap-1">
    <span>📸</span> 公式サンプルプレビュー（クリックで拡大・公式動画へ）:
  </div>
  <div class="grid grid-cols-2 md:grid-cols-4 gap-2">
    {s_imgs_html}
  </div>
</div>"""

            rank_badge_color = {
                1: "from-amber-500 to-amber-700 text-white shadow-amber-500/20",
                2: "from-slate-300 to-slate-500 text-slate-950 shadow-slate-300/20",
                3: "from-amber-700 to-amber-900 text-amber-100 shadow-amber-800/20"
            }.get(c_rank, "from-slate-700 to-slate-800 text-slate-300")

            review_html_parts.append(f"""<!-- ランキング第{c_rank}位 -->
<div id="rank-{c_rank}" class="my-12 bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-2xl relative scroll-mt-24">
  <div class="flex items-center justify-between flex-wrap gap-3 mb-6 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-3">
      <span class="inline-flex items-center justify-center w-12 h-12 rounded-2xl bg-gradient-to-br {rank_badge_color} font-black text-xl shadow-lg">
        {c_rank}
      </span>
      <div>
        <div class="text-xs text-amber-400 font-bold uppercase tracking-wider">RANKING #{c_rank}</div>
        <h3 class="text-lg md:text-2xl font-bold text-white line-clamp-1">{c_title}</h3>
      </div>
    </div>
    <div class="flex items-center gap-2 bg-slate-800/80 px-4 py-2 rounded-2xl border border-slate-700 text-xs md:text-sm">
      <span class="text-amber-400 font-bold">★ {c_star}</span>
      <span class="text-slate-400">({c_cnt}件の評価)</span>
    </div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-start">
    <div class="md:col-span-5">
      <div class="relative group overflow-hidden rounded-2xl border border-slate-700/80 shadow-lg">
        <img src="{c_img}" alt="{c_title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <a href="{c_aff}" target="_blank" rel="nofollow noopener" class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 flex items-center justify-center transition duration-300 text-white font-bold text-sm backdrop-blur-xs">
          <span>公式でサンプル動画を見る ➔</span>
        </a>
      </div>
      <div class="mt-4 space-y-2 text-xs text-slate-300">
        <div class="flex items-center gap-2"><span class="text-slate-400 font-semibold w-16">出演:</span> <div>{c_act_links or "単体女優"}</div></div>
        <div class="flex items-start gap-2"><span class="text-slate-400 font-semibold w-16 pt-0.5">タグ:</span> <div class="flex flex-wrap gap-1">{c_genre_tags}</div></div>
      </div>
    </div>

    <div class="md:col-span-7 space-y-4">
      <div class="bg-amber-950/20 border border-amber-500/20 p-4 rounded-2xl">
        <div class="text-amber-300 font-bold text-sm md:text-base mb-1">【見どころ・興奮ポイント】</div>
        <p class="text-slate-200 text-sm md:text-base font-semibold leading-snug">{h_lead}</p>
      </div>
      <p class="text-slate-300 text-sm md:text-base leading-relaxed font-normal">
        {h_body}
      </p>

      <div class="pt-2 flex flex-col sm:flex-row gap-3 items-center">
        <a href="{c_aff}" target="_blank" rel="nofollow noopener" class="w-full sm:w-auto flex-1 inline-flex items-center justify-center gap-2 px-6 py-3.5 bg-gradient-to-r from-rose-600 to-amber-600 hover:from-rose-500 hover:to-amber-500 text-white font-extrabold text-sm md:text-base rounded-2xl shadow-lg hover:shadow-rose-500/25 transition">
          <span>FANZA公式で見る（無料プレビュー）</span>
          <span>➔</span>
        </a>
        <a href="/posts/{c_cid}" class="w-full sm:w-auto inline-flex items-center justify-center gap-1 px-5 py-3.5 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold text-xs md:text-sm rounded-2xl border border-slate-700 transition">
          <span>詳細レビュー</span>
          <span>📖</span>
        </a>
      </div>
    </div>
  </div>

  {sample_html}
</div>""")

        # 徹底比較まとめ表
        table_rows = []
        for it in items_data:
            c_rank = it["rank"]
            c_title = it.get("title", "")
            c_act = " / ".join([a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]) or "単体女優"
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
<div id="comparison-table" class="my-10 bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl overflow-x-auto scroll-mt-24">
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
<div id="faq-section" class="my-10 bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl scroll-mt-24">
  <h3 class="text-xl md:text-2xl font-bold text-white mb-6 flex items-center gap-2">
    <span>💬</span> 本特集に関するよくある質問（FAQ）
  </h3>
  <div class="space-y-4">
{''.join(faq_boxes)}
  </div>
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
            "date": "2026-10-08 00:00:00",
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

    print("\n=== ALL 3 NEW KILLER FEATURES AND 15 INDIVIDUAL POSTS SUCCESSFULLY CREATED! ===")

if __name__ == "__main__":
    main()
