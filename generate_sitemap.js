const fs = require('fs');
const path = require('path');

const baseUrl = 'https://haitoku.pages.dev';
const postsDir = path.join(__dirname, 'src', 'data', 'posts');
const mangaDir = path.join(__dirname, 'src', 'data', 'manga');
const publicDir = path.join(__dirname, 'public');

if (!fs.existsSync(publicDir)) {
  fs.mkdirSync(publicDir, { recursive: true });
}

const nowIso = new Date().toISOString();

// ==========================================
// 1. 主要固定ページ用サイトマップ (sitemap_main.xml)
// ==========================================
let mainXml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>${baseUrl}</loc>
    <lastmod>${nowIso}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>${baseUrl}/fanza-tv-plus</loc>
    <lastmod>${nowIso}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>${baseUrl}/fanza-device-guide</loc>
    <lastmod>${nowIso}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.98</priority>
  </url>
  <url>
    <loc>${baseUrl}/features</loc>
    <lastmod>${nowIso}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.95</priority>
  </url>
  <url>
    <loc>${baseUrl}/ranking</loc>
    <lastmod>${nowIso}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>${baseUrl}/manga</loc>
    <lastmod>${nowIso}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>${baseUrl}/archives</loc>
    <lastmod>${nowIso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>`;
fs.writeFileSync(path.join(publicDir, 'sitemap_main.xml'), mainXml, 'utf8');

// ==========================================
// 2. 動画レビュー記事用サイトマップ (sitemap_posts.xml)
// ==========================================
const actressSet = new Set();
const genreSet = new Set();
const makerSet = new Set();

let postsXml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n`;

if (fs.existsSync(postsDir)) {
  const files = fs.readdirSync(postsDir).filter(f => f.endsWith('.json'));
  const now = Date.now();
  for (const file of files) {
    try {
      const post = JSON.parse(fs.readFileSync(path.join(postsDir, file), 'utf8'));
      if (!post || !post.id) continue;
      const postDate = post.date ? new Date(post.date).getTime() : 0;
      if (postDate > now) continue; // 発売日未到来の予約作品は除外
      const ageDays = (now - postDate) / (1000 * 60 * 60 * 24);
      const priority = ageDays < 30 ? 0.95 : ageDays < 90 ? 0.85 : ageDays < 180 ? 0.75 : 0.65;
      const lastmod = post.date ? new Date(post.date).toISOString() : nowIso;
      postsXml += `  <url>
    <loc>${baseUrl}/posts/${post.id}</loc>
    <lastmod>${lastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>${priority}</priority>
  </url>\n`;
      (post.actresses || []).forEach(a => { if (a) actressSet.add(a); });
      (post.genres || []).forEach(g => { if (g) genreSet.add(g); });
      if (post.maker) makerSet.add(post.maker);
    } catch (e) {}
  }
}
postsXml += `</urlset>`;
fs.writeFileSync(path.join(publicDir, 'sitemap_posts.xml'), postsXml, 'utf8');

// ==========================================
// 3. マンガ記事用サイトマップ (sitemap_manga.xml)
// ==========================================
const authorSet = new Set();
let mangaXml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n`;

if (fs.existsSync(mangaDir)) {
  const mangaFiles = fs.readdirSync(mangaDir).filter(f => f.endsWith('.json'));
  for (const file of mangaFiles) {
    try {
      const manga = JSON.parse(fs.readFileSync(path.join(mangaDir, file), 'utf8'));
      if (!manga || !manga.id) continue;
      const lastmod = manga.date ? new Date(manga.date).toISOString() : nowIso;
      mangaXml += `  <url>
    <loc>${baseUrl}/manga/${manga.id}</loc>
    <lastmod>${lastmod}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.85</priority>
  </url>\n`;
      (manga.author || []).forEach(a => { if (a && a.trim()) authorSet.add(a.trim()); });
      (manga.genres || []).forEach(g => { if (g) genreSet.add(g); });
    } catch (e) {}
  }
}
mangaXml += `</urlset>`;
fs.writeFileSync(path.join(publicDir, 'sitemap_manga.xml'), mangaXml, 'utf8');

// ==========================================
// 4. 女優・ジャンル・メーカー・著者用サイトマップ (sitemap_categories.xml)
// ==========================================
const slugsData = JSON.parse(fs.readFileSync(path.join(__dirname, 'src', 'lib', 'slugs.json'), 'utf8'));
const actressSlugMap = slugsData.actresses || {};
const genreSlugMap = slugsData.genres || {};

let catXml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n`;

actressSet.forEach(a => {
  const slug = actressSlugMap[a] || encodeURIComponent(a);
  catXml += `  <url>
    <loc>${baseUrl}/actress/${slug}</loc>
    <lastmod>${nowIso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>\n`;
});

genreSet.forEach(g => {
  const slug = genreSlugMap[g] || encodeURIComponent(g);
  catXml += `  <url>
    <loc>${baseUrl}/genre/${slug}</loc>
    <lastmod>${nowIso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>\n`;
});

makerSet.forEach(m => {
  catXml += `  <url>
    <loc>${baseUrl}/maker/${encodeURIComponent(m)}</loc>
    <lastmod>${nowIso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.80</priority>
  </url>\n`;
});

authorSet.forEach(a => {
  catXml += `  <url>
    <loc>${baseUrl}/author/${encodeURIComponent(a)}</loc>
    <lastmod>${nowIso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.80</priority>
  </url>\n`;
});

catXml += `</urlset>`;
fs.writeFileSync(path.join(publicDir, 'sitemap_categories.xml'), catXml, 'utf8');

// ==========================================
// 5. Sitemap Index (マスターインデックス sitemap.xml & sitemap_index.xml)
// ==========================================
const sitemapIndexXml = `<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>${baseUrl}/sitemap_main.xml</loc>
    <lastmod>${nowIso}</lastmod>
  </sitemap>
  <sitemap>
    <loc>${baseUrl}/sitemap_posts.xml</loc>
    <lastmod>${nowIso}</lastmod>
  </sitemap>
  <sitemap>
    <loc>${baseUrl}/sitemap_manga.xml</loc>
    <lastmod>${nowIso}</lastmod>
  </sitemap>
  <sitemap>
    <loc>${baseUrl}/sitemap_categories.xml</loc>
    <lastmod>${nowIso}</lastmod>
  </sitemap>
</sitemapindex>`;

fs.writeFileSync(path.join(publicDir, 'sitemap.xml'), sitemapIndexXml, 'utf8');
fs.writeFileSync(path.join(publicDir, 'sitemap_index.xml'), sitemapIndexXml, 'utf8');

console.log('✅ Generated public/sitemap.xml (Sitemap Index) and sub-sitemaps:');
console.log(' - public/sitemap_main.xml');
console.log(' - public/sitemap_posts.xml');
console.log(' - public/sitemap_manga.xml');
console.log(' - public/sitemap_categories.xml');
