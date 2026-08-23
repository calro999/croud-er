const fs = require('fs');
const path = require('path');
const https = require('https');

const API_ID = "4Lx0ftRf17Uuad6Ud7Gb";
const API_AFFILIATE_ID = "onchan555-999";
const OUT_AFFILIATE_ID = "onchan555-003";

const targetThemes = [
  {
    id: "feature_freshman_welcome_party_drunk_seduction",
    query: "新人OL 歓迎会",
    title: "【歓迎会の二次会帰りに始まる下剋上】新入社員×歓迎会特集！居酒屋の個室や先輩の部屋で泥酔した新人OLを朝まで生ハメし尽くす名作選",
    category: "オフィス・OL",
    themeKeyword: "新入社員・歓迎会・新人OL・居酒屋個室・泥酔・二次会・終電逃し・生中出し",
    searchIntent: "4月の新歓コンパや歓迎会で酒を飲まされた初々しい新入社員の女子が、先輩や上司にお持ち帰りされてハメられるAVを探しているユーザー向け",
    introTone: "春の夜、緊張した面持ちで乾杯を繰り返す新入社員の歓迎会。二次会を終え、アルコールで頬を赤く染めた新人OL。「もう歩けないです…」と寄り添ってくる無防備な身体をタクシーに乗せ、ホテルで新社会人の洗礼として激しく奥深くまで注ぎ込む——。",
    tags: ["新入社員", "歓迎会", "新人OL", "泥酔", "居酒屋", "お持ち帰り", "生中出し", "オフィス"]
  },
  {
    id: "feature_job_hunting_recruit_suit_creampie",
    query: "就活生 スーツ",
    title: "【黒髪リクルートスーツに包まれた緊張と背徳】就活女子大生特集！面接直前のホテルや企業説明会の裏で内定と引き換えに貫かれる名作選",
    category: "女子大生・スーツ",
    themeKeyword: "就活生・リクルートスーツ・黒髪・パンプス・面接前・内定・生中出し・面接官",
    searchIntent: "黒髪に黒のリクルートスーツを着た清楚な就活生が、面接官に弱みを握られたり面接会場の近くでハメられるシチュエーションAVを探しているユーザー向け",
    introTone: "糊の効いた白いブラウスと、黒のリクルートスーツに身を包んだ女子大生。人生をかけた就職活動の極度の緊張感の中、面接官に呼び出されたホテルの密室。内定への焦りと恐怖、そして強引な愛撫に濡れそぼっていくスーツスカートの奥の生々しい情欲——。",
    tags: ["就活生", "リクルートスーツ", "女子大生", "黒髪", "面接官", "内定", "生中出し", "スーツ"]
  },
  {
    id: "feature_kings_game_drinking_party_dare_sex",
    query: "王様ゲーム",
    title: "【命令ひとつで始まる理性を超えた過激な罰ゲーム】王様ゲーム・宅飲み特集！番号順に服を脱ぎキスから生挿入までエスカレートする乱痴気騒ぎAV名作選",
    category: "素人・乱交",
    themeKeyword: "王様ゲーム・宅飲み・罰ゲーム・キス・服脱ぎ・生挿入・サークル仲間・乱痴気騒ぎ",
    searchIntent: "宅飲みやサークルの飲み会で王様ゲームを始め、最初は軽いキスだった命令が徐々に服を脱がせ生本番へとエスカレートしていくAVを探しているユーザー向け",
    introTone: "「王様だーれだ！」の掛け声とともに割り箸が引かれる深夜の宅飲み。酔いが回るにつれて過激さを増していく王様の命令。最初は恥ずかしがっていた女の子が、皆の見ている前で服を脱がされ、最終的に生で突かれながら歓喜の声を上げる乱痴気騒ぎの極致——。",
    tags: ["王様ゲーム", "宅飲み", "罰ゲーム", "乱交", "露出", "生中出し", "女子大生", "素人風"]
  },
  {
    id: "feature_snowboard_resort_lodge_after_ski_sex",
    query: "スノボ ゲレンデ",
    title: "【白銀のゲレンデと暖炉の温もり】スノボ女子×スキー場ロッジ特集！ウェアを脱ぎ捨て冷え切った身体を温め合う雪山の濃厚密着交尾AV名作選",
    category: "スポーツ・旅行",
    themeKeyword: "スノボ・ゲレンデ・スキー場・ロッジ・スノーボードウェア・雪山・暖炉・密着",
    searchIntent: "スキー場やスノボ旅行で可愛いスノボ女子と出会い、ナイター終わりのロッジやコテージでウェアを脱がせてハメまくるリゾートAVを探しているユーザー向け",
    introTone: "粉雪舞い散る白銀のゲレンデ。カラフルなスノボウェアにニット帽をかぶったゲレンデ美女。吹雪を避けて駆け込んだ山小屋ロッジの暖炉の前、何重にも着込んだウェアを一枚ずつ脱がせ、火照った素肌同士を擦り合わせながら激しく雪山の静寂を破る——。",
    tags: ["スノボ", "ゲレンデ", "スキー場", "ロッジ", "ウェア", "雪山", "中出し", "素人風"]
  },
  {
    id: "feature_glamping_luxury_tent_nature_intimacy",
    query: "グランピング",
    title: "【大自然の中の豪華ドームテントで過ごす夜】グランピング・隠れ家特集！満天の星空の下で焚き火を眺めキングサイズベッドで乱れる極上リゾートAV名作選",
    category: "野外・シチュエーション",
    themeKeyword: "グランピング・ドームテント・豪華リゾート・焚き火・星空・キングサイズベッド・大自然",
    searchIntent: "大自然の中のお洒落なグランピングドームテントで、焚き火やBBQを楽しんだあとにラグジュアリーなベッドでハメ合う高級アウトドアAVを探しているユーザー向け",
    introTone: "パチパチと爆ぜる焚き火の炎と、虫の音が心地よい大自然の夜。透明なドームテントの中から見上げる満天の星空。冷えた夜風とは対照的に、豪華なキングサイズベッドの上で熱く絡み合う二人の肉体。日常を完全に忘れた極上のグランピングセックス——。",
    tags: ["グランピング", "ドームテント", "アウトドア", "リゾート", "キングサイズベッド", "中出し", "美少女", "野外"]
  },
  {
    id: "feature_houseboat_yakatabune_river_cruise_affair",
    query: "屋形船",
    title: "【川面に揺れる提灯の灯りと座敷の狂宴】屋形船・宴会特集！波に揺れる船内で浴衣姿のコンパニオンやバイト美女と人目を忍んで繋がる背徳名作選",
    category: "和風・宴会",
    themeKeyword: "屋形船・宴会・川下り・提灯・座敷・浴衣コンパニオン・揺れる船内・背徳",
    searchIntent: "屋形船の貸切宴会で、川の揺れとアルコールに酔いしれながら、座敷の奥やトイレで浴衣美女とこっそりハメ合う風情あるAVを探しているユーザー向け",
    introTone: "川面に揺れる赤提灯の光と、心地よい波の揺らめき。天ぷらと酒が振る舞われる屋形船の座敷。宴会が盛り上がる中、船尾の物陰や障子の隙間で交わされる秘密の合図。船の揺れに合わせて深く突き刺さる肉棒に、川音に紛れて吐息を漏らす——。",
    tags: ["屋形船", "宴会", "和風", "浴衣", "コンパニオン", "中出し", "背徳", "酒"]
  },
  {
    id: "feature_night_pool_party_luxury_hotel_creampie",
    query: "ナイトプール",
    title: "【ネオン輝く水面とライトアップされた肉体美】ナイトプール特集！光るカクテルを片手に極小ビキニの美女たちとプールサイドの個室ベッドで乱れる名作選",
    category: "ギャル・水着",
    themeKeyword: "ナイトプール・ライトアップ・極小ビキニ・ラグジュアリーホテル・カクテル・プールサイド",
    searchIntent: "高級ホテルのナイトプールで、SNS映えする水着を着たスタイル抜群の美女たちとプールサイドのガゼボでハメ倒すパーティー系AVを探しているユーザー向け",
    introTone: "ピンクやブルーのLEDにライトアップされた幻想的な夜のプール。水着の上からでもわかる豊満な胸元と、水滴を弾く滑らかな美肌。ガゼボのカーテンを閉め切ったベッドの上、濡れたビキニのクロッチをずらして滑り込む極上のナイトリゾート交尾——。",
    tags: ["ナイトプール", "ビキニ", "水着", "ギャル", "ラグジュアリー", "中出し", "美脚", "パリピ"]
  },
  {
    id: "feature_rooftop_beer_garden_summer_night_sex",
    query: "ビアガーデン",
    title: "【心地よい夜風と生ビールの開放感】屋上ビアガーデン特集！バイト終わりの制服美女やほろ酔いOLとネオンの陰で人目を忍んで交わる名作選",
    category: "シチュエーション",
    themeKeyword: "ビアガーデン・屋上・生ビール・制服バイト・夜風・ネオン・開放感・立ちバック",
    searchIntent: "デパートの屋上ビアガーデンで、ビールを運ぶ制服姿のバイト美女や泥酔したOLと、屋上の物陰で立ちバックでハメる夏の夜AVを探しているユーザー向け",
    introTone: "ジョッキのぶつかる乾杯の音と、賑やかな笑い声が夜空に溶けていく屋上ビアガーデン。ラストオーダーを終えた薄暗いビール樽置き場の裏。制服のエプロンをまくり上げ、夜景の光を背に受けて激しく腰を振る、真夏の夜の開放的な情事——。",
    tags: ["ビアガーデン", "屋上", "バイト制服", "生ビール", "立ちバック", "中出し", "OL", "真夏"]
  },
  {
    id: "feature_female_bartender_cocktail_counter_sex",
    query: "バーテンダー 女性",
    title: "【シェイカーを振る凛とした指先が乱れる夜】女性バーテンダー特集！閉店後の静かなBARカウンターの上でカクテルグラスを横目に突かれる名作選",
    category: "職業・制服",
    themeKeyword: "バーテンダー・女性バーテン・BARカウンター・ベスト・カクテル・閉店後・シェイカー",
    searchIntent: "黒ベストを着こなすクールで美しい女性バーテンダーが、営業終了後の店内でカウンターの上に座らされハメられるシチュエーションAVを探しているユーザー向け",
    introTone: "バックバーに並ぶ琥珀色のボトルと、静かに流れるジャズの調べ。看板の明かりを落とした深夜のBAR。黒いベストとネクタイを緩められた美人バーテンダーが、磨き上げられた一枚板のカウンターの上で、グラスを揺らしながら激しいピストンに溺れていく——。",
    tags: ["バーテンダー", "BAR", "カウンター", "ベスト", "制服", "中出し", "クールビューティー", "酒"]
  },
  {
    id: "feature_darts_bar_private_room_bet_game_sex",
    query: "ダーツバー",
    title: "【ブルを外した罰ゲームで衣服を脱ぎ捨てる】ダーツバー特集！薄暗いVIPルームでハットトリックの歓声に包まれながら即ハメされる夜遊びAV名作選",
    category: "素人・夜遊び",
    themeKeyword: "ダーツバー・VIP個室・ダーツマシン・罰ゲーム・テキーラ・即ハメ・ミニスカ",
    searchIntent: "ダーツバーのVIPルームでテキーラを賭けたマッチを行い、負けたミニスカ美女がそのままソファでハメられる夜遊び系AVを探しているユーザー向け",
    introTone: "エレクトリックダーツマシンの鮮やかなライティングと、矢が刺さる小気味よい音。テキーラのショットを重ねるうちに熱を帯びるVIPブース。ダーツの勝負に負けたミニスカ美女をソファに押し倒し、周囲の歓声にかき消されながら奥まで貫くスリリングな夜——。",
    tags: ["ダーツバー", "VIPルーム", "罰ゲーム", "テキーラ", "即ハメ", "中出し", "ミニスカート", "素人風"]
  },
  {
    id: "feature_bowling_alley_night_game_mini_skirt_sex",
    query: "ボウリング",
    title: "【ストライクの瞬間に揺れるミニスカと美尻】ボウリング場特集！深夜の貸切レーンでシューズを履いたまま投球フォームの体勢で突かれる名作選",
    category: "スポーツ・夜遊び",
    themeKeyword: "ボウリング・貸切レーン・投球フォーム・ミニスカ・美尻・深夜・即ハメ",
    searchIntent: "深夜のボウリング場で、ミニスカ姿の女の子が投球フォームのアドレスをとったまま背後からハメられるフェティッシュなAVを探しているユーザー向け",
    introTone: "ピンが弾け飛ぶ爽快な轟音と、磨き上げられたウッドレーンの光沢。深夜の貸切ボウリング場で、ボールを構えるミニスカ美女の背後からぴったりと重なる男の影。スコアボードのモニター前で、ボールを握らせたまま激しく腰を打ち付ける背後交尾——。",
    tags: ["ボウリング", "ミニスカート", "貸切レーン", "背後密着", "中出し", "美尻", "素人風"]
  },
  {
    id: "feature_all_night_karaoke_missed_train_creampie",
    query: "カラオケ オール",
    title: "【始発を待つ明け方の気だるい密着】カラオケオール・朝帰り特集！歌い疲れて眠る友人の横でソファーに押し倒され声押し殺しイカされる名作選",
    category: "女子大生・素人",
    themeKeyword: "カラオケオール・始発待ち・明け方・歌い疲れ・サイレント・ソファー・朝帰り",
    searchIntent: "終電を逃してカラオケでオール（朝まで）過ごす男女が、他の友達が寝ている隣で声を殺してハメ合うリアルな青春AVを探しているユーザー向け",
    introTone: "明け方4時の薄暗いカラオケルーム。テーブルの上に散らばるポテトと空いたピッチャー。歌い疲れてソファーの端で泥のように眠る友人たち。そのすぐ隣、ブランケットに隠れて息を潜めながら、始発までの時間を惜しむように求め合う秘密の交わり——。",
    tags: ["カラオケ", "オール", "始発待ち", "声我慢", "サイレント", "中出し", "女子大生", "素人風"]
  },
  {
    id: "feature_wine_sommelier_cellar_tasting_seduction",
    query: "ソムリエ ワイン",
    title: "【ワインセラーのひんやりした静寂と熱い吐息】美人ソムリエール特集！年代物ヴィンテージの香りに包まれた地下貯蔵庫でドレスを捲られる名作選",
    category: "職業・制服",
    themeKeyword: "ソムリエ・ソムリエール・ワインセラー・地下貯蔵庫・テイスティング・ドレス・上品",
    searchIntent: "上品で知的な美人ソムリエールが、地下のワインセラーでワインの試飲を口実に客に抱かれ、樽に手をついて突かれる優雅なAVを探しているユーザー向け",
    introTone: "温度と湿度が厳格に保たれた地下ワインセラーの重厚な静寂。グラスを傾けテイスティングを行う気品ある美人ソムリエール。赤ワインで濡れた唇に重ねられる情熱的な口づけ。木樽が並ぶ薄暗い通路で、黒のイブニングドレスを捲り上げられて乱れる極上の夜——。",
    tags: ["ソムリエ", "ワインセラー", "地下貯蔵庫", "ドレス", "上品", "中出し", "美魔女", "テイスティング"]
  },
  {
    id: "feature_drinking_party_drunk_female_boss_hotel",
    query: "新入社員 飲み会",
    title: "【会社の飲み会で終電を逃した僕に差し伸べられた手】飲み会終電逃し特集！職場の憧れの美女の自宅にお泊まりして朝まで中出しし合う名作選",
    category: "オフィス・OL",
    themeKeyword: "飲み会・終電逃し・お泊まり・職場の先輩・憧れの同僚・ワンルーム・朝まで生ハメ",
    searchIntent: "会社の飲み会終わりに終電を逃し、同僚や先輩の家に泊まることになってそのままベッドで朝までハメ倒すオフィスラブAVを探しているユーザー向け",
    introTone: "改札口のシャッターが降りる音。終電を逃し途方に暮れる僕に「うちに泊まってく？」と微笑んだ職場の憧れの女性。シャワーを浴びて現れた濡れ髪の彼女の無防備な部屋着姿に、我慢していた欲望の防波堤が一気に決壊する——。",
    tags: ["飲み会", "終電逃し", "お泊まり", "社内恋愛", "OL", "生中出し", "部屋着", "甘々"]
  },
  {
    id: "feature_internship_college_student_office_seduction",
    query: "インターン 生徒",
    title: "【オフィス実習中に仕組まれた甘い罠】インターン女子大生特集！指導係の先輩社員と会議室で二人きりになりスーツ姿のまま奪われる名作選",
    category: "女子大生・オフィス",
    themeKeyword: "インターン・女子大生・オフィス実習・指導係・会議室・リクルートスーツ・初々しい",
    searchIntent: "就活インターンシップに参加した女子大生が、優秀な指導社員に会議室で密着指導され、そのまま机の上で犯されるシチュエーションAVを探しているユーザー向け",
    introTone: "緊張した面持ちでパソコンに向かうインターンシップの女子大生。ブラインドの降りた会議室で、マンツーマンの業務指導。キーボードを打つ手に重なる指導員の指先。まだ社会を知らない初々しい身体を、デスクに押し倒して貪り尽くす——。",
    tags: ["インターン", "女子大生", "リクルートスーツ", "会議室", "指導員", "中出し", "初々しい", "オフィス"]
  },
  {
    id: "feature_poolside_summer_bikini_creampie_climax",
    query: "ナイトプール ビキニ",
    title: "【プール上がりの濡れそぼるバストとくびれ】サマーリゾート・ビキニ特集！貸切ヴィラのプライベートプールで水から上がった瞬間そのまま貫く名作選",
    category: "水着・リゾート",
    themeKeyword: "プライベートプール・貸切ヴィラ・ビキニ・水滴・濡れ髪・即ハメ・生中出し",
    searchIntent: "プライベートヴィラのプールサイドで、水滴に濡れたビキニ美女を水から引き揚げた瞬間にそのまま生挿入するリゾートAVを探しているユーザー向け",
    introTone: "エメラルドグリーンに輝くプライベートプールの水面。プールサイドの手すりに手をかけ、水から上がり息を弾ませるビキニ美女。滴る水滴を拭う間もなく、濡れた水着をずらして後ろから一気に突き入れる、真夏の贅沢極まるプールサイドセックス——。",
    tags: ["プライベートプール", "ビキニ", "水着", "貸切ヴィラ", "即ハメ", "生中出し", "美脚", "真夏"]
  },
  {
    id: "feature_billiards_table_posture_deep_penetration",
    query: "ビリヤード",
    title: "【キューを構える前傾姿勢の無防備な美尻】ビリヤード特集！ラシャ台の上にうつ伏せにされ美しいフォームのまま背後から激しく突かれる名作選",
    category: "スポーツ・夜遊び",
    themeKeyword: "ビリヤード・プールバー・ラシャ台・前傾姿勢・キュー・背後挿入・ミニスカ",
    searchIntent: "ビリヤード台の上でキューを構えた前傾姿勢の女性が、ミニスカを捲り上げられて後ろから生ハメされるフェティッシュなAVを探しているユーザー向け",
    introTone: "スポットライトに照らし出された緑色のビリヤード台。的球を狙い、台の上に胸を乗せて前傾姿勢をとるミニスカ美女。キューを持つ腕の隙間から伸びる手先、スカートをたくし上げられ、完璧なフォームのまま深奥まで貫かれる美しき撞球のエロス——。",
    tags: ["ビリヤード", "プールバー", "ラシャ台", "前傾姿勢", "背後挿入", "中出し", "美尻", "ミニスカート"]
  },
  {
    id: "feature_group_date_gokon_takeout_hotel_sex",
    query: "合コン お持ち帰り",
    title: "【合コンの勝者だけが味わえる至福の果実】合コンお持ち帰り特集！ゲームで負けた罰ゲームから抜け駆けしてホテル直行で生ハメする決定版名作選",
    category: "素人・ナンパ",
    themeKeyword: "合コン・お持ち帰り・抜け駆け・タクシー・ホテル直行・泥酔・即ハメ・素人風",
    searchIntent: "合コンで一番可愛い女の子を他の男たちを出し抜いてお持ち帰りし、ホテルで朝まで濃厚にハメ倒すドキュメント風AVを探しているユーザー向け",
    introTone: "コールが飛び交う賑やかな合コンの席。トイレに立った彼女を追いかけ、廊下の物陰で交わした秘密のキス。会計のドサクサに紛れて二人でタクシーに飛び乗り、ホテルの部屋に入った瞬間に激しく貪り合う、完全勝利のお持ち帰りナイト——。",
    tags: ["合コン", "お持ち帰り", "抜け駆け", "ホテル直行", "即ハメ", "生中出し", "素人風", "女子大生"]
  },
  {
    id: "feature_resort_hotel_honeymoon_suite_passion",
    query: "グランピング",
    title: "【二人だけの秘密の隠れ家で愛し合う】プライベートコテージ特集！誰の視線も届かない森のコテージで服を着る時間さえ惜しんで交わる名作選",
    category: "旅行・リゾート",
    themeKeyword: "プライベートコテージ・森の隠れ家・露天ジャグジー・ウッドデッキ・全裸・朝まで",
    searchIntent: "森の中に佇む貸切コテージで、露天ジャグジーやウッドデッキを全裸で行き来しながら一日中ハメ狂うカップル系AVを探しているユーザー向け",
    introTone: "木漏れ日が差し込む静寂の森に佇むプライベートコテージ。ウッドデッキに設置された露天ジャグジーから立ち上る湯気。誰にも邪魔されない空間で、一日中全裸のまま過ごし、思い立った場所で何度でも繋がる極上のリゾートバケーション——。",
    tags: ["コテージ", "リゾート", "ジャグジー", "ウッドデッキ", "全裸", "生中出し", "美少女", "旅行"]
  },
  {
    id: "feature_yakatabune_summer_night_river_coitus",
    query: "屋形船",
    title: "【花火大会の夜空の下で揺れる川面の情事】屋形船×花火特集！ドーンと響く打ち上げ花火の轟音に合わせて船底で激しく突き上げる名作選",
    category: "和風・イベント",
    themeKeyword: "屋形船・花火大会・打ち上げ花火・轟音・浴衣・船底・川下り・生ハメ",
    searchIntent: "花火大会を屋形船から鑑賞しながら、花火の轟音に紛れて浴衣姿の美女と船内でハメ狂う情緒溢れるAVを探しているユーザー向け",
    introTone: "夜空を彩る大輪の花火と、胸に響く重低音の破裂音。川面を埋め尽くす船の群れ。窓の外を華やかに照らす閃光の合間、船底の個室で浴衣をはだけさせた美女。花火の轟音にかき消されながら、激しく打ち付けるピストンに歓喜の涙を流す——。",
    tags: ["屋形船", "花火大会", "浴衣", "和風", "打ち上げ花火", "中出し", "生ハメ", "情緒"]
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
  console.log("=== Starting generation of 20 brand-new high-depth feature articles (Batch 6) ===");
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
      published: new Date(Date.now() - ((i + 125) * 3600000)).toISOString(),
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

  console.log(`=== Complete! Successfully generated ${successCount} articles in Batch 6. ===`);
}

run();
