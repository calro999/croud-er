const fs = require('fs');
const path = require('path');
const https = require('https');

const API_ID = "4Lx0ftRf17Uuad6Ud7Gb";
const API_AFFILIATE_ID = "onchan555-999";
const OUT_AFFILIATE_ID = "onchan555-003";

const targetThemes = [
  {
    id: "feature_home_drinking_college_girl_drunk_hotel",
    query: "宅飲み 女子大生",
    title: "【終電逃した女子大生とワンルームの熱帯夜】宅飲み・泥酔女子大生特集！部屋着姿の無防備な寝姿から雪崩れ込む濃厚朝まで生ハメAV名作選",
    category: "女子大生・素人",
    themeKeyword: "宅飲み・女子大生・終電逃し・泥酔・ワンルーム・部屋着・朝まで生ハメ",
    searchIntent: "サークルや友人の宅飲みで終電を逃した女子大生が、酒の勢いと無防備な部屋着姿のままワンルームでハメ狂うリアル系AVを探しているユーザー向け",
    introTone: "缶ビールとチューハイの空き缶が転がる狭いワンルーム。終電を逃し、ほろ酔い気分で「もう泊めてよ」とベッドに倒れ込む女子大生。薄手のスウェットから覗く無防備な太ももと甘いアルコールの息遣い。理性のタガが外れた夜、朝を迎えるまで貪り尽くす宅飲みセックス——。",
    tags: ["宅飲み", "女子大生", "泥酔", "終電逃し", "ワンルーム", "部屋着", "生中出し", "素人風"]
  },
  {
    id: "feature_love_hotel_girls_party_secret_encounter",
    query: "ラブホ 女子会",
    title: "【キングサイズベッドと露天風呂付き女子会】ラブホ女子会特集！シャンパンでほろ酔いになった美女たちが乱入した男と乱れ狂うハーレムAV名作選",
    category: "シチュエーション",
    themeKeyword: "ラブホ女子会・スイートルーム・シャンパン・バスローブ・ハーレム・泥酔",
    searchIntent: "豪華なラブホテルのスイートルームで女子会を開いていた美女グループが、男を呼んで乱交やハーレム状態になる豪華絢爛なAVを探しているユーザー向け",
    introTone: "きらびやかなシャンデリアと巨大なキングサイズベッドが並ぶラブホテルのスイートルーム。バスローブ姿でシャンパンを煽り、開放的な空気に包まれた女子会。デリバリーや男友達の乱入により、いつしか女同士の身体の触れ合いから激しい乱交劇へと発展していく——。",
    tags: ["ラブホ女子会", "スイートルーム", "ハーレム", "乱交", "バスローブ", "中出し", "美少女", "シャンパン"]
  },
  {
    id: "feature_shared_table_izakaya_pickup_takeout",
    query: "相席 居酒屋",
    title: "【初対面の駆け引きとお持ち帰りの瞬間】相席居酒屋・ナンパ特集！アルコールと薄暗い個室で距離を縮めホテル直行で貪り合う即ハメAV名作選",
    category: "素人・ナンパ",
    themeKeyword: "相席居酒屋・ナンパ・お持ち帰り・初対面・個室・即ハメ・泥酔",
    searchIntent: "相席居酒屋で出会った素人風の女子2人組を巧みなトークとお酒でお持ち帰りし、ホテルで激しくハメるナンパドキュメント風AVを探しているユーザー向け",
    introTone: "賑やかな店内のざわめきと、乾杯のグラスがぶつかり合う相席居酒屋。テーブルの下で触れ合う膝と、視線が交差するたびに高まる緊張感。終電間際の会計を済ませ、タクシーに滑り込んで向かったラブホテルで、初対面とは思えないほど貪欲に求め合うリアルな肉欲劇——。",
    tags: ["相席居酒屋", "ナンパ", "お持ち帰り", "ホテル直行", "即ハメ", "中出し", "素人風", "女子大生"]
  },
  {
    id: "feature_karaoke_private_room_blind_spot_sex",
    query: "カラオケ 個室",
    title: "【大音量のBGMとモニターの死角】カラオケ個室特集！ドアの小窓から店員が覗くスリルに怯えつつソファの上で激しく腰を振る密室交尾AV名作選",
    category: "シチュエーション",
    themeKeyword: "カラオケ個室・大音量・ドア小窓・モニター死角・ソファ・声我慢・露出",
    searchIntent: "大音量で音楽が流れるカラオケボックスの個室で、店員がいつ入ってくるかわからないスリルの中でハメるシチュエーションAVを探しているユーザー向け",
    introTone: "重低音のBGMが響き渡るカラオケの完全個室。ドアのガラス窓に背を向け、モニターの光が明滅するソファの上。スカートをまくり上げ、店員の足音に怯えながらも大音量に紛れて腰を突き上げる。スリルと快楽が限界突破する密室のカーニバル——。",
    tags: ["カラオケ", "個室", "大音量", "ソファ", "声我慢", "中出し", "スリル", "ミニスカート"]
  },
  {
    id: "feature_internet_cafe_pair_seat_silent_climax",
    query: "漫画喫茶 ペアシート",
    title: "【薄いパーテーションと静寂のブース】ネットカフェ・漫画喫茶特集！防音性のないペアシートのフラットマットで息を殺してイキ乱れる名作選",
    category: "シチュエーション",
    themeKeyword: "漫画喫茶・ネットカフェ・ペアシート・フラットマット・薄い壁・サイレント・息を殺して",
    searchIntent: "漫画喫茶やネカフェのフラットペアシートで、周囲に音が筒抜けな中で息を殺してハメ合うサイレント系AVを探しているユーザー向け",
    introTone: "キーボードのタイピング音だけが響く静まり返ったネットカフェ。天井の空いた薄いパーテーションで区切られたペアシートのフラットマット。靴を脱ぎ、至近距離で重なり合う二人の体。声を漏らせば隣のブースに即座にバレる極限状態での濃厚サイレント交尾——。",
    tags: ["漫画喫茶", "ネットカフェ", "ペアシート", "フラットマット", "サイレント", "声我慢", "中出し", "素人風"]
  },
  {
    id: "feature_drive_recorder_car_sex_secret_footage",
    query: "ドライブレコーダー",
    title: "【車載カメラが記録した衝撃の車内情事】ドライブレコーダー・流出特集！駐車中の車内で繰り広げられる生々しいフェラと密着性交の決定版AV名作選",
    category: "素人・ハメ撮り",
    themeKeyword: "ドライブレコーダー・ドラレコ・車載カメラ・車内SEX・流出・固定視点・リアリティ",
    searchIntent: "ドライブレコーダーの固定カメラ目線で、車内で密かに行われるリアルなセックスやフェラチオが記録されたドキュメント風AVを探しているユーザー向け",
    introTone: "フロントガラスの内側に設置されたドライブレコーダーの広角レンズ。夜のコインパーキング、エンジンを切った静寂の車内で、助手席のシートを倒し重なり合う男女。カメラの存在を意識しながらも溢れ出る性欲を抑えきれず、車体を軋ませるリアルな記録映像——。",
    tags: ["ドライブレコーダー", "車内セックス", "ドラレコ", "固定カメラ", "流出風", "中出し", "リアル", "ハメ撮り"]
  },
  {
    id: "feature_security_camera_surveillance_secret_coitus",
    query: "防犯カメラ",
    title: "【監視モニターに映し出された真夜中の情事】防犯カメラ・監視映像特集！誰もいない夜のオフィスや店舗の死角で繰り広げられる禁断交尾AV名作選",
    category: "シチュエーション",
    themeKeyword: "防犯カメラ・監視カメラ・モノクロ映像・夜間オフィス・店舗裏・死角・背徳",
    searchIntent: "オフィスの廊下や店舗の防犯カメラのモノクロアングルから、深夜に男女が密かに交わる背徳的な映像を捉えたマニアックなAVを探しているユーザー向け",
    introTone: "無機質なタイムスタンプが時を刻む監視カメラのモノクロモニター。深夜0時を回ったオフィスのフロア、残業中の男女が人目を忍んで重なり合う。カメラのレンズが冷徹に見つめる中、デスクに手をつき激しく腰を振る背徳の記録——。",
    tags: ["防犯カメラ", "監視カメラ", "夜間オフィス", "死角", "モノクロ", "中出し", "職場不倫", "リアル"]
  },
  {
    id: "feature_father_in_law_cohabitation_secret_affair",
    query: "同居 義父",
    title: "【旦那が不在の家で繰り返される背徳の契り】同居・義父×若妻特集！台所や居間で義父のたくましい男根に屈し快楽堕ちしていく禁断近親AV名作選",
    category: "人妻・家庭内",
    themeKeyword: "義父・同居・若妻・昼下がり・旦那不在・近親相姦・快楽堕ち・背徳",
    searchIntent: "義理の父親と同居する若妻が、夫の留守中に義父に言い寄られ、罪悪感を抱きながらも身体の相性に屈していく近親背徳AVを探しているユーザー向け",
    introTone: "夫が出勤したあとの静まり返る一軒家。義父の重たい足音が廊下に響く。洗濯物を畳む若妻の背後から伸びる無骨な手。最初は拒んでいたものの、夫とは違う濃厚で強引な愛撫にいつしか身体が熱く疼き、畳の上で義父の肉棒を貪る禁断の昼下がり——。",
    tags: ["義父", "同居", "人妻", "若妻", "近親相姦", "中出し", "背徳", "家庭内不倫"]
  },
  {
    id: "feature_daughter_in_law_and_father_in_law_affair",
    query: "息子の嫁",
    title: "【息子には言えない秘密の快楽指導】息子の嫁×義父特集！初々しい若妻を義父が手取り足取り調教し濃厚生中出しを注ぎ込む家庭内背徳AV名作選",
    category: "人妻・家庭内",
    themeKeyword: "息子の嫁・義父・若妻・調教・生中出し・家庭内・秘密・寝取られ",
    searchIntent: "息子の結婚相手である清楚な若嫁を、義父が弱みを握ったり巧みに誘惑して自分専用の肉便器へと調教していくAVを探しているユーザー向け",
    introTone: "新婚ホヤホヤの息子の嫁。まだぎこちない笑顔を見せる清楚な若妻に、義父の歪んだ情欲が牙をむく。「息子のために大人の身体を教えてやる」という名目で開かれた太ももの奥、純白の肌に刻み込まれる義父の生々しい遺伝子——。",
    tags: ["息子の嫁", "義父", "人妻", "調教", "生中出し", "家庭内", "NTR", "熟女"]
  },
  {
    id: "feature_husband_business_transfer_solitary_affair",
    query: "単身赴任",
    title: "【夫が遠く離れた街で過ごす寂しい夜に】単身赴任妻特集！寂しさを埋めるように近所の男や元カレを自宅に招き入れ朝まで乱れ狂う不倫AV名作選",
    category: "人妻・不倫",
    themeKeyword: "単身赴任・人妻・孤独・寂しさ・浮気・自宅不倫・朝まで・欲求不満",
    searchIntent: "夫が単身赴任で家を空けている人妻が、孤独と性欲に耐えかねて自宅に男を連れ込み、ベッドで貪り合うリアルな不倫AVを探しているユーザー向け",
    introTone: "夫が地方へ単身赴任して半年。広すぎるダブルベッドに一人横たわる夜の冷たさ。乾いた心と身体を満たすため、鍵を開けて招き入れた男。夫の写真が飾られた部屋で、激しいピストンにシーツを握りしめながら絶頂の波に身を任せる——。",
    tags: ["単身赴任", "人妻", "孤独", "不倫", "欲求不満", "ダブルベッド", "中出し", "生ハメ"]
  },
  {
    id: "feature_home_visit_massage_erotic_touch_creampie",
    query: "出張マッサージ",
    title: "【自宅の布団で受けるきわどい密着施術】出張訪問マッサージ特集！女性セラピストや人妻客がオイルまみれで境界線を越える本番サービスAV名作選",
    category: "エステ・マッサージ",
    themeKeyword: "出張マッサージ・訪問エステ・自宅施術・オイル・鼠蹊部・本番行為・密着",
    searchIntent: "自宅に呼んだ出張マッサージ師と徐々にきわどい施術になり、最終的に本番セックスへと発展するリアルなマッサージAVを探しているユーザー向け",
    introTone: "呼び鈴が鳴り、玄関を開けると現れたのは大きな施術バッグを持った美人セラピスト。自宅のリビングに敷かれたマットの上、温かいオイルが素肌に塗り伸ばされる。際どい鼠蹊部のマッサージから、互いの息が荒くなり自然と重なり合う至福のプライベート施術——。",
    tags: ["出張マッサージ", "訪問エステ", "オイル", "鼠蹊部", "自宅", "中出し", "密着", "本番"]
  },
  {
    id: "feature_mens_esthe_close_contact_aroma_creampie",
    query: "メンズエステ 密着",
    title: "【紙パンツ一枚の限界ギリギリ密着施術】メンズエステ特集！密着オイルトリートメントと甘い吐息で焦らされ抜きあり本番に雪崩れ込む神回AV名作選",
    category: "風俗・エステ",
    themeKeyword: "メンズエステ・メンエス・密着・紙パンツ・オイル・抜きあり・本番・添い寝",
    searchIntent: "人気のメンズエステで、可愛いセラピストが薄着で密着し、紙パンツをずらして本番セックスまでしてくれる裏オプ系AVを探しているユーザー向け",
    introTone: "アロマの香りが満ちるマンションの一室。薄手のワンピース一枚の美人セラピストが、全身を使って滑り込むように行う密着マッサージ。紙パンツ越しに伝わる柔らかな太ももの感触と、耳元で囁かれる甘い淫語に理性が限界を迎え、本番交尾へと突入する——。",
    tags: ["メンズエステ", "メンエス", "密着", "オイルマッサージ", "紙パンツ", "本番", "中出し", "癒やし"]
  },
  {
    id: "feature_delivery_health_hotel_secret_honban",
    query: "デリヘル 本番",
    title: "【パネル以上の極上美女が部屋にやってきた】デリヘル本番特集！ビジネスホテルのドアを開けた瞬間から始まる濃厚生中出し即ハメAV名作選",
    category: "風俗・デリヘル",
    themeKeyword: "デリヘル・派遣風俗・ビジネスホテル・本番生ハメ・即尺・生中出し・素人風",
    searchIntent: "ビジネスホテルに呼んだデリヘル嬢が、予想以上の極上美女で、部屋に入った瞬間から濃厚な本番セックスを堪能させてくれるAVを探しているユーザー向け",
    introTone: "出張先の味気ないビジネスホテルの客室。ノックの音とともに現れたのは、街で見かけるような清楚な美女。「今日はいっぱい気持ちよくなってくださいね」と微笑みながら、ベッドの上で惜しみなく身体を捧げてくれる極上のデリヘルナイト——。",
    tags: ["デリヘル", "ビジネスホテル", "本番", "生中出し", "即尺", "風俗", "美少女", "素人風"]
  },
  {
    id: "feature_pink_salon_oral_service_facial_finish",
    query: "ピンサロ",
    title: "【薄暗いボックス席でのお口の極上ご奉仕】ピンサロ特集！入店から退店までひたすら咥え込まれ喉奥まで突っ込む濃厚口淫バキュームAV名作選",
    category: "風俗・フェラ",
    themeKeyword: "ピンサロ・ピンクサロン・ボックス席・お口のご奉仕・即尺・深喉・ごっくん",
    searchIntent: "ピンサロの薄暗い店内で、可愛い女の子がひたすら一生懸命にフェラチオや手コキで抜いてくれる口淫特化AVを探しているユーザー向け",
    introTone: "ネオンが妖しく光るピンサロの狭いボックス席。ズボンを下ろした瞬間に温かい唇で迎えられる男根。ジュポジュポと店内に響く淫らな水音と、上目遣いで見つめられながら喉の奥深くまで咥え込まれる極上のオーラルバキューム——。",
    tags: ["ピンサロ", "ピンクサロン", "フェラチオ", "即尺", "口内射精", "ごっくん", "風俗", "ディープスロート"]
  },
  {
    id: "feature_soapland_bath_body_wash_foam_dance",
    query: "ソープ",
    title: "【マットの上で滑り合う最高峰の肉体美】ソープランド特集！泡踊り洗体から始まる至福のぬくもりと子宮口まで突き入れる完全奉仕AV名作選",
    category: "風俗・ソープ",
    themeKeyword: "ソープランド・ソープ・洗体・泡踊り・ローションマット・完全奉仕・極上風俗",
    searchIntent: "高級ソープランドで、極上の美女が泡だらけになって全身で洗体してくれ、マットの上で滑りながらハメ合う最高峰の風俗AVを探しているユーザー向け",
    introTone: "湯気立ち込めるバスルーム、専用マットの上に敷き詰められた滑らかな泡。全身を泡まみれにした極上ソープ嬢が、自身の豊かなバストとヒップを擦り付けながら行う官能の泡踊り。滑走する快感の果て、ベッドの上で貪り合う最高級の性の歓喜——。",
    tags: ["ソープランド", "ソープ", "洗体", "泡踊り", "マット", "ローション", "中出し", "完全奉仕"]
  },
  {
    id: "feature_body_washing_sensual_foam_bath_creampie",
    query: "洗体",
    title: "【泡にまみれて擦り合う官能の素肌】洗体・お風呂特集！温かいシャワーと濃密な泡で全身を隅々まで愛撫され洗い流される極上バスタイムAV名作選",
    category: "お風呂・洗体",
    themeKeyword: "洗体・お風呂・泡・シャワー・バスルーム・全身愛撫・素肌密着",
    searchIntent: "お風呂場で美女に全身を泡だらけで洗われながら、股間や敏感な部分を念入りに刺激される洗体シチュエーションAVを探しているユーザー向け",
    introTone: "白いタイル張りのバスルーム、温かいシャワーの湯気。スポンジと豊かな泡を手に、爪先から首筋まで丁寧に洗い上げる美女。次第に泡の手は股間へと伸び、滑らかな泡の潤滑の中で擦れ合う素肌。湯船の中でそのまま繋がる至極の入浴交尾——。",
    tags: ["洗体", "お風呂", "バスルーム", "泡", "シャワー", "中出し", "密着", "美肌"]
  },
  {
    id: "feature_foam_dance_lotion_slide_intense_sex",
    query: "泡踊り",
    title: "【ローションと泡が織りなす極限の滑走感】泡踊り特集！マットの上で全身の体重を乗せて滑り込む究極のボディスライダー交尾AV名作選",
    category: "風俗・ソープ",
    themeKeyword: "泡踊り・ローション・スライダー・マット・摩擦ゼロ・全身密着・激ピストン",
    searchIntent: "ローションと泡がたっぷり塗られたマットの上で、女性が全身を使って男の上を滑りまくるダイナミックな泡踊りAVを探しているユーザー向け",
    introTone: "摩擦係数ゼロのマットの上、大量のローションとキメ細やかな泡。助走をつけて男の身体の上へと滑り込むソープ嬢の柔肌。ヌルヌルと滑り合う快感の中、体勢を変えながら一気に奥深くまで貫く。水飛沫と泡を撒き散らしながら絶頂へと昇りつめる——。",
    tags: ["泡踊り", "ローション", "マット", "ソープ", "滑走", "中出し", "巨乳", "美尻"]
  },
  {
    id: "feature_happening_bar_wife_swapping_experience",
    query: "ハプニングバー",
    title: "【仮面の下で剥き出しになる乱交と背徳】ハプニングバー特集！人妻やカップルが暗がりの中で見知らぬ男たちに抱かれ乱れ狂うリアルNTR名作選",
    category: "素人・NTR",
    themeKeyword: "ハプニングバー・カップル喫茶・乱交・見せ合い・人妻NTR・暗がり・仮面",
    searchIntent: "ハプニングバーに連れてこられた素人人妻や彼女が、周囲の客に見られながら他の男に生ハメされる背徳的なNTR・乱交AVを探しているユーザー向け",
    introTone: "妖しい紫色の照明と、重厚なカーテンで仕切られたプレイルーム。仮面をつけた男女が入り乱れる大人の秘密基地。夫の目の前で、見知らぬ筋骨隆々な男たちに代わる代わる貫かれる若妻。見られる羞恥が最高の快楽へと反転する禁断のハプニング——。",
    tags: ["ハプニングバー", "乱交", "NTR", "人妻", "カップル喫茶", "中出し", "露出", "背徳"]
  },
  {
    id: "feature_swimwear_bikini_tanning_pool_creampie",
    query: "水着ギャル 海の家",
    title: "【真夏の太陽に焼かれた小麦肌の肉欲】ビーチ・ビキニギャル特集！露出度の高い極小水着をずらし砂浜の物陰やパラソルの下で貪る生ハメ名作選",
    category: "ギャル・水着",
    themeKeyword: "ビキニギャル・極小水着・小麦肌・パラソル・砂浜・野外露出・生ハメ",
    searchIntent: "海辺で極小マイクロビキニを着たスタイル抜群のギャルが、パラソルの下や岩陰で大胆に生ハメされる真夏の野外AVを探しているユーザー向け",
    introTone: "眩しい日差しが照りつける海岸線。Tバックのマイクロビキニからこぼれ落ちそうな豊満な美尻と胸元。パラソルの影に連れ込まれ、砂まみれになりながら極小ビキニを横にずらされる。波の音にかき消されながら、真夏の情熱のままに注ぎ込まれる白濁液——。",
    tags: ["ビキニ", "水着ギャル", "小麦肌", "野外", "露出", "中出し", "美尻", "真夏"]
  },
  {
    id: "feature_private_room_internet_cafe_secret_affair",
    query: "漫画喫茶 ペアシート",
    title: "【鍵付き完全個室の密閉された空間】最新ネットカフェ完全個室特集！防音フラットルームの鍵を閉めて二人きりで貪り尽くす防音個室交尾AV名作選",
    category: "シチュエーション",
    themeKeyword: "ネットカフェ・鍵付き完全個室・防音・フラットシート・二人きり・密室",
    searchIntent: "最新の鍵付き防音個室ネットカフェで、外を気にせず大声で喘ぎながらハメ倒すリアルなネカフェAVを探しているユーザー向け",
    introTone: "重厚な鍵付きドアで完全に密閉された最新型ネットカフェのフラット個室。外の雑踏を完全にシャットアウトした二人だけの空間。マットの上に倒れ込み、周りを気にせず思い切り声を上げながら腰を打ち付け合う、現代のプライベート密室エロス——。",
    tags: ["ネットカフェ", "完全個室", "防音", "フラットシート", "中出し", "美少女", "密室", "即ハメ"]
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
  console.log("=== Starting generation of 20 brand-new high-depth feature articles (Batch 4) ===");
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
      published: new Date(Date.now() - ((i + 75) * 3600000)).toISOString(),
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

  console.log(`=== Complete! Successfully generated ${successCount} articles in Batch 4. ===`);
}

run();
