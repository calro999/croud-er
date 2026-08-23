const fs = require('fs');
const path = require('path');
const https = require('https');

const API_ID = "4Lx0ftRf17Uuad6Ud7Gb";
const API_AFFILIATE_ID = "onchan555-999";
const OUT_AFFILIATE_ID = "onchan555-003";

const targetThemes = [
  {
    id: "feature_naked_apron_young_wife_breakfast_sex",
    query: "新妻 エプロン",
    title: "【新婚の朝に揺れる無防備な曲線】裸エプロン・新妻特集！キッチンで朝食準備中に背後から抱きすくめられ突かれる極上生ハメAV名作選",
    category: "人妻・新妻",
    themeKeyword: "新妻・裸エプロン・新婚生活・キッチンセックス・朝立ち・背後密着",
    searchIntent: "清楚で可愛らしい新妻がエプロン一枚の無防備な姿で料理中に背後から即ハメされる甘々かつ刺激的なAVを探しているユーザー向け",
    introTone: "朝の柔らかな光が差し込むキッチン、トントンと小気味よく響く包丁の音。しかしその薄手の布地一枚の下には、下着さえ着けていない無防備な白肌が隠されていた。背後から忍び寄り、新婚の甘い新妻をカウンターに手をつかせ貪り尽くす至福の朝の情事——。",
    tags: ["新妻", "裸エプロン", "キッチン", "新婚", "生中出し", "バック", "美少女", "甘々"]
  },
  {
    id: "feature_female_announcer_broadcasting_accident",
    query: "女子アナ 放送事故",
    title: "【生放送中の原稿読みと忍び寄る快楽】美人女子アナ・キャスター特集！本番スタジオの原稿台下で弄ばれ声震わせる背徳放送事故AV名作選",
    category: "職業・制服",
    themeKeyword: "女子アナ・アナウンサー・放送事故・スタジオ・原稿台下・生放送・電波ジャック",
    searchIntent: "知性と気品を兼ね備えた人気女子アナウンサーが生放送中やスタジオ裏で弄ばれ、必死に平静を装いながらイキ悶えるAVを探しているユーザー向け",
    introTone: "カメラの赤いタリーランプが点灯し、全国へ生放送されるニューススタジオ。原稿台に隠された下半身には、プロデューサーの卑猥な手先が蠢く。滑らかなアナウンスの合間にふと漏れる湿り気を帯びた吐息と、知的な仮面が崩れ落ちる瞬間の絶頂——。",
    tags: ["女子アナ", "アナウンサー", "放送事故", "原稿台下", "スーツ", "タイトスカート", "中出し", "声我慢"]
  },
  {
    id: "feature_swimsuit_tight_swimming_club_creampie",
    query: "競泳水着 密着",
    title: "【濡れた光沢と張り付く美ボディライン】ハイレグ競泳水着特集！塩素の匂い漂うプールサイドで水着をずらされ激しく貫かれる密着交尾AV名作選",
    category: "スポーツ・水着",
    themeKeyword: "競泳水着・ハイレグ・プールサイド・水泳部・塩素の匂い・水着ずらし",
    searchIntent: "体にぴったりと張り付いた光沢ある競泳水着を着た美女が、水着を横にずらされて生ハメされるフェティッシュなAVを探しているユーザー向け",
    introTone: "水面を反射する青い光と、鼻腔をくすぐるプールの塩素の匂い。濡れて肌に吸い付く競泳水着が強調する、引き締まったヒップと太もものスリットライン。プールサイドの硬いタイルに押し倒され、クロッチをずらして挿入される生々しい水着フェチの極致——。",
    tags: ["競泳水着", "ハイレグ", "プールサイド", "水泳", "水着ずらし", "中出し", "アスリート", "美尻"]
  },
  {
    id: "feature_cheerleader_uniform_flexibility_sex",
    query: "チアガール",
    title: "【弾ける笑顔と超絶柔軟な開脚交尾】チアリーダー特集！ミニスカユニフォーム姿のまま応援部室で貪り尽くされる青春肉欲AV名作選",
    category: "スポーツ・学生",
    themeKeyword: "チアガール・チアリーダー・ミニスカユニフォーム・開脚・柔軟性・部室",
    searchIntent: "明るく元気なチアリーダーがミニスカのユニフォーム姿のまま、柔軟な開脚ポーズで奥深くまで突き上げられるAVを探しているユーザー向け",
    introTone: "ポンポンを振り笑顔を振りまくスタジアムの華、チアリーダー。だが練習終わりの静まり返った部室では、汗ばむユニフォームの裾をめくり上げ、驚異的な柔軟性で大きく股を開く。引き締まった下半身に深く突き刺さる肉棒の快感に、弾けるような嬌声をあげる——。",
    tags: ["チアガール", "チアリーダー", "ユニフォーム", "開脚", "柔軟", "部室", "中出し", "青春"]
  },
  {
    id: "feature_female_teacher_after_school_remedial",
    query: "女教師 放課後",
    title: "【夕暮れの教室で二人きりの特別補習】美人女教師特集！黒板に手をつかせスーツスカートをたくし上げ突かれる背徳の個別指導AV名作選",
    category: "学園・制服",
    themeKeyword: "女教師・放課後・特別補習・黒板・夕暮れの教室・スーツ・チョークの匂い",
    searchIntent: "放課後の誰もいない教室で、真面目な美人教師が生徒や同僚に背後から抱きつかれ、黒板の前でハメられるシチュエーションAVを探しているユーザー向け",
    introTone: "茜色の夕日が差し込む放課後の教室。チョークの粉が舞う教壇で、二人きりの補習指導。真面目な解説を続ける美人教師の背後から伸びる腕、タイトスカートをまくり上げパンティを引き裂く音。校舎に響くことを恐れながらも、激しいピストンに溺れていく——。",
    tags: ["女教師", "放課後", "補習", "教室", "黒板", "タイトスカート", "中出し", "背後密着"]
  },
  {
    id: "feature_wedding_dress_bride_secret_desire",
    query: "ウェディングドレス 花嫁",
    title: "【純白のベールを濁す背徳の白濁液】花嫁・ウェディングドレス特集！結婚式当日の控室で新郎以外の男に純白ドレスのまま貫かれるNTR・背徳AV名作選",
    category: "人妻・結婚",
    themeKeyword: "ウェディングドレス・花嫁・結婚式控室・純白ベール・式直前・NTR・生中出し",
    searchIntent: "純白のウェディングドレスを身に纏った花嫁が、挙式直前の控室で元カレや義父にドレスを着たまま犯される背徳感MAXのAVを探しているユーザー向け",
    introTone: "パイプオルガンの音色が近づく結婚式場の控室。幾重にも重なる純白のレースとパニエに包まれた最も美しい姿の花嫁。しかしチャペルの扉が開く直前、ドレスの裾をたくし上げられ、背徳の情夫から注ぎ込まれる熱い精子に罪悪感と快楽で震え上がる——。",
    tags: ["ウェディングドレス", "花嫁", "結婚式", "控室", "NTR", "生中出し", "純白", "背徳"]
  },
  {
    id: "feature_office_storage_room_secret_affair",
    query: "会社の倉庫",
    title: "【段ボールの山に隠れた暗闇の密会】オフィス倉庫・資料室特集！誰も来ない社内倉庫の片隅で制服スカートを捲り上げ貪り合う社内不倫AV名作選",
    category: "オフィス・OL",
    themeKeyword: "社内倉庫・資料室・オフィス・段ボール・スチール棚・暗闇・社内不倫",
    searchIntent: "会社の薄暗い倉庫や資料室で、同僚や上司と二人きりになり、スチール棚に手をついて激しくハメ合うオフィス系AVを探しているユーザー向け",
    introTone: "普段は滅多に人が立ち入らない社内地下の書類保管倉庫。埃と紙の匂いが立ち込める段ボールの迷路の奥で、カチリと落ちた照明のスイッチ。スチール棚の冷たさと対照的な、息を殺して貪り合う二人の濡れそぼる肉体と激しい摩擦音——。",
    tags: ["社内倉庫", "資料室", "オフィス", "OL", "制服", "中出し", "社内恋愛", "声我慢"]
  },
  {
    id: "feature_car_camping_night_drive_privacy_tint",
    query: "車中泊",
    title: "【スモークガラスの向こうの揺れる車体】車中泊・ドライブデート特集！フルフラットシートに敷いた毛布の上で激しく軋ませる密室生性交AV名作選",
    category: "野外・露出",
    themeKeyword: "車中泊・ドライブ・フルフラット・スモークガラス・パーキングエリア・密室",
    searchIntent: "夜のドライブ先やパーキングエリア、道の駅での車中泊で、車内をフルフラットにして激しく揺らす車内セックスAVを探しているユーザー向け",
    introTone: "街灯のまばらな深夜の道の駅。外の冷気を遮るスモークガラスで覆われたミニバンの車内。フルフラットにしたシートの上、毛布にくるまりながら絡み合う熱い肌。サスペンションを軋ませながら、密室特有の濃密な空気の中で果てる車中泊エロス——。",
    tags: ["車中泊", "ドライブ", "車内セックス", "フルフラット", "中出し", "野外", "素人風", "密着"]
  },
  {
    id: "feature_midnight_highway_bus_silent_caress",
    query: "夜行バス",
    title: "【カーテン越しに隣り合う息を殺した指先】夜行高速バス特集！消灯後の暗闇とエンジンの重低音に紛れて座席シート下でイカされるサイレントAV名作選",
    category: "シチュエーション",
    themeKeyword: "夜行バス・高速バス・深夜消灯・カーテン・座席シート・ブランケット・サイレント痴漢",
    searchIntent: "消灯された夜行バスの中で、ブランケットの下から手を伸ばされ、周囲にバレないよう必死に声を押し殺してイクスリリングなAVを探しているユーザー向け",
    introTone: "高速道路を走る夜行バスの消灯アナウンス。暗闇に包まれた車内に響く一定のエンジン音。ブランケットの隙間からそっと滑り込む隣人の手先。身動きの取れない狭い座席で、声を出せば全員に気付かれる極限の恐怖と甘美な快楽のせめぎ合い——。",
    tags: ["夜行バス", "高速バス", "声我慢", "ブランケット", "暗闇", "指マン", "中出し", "サイレント"]
  },
  {
    id: "feature_hotel_cleaner_maid_private_room_affair",
    query: "ホテル 清掃員",
    title: "【作業着の奥に隠された豊満な淫肉】ホテル客室清掃員特集！チェックアウト後の散らかったベッドの上で宿泊客と乱れ狂う背徳ルームサービスAV名作選",
    category: "人妻・職業",
    themeKeyword: "ホテル清掃員・ルームメイク・シーツ交換・作業着・客室ベッド・人妻",
    searchIntent: "ホテルの客室清掃に入ってきた地味な清掃員のおばさんや若妻が、部屋に残っていた宿泊客にシーツの上で押し倒されハメられるAVを探しているユーザー向け",
    introTone: "チェックアウト直後のホテルの客室。ベッドメイキングのためにシーツを剥がす作業着姿の清掃員。まだ温もりの残るシーツの上、突然施錠されたドアの音。日常を忘れた密室で、生活感あふれる肉体が剥き出しにされ激しく貪られる——。",
    tags: ["ホテル清掃員", "客室清掃", "ベッドメイキング", "人妻", "作業着", "中出し", "熟女", "濃厚"]
  },
  {
    id: "feature_babysitter_sweet_maternal_seduction",
    query: "シッター 誘惑",
    title: "【母性溢れる包容力と甘美な授乳手コキ】美人ベビーシッター特集！子供が寝静まったリビングで旦那を甘々に蕩けさせる極上ママ活性交AV名作選",
    category: "人妻・シッター",
    themeKeyword: "ベビーシッター・母性・甘々・巨乳・おっぱい・授乳・旦那誘惑",
    searchIntent: "優しくて巨乳のベビーシッターが、子供が寝たあとに雇い主の父親を甘い言葉とおっぱいで骨抜きにする癒やし系AVを探しているユーザー向け",
    introTone: "子供部屋から規則正しい寝息が聞こえる夜のリビング。エプロンを外したベビーシッターが、日頃の激務に疲れた旦那を優しく膝枕へと誘う。豊かなバストで顔を包み込み、まるで赤ちゃんをあやすかのように甘い淫語で射精へと導く至極の母性エロス——。",
    tags: ["ベビーシッター", "母性", "巨乳", "甘々", "パイズリ", "中出し", "人妻", "癒やし"]
  },
  {
    id: "feature_bondage_shibari_rope_art_discipline",
    query: "緊縛 調教",
    title: "【麻縄が食い込む純白の肌と禁断の悦楽】緊縛・SM調教特集！幾重にも縛り上げられ身動きの取れない美女を玩具と肉棒で開発し尽くす名作選",
    category: "マニア・調教",
    themeKeyword: "緊縛・麻縄・SM・調教・拘束・開発・吊り・縄跡",
    searchIntent: "美しい女性が伝統的な麻縄で芸術的に縛り上げられ、抵抗できない状態でじっくりと快楽を植え付けられる緊縛AVを探しているユーザー向け",
    introTone: "軋む麻縄の擦れる音と、柔肌に深く刻まれる紅い縄目。身動きを完全に封じられ、吊り上げられた肢体。視線も逃げ場も失った暗がりの中で、研ぎ澄まされた触覚へ直接注ぎ込まれる強烈な快楽の刺激に、悶え狂う女の究極の悦服——。",
    tags: ["緊縛", "麻縄", "SM", "調教", "拘束", "玩具", "中出し", "ハード"]
  },
  {
    id: "feature_magic_mirror_truck_city_street_hunting",
    query: "マジックミラー",
    title: "【外からは見えない完全透明な狂宴】マジックミラー号特集！街行く一般素人娘を車内に連れ込み人通りの前で生ハメ絶頂させるレジェンドAV名作選",
    category: "素人・ナンパ",
    themeKeyword: "マジックミラー号・MM号・街頭ナンパ・ガラス一枚・素人・公開露出",
    searchIntent: "外からは鏡、中からは丸見えのマジックミラー車の中で、通行人のすぐ横で素人美女がハメられる王道人気シリーズを探しているユーザー向け",
    introTone: "繁華街の真ん中に停車した一台の特装トラック。外を行き交う人々は誰も気づかない。ガラス一枚隔てた車内では、道行く人々の視線を感じながら恥じらいに頬を染める美女が、激しいピストンに腰を跳ねさせ潮を噴き上げている——。",
    tags: ["マジックミラー", "MM号", "素人", "ナンパ", "露出", "中出し", "フェラチオ", "ハメ撮り"]
  },
  {
    id: "feature_corporate_receptionist_polite_seduction",
    query: "受付嬢",
    title: "【丁寧な敬語と完璧な笑顔の裏の性欲】企業の顔・受付嬢特集！総合受付のカウンター裏や応接室でスーツ姿のまま貪り尽くすハイレグ交尾AV名作選",
    category: "オフィス・制服",
    themeKeyword: "受付嬢・企業の顔・敬語・スカーフ・タイトスカート・応接室・カウンター裏",
    searchIntent: "大手企業の清楚で美しい受付嬢が、上品な制服とスカーフを身に着けたまま応接室やカウンター裏でハメ狂うAVを探しているユーザー向け",
    introTone: "大理石のエントランスに立つ、気品漂う美人受付嬢。完璧な笑顔と丁寧な敬語で案内された閉ざされた役員応接室。首元のシルクスカーフを解き、タイトスカートのスリットから溢れ出る淫らな蜜壺を、激しいピストンで満たす背徳のビジネスクラス——。",
    tags: ["受付嬢", "オフィス", "制服", "スカーフ", "タイトスカート", "中出し", "敬語", "美脚"]
  },
  {
    id: "feature_insurance_lady_pillow_sales_contract",
    query: "生保レディ",
    title: "【契約書と引き換えに捧げる熱い肉体】生保レディ特集！ノルマに追われた美人外交員が顧客の自宅でスーツを脱ぎ捨て乱れる枕営業AV名作選",
    category: "人妻・職業",
    themeKeyword: "生保レディ・保険外交員・枕営業・契約書・ノルマ・顧客自宅・スーツ",
    searchIntent: "保険の契約を取るために顧客の自宅を訪れ、胸元を開いて肉体関係を結ぶ生保レディのリアルな枕営業AVを探しているユーザー向け",
    introTone: "月末のノルマ達成に追われ、雨の日の夕暮れに顧客の自宅を訪れた生保外交員。テーブルに広げられた保険の設計書と、差し出された一杯のお茶。契約のサインと引き換えに、スーツのボタンを一つずつ外して畳の上に横たわる切実で生々しい大人の取引——。",
    tags: ["生保レディ", "保険外交員", "枕営業", "スーツ", "人妻", "中出し", "フェラチオ", "背徳"]
  },
  {
    id: "feature_shrine_maiden_miko_sacred_purification",
    query: "巫女 神社",
    title: "【白衣緋袴に包まれた聖域の処女肉】巫女・神社特集！厳かな社務所や神聖な拝殿で袴を脱がされ神への奉納として乱れ突かれる純潔交尾AV名作選",
    category: "和風・着物",
    themeKeyword: "巫女・神社・社務所・白衣緋袴・お祓い・神聖・純潔・奉納",
    searchIntent: "清楚で神聖な巫女さんが白衣緋袴姿のまま、神社の社務所や畳の上で袴をたくし上げられてハメられる和風シチュエーションAVを探しているユーザー向け",
    introTone: "静まり返る境内に響く玉砂利を踏む音と、風に揺れる木々のざわめき。穢れを知らない純白の衣と鮮やかな緋袴を纏った巫女。神聖な社務所の奥、注連縄が飾られた畳の上で袴の紐を解かれ、神聖な肉体に生々しい男の情欲が刻み込まれる——。",
    tags: ["巫女", "神社", "和風", "白衣緋袴", "純潔", "中出し", "美少女", "社務所"]
  },
  {
    id: "feature_noble_young_lady_and_maid_servant",
    query: "お嬢様 メイド",
    title: "【豪邸の天蓋ベッドで繰り広げられる秘密】お嬢様×専属メイド特集！世間知らずな令嬢をメイドが手取り足取り開発する百合＆主従AV名作選",
    category: "コスプレ・主従",
    themeKeyword: "お嬢様・メイド・豪邸・天蓋ベッド・主従・処女開発・レッスン",
    searchIntent: "箱入り娘のお嬢様が、専属メイドにお手入れや初夜の練習として体を開発される高貴で背徳的な主従関係AVを探しているユーザー向け",
    introTone: "広大な洋館の奥、レースの天蓋が揺れる豪華なベッドルーム。世間知らずで純真無垢なお嬢様と、長年仕える専属メイド。主従の垣根を越え、絹のような素肌を指先と舌で丹念に愛撫し、大人の快楽の扉をそっと開いていく優美で淫らな夜——。",
    tags: ["お嬢様", "メイド", "主従", "天蓋ベッド", "処女開発", "美少女", "中出し", "コスプレ"]
  },
  {
    id: "feature_gal_nurse_inpatient_ward_night_duty",
    query: "ギャル 看護師",
    title: "【ナースコールのたびに即尺してくれる病棟】ギャルナース特集！明るい髪色とミニスカ白衣で入院患者の溜まった精子を抜きまくる神対応AV名作選",
    category: "医療・ナース",
    themeKeyword: "ギャルナース・看護師・ナースコール・即尺・入院病棟・白衣・パイパン",
    searchIntent: "派手めで可愛いギャル看護師が、ナースコールで呼ばれるたびに病室で患者のチ○ポを笑顔で即尺・中出しさせてくれるAVを探しているユーザー向け",
    introTone: "深夜の病棟に響くナースコールの電子音。駆けつけてくれたのは、明るい茶髪にネイルを光らせたギャル看護師。「溜まって辛いんでしょ？」といたずらっぽく笑いながら、布団の中に潜り込み手際よく男根を咥え込む、患者だけの秘密の特別看護——。",
    tags: ["ギャル", "ナース", "看護師", "即尺", "病室", "白衣", "中出し", "フェラチオ"]
  },
  {
    id: "feature_black_skin_gal_aggressive_seduction",
    query: "黒ギャル 痴女",
    title: "【小麦色の小麦肌と本能剥き出しの腰使い】黒ギャル特集！ハイレグ水着と金髪小麦肌で男を跨ぎ限界まで搾り取るノンストップ逆レイプAV名作選",
    category: "ギャル・素人",
    themeKeyword: "黒ギャル・小麦肌・金髪・痴女・逆レイプ・騎乗位・搾り取り・爆乳",
    searchIntent: "肌が黒く焼けた派手な黒ギャルが、圧倒的な性欲と腰使いで男を組み敷き、連続射精させるエネルギッシュな痴女AVを探しているユーザー向け",
    introTone: "オイルでテラテラと輝く小麦色の引き締まった美ボディと、派手な金髪。ギラギラした太陽のように積極的な黒ギャルが、男の上に跨がり本能のままに腰を打ちつける。息をもつかせぬ激しい騎乗位ピストンで、男の精子を最後の一滴まで吸い尽くす——。",
    tags: ["黒ギャル", "小麦肌", "痴女", "騎乗位", "中出し", "逆レイプ", "巨乳", "爆乳"]
  },
  {
    id: "feature_tight_clothing_huge_breasts_fetish",
    query: "着衣巨乳",
    title: "【ニット越しに主張する圧倒的な質量】着衣巨乳特集！身体のラインを強調するピチピチニットやシャツのボタンが弾け飛ぶ神乳AV名作選",
    category: "巨乳・爆乳",
    themeKeyword: "着衣巨乳・ピチピチニット・胸強調・シャツ弾ける・パイズリ・谷間・重量感",
    searchIntent: "脱ぐ前が一番エロい！タイトなリブニットやシャツを着た巨乳美女が、服の上から揉みしだかれパイズリされる着衣フェチAVを探しているユーザー向け",
    introTone: "街中で誰もが思わず二度見してしまう、ピチピチのタートルネックニットを押し上げる爆乳の圧倒的シルエット。服を脱がせる前の張り詰めた布地越しに揉みしだく悦楽。布を捲り上げた瞬間にこぼれ落ちる豊潤な果実を、心ゆくまで貪り尽くす——。",
    tags: ["着衣巨乳", "巨乳", "ニット", "パイズリ", "爆乳", "中出し", "フェチ", "谷間"]
  }
];

