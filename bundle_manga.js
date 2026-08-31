const fs = require('fs');
const path = require('path');

const mangaDir = path.join(__dirname, 'src', 'data', 'manga');
const outputFile = path.join(__dirname, 'public', 'data', 'manga.json');

console.log('--- Prebuild: Bundling manga JSONs ---');

if (!fs.existsSync(mangaDir)) {
  console.log('No manga directory found. Creating empty manga.json.');
  fs.mkdirSync(path.join(__dirname, 'public', 'data'), { recursive: true });
  fs.writeFileSync(outputFile, JSON.stringify([], null, 2), 'utf-8');
  process.exit(0);
}

const files = fs.readdirSync(mangaDir).filter(f => f.endsWith('.json'));
const allManga = [];

for (const file of files) {
  try {
    const content = fs.readFileSync(path.join(mangaDir, file), 'utf-8');
    const data = JSON.parse(content);
    allManga.push(data);
  } catch (e) {
    console.warn(`Skipping ${file}: ${e.message}`);
  }
}

// 日付降順ソート
allManga.sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());

// 一覧表示・検索・スコアリングに必要な軽量フィールドのみを抽出（巨大なreview長文HTMLやサンプル画像を省きファイルサイズを劇的に軽量化）
const summaryManga = allManga.map(m => {
  let shortReview = "";
  if (m.review) {
    shortReview = m.review.replace(/<[^>]*>?/gm, '').trim().slice(0, 120);
    if (m.review.length > 120) shortReview += '...';
  }
  return {
    id: m.id,
    hinban: m.hinban || "",
    title: m.title || "",
    review: shortReview,
    image: m.image || "",
    affiliate_url: m.affiliate_url || "",
    tachiyomi_url: m.tachiyomi_url || "",
    genres: m.genres || [],
    author: m.author || [],
    publisher: m.publisher || "",
    date: m.date || "",
    labels: m.labels || []
  };
});

fs.mkdirSync(path.join(__dirname, 'public', 'data'), { recursive: true });
fs.writeFileSync(outputFile, JSON.stringify(summaryManga), 'utf-8');
console.log(`Bundled ${summaryManga.length} manga into ${outputFile} (Optimized for Cloudflare Pages < 25MB limit)`);
