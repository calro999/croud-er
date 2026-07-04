import os
import json
import re
import requests
from pathlib import Path

# 出力先ディレクトリ
OUTPUT_DIR = Path("/Users/calro/Downloads/post")
POSTS_DIR = Path("src/data/posts")

# マイルド化置換マップ（Xの規約・センシティブ制限対策を大幅強化）
MILD_REPLACEMENTS = {
    # 性的・過激な行為や設定の言い換え
    "騎乗位": "息の合ったパフォーマンス",
    "キス・接吻": "甘いキス",
    "接吻": "キス",
    "巨乳": "スタイル抜群",
    "爆乳": "スタイル抜群",
    "豊満": "スタイル抜群",
    "美乳": "スタイル抜群",
    "美少女": "可憐なヒロイン",
    "中出し": "情熱的な愛",
    "フェラ": "甘いひととき",
    "手コキ": "手と手の触れ合い",
    "クンニ": "優しい愛撫",
    "愛撫": "スキンシップ",
    "潮吹き": "最高潮の盛り上がり",
    "本番": "大人の時間",
    "淫乱": "情熱的",
    "素人": "親しみやすい",
    "痴漢": "スリリングなハプニング",
    "密室": "プライベート空間",
    "監禁": "クローズドな関係",
    "制服": "お揃いのスタイル",
    "コスプレ": "特別な衣装",
    "緊縛": "緊迫した展開",
    "SM": "刺激的な関係",
    "エロ": "セクシー",
    "セクシー": "魅惑的",
    "官能": "ロマンチック",
    "快楽": "心地よさ",
    "背徳": "秘密の",
    "背徳感": "ドキドキ感",
    "興奮": "高揚感",
    "妄想": "想像",
    "狂気": "情熱",
    "脳裏に深く刻み込まれる": "印象に残る",
    "最高傑作": "話題の作品",
    "バズり中": "人気の",
    "AV": "作品",
    "アダルト": "大人向け",
    "おっぱい": "胸元",
    "セックス": "愛の営み",
    "ローター": "マッサージ器",
    "バイブ": "大人のおもちゃ",
    "オナニー": "セルフケア",
    "射精": "絶頂",
    
    # 追加のセンシティブワード対策
    "ネトラレ": "秘密の関係",
    "寝取り": "秘密の関係",
    "寝取られ": "秘密の関係",
    "NTR": "秘密の関係",
    "不倫": "秘密の関係",
    "裸": "美しい姿",
    "全裸": "美しい姿",
    "半裸": "美しい姿",
    "露出": "披露",
    "ぐっちょり": "しっとり",
    "野球拳": "ゲーム",
    "痴女": "大胆な女性",
    "売春": "特別な出会い",
    "援交": "特別な出会い",
    "jk": "学生風",
    "jc": "学生風",
    "女子校生": "学生風",
    "女子高生": "学生風",
    "巨尻": "スタイル抜群",
    "美尻": "スタイル抜群",
    "お尻": "ヒップ",
    "尻": "ヒップ",
    "フェチ": "こだわり",
    "マゾ": "刺激的",
    "サド": "刺激的",
    "拷問": "刺激的",
    "調教": "特別なレッスン",
    "輪姦": "大勢での関係",
    "乱交": "大勢での関係",
}

def clean_html(html_content):
    # HTMLタグを除去
    clean = re.compile('<.*?>')
    text = re.sub(clean, '', html_content)
    # 連続する空白や改行を整理
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def mildify(text):
    # 置換をループ（長さに依存しないようにキーの長さ順にソートして置換）
    sorted_keys = sorted(MILD_REPLACEMENTS.keys(), key=len, reverse=True)
    for orig in sorted_keys:
        text = text.replace(orig, MILD_REPLACEMENTS[orig])
    return text