function fetchFanzaAPI(keyword) {
  return new Promise((resolve) => {
    const url = `https://api.dmm.com/affiliate/v3/ItemList?api_id=${API_ID}&affiliate_id=${API_AFFILIATE_ID}&site=FANZA&service=digital&floor=videoa&hits=10&sort=rank&keyword=${encodeURIComponent(keyword)}&output=json`;
    https.get(url, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const json = JSON.parse(data);
          resolve(json?.result?.items || []);
        } catch (e) {
          resolve([]);
        }
      });
    }).on('error', () => resolve([]));
  });
}

function cleanAffiliateUrl(rawUrl) {
  if (!rawUrl) return "";
  let u = rawUrl.replace(/affiliate_id=[^&]+/, `affiliate_id=${OUT_AFFILIATE_ID}`);
  u = u.replace(/af_id=[^&]+/, `af_id=${OUT_AFFILIATE_ID}`);
  u = u.replace(/ch_id=[^&]+/, `ch_id=${OUT_AFFILIATE_ID}`);
  return u;
}

function generateInDepthArticle(theme, items) {
  const selectedItems = items.slice(0, 4);
  
  let bodyHtml = `
<div class="space-y-12 text-slate-200">
  <!-- イントロダクション -->
  <section class="bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 border border-pink-500/20 rounded-2xl p-6 md:p-8 shadow-xl">
    <div class="flex items-center gap-3 mb-4">
      <span class="px-3 py-1 bg-pink-500/20 text-pink-400 border border-pink-500/40 rounded-full text-xs font-semibold uppercase tracking-wider">厳選ディープ特集</span>
      <span class="text-xs text-slate-400">公式FANZA Web API リアルタイムデータ取得</span>
    </div>
    <h2 class="text-xl md:text-2xl font-bold text-white mb-4 leading-relaxed">${theme.title}</h2>
    <p class="text-slate-300 leading-relaxed mb-6">${theme.introTone}</p>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 p-4 bg-slate-950/60 rounded-xl border border-slate-700/50 text-sm">
      <div class="flex items-center gap-2">
        <span class="text-pink-400">🎯</span>
        <span class="text-slate-300"><strong>検索意図:</strong> ${theme.searchIntent}</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="text-pink-400">🔑</span>
        <span class="text-slate-300"><strong>中核キーワード:</strong> ${theme.themeKeyword}</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="text-pink-400">⚡</span>
        <span class="text-slate-300"><strong>収録作品数:</strong> 厳選${selectedItems.length}タイトル（全作API直結）</span>
      </div>
    </div>
  </section>

  <!-- 比較マトリクス表 -->
  <section class="space-y-4">
    <div class="flex items-center gap-2 border-l-4 border-pink-500 pl-3">
      <h3 class="text-lg md:text-xl font-bold text-white">【徹底比較】特集収録作品 スペック一覧マトリクス</h3>
    </div>
    <div class="overflow-x-auto rounded-xl border border-slate-700 bg-slate-900/80 shadow-md">
      <table class="w-full text-left text-xs md:text-sm text-slate-300 divide-y divide-slate-800">
        <thead class="bg-slate-950/80 text-pink-400 font-semibold">
          <tr>
            <th class="p-3">作品名 / 品番</th>
            <th class="p-3">主演出演者</th>
            <th class="p-3">メーカー / レーベル</th>
            <th class="p-3">抜きどころ・最大の見せ場</th>
            <th class="p-3 text-center">公式配信</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-slate-800/60">`;

  selectedItems.forEach(item => {
    const actresses = (item.iteminfo?.actress || []).map(a => a.name).join(', ') || '単体・企画女優';
    const maker = item.iteminfo?.maker?.[0]?.name || item.iteminfo?.label?.[0]?.name || '公式配信レーベル';
    const contentId = item.content_id || item.product_id;
    const affLink = cleanAffiliateUrl(item.affiliateURL || item.URL);
    
    bodyHtml += `
          <tr class="hover:bg-slate-800/40 transition">
            <td class="p-3 font-medium text-white max-w-xs truncate">${item.title} <br><span class="text-xs text-pink-400 font-mono">${contentId.toUpperCase()}</span></td>
            <td class="p-3 text-slate-300">${actresses}</td>
            <td class="p-3 text-slate-400">${maker}</td>
            <td class="p-3 text-slate-300">至近距離密着ピストン＆濃厚フィニッシュ</td>
            <td class="p-3 text-center"><a href="${affLink}" target="_blank" rel="noopener noreferrer" class="inline-block px-3 py-1 bg-pink-600 hover:bg-pink-500 text-white rounded text-xs font-semibold shadow">本編を見る</a></td>
          </tr>`;
  });

  bodyHtml += `
        </tbody>
      </table>
    </div>
  </section>

  <!-- 作品別徹底詳細レビュー（1作品ずつ長文解説） -->
  <section class="space-y-12">
    <div class="flex items-center gap-2 border-l-4 border-pink-500 pl-3">
      <h3 class="text-lg md:text-xl font-bold text-white">【完全個別レビュー】厳選収録作品の深層分析＆抜きどころ解説</h3>
    </div>`;

  selectedItems.forEach((item, index) => {
    const actresses = (item.iteminfo?.actress || []).map(a => a.name).join(' / ') || '厳選実力派キャスト';
    const maker = item.iteminfo?.maker?.[0]?.name || '公式メーカー';
    const label = item.iteminfo?.label?.[0]?.name || '公式レーベル';
    const contentId = item.content_id || item.product_id;
    const affLink = cleanAffiliateUrl(item.affiliateURL || item.URL);
    const imgUrl = item.imageURL?.large || item.imageURL?.small || '';
    const desc = item.iteminfo?.description || item.review?.first || item.title;
    const price = item.prices?.price || item.prices?.deliveries?.delivery?.[0]?.price || '各プラン対応';

    bodyHtml += `
    <article class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-6 md:p-8 space-y-6 shadow-2xl">
      <div class="flex flex-wrap items-center justify-between gap-2 pb-4 border-b border-slate-800">
        <span class="px-3 py-1 bg-pink-600 text-white font-bold text-xs rounded-full shadow">FILE 0${index + 1}</span>
        <span class="text-xs font-mono text-pink-400 tracking-wider">品番: ${contentId.toUpperCase()}</span>
      </div>

      <h4 class="text-lg md:text-2xl font-bold text-white leading-snug hover:text-pink-400 transition">${item.title}</h4>

      <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-start">
        <div class="md:col-span-5 space-y-3">
          <div class="relative overflow-hidden rounded-xl border border-slate-700 bg-slate-950 shadow-inner group">
            <img src="${imgUrl}" alt="${item.title}" class="w-full h-auto object-cover transform group-hover:scale-105 transition duration-300" loading="lazy" />
          </div>
          <div class="p-3 bg-slate-950/80 rounded-lg border border-slate-800 text-xs space-y-1 text-slate-400 font-mono">
            <div><strong class="text-slate-300 font-sans">出演女優:</strong> ${actresses}</div>
            <div><strong class="text-slate-300 font-sans">メーカー:</strong> ${maker}</div>
            <div><strong class="text-slate-300 font-sans">レーベル:</strong> ${label}</div>
            <div><strong class="text-slate-300 font-sans">参考価格:</strong> ${price}</div>
          </div>
          <a href="${affLink}" target="_blank" rel="noopener noreferrer" class="block w-full text-center py-3 px-4 bg-gradient-to-r from-pink-600 to-rose-600 hover:from-pink-500 hover:to-rose-500 text-white font-bold rounded-xl shadow-lg transform hover:-translate-y-0.5 transition duration-150">
            FANZA公式で作品詳細・本編を見る ➔
          </a>
        </div>

        <div class="md:col-span-7 space-y-4 text-slate-300 leading-relaxed text-sm md:text-base">
          <div class="p-4 bg-slate-950/50 rounded-xl border-l-2 border-pink-500">
            <h5 class="text-xs uppercase tracking-wider text-pink-400 font-bold mb-1">公式あらすじ / 作品概要</h5>
            <p class="text-xs md:text-sm text-slate-300 line-clamp-4 leading-relaxed">${desc}</p>
          </div>

          <div class="space-y-3">
            <h5 class="text-sm font-bold text-white flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-pink-500"></span> 本作が誇る3大抜きどころ・ハイライト
            </h5>
            <ul class="space-y-2 text-xs md:text-sm text-slate-300">
              <li class="p-2.5 bg-slate-800/40 rounded-lg border border-slate-700/50">
                <strong class="text-pink-300">① 状況のリアリティと焦らしの演出:</strong> 舞台設定の細部までこだわり抜かれた小道具とアングルが、見る者を完全にその場へと引きずり込みます。
              </li>
              <li class="p-2.5 bg-slate-800/40 rounded-lg border border-slate-700/50">
                <strong class="text-pink-300">② 吐息と水音が絡み合う極上ピストン:</strong> 逃げ場のない密着状態から放たれる執拗な腰使いに、女優陣が徐々に理性を失っていく絶頂シーンは圧巻。
              </li>
              <li class="p-2.5 bg-slate-800/40 rounded-lg border border-slate-700/50">
                <strong class="text-pink-300">③ 限界突破の濃厚フィニッシュ:</strong> 限界まで焦らされた末の大量射精・濃厚生中出しの瞬間まで余すところなく収録。
              </li>
            </ul>
          </div>

          <div class="p-3 bg-pink-950/20 border border-pink-900/40 rounded-lg text-xs text-pink-200">
            💡 <strong>おすすめ視聴シチュエーション:</strong> 深夜にイヤホン・ヘッドホンを装着し、吐息や衣擦れの音まで逃さず没入視聴するのが最も抜けるおすすめスタイルです。
          </div>
        </div>
      </div>
    </article>`;
  });

  bodyHtml += `
  </section>

  <!-- 視聴ガイド＆FAQ -->
  <section class="bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 space-y-6">
    <div class="flex items-center gap-2 border-l-4 border-pink-500 pl-3">
      <h3 class="text-lg md:text-xl font-bold text-white">【特集総括】このジャンルを最高に楽しむためのQ&A</h3>
    </div>
    <div class="space-y-4 text-sm text-slate-300">
      <div class="p-4 bg-slate-950/60 rounded-xl border border-slate-800">
        <h4 class="font-bold text-pink-400 mb-1">Q. なぜこのシチュエーションはこれほどまでに興奮をそそるのか？</h4>
        <p class="leading-relaxed">日常空間に潜む「触れてはならない境界線」を越えるスリルと、制服やシチュエーション特有の拘束感が、観る者の支配欲と背徳感を極限まで刺激するためです。</p>
      </div>
      <div class="p-4 bg-slate-950/60 rounded-xl border border-slate-800">
        <h4 class="font-bold text-pink-400 mb-1">Q. FANZA公式配信で視聴するメリットは？</h4>
        <p class="leading-relaxed">高画質ストリーミング再生はもちろん、スマホ・タブレットへのダウンロード保存にも対応。広告なしの完全シームレスな高音質環境で、女優の生々しい吐息や肌の質感を堪能できます。</p>
      </div>
    </div>
  </section>
</div>`;

  return bodyHtml;
}

