# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・超大型キラー特集3記事自動生成スクリプト
1. 【ギャル・黒ギャル・肉食ビッチ＆生意気搾精特化】
   『【生意気メスガキ＆極上腰振り】FANZA「ギャル・黒ギャル・ビッチ搾精」おすすめ神作ランキングTOP5！派手髪ネイルの肉食ギャルが「ざぁ〜こ♡」と煽りながら骨抜きにする至高のギャルハメAV選【2026年最新】』
2. 【時間停止・タイムストップ＆絶対無防備やりたい放題特化】
   『【男の究極妄想・やりたい放題】FANZA「時間停止・タイムストップ＆無防備中出し」おすすめ神作ランキングTOP5！ピタリと静止した無防備美女を弄び尽くし時間解除と同時に限界アクメさせる至高のファンタジーAV選【2026年最新】』
3. 【ガチハメ撮り・スマホ個人撮影＆素人流出風特化】
   『【生々しすぎる密室プライベート】FANZA「ガチハメ撮り・スマホ個人撮影＆素人流出風」おすすめ神作ランキングTOP5！作られた演技ゼロの生々しい喘ぎと無防備なアヘ顔に興奮が止まらない至高のリアル交尾AV選【2026年最新】』
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

INDIVIDUAL_REVIEWS = {
    # 記事1: ギャル
    "midv00274": """<h2>『有名ヤリマンギャルに成長した幼馴染と地元で遭遇して3日3晩で12発もぶっこ抜かれた思い出 七沢みあ』詳細レビュー</h2>
<p>圧倒的な童顔美少女として絶対的人気を誇る七沢みあが、ド派手な金髪ヤリマンギャルへと変貌を遂げ、地元で再会した主人公を昼夜問わず逆レイプ搾精し尽くす超メガヒット作。普段の清楚で愛らしいイメージを鮮やかに裏切るビッチっぷりと、小柄な身体をフルに使った積極的なグラインドが男の射精中枢を激しく揺さぶります。</p>

<h3>見どころ：垢抜けてエロフェロモン全開の幼馴染ギャル</h3>
<p>数年ぶりに帰省した地元で遭遇した七沢みあは、露出度の高いショートパンツに谷間全開のギャル服姿。「久しぶりじゃん！ちょっと部屋寄ってきなよ〜」と軽いノリで部屋に連れ込まれ、あっという間に押し倒される展開にテンションが一気に跳ね上がります。耳元で囁かれる小悪魔な挑発と、ぷるぷるの唇でしゃぶりつかれるフェラチオの快感は悶絶必至です。</p>

<h3>実用ポイント：3日3晩で12発抜かれる底なしの性欲と中出し連打</h3>
<p>「まだまだ出せるっしょ？」「男のくせにへばるの早すぎ〜」と嘲笑いながら、射精直後の敏感なペニスに跨がり直して腰を動かし続ける七沢みあ。小柄な腰が激しく打ち付けられるたびに結合部から愛液が飛び散り、子宮口に連続で白濁液を注ぎ込まれる限界交尾は、実用度・抜きやすさともに満点です。</p>""",

    "snos00369": """<h2>『普段は生意気なギャル教え子が…熱出した僕を心配し熱烈看病！ムラムラち●ぽまで介助してくれるギャップ母性に僕、大量射精！ 七ツ森りり』詳細レビュー</h2>
<p>トップモデル級のスタイルと美貌を誇る七ツ森りりが、学校ではタメ口でからかってくる生意気ギャル教え子を熱演。風邪で寝込んだ冴えない教師の自宅アパートへ突然やってきて、献身的な看病から下半身のムラムラ解消まで手厚くお世話してくれる至高のギャップ萌え作品です。</p>

<h3>見どころ：生意気な口調の裏に隠された一途な好意と献身エロス</h3>
<p>「先生さぁ、一人暮らしなんだから体調管理くらいちゃんとしなよ！」と文句を言いながらも、おかゆを作ってくれたり汗を拭いてくれたりするりりちゃん。布団の中で勃起してしまったペニスに気づくと、「…なにこれ、病気のくせにエロいこと考えてんの？」と呆れつつも、頬を赤らめてズボンの中に手を滑り込ませてきます。</p>

<h3>実用ポイント：熱っぽい吐息とスレンダー美脚での跨がり騎乗位</h3>
<p>「早く元気になってよね…」と囁きながら、パジャマをはだけさせて跨がってくる七ツ森りり。すらりと伸びた長い美脚で男の腰をロックし、熱気を帯びた膣内でじっくりと肉棒を締め上げる腰使いは芸術的なエロスを誇ります。精子を子宮に受け止めて満足そうに微笑む表情に男の自尊心は完全に満たされます。</p>""",

    "miaa00859": """<h2>『近所のスーパーでよく会う行き遅れギャルおばさんと意気投合して家に誘われ行ったら ギンギン青年チ○ポに発情して欲求不満なデカ尻で一晩で10発中出しSEXさせてくれた。 AIKA』詳細レビュー</h2>
<p>レジェンド黒ギャル女優・AIKAが、近所のスーパーで買い出し中に知り合った若い男を自宅に招き入れ、溜まりに溜まった性欲を爆発させて一晩で10発もの中出しを貪り尽くすド迫力の肉食エロス。日焼けした小麦色の肌と熟れきった肉感ヒップが、若い男のエネルギーを一滴残らず吸い尽くします。</p>

<h3>見どころ：ビール片手に下ネタ全開で誘惑してくるアラサーギャル</h3>
<p>「若い男の子の部屋ってなんか落ち着く〜」と缶ビールを飲みながら胸元を無防備に晒すAIKA。酔いが回るにつれてボディタッチが過激になり、自分から男の股間に手を伸ばして「すごい硬くなってんじゃん…お姉さんとエッチなことしちゃう？」と肉食の瞳をギラつかせる瞬間はアドレナリン全開です。</p>

<h3>実用ポイント：重量感ある美巨尻の高速ピストンとエンドレス中出し</h3>
<p>四つん這いにさせたAIKAの豊満な褐色ヒップを掴み、後ろから容赦なく打ち据えるバック。肉が激しく衝突する快音とともに「もっと奥突いて！全部出して！」と淫語を連発。射精しても休む間もなく次の回戦へと引きずり込まれる怒涛の10発中出しは、精力を極限まで燃焼させたい夜に最適です。</p>""",

    "mida00474": """<h2>『都会のイケメン彼氏に婚約破棄された幼馴染ギャルと帰省先で再会。 コンビニすらないド田舎でコンドームも買えずにヤケクソ腰振りラッキー中出し14発できちゃったボク。 うんぱい』詳細レビュー</h2>
<p>SNS総フォロワー数数百万人を誇る圧倒的インフルエンサー女優・うんぱいが、失恋のショックでド田舎の実家に戻ってきた傷心ギャルを熱演。ゴムの買い置きもない田舎の民家で、幼馴染の主人公とヤケクソ気味に生ハメ交尾になだれ込み、合計14発もの中出しを重ねて快楽堕ちしていく大人気作です。</p>

<h3>見どころ：ヤケ酒で自暴自棄になった神乳ギャルの無防備な誘惑</h3>
<p>「都会の男なんて大っ嫌い！」と浴びるように酒を飲み、胸の谷間をはだけさせて畳の上に転がるうんぱい。柔らかく豊満なFカップバストを押し付けられ、「アンタなら…ゴムなくてもいいよ？」と耳元で囁かれた瞬間の男の理性の消し飛び方は尋常ではありません。</p>

<h3>実用ポイント：ゴムなし生ハメの温もりと14発の連続種付け</h3>
<p>生肉と生肉が直接こすれ合う滑らかな感触に、うんぱいの嬌声も次第に本気のアクメへと変化。狭い膣内にドクドクと熱い精液が注ぎ込まれるたびに腰をビクビク跳ね上げ、「中に出されるの…超気持ちいい…！」と完全に生交尾の快楽に目覚める姿は実用度無限大です。</p>""",

    # 記事2: 時間停止
    "mida00558": """<h2>『さくらってリア充で幸せそうでムカつくから時間停止オジサンに好き放題レ●プしてもらったんだ。 水卜さくら』詳細レビュー</h2>
<p>圧倒的な透明感と吸い込まれるような瞳を持つトップ単体女優・水卜さくらが、妬みを買って時間停止能力を持つ中年男に日常のあらゆる場面で時間を止められ、無抵抗のまま肉体を弄ばれる傑作ファンタジーAV。ピタリと時間が止まった世界で、無防備な美少女を好き勝手に犯す背徳の全能感が凝縮されています。</p>

<h3>見どころ：表情を固定されたまま下着を脱がされる完全な無防備さ</h3>
<p>彼氏とデート中、あるいは街を歩いている最中にカチリと音が響き、マネキンのように静止する水卜さくら。動けない彼女の短いスカートをめくり、純白のショーツをずらして濡れそぼる秘部を指先でじっくり弄ぶシーンは、究極の覗き見・いたずら願望を完全に満たしてくれます。</p>

<h3>実用ポイント：時間解除の瞬間に一気に押し寄せる絶頂フラッシュ</h3>
<p>静止している彼女の膣内へ根元までペニスを突き刺し、たっぷり精液を流し込んだ直後に時間を解除！動き出した瞬間、体内に満ちた熱い精液と未知の快感に水卜さくらの瞳が見開かれ、声にならない絶叫とともに腰をガクガク痙攣させてイキ狂うクライマックスは圧巻の破壊力です。</p>""",

    "1start00518": """<h2>『ギャルコンビ時間停止 観光地で悪態をつく映えに必死なコンビニバイトの女2人を懲らしめろ！ 恋渕ももな×星乃莉子』詳細レビュー</h2>
<p>美巨乳の絶対女王・恋渕ももなと、スレンダー美少女・星乃莉子の最強ツートップが共演！観光地のコンビニで生意気な態度をとる映え重視ギャルふたりに対し、時間停止装置を発動して好き放題に肉体を開発・連続中出しでお仕置きする爽快かつ濃厚な時間停止作です。</p>

<h3>見どころ：対照的な2大美女が同時に静止する圧巻の光景</h3>
<p>コンビニのレジカウンターでスマホをいじりながら悪態をつくももなと莉子。時間を止めた瞬間、ピタリと動きを止めたふたりの制服を脱がせ、ももなの巨大な爆乳と莉子の引き締まった美尻を同時に堪能できる至福の構図。ふたりの秘部に交互に指を入れ、蜜を溢れさせていくプロセスは興奮度MAXです。</p>

<h3>実用ポイント：2人同時に時間解除してダブル絶頂中出し</h3>
<p>2人の膣内にそれぞれペニスを挿入して腰を振り、精液を奥深くまで注ぎ込んだ状態で時間を再開！「えっ！？なにこれ！？」とパニックになりながらも、すでにツボを突かれて敏感になりすぎた身体が快楽を拒めず、ふたり揃って白目を剥いて潮を噴き出す壮絶なWアクメは必見です。</p>""",

    "13dsvr01944": """<h2>『【VR】【8K】時間停止VR 神木麗』詳細レビュー</h2>
<p>完璧な美貌と豊満な神ボディで業界を席巻する神木麗が、超高画質8K VRの世界であなたの目の前で完全に静止！息遣いまで止まった神木麗の顔面に限界まで顔を近づけ、無防備な胸元や秘部をゼロ距離で観察しながら弄べる、まさにVR×時間停止の歴史的最高傑作です。</p>

<h3>見どころ：8K超至近距離で眺める静止した国宝級ボディ</h3>
<p>Meta Quest等のVRゴーグルを装着すると、目の前に等身大の神木麗が完全静止。まつ毛の先、唇の潤い、肌の産毛までくっきりと見える圧倒的解像度の中で、胸のボタンを外し、ブラジャーをめくって張りのある乳房を揉みしだく臨場感は、脳が現実と錯覚するほどの衝撃を与えます。</p>

<h3>実用ポイント：静止したまま犯し、解除で目の前でイキ乱れる没入体験</h3>
<p>動かない神木麗の膣内へゆっくりと男根を沈め、自分のペースで好きなだけ腰を打ち付ける全能感。そしてVRコントローラーで時間を解除した瞬間、目の前数センチの距離で神木麗が息を呑み、あなたを見つめ返しながら恍惚の表情でイキ崩れる瞬間は、二度と通常の動画に戻れなくなる異次元の実用度です。</p>""",

    "mimk00122": """<h2>『鉄拳精裁ストップマン 時間停止vs元彼殺しサイコ女 原作・alansmithee同人を実写化！ 黒川すみれ』詳細レビュー</h2>
<p>大人気同人サークルの大ヒット傑作CGを、妖艶な美貌と卓越した演技力を持つ黒川すみれ主演で完全実写化。狂気と殺意を秘めた危険な美女を相手に、時間停止能力を駆使して反撃し、屈辱と快楽で完全服従させていくサスペンスフルかつ超濃厚なダークエロスです。</p>

<h3>見どころ：凶器を手にした冷酷美女がマネキン化する緊張と緩和</h3>
<p>冷たい視線で男を追い詰める黒川すみれが、能力発動と同時にピタッと静止。さっきまでの殺気配が一変し、無抵抗な肉体へと変貌するギャップが男の支配欲を猛烈に刺激します。拘束具を嵌め、動けない彼女の衣服を切り裂いていく背徳のイタズラはゾクゾクする興奮に満ちています。</p>

<h3>実用ポイント：プライドをへし折る奥突きピストンと屈服アクメ</h3>
<p>時間を解除するたびに「殺してやる…！」と睨みつけてくる黒川すみれだが、秘部の奥深くに激しいピストンを食らううちに次第に強気な言葉が甘い喘ぎ声へと崩壊。最後は涙目になって自ら腰を浮かせて快楽を受け入れる屈服中出しは、M女・強気美女好きのツボを完全に貫通します。</p>""",

    "hsoda00004": """<h2>『時間停止学級。時間を止める事が出来る神装置で、好きな時に挿れたり、止めたりし放題。』詳細レビュー</h2>
<p>時間停止AVの元祖にして金字塔、SODのメガヒットシリーズ『時間停止学級』の超人気回。学校の教室、体育館、職員室で神装置のリモコンをカチリと押すだけで、授業中の女子生徒や女教師たちがその場で完全フリーズ！日常の風景の中で繰り広げられる究極のやりたい放題イタズラ絵巻です。</p>

<h3>見どころ：クラスメイトたちの前で堂々と行われる無防備セックス</h3>
<p>黒板に向かって授業を聞いている女子生徒たちのスカートをめくり、ショーツを脱がせて教室の机の上に並べる背徳感。隣に男子生徒や先生が静止している状況で、無防備な女子の股間にペニスを挿入して腰を振るシチュエーションは、男の露出・覗き見妄想を限界まで煽り立てます。</p>

<h3>実用ポイント：止めたり動かしたりを繰り返す焦らしピストン</h3>
<p>動かして感じさせ、イキそうになったら止めて焦らし、再び動かして絶頂へ追い込むテクニカルな時間操作。女子生徒たちが何が起きているかわからないまま、下半身から溢れる愛液でスカートを汚し、連続で中出しを受け止める快感はシリーズ随一の実用度を誇ります。</p>""",

    # 記事3: ハメ撮り
    "ssis00875": """<h2>『河北彩花の完全プライベートセックス全部撮った！ 圧倒的に支持される新時代トップ女優と朝まで2人きりの生々ハメ撮りFUCK 河北彩花』詳細レビュー</h2>
<p>現代AV界の頂点に君臨する国民的トップ女優・河北彩花が、撮影スタジオを飛び出し、男と2人きりのホテル密室で完全プライベートな濃密セックスに溺れる歴史的神作。過剰な演出や照明を極限まで削ぎ落とし、ハンディカメラ1台で捉えられた河北彩花の素の表情と生々しい愛液の交わりが画面から溢れ出します。</p>

<h3>見どころ：ベッドの上でゴロゴロしながら見せる無防備な笑顔と甘え声</h3>
<p>カメラを向けられて「恥ずかしいから撮らないでよぉ…」とシーツに顔を埋める河北彩花。ノーメイクに近いナチュラルな美貌と、お酒を飲んでほんのり赤らんだ頬がリアルな恋人感を演出します。不意にカメラを見つめてキスをねだってくるゼロ距離の破壊力に男の心拍数は跳ね上がります。</p>

<h3>実用ポイント：女優の仮面を脱ぎ捨てて本能でヨガる生々しい喘ぎと中出し</h3>
<p>照明の薄暗い部屋で、肌と肌が激しくぶつかり合う鈍い音と、粘膜が擦れ合うリアルな水音。河北彩花がカメラを忘れて男の首に腕を回し、瞳を潤ませながら「彩花のなかに…いっぱい出して…」と懇願するシーンは、全AVファンが夢見た至高の射精トリガーです。</p>""",

    "snos00312": """<h2>『【緊急ロケ企画】AV女優がSNSで一般男性とヤリモクマッチングしたら…まさかの素人チ●ポのほうが キモチいいぃぃ！！！生々ハメ撮りドキュメント Gonzo Document 渚あいり』詳細レビュー</h2>
<p>愛くるしいタヌキ顔と抜群のスタイルで大人気の渚あいりが、SNSのマッチングアプリで一般男性とガチでアポを取り、ホテルの密室でヤリモク逢瀬を敢行する衝撃のハメ撮りドキュメント。プロの男優とは違う素人男子の荒々しい攻めに、渚あいりがガチで感じて快楽堕ちしていく生々しさが異常な興奮を呼びます。</p>

<h3>見どころ：マッチングアプリ特有の緊張感から一気に崩れるガード</h3>
<p>ホテルのロビーで待ち合わせ、部屋に入って乾杯した直後から始まるぎこちないスキンシップ。素人男性の手が恐る恐る胸に伸びると、渚あいりの吐息が一気に熱くなり、「アプリで会った人とこんなことするの初めて…」と呟きながら舌を絡ませていくリアルなドキュメンタリータッチが最高にエロティックです。</p>

<h3>実用ポイント：素人チンポの不器用なピストンに本気で啼く渚あいり</h3>
<p>ベッドの上で手持ちカメラを回しながら、男の激しいピストンに揺られる渚あいり。カメラ目線でアヘ顔を晒し、「素人のくせに…めっちゃ硬い…！イッちゃう！」と本気のアクメで腰を跳ね上げる姿は、計算された演技では絶対に撮れない生々しいエロスを放ちます。</p>""",

    "ajsp00001": """<h2>『【スマホ推奨】『彼女が3日間家族旅行で家を空けるというので、彼女の友達と3日間ハメまくった記録（仮） 枢木あおい』より 1日目のスマホハメ撮り動画FULL 枢木あおい』詳細レビュー</h2>
<p>小動物系の愛らしいルックスとスレンダー美脚で人気の枢木あおいが、スマホ縦画面撮影の超リアルなハメ撮り映像で男を魅了する大ヒット作。留守中の部屋で彼女の友達と一線を越えてしまう極限の背徳シチュエーションが、スマホの画面いっぱいに広がる縦撮り映像によって完璧な臨場感を生み出しています。</p>

<h3>見どころ：スマホ全画面で目の前に迫る超至近距離の背徳密会</h3>
<p>スマホを縦にして鑑賞すると、まるで自分のスマートフォンに流出動画が届いたかのような生々しい錯覚に陥る本作。ベッドの上で下着姿になった枢木あおいが、「彼女にバレたらどうすんの…？」と戸惑いながらも、ペニスを握りしめてフェラを始める距離感の近さは圧巻です。</p>

<h3>実用ポイント：手ブレと息遣いがリアルすぎる縦撮り生中出し</h3>
<p>片手でスマホを持ちながら、もう片方の手であおいの腰を掴んで突き入れるPOVハメ撮り。画面越しに目が合い、切なげな顔で「中に…出しちゃダメだよ…？」と言われながらも奥深くまで白濁液をドクドク注ぎ込む瞬間は、背徳オナニーの最高峰と言えます。</p>""",

    "mida00812": """<h2>『尊すぎる原石 最強幼ビジュAV DEBUT 平野楓』詳細レビュー</h2>
<p>業界に激震を走らせた超ド級の大型新人・平野楓の鮮烈なAVデビュー作。尊すぎるほどの透明感あふれる幼顔と、まだカメラに慣れていない初々しい恥じらいが、密室での個別撮影・ハメ撮り風のアングルによって余すところなく捉えられています。</p>

<h3>見どころ：カメラを直視できずに頬を真っ赤にする圧倒的ウブ感</h3>
<p>ホテルのベッドに腰掛け、スタッフに服を脱がされるだけで耳まで赤く染めてしまう平野楓。細い指で胸元を隠そうとする仕草や、初めて見る大人の男根に怯えながらも好奇心を隠せない純真な瞳は、全男性の加虐心と庇護欲を同時に直撃します。</p>

<h3>実用ポイント：未知の刺激に身体を弓なりにして震える初絶頂</h3>
<p>狭く引き締まった秘部へゆっくりと男根が進入した瞬間、小さな口を開けて息を呑む平野楓。痛みが快感に変わるにつれて華奢な手足がベッドのシーツを強く握りしめ、初めて味わう激しいオーガズムに身を震わせる姿は、二度と再現できない奇跡のドキュメントです。</p>"""
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
    date_str = it.get("date", "2026-10-05 23:00:00")
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
<p>本作は、{act_str}が圧倒的なエロティシズムと鬼気迫る演技力を発揮し、シチュエーションの興奮を最高潮に高めた話題の傑作です。</p>
<h3>主演キャスト（{act_str}）の熱演と見どころ</h3>
<p>{act_str}の吐息が肌を伝わるようなゼロ距離の臨場感と、次第に理性を奪われて快楽に溺れていく艶やかな表情の変化は必見。汗ばんだ肌と絡み合う視線が男の本能を強く刺激します。</p>
<h3>実用ポイント・結合と絶頂の臨場感</h3>
<p>クライマックスで繰り広げられる激しいピストンと、子宮奥深くまで突き刺さる濃厚な生交尾は破壊力抜群。反響する水音と途切れ途切れの嬌声が五感をダイレクトに直撃し、限界射精へと導いてくれます。</p>
<h3>総評・おすすめの鑑賞スタイル</h3>
<p>細部にまでこだわり抜かれた官能描写と圧倒的な実用度を兼ね備えた一本。今夜じっくりと独りで濃厚な射精を味わいたい時に自信を持っておすすめできる名作です。</p>"""

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
# 記事1: ギャル・黒ギャル・肉食ビッチ＆生意気搾精 特化
# ==============================================================================
def generate_article_gyaru():
    print("=== Generating Article 1: ギャル・黒ギャル・ビッチ搾精 特化 ===")
    cids = ["midv00274", "mida00546", "snos00369", "miaa00859", "mida00474"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["ギャル", "黒ギャル", "ビッチ", "中出し", "逆レイプ", "殿堂入り"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 1 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-pink-950/40 via-slate-900 to-slate-950 border border-pink-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-pink-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-pink-500/20 text-pink-300 border border-pink-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">GYARU & SEXY BITCH SPECIAL</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月05日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【生意気メスガキ＆極上腰振り】FANZA「ギャル・黒ギャル・ビッチ搾精」おすすめ神作ランキングTOP5！派手髪ネイルの肉食ギャルが「ざぁ〜こ♡」と煽りながら骨抜きにする至高のギャルハメAV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    男の征服欲とドM本能を同時に狂わせる不滅の王道ジャンル、それが「ギャル・ビッチ・肉食メスガキ搾精モノ」です。派手な髪色にバッチリ決めたアイメイク、キラキラ光る長いネイル、そして小麦色や美白の露出度全開ボディ。普段は「おじさんキモ〜い」「童貞とかマジウケるんだけど」と小馬鹿にしてくる生意気なギャルたちが、いざベッドになだれ込むと誰よりも淫乱で貪欲な肉食牝へと豹変します。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    「えー、こんな硬いので突かれたらイッちゃうじゃん！」「もっと奥まで中出ししてよぉ！」と挑発しながら、男の上に跨がって容赦なく腰をグラインドさせてくる騎乗位。射精直後でヘトヘトになったペニスを逃がさず、「男のくせに休むの早すぎ〜♡まだまだ出すでしょ？」と追撃ピストンで2発目、3発目を強引に搾り取られる快感は、一度味わえば二度と抜け出せない禁断の中毒性を持っています。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、レビュー330件超の伝説的メガヒットを記録した七沢みあのヤリマン幼馴染ギャル作から、松本いちか＆春陽モカのWギャル泥酔部屋入り浸り、七ツ森りりの生意気教え子ギャップ看病、レジェンドAIKAの欲求不満デカ尻10発中出し、そしてSNS最強インフルエンサーうんぱいの田舎ヤケクソ生ハメ14発まで、ギャルエロの真髄を極めた【ギャル神作TOP5】を徹底レビューします！
  </p>
</div>

<!-- 選び方の基準 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-pink-400">💄</span> ギャル・ビッチ作品で限界射精を迎える3大チェックポイント
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-pink-300 mb-2">① 生意気な挑発から快楽堕ちトロ顔へのギャップ</h4>
      <p class="text-slate-300 leading-relaxed">上から目線で煽っていたギャルが、深いピストンで奥を突かれた瞬間に白目を剥いて「ごめんなさいイッちゃう！」とメス堕ちする表情の変化が最大の抜きどころです。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-pink-300 mb-2">② 容赦ない腰振りグラインドと追撃搾精</h4>
      <p class="text-slate-300 leading-relaxed">ギャルならではの柔軟な股関節と躍動感ある腰使い。射精してもチ○ポを抜かずに2回戦、3回戦へと強制連行する底なしのスタミナが男の精力を焼き尽くします。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-pink-300 mb-2">③ ゴムなし生中出しへの異常な執着</h4>
      <p class="text-slate-300 leading-relaxed">「生で挿れてよ」「全部中にドピュドピュ出して！」と自ら子宮口を開いて精子をねだる背徳の生ハメ願望。溢れ出る白濁液を誇らしげに見つめる姿が興奮を倍増させます。</p>
    </div>
  </div>
</div>

<!-- 目次 -->
<div class="my-8 bg-slate-900/60 border border-slate-800 rounded-2xl p-5 shadow-inner">
  <h4 class="text-sm font-bold text-slate-300 mb-3 flex items-center gap-2">
    <span>📑</span> 目次：おすすめランキングTOP5
  </h4>
  <ul class="space-y-2 text-xs md:text-sm text-pink-400/90 font-medium">
    <li><a href="#rank-1" class="hover:underline flex items-center justify-between"><span>第1位：有名ヤリマンギャルに成長した幼馴染（七沢みあ）</span><span class="text-slate-500 text-xs">レビュー330件の歴史的メガヒット</span></a></li>
    <li><a href="#rank-2" class="hover:underline flex items-center justify-between"><span>第2位：終電後僕の部屋に入り浸りギャル（松本いちか×春陽モカ）</span><span class="text-slate-500 text-xs">Wギャル泥酔ローション風呂</span></a></li>
    <li><a href="#rank-3" class="hover:underline flex items-center justify-between"><span>第3位：普段は生意気なギャル教え子が熱烈看病（七ツ森りり）</span><span class="text-slate-500 text-xs">ギャップ萌え母性搾精</span></a></li>
    <li><a href="#rank-4" class="hover:underline flex items-center justify-between"><span>第4位：行き遅れギャルおばさんと意気投合（AIKA）</span><span class="text-slate-500 text-xs">欲求不満デカ尻一晩10発中出し</span></a></li>
    <li><a href="#rank-5" class="hover:underline flex items-center justify-between"><span>第5位：都会のイケメン彼氏に婚約破棄された幼馴染ギャル（うんぱい）</span><span class="text-slate-500 text-xs">田舎ヤケクソ生ハメ14発</span></a></li>
  </ul>
</div>"""
    html_parts.append(intro_html)

    # ランキング5作品詳細
    for idx, it in enumerate(items):
        cid = it.get("content_id")
        title = it.get("title")
        acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        act_links = " ".join([get_actress_link(a) for a in acts])
        genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        genre_links = " ".join([get_genre_link(g) for g in genres[:5]])
        hinban = cid.upper()
        aff_url = it.get("affiliate_url_clean")
        img_large = it.get("imageURL", {}).get("large")
        s_imgs = get_sample_images(it, 4)

        rank_num = idx + 1
        rank_badge = f'<span class="bg-gradient-to-r from-pink-500 to-rose-400 text-slate-950 text-sm md:text-base font-black px-4 py-1 rounded-full shadow-lg">第{rank_num}位（殿堂入り）</span>' if rank_num == 1 else f'<span class="bg-slate-700 text-pink-300 text-sm md:text-base font-black px-4 py-1 rounded-full">第{rank_num}位</span>'

        # 作品ごとの詳細レビュー文
        rev_html = INDIVIDUAL_REVIEWS.get(cid, "")
        clean_rev = re.sub(r'<h2>.*?</h2>', '', rev_html)

        sample_imgs_html = ""
        if s_imgs:
            imgs_tags = "".join([f'<img src="{sim}" alt="サンプル画像" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />' for sim in s_imgs])
            sample_imgs_html = f'<div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-6">{imgs_tags}</div>'

        item_card = f"""<div id="rank-{rank_num}" class="my-10 bg-slate-900 border {'border-2 border-pink-500/40' if rank_num == 1 else 'border-slate-800'} rounded-2xl p-6 md:p-8 shadow-2xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-3">
      {rank_badge}
      <h3 class="text-lg md:text-2xl font-black text-white">{title}</h3>
    </div>
    <div class="text-xs text-slate-400">品番：{hinban} / 出演：{act_links}</div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <div class="space-y-4">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block group relative overflow-hidden rounded-xl border border-slate-700">
        <img src="{img_large}" alt="{title}" class="w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-4">
          <span class="text-white text-xs font-bold bg-pink-600/90 px-3 py-1 rounded-full">FANZA公式で作品詳細を見る →</span>
        </div>
      </a>
      <div class="flex flex-wrap gap-2">
        {genre_links}
      </div>
    </div>
    <div class="space-y-4 text-xs md:text-sm text-slate-300 leading-relaxed">
      {clean_rev}
      <div class="pt-2">
        <a href="/posts/{cid}" class="text-xs text-pink-400 hover:text-pink-300 underline font-bold">👉 作品個別ページ（サンプル画像・詳細レビュー）を見る</a>
      </div>
    </div>
  </div>

  {sample_imgs_html}

  <div class="text-center">
    <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-2 bg-gradient-to-r from-pink-500 via-rose-500 to-pink-500 hover:opacity-95 text-white font-black text-sm md:text-base px-8 py-4 rounded-xl shadow-xl transition transform hover:scale-105">
      <span>今すぐFANZA公式で『{title[:20]}…』をフル視聴する</span>
      <span>🚀</span>
    </a>
  </div>
</div>"""
        html_parts.append(item_card)

    # 比較表、関連記事リンク、FAQ
    table_and_links = """<!-- スペック比較まとめ表 -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl overflow-x-auto">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>📊</span> おすすめギャル神作TOP5 徹底スペック比較表
  </h3>
  <table class="w-full text-left text-xs md:text-sm text-slate-300">
    <thead class="bg-slate-800/80 text-pink-300 uppercase font-bold border-b border-slate-700">
      <tr>
        <th class="p-3">順位・タイトル</th>
        <th class="p-3">主演女優</th>
        <th class="p-3">ギャル属性・シチュエーション</th>
        <th class="p-3">射精圧・実用度</th>
        <th class="p-3">公式リンク</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-slate-800">
      <tr class="hover:bg-slate-800/40">
        <td class="p-3 font-bold text-white">第1位：有名ヤリマンギャルに成長した幼馴染</td>
        <td class="p-3">七沢みあ</td>
        <td class="p-3">幼馴染再会・3日3晩12発ぶっこ抜き</td>
        <td class="p-3 text-pink-400 font-bold">★★★★★ (120%)</td>
        <td class="p-3"><a href="/posts/midv00274" class="text-pink-400 hover:underline">詳細</a></td>
      </tr>
      <tr class="hover:bg-slate-800/40">
        <td class="p-3 font-bold text-white">第2位：終電後僕の部屋に入り浸りギャル</td>
        <td class="p-3">松本いちか×春陽モカ</td>
        <td class="p-3">泥酔お泊まり・Wギャルローション風呂</td>
        <td class="p-3 text-pink-400 font-bold">★★★★★ (115%)</td>
        <td class="p-3"><a href="/posts/mida00546" class="text-pink-400 hover:underline">詳細</a></td>
      </tr>
      <tr class="hover:bg-slate-800/40">
        <td class="p-3 font-bold text-white">第3位：普段は生意気なギャル教え子看病</td>
        <td class="p-3">七ツ森りり</td>
        <td class="p-3">風邪看病・ギャップ母性跨がり騎乗位</td>
        <td class="p-3 text-pink-400 font-bold">★★★★★ (110%)</td>
        <td class="p-3"><a href="/posts/snos00369" class="text-pink-400 hover:underline">詳細</a></td>
      </tr>
      <tr class="hover:bg-slate-800/40">
        <td class="p-3 font-bold text-white">第4位：行き遅れギャルおばさんと意気投合</td>
        <td class="p-3">AIKA</td>
        <td class="p-3">近所スーパー・欲求不満デカ尻10発</td>
        <td class="p-3 text-pink-400 font-bold">★★★★★ (115%)</td>
        <td class="p-3"><a href="/posts/miaa00859" class="text-pink-400 hover:underline">詳細</a></td>
      </tr>
      <tr class="hover:bg-slate-800/40">
        <td class="p-3 font-bold text-white">第5位：都会彼氏に婚約破棄された幼馴染</td>
        <td class="p-3">うんぱい</td>
        <td class="p-3">田舎実家・ヤケクソ生ハメ中出し14発</td>
        <td class="p-3 text-pink-400 font-bold">★★★★★ (110%)</td>
        <td class="p-3"><a href="/posts/mida00474" class="text-pink-400 hover:underline">詳細</a></td>
      </tr>
    </tbody>
  </table>
</div>

<!-- 関連記事・内部リンク -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>🔗</span> あわせて読みたい！おすすめの超人気キラー特集記事
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs md:text-sm">
    <a href="/posts/feature_fanza_reverse_rape_forced_ejaculation_cowgirl_ranking_2026" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-pink-500/50 transition block">
      <div class="font-bold text-pink-300 mb-1">【男が犯される極限快楽】逆レイプ・連続強制搾精・腰振り騎乗位TOP5</div>
      <p class="text-slate-400 line-clamp-2">肉食美女に拘束され射精後も逃げ場ゼロで金玉が空になるまで搾り取られるドM昇天AV選！</p>
    </a>
    <a href="/posts/feature_fanza_sugar_daddy_allowance_raw_creampie_ranking_2026" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-amber-500/50 transition block">
      <div class="font-bold text-amber-300 mb-1">【お金の魔力でプライド崩壊】パパ活女子・お手当増額生中出しTOP5</div>
      <p class="text-slate-400 line-clamp-2">小遣い稼ぎの生意気美少女がお手当に負けて生ハメ種付けを受け入れる屈辱快楽AV選！</p>
    </a>
    <a href="/posts/feature_fanza_titfuck_paizuri_huge_breasts_suffocation_ranking_2026" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-rose-500/50 transition block">
      <div class="font-bold text-rose-300 mb-1">【神乳に埋もれて昇天】極上パイズリ・巨乳挟まれ窒息射精ランキングTOP5</div>
      <p class="text-slate-400 line-clamp-2">たわわな爆乳の谷間に包まれて精子を一滴残らず搾り取られる夢の母性＆快楽AV選！</p>
    </a>
    <a href="/posts/feature_fanza_aphrodisiac_drugged_ecstasy_spasm_ranking_2026" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-purple-500/50 transition block">
      <div class="font-bold text-purple-300 mb-1">【理性崩壊の肉欲痙攣】媚薬・キメセク・ガンギマリ発情おすすめ神作TOP5</div>
      <p class="text-slate-400 line-clamp-2">清楚美女が超強力媚薬で白目を剥いて腰を振り乱す限界潮吹き交尾AV選！</p>
    </a>
  </div>
</div>

<!-- よくある質問（FAQ） -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>❓</span> ギャル・ビッチAVに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-4 text-xs md:text-sm">
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-pink-300 mb-2">Q1. ギャルAVで最も抜けるシチュエーションは何ですか？</h4>
      <p class="text-slate-300 leading-relaxed">普段は生意気な態度をとっているギャルが、深いピストンで奥を突かれた瞬間に「もうダメ、イッちゃう！」と素に戻って啼き狂うメス堕ちシーンです。</p>
    </div>
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-pink-300 mb-2">Q2. 初めてギャル作品を観るならどの作品がおすすめですか？</h4>
      <p class="text-slate-300 leading-relaxed">第1位の七沢みあ主演作（MIDV-0274）です。レビュー330件超の圧倒的高評価を誇り、ヤリマン幼馴染の積極的な腰振りと中出し連発で確実に射精できます。</p>
    </div>
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-pink-300 mb-2">Q3. Wギャルや乱交を楽しみたい場合は？</h4>
      <p class="text-slate-300 leading-relaxed">第2位の松本いちか×春陽モカ共演作（MIDA-0546）が最適です。泥酔した2大人気ギャルに挟まれ、ローション風呂で朝まで搾り取られる夢のシチュエーションを体験できます。</p>
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
                "name": "FANZA「ギャル・黒ギャル・ビッチ搾精」おすすめ神作ランキングTOP5",
                "description": "派手髪ネイルの肉食ギャルが「ざぁ〜こ♡」と煽りながら骨抜きにする至高のギャルハメAV選【2026年最新】",
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
                        "name": "ギャルAVで最も抜けるシチュエーションは何ですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "普段は生意気な態度をとっているギャルが、深いピストンで奥を突かれた瞬間に「もうダメ、イッちゃう！」と素に戻って啼き狂うメス堕ちシーンです。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "初めてギャル作品を観るならどの作品がおすすめですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第1位の七沢みあ主演作（MIDV-0274）です。レビュー330件超の圧倒的高評価を誇り、ヤリマン幼馴染の積極的な腰振りと中出し連発で確実に射精できます。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Wギャルや乱交を楽しみたい場合は？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第2位の松本いちか×春陽モカ共演作（MIDA-0546）が最適です。泥酔した2大人気ギャルに挟まれ、ローション風呂で朝まで搾り取られる夢のシチュエーションを体験できます。"
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
        "id": "feature_fanza_gyaru_tanned_bitch_reverse_sperm_drain_ranking_2026",
        "title": "【生意気メスガキ＆極上腰振り】FANZA「ギャル・黒ギャル・ビッチ搾精」おすすめ神作ランキングTOP5！派手髪ネイルの肉食ギャルが「ざぁ〜こ♡」と煽りながら骨抜きにする至高のギャルハメAV選【2026年最新】",
        "date": "2026-10-05 23:50:00",
        "hinban": "GYARU-BITCH-REVERSE-DRAIN-2026",
        "price": "300~",
        "maker": "FANZA公式セレクション",
        "actresses": ["七沢みあ", "松本いちか", "春陽モカ", "七ツ森りり", "AIKA", "うんぱい"],
        "genres": ["ギャル", "黒ギャル", "美少女", "中出し", "逆レイプ", "騎乗位", "潮吹き", "特集", "殿堂入り"],
        "image": cover_image,
        "review": full_html
    }

    file_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f" -> Successfully saved Article 1 ({char_count} chars) to {file_path}")


# ==============================================================================
# 記事2: 時間停止・タイムストップ＆絶対無防備やりたい放題 特化
# ==============================================================================
def generate_article_time_stop():
    print("=== Generating Article 2: 時間停止・タイムストップ＆無防備やりたい放題 特化 ===")
    cids = ["mida00558", "1start00518", "13dsvr01944", "mimk00122", "hsoda00004"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["時間停止", "無防備", "いたずら", "中出し", "ファンタジー", "殿堂入り"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 2 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-indigo-950/40 via-slate-900 to-slate-950 border border-indigo-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-indigo-500/20 text-indigo-300 border border-indigo-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">TIME STOP & FROZEN ECSTASY SPECIAL</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月05日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【男の究極妄想・やりたい放題】FANZA「時間停止・タイムストップ＆無防備中出し」おすすめ神作ランキングTOP5！ピタリと静止した無防備美女を弄び尽くし時間解除と同時に限界アクメさせる至高のファンタジーAV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    男なら少年時代に一度は夢想したであろう究極のチート能力、それが「時間を止めて世界中の美女を好き放題に弄ぶ」という時間停止ファンタジーです。ボタンをカチリと押した瞬間、世界中のすべての音が消え去り、歩行中、会話中、授業中、仕事中の美女たちがマネキンのようにその場でピタリと完全フリーズ。相手の意思や拒絶を完全に無力化し、無抵抗な身体を好きなだけ堪能できる全能感は他のシチュエーションとは一線を画す圧倒的快楽をもたらします。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    静止した美女の衣服をゆっくりと剥ぎ取り、純白のショーツをずらして露わになる無防備な秘部。指先で愛撫してもピクリとも動かない美女の膣内へ、男根をズブズブと奥深くまで沈め、自分の好きなリズムで生中出しをキメる背徳の極致。そして本ジャンル最大のカタルシスは「時間解除の瞬間」に訪れます。止まっていた時間が動き出した瞬間、体内に満ちた熱い精液と未知の快楽が一気に押し寄せ、美女たちがパニックと悶絶のアヘ顔で腰を跳ね上げる瞬間は興奮の頂点を叩き出します。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、水卜さくらがリア充の日常から突如停止オジサンに好き放題犯される話題作から、恋渕ももな×星乃莉子のWトップ女優コンビニ時間停止、神木麗の息づかいまで止まる超高画質8K VR時間停止、黒川すみれのサイコ美女停止同人実写化、そしてSOD伝統の時間停止学級シリーズまで、全能感と実用度の頂点を極めた【時間停止神作TOP5】を徹底比較・レビューします！
  </p>
</div>

<!-- 選び方の基準 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-indigo-400">⏱️</span> 時間停止作品で究極の全能感を味わう3大チェックポイント
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-indigo-300 mb-2">① 静止状態のリアルさと無防備な肉体描写</h4>
      <p class="text-slate-300 leading-relaxed">瞬きひとつせずマネキン化した美女の服をめくり、無防備な谷間や恥毛、ピンク色の秘部をじっくり鑑賞・愛撫できる視覚的クオリティが重要です。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-indigo-300 mb-2">② 時間解除フラッシュで一斉に襲いかかる絶頂</h4>
      <p class="text-slate-300 leading-relaxed">時間を動かした瞬間、蓄積された快楽と精液の熱さに女優の瞳が見開かれ、声にならない嬌声とともに激しく痙攣するカタルシスが最高潮の抜きどころです。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-indigo-300 mb-2">③ 日常空間（教室・路上・コンビニ）での背徳感</h4>
      <p class="text-slate-300 leading-relaxed">周囲の他人が止まっているすぐ横で堂々と行われる無防備セックス。バレるはずがないのに心臓が高鳴るスリルが男の脳髄を痺れさせます。</p>
    </div>
  </div>
</div>

<!-- 目次 -->
<div class="my-8 bg-slate-900/60 border border-slate-800 rounded-2xl p-5 shadow-inner">
  <h4 class="text-sm font-bold text-slate-300 mb-3 flex items-center gap-2">
    <span>📑</span> 目次：おすすめランキングTOP5
  </h4>
  <ul class="space-y-2 text-xs md:text-sm text-indigo-400/90 font-medium">
    <li><a href="#rank-1" class="hover:underline flex items-center justify-between"><span>第1位：さくらってリア充で幸せそうだから（水卜さくら）</span><span class="text-slate-500 text-xs">透明感美女の無抵抗レ●プ</span></a></li>
    <li><a href="#rank-2" class="hover:underline flex items-center justify-between"><span>第2位：ギャルコンビ時間停止（恋渕ももな×星乃莉子）</span><span class="text-slate-500 text-xs">Wトップ女優のコンビニ懲らしめ</span></a></li>
    <li><a href="#rank-3" class="hover:underline flex items-center justify-between"><span>第3位：【VR】【8K】時間停止VR（神木麗）</span><span class="text-slate-500 text-xs">ゼロ距離密着の究極没入VR</span></a></li>
    <li><a href="#rank-4" class="hover:underline flex items-center justify-between"><span>第4位：鉄拳精裁ストップマン（黒川すみれ）</span><span class="text-slate-500 text-xs">人気同人原作のサイコ美女屈服</span></a></li>
    <li><a href="#rank-5" class="hover:underline flex items-center justify-between"><span>第5位：時間停止学級。神装置で挿れ放題（SOD）</span><span class="text-slate-500 text-xs">元祖にして最高峰の学級停止</span></a></li>
  </ul>
</div>"""
    html_parts.append(intro_html)

    # ランキング5作品詳細
    for idx, it in enumerate(items):
        cid = it.get("content_id")
        title = it.get("title")
        acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        act_links = " ".join([get_actress_link(a) for a in acts]) if acts else "豪華キャスト"
        genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        genre_links = " ".join([get_genre_link(g) for g in genres[:5]])
        hinban = cid.upper()
        aff_url = it.get("affiliate_url_clean")
        img_large = it.get("imageURL", {}).get("large")
        s_imgs = get_sample_images(it, 4)

        rank_num = idx + 1
        rank_badge = f'<span class="bg-gradient-to-r from-indigo-500 to-purple-400 text-slate-950 text-sm md:text-base font-black px-4 py-1 rounded-full shadow-lg">第{rank_num}位（殿堂入り）</span>' if rank_num == 1 else f'<span class="bg-slate-700 text-indigo-300 text-sm md:text-base font-black px-4 py-1 rounded-full">第{rank_num}位</span>'

        rev_html = INDIVIDUAL_REVIEWS.get(cid, "")
        clean_rev = re.sub(r'<h2>.*?</h2>', '', rev_html)

        sample_imgs_html = ""
        if s_imgs:
            imgs_tags = "".join([f'<img src="{sim}" alt="サンプル画像" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />' for sim in s_imgs])
            sample_imgs_html = f'<div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-6">{imgs_tags}</div>'

        item_card = f"""<div id="rank-{rank_num}" class="my-10 bg-slate-900 border {'border-2 border-indigo-500/40' if rank_num == 1 else 'border-slate-800'} rounded-2xl p-6 md:p-8 shadow-2xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-3">
      {rank_badge}
      <h3 class="text-lg md:text-2xl font-black text-white">{title}</h3>
    </div>
    <div class="text-xs text-slate-400">品番：{hinban} / 出演：{act_links}</div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <div class="space-y-4">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block group relative overflow-hidden rounded-xl border border-slate-700">
        <img src="{img_large}" alt="{title}" class="w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-4">
          <span class="text-white text-xs font-bold bg-indigo-600/90 px-3 py-1 rounded-full">FANZA公式で作品詳細を見る →</span>
        </div>
      </a>
      <div class="flex flex-wrap gap-2">
        {genre_links}
      </div>
    </div>
    <div class="space-y-4 text-xs md:text-sm text-slate-300 leading-relaxed">
      {clean_rev}
      <div class="pt-2">
        <a href="/posts/{cid}" class="text-xs text-indigo-400 hover:text-indigo-300 underline font-bold">👉 作品個別ページ（サンプル画像・詳細レビュー）を見る</a>
      </div>
    </div>
  </div>

  {sample_imgs_html}

  <div class="text-center">
    <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-2 bg-gradient-to-r from-indigo-500 via-purple-500 to-indigo-500 hover:opacity-95 text-white font-black text-sm md:text-base px-8 py-4 rounded-xl shadow-xl transition transform hover:scale-105">
      <span>今すぐFANZA公式で『{title[:20]}…』をフル視聴する</span>
      <span>🚀</span>
    </a>
  </div>
</div>"""
        html_parts.append(item_card)

    table_and_links = """<!-- スペック比較まとめ表 -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl overflow-x-auto">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>📊</span> おすすめ時間停止神作TOP5 徹底スペック比較表
  </h3>
  <table class="w-full text-left text-xs md:text-sm text-slate-300">
    <thead class="bg-slate-800/80 text-indigo-300 uppercase font-bold border-b border-slate-700">
      <tr>
        <th class="p-3">順位・タイトル</th>
        <th class="p-3">主演女優</th>
        <th class="p-3">停止シチュエーション・特徴</th>
        <th class="p-3">全能感・実用度</th>
        <th class="p-3">公式リンク</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-slate-800">
      <tr class="hover:bg-slate-800/40">
        <td class="p-3 font-bold text-white">第1位：さくらってリア充で幸せそうだから</td>
        <td class="p-3">水卜さくら</td>
        <td class="p-3">日常デート中フリーズ・解除絶頂フラッシュ</td>
        <td class="p-3 text-indigo-400 font-bold">★★★★★ (120%)</td>
        <td class="p-3"><a href="/posts/mida00558" class="text-indigo-400 hover:underline">詳細</a></td>
      </tr>
      <tr class="hover:bg-slate-800/40">
        <td class="p-3 font-bold text-white">第2位：ギャルコンビ時間停止</td>
        <td class="p-3">恋渕ももな×星乃莉子</td>
        <td class="p-3">コンビニ制服悪態ギャル懲らしめ・同時中出し</td>
        <td class="p-3 text-indigo-400 font-bold">★★★★★ (115%)</td>
        <td class="p-3"><a href="/posts/1start00518" class="text-indigo-400 hover:underline">詳細</a></td>
      </tr>
      <tr class="hover:bg-slate-800/40">
        <td class="p-3 font-bold text-white">第3位：【VR】【8K】時間停止VR</td>
        <td class="p-3">神木麗</td>
        <td class="p-3">8Kゼロ距離VR・神ボディ完全マネキン化</td>
        <td class="p-3 text-indigo-400 font-bold">★★★★★ (125%)</td>
        <td class="p-3"><a href="/posts/13dsvr01944" class="text-indigo-400 hover:underline">詳細</a></td>
      </tr>
      <tr class="hover:bg-slate-800/40">
        <td class="p-3 font-bold text-white">第4位：鉄拳精裁ストップマン</td>
        <td class="p-3">黒川すみれ</td>
        <td class="p-3">人気同人実写化・サイコ美女への時間停止屈服</td>
        <td class="p-3 text-indigo-400 font-bold">★★★★★ (110%)</td>
        <td class="p-3"><a href="/posts/mimk00122" class="text-indigo-400 hover:underline">詳細</a></td>
      </tr>
      <tr class="hover:bg-slate-800/40">
        <td class="p-3 font-bold text-white">第5位：時間停止学級。神装置で挿れ放題</td>
        <td class="p-3">SODセレクト</td>
        <td class="p-3">教室・体育館・日常空間やりたい放題イタズラ</td>
        <td class="p-3 text-indigo-400 font-bold">★★★★★ (115%)</td>
        <td class="p-3"><a href="/posts/hsoda00004" class="text-indigo-400 hover:underline">詳細</a></td>
      </tr>
    </tbody>
  </table>
</div>

<!-- 関連記事・内部リンク -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>🔗</span> あわせて読みたい！おすすめの超人気キラー特集記事
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs md:text-sm">
    <a href="/posts/feature_fanza_common_sense_alteration_hypnosis_ranking" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-indigo-500/50 transition block">
      <div class="font-bold text-indigo-300 mb-1">【常識改変・催眠洗脳】おすすめ殿堂入り神作TOP5</div>
      <p class="text-slate-400 line-clamp-2">倫理観崩壊で恥じらいゼロの美少女たちがチンポを奪い合う背徳ファンタジー傑作選！</p>
    </a>
    <a href="/posts/feature_fanza_vr_8k_ultra_immersive_best_ranking" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-purple-500/50 transition block">
      <div class="font-bold text-purple-300 mb-1">【8K圧倒的没入感】FANZA VR動画おすすめ殿堂入り神作TOP5</div>
      <p class="text-slate-400 line-clamp-2">Meta Quest対応！至近距離ゼロ距離密着で脳がバグるバーチャル名作選！</p>
    </a>
    <a href="/posts/feature_fanza_reverse_rape_forced_ejaculation_cowgirl_ranking_2026" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-pink-500/50 transition block">
      <div class="font-bold text-pink-300 mb-1">【男が犯される極限快楽】逆レイプ・連続強制搾精・腰振り騎乗位TOP5</div>
      <p class="text-slate-400 line-clamp-2">肉食美女に拘束され射精後も逃げ場ゼロで金玉が空になるまで搾り取られるドM昇天AV選！</p>
    </a>
    <a href="/posts/feature_fanza_gyaru_tanned_bitch_reverse_sperm_drain_ranking_2026" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-pink-400/50 transition block">
      <div class="font-bold text-pink-300 mb-1">【生意気メスガキ＆極上腰振り】ギャル・黒ギャル・ビッチ搾精TOP5</div>
      <p class="text-slate-400 line-clamp-2">派手髪ネイルの肉食ギャルが「ざぁ〜こ♡」と煽りながら骨抜きにする至高のギャルハメAV選！</p>
    </a>
  </div>
</div>

<!-- よくある質問（FAQ） -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>❓</span> 時間停止AVに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-4 text-xs md:text-sm">
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-indigo-300 mb-2">Q1. 時間停止AVの一番の抜きどころ・興奮ポイントは？</h4>
      <p class="text-slate-300 leading-relaxed">時間を止めた状態での無防備ないたずらと、時間を解除した瞬間に一気に快楽と精液の熱さが伝わって美女が白目を剥く「解除アクメ」です。</p>
    </div>
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-indigo-300 mb-2">Q2. 最もリアルで圧倒的な臨場感を味わえる作品は？</h4>
      <p class="text-slate-300 leading-relaxed">第3位の神木麗主演『時間停止VR』（13DSVR-01944）です。8K高画質で神木麗が目の前でマネキン化し、ゼロ距離で触れ合うVR体験は異次元です。</p>
    </div>
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-indigo-300 mb-2">Q3. 美少女の無防備な表情と切ないエロスを楽しむなら？</h4>
      <p class="text-slate-300 leading-relaxed">第1位の水卜さくら主演作（MIDA-0558）が最適です。透明感抜群の美少女がリア充の日常から突如時間を止められて弄ばれる背徳感が満点です。</p>
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
                "name": "FANZA「時間停止・タイムストップ＆無防備中出し」おすすめ神作ランキングTOP5",
                "description": "ピタリと静止した無防備美女を弄び尽くし時間解除と同時に限界アクメさせる至高のファンタジーAV選【2026年最新】",
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
                        "name": "時間停止AVの一番の抜きどころ・興奮ポイントは？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "時間を止めた状態での無防備ないたずらと、時間を解除した瞬間に一気に快楽と精液の熱さが伝わって美女が白目を剥く「解除アクメ」です。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "最もリアルで圧倒的な臨場感を味わえる作品は？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第3位の神木麗主演『時間停止VR』（13DSVR-01944）です。8K高画質で神木麗が目の前でマネキン化し、ゼロ距離で触れ合うVR体験は異次元です。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "美少女の無防備な表情と切ないエロスを楽しむなら？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第1位の水卜さくら主演作（MIDA-0558）が最適です。透明感抜群の美少女がリア充の日常から突如時間を止められて弄ばれる背徳感が満点です。"
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
        "id": "feature_fanza_time_stop_freeze_unprotected_creampie_ranking_2026",
        "title": "【男の究極妄想・やりたい放題】FANZA「時間停止・タイムストップ＆無防備中出し」おすすめ神作ランキングTOP5！ピタリと静止した無防備美女を弄び尽くし時間解除と同時に限界アクメさせる至高のファンタジーAV選【2026年最新】",
        "date": "2026-10-05 23:55:00",
        "hinban": "TIME-STOP-FREEZE-CREAMPIE-2026",
        "price": "300~",
        "maker": "FANZA公式セレクション",
        "actresses": ["水卜さくら", "恋渕ももな", "星乃莉子", "神木麗", "黒川すみれ"],
        "genres": ["時間停止", "イタズラ", "無防備", "中出し", "美少女", "VR", "ファンタジー", "特集", "殿堂入り"],
        "image": cover_image,
        "review": full_html
    }

    file_path = os.path.join(OUTPUT_DIR, f"{post_data['id']}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f" -> Successfully saved Article 2 ({char_count} chars) to {file_path}")


# ==============================================================================
# 記事3: ガチハメ撮り・スマホ個人撮影＆素人流出風 特化
# ==============================================================================
def generate_article_hametori():
    print("=== Generating Article 3: ガチハメ撮り・スマホ個人撮影＆素人流出風 特化 ===")
    cids = ["ssis00875", "midv00609", "snos00312", "ajsp00001", "mida00812"]
    items = []
    for cid in cids:
        it = fetch_fanza_item(cid)
        if it:
            items.append(it)
            generate_individual_post_if_needed(it, ["ハメ撮り", "個人撮影", "素人", "スマホ", "プライベート", "殿堂入り"])
            print(f" -> Fetched: {cid} ({it.get('title')[:30]})")
        time.sleep(0.3)

    if len(items) < 5:
        raise Exception(f"Failed to fetch 5 items for Article 3 (got {len(items)})")

    cover_image = items[0].get("imageURL", {}).get("large", "")
    html_parts = []

    intro_html = f"""<div class="my-8 bg-gradient-to-br from-emerald-950/40 via-slate-900 to-slate-950 border border-emerald-500/30 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-10 -right-10 w-48 h-48 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="flex items-center gap-3 mb-4">
    <span class="bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 px-3 py-1 rounded-full text-xs font-black tracking-wider uppercase">REAL HAMETORI & PRIVATE LEAK SPECIAL</span>
    <span class="text-slate-400 text-xs">更新日：2026年10月06日</span>
  </div>
  <h2 class="text-2xl md:text-3xl font-black text-white leading-tight mb-4 tracking-tight">
    【生々しすぎる密室プライベート】FANZA「ガチハメ撮り・スマホ個人撮影＆素人流出風」おすすめ神作ランキングTOP5！作られた演技ゼロの生々しい喘ぎと無防備なアヘ顔に興奮が止まらない至高のリアル交尾AV選【2026年最新】
  </h2>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    スタジオ撮影の豪華な照明や凝ったカメラワーク、作られた演出では決して味わえない究極のリアルエロス、それが「ガチハメ撮り・スマホ個人撮影・密室流出風モノ」です。ホテルの薄暗いベッドルームやアパートのワンルーム、片手に持ったスマートフォンやハンディカム1台だけで記録された映像には、女優たちがプロとしての鎧を脱ぎ捨て、ひとりの女として本能の性欲に溺れていく生々しい姿が刻み込まれています。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed mb-4">
    「恥ずかしいからカメラ向けないでよぉ…」と照れながらシーツに顔を埋める無防備な笑顔。しかしひとたび愛撫が始まると、カメラの存在を忘れて吐息を熱くし、濡れそぼる秘部から溢れ出す愛液のぬめり、耳元で響くリアルな水音と粘膜の擦れ合い。「撮りながら中に挿れて…」「私の顔見ながらいっぱい出して…」とカメラ越しに目を合わせながら腰を突き上げられる主観目線は、まるで自分が美女と二人きりで生交尾しているかのような圧倒的没入感を与えます。
  </p>
  <p class="text-slate-300 text-sm md:text-base leading-relaxed">
    本記事では、新時代No.1トップ女優・河北彩花が二人きりの密室で素の性欲を解き放つ歴史的ハメ撮り作から、石川澪の超プライベートガチイキ濃密セックス、渚あいりのSNSマッチングアプリ逢瀬ハメ撮りドキュメント、枢木あおいのリアルスマホ縦撮り彼女の友達生ハメ、そして話題沸騰の超美少女・平野楓の無防備個撮デビューまで、リアリティと実用度で右に出るもののない【ガチハメ撮り神作TOP5】を徹底比較・レビューします！
  </p>
</div>

<!-- 選び方の基準 -->
<div class="my-8 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span class="text-emerald-400">📱</span> ガチハメ撮り作品で圧倒的リアル絶頂を迎える3大チェックポイント
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-emerald-300 mb-2">① カメラを意識した羞恥心から素の快楽へ崩れる表情</h4>
      <p class="text-slate-300 leading-relaxed">「撮らないで」と手で顔を覆っていた美女が、快感に耐えきれずカメラ目線でアヘ顔を晒してヨガるリアルな表情変化が最大のシコりどころです。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-emerald-300 mb-2">② 作られた演出ゼロの生々しい肉体衝突音と汁音</h4>
      <p class="text-slate-300 leading-relaxed">マイクの加工がないからこそ響く、腰と腰がぶつかる鈍い音、ぐちゅぐちゅと泡立つ粘膜の擦れ合い、生々しい吐息の臨場感が聴覚をダイレクトに直撃します。</p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/60">
      <h4 class="font-bold text-emerald-300 mb-2">③ スマホ縦画面や手ブレがもたらす完全主観没入</h4>
      <p class="text-slate-300 leading-relaxed">スマホ画面いっぱいに広がる縦撮り映像や片手撮影特有の揺れが、「自分自身のスマホに保存された流出動画」のような錯覚をもたらし射精圧を高めます。</p>
    </div>
  </div>
</div>

<!-- 目次 -->
<div class="my-8 bg-slate-900/60 border border-slate-800 rounded-2xl p-5 shadow-inner">
  <h4 class="text-sm font-bold text-slate-300 mb-3 flex items-center gap-2">
    <span>📑</span> 目次：おすすめランキングTOP5
  </h4>
  <ul class="space-y-2 text-xs md:text-sm text-emerald-400/90 font-medium">
    <li><a href="#rank-1" class="hover:underline flex items-center justify-between"><span>第1位：河北彩花の完全プライベートセックス全部撮った！（河北彩花）</span><span class="text-slate-500 text-xs">トップ女優の素顔ハメ撮り</span></a></li>
    <li><a href="#rank-2" class="hover:underline flex items-center justify-between"><span>第2位：人気女優の超プライベート映像！ガチイキ生々ハメ撮り（石川澪）</span><span class="text-slate-500 text-xs">二人きりの完全密着</span></a></li>
    <li><a href="#rank-3" class="hover:underline flex items-center justify-between"><span>第3位：AV女優がSNSで一般男性とマッチング（渚あいり）</span><span class="text-slate-500 text-xs">ガチアポ素人交尾ドキュメント</span></a></li>
    <li><a href="#rank-4" class="hover:underline flex items-center justify-between"><span>第4位：【スマホ推奨】彼女の友達とハメまくった記録（枢木あおい）</span><span class="text-slate-500 text-xs">スマホ全画面縦撮り生中出し</span></a></li>
    <li><a href="#rank-5" class="hover:underline flex items-center justify-between"><span>第5位：尊すぎる原石 最強幼ビジュAV DEBUT（平野楓）</span><span class="text-slate-500 text-xs">初々しいウブ娘の密室個撮</span></a></li>
  </ul>
</div>"""
    html_parts.append(intro_html)

    # ランキング5作品詳細
    for idx, it in enumerate(items):
        cid = it.get("content_id")
        title = it.get("title")
        acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        act_links = " ".join([get_actress_link(a) for a in acts])
        genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
        genre_links = " ".join([get_genre_link(g) for g in genres[:5]])
        hinban = cid.upper()
        aff_url = it.get("affiliate_url_clean")
        img_large = it.get("imageURL", {}).get("large")
        s_imgs = get_sample_images(it, 4)

        rank_num = idx + 1
        rank_badge = f'<span class="bg-gradient-to-r from-emerald-500 to-teal-400 text-slate-950 text-sm md:text-base font-black px-4 py-1 rounded-full shadow-lg">第{rank_num}位（殿堂入り）</span>' if rank_num == 1 else f'<span class="bg-slate-700 text-emerald-300 text-sm md:text-base font-black px-4 py-1 rounded-full">第{rank_num}位</span>'

        rev_html = INDIVIDUAL_REVIEWS.get(cid, "")
        clean_rev = re.sub(r'<h2>.*?</h2>', '', rev_html)

        sample_imgs_html = ""
        if s_imgs:
            imgs_tags = "".join([f'<img src="{sim}" alt="サンプル画像" class="rounded-lg border border-slate-800 object-cover w-full h-28" loading="lazy" />' for sim in s_imgs])
            sample_imgs_html = f'<div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-6">{imgs_tags}</div>'

        item_card = f"""<div id="rank-{rank_num}" class="my-10 bg-slate-900 border {'border-2 border-emerald-500/40' if rank_num == 1 else 'border-slate-800'} rounded-2xl p-6 md:p-8 shadow-2xl relative">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-3">
      {rank_badge}
      <h3 class="text-lg md:text-2xl font-black text-white">{title}</h3>
    </div>
    <div class="text-xs text-slate-400">品番：{hinban} / 出演：{act_links}</div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <div class="space-y-4">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block group relative overflow-hidden rounded-xl border border-slate-700">
        <img src="{img_large}" alt="{title}" class="w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-4">
          <span class="text-white text-xs font-bold bg-emerald-600/90 px-3 py-1 rounded-full">FANZA公式で作品詳細を見る →</span>
        </div>
      </a>
      <div class="flex flex-wrap gap-2">
        {genre_links}
      </div>
    </div>
    <div class="space-y-4 text-xs md:text-sm text-slate-300 leading-relaxed">
      {clean_rev}
      <div class="pt-2">
        <a href="/posts/{cid}" class="text-xs text-emerald-400 hover:text-emerald-300 underline font-bold">👉 作品個別ページ（サンプル画像・詳細レビュー）を見る</a>
      </div>
    </div>
  </div>

  {sample_imgs_html}

  <div class="text-center">
    <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="inline-flex items-center justify-center gap-2 bg-gradient-to-r from-emerald-500 via-teal-500 to-emerald-500 hover:opacity-95 text-white font-black text-sm md:text-base px-8 py-4 rounded-xl shadow-xl transition transform hover:scale-105">
      <span>今すぐFANZA公式で『{title[:20]}…』をフル視聴する</span>
      <span>🚀</span>
    </a>
  </div>
</div>"""
        html_parts.append(item_card)

    table_and_links = """<!-- スペック比較まとめ表 -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl overflow-x-auto">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>📊</span> おすすめガチハメ撮り神作TOP5 徹底スペック比較表
  </h3>
  <table class="w-full text-left text-xs md:text-sm text-slate-300">
    <thead class="bg-slate-800/80 text-emerald-300 uppercase font-bold border-b border-slate-700">
      <tr>
        <th class="p-3">順位・タイトル</th>
        <th class="p-3">主演女優</th>
        <th class="p-3">撮影スタイル・リアル感</th>
        <th class="p-3">シコり度・実用度</th>
        <th class="p-3">公式リンク</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-slate-800">
      <tr class="hover:bg-slate-800/40">
        <td class="p-3 font-bold text-white">第1位：河北彩花の完全プライベートセックス</td>
        <td class="p-3">河北彩花</td>
        <td class="p-3">ホテル2人きり密着・ハンディカメラ生々撮影</td>
        <td class="p-3 text-emerald-400 font-bold">★★★★★ (130%)</td>
        <td class="p-3"><a href="/posts/ssis00875" class="text-emerald-400 hover:underline">詳細</a></td>
      </tr>
      <tr class="hover:bg-slate-800/40">
        <td class="p-3 font-bold text-white">第2位：人気女優の超プライベート映像</td>
        <td class="p-3">石川澪</td>
        <td class="p-3">完全プライベート・ガチイキ濃密交尾</td>
        <td class="p-3 text-emerald-400 font-bold">★★★★★ (120%)</td>
        <td class="p-3"><a href="/posts/midv00609" class="text-emerald-400 hover:underline">詳細</a></td>
      </tr>
      <tr class="hover:bg-slate-800/40">
        <td class="p-3 font-bold text-white">第3位：AV女優がSNSでマッチング</td>
        <td class="p-3">渚あいり</td>
        <td class="p-3">マッチングアプリガチアポ・素人男子交尾ドキュメント</td>
        <td class="p-3 text-emerald-400 font-bold">★★★★★ (115%)</td>
        <td class="p-3"><a href="/posts/snos00312" class="text-emerald-400 hover:underline">詳細</a></td>
      </tr>
      <tr class="hover:bg-slate-800/40">
        <td class="p-3 font-bold text-white">第4位：【スマホ推奨】彼女の友達とハメまくった記録</td>
        <td class="p-3">枢木あおい</td>
        <td class="p-3">スマホ縦画面フル表示・背徳浮気生中出し</td>
        <td class="p-3 text-emerald-400 font-bold">★★★★★ (115%)</td>
        <td class="p-3"><a href="/posts/ajsp00001" class="text-emerald-400 hover:underline">詳細</a></td>
      </tr>
      <tr class="hover:bg-slate-800/40">
        <td class="p-3 font-bold text-white">第5位：尊すぎる原石 最強幼ビジュAV DEBUT</td>
        <td class="p-3">平野楓</td>
        <td class="p-3">ウブ美少女初体験・密室個撮ドキュメント</td>
        <td class="p-3 text-emerald-400 font-bold">★★★★★ (110%)</td>
        <td class="p-3"><a href="/posts/mida00812" class="text-emerald-400 hover:underline">詳細</a></td>
      </tr>
    </tbody>
  </table>
</div>

<!-- 関連記事・内部リンク -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>🔗</span> あわせて読みたい！おすすめの超人気キラー特集記事
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs md:text-sm">
    <a href="/posts/feature_fanza_pov_subjective_immersion_masterpiece_ranking" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-emerald-500/50 transition block">
      <div class="font-bold text-emerald-300 mb-1">【極上の密着・耳元吐息】主観・POVおすすめ殿堂入り神作TOP5</div>
      <p class="text-slate-400 line-clamp-2">ゼロ距離キスと見つめ合い生ハメで脳がバグる圧倒的没入感傑作選！</p>
    </a>
    <a href="/posts/feature_fanza_magic_mirror_go_real_amateur_best_ranking" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-amber-500/50 transition block">
      <div class="font-bold text-amber-300 mb-1">【25年売れ続ける伝説】マジックミラー号＆リアル素人ナンパ傑作選</div>
      <p class="text-slate-400 line-clamp-2">生々しい恥じらいと本気アクメに悶絶する歴代神回ランキング！</p>
    </a>
    <a href="/posts/feature_fanza_gyaru_tanned_bitch_reverse_sperm_drain_ranking_2026" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-pink-500/50 transition block">
      <div class="font-bold text-pink-300 mb-1">【生意気メスガキ＆極上腰振り】ギャル・黒ギャル・ビッチ搾精TOP5</div>
      <p class="text-slate-400 line-clamp-2">派手髪ネイルの肉食ギャルが「ざぁ〜こ♡」と煽りながら骨抜きにする至高のギャルハメAV選！</p>
    </a>
    <a href="/posts/feature_fanza_time_stop_freeze_unprotected_creampie_ranking_2026" class="p-4 bg-slate-800/60 hover:bg-slate-800 rounded-xl border border-slate-700/60 hover:border-indigo-500/50 transition block">
      <div class="font-bold text-indigo-300 mb-1">【男の究極妄想・やりたい放題】時間停止・タイムストップ＆無防備中出しTOP5</div>
      <p class="text-slate-400 line-clamp-2">ピタリと静止した無防備美女を弄び尽くし時間解除と同時に限界アクメさせる至高のAV選！</p>
    </a>
  </div>
</div>

<!-- よくある質問（FAQ） -->
<div class="my-10 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
  <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
    <span>❓</span> ガチハメ撮りAVに関するよくある質問（FAQ）
  </h3>
  <div class="space-y-4 text-xs md:text-sm">
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-emerald-300 mb-2">Q1. ガチハメ撮り作品と通常のAVの最大の違いは何ですか？</h4>
      <p class="text-slate-300 leading-relaxed">演出や決められた台本、派手な照明がなく、女優の自然な反応、生々しい吐息、手持ちカメラ特有の至近距離アングルで本物の密会を覗き見している感覚になれる点です。</p>
    </div>
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-emerald-300 mb-2">Q2. スマホで観るのに最も適したハメ撮り作品は？</h4>
      <p class="text-slate-300 leading-relaxed">第4位の枢木あおい主演作（AJSP-00001）です。スマホ縦画面フルサイズで鑑賞できるように制作されており、自分のスマホで流出動画を見ているような超リアルな体験が可能です。</p>
    </div>
    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/50">
      <h4 class="font-bold text-emerald-300 mb-2">Q3. トップ女優の素顔や本気エロスを味わいたいなら？</h4>
      <p class="text-slate-300 leading-relaxed">第1位の河北彩花主演作（SSIS-00875）です。業界No.1女優がカメラを忘れて男に甘え、本能のまま乱れるプライベートセックスは全ファン必見です。</p>
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
                "name": "FANZA「ガチハメ撮り・スマホ個人撮影＆素人流出風」おすすめ神作ランキングTOP5",
                "description": "作られた演技ゼロの生々しい喘ぎと無防備なアヘ顔に興奮が止まらない至高のリアル交尾AV選【2026年最新】",
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
                        "name": "ガチハメ撮り作品と通常のAVの最大の違いは何ですか？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "演出や決められた台本、派手な照明がなく、女優の自然な反応、生々しい吐息、手持ちカメラ特有の至近距離アングルで本物の密会を覗き見している感覚になれる点です。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "スマホで観るのに最も適したハメ撮り作品は？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第4位の枢木あおい主演作（AJSP-00001）です。スマホ縦画面フルサイズで鑑賞できるように制作されており、自分のスマホで流出動画を見ているような超リアルな体験が可能です。"
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "トップ女優の素顔や本気エロスを味わいたいなら？",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "第1位の河北彩花主演作（SSIS-00875）です。業界No.1女優がカメラを忘れて男に甘え、本能のまま乱れるプライベートセックスは全ファン必見です。"
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
        "id": "feature_fanza_hametori_smartphone_private_leak_ranking_2026",
        "title": "【生々しすぎる密室プライベート】FANZA「ガチハメ撮り・スマホ個人撮影＆素人流出風」おすすめ神作ランキングTOP5！作られた演技ゼロの生々しい喘ぎと無防備なアヘ顔に興奮が止まらない至高のリアル交尾AV選【2026年最新】",
        "date": "2026-10-06 00:00:00",
        "hinban": "HAMETORI-SMARTPHONE-LEAK-2026",
        "price": "300~",
        "maker": "FANZA公式セレクション",
        "actresses": ["河北彩花（河北彩伽）", "石川澪", "渚あいり", "枢木あおい", "平野楓"],
        "genres": ["ハメ撮り", "個人撮影", "素人", "スマホ", "主観", "中出し", "ドキュメンタリー", "特集", "殿堂入り"],
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
    generate_article_gyaru()
    print("--------------------------------------------------")
    generate_article_time_stop()
    print("--------------------------------------------------")
    generate_article_hametori()
    print("==================================================")
    print("3記事すべての生成が正常に完了しました！")
    print("==================================================")

if __name__ == "__main__":
    main()
