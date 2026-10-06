# -*- coding: utf-8 -*-
"""
FANZA公式APIリアルタイム取得・新規キラー特集3記事自動生成スクリプト v2
1. 【白ギャル・清楚系ギャル特化】
   『【男ウケ最強の透き通る素肌とあざとさ】FANZA「白ギャル・清楚系ギャル」おすすめ神作ランキングTOP5！色白モチ肌×明るい茶髪×神対応イチャラブで男を沼らせる至高の傑作選【2026年最新】』
2. 【童貞狩り・積極的肉食お姉さん特化】
   『【ウブな男の子を骨抜きに貪り尽くす】FANZA「童貞狩り・積極的肉食お姉さん」おすすめ神作ランキングTOP5！からかい寸止めから生ハメ主導権掌握まで理性を狂わせる至高の搾精傑作選【2026年最新】』
3. 【元カノ・再会未練セックス特化】
   『【昔付き合っていたあの子と数年ぶりの再会】FANZA「元カノ・未練と衝動の再会セックス」おすすめ神作ランキングTOP5！大人の色気をまとった元恋人とホテルで貪り合う至高の背徳名作選【2026年最新】』
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
    # 記事1: 白ギャル・清楚系ギャル特化
    "midv00927": """<h2>『宿題代行するだけでおま○こ貸してくれる入り浸り幼馴染ギャル SEXのハードルが低すぎて調子に乗って20発も中出ししまくった話 石原希望』詳細レビュー</h2>
<p>天性の明るさと底抜けの可愛さで男性ファンを魅了し続けるトップ女優・石原希望が、「部屋に入り浸る都合の良すぎる幼馴染白ギャル」を演じた大傑作です。金髪に近い明るい茶髪に透き通るような白い素肌、そして部屋着のショートパンツから覗く健康的な太ももが、男の妄想を最初からクライマックスへと導きます。「宿題やってくれたら、エッチなことさせてあげるよ？」という軽すぎるノリから始まり、次第に本能むき出しの交わりへと発展していく展開が最高に刺激的です。</p>

<h3>見どころ：飾らない笑顔と「エッチ大好きな素直さ」が男心を直撃</h3>
<p>黒ギャルとは一味違う、色白モチ肌に抜け感のあるナチュラルメイクが石原希望の抜群の美貌を際立たせています。「ねえ、まだ宿題終わんないの？待ちくたびれちゃった」「早くシよ？」と無防備に甘えてくる仕草は、どんな男でも理性が吹き飛ぶ破壊力です。ベッドに倒れ込んだ瞬間に見せる悪戯っぽい笑顔と、唇を重ねた瞬間に漏れる熱い吐息のギャップに心を完全に奪われます。</p>

<h3>実用ポイント：ピストンに合わせて乱れ狂う愛らしい嬌声と追撃の腰振り</h3>
<p>結合した瞬間、石原希望の表情は快楽に染まり、白肌をほんのりピンク色に上気させながら「あっ…すごい、奥まで当たってる…！」と腰を跳ね上げます。正常位で密着しながら見つめ合ってピストンを繰り返すシーンでは、彼女の愛くるしい顔が至近距離で喘ぎ狂い、射精の瞬間まで目を離せません。さらに射精後も「まだまだ出せるでしょ？」と跨がって腰を振ってくる濃厚な追撃プレイは、抜きやすさにおいてトップクラスの実力を誇ります。</p>""",

    "1stars00836": """<h2>『ノリ良し、顔良し、都合良し。最高にシコい愛人ギャルと朝までヤリ倒す。 小倉由菜』詳細レビュー</h2>
<p>圧倒的なビジュアルとキュートなハスキーボイスで絶大な支持を集める小倉由菜が、男の都合に合わせていつでも部屋にやってきては快楽を与えてくれる「完璧すぎる愛人白ギャル」に扮した名作。日焼けしていない透き通るような白肌に、絶妙に垢抜けたヘアメイクがマッチし、清潔感とスケベさが奇跡のバランスで同居しています。</p>

<h3>見どころ：ノリの軽さと抜群の包容力が生み出す究極の居心地</h3>
<p>チャイムが鳴ってドアを開けると、満面の笑顔で「お待たせ〜！会いたかったよ♡」と抱きついてくる小倉由菜。缶ビールを片手に他愛のない会話で盛り上がり、そのまま自然な流れでソファーになだれ込む導入は、全男性の憧れるシチュエーションそのものです。彼女の屈託のない笑顔と、耳元で囁かれる甘い淫語のコンビネーションが脳を心地よく麻痺させます。</p>

<h3>実用ポイント：ソファーやベッドで繰り広げられる体位無制限の連続交尾</h3>
<p>ショート丈の服をたくし上げ、パンツを横にずらしただけの半脱ぎ状態で始まるソファーセックス。小倉由菜の引き締まったウエストと美尻が激しく揺れ、奥を突かれるたびに「んっ、ああっ…そこ気持ちいい…！」と舌を出しながら恍惚の表情を浮かべます。男の欲望を一切否定せず、朝を迎えるまで何度でも求めに応じてくれる贅沢な交わりは、溜まった性欲を根こそぎ解き放つ決定打となります。</p>""",

    "cjod00494": """<h2>『白ギャルエースモカちんが無制限中出しOK！ヒミツの風俗学園フルコースで痴女られたボク 春陽モカ』詳細レビュー</h2>
<p>白ギャル界の若きカリスマとして名高い春陽モカが、秘密の風俗学園で無制限中出しサービスを提供する特級キャストとして登場。透明感のある白い素肌とスラリと伸びる美脚、そして何より「男をイカせるのが大好き」というドスケベなサービス精神が画面全体から溢れ出る、実用度特化の傑作です。</p>

<h3>見どころ：あざといギャル語と超積極的なフェラ奉仕</h3>
<p>「ウチのテクで一瞬で昇天させてあげるから覚悟してね？」と生意気そうに微笑みながら、膝立ちになってペニスを丁寧に舐め上げていく春陽モカ。大きな瞳で上目遣いに見つめながら、亀頭から竿、金玉まで余すところなく舌を這わせる濃厚なバキュームフェラは圧巻です。ジュポジュポと響く水音と、喉奥深くまで咥え込むプロフェッショナルな奉仕に男の腰は浮きっぱなしになります。</p>

