const fs = require('fs');
const path = require('path');

// ビルド時に個別JSONファイルを結合して一時的なposts.jsonを生成し、
// Next.jsビルドがそれを静的読み込みできるようにするプレビルド処理
const POSTS_DIR = path.join(__dirname, 'src', 'data', 'posts');
const PUBLIC_DATA_DIR = path.join(__dirname, 'public', 'data');
const OUTPUT_FILE = path.join(PUBLIC_DATA_DIR, 'posts.json');

function main() {
  console.log('--- Prebuild: Bundling individual post JSONs for Next.js ---');
  
  // posts.json出力先のディレクトリを作成
  fs.mkdirSync(PUBLIC_DATA_DIR, { recursive: true });

  let posts = [];
  
  if (fs.existsSync(POSTS_DIR)) {
    const files = fs.readdirSync(POSTS_DIR).filter(file => file.endsWith('.json'));
    
    posts = files.map(file => {
      try {
        const content = fs.readFileSync(path.join(POSTS_DIR, file), 'utf8');
        return JSON.parse(content);
      } catch (err) {
        console.error(`Failed to parse: ${file}`, err);
        return null;
      }
    }).filter(Boolean);

    // 未来の発売日・公開日（予約作品）を除外
    const now = new Date();
    posts = posts.filter(post => {
      if (!post.date) return true;
      const postDate = new Date(post.date);
      return postDate.getTime() <= now.getTime();
    });

    // 最新記事順（date降順）にソート
    posts.sort((a, b) => {
      const dateA = new Date(a.date || 0);
      const dateB = new Date(b.date || 0);
      return dateB.getTime() - dateA.getTime();
    });

    // 一覧表示・検索に必要な軽量フィールドのみを抽出（巨大なreview長文HTMLやsample_images配列を省きHTMLサイズを劇的に軽量化）
    const summaryPosts = posts.map(post => {
      // reviewからHTMLタグを除去して先頭120文字のみ抽出
      let shortReview = "";
      if (post.review) {
        shortReview = post.review.replace(/<[^>]*>?/gm, '').trim().slice(0, 120);
        if (post.review.length > 120) shortReview += '...';
      }

      // 10選記事の場合、記事内の作品画像1〜4枚を抽出して4分割コラージュサムネイル用に保持
      let featuredImages = undefined;
      const isTenSelection = (post.title && post.title.includes("10選")) ||
        (post.genres && post.genres.some(g => typeof g === 'string' && g.includes("10選")));

      if (isTenSelection) {
        const rawContent = post.review || post.content || "";
        const matches = rawContent.match(/https?:\/\/[^\s"'<>]+\.(?:jpg|jpeg|png)/g) || [];
        const seen = new Set();
        const uniq = [];
        for (const m of matches) {
          if (!seen.has(m)) {
            seen.add(m);
            uniq.push(m);
          }
        }
        if (uniq.length >= 4) {
          featuredImages = uniq.slice(0, 4);
        } else if (uniq.length > 0) {
          featuredImages = uniq;
        }
      }

      return {
        id: post.id,
        hinban: post.hinban || "",
        title: post.title || "",
        review: shortReview,
        image: post.image || "",
        featured_images: featuredImages,
        affiliate_url: post.affiliate_url || "",
        genres: post.genres || [],
        actresses: post.actresses || [],
        directors: post.directors || [],
        maker: post.maker || "",
        price: post.price || "300~",
        date: post.date || "",
        labels: post.labels || [],
        sample_movie_url: post.sample_movie_url || "",
        sample_images: post.sample_images || []
      };
    });

    fs.writeFileSync(OUTPUT_FILE, JSON.stringify(summaryPosts), 'utf8');
    console.log(`Bundled ${summaryPosts.length} posts into ${OUTPUT_FILE} (Optimized for ultra-fast load and Cloudflare Pages limit)`);
  }
}

main();
