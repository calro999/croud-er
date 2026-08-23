const fs = require('fs');
const path = require('path');
const https = require('https');

const API_ID = "4Lx0ftRf17Uuad6Ud7Gb";
const API_AFFILIATE_ID = "onchan555-999";
const OUT_AFFILIATE_ID = "onchan555-003";

const targetThemes = [
  {
    id: "feature_stepsister_private_room_secret_affair",
    query: "義妹 部屋",
    title: "【親の再婚でひとつ屋根の下に暮らす義妹】義妹×自室密会特集！ドアノブを回せば無防備な姿でくつろぐ義理の妹と交わす禁断の近親交尾AV名作選",
    category: "家庭内・義妹",
    themeKeyword: "義妹・再婚・ひとつ屋根の下・自室・ドアノブ・無防備・近親相姦・生中出し",
    searchIntent: "親の再婚によって義理の妹となった美少女と、実家の自室でこっそりハメ狂う背徳的な家庭内シチュエーションAVを探しているユーザー向け",
    introTone: "親の再婚によって突然始まった、血の繋がらない義妹との同居生活。ノックもそこそこに開けたドアの向こう、ベッドの上で薄着のまま寝転ぶ無防備な白い太もも。家族としての境界線を越え、親の足音に怯えながら自室で激しく求め合う禁断の近親愛——。",
    tags: ["義妹", "近親相姦", "ひとつ屋根の下", "自室", "無防備", "生中出し", "美少女", "背徳"]
  },
  {
    id: "feature_sister_in_law_bathroom_intrusion_sex",
    query: "義姉 風呂",
    title: "【湯煙の中で鉢合わせた義理の姉の柔肌】義姉×お風呂特集！脱衣所のドアを開けた瞬間に目撃した豊満ボディと洗い場で貪り合う濃厚入浴AV名作選",
    category: "家庭内・義姉",
    themeKeyword: "義姉・お風呂・鉢合わせ・湯煙・脱衣所・洗い場・豊満・生ハメ",
    searchIntent: "実家や同居先で義理の姉がお風呂に入っているところに偶然鉢合わせし、そのまま洗い場や湯船で生ハメするお風呂背徳AVを探しているユーザー向け",
    introTone: "すりガラスの扉の向こうに浮かび上がる、湯煙に濡れた豊満な女体のシルエット。鍵のかかっていない浴室のドアを開けてしまった瞬間の息を呑む静寂。恥じらいながらも隠しきれない豊かなバストを押し当てられ、泡立つ洗い場で貪り尽くす義姉との秘密の入浴交尾——。",
    tags: ["義姉", "お風呂", "入浴", "洗い場", "鉢合わせ", "豊満", "中出し", "近親相姦"]
  },
  {
    id: "feature_childhood_friend_loungewear_first_time",
    query: "幼馴染 部屋着",
    title: "【昔からの気安さと急激に意識する女の身体】幼馴染×部屋着特集！実家のコタツやベッドの上で無防備な幼馴染を女として激しく犯す名作選",
    category: "素人・幼馴染",
    themeKeyword: "幼馴染・部屋着・コタツ・無防備・実家・ベッド・友達から女へ・生ハメ",
    searchIntent: "気兼ねない関係だった幼馴染の女の子が、部屋着姿で遊びに来た際にふとしたきっかけで女として意識し、そのまま生ハメするリアル系AVを探しているユーザー向け",
    introTone: "昔から家族ぐるみの付き合いで、男の部屋にも平気でジャージや部屋着で上がり込んでくる幼馴染。だが、ソファでくつろぐ胸元の谷間や生足の白さにふと目が眩む。冗談交じりのじゃれ合いから熱いキスへと変わり、幼馴染の枠を越えて貪り合う青春の肉欲——。",
    tags: ["幼馴染", "部屋着", "素人風", "美少女", "実家", "生中出し", "青春", "無防備"]
  },
  {
    id: "feature_childhood_friend_confession_hotel_sex",
    query: "幼馴染 告白",
    title: "【ずっと好きだった想いが溢れ出す夜】幼馴染×告白特集！秘めていた想いを打ち明けられ涙と熱い抱擁の中で朝まで繋がり合う純愛濃厚セックスAV名作選",
    category: "素人・幼馴染",
    themeKeyword: "幼馴染・告白・両想い・純愛・初体験・朝まで・ホテル・濃厚キス",
    searchIntent: "昔からの幼馴染にずっと好きだったと告白され、ホテルや自室で互いの想いを確認しながら情熱的に愛し合う純愛エロスAVを探しているユーザー向け",
    introTone: "夜風が吹き抜ける帰り道、突然袖を引かれて打ち明けられた「ずっと好きだった」の一言。長年胸に秘めていた想いが溢れ出し、飛び込んだホテルのベッド。幼い頃の記憶を重ねながら、愛しさと情熱を込めて一晩中奥深くまで注ぎ込み続ける至福の純愛交尾——。",
    tags: ["幼馴染", "告白", "純愛", "両想い", "濃厚キス", "生中出し", "美少女", "初体験"]
  },
  {
    id: "feature_female_subordinate_business_trip_hotel",
    query: "後輩 女子社員",
    title: "【出張先のビジネスホテルで頼ってきた後輩】後輩女子社員特集！普段は甘え上手な部下が部屋着姿で部屋を訪れ朝まで腰を振るオフィス下剋上AV名作選",
    category: "オフィス・OL",
    themeKeyword: "後輩女子社員・出張・ビジネスホテル・部屋着・相談・オフィスラブ・生中出し",
    searchIntent: "出張先のホテルで後輩の女性社員が「相談があるんです」と部屋にやってきて、無防備な姿のままベッドでハメ合うオフィス系AVを探しているユーザー向け",
    introTone: "慣れない地方出張の夜、ホテルの部屋をノックする音。ドアを開けると、お風呂上がりのすっぴんにホテルの浴衣姿の後輩女子社員。「先輩の部屋で飲んでもいいですか？」と微笑む無防備な後輩をベッドに押し倒し、職場の上下関係を快楽で上書きする夜——。",
    tags: ["後輩", "女子社員", "OL", "出張", "ビジネスホテル", "浴衣", "生中出し", "社内恋愛"]
  },
  {
    id: "feature_colleague_peers_office_secret_romance",
    query: "同期 社内恋愛",
    title: "【同期入社だからこそ分かち合える秘密】同期社員×社内恋愛特集！残業終わりのオフィスや終電後の自宅で激しく求め合うリアルな情事AV名作選",
    category: "オフィス・OL",
    themeKeyword: "同期社員・社内恋愛・残業・終電後・秘密の社内恋愛・自宅マンション・スーツ",
    searchIntent: "同じ年に会社に入った同期の美人社員と、残業後や飲み会終わりに自宅でベッドになだれ込み激しく愛し合うリアルなオフィスラブAVを探しているユーザー向け",
    introTone: "研修時代から苦楽を共にしてきた同期の美人社員。仕事の愚痴を言い合う居酒屋の帰り道、どちらからともなく重なる手。自宅マンションのドアを閉めた瞬間、スーツを脱ぎ散らかしてベッドへ倒れ込む。誰にも言えない同期同士の濃厚な秘密の契り——。",
    tags: ["同期", "社内恋愛", "オフィス", "OL", "スーツ", "残業", "中出し", "リアル"]
  },
  {
    id: "feature_pta_chairwoman_secret_parent_meeting",
    query: "PTA 会長",
    title: "【厳格な人妻PTA会長が会合の夜に見せる雌の顔】PTA役員・人妻特集！学校の会議室や打ち上げの居酒屋個室でスーツを乱され犯される背徳AV名作選",
    category: "人妻・PTA",
    themeKeyword: "PTA会長・PTA役員・保護者会・学校会議室・スーツ・人妻・背徳・打ち上げ",
    searchIntent: "学校のPTA活動で役員を務める真面目でお堅い美人ママが、役員会のあとや準備室で男親や教員に言い寄られハメられる背徳AVを探しているユーザー向け",
    introTone: "学校の運営や地域活動を仕切る、誰からも尊敬される清楚な人妻PTA会長。だが、夜の資料作成で二人きりになった準備室で、スーツのタイトスカートをたくし上げられる。母親としての立場と、一人の女として疼く身体の狭間で狂おしく乱れる背徳のPTA——。",
    tags: ["PTA会長", "PTA役員", "人妻", "保護者会", "スーツ", "タイトスカート", "中出し", "背徳"]
  },
  {
    id: "feature_pta_executive_committee_harem_encounter",
    query: "PTA 役員",
    title: "【男一人に群がる欲求不満なママたち】PTA役員会ハーレム特集！プリント刷りの印刷室や合宿先で熟れきった人妻たちに囲まれ搾り取られる極上名作選",
    category: "人妻・ハーレム",
    themeKeyword: "PTA役員・印刷室・役員合宿・人妻ハーレム・欲求不満ママ・逆レイプ・搾り取り",
    searchIntent: "PTA役員に選ばれた男性が、周りの欲求不満な美人妻たちに囲まれ、学校の印刷室や合宿所で代わる代わる逆レイプされるハーレムAVを探しているユーザー向け",
    introTone: "輪転機がリズミカルに紙を吐き出す放課後の印刷室。インクの匂いが立ち込める密室で、男を囲む複数のPTA役員ママたち。日頃の欲求不満を晴らすかのように、次々とスーツのボタンを外し男根に群がる。美熟女たちに囲まれて骨抜きにされる至福のハーレム——。",
    tags: ["PTA役員", "人妻", "ハーレム", "印刷室", "逆レイプ", "熟女", "中出し", "輪姦"]
  },
  {
    id: "feature_neighborhood_association_hot_spring_trip",
    query: "町内会 温泉",
    title: "【自治会の親睦旅行で混浴乱交】町内会・温泉慰安旅行特集！老舗旅館の大広間や貸切露天風呂で酒の勢いに任せて交わされる近隣不倫AV名作選",
    category: "人妻・温泉",
    themeKeyword: "町内会・自治会・温泉旅行・大広間・貸切風呂・混浴・宴会・近所の人妻",
    searchIntent: "町内会や自治会の温泉旅行で、近所の若妻や奥さんたちと宴会で泥酔し、浴衣をはだけさせて温泉旅館でハメ狂うシチュエーションAVを探しているユーザー向け",
    introTone: "年に一度の町内会親睦温泉旅行。大広間での宴会が進み、浴衣の胸元がはだけていく近所の人妻たち。障子で仕切られただけの客室で、夫や近隣住民の目を盗みながら行われる秘密の情事。湯上がりの火照った身体に容赦なく注ぎ込まれる背徳の種付け——。",
    tags: ["町内会", "自治会", "温泉旅行", "宴会", "人妻", "浴衣", "中出し", "乱交"]
  },
  {
    id: "feature_apartment_landlady_rent_negotiation_sex",
    query: "大家 アパート",
    title: "【家賃の滞納と引き換えに捧げる妖艶な身体】美人大家さん特集！アパートの管理人室や入居者の部屋を訪れ豊満な肉体で家賃を回収する背徳AV名作選",
    category: "人妻・未亡人",
    themeKeyword: "大家さん・アパート・家賃滞納・管理人室・未亡人・肉体支払い・豊満",
    searchIntent: "アパートの若き美人大家さん（未亡人）が、家賃を払えない住人の部屋を訪れ、身体で支払わせたり自ら誘惑してハメるAVを探しているユーザー向け",
    introTone: "古びたアパートを一人で切り盛りする、妖艶な色香を漂わせる若き未亡人の大家さん。家賃の催促に訪れた部屋のドアが閉まる瞬間、エプロンを外し「身体で払ってくれる？」と囁く。管理人室のベッドの上で、住人の若い男根を貪り尽くす熟れた肉欲の回収劇——。",
    tags: ["大家さん", "アパート", "未亡人", "人妻", "家賃滞納", "管理人室", "中出し", "熟女"]
  },
  {
    id: "feature_housekeeper_maid_private_service_creampie",
    query: "家政婦 密着",
    title: "【エプロンの下は極上の奉仕精神】家政婦・出張メイド特集！旦那様のお部屋掃除からシモのお世話まで完璧にこなすご奉仕生ハメAV名作選",
    category: "職業・制服",
    themeKeyword: "家政婦・家事代行・メイド・エプロン・シモの世話・ご奉仕・寝室・旦那様",
    searchIntent: "自宅に雇った清楚な家政婦や家事代行の女性が、掃除中にエプロン姿のまま旦那様の性処理まで完璧にこなしてくれるご奉仕AVを探しているユーザー向け",
    introTone: "広々とした豪邸のベッドルームで、シーツを整えるエプロン姿の美人家政婦。「旦那様、何か他にお手伝いすることはございますか？」と微笑みながら、主人の股間に膝をつく。丁寧な言葉遣いと完璧なご奉仕テクニックで、主人の精子を一滴残らず吸い尽くす——。",
    tags: ["家政婦", "家事代行", "メイド", "エプロン", "ご奉仕", "中出し", "フェラチオ", "清楚系"]
  },
  {
    id: "feature_housework_agency_anal_cleaning_service",
    query: "家事代行",
    title: "【キッチンから寝室までピカピカに磨き上げる】家事代行サービス特集！タイトな作業着姿で水回り掃除に励む若妻を背後から突く即ハメAV名作選",
    category: "人妻・職業",
    themeKeyword: "家事代行・若妻・水回り掃除・キッチン・エプロン・作業着・立ちバック",
    searchIntent: "家事代行サービスでやってきた人妻スタッフが、お風呂やキッチンの掃除中に後ろから抱きつかれ、立ちバックでハメられるシチュエーションAVを探しているユーザー向け",
    introTone: "シンクを磨くキュッキュッというリズミカルな音。エプロンの下から覗く、作業着に包まれた若妻の引き締まったヒップ。掃除の邪魔をするように背後から伸びる腕、驚きながらも拒みきれない甘い吐息。磨き上げられたキッチンのカウンターで始まる即ハメ情事——。",
    tags: ["家事代行", "人妻", "エプロン", "キッチン", "立ちバック", "中出し", "素人風", "即ハメ"]
  },
  {
    id: "feature_family_peeping_hidden_camera_domestic",
    query: "家庭内 覗き",
    title: "【襖の隙間から覗く家族の秘密のオナニー】家庭内覗き・盗撮特集！脱衣所や自室で密かに快楽に耽る姉妹や母の無防備な自慰を暴く名作選",
    category: "家庭内・マニア",
    themeKeyword: "家庭内覗き・襖の隙間・自慰・オナニー・脱衣所・姉妹・母親・盗撮風",
    searchIntent: "実家で襖の隙間やドアの鍵穴から、家族（姉、妹、母）が自室や脱衣所でオナニーしている姿を覗き見るドキドキ感満載のAVを探しているユーザー向け",
    introTone: "静まり返った深夜の実家。襖の隙間から漏れる微かな灯りと、衣擦れに混じる湿った水音。息を殺して覗き込んだ先には、パンティに手を忍ばせ指先を激しく動かす家族の無防備な顔。覗かれているとも知らずに絶頂に身を震わせる生々しい自慰の瞬間——。",
    tags: ["家庭内覗き", "オナニー", "自慰", "襖の隙間", "姉妹", "母親", "盗撮風", "リアル"]
  },
  {
    id: "feature_asmr_whispering_ear_licking_brain_melt",
    query: "ASMR 囁き",
    title: "【両耳から脳髄を直接犯される甘い淫語】ASMR・バイノーラル特集！鼓膜に息を吹きかけられながら至近距離でヌカれる究極の脳トロAV名作選",
    category: "フェチ・ASMR",
    themeKeyword: "ASMR・バイノーラル・耳元囁き・耳舐め・脳トロ・立体音響・臨場感・主観",
    searchIntent: "高性能バイノーラルマイクを使い、耳元で甘い囁きや耳舐め、吐息を吹きかけられながら抜いてもらえる最高音質のASMR系AVを探しているユーザー向け",
    introTone: "ヘッドホンを装着した瞬間に広がる、圧倒的な臨場感。吐息の温もりまで伝わるような至近距離の耳元囁きと、ジュポジュポと鼓膜を震わせる濃厚な耳舐めの音。脳の芯までとろけるような快感の波に呑まれ、抗う術もなく射精へと導かれる究極のASMRエロス——。",
    tags: ["ASMR", "バイノーラル", "耳元囁き", "耳舐め", "脳トロ", "立体音響", "手コキ", "癒やし"]
  },
  {
    id: "feature_binaural_ear_cleaning_relaxation_massage",
    query: "バイノーラル",
    title: "【立体音響で体感する密着耳かきと射精管理】バイノーラルマイク特化特集！左右の耳から交互に囁かれる淫語と膝枕で蕩ける極楽主観AV名作選",
    category: "フェチ・ASMR",
    themeKeyword: "バイノーラル・立体音響・耳かき・膝枕・主観・射精管理・囁き",
    searchIntent: "バイノーラル録音によるリアルな音響で、膝枕での耳かきや射精管理を疑似体験できる超主観・没入型AVを探しているユーザー向け",
    introTone: "柔らかな太ももの上に頭を乗せた膝枕の視界。カリカリと心地よく響く耳かきの音と、左右から包み込むように囁かれる優しい甘言。「もう我慢できないの？」と笑いながら、耳元と股間を同時に支配される極上のバイノーラル体験——。",
    tags: ["バイノーラル", "立体音響", "膝枕", "耳かき", "主観", "射精管理", "中出し", "ASMR"]
  },
  {
    id: "feature_ear_licking_sensual_whisper_coitus",
    query: "耳舐め ASMR",
    title: "【濡れた舌先が耳腔を侵犯する官能の調べ】耳舐め特化ASMR特集！唾液の湿った水音と甘美な吐息で全身の毛穴を逆立てる濃密オーラルAV名作選",
    category: "フェチ・ASMR",
    themeKeyword: "耳舐め・ASMR・唾液・耳腔・水音・甘美な吐息・ゾクゾク・フェラチオ",
    searchIntent: "耳舐めのリアルな水音や吐息を徹底的にフィーチャーし、耳から全身へ走る電流のような快感を楽しめるAVを探しているユーザー向け",
    introTone: "ペロリと耳たぶを這う温かい舌先の感触。耳の奥深くまで差し込まれる舌の動きと、クチュクチュと響く生々しい唾液の音。背筋を駆け上がるゾクゾクとした悪寒のような快楽に身を捩りながら、耳と肉棒を同時に責め立てられる背徳のトリップ——。",
    tags: ["耳舐め", "ASMR", "唾液", "耳腔", "水音", "フェラチオ", "中出し", "快感"]
  },
  {
    id: "feature_mind_control_hypnosis_absolute_obedience",
    query: "洗脳 調教",
    title: "【常識も羞恥心も書き換えられる絶対服従】洗脳・催眠調教特集！真面目で清楚な美女が暗示によって快楽の奴隷へと堕ちていくサイキックAV名作選",
    category: "マニア・調教",
    themeKeyword: "洗脳・催眠・調教・絶対服従・暗示・快楽堕ち・清楚系・常識改変",
    searchIntent: "清楚で真面目な美少女や人妻が、洗脳や催眠によって羞恥心を奪われ、どんな変態的な命令にも笑顔で従うようになる調教系AVを探しているユーザー向け",
    introTone: "カチリと指を鳴らされた瞬間、虚ろになる美しい瞳。どれほど嫌がっていた命令も、暗示によって「最高の快楽」へと書き換えられる。人前での全裸露出から下劣な男根への奉仕まで、自ら進んで悦びの声を上げながら服従する完全調教の深淵——。",
    tags: ["洗脳", "調教", "催眠", "絶対服従", "快楽堕ち", "中出し", "清楚系", "ハード"]
  },
  {
    id: "feature_ear_cleaning_healing_esthetician_seduction",
    query: "耳かき エステ",
    title: "【膝枕で耳かきされながら昇天する至福の癒やし】耳かきエステ・回春サロン特集！浴衣姿の美人セラピストがゼロ距離密着で抜いてくれる名作選",
    category: "エステ・癒やし",
    themeKeyword: "耳かきエステ・回春サロン・膝枕・浴衣・ゼロ距離密着・耳掃除・抜きあり",
    searchIntent: "和風の耳かき小町や回春エステで、浴衣姿の可愛い女の子に膝枕されながら耳かきと性処理をしてもらえる癒やし系AVを探しているユーザー向け",
    introTone: "畳敷きの和室、行燈の柔らかな灯り。膝枕をしてくれるのは、艶やかな浴衣姿の美少女セラピスト。心地よい耳かきの刺激に身を委ねていると、いつしか浴衣の襟元がはだけ、胸元を押し当てられながら股間を優しく包み込まれる至高の和風回春劇——。",
    tags: ["耳かき", "エステ", "回春", "膝枕", "浴衣", "密着", "手コキ", "癒やし"]
  },
  {
    id: "feature_senior_female_student_drunk_seduction",
    query: "先輩 女子大生",
    title: "【憧れの美人先輩が酒に酔って見せた素顔】大学の先輩×宅飲み特集！サークルの合宿先や先輩の部屋で無防備に迫られ結ばれる下剋上AV名作選",
    category: "女子大生・素人",
    themeKeyword: "大学の先輩・女子大生・宅飲み・サークル合宿・泥酔・逆誘惑・下剋上",
    searchIntent: "大学サークルで憧れていた美人な先輩女子大生と、宅飲みや合宿で二人きりになり、酔った勢いで逆誘惑されてハメる青春エロスAVを探しているユーザー向け",
    introTone: "大学のサークルでいつも頼りになる、高嶺の花の美人先輩。だが合宿終わりの部屋飲みで酔いつぶれ、「私のこと、女として見てないの？」と上目遣いで抱きついてくる。憧れだった先輩の柔らかな身体をベッドに押し倒し、激しく腰を打ち付ける歓喜の夜——。",
    tags: ["先輩", "女子大生", "宅飲み", "泥酔", "サークル", "生中出し", "美少女", "青春"]
  },
  {
    id: "feature_predatory_slut_reverse_hunting_creampie",
    query: "痴女 逆ナン",
    title: "【街中で男を品定めし狩り尽くす肉食系女子】逆ナン痴女特集！路上で逆ナンした獲物をラブホに連れ込み自分から腰を振り生中出しさせる名作選",
    category: "素人・痴女",
    themeKeyword: "逆ナン・痴女・肉食系・街頭ハント・ホテル直行・騎乗位・生中出し・逆レイプ",
    searchIntent: "性欲が強すぎる肉食系の美女が、街中で好みの男を逆ナンし、ホテルに連れ込んで自分から跨がり腰を振りまくる痴女系AVを探しているユーザー向け",
    introTone: "夜の街を闊歩する、露出度の高い服装の美脚美女。獲物を見つけた瞬間、甘い笑顔で腕を絡ませてくる。「今夜、私と気持ちいいことしない？」と誘い込まれたホテルの部屋で、男をベッドに縛り付け自ら跨がって激しく腰を跳ねさせる肉食痴女の狂宴——。",
    tags: ["逆ナン", "痴女", "肉食系", "騎乗位", "生中出し", "美脚", "素人風", "逆レイプ"]
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
  console.log("=== Starting generation of 20 brand-new high-depth feature articles (Batch 5) ===");
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
      published: new Date(Date.now() - ((i + 100) * 3600000)).toISOString(),
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

  console.log(`=== Complete! Successfully generated ${successCount} articles in Batch 5. ===`);
}

run();
