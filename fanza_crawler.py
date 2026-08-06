def generate_article_with_llm(item):
    title = item.get("title", "")
    comment = item.get("comment", "")
    genres = ", ".join([g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])])
    
    safe_title = clean_for_safety(title)
    safe_comment = clean_for_safety(comment)
    safe_genres = clean_for_safety(genres)

    prompt = f"""以下の作品情報を基にして、指定の執筆ルールに従ってブログ記事のHTML本文（レビュー文）を生成してください。

【作品名】: {safe_title}
【あらすじ】: {safe_comment}
【ジャンル】: {safe_genres}

【執筆ルール】
1. ペルソナ: ネットで絶大な支持を集めるカリスマ熱血レビュアー。圧倒的な文章の熱量で語ってください。
2. 感情的なキャッチコピー: 冒頭に見出し（<h3>）を配置してください。
3. 心理描写: ストーリー・心理・情景の推しポイントを熱量MAXで書いてください。
4. 出力フォーマット: 本文のみをHTML（<p>, <h3>, <strong>）で出力し、マークダウンのコードブロックは一切出力しないでください。
"""

    system_message = "あなたはネットで絶大な支持を集めるカリスマ熱血レビュアーです。規約に配慮しつつ極めて熱量の高いレビュー文をHTML形式で作成します。"

    generated = generate_article_with_llm_text(prompt, system_message)
    if generated:
        print("Successfully generated review via Multi-LLM Engine.")
        return generated

    print("Warning: All LLM models failed. Using high-quality fallback template.")
    fallback_html = f"""
    <h3>禁断のシチュエーションが織りなす大人の濃厚ストーリー！</h3>
    <p>日常のすぐ裏側に潜むスリリングな関係を描いた、本能を揺さぶる名作が登場しました。</p>
    <p><strong>「日常が静かに、しかし劇的に崩壊していく感覚」</strong>をじっくりと味わえる本作。登場人物たちが織りなす葛藤と、罪悪感に濡れた表情はまさにマニアも納得の仕上がりです。</p>
    <p>禁断 of 領域へと足を踏み入れていく二人の蜜月を、ぜひその目で確かめてみてください。</p>
    """
    return fallback_html.strip()

def save_individual_post(post_data):
    os.makedirs(POSTS_DIR, exist_ok=True)
    post_id = post_data["id"]
    file_path = os.path.join(POSTS_DIR, f"{post_id}.json")
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f"Successfully saved individual JSON: {file_path}")

def main():
    try:
        # 1. FANZAから商品取得
        item = fetch_fanza_item()
        if not item:
            print("No new items found that haven't been posted yet. Exiting cleanly (exit 0).")
            return

        content_id = item.get("content_id")
        title = item.get("title")
        affiliate_url = item.get("affiliateURL")
        
        # リンク用のアフィリエイトIDをonchan555-003に変更
        if affiliate_url:
            affiliate_url = affiliate_url.replace("af_id=onchan555-999", "af_id=onchan555-003")
            api_aff_id = os.environ.get("FANZA_AFFILIATE_ID")
            if api_aff_id and api_aff_id != "onchan555-003":
                affiliate_url = affiliate_url.replace(f"af_id={api_aff_id}", "af_id=onchan555-003")

        print(f"Selected FANZA Item: {title} ({content_id})")

        # 画像URL
        image_url = ""
        images = item.get("imageURL", {})
        if images:
            image_url = images.get("large") or images.get("list") or ""
        
        movie = item.get("sampleMovieURL", {})
        sample_movie_url = movie.get("size_720_480") or movie.get("size_644_414") or movie.get("size_560_360") or movie.get("size_476_306") or ""
        if sample_movie_url and "onchan555-999" in sample_movie_url:
            sample_movie_url = sample_movie_url.replace("onchan555-999", LINK_AFFILIATE_ID)


        # サブ画像URL
        sample_images = []
        sample_img_obj = item.get("sampleImageURL", {}).get("sample_l", {})
        if sample_img_obj:
            sample_images = sample_img_obj.get("image", [])

        # 2. LLMでレビュー文生成
        review_html = generate_article_with_llm(item)

        # 3. 個別JSONデータ構造の組み立て
        post_data = {
            "id": content_id,
            "hinban": generate_hinban(content_id),
            "title": f"【超ド級の背徳感】 {title}",
            "review": review_html,
            "image": image_url,
            "sample_movie_url": sample_movie_url,
            "sample_images": sample_images,
            "affiliate_url": affiliate_url,
            "genres": [g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])],
            "actresses": [a.get("name", "") for a in item.get("iteminfo", {}).get("actress", [])],
            "maker": item.get("iteminfo", {}).get("maker", [{}])[0].get("name", ""),
            "date": item.get("date", time.strftime("%Y-%m-%d %H:%M:%S")),
            "labels": ["FANZA新作", "人妻", "ネトラレ", "背徳不倫"]
        }

        # 個別のJSONとして保存する
        save_individual_post(post_data)

        # 4. キャッシュに保存
        save_to_cache(content_id)
        print("Crawler run completed successfully.")

    except Exception as e:
        print(f"Error in execution: {e}")
        exit(1)

if __name__ == "__main__":
    main()
