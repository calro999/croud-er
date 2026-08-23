const fs = require('fs');
const path = require('path');
const https = require('https');

const API_ID = "4Lx0ftRf17Uuad6Ud7Gb";
const API_AFFILIATE_ID = "onchan555-999";
const OUT_AFFILIATE_ID = "onchan555-003";

const targetThemes = [
  {
    id: "feature_beach_house_bikini_gal_summer_creampie",
    query: "水着ギャル 海の家",
    title: "【灼熱の砂浜と海の家の甘い罠】水着ギャル×海の家特集！オイルまみれの小麦肌ビキニを剥ぎ取りシャワー室で突く真夏の生ハメAV名作選",
    category: "ギャル・素人",
    themeKeyword: "海の家・水着ギャル・ビキニ・サンオイル・シャワールーム・真夏・ナンパ",
    searchIntent: "夏のビーチや海の家、シャワールームでビキニ姿の開放的なギャルがオイルまみれでハメられるリゾート系AVを探しているユーザー向け",
    introTone: "照りつける太陽と波の音、ココナッツオイルの甘い香り漂う真夏のビーチ。海の家の薄暗い簡易シャワー室で、砂混じりのビキニを無理やりずらされた水着ギャル。火照りきった身体に冷たい水滴と熱い肉棒が同時に突き刺さり、波音をかき消す喘ぎ声を響かせる——。",
    tags: ["海の家", "水着ギャル", "ビキニ", "サンオイル", "シャワー室", "中出し", "ナンパ", "真夏"]
  },
  {
    id: "feature_tennis_player_mini_skirt_court_sex",
    query: "テニス ウェア",
    title: "【ミニスカスコートの下の生々しいパンチラ】女子テニス部・テニスウェア特集！汗ばむクラブハウスでスコートをめくり上げ激突するアスリートAV名作選",
    category: "スポーツ・水着",
    themeKeyword: "テニスウェア・スコート・ミニスカート・テニス部・クラブハウス・アンダーパンツ・アスリート",
    searchIntent: "白のミニスカテニスウェア（スコート）を着た健康的な美脚美女が、クラブハウスや更衣室でスコートを捲られてハメられるAVを探しているユーザー向け",
    introTone: "コートを駆け巡る軽快な足音と、激しいラリーのたびにひらりと翻る純白のスコート。試合後の熱気が残るクラブハウスの片隅、汗で肌に張り付くウェアの隙間から滑り込む手先。引き締まった太ももを大きく開かせ、アンダースコートをずらして奥深くまで貫く歓喜のゲームセット——。",
    tags: ["テニス", "スコート", "ミニスカート", "スポーツウェア", "クラブハウス", "中出し", "美脚", "アスリート"]
  },
  {
    id: "feature_volleyball_uniform_bloomers_creampie",
    query: "バレーボール ユニフォーム",
    title: "【引き締まった太ももと躍動する美尻】女子バレーボール特集！ピチピチユニフォームと短パン姿のまま体育倉庫で突き上げられる汗だく交尾AV名作選",
    category: "スポーツ・学生",
    themeKeyword: "バレーボール・女子バレー・ユニフォーム・短パン・体育倉庫・跳躍力・汗だく",
    searchIntent: "バレーボール部のスレンダーかつ美尻な選手が、ピチピチのユニフォーム姿のまま体育倉庫のマットの上でハメ倒されるAVを探しているユーザー向け",
    introTone: "体育館に響くシューズのスキール音とボールを弾く鋭い衝撃音。跳躍のたびに揺れるバストと、ぴったりとヒップに張り付いたバレーショーツ。放課後、鍵の閉められた体育倉庫の飛び箱やマットの上で、汗ばむユニフォーム越しに激しく腰を打ち付け合う情熱のスパイク——。",
    tags: ["バレーボール", "ユニフォーム", "短パン", "体育倉庫", "マット", "汗だく", "中出し", "美尻"]
  },
  {
    id: "feature_track_and_field_bloomer_clubhouse_sex",
    query: "陸上 ブルマ",
    title: "【褐色の引き締まった肉体と食い込むブルマ】陸上部・ブルマ特集！放課後の夕暮れの部室で汗の匂いに包まれながら貫かれる極上アスリートAV名作選",
    category: "スポーツ・学生",
    themeKeyword: "陸上部・ブルマ・ランパン・セパレート・トラック・部室・汗だく・美脚",
    searchIntent: "陸上部の女子選手がセパレートユニフォームやブルマ姿で、夕方の部室で汗だくのまま激しく突かれるフェティッシュなAVを探しているユーザー向け",
    introTone: "西日に照らされたグラウンドの赤土と、練習終わりの独特な汗の薫り。太ももの付け根まで露わになった陸上ブルマの食い込み。薄暗い部室のベンチに組み敷かれ、鍛え抜かれた柔軟な脚を肩に担ぎ上げられて奥深くまで打ち込まれるピストンに、息を乱して絶頂する——。",
    tags: ["陸上部", "ブルマ", "セパレート", "部室", "汗だく", "美脚", "中出し", "アスリート"]
  },
  {
    id: "feature_rhythmic_gymnastics_leotard_flexibility",
    query: "新体操 レオタード",
    title: "【極限の柔軟性とハイレグレオタードの艶技】新体操・レオタード特集！180度開脚スプリットの体勢で美肉の深奥を突かれ悶える軟体交尾AV名作選",
    category: "スポーツ・フェチ",
    themeKeyword: "新体操・レオタード・ハイレグ・柔軟・180度開脚・スプリット・軟体・バック",
    searchIntent: "新体操の選手が煌びやかなハイレグレオタードを着たまま、驚異的な開脚ポーズで根元まで生挿入される軟体フェチAVを探しているユーザー向け",
    introTone: "スパンコールが煌めく薄手のレオタードと、極限までシェイプされたしなやかな肢体。マットの上で軽やかに180度開脚された両脚の間、薄い布地を押し退けて現れる無防備な蜜壺。驚異の柔軟性を活かしたアクロバティックな体位で、子宮口を激しくノックされる軟体の悦楽——。",
    tags: ["新体操", "レオタード", "ハイレグ", "180度開脚", "柔軟", "軟体", "中出し", "美脚"]
  },
  {
    id: "feature_female_doctor_stethoscope_clinic_seduction",
    query: "女医 聴診器",
    title: "【白衣の奥から響く冷徹な女医の鼓動】美人女医×聴診器特集！夜間診療所の密室で診察用ベッドに横たわり聴診器を当てられながら乱れる逆診察AV名作選",
    category: "医療・ナース",
    themeKeyword: "女医・聴診器・白衣・夜間診療・診察室・診察台・タイトスカート・カルテ",
    searchIntent: "クールで知的な美人女医が、白衣の胸元を開け聴診器を当てられながら診察室で下剋上セックスされるシチュエーションAVを探しているユーザー向け",
    introTone: "冷たい金属の聴診器が素肌に触れた瞬間の冷涼な刺激。夜間診療所の静まり返った診察室で、患者のカルテを閉じた美人女医。白衣のボタンを一つずつ外され、タイトスカートをまくり上げられて診察台に横たわる。知的な表情が快楽の波に呑まれ蕩けていく——。",
    tags: ["女医", "聴診器", "白衣", "診察室", "診察台", "タイトスカート", "中出し", "医療"]
  },
  {
    id: "feature_dental_assistant_mask_whisper_creampie",
    query: "歯科助手",
    title: "【マスク越しの潤んだ瞳と耳元の吐息】歯科助手特集！診察後の薄暗い消毒室やユニットの上で胸を押し当て手コキ・生ハメしてくれる濃厚治療AV名作選",
    category: "医療・ナース",
    themeKeyword: "歯科助手・マスク・衛生士・消毒室・診療ユニット・胸当て・手コキ・中出し",
    searchIntent: "マスク姿の可愛い歯科助手が、治療中や閉院後の院内でこっそり患者や院長の性欲を処理してくれる歯科系AVを探しているユーザー向け",
    introTone: "マスクの上から覗く大きな瞳と、耳元で囁かれる甘い吐息。閉院後のデンタルクリニック、消毒液の匂いが満ちる準備室で二人きり。ピンクのエプロンをたくし上げ、ユニットシートの上で至近距離から見つめられながら注ぎ込まれる生々しい白濁液——。",
    tags: ["歯科助手", "マスク", "クリニック", "エプロン", "胸当て", "中出し", "手コキ", "美少女"]
  },
  {
    id: "feature_pharmacist_dispensing_pharmacy_white_coat",
    query: "薬剤師",
    title: "【調剤室の棚の陰で交わされる禁断の処方箋】美人薬剤師特集！白衣と眼鏡の奥に秘めた淫乱な性欲を薬棚に押し付け解放する調剤室交尾AV名作選",
    category: "医療・職業",
    themeKeyword: "薬剤師・調剤薬局・調剤室・白衣・眼鏡・薬棚・処方箋・密着",
    searchIntent: "清潔感あふれる美人薬剤師が、薬局の調剤室の奥で白衣を着たまま薬棚に手をついて突かれるインテリフェチAVを探しているユーザー向け",
    introTone: "無数に並ぶ薬品瓶と正確無比な計量機器に囲まれた調剤室。処方箋のチェックを終えた美人薬剤師の背後から伸びる淫らな手。白衣を脱ぎ捨てる間もなく、薬棚に押し付けられて始まる情熱的なピストン。調合された媚薬のように熱く疼く蜜壺が激しく波打つ——。",
    tags: ["薬剤師", "調剤薬局", "白衣", "眼鏡", "調剤室", "中出し", "清楚系", "職場セックス"]
  },
  {
    id: "feature_bookstore_clerk_apron_aisle_creampie",
    query: "書店員",
    title: "【本棚の死角で静寂を破る湿った摩擦音】書店員・本屋特集！エプロン姿のまま人通りのある通路の物陰で声押し殺しイキ乱れるサイレントAV名作選",
    category: "シチュエーション",
    themeKeyword: "書店員・本屋・エプロン・本棚の死角・通路・声我慢・立ち読み・サイレント",
    searchIntent: "本屋の店員がエプロン姿で品出し中に、本棚の死角に連れ込まれて客や店長にこっそりハメられるサイレント系AVを探しているユーザー向け",
    introTone: "静まり返る書店のフロア、ページをめくる音だけが響く空間。背の高いコミック棚の最奥、防犯カメラの死角でエプロンを捲り上げられた書店員美女。客の足音がすぐそこまで近づく恐怖の中、口を手で押さえながら奥深くまで突き立てられる快楽に打ち震える——。",
    tags: ["書店員", "本屋", "エプロン", "本棚の死角", "声我慢", "中出し", "素人風", "サイレント"]
  },
  {
    id: "feature_apparel_store_fitting_room_seduction",
    query: "アパレル 店員",
    title: "【試着室のカーテン一枚隔てた熱気】アパレル店員特集！狭いフィッティングルームの中で店員美女と密着し鏡の前でハメ狂う即ハメAV名作選",
    category: "職業・制服",
    themeKeyword: "アパレル店員・試着室・フィッティングルーム・カーテン・全身鏡・即ハメ・オシャレ",
    searchIntent: "お洒落なアパレルショップの美人店員が、試着室の中でサイズ合わせにかこつけて客と密着しそのまま交わるAVを探しているユーザー向け",
    introTone: "最新のトレンド服が並ぶブティックの試着室。カーテン一枚で遮られただけの狭い個室に、サイズ直しの名目で入ってきたスタイル抜群のショップ店員。三面鏡に映し出される、衣服を着崩し壁に押し付けられた二人の生々しい結合部と甘い吐息——。",
    tags: ["アパレル", "ショップ店員", "試着室", "フィッティングルーム", "全身鏡", "中出し", "美脚", "即ハメ"]
  },
  {
    id: "feature_flower_shop_apron_blooming_creampie",
    query: "花屋",
    title: "【色鮮やかな花々と水滴に濡れる柔肌】フラワーショップ店員特集！芳しい生花の香りに包まれた作業場でエプロンをたくし上げ交わる純愛AV名作選",
    category: "職業・制服",
    themeKeyword: "花屋・フラワーショップ・生花・エプロン・水滴・作業場・切り花・清楚",
    searchIntent: "お花屋さんで働く清楚で心優しい看板娘が、花束に囲まれた店内の奥でエプロン姿のまま優しくハメられる癒やし系AVを探しているユーザー向け",
    introTone: "色とりどりの薔薇や百合が咲き誇り、瑞々しい水の匂いが漂うフラワーショップ。開店前の薄暗い作業場で、水揚げ作業中のエプロン美女。花びらのように柔らかく濡れそぼった蜜花を優しく押し広げられ、甘い花の香りに包まれながら溶け合うように果てる——。",
    tags: ["花屋", "フラワーショップ", "エプロン", "清楚", "癒やし", "中出し", "美少女", "純愛"]
  },
  {
    id: "feature_bakery_freshly_baked_sweet_dough_sex",
    query: "パン屋",
    title: "【焼きたてパンの香ばしい小麦の香りと熱気】ベーカリー・パン屋店員特集！早朝の厨房で粉まみれの三角巾＆エプロン姿で突かれる早朝交尾AV名作選",
    category: "職業・制服",
    themeKeyword: "パン屋・ベーカリー・早朝仕込み・厨房・オーブン・三角巾・エプロン・小麦粉",
    searchIntent: "早朝のパン屋で仕込み作業中の看板娘が、オーブンの熱気漂う厨房でエプロンをたくし上げられてハメられるシチュエーションAVを探しているユーザー向け",
    introTone: "夜明け前の静かな街に漂う、焼きたてパンの香ばしい匂い。オーブンの熱気でほんのり上気した頬と、小麦粉で白く汚れたエプロン。仕込み台に腰を乗せられ、朝の光が差し込む厨房で激しく打ち付けられるピストンのリズムに、甘い声を漏らし乱れる——。",
    tags: ["パン屋", "ベーカリー", "厨房", "早朝", "エプロン", "三角巾", "中出し", "美少女"]
  },
  {
    id: "feature_office_tea_room_secret_whisper_sex",
    query: "OL 給湯室",
    title: "【湯沸かし器の蒸気とコップの触れ合う音】オフィス給湯室特集！お茶出しの合間にドアを施錠しスーツのタイトスカート越しに貪る社内情事AV名作選",
    category: "オフィス・OL",
    themeKeyword: "給湯室・OL・お茶出し・湯沸かし器・施錠・タイトスカート・社内情事・立ちバック",
    searchIntent: "会社の給湯室でお茶を入れている美人OLが、後ろから入ってきた上司や同僚に内鍵をかけられ立ちバックでハメられるオフィスAVを探しているユーザー向け",
    introTone: "シューという湯沸かし器の蒸気音と、食器が触れ合う微かな金属音。お茶出しの準備をする美人OLの背後で、カチリと鳴った給湯室のドアの鍵。シンクに手をつかせ、タイトスカートをたくし上げてストッキングを引き裂く。誰かがノックする恐怖の中での濃厚ピストン——。",
    tags: ["給湯室", "OL", "オフィス", "タイトスカート", "立ちバック", "中出し", "社内不倫", "声我慢"]
  },
  {
    id: "feature_elevator_emergency_stop_intense_sex",
    query: "エレベーター 密室",
    title: "【急停止ボタンを押した瞬間始まる狂宴】エレベーター密室特集！監視カメラを隠し密閉された昇降機の中で階下への到着を焦らし貫く名作選",
    category: "シチュエーション",
    themeKeyword: "エレベーター・密室・急停止・防犯カメラ・階数表示・昇降機・閉じ込め",
    searchIntent: "高層ビルのエレベーターで二人きりになり、非常停止ボタンを押して密室の中で激しくハメ合うスリリングなAVを探しているユーザー向け",
    introTone: "上昇を続ける高層ビルのエレベーター。二人きりになった瞬間に押された非常停止ボタン。照明が非常灯に切り替わり、密閉された空間で加速する呼吸。手すりに掴まらせ、鏡張りの壁に映る乱れた姿を見せつけながら激しく腰を打ち付ける極限密室劇——。",
    tags: ["エレベーター", "密室", "急停止", "防犯カメラ", "立ちバック", "中出し", "OL", "スリル"]
  },
  {
    id: "feature_commuter_train_packed_silent_touch",
    query: "満員電車",
    title: "【身動きの取れない超密着の車内】満員電車・通勤通学特集！揺れる吊り革の下で逃げ場を失い指先と肉棒の侵入を受け入れる背徳痴漢AV名作選",
    category: "シチュエーション",
    themeKeyword: "満員電車・通勤・通学・吊り革・ドア付近・密着・身動き取れない・サイレント",
    searchIntent: "通勤ラッシュの超満員電車で、密着した男女が周囲に気づかれないようスカートの下で指マンや挿入される王道シチュエーションAVを探しているユーザー向け",
    introTone: "朝の通勤ラッシュ、押し合いへし合いの満員電車。ドアのガラスに押し付けられた無防備な背中。電車の揺れに合わせて密着する男の股間。逃げ場のない超密着空間で、スカートの奥に滑り込んだ手が次第に女の理性を溶かし、生々しい絶頂へと導いていく——。",
    tags: ["満員電車", "通勤電車", "密着", "声我慢", "スカート", "中出し", "OL", "女子大生"]
  },
  {
    id: "feature_oil_massage_spa_sensual_detox_creampie",
    query: "エステ オイル",
    title: "【全身テカテカに光る滑走ボディ】高級アロマオイルエステ特集！温められたヌルヌルオイルで秘部まで丹念にほぐされ快楽堕ちする極上スパAV名作選",
    category: "エステ・マッサージ",
    themeKeyword: "オイルマッサージ・高級エステ・アロマオイル・ヌルヌル・全身密着・滑走・デトックス",
    searchIntent: "高級エステサロンで美女が温かいオイルを全身に塗られ、ヌルヌルの摩擦感の中で秘部を弄ばれ本番セックスに持ち込まれるAVを探しているユーザー向け",
    introTone: "薄暗い間接照明と心地よいアジアンヒーリング音楽。温められた上質なアロマオイルが白い素肌に注がれ、手のひら全体で滑るように行われる全身トリートメント。鼠蹊部から秘部へと徐々に侵入するオイル塗れの指先と、滑走する肉体同士の甘美な交歓——。",
    tags: ["オイルマッサージ", "エステ", "アロマオイル", "ヌルヌル", "中出し", "巨乳", "美肌", "密着"]
  },
  {
    id: "feature_dry_head_spa_scalp_massage_relaxation",
    query: "ヘッドスパ",
    title: "【頭皮の極上指圧と耳元の吐息で脳トロ昇天】ヘッドスパ・専門店特集！薄暗いリクライニングチェアで頭部を揉みほぐされ股間まで緩む極楽射精AV名作選",
    category: "エステ・癒やし",
    themeKeyword: "ヘッドスパ・頭皮マッサージ・リクライニングチェア・脳トロ・耳元吐息・回春・リラクゼーション",
    searchIntent: "ヘッドスパ専門店で美人セラピストに頭皮をマッサージされながら、耳元で淫語を囁かれ下半身も抜いてもらう回春系AVを探しているユーザー向け",
    introTone: "静寂に包まれた完全個室、柔らかなリクライニングチェアに深く沈み込む身体。熟練のセラピストの指先が頭皮のツボを捉え、脳がとろけるような極上の快楽が全身を駆け巡る。頭部の快感と連動するように勃起した男根を、優しく包み込み射精へ導く至福のサロン——。",
    tags: ["ヘッドスパ", "マッサージ", "リラクゼーション", "脳トロ", "手コキ", "中出し", "癒やし", "セラピスト"]
  },
  {
    id: "feature_yoga_instructor_tight_leggings_stretch",
    query: "ヨガ スパッツ",
    title: "【吸い付くレギンスと超柔軟ポーズの美尻】美人ヨガインストラクター特集！ホットヨガの汗だくスタジオでポーズ指導から雪崩れ込む密着生交尾AV名作選",
    category: "スポーツ・フィットネス",
    themeKeyword: "ヨガインストラクター・ホットヨガ・スパッツ・レギンス・開脚・ポーズ指導・汗だく",
    searchIntent: "ピチピチのヨガウェアを着た美人インストラクターが、スタジオでポーズ指導中に密着され生ハメされる柔軟美ボディAVを探しているユーザー向け",
    introTone: "室温38度、湿度65%のホットヨガスタジオ。玉のような汗が滴るタイトなヨガレギンス越しの引き締まった美尻。ダウンドッグのポーズをとるインストラクターの背後からぴったりと重なる腰。しなやかな柔軟性と汗の摩擦が織りなす極上のホットセックス——。",
    tags: ["ヨガ", "ヨガインストラクター", "スパッツ", "レギンス", "ホットヨガ", "汗だく", "中出し", "美尻"]
  },
  {
    id: "feature_pilates_reformer_machine_hip_curve_sex",
    query: "ピラティス",
    title: "【マシン器具に固定された美しい肉体美】ピラティス・リフォーマー特集！引き締まった美くびれとヒップラインを器具の上で突き上げる筋膜調教AV名作選",
    category: "スポーツ・フィットネス",
    themeKeyword: "ピラティス・リフォーマー・マシンピラティス・美くびれ・ヒップアップ・スパッツ・器具固定",
    searchIntent: "最新のマシンピラティス器具（リフォーマー）を使ったトレーニング中に、美ボディの女性が器具の上でハメられるフェティッシュなAVを探しているユーザー向け",
    introTone: "専用マシン「リフォーマー」のスプリングが軋むプライベートスタジオ。ストラップで脚を固定され、美しい背筋とヒップラインを強調した姿勢。体幹を意識した呼吸の合間に滑り込む肉棒。逃げ場のない器具の上で、芯まで響くディープピストンに悶絶する——。",
    tags: ["ピラティス", "マシンピラティス", "リフォーマー", "美くびれ", "美尻", "中出し", "スパッツ", "フィットネス"]
  },
  {
    id: "feature_kimono_young_wife_inn_midnight_creampie",
    query: "着物 若妻",
    title: "【衣擦れの音とはんなり乱れる帯の隙間】着物若妻・老舗旅館特集！客室の畳の上で帯を解かれ白い太ももを露わに突かれる極上和風艶情AV名作選",
    category: "和風・着物",
    themeKeyword: "着物・若妻・老舗旅館・畳・帯解き・うなじ・はんなり・和風艶情",
    searchIntent: "美しい着物を着た人妻や若女将が、畳の部屋で帯を解かれ着崩れた姿のまま激しく交わる和風エロスAVを探しているユーザー向け",
    introTone: "い草の香りが立ち込める静かな和室。しっとりと結い上げられたうなじと、艶やかな着物の衣擦れの音。男の手によって帯が解かれ、幾重にも重なる襟元がはだける瞬間。畳の上に散らばる着物と、白く透き通る柔肌に深く突き刺さる熱い欲望の調べ——。",
    tags: ["着物", "若妻", "和風", "畳", "老舗旅館", "中出し", "美魔女", "人妻"]
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
  console.log("=== Starting generation of 20 brand-new high-depth feature articles (Batch 3) ===");
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
      published: new Date(Date.now() - ((i + 50) * 3600000)).toISOString(),
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

  console.log(`=== Complete! Successfully generated ${successCount} articles in Batch 3. ===`);
}

run();