<h3>実用ポイント：無制限中出しが生み出す背徳感と子宮直撃ピストン</h3>
<p>「中にいっぱい出していいよ♡モカの中でドクドク出して！」と太ももを大きく広げて誘惑してくる春陽モカ。狭い膣内が吸い付くようにペニスを締め付け、奥を激しく突くたびに彼女の身体が小刻みに痙攣します。ゴムなしで直に伝わる温もりと、射精後にペニスを抜いた瞬間にとろりと溢れ出る精液のコントラストは、強烈な征服感と快感をもたらします。</p>""",

    "1svgal00001": """<h2>『罰ゲームで童貞狩りにやってきたクラスメイトの白ギャルJ〇が陰キャな僕のデカチンに「超どハマり！」何回も… 逢月ひまり』詳細レビュー</h2>
<p>透き通るような白肌とあどけない美貌を持つ逢月ひまりが、クラスの罰ゲームをきっかけに陰キャ男子の自宅を訪れ、隠されたデカチンに夢中になって自らハメ狂ってしまうという王道ギャルシチュエーション。最初はからかうような軽い気持ちだった白ギャルが、快楽の沼にハマってメスの顔へと変貌していくグラデーションが見事に描かれています。</p>

<h3>見どころ：からかいから本気の中毒へと堕ちていく表情の変遷</h3>
<p>「ちょっと見せてみなよ〜」と軽いノリでズボンを下ろした逢月ひまりが、予想外の巨大なモノを前にして息を呑み、瞳を潤ませるリアクションが秀逸です。恐る恐る触れていた手つきが次第に熱を帯び、自分から下着を脱ぎ捨てて跨がっていく積極性へとシフト。ギャルの強気なプライドが快感によって心地よく崩壊していく過程に興奮が止まりません。</p>

<h3>実用ポイント：我を忘れて腰を打ち付けまくる杭打ち騎乗位</h3>
<p>ベッドの上で陰キャ男子の上に跨がり、大きなペニスを膣奥深くまで飲み込んでいく逢月ひまり。あまりの快感に「やばっ…これすごい…頭おかしくなりそう…！」と口元を緩め、激しく腰を上下させる杭打ち騎乗位は圧巻の迫力です。清楚で可憐なルックスの白ギャルが、快楽に負けてなりふり構わず腰を振り乱す姿は、視聴者の射精欲を限界まで昂らせます。</p>""",

    "mida00546": """<h2>『終電後僕の部屋に入り浸りギャル 4次会ビッ痴酔いパーティ 密着ヌルッヌルッのローション風呂ナイトプールごっこで朝までブッ続け生中出し 松本いちか 春陽モカ』詳細レビュー</h2>
<p>当代屈指の人気を誇る小悪魔白ギャルの松本いちかと、美脚スレンダー白ギャルの春陽モカという奇跡のWキャスト。飲み会の終電を逃した2人が部屋になだれ込み、お酒の勢いとノリの良さで密着ローション風呂から朝までの乱交生ハメへと雪崩れ込む、男の妄想の極致を具現化した超豪華作品です。</p>

<h3>見どころ：白ギャル2人に囲まれる圧倒的多幸感とお風呂イチャラブ</h3>
<p>狭いお風呂場にローションを流し込み、「ナイトプールごっこしよ〜！」と水着や下着姿で身体を密着させてくる2人の白ギャル。左右からモチモチの柔肌を押し付けられ、滑らかなローション越しにペニスを手や太ももで挟み込まれるハーレムシチュエーションは夢のような刺激です。松本いちかのあざとい淫語と春陽モカの妖艶な視線が絡み合い、息つく暇もありません。</p>

<h3>実用ポイント：左右交互に味わう贅沢極まる中出しサンドイッチ</h3>
<p>浴室からベッドへと場所を移し、2人の白ギャルを交互に貪り尽くす本番シーン。松本いちかの小柄で締まりの良い膣内を突き上げた直後、春陽モカの長い美脚を担ぎ上げて奥深くまで貫く贅沢さは言葉を失います。2人が見つめ合いながら「次ウチの番ね♡」「もっと奥までちょうだい」と交代で腰を求めてくる展開は、一滴残らず精子を吸い尽くされる破壊力を秘めています。</p>""",

    # 記事2: 童貞狩り・積極的肉食お姉さん特化
    "cawd00827": """<h2>『「童貞請負人」の異名を持つ童貞を愛して止まない私がまさか絶倫童貞に敗北キメセク中出し堕ちするなんて… 伊藤舞雪』詳細レビュー</h2>
<p>グラマラスな神ボディと大人の色香で男性を圧倒する伊藤舞雪が、「童貞のウブな反応を愛してやまない童貞請負人」を熱演。経験のない男子を優しく、そしてサディスティックにからかいながら手玉に取るはずが、男子の底なしの性欲と持久力に圧倒され、自らが快楽に溺れていく逆転のドラマが描かれた屈指の名作です。</p>

<h3>見どころ：余裕たっぷりの大人の色香からメスへの屈服劇</h3>
<p>「童貞くん、そんなに緊張しなくていいんだよ？」と妖艶な微笑みを浮かべ、耳元に吐息を吹きかけながら身体の隅々まで弄んでいく伊藤舞雪。豊満なFカップバストを押し付け、巧みな舌遣いで翻弄する序盤の主導権掌握っぷりはゾクゾクする色気を放ちます。しかし男子が勃起を収めずに激しく突き上げ始めると、次第に瞳がトロンと溶け、喘ぎ声が本気になっていくギャップがたまりません。</p>

<h3>実用ポイント：神乳が揺れまくる濃厚密着交尾と連続絶頂</h3>
<p>男子に上から組み敷かれ、力強くピストンされるたびに伊藤舞雪の豊満な胸が激しく波打ちます。「待って、童貞のくせに激しすぎる…！ああっ、もうダメ…！」と普段の余裕を完全に失い、子宮を突かれて白目を剥いてアクメに達する姿は至高のエロティシズム。主導権を握っていたはずの美女が快感で壊れていく姿は、男の征服欲をこれ以上ないほど満たします。</p>""",

    "bacj00064": """<h2>『童貞の教え子を誘惑して弄ぶために教師になりました 岬さくら』詳細レビュー</h2>
<p>知的な眼鏡とタイトなスーツに身を包んだ美人教師・岬さくらが、「教え子のウブな童貞を奪って狂わせる」という歪んだ性癖を遺憾なく発揮する背徳の名作。放課後の静まり返る準備室で、真面目な生徒を密室に呼び出し、抗えない大人の色気でじわじわと理性を侵食していく心理描写が極めて生々しく描かれます。</p>