async function run() {
  console.log("=== Starting generation of 20 brand-new high-depth feature articles (Batch 2) ===");
  const postsDir = path.join(__dirname, 'src', 'data', 'posts');

  let successCount = 0;
  for (let i = 0; i < targetThemes.length; i++) {
    const theme = targetThemes[i];
    console.log(`[${i+1}/${targetThemes.length}] Fetching API data for query: "${theme.query}" -> ${theme.id}`);
    
    const items = await fetchFanzaAPI(theme.query);
    if (!items || items.length < 3) {
      console.warn(`[WARN] Skipping ${theme.id}, insufficient items: ${items.length}`);
      continue;
    }

    const htmlContent = generateInDepthArticle(theme, items);
    const topItem = items[0];
    const topAffLink = cleanAffiliateUrl(topItem.affiliateURL || topItem.URL);
    const topImg = topItem.imageURL?.large || topItem.imageURL?.small || '';

    const postDoc = {
      id: theme.id,
      title: theme.title,
      content: htmlContent,
      published: new Date(Date.now() - ((i + 25) * 3600000)).toISOString(),
      updated: new Date().toISOString(),
      labels: theme.tags,
      author: {
        name: "背徳エロス編集部",
        url: "https://haitoku.pages.dev"
      },
      productInfo: {
        service_name: "デジタルアワード / FANZA公式",
        floor_name: "ビデオ動画",
        category_name: theme.category,
        content_id: topItem.content_id || topItem.product_id,
        title: topItem.title,
        URL: topAffLink,
        affiliateURL: topAffLink,
        imageURL: {
          large: topImg,
          list: topItem.imageURL?.list || topImg,
          small: topItem.imageURL?.small || topImg
        },
        actress: (topItem.iteminfo?.actress || []).map(a => a.name).join(', '),
        maker: topItem.iteminfo?.maker?.[0]?.name || '公式配信レーベル',
        sampleMovieURL: topItem.sampleMovieURL?.size_720_480 || topItem.sampleMovieURL?.size_480_360 || null
      }
    };

    const filePath = path.join(postsDir, `${theme.id}.json`);
    fs.writeFileSync(filePath, JSON.stringify(postDoc, null, 2), 'utf8');
    console.log(`✓ Generated: ${filePath} (Items: ${items.length})`);
    successCount++;

    await new Promise(r => setTimeout(r, 600));
  }

  console.log(`=== Complete! Successfully generated ${successCount} articles in Batch 2. ===`);
}

run();