def extract_summary(review_html):
    # HTMLから不要なレビュー用定型文を除去して、最初の自然な文を抽出する
    text = clean_html(review_html)
    
    # レビュー用の煽り文句を除去
    text = re.sub(r'【[^】]+】', '', text)
    text = re.sub(r'『[^』]+』の全貌と圧倒的魅力に迫る！?', '', text)
    text = re.sub(r'その魅力の真髄と.*?レビューしていきます！?', '', text)
    text = re.sub(r'絶対に一度は見るべき.*?話題を呼んでいる', '', text)
    text = re.sub(r'なぜここまで多くの人々を熱狂させ.*?深掘りして', '', text)
    
    # 句点で分割して最初の数文を取得
    sentences = re.split(r'(?<=[。！?])', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    summary_parts = []
    length = 0
    for s in sentences:
        # 技術的・メタ的な文言は除外
        if any(w in s for w in ["アングル", "カメラ", "画質", "BGM", "口コミ", "総評", "保存", "非常にもったいない", "演出"]):
            continue
        if len(s) > 5 and length + len(s) < 80:
            summary_parts.append(s)
            length += len(s)
            
    summary = "".join(summary_parts)
    if not summary and sentences:
        summary = sentences[0]
        
    return summary

def process_post(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    post_id = data.get("id")
    title = data.get("title", "")
    hinban = data.get("hinban", "")
    review = data.get("review", "")
    actresses = data.get("actresses", [])
    
    # 品番の整形
    if "(" in hinban:
        hinban = hinban.split("(")[0].strip()
        
    # タイトルのクレンジングと分割（【フック】とメインタイトル）
    hook = ""
    main_title = title.replace("【VR】", "").strip()
    
    hook_match = re.match(r'^【([^】]+)】\s*(.*)', main_title)
    if hook_match:
        hook = hook_match.group(1)
        main_title = hook_match.group(2).strip()
    
    # マイルド化
    if hook:
        hook = f"【{mildify(hook)}】"
    main_title = mildify(main_title)
    
    # タイトルが長すぎる場合は切り詰める（最大50文字程度）
    if len(main_title) > 50:
        main_title = main_title[:47] + "…"
    
    main_title_formatted = f"「{main_title}」"
    
    # 要約の作成とマイルド化
    summary_text = extract_summary(review)
    summary_text = mildify(summary_text)
    
    # 句点で分割して個々の文にする
    raw_sentences = re.split(r'(?<=[。！?])', summary_text)
    sentences = []
    for s in raw_sentences:
        s = s.strip()
        if s and len(s) > 2:
            sentences.append(s)
            
    # 固定フッター部分の組み立て
    footer = f"\n\n⬇️品番⬇️\n\n品番：{hinban}\n詳しくはプロフから👏"
    
    # 140字以内のシミュレーションと組み立て
    post_parts = []
    if hook:
        post_parts.append(hook)
        post_parts.append("")
    post_parts.append(main_title_formatted)
    
    current_text = "\n".join(post_parts) + footer
    available_len = 140 - len(current_text)
    
    added_sentences = []
    for s in sentences:
        # 空行区切りにするため、2文字(改行2つ分)のオーバーヘッドを計算
        needed_len = len(s) + 2
        if available_len >= needed_len:
            added_sentences.append(s)
            available_len -= needed_len
        else:
            # 1つも入らない場合は切り詰めてでも1つ入れる
            if not added_sentences:
                slice_len = available_len - 4
                if slice_len > 5:
                    added_sentences.append(s[:slice_len] + "…")
            break
            
    # 最終的なリストの組み立て
    final_parts = []
    if hook:
        final_parts.append(hook)
        final_parts.append("")
    final_parts.append(main_title_formatted)
    
    for s in added_sentences:
        final_parts.append("")
        final_parts.append(s)
        
    final_parts.append("")
    final_parts.append("⬇️品番⬇️")
    final_parts.append("")
    final_parts.append(f"品番：{hinban}")
    final_parts.append("詳しくはプロフから👏")
    
    post_text = "\n".join(final_parts)
    
    # 念のための最終文字数制限
    if len(post_text) > 140:
        post_text = post_text[:137] + "…"
    
    # 出力先ディレクトリの作成
    post_dir = OUTPUT_DIR / post_id
    post_dir.mkdir(parents=True, exist_ok=True)
    
    # テキスト保存
    with open(post_dir / f"{post_id}.txt", 'w', encoding='utf-8') as f_out:
        f_out.write(post_text)
        
    # 画像のダウンロード
    image_urls = []
    if data.get("image"):
        image_urls.append(("cover.jpg", data.get("image")))
    
    samples = data.get("sample_images", [])
    for idx, sample_url in enumerate(samples[:3]):  # 最大3枚
        image_urls.append((f"sample_{idx+1}.jpg", sample_url))
        
    for name, url in image_urls:
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                with open(post_dir / name, 'wb') as img_f:
                    img_f.write(r.content)
        except Exception:
            pass # エラーは握りつぶして継続

def main():
    print("Xポスト用データの生成を開始します...")
    json_files = list(POSTS_DIR.glob("*.json"))
    print(f"合計 {len(json_files)} 件の記事が見つかりました。")
    
    for idx, json_file in enumerate(json_files):
        try:
            process_post(json_file)
            if (idx + 1) % 20 == 0 or (idx + 1) == len(json_files):
                print(f"進捗: {idx + 1}/{len(json_files)} 件処理完了。")
        except Exception as e:
            print(f"エラー発生 ({json_file.name}): {e}")
            
    print("すべての処理が完了しました。")

if __name__ == "__main__":
    main()