<h3>見どころ：密室の背徳感とからかい寸止めの焦らしプレイ</h3>
<p>「先生のスカートの中、見てみたい？」とタイトスカートの裾をゆっくりとたくし上げ、黒ストッキングに包まれた太ももを教え子の目の前に晒す岬さくら。生徒が顔を真っ赤にして呼吸を乱すのを観察しながら、楽しそうに微笑むサディスティックな表情が男心を狂わせます。机の下に潜り込ませての密着フェラなど、シチュエーションの完成度が群を抜いています。</p>

<h3>実用ポイント：教卓の上で足を絡め取られる主導権完全掌握セックス</h3>
<p>教卓の上に生徒を押し倒し、自ら下着を脱ぎ捨てて跨がっていく岬さくら。耳元で「先生のオマ○コで初めてを迎えられて幸せでしょ？」と囁きながら、締め付けの強い膣内でゆっくりとペニスを搾り取っていきます。逃げ場のない密室で大人の女性に身体も心も完全に支配される感覚は、他では味わえない強烈な射精トリガーとなります。</p>""",

    "ipx00830": """<h2>『美人家庭教師あんな先生の接吻レクチャー個人レッスン 加美杏奈』詳細レビュー</h2>
<p>端正な美貌と包容力あふれるお姉さんオーラで絶大な人気を誇る加美杏奈が、童貞の教え子に「大人のキスの仕方」を手取り足取り教え込む個人レッスン作品。勉強部屋という狭いパーソナルスペースで、吐息が触れ合うほどの距離から始まる濃密なリップ音とスキンシップが、視聴者の鼓膜と理性を同時に溶かしていきます。</p>

<h3>見どころ：息が詰まるほどの至近距離で交わされる濃厚ディープキス</h3>
<p>参考書を広げた机の隣で、「じゃあ、先生がお手本見せてあげるね」と顔を寄せてくる加美杏奈。柔らかい唇が重なり、湿った舌先が口内へと侵入して絡み合う生々しい水音が部屋に響き渡ります。目を開けるとすぐそこに彼女の艶やかな瞳と上気した頬があり、まるで自分自身が個人レッスンを受けているかのような強烈な没入感を味わえます。</p>

<h3>実用ポイント：キスの延長でなし崩し的に始まる生ハメ筆おろし</h3>
<p>長時間のディープキスで生徒の下半身がカチカチに硬くなると、加美杏奈は優しく微笑みながらズボンに手を伸ばします。「こんなに大きくしちゃって…じゃあ、続きも教えてあげる」とベッドへ誘導。キスを途切れさせることなく、下半身だけを結合させてゆっくりと愛を確かめ合うように腰を振るシーンは、優しさとエロティシズムの極致です。</p>""",

    "miae00281": """<h2>『はじめて彼女ができたので幼なじみとSEXや中出しの練習をする事にした 神宮寺ナオ』詳細レビュー</h2>
<p>透明感と圧倒的な美貌を誇る神宮寺ナオが、彼女ができたばかりの童貞幼馴染のために「セックスの練習台」を買って出る切なくもドスケベな傑作。昔からの気心の知れた関係だからこその飾らない会話から、ひとたび肌を重ねると女としての本能が溢れ出し、互いに後戻りできない快楽の深みへハマっていく様が秀逸です。</p>

<h3>見どころ：幼馴染という関係性の崩壊と生々しい性教育</h3>
<p>「彼女を喜ばせたいなら、もっと優しく触らないとダメだよ」と、自分の胸や秘部を使って愛撫のレクチャーを行う神宮寺ナオ。最初は冷静にアドバイスしていたはずが、敏感な身体を刺激されるうちに次第に吐息が熱くなり、瞳が潤んでいきます。幼馴染の枠を超えて一人の「メス」として求めてしまう禁断の背徳感が画面を満たします。</p>

<h3>実用ポイント：練習の域を超えて本能で求め合う濃厚中出し</h3>
<p>「これ、本当に練習だからね…？」と言いながらも、結合した瞬間から神宮寺ナオの腰は止まらなくなります。正常位で強く抱きしめ合い、お互いの体温を全身で感じながら激しく腰を打ち付ける交わり。最後は「彼女には内緒だよ…」と耳元で呟かれながら膣内深くに精液を放つシーンは、罪悪感と快楽が混ざり合った最高の抜きどころです。</p>""",

    "mide00921": """<h2>『もしかしたら…（耳元で）今夜、童貞卒業できるかもね 終電逃した女上司とビジネスホテルにお泊まりしたら童貞がバレて… 藍芽みずき』詳細レビュー</h2>
<p>知的なルックスと抜群のプロポーションを誇る藍芽みずきが、出張先で終電を逃し、部下とシングルルームに相部屋宿泊することになった美人上司を熱演。普段は厳しい上司が、部下が童貞であることを知った瞬間から小悪魔的な色気を発揮し、ベッドの上で朝まで男にしてあげる極上のオフィスラブ作品です。</p>

<h3>見どころ：職場での厳しい顔から一変するベッドでの妖艶なお姉さんモード</h3>
<p>お風呂上がりにバスローブ姿で現れ、缶ビールを飲みながら「君、もしかして女の子と寝たことないの？」と悪戯っぽく微笑む藍芽みずき。耳元に顔を寄せ、「今夜、童貞卒業させてあげようか？」と甘く囁く声のトーンに男の心臓は跳ね上がります。上下関係のギャップを巧みに利用したからかいが、男の征服欲と被虐欲を同時に刺激します。</p>

<h3>実用ポイント：手取り足取り教え込まれる密室の一夜漬けレッスン</h3>
<p>ベッドに横たわらせた部下の上に優しく跨がり、手取り足取りペニスを自分の秘部へと導く藍芽みずき。結合した瞬間の部下の驚いた表情を愛おしそうに見つめ、「上手に動かせるかな？」と腰の動かし方をリードしてくれます。大人の女性の包容力とテクニックに身を委ね、心ゆくまで射精できる至福の時間が凝縮されています。</p>""",

    # 記事3: 元カノ・再会未練セックス特化
    "ipzz00047": """<h2>『大好きだったけどフラれた元カノと偶然再会したら昔よりも圧倒的にかわいくなっててテンション爆上がったボクは ダメ元ラブホデート誘ったらまさかのOKで朝までノンストップ中出しSEXしまくった。 二葉エマ』詳細レビュー</h2>
