const fs = require('fs');
const path = require('path');

const baseUrl = 'https://haitoku.pages.dev';
const postsDir = path.join(__dirname, 'src', 'data', 'posts');
const mangaDir = path.join(__dirname, 'src', 'data', 'manga');

let xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>${baseUrl}</loc>
    <lastmod>${new Date().toISOString()}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>${baseUrl}/fanza-tv-plus</loc>
    <lastmod>${new Date().toISOString()}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>${baseUrl}/fanza-device-guide</loc>
    <lastmod>${new Date().toISOString()}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.98</priority>
  </url>
  <url>
    <loc>${baseUrl}/features</loc>
    <lastmod>${new Date().toISOString()}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.95</priority>
  </url>
  <url>
    <loc>${baseUrl}/ranking</loc>
    <lastmod>${new Date().toISOString()}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>${baseUrl}/archives</loc>
    <lastmod>${new Date().toISOString()}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>${baseUrl}/manga</loc>
    <lastmod>${new Date().toISOString()}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
`;

const actressSet = new Set();
const genreSet = new Set();
const makerSet = new Set();

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
      const lastmod = post.date ? new Date(post.date).toISOString() : new Date().toISOString();
      xml += `  <url>
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

const slugsData = JSON.parse(fs.readFileSync(path.join(__dirname, 'src', 'lib', 'slugs.json'), 'utf8'));
const actressSlugMap = slugsData.actresses || {};
const genreSlugMap = slugsData.genres || {};

actressSet.forEach(a => {
  const slug = actressSlugMap[a] || encodeURIComponent(a);
  xml += `  <url>
    <loc>${baseUrl}/actress/${slug}</loc>
    <lastmod>${new Date().toISOString()}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>\n`;
});

genreSet.forEach(g => {
  const slug = genreSlugMap[g] || encodeURIComponent(g);
  xml += `  <url>
    <loc>${baseUrl}/genre/${slug}</loc>
    <lastmod>${new Date().toISOString()}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>\n`;
});

makerSet.forEach(m => {
  xml += `  <url>
    <loc>${baseUrl}/maker/${encodeURIComponent(m)}</loc>
    <lastmod>${new Date().toISOString()}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>\n`;
});

const authorSet = new Set();

if (fs.existsSync(mangaDir)) {
  const mangaFiles = fs.readdirSync(mangaDir).filter(f => f.endsWith('.json'));
  for (const file of mangaFiles) {
    try {
      const manga = JSON.parse(fs.readFileSync(path.join(mangaDir, file), 'utf8'));
      if (!manga || !manga.id) continue;
      const lastmod = manga.date ? new Date(manga.date).toISOString() : new Date().toISOString();
      xml += `  <url>
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

authorSet.forEach(a => {
  xml += `  <url>
    <loc>${baseUrl}/author/${encodeURIComponent(a)}</loc>
    <lastmod>${new Date().toISOString()}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>\n`;
});

xml += `</urlset>`;

const publicDir = path.join(__dirname, 'public');
if (!fs.existsSync(publicDir)) {
  fs.mkdirSync(publicDir);
}
fs.writeFileSync(path.join(publicDir, 'sitemap.xml'), xml, 'utf8');
console.log('Generated public/sitemap.xml');
