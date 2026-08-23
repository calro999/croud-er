const fs = require('fs');
const path = require('path');
const https = require('https');

const API_ID = "4Lx0ftRf17Uuad6Ud7Gb";
const API_AFFILIATE_ID = "onchan555-999";
const OUT_AFFILIATE_ID = "onchan555-003";

const targetThemes = [
  {
    id: "feature_barista_cafe_counter_creampie",
    query: "バリスタ",
    title: "【芳醇な珈琲アロマと禁断の密着交尾】美人バリスタ特集！エプロン越しの豊満な曲線とカウンター裏で貪り合う濃厚生中出しAV名作選",
    category: "シチュエーション",
    themeKeyword: "美人バリスタ・カフェ店員・エプロン密着・カウンター裏セックス",
    searchIntent: "カフェ店員や美人バリスタがエプロン姿のまま店内でハメ狂う背徳的な作品を探しているユーザー向け",
    introTone: "挽きたての豆の香ばしい薫りとスチームミルクの甘い蒸気が満ちるお洒落なカフェ空間。しかしカウンターの裏側、客席の死角では、清楚なエプロンをたくし上げ、店長や常連客の猛々しい男根を受け止める美しきバリスタたちの淫らな姿があった——。",
    tags: ["バリスタ", "カフェ店員", "エプロン", "職場セックス", "カウンター裏", "中出し", "美少女", "フェラチオ"]
  },
  {
    id: "feature_dentist_dental_hygienist_chair_creampie",
    query: "歯科衛生士",
    title: "【診療台の上で無防備に開く美肉】歯科衛生士・美人女医特集！胸元押し当て密着治療から雪崩れ込む背徳生ハメ診察AV名作選",
    category: "医療・ナース",
    themeKeyword: "歯科衛生士・歯科医・診療台セックス・密着治療・白衣",
    searchIntent: "歯医者での治療中に胸を押し当てられたり、診察台の上で無防備な体勢のまま開発されるマニアックなAVを探しているユーザー向け",
    introTone: "無機質なタービンの回転音と消毒液の匂いが漂うデンタルクリニック。リクライニングされた診療台の上、至近距離で覆いかぶさる歯科衛生士の柔らかな胸の感触と、息がかかるほどの距離で交わされる背徳の愛撫が男の理性を木っ端微塵に粉砕する——。",
    tags: ["歯科衛生士", "歯科医", "診察室", "診療台", "密着治療", "巨乳", "中出し", "フェラチオ"]
  },
  {
    id: "feature_cabin_attendant_layover_hotel_sex",
    query: "キャビンアテンダント",
    title: "【フライト後の極上ステイ先密会】客室乗務員（CA）特集！美脚タイトスカートを破り捨て高級ホテルで乱れ咲くハイステータス肉欲AV名作選",
    category: "職業・制服",
    themeKeyword: "キャビンアテンダント・CA・客室乗務員・フライトアテンダント・ステイ先ホテル・美脚スリット",
    searchIntent: "清楚で高嶺の花であるキャビンアテンダント（CA）がステイ先のホテルで乱れる高画質・本格AVを探しているユーザー向け",
    introTone: "国際線の長いフライトを終え、張り詰めた緊張感から解放されたステイ先の異国の高級ホテル。完璧なマナーと気品を纏った美人キャビンアテンダントが、スリットの入ったタイトスカートを脱ぎ捨て、パイロットや富裕層乗客の貪欲なピストンに喘ぎ狂う——。",
    tags: ["キャビンアテンダント", "CA", "スプレッドレッグ", "美脚", "タイトスカート", "高級ホテル", "中出し", "不倫"]
  },
  {
    id: "feature_business_trip_bullet_train_green_car",
    query: "新幹線",
    title: "【座席シート越しの息を殺した逢瀬】新幹線・出張移動特集！グリーン車のシート越しや多目的室で声押し殺しイキ乱れる背徳性交AV名作選",
    category: "シチュエーション",
    themeKeyword: "新幹線・グリーン車・出張・移動中・多目的室・声我慢",
    searchIntent: "出張の新幹線移動中やグリーン車、トイレ・多目的室で人目を忍んで行われるスリリングなセックスAVを探しているユーザー向け",
    introTone: "時速300kmで疾走する新幹線の車内。静まり返ったグリーン車の座席シートの隙間から滑り込む手、ブランケットの下で蠢く指先。隣の乗客に気づかれぬよう必死に声を殺しながら、絶頂の波に身悶える出張帰りの男女が織りなす極上の移動中エロス——。",
    tags: ["新幹線", "出張", "グリーン車", "移動中", "声我慢", "露出", "中出し", "OL"]
  },
  {
    id: "feature_convenience_store_night_shift_backroom",
    query: "コンビニ 夜勤",
    title: "【防犯カメラの死角で贪る背徳】深夜コンビニ夜勤バイト特集！バックヤードの冷たいスチール棚に押し付け乱れ合う生交尾AV名作選",
    category: "シチュエーション",
    themeKeyword: "コンビニ夜勤・深夜バイト・バックヤード・制服・防犯カメラ死角",
    searchIntent: "深夜のコンビニバイト中、バックヤードやレジ裏で二人きりになった男女が制服姿のまま交わる背徳AVを探しているユーザー向け",
    introTone: "深夜2時の青白い蛍光灯に照らされたコンビニエンスストア。来客チャイムが鳴り止んだ静寂の合間、防犯カメラの死角となるバックヤードで、揃いの制服を脱ぎ捨て段ボールの山に組み敷かれるバイト美女たちの生々しい情欲の交歓——。",
    tags: ["コンビニ", "夜勤", "バックヤード", "制服", "生ハメ", "中出し", "女子大生", "職場不倫"]
  },
  {
    id: "feature_open_air_bath_mixed_hot_spring_inn",
    query: "混浴 露天風呂",
    title: "【湯煙の向こうに浮かぶ生肌】秘湯・混浴露天風呂特集！タオル一枚の無防備な肉体に欲情し湯船の中で絡み合う濃厚生ハメ温泉AV名作選",
    category: "温泉・旅情",
    themeKeyword: "混浴・露天風呂・秘湯・温泉旅館・タオル一枚・湯船セックス",
    searchIntent: "秘湯の混浴露天風呂で偶然居合わせた美女や若妻とタオル越しに密着し、湯船の中で生ハメする温泉シチュエーションAVを探しているユーザー向け",
    introTone: "立ち込める硫黄の香りと澄んだせせらぎの音。乳白色の湯煙の彼方に現れた、濡れそぼるタオル一枚の無防備な女体。視線が交差した瞬間に加速する鼓動、湯船の中で触れ合う濡れた太ももと熱を帯びた欲望が溶け合う極上の混浴温泉劇——。",
    tags: ["混浴", "露天風呂", "温泉", "秘湯", "タオル一枚", "素人風", "中出し", "野外露出"]
  },
  {
    id: "feature_gym_personal_trainer_hip_thrust",
    query: "パーソナルトレーナー",
    title: "【タイトスパッツに浮き出る極上美尻】美人パーソナルトレーナー特集！汗ばむ密着トレーニング指導から雪崩れ込む筋膜リリース交尾AV名作選",
    category: "スポーツ・フィットネス",
    themeKeyword: "パーソナルトレーナー・フィットネス・美尻・タイトスパッツ・密着指導・汗だく",
    searchIntent: "鍛え抜かれた肉体美を持つ美人パーソナルトレーナーがスパッツ姿で密着指導し、そのまま性交に発展するエロティックなフィットネスAVを探しているユーザー向け",
    introTone: "引き締まった美くびれと、薄手のタイトスパッツに浮かび上がる丸みを帯びた大臀筋。プライベートジムの完全個室で、汗ばむ素肌を擦り付けながら行われるマンツーマンのストレッチ指導は、次第に互いの肉欲を限界まで追い込む筋膜リリース交尾へと変貌する——。",
    tags: ["パーソナルトレーナー", "フィットネス", "美尻", "スパッツ", "汗だく", "中出し", "巨乳", "アスリート"]
  },
  {
    id: "feature_golf_lesson_swing_guidance_seduction",
    query: "ゴルフ レッスン",
    title: "【背後からの密着スイング指導の甘い罠】美人ゴルフレッスンプロ特集！インドア個室で後ろから抱きすくめられ貫かれる背徳レッスンAV名作選",
    category: "スポーツ・フィットネス",
    themeKeyword: "ゴルフレッスン・ミニスカウェア・密着スイング・インドアゴルフ・背後挿入",
    searchIntent: "美人ゴルフインストラクターやミニスカ姿の生徒が、個室シミュレーションゴルフ場で背後から密着されハメられるAVを探しているユーザー向け",
    introTone: "鮮やかなミニスカートのゴルフウェアからスラリと伸びる健康的な美脚。インドア練習場の打席ブースで、アドレスの姿勢をとる美女の背後からぴったりと密着する腰の感触。クラブを握る手に重なる指先と、スイングの指導にかこつけて滑り込む肉棒の甘い痺れ——。",
    tags: ["ゴルフ", "ミニスカート", "レッスンプロ", "背後密着", "中出し", "美脚", "スポーツウェア"]
  },
  {
    id: "feature_female_boss_hotel_room_sharing",
    query: "女上司 相部屋",
    title: "【普段の威厳が蕩ける熱帯夜】女上司×出張相部屋特集！酒に酔い隙だらけになったキャリアウーマンをベッドに押し倒す下剋上交尾AV名作選",
    category: "オフィス・OL",
    themeKeyword: "女上司・出張相部屋・泥酔・キャリアウーマン・下剋上セックス・スーツ",
    searchIntent: "会社では冷徹で厳しい美人上司が出張先のホテル相部屋で酒に酔い、部下に抱かれて雌の顔を見せる下剋上シチュエーションAVを探しているユーザー向け",
    introTone: "職場では一切の隙を見せない敏腕美人上司。だが、取引先との飲み会を終え、手違いで同室となったツインルームの扉を閉めた瞬間、スーツを脱ぎ捨て下着姿でベッドに倒れ込む。理性のタガが外れた夜、立場を逆転させた部下の貪欲な攻めに甘い嬌声を響かせる——。",
    tags: ["女上司", "相部屋", "出張", "泥酔", "下剋上", "OL", "中出し", "スーツ"]
  },
  {
    id: "feature_apartment_neighbor_thin_wall_affair",
    query: "隣人 壁",
    title: "【薄い壁一枚越しに響く淫らな吐息】隣人妻・隣の部屋特集！壁から伝わる喘ぎ声に発情した隣人同士が境界を越えて貪り合う濃厚不倫AV名作選",
    category: "人妻・団地",
    themeKeyword: "隣人・アパート隣室・壁薄・喘ぎ声・隣の奥さん・クレームから不倫",
    searchIntent: "アパートの薄い壁越しに聞こえる声に欲情し、隣の住人や若妻と部屋を行き来して生ハメするリアルな近隣背徳AVを探しているユーザー向け",
    introTone: "木造アパートの薄い石膏ボード一枚を隔てた向こう側から、毎夜漏れ聞こえてくる生々しいベッドの軋みと湿り気を帯びた吐息。壁に耳を当ててオナニーしていた欲望の限界点。クレームをつける名目で開かれた隣室のドアの先で、二人は飢えた獣のように重なり合う——。",
    tags: ["隣人", "壁薄", "人妻", "不倫", "喘ぎ声", "アパート", "生中出し", "密着"]
  },
  {
    id: "feature_tutor_parent_teacher_private_lesson",
    query: "家庭教師 母親",
    title: "【子供が机に向かう隣室で交わす密約】教え子の母親×家庭教師特集！静まり返るリビングで息を殺して突く背徳の教育指導AV名作選",
    category: "人妻・不倫",
    themeKeyword: "家庭教師・生徒の母親・人妻・お茶出し・隣室セックス・息を殺して",
    searchIntent: "子供の家庭教師をしに訪れた先で、欲求不満な教え子の母親から誘惑され、子供が勉強している隣の部屋でハメ狂うAVを探しているユーザー向け",
    introTone: "子供部屋のドアの向こうでシャーペンの走る音が響く中、お茶を運んできた母親の無防備な胸元と擦れ合う柔肌。家庭の悩みを聞き出すうちに密着する距離感。子供に気づかれぬよう口元を手で塞ぎながら、リビングのソファで激しく腰を打ち付ける禁断の情事——。",
    tags: ["家庭教師", "人妻", "母親", "不倫", "声我慢", "中出し", "熟女", "教育ママ"]
  },
  {
    id: "feature_camp_tent_sleeping_bag_midnight_sex",
    query: "キャンプ テント",
    title: "【満天の星空と狭いテント内の濃厚密着】キャンプ・アウトドア特集！シュラフ（寝袋）に滑り込み吐息漏らす大自然の野外生交尾AV名作選",
    category: "野外・露出",
    themeKeyword: "キャンプ・テント・シュラフ・寝袋・大自然・アウトドア・夜這い",
    searchIntent: "キャンプ場の狭いテント内や寝袋の中で、外の気配を感じながら密着して行われるアウトドアセックスAVを探しているユーザー向け",
    introTone: "静寂に包まれた夜のキャンプ場、テントのフライシートを打つ夜風の音。外気温の低さとは対照的に、ひとつのシュラフ（寝袋）に滑り込んだ二人の素肌から立ち上る熱気。大自然の闇に包まれながら、布一枚隔てた外の気配に怯えつつも貪り合う極上のアウトドア密着愛——。",
    tags: ["キャンプ", "テント", "シュラフ", "野外", "露出", "中出し", "美少女", "アウトドア"]
  },
  {
    id: "feature_sauna_capsule_hotel_midnight_massage",
    query: "サウナ エステ",
    title: "【熱気と汗にまみれたととのい絶頂】個室サウナ＆垢すりエステ特集！限界まで火照った柔肌にオイルを塗りたくり貪り尽くす発汗交尾AV名作選",
    category: "エステ・マッサージ",
    themeKeyword: "サウナ・個室サウナ・垢すり・オイルエステ・発汗・熱気・ととのい",
    searchIntent: "サウナ施設やプライベートサウナ、垢すりエステで汗だくになった男女が火照った体のまま交わる発汗シチュエーションAVを探しているユーザー向け",
    introTone: "立ち込めるアロマロウリュの熱波と、玉のように噴き出す汗。火照りきった素肌に冷たいオイルが垂らされ、滑り合う肉体同士の生々しい摩擦音。心拍数が跳ね上がり、究極の「ととのい」の向こう側へと突き抜ける極上サウナセックスの悦楽——。",
    tags: ["サウナ", "エステ", "オイルマッサージ", "汗だく", "垢すり", "中出し", "巨乳", "発汗"]
  },
  {
    id: "feature_cosplay_event_dressing_room_secret",
    query: "コスプレ 更衣室",
    title: "【パーテーションの裏の生々しい素肌】コスプレ更衣室特集！撮影会・イベント舞台裏の熱気の中で衣装を半分脱がされ乱れる背徳性交AV名作選",
    category: "コスプレ・アキバ",
    themeKeyword: "コスプレ更衣室・撮影会・イベント裏・パーテーション・衣装半脱ぎ・カメコ",
    searchIntent: "イベント会場の更衣室や撮影スタジオの控え室で、コスプレイヤーが衣装を着崩したままハメられるマニアックなAVを探しているユーザー向け",
    introTone: "熱気渦巻く即売会・撮影会イベントの舞台裏。パーテーションで仕切られただけの薄暗い更衣スペースで、ウィッグを乱しキャラ衣装をたくし上げた美少女コスプレイヤー。カメラマンの要求に流されるまま、生々しい肉欲のピストンに身を委ねる——。",
    tags: ["コスプレ", "更衣室", "撮影会", "衣装半脱ぎ", "中出し", "美少女", "フェラチオ", "ハメ撮り"]
  },
  {
    id: "feature_class_reunion_first_love_secret_hotel",
    query: "同窓会 不倫",
    title: "【10年ぶりの再会と昔の憧れ】同窓会W不倫特集！大人びた初恋のマドンナと二次会を抜け出し朝まで生中出しし尽くす背徳情事AV名作選",
    category: "人妻・不倫",
    themeKeyword: "同窓会・同級生・W不倫・初恋・再会・ホテル・朝まで生ハメ",
    searchIntent: "同窓会で久しぶりに再会した昔のクラスメイトや初恋の人妻とホテルへ雪崩れ込み、懐かしさと罪悪感の中で交わるAVを探しているユーザー向け",
    introTone: "学生時代の面影を残しつつも、人妻としての色香を纏ったかつてのクラスのマドンナ。アルコールの力で蘇る淡い記憶と、現在の満たされない日常。二次会の喧騒を抜け出して駆け込んだホテルの密室で、10年分の空白を埋めるように貪り合う純愛と肉欲の混濁——。",
    tags: ["同窓会", "W不倫", "人妻", "初恋", "再会", "生中出し", "濃厚キス", "美魔女"]
  },
  {
    id: "feature_married_woman_delivery_driver_seduction",
    query: "配達員 人妻",
    title: "【汗ばむ配達員と欲求不満な団地妻】宅配ドライバー×人妻特集！荷物受け取りの玄関先から引きずり込まれる汗だく即ハメAV名作選",
    category: "人妻・団地",
    themeKeyword: "配達員・宅配ドライバー・団地妻・玄関先・猛暑・即ハメ・不倫",
    searchIntent: "猛暑の中配達にやってきた逞しい宅配員と、薄着で出迎えた欲求不満な若妻が玄関先でそのまま交わるシチュエーションAVを探しているユーザー向け",
    introTone: "真夏の猛暑、滴る汗を拭いながらチャイムを鳴らした団地の一室。ドアを開けた若妻はノーブラに薄手のキャミソール姿。サインを交わす指先が触れ合った瞬間、引きずり込まれた玄関のタタキで始まる、激しく汗が飛び散る即ハメ濃厚性交——。",
    tags: ["配達員", "団地妻", "人妻", "玄関", "即ハメ", "汗だく", "中出し", "不倫"]
  },
  {
    id: "feature_school_infirmary_nurse_bed_examination",
    query: "保健室 先生",
    title: "【カーテンに閉ざされた簡易ベッドの温もり】養護教諭・保健室の先生特集！白衣の奥の豊満ボディで手厚く性処理してくれる濃厚診察AV名作選",
    category: "学園・制服",
    themeKeyword: "保健室・養護教諭・保健室の先生・ベッド・カーテン・白衣・検温・性処理",
    searchIntent: "優しくてエロい保健室の先生がカーテンで仕切られたベッドの上で生徒や同僚教師を優しく癒やしハメる学園AVを探しているユーザー向け",
    introTone: "放課後の静かな保健室。カーテンで仕切られた簡易ベッドの狭い空間で、優しく額に手を当てる美人養護教諭。熱っぽい身体を診察するはずの手がいつしか股間へと伸び、白衣の胸元を開いて優しく包み込む究極の癒やしと背徳のヘルスケア——。",
    tags: ["保健室", "養護教諭", "白衣", "学園", "簡易ベッド", "巨乳", "中出し", "癒やし"]
  },
  {
    id: "feature_piano_teacher_private_lesson_metronome",
    query: "ピアノ 先生",
    title: "【防音レッスン室に響く不協和音と嬌声】美人ピアノ講師特集！メトロノームの等間隔ビートに合わせて鍵盤上で乱れ突かれる背徳連弾AV名作選",
    category: "職業・制服",
    themeKeyword: "ピアノ講師・音楽教室・防音室・メトロノーム・グランドピアノ・連弾",
    searchIntent: "清楚な美人ピアノ講師が防音のレッスン室でグランドピアノの上に寝かされ、メトロノームに合わせて激しく突かれるAVを探しているユーザー向け",
    introTone: "重厚な防音扉に閉ざされたレッスンルーム。メトロノームが刻む無機質なクリック音に重ねられる、鍵盤を乱暴に叩く音と湿っぽい喘ぎ声。譜面台を握りしめ、美しい指先を震わせながら激しいピストンを受け止めるピアノ講師の知られざる淫乱の旋律——。",
    tags: ["ピアノ講師", "音楽教室", "防音室", "メトロノーム", "グランドピアノ", "中出し", "清楚系", "連弾"]
  },
  {
    id: "feature_art_college_oil_painting_nude_model",
    query: "美大 ヌード",
    title: "【キャンバスの裏で交わる絵の具と体液】美大生・デッサンモデル特集！油絵の香りが立ち込めるアトリエで素肌を晒し貪り合う肉欲性交AV名作選",
    category: "学園・制服",
    themeKeyword: "美大生・ヌードデッサン・アトリエ・油絵・放課後・キャンバス・美術室",
    searchIntent: "美術室やアトリエでヌードモデルを務める女子大生が、ポーズをとるうちに欲情してそのまま交わる芸術的エロスAVを探しているユーザー向け",
    introTone: "テレピン油と乾いた絵の具の匂いが充満する放課後のアトリエ。イーゼルの前で衣服を脱ぎ捨て、デッサンモデルとして晒された白く滑らかな裸体。筆先を見つめる視線が熱を帯び、キャンバスの影で繰り広げられる生々しいデッサン交尾の狂宴——。",
    tags: ["美大生", "ヌードデッサン", "アトリエ", "美術室", "油絵", "中出し", "美少女", "ハメ撮り"]
  },
  {
    id: "feature_hair_salon_shampoo_beauty_seduction",
    query: "美容師 シャンプー",
    title: "【シャンプー台での耳元吐息と胸押し当て】美人美容師特集！薄暗いシャンプーブースで密着されクロスの中でイカされる濃厚サロンAV名作選",
    category: "職業・制服",
    themeKeyword: "美容師・ヘアサロン・シャンプー台・密着・胸当て・耳元吐息・カットクロス",
    searchIntent: "美容室のシャンプー中に豊かな胸を頭に押し当てられたり、カットクロスの下でこっそり手コキされるサロン系AVを探しているユーザー向け",
    introTone: "薄暗い照明と心地よい流水音が響くヘアサロンのシャンプーブース。仰向けになった首筋に触れる柔らかな指先と、頭部に押し当てられる豊かなバストの感触。カットクロスの下で密かに勃起した男根を、耳元の甘い吐息とともに優しく導くサロンの裏サービス——。",
    tags: ["美容師", "ヘアサロン", "シャンプー台", "胸当て", "耳元吐息", "手コキ", "中出し", "巨乳"]
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
  
  let totalWordsEstimate = 0;
  
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
  console.log("=== Starting generation of 20 brand-new high-depth feature articles ===");
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
      published: new Date(Date.now() - (i * 3600000)).toISOString(),
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

    // Small sleep to be polite to the API
    await new Promise(r => setTimeout(r, 600));
  }

  console.log(`=== Complete! Successfully generated ${successCount} articles. ===`);
}

run();