<p>圧倒的なアイドル級ルックスと抜群の愛嬌を誇る二葉エマが、昔自分をフッた元カノとして偶然再会。学生時代よりも洗練され、大人びた色気を漂わせる彼女にダメ元で声をかけたところ、まさかのOKが出てラブホテルで朝まで狂ったようにハメ倒すという、男の長年のリベンジ妄想を完璧に具現化した大傑作です。</p>

<h3>見どころ：昔より遥かに色っぽくなった元カノの無防備なホテル姿</h3>
<p>街中で偶然目が合い、懐かしさから居酒屋で乾杯した後のホテルチェックイン。部屋に入ると、少し照れくさそうに笑いながら「なんか昔を思い出すね…」と髪をかき上げる二葉エマの破壊力は言葉を失います。昔は知り得なかった大人の女性としてのフェロモンと、付き合っていた頃の懐かしい笑顔が交錯し、男の欲望は最初から沸点に達します。</p>

<h3>実用ポイント：昔の記憶を上書きするように貪り尽くすノンストップ中出し</h3>
<p>ベッドになだれ込むと、昔の未練をすべてぶつけるように激しいキスと愛撫が始まります。二葉エマの引き締まったウエストを掴み、後ろから深く突き入れると、彼女はシーツを握りしめて「あっ、すごい…昔よりずっといい…！」と歓喜の声を漏らします。フッたはずの男のイチモツに完全に溺れ、朝を迎えるまで何度も中出しを許してしまう姿は最高のカタルシスです。</p>""",

    "cawd00361": """<h2>『初恋の元カノがごっくん大好きちんしゃぶ狂い 中出しチ●ポも追撃フェラで即復活！金玉カラカラになるまでハメ続けた同窓会の夜 沙月恵奈』詳細レビュー</h2>
<p>清楚で可憐なルックスを持ちながら、AV界屈指のフェラチオテクニックと淫乱さを兼ね備えた沙月恵奈。中学・高校時代の初恋の元カノと同窓会で数年ぶりに再会したところ、ウブだったはずの彼女が「ごっくん大好きなちんしゃぶ狂い」に豹変していたという、男の脳を狂わせる衝撃作です。</p>

<h3>見どころ：純情だった初恋相手の信じられないド変態化</h3>
<p>同窓会の二次会を抜け出し、ホテルの部屋に入った途端に跪いてペニスをしゃぶり始める沙月恵奈。「ずっとあなたのオチンチンが忘れられなかったの…」と潤んだ瞳で見つめながら、舌全体を使ってジュルジュルと音を立ててしゃぶり尽くす姿は圧巻です。初恋の美化された思い出が、最高峰のド変態プレイによって極上の快感へと塗り替えられます。</p>

<h3>実用ポイント：射精直後の追撃フェラと金玉がカラになるまでの連続交尾</h3>
<p>一度中出ししてぐったりしたペニスを、沙月恵奈は休ませることなく口に含んで丁寧に清掃フェラ。温かい唾液と巧みな舌使いで即座に硬度を取り戻させると、再び自分から跨がって奥まで挿入します。一晩で何発も射精を搾り取られ、精液をすべてごっくんと飲み干される圧倒的なご馳走感は、ドスケベな体験を求める全ユーザーに強く推奨できます。</p>""",

    "miab00452": """<h2>『元カノ相部屋同窓会 5年ぶりに再会した元カノ2人と飲んだらお酒に酔って昔の恋話が再燃！終電で帰してくれず相部屋ラブホで朝まで奪い合い中出し 逢沢みゆ 北岡果林』詳細レビュー</h2>
<p>可憐な美少女・逢沢みゆと、妖艶な色気を持つ北岡果林という超豪華な2大女優が、なんと「元カノ2人」として同時に登場。同窓会で5年ぶりに再会した男を巡って酒の勢いで昔の恋バナがヒートアップし、終電を逃した勢いでラブホテルの相部屋になだれ込んで朝まで奪い合いの生ハメを行うという、夢のハーレム作品です。</p>

<h3>見どころ：元カノ同士の嫉妬と張り合いが生み出すエスカレート</h3>
<p>「私と付き合ってた時のほうが楽しかったでしょ？」「いや、私のほうが相性良かったもん」と、お酒に酔った2人がベッドの上でペニスを取り合う贅沢すぎる構図。逢沢みゆの華奢な身体と北岡果林のグラマラスな肉体が左右から密着し、男の耳元にそれぞれの甘い淫語を吹き込んでくるシーンは、脳の快楽物質がドバドバと溢れ出す危険な興奮を呼び起こします。</p>

<h3>実用ポイント：左右から同時に攻め立てられる贅沢極まる中出しサンド</h3>
<p>ベッドの中央で横たわる男に対し、一人がフェラをし、もう一人が顔元でキスをしてくるなど、全身の性感帯を休む暇なく刺激。さらに2人の元カノに交代で生挿入を繰り返し、どちらの膣内にもたっぷりと白濁液を注ぎ込んでいく本番シチュエーションは実用性満点です。過去の思い出と現在の肉欲が混ざり合う最高潮の射精を体験できます。</p>""",

    "mngs00002": """<h2>『AV女優になった元カノ幼馴染と再会 久しぶりに会った彼女が垢抜けて可愛くなってたのでついデートに誘ったらまさかのOK… 新井リマ』詳細レビュー</h2>
<p>天真爛漫な笑顔と抜群の美貌で人気の新井リマが、「AV女優として大成功した元カノ兼幼馴染」という奇抜かつ男の妄想を完璧に刺激するシチュエーションを演じた名作。昔は手すら満足に握れなかったウブな幼馴染が、プロのAV女優として洗練された姿で目の前に現れ、ホテルで昔の記憶を取り戻すように交わるエモーショナルな作品です。</p>

<h3>見どころ：垢抜けた元カノの圧倒的な美貌とプロの包容力</h3>
<p>画面の中でしか見られなくなっていたはずの新井リマが、プライベートの私服姿で待ち合わせ場所に登場。昔のぎこちなさを懐かしみながら、ホテルに入ると「昔はこんなことできなかったよね…」と優しくリードしてくれる姿に胸が高鳴ります。芸能人のようなオーラを纏った元カノを独占できる優越感が男のプライドを刺激します。</p>

