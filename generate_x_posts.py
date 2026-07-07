import os
import json
import re
import requests
from pathlib import Path

# 出力先ディレクトリ
OUTPUT_DIR = Path("/Users/calro/Downloads/post")
POSTS_DIR = Path("src/data/posts")

# 伏せ字置換マップ（Xの規約・センシティブ制限対策・検索性維持）
MILD_REPLACEMENTS = {
    "生中出し": "生中*し",
    "中出し": "中*し",
    "ネトラレ": "ネト*レ",
    "寝取り": "寝*り",
    "寝取られ": "寝取*れ",
    "おっぱい": "おっ*い",
    "セックス": "セッ*ス",
    "オナニー": "オナ*ー",
    "クンニ": "クン*",
    "フェラ": "フェ*",
    "騎乗位": "騎*位",
    "潮吹き": "潮*き",
    "巨乳": "巨*",
    "爆乳": "爆*",
    "射精": "射*",
    "放尿": "放*",
    "黄金": "黄*",
    "本番": "本*",
    "痴漢": "痴*",
    "強姦": "強*",
    "監禁": "監*",
    "奴隷": "奴*",
    "輪姦": "輪*",
    "乱交": "乱*",
    "SM": "S*",
    "ザーメン": "ザー*",
    "マンコ": "マ*コ",
    "おまんこ": "おま*こ",
    "ちんこ": "ち*こ",
    "チンポ": "チ*ポ",
    "デカチン": "デカ*",
    "不倫": "不*",
    "露出": "露*",
    "全裸": "全*",
    "半裸": "半*",
    "ハメ撮り": "ハメ*",
    "バイブ": "バイ*",
    "ローター": "ロー*",
    "オナホ": "オナ*",
    "痴女": "痴*",
    "性交": "性*",
    "SEX": "S*X",
    "野球拳": "野*拳",
    "素人": "素*",
    "興奮": "興*",
    "背徳": "背*",
    "裸": "裸*",
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
        # 大文字小文字を考慮して置換
        text = re.sub(re.escape(orig), MILD_REPLACEMENTS[orig], text, flags=re.IGNORECASE)
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

def generate_unique_hook(data):
    actresses = data.get("actresses", [])
    genres = data.get("genres", [])
    title = data.get("title", "")
    
    actress = actresses[0] if actresses else ""
    
    # 伏せ字化した女優名
    if actress:
        actress_masked = mildify(actress)
        # 女優名優先のフック（独自の煽り文句）
        if "ハイクオリティVR" in genres or "VR専用" in genres or "VR" in title:
            return f"【{actress_masked}さんの超リアルVR】"
        elif "若妻・幼妻" in genres or "人妻" in genres or "奥様" in title or "妻" in title:
            return f"【{actress_masked}さんが魅せる秘密の関係】"
        elif "素人" in genres or "素人" in title:
            return f"【{actress_masked}さんの素顔に迫る】"
        elif "巨乳" in genres or "爆乳" in genres or "巨乳" in title:
            return f"【{actress_masked}さんの抜群スタイル】"
        else:
            return f"【{actress_masked}さん出演の話題作】"
            
    # 女優名がない場合
    if "ハイクオリティVR" in genres or "VR専用" in genres or "VR" in title:
        return "【圧倒的臨場感のVR】"
    elif "若妻・幼妻" in genres or "人妻" in genres or "奥様" in title or "妻" in title:
        return "【秘密の関係にドキドキ】"
    elif "素人" in genres or "素人" in title:
        return "【親しみやすさが魅力】"
    elif "巨乳" in genres or "爆乳" in genres or "巨乳" in title:
        return "【スタイル抜群のヒロイン】"
        
    return "【今夜おすすめの注目作】"

def process_post(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    post_id = data.get("id")
    title = data.get("title", "")
    hinban = data.get("hinban", "")
    review = data.get("review", "")
    actresses = data.get("actresses", [])
    
    # 品番のチェック（存在しないか、無効な値ならスキップ）
    if not hinban:
        print(f"[{post_id}] 品番情報がないためポスト作成をスキップします。")
        return
        
    hinban_clean = hinban.strip()
    if not hinban_clean or hinban_clean.lower() in ["n/a", "none", "null", "なし", "-", "n/a (n/a)"]:
        print(f"[{post_id}] 無効な品番 ({hinban}) のためポスト作成をスキップします。")
        return
        
    # 品番の整形
    if "(" in hinban_clean:
        hinban_clean = hinban_clean.split("(")[0].strip()
        
    # タイトルのクレンジング（重複フックの排除）
    title_clean = title
    title_clean = re.sub(r'【超ド級の背徳感】', '', title_clean)
    title_clean = re.sub(r'【VR】', '', title_clean)
    title_clean = re.sub(r'【[^】]+】', '', title_clean) # 既存のブラケットフックを全て削る
    title_clean = title_clean.strip()
    
    # 動的に独自のフック（煽り文句）を生成
    hook = generate_unique_hook(data)
    
    # タイトルの伏せ字化（マイルド化）
    main_title = mildify(title_clean)
    
    # ベースのパーツ（フック、メインタイトル）
    base_parts = [hook, "", f"「{main_title}」"]
    
    # フッターのパーツ（CTA、品番導線）
    cta = "詳しくはプロフから👏"
    footer_parts = [
        "",
        cta,
        "",
        "⬇️品番⬇️",
        "",
        f"品番：{hinban_clean}"
    ]
    
    # ベース + フッターの合計文字数を計算
    base_text = "\n".join(base_parts + footer_parts)
    available_len = 140 - len(base_text)
    
    added_sentences = []
    # 余白が15文字以上ある場合のみ、紹介文（要約）の挿入を試みる
    if available_len >= 15:
        summary_text = extract_summary(review)
        summary_text = mildify(summary_text)
        
        # 句点で分割して個々の文にする
        raw_sentences = re.split(r'(?<=[。！?])', summary_text)
        sentences = []
        for s in raw_sentences:
            s = s.strip()
            if s and len(s) > 2:
                sentences.append(s)
                
        for s in sentences:
            # 空行区切りにするため、各文の文字数＋2（改行2つ分）をオーバーヘッドとして計算
            needed_len = len(s) + 2
            if available_len >= needed_len:
                added_sentences.append(s)
                available_len -= needed_len
            else:
                break
                
    # 最終的なポストの組み立て
    final_parts = [hook, "", f"「{main_title}」"]
    
    # 紹介文があれば空行を挟んで追加
    for s in added_sentences:
        final_parts.append("")
        final_parts.append(s)
        
    # フッターの追加
    final_parts.extend(footer_parts)
    
    post_text = "\n".join(final_parts)
    
    # 最終文字数制限のチェック
    if len(post_text) > 140:
        post_text = post_text[:137] + "…"
        
    # 出力先ディレクトリの特定
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
    for idx, sample_url in enumerate(samples[:3]):
        image_urls.append((f"sample_{idx+1}.jpg", sample_url))
        
    for name, url in image_urls:
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                with open(post_dir / name, 'wb') as img_f:
                    img_f.write(r.content)
        except Exception:
            pass
            
    return post_id

def main():
    import shutil
    print("Xポスト用データの生成を開始します...")
    json_files = list(POSTS_DIR.glob("*.json"))
    print(f"合計 {len(json_files)} 件の記事が見つかりました。")
    
    processed_ids = set()
    
    for idx, json_file in enumerate(json_files):
        try:
            # 正常に処理された場合はIDをセットに追加
            post_id = json_file.stem
            res = process_post(json_file)
            # process_postがスキップされずに完了した場合のみIDを記録
            # 実際には process_post 内でスキップ時は return しているので、最後まで到達した場合にIDを追加するように process_post の末尾に return post_id を追加します
            if res:
                processed_ids.add(res)
                
            if (idx + 1) % 20 == 0 or (idx + 1) == len(json_files):
                print(f"進捗: {idx + 1}/{len(json_files)} 件処理完了。")
        except Exception as e:
            print(f"エラー発生 ({json_file.name}): {e}")
            
    # クリーンアップ処理
    print("不要な古いフォルダのクリーンアップを開始します...")
    for item in OUTPUT_DIR.iterdir():
        if item.is_dir():
            if item.name not in processed_ids:
                try:
                    shutil.rmtree(item)
                    print(f"削除しました (品番なし等の対象外): {item.name}")
                except Exception as e:
                    print(f"削除エラー ({item.name}): {e}")
                    
    print("すべての処理が完了しました。")

if __name__ == "__main__":
    main()