<h3>実用ポイント：培われた凄テクと幼馴染としての情愛が交錯する生ハメ</h3>
<p>AVの世界で磨き上げられた巧みな腰使いと、幼馴染としての深い愛情が合わさったセックスは極上の快感をもたらします。正常位で顔を寄せ合い、昔の思い出話をしながらゆっくりと腰を沈めていくシーンでは、新井リマの瞳に愛おしさが満ち溢れ、まるで本物の恋人と交わっているかのような多幸感に包まれます。</p>""",

    "1seven00013": """<h2>『俺の上司の嫁が元カノだった… 出世より射精を優先してしまった話 大槻ひびき』詳細レビュー</h2>
<p>AV界の生けるレジェンド・大槻ひびきが、会社の厳格な上司の妻となって現れた「忘れられない元カノ」を演じる、背徳感MAXのドラマチック名作。上司の自宅に招かれた部下が、キッチンや浴室の隙間を縫って昔の恋人と密会し、出世や社会的な立場をかなぐり捨てて快楽に溺れていく緊迫のストーリーが展開されます。</p>

<h3>見どころ：上司が隣の部屋にいる状況でのスリリングな密会エロス</h3>
<p>リビングで上司がテレビを見ている隙に、キッチンで二人きりになった瞬間、大槻ひびきがエプロン越しに身体を寄せてくる背徳のオープニング。「見つかったらどうするの…？」と口では拒みながらも、元彼の逞しい身体に触れられて秘部を濡らしていく人妻の葛藤が極めてリアルです。息を潜めながら交わす声を出せないキスに心拍数が急上昇します。</p>

<h3>実用ポイント：声を押し殺しながら貪り合う禁断のサイレント中出し</h3>
<p>物音を立てられない極限状態の中、大槻ひびきの口を手で塞ぎながら激しく腰を突き入れるスリリングな交尾。上司の妻という越えてはならない一線を越え、元カノの温かい膣内に容赦なく精液を撃ち込む瞬間は、他のどんな作品でも味わえない圧倒的な征服感と背徳のオルガズムをもたらします。</p>"""
}

# 3記事のメタ情報
ARTICLES = [
    {
        "id": "feature_fanza_white_skin_gyaru_cute_lovelove_ranking_2026",
        "title": "【男ウケ最強の透き通る素肌とあざとさ】FANZA「白ギャル・清楚系ギャル」おすすめ神作ランキングTOP5！色白モチ肌×明るい茶髪×神対応イチャラブで男を沼らせる至高の傑作選【2026年最新】",
        "hinban": "WHITE-GYARU-CUTE-LOVELOVE-2026",
        "cids": ["midv00927", "1stars00836", "cjod00494", "1svgal00001", "mida00546"],
        "hero_tag": "WHITE SKIN GYARU SPECIAL",
        "genres": ["白ギャル", "ギャル", "美少女", "イチャラブ", "中出し", "素人風", "主観", "特集", "殿堂入り"],
        "lead_p1": "日焼けした黒ギャルとは一線を画し、世の男性たちから圧倒的な熱狂的支持を集めているのが「白ギャル・清楚系ギャル」というジャンルです。透き通るような雪白のモチ肌に、抜け感のある明るい茶髪、そして派手すぎないナチュラルメイク。街で見かけるような親しみやすさと、男心を惑わすあざと可愛い笑顔が絶妙に融合した彼女たちは、まさに現代の男が夢見る理想のヒロインと言えます。",
        "lead_p2": "白ギャル作品の最大の魅力は、ノリの良さとエッチに対する素直な積極性にあります。「ねえ、まだシないの？」「ウチの身体、好きにしていいよ♡」と気兼ねなく甘えてくるフランクな距離感は、堅苦しい駆け引きを忘れさせてくれます。ベッドに入れば恥じらいを捨てて自分から腰を動かし、大好きな彼氏を喜ばせようと一生懸命にご奉仕してくれる姿に、男性ホルモンは限界まで刺激されます。",
        "lead_p3": "本特集では、石原希望の宿題代行おま○こ幼馴染から、小倉由菜の完璧な都合のいい愛人ギャル、春陽モカの無制限中出し風俗学園、逢月ひまりの罰ゲーム童貞狩り逆転劇、そして松本いちか＆春陽モカの贅沢すぎるローション風呂W白ギャルまで、抜きやすさと可愛らしさを極めた【白ギャル神作TOP5】を徹底解説します！",
        "points": [
            ("① 透き通る色白肌と明るい髪色の絶妙なギャップ", "日焼けしていないモチモチの白肌に、ふんわり巻いた明るいヘアカラー。清楚な清潔感とギャルの色気が共存し、視覚的な美しさが際立ちます。"),
            ("② 男を立てて甘やかしてくれる神対応のコミュ力", "ツンツンした態度は一切なく、屈託のない笑顔と抜群のノリで距離をゼロにしてくれる居心地の良さ。疲れた男を全力で肯定してくれます。"),
            ("③ ベッドで見せる素直で貪欲なメスの本能", "普段の明るいノリから一転、挿入された瞬間に熱い吐息を漏らし、自分から積極的に中出しを求めてくるギャップが最強の射精トリガーとなります。")
        ],
        "table_headers": ["順位・タイトル", "主演女優", "シチュエーション", "あざとさ・実用度", "詳細"],
        "faqs": [
            ("Q1. 白ギャル作品は黒ギャルとどう違うのですか？", "黒ギャルが小麦色の肌と派手なギャルカルチャーを前面に出すのに対し、白ギャルは透明感のある色白肌をベースに、ナチュラルな茶髪やトレンドメイクを取り入れたスタイルです。清楚な美少女感とギャルのノリの良さが両立しており、男ウケが非常に高いのが特徴です。"),
            ("Q2. 白ギャル作品で一番おすすめの女優は誰ですか？", "まずは石原希望や小倉由菜、松本いちか、春陽モカの作品からチェックするのが鉄板です。彼女たちは天性の明るさと高い演技力、そして抜群のプロポーションを兼ね備えており、白ギャルの魅力を余すところなく味わえます。"),
            ("Q3. イチャラブ系と痴女系ではどちらが抜きやすいですか？", "心の癒やしや彼女感を味わいたいなら石原希望や小倉由菜のイチャラブ系、圧倒的な刺激や連続射精を求めるなら春陽モカや松本いちかの痴女系・中出し特化作が最適です。本特集ではどちらの需要もカバーしています。"),
            ("Q4. FANZAで購入する場合、見放題と単品購入どちらが良いですか？", "本特集で厳選したような高評価の神作は、何度でも見返して抜けるマスターピースばかりです。手元に高画質HD版を永続的に残せる単品購入（ダウンロード／ストリーミング）が最も満足度が高くおすすめです。")
        ],
        "related": [
            ("/posts/feature_fanza_cohabitation_sweet_girlfriend_lovelove_ranking_2026", "【本物の彼女のような多幸感】FANZA「同棲生活・甘々イチャラブ」おすすめ神作ランキングTOP5！", "生活感あふれる部屋着とすっぴん風メイクで密着する至福の同棲生活特集。"),
            ("/posts/feature_gyaru_jk_tanned_skin_raw_creampie_school", "【健康的な褐色肌とピチピチ制服】黒ギャルJK・学校密会中出しAV名作選", "小麦色の小麦肌と放課後の背徳感を味わいたい方はこちらもチェック！"),
            ("/posts/feature_fanza_vr_high_immersion_selection", "【圧倒的没入感】8K/4K超高画質VRエロ動画おすすめ神作まとめ", "目の前に実在するかのようなゼロ距離体験を楽しめる最新VR特集。"),
            ("/posts/feature_beauty_cosplay_heroine_ranking_2026", "【二次元の理想を完全具現化】FANZA本格コスプレ・ヒロイン特化おすすめ神作TOP5！", "ハイクオリティな衣装とトップ女優が魅せるファンタジー特集。")
        ]
    },
    {
        "id": "feature_fanza_virgin_hunting_aggressive_older_sister_ranking_2026",
        "title": "【ウブな男の子を骨抜きに貪り尽くす】FANZA「童貞狩り・積極的肉食お姉さん」おすすめ神作ランキングTOP5！からかい寸止めから生ハメ主導権掌握まで理性を狂わせる至高の搾精傑作選【2026年最新】",
        "hinban": "VIRGIN-HUNTING-OLDER-SISTER-2026",
        "cids": ["cawd00827", "bacj00064", "ipx00830", "miae00281", "mide00921"],
        "hero_tag": "VIRGIN HUNTING SISTER SPECIAL",
        "genres": ["童貞狩り", "お姉さん", "逆夜這い", "搾精", "主導権", "美少女", "中出し", "特集", "殿堂入り"],
        "lead_p1": "男性なら誰もが一度は妄想する「年上の綺麗なお姉さんに翻弄され、骨抜きにされるシチュエーション」。その欲望を極限まで尖らせたジャンルが【童貞狩り・積極的肉食お姉さん】です。単なる優しい筆おろしとは一線を画し、ウブな男の子の反応をサディスティックにからかい、寸止めや耳元淫語で焦らした末に、自分から身体を重ねて精子を根こそぎ吸い上げる圧倒的な主導権掌握劇がここにあります。",
        "lead_p2": "経験のない男の子が緊張で身体を強張らせ、赤面しながら息を荒げる姿を見て、お姉さんたちの性欲のスイッチは完全にオンになります。「そんなに緊張してたら何もできないよ？」「お姉ちゃんが気持ちいいこと全部教えてあげる♡」と甘く危険な囁きで理性を溶かし、最後は男の制御不能な本能を引きずり出して自らも快楽の深みへと堕ちていくダイナミズムが圧巻です。",
        "lead_p3": "本特集では、伊藤舞雪の童貞請負人キメセク敗北ドラマから、岬さくらの美人教師による準備室誘惑、加美杏奈の勉強部屋ディープキス個人レッスン、神宮寺ナオの幼馴染SEX練習中出し、そして藍芽みずきの出張ホテル終電逃し一夜漬けレッスンまで、男の被虐欲と征服欲を同時に刺激する【童貞狩り神作TOP5】を徹底レビューします！",
        "points": [
            ("① 逃げ場のない密室で繰り広げられるからかいと寸止め", "準備室、勉強部屋、ホテルのシングルルーム。二人きりの空間で耳元に吐息を吹きかけられ、限界まで焦らされる背徳感が脳髄を痺れさせます。"),
            ("② 大人の色気とテクニックで主導権を握られる快感", "豊かなバストや滑らかな太ももを惜しげもなく密着させ、巧みな舌使いで硬度を極限まで高めてくれる至れり尽くせりの奉仕。"),
            ("③ 理性が崩壊した男の絶倫ピストンに屈する逆転劇", "からかっていたはずのお姉さんが、男の本能剥き出しの激しい腰振りに耐えきれず、白目を剥いてアクメに堕ちるカタルシスが最高の実用性を誇ります。")
        ],
        "table_headers": ["順位・タイトル", "主演女優", "シチュエーション", "主導権・背徳度", "詳細"],
        "faqs": [
            ("Q1. 「童貞狩り」作品は普通の筆おろし作品と何が違いますか？", "一般的な筆おろし作品が「優しく包み込む聖母のようなケア」を重視するのに対し、童貞狩り作品は「お姉さん側が童貞を弄び、からかい、主導権を握って搾り取るアグレッシブさ」が最大の特徴です。刺激が段違いに強く、濃厚な抜きやすさがあります。"),
            ("Q2. ドM気質の男性でなくても楽しめますか？", "十分に楽しめます！最初は主導権をお姉さんに握られて翻弄されますが、後半では男側の激しいピストンによってお姉さんが快楽に屈服し、メスの顔を晒す展開が多いため、ドM欲と征服欲の両方を完璧に満たすことができます。"),
            ("Q3. どの作品から観るのがおすすめですか？", "大人のグラマラスな色気を味わいたいなら伊藤舞雪の『cawd00827』、禁断のシチュエーションと寸止め焦らしを味わいたいなら岬さくらの『bacj00064』が群を抜いて完成度が高くおすすめです。"),
            ("Q4. 作品選びで失敗しないためのポイントは？", "シチュエーション設定のリアルさと、女優の演技力が鍵になります。本特集で取り上げた女優陣はいずれも演技力とエロス表現においてトップクラスの実力派ばかりですので、安心して没入できます。")
        ],
        "related": [
            ("/posts/feature_virgin_deflowering_gentle_older_sister", "【緊張で震えるウブな男の子を優しく包み込む】童貞・筆おろし特集！", "優しく包み込まれる王道ケアを楽しみたい方はこちらも必見。"),
            ("/posts/feature_fanza_female_boss_office_affair_ranking_2026", "【オフィスで豹変するキャリア美女】美人女上司・出張相部屋神作TOP5！", "大人の女性による密室の誘惑をテーマにした大人気特集。"),
            ("/posts/feature_whispering_tutor_private_room_study_lesson", "【耳元の囁き】美少女家庭教師・勉強部屋密着特集！", "吐息と至近距離のからかいレッスンを堪能できる名作選。"),
            ("/posts/feature_vicious_practitioner_sensual_massage_training", "【悪辣施術師・密室オイル生ハメ調教特集】", "密室での主導権掌握と快感開発をテーマにしたマニア向け傑作選。")
        ]
    },
    {
        "id": "feature_fanza_ex_girlfriend_reunion_unrequited_passion_ranking_2026",
        "title": "【昔付き合っていたあの子と数年ぶりの再会】FANZA「元カノ・未練と衝動の再会セックス」おすすめ神作ランキングTOP5！大人の色気をまとった元恋人とホテルで貪り合う至高の背徳名作選【2026年最新】",
        "hinban": "EX-GIRLFRIEND-REUNION-PASSION-2026",
        "cids": ["ipzz00047", "cawd00361", "miab00452", "mngs00002", "1seven00013"],
        "hero_tag": "EX-GIRLFRIEND REUNION SPECIAL",
        "genres": ["元カノ", "同窓会", "再会", "未練", "美少女", "中出し", "ドラマ", "特集", "殿堂入り"],
        "lead_p1": "街の雑踏、居酒屋、あるいは数年ぶりの同窓会――ふとした瞬間に訪れる「かつて愛し合った元カノとの再会」。別れた当時のほろ苦い記憶とともに、目の前に現れた彼女が昔よりも遥かに洗練され、色気をまとった大人の女性へと変貌していたとき、男の理性の堤防は音を立てて決壊します。それこそが【元カノ・再会セックス】が持つ抗えない魔力です。",
        "lead_p2": "「もう私たち、あの頃とは違うんだよ…？」と最初は戸惑いを見せながらも、グラスを重ねるうちに蘇る昔のあだ名と懐かしい笑顔。お互いの身体の相性を知り尽くしているからこそ、一度触れ合ってしまえば遠慮も躊躇も消え去り、貪り合うような生交尾へと雪崩れ込みます。過去の未練と現在の肉欲が激しくスパークする瞬間は、他のどんなシチュエーションよりも生々しくエロティックです。",
        "lead_p3": "本特集では、二葉エマのフッた元彼とまさかの再会ラブホ中出しから、沙月恵奈の初恋相手がちんしゃぶ狂いに豹変した同窓会の夜、逢沢みゆ＆北岡果林の元カノ2人相部屋奪い合い、新井リマのAV女優になった元カノ幼馴染、そして大槻ひびきの上司の妻となった元カノとの禁断不倫まで、男の未練と妄想を完璧に満たす【元カノ神作TOP5】を厳選紹介します！",
        "points": [
            ("① 当時よりも遥かに美しく色っぽくなった元恋人の姿", "学生時代や付き合っていた頃には見せなかった大人の色気。垢抜けたファッションと女としてのフェロモンが男のプライドと欲望を刺激します。"),
            ("② 身体が覚えている相性の良さと、昔を超越する乱れっぷり", "「ここが好きだったよね…？」と敏感なツボを知り尽くした愛撫。懐かしさと新鮮さが混ざり合い、初体験以上の興奮が押し寄せます。"),
            ("③ 戻れない過去への未練をすべてぶつける濃厚中出し", "今夜限りの過ちと知りながら、身体の芯深くまで注ぎ込む白濁液。切なさと背徳感が最高の射精カタルシスを生み出します。")
        ],
        "table_headers": ["順位・タイトル", "主演女優", "再会シチュエーション", "背徳度・情念", "詳細"],
        "faqs": [
            ("Q1. 元カノ再会ジャンルが男性からこれほど支持される理由は何ですか？", "「過去の恋愛への未練」と「成長した元カノを抱く優越感」、そして「身体の相性を知っている者同士の気兼ねのなさ」が完璧に合致しているからです。現実ではなかなか起こり得ない男のロマンをリアルに擬似体験できるのが最大の魅力です。"),
            ("Q2. 切ないストーリー重視ですか？それとも即抜き実用重視ですか？", "本特集で選んだ5作品は、再会のエモーショナルな導入から、ホテルに入った後の濃厚なハメ倒しまで、ドラマ性と抜きやすさの双方がハイレベルに両立しています。じっくりシチュエーションに浸りたい時も、即座に抜きたい時も活躍します。"),
            ("Q3. 一番おすすめのタイトルを1本だけ選ぶならどれですか？", "王道の再会ラブホデートで圧倒的な可愛らしさを堪能したいなら二葉エマの『ipzz00047』、同窓会からの濃厚フェラ＆追撃搾精を味わいたいなら沙月恵奈の『cawd00361』が間違いのない大傑作です。"),
            ("Q4. 複数人で乱れる作品もありますか？", "逢沢みゆと北岡果林が共演する『miab00452』は、なんと「元カノ2人と同時に相部屋宿泊する」という贅沢極まるハーレム作品です。元カノ同士が男のイチモツを奪い合う展開は圧巻です。")
        ],
        "related": [
            ("/posts/feature_wedding_afterparty_hotel_take_home", "【友人の結婚式二次会で意気投合した美女】ホテルお持ち帰り中出し名作選", "フォーマルな衣装の美女とホテルで朝まで乱れる大人気特集。"),
            ("/posts/feature_fanza_cohabitation_sweet_girlfriend_lovelove_ranking_2026", "【本物の彼女のような多幸感】FANZA「同棲生活・甘々イチャラブ」おすすめ神作TOP5！", "恋人感覚と濃密なスキンシップをじっくり味わえる神作特集。"),
            ("/posts/feature_workplace_inhouse_ntr_secret_affair", "【社内恋愛NTR特集】給湯室・非常階段での背徳中出しAV傑作選", "身近な関係性だからこそ燃え上がる背徳の愛欲を描いた名作選。"),
            ("/posts/feature_yukata_hot_spring_inn_endless_creampie", "【浴衣・温泉旅館お泊まりAV特集】湯上がり素肌と畳の上で朝まで生ハメ名作選", "旅情とお泊まりデートの開放感に浸れる傑作まとめ。")
        ]
    }
]

def main():
    print("=== STARTING GENERATION OF 3 NEW KILLER FEATURES V2 ===")
    
    for art_idx, art in enumerate(ARTICLES, 1):
        art_id = art["id"]
        art_title = art["title"]
        print(f"\n[{art_idx}/3] Processing: {art_title} ({art_id})")
        
        items_data = []
        all_actresses = []
        
        # 1. 各CIDのアイテム情報を都度FANZA APIから取得
        for rank, cid in enumerate(art["cids"], 1):
            print(f" -> Fetching FANZA API for CID: {cid} (Rank {rank})...")
            it = fetch_fanza_item(cid)
            if not it:
                print(f" [WARN] Failed to fetch item {cid}, skipping...")
                continue
            it["rank"] = rank
            items_data.append(it)
            time.sleep(0.5) # API負荷軽減
            
            # 個別ポストの生成（存在しない、または最新化）
            single_post_path = os.path.join(OUTPUT_DIR, f"{cid}.json")
            item_actresses = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
            for a in item_actresses:
                if a not in all_actresses:
                    all_actresses.append(a)
                    
            item_genres = [g.get("name") for g in it.get("iteminfo", {}).get("genre", [])]
            item_maker = it.get("iteminfo", {}).get("maker", [{}])[0].get("name", "公式")
            item_date = it.get("date", "2026-10-06 00:00:00")
            item_img = it.get("imageURL", {}).get("large", "")
            item_aff_url = it.get("affiliate_url_clean") or it.get("affiliateURL", "")
            
            # 個別作品用レビューHTML
            individual_rev_html = INDIVIDUAL_REVIEWS.get(cid, f"<p>{it.get('title', '')}の詳細レビューです。</p>")
            sample_imgs = get_sample_images(it, max_count=6)
            s_img_tags = "".join([f'<a href="{item_aff_url}" target="_blank" rel="nofollow noopener" class="overflow-hidden rounded-xl border border-slate-700/80 hover:border-amber-400 transition block group"><img src="{img}" alt="サンプル画像" class="w-full h-auto object-cover group-hover:scale-105 transition duration-300" loading="lazy" /></a>' for img in sample_imgs])
            
            single_html = f"""<div class="space-y-8 text-slate-200">
  <div class="relative rounded-2xl overflow-hidden border border-slate-700 shadow-2xl bg-slate-900">
    <a href="{item_aff_url}" target="_blank" rel="nofollow noopener" class="block group">
      <img src="{item_img}" alt="{it.get('title', '')}" class="w-full h-auto object-cover group-hover:scale-102 transition duration-300" />
      <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-6">
        <span class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-amber-500 to-rose-600 text-white font-bold rounded-xl shadow-lg group-hover:brightness-110 transition">
          ▶ FANZA公式でこの作品を今すぐ視聴する
        </span>
      </div>
    </a>
  </div>

  <div class="p-6 bg-slate-800/80 rounded-2xl border border-slate-700/80">
    <h1 class="text-2xl font-bold text-white mb-4">{it.get('title', '')}</h1>
    <div class="flex flex-wrap gap-2 mb-6">
      {' '.join([get_actress_link(a) for a in item_actresses])}
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
                "title": it.get("title", ""),
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
    <span class="inline-flex items-center justify-center w-10 h-10 rounded-2xl bg-gradient-to-br from-amber-400 to-rose-600 text-white font-black text-xl shadow-lg">
      {rank}
    </span>
    <div>
      <span class="text-xs font-bold text-amber-400 uppercase tracking-widest">RANKING NO.{rank}</span>
      <h3 class="text-xl md:text-2xl font-extrabold text-white leading-tight">
        {title}
      </h3>
    </div>
  </div>

  <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 mb-6">
    <div class="lg:col-span-5">
      <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="block overflow-hidden rounded-2xl border border-slate-700 group relative">
        <img src="{img}" alt="{title}" class="w-full h-auto object-cover group-hover:scale-105 transition duration-300" loading="lazy" />
        <div class="absolute top-3 left-3 bg-black/70 backdrop-blur-md px-3 py-1 rounded-full text-xs font-bold text-amber-300 border border-amber-500/40">
          ★ {rating} ({rev_cnt}件の評価)
        </div>
      </a>
      
      <div class="mt-4 p-4 bg-slate-800/80 rounded-2xl border border-slate-700/60 text-xs space-y-2">
        <div class="flex justify-between items-center text-slate-300">
          <span class="font-bold text-slate-400">主演女優:</span>
          <span>{' '.join([get_actress_link(a) for a in item_actresses])}</span>
        </div>
        <div class="flex justify-between items-center text-slate-300">
          <span class="font-bold text-slate-400">メーカー:</span>
          <span class="text-white font-medium">{maker}</span>
        </div>
        <div class="flex justify-between items-center text-slate-300">
          <span class="font-bold text-slate-400">品番:</span>
          <span class="text-slate-200 font-mono">{cid}</span>
        </div>
      </div>
    </div>

    <div class="lg:col-span-7 space-y-4 text-slate-200 text-sm md:text-base leading-relaxed">
      {ind_review}
      
      <div class="pt-4 flex flex-wrap gap-2">
        {' '.join([get_genre_link(g) for g in item_genres[:6]])}
      </div>
    </div>
  </div>

  {f'''<div class="mb-6">
    <h4 class="text-sm font-bold text-slate-400 mb-3 flex items-center gap-1.5">
      <span>📷</span> サンプルシーン・ハイライト
    </h4>
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
      {s_tags}
    </div>
  </div>''' if s_tags else ''}

  <div class="flex flex-col sm:flex-row gap-3 pt-2">
    <a href="{aff_url}" target="_blank" rel="nofollow noopener" class="flex-1 inline-flex items-center justify-center gap-2 px-6 py-4 bg-gradient-to-r from-amber-500 via-rose-500 to-rose-600 hover:brightness-110 text-white font-extrabold rounded-2xl shadow-xl transition transform hover:-translate-y-0.5 text-center text-base">
      <span>🔥</span> FANZA公式でこの作品を視聴する（独占・HD配信）
    </a>
    <a href="/posts/{cid}" class="inline-flex items-center justify-center px-6 py-4 bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white font-bold rounded-2xl border border-slate-700 transition text-sm text-center">
      個別詳細ページを見る
    </a>
  </div>
</div>""")

        # 徹底比較スペック表
        table_rows = []
        for it in items_data:
            c_rank = it["rank"]
            c_cid = it.get("content_id", "")
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
            "date": "2026-10-07 00:00:00",
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
