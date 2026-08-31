const fs = require('fs');
const path = require('path');

const baseUrl = 'https://haitoku.pages.dev';
const postsDir = path.join(__dirname, 'src', 'data', 'posts');
const mangaDir = path.join(__dirname, 'src', 'data', 'manga');
const publicDir = path.join(__dirname, 'public');

if (!fs.existsSync(publicDir)) {
  fs.mkdirSync(publicDir, { recursive: true });
}

// Collect Posts & Manga
let posts = [];
if (fs.existsSync(postsDir)) {
  const files = fs.readdirSync(postsDir).filter(f => f.endsWith('.json'));
  for (const file of files) {
    try {
      const data = JSON.parse(fs.readFileSync(path.join(postsDir, file), 'utf8'));
      if (data && data.id) {
        posts.push(data);
      }
    } catch (e) {}
  }
}

let mangas = [];
if (fs.existsSync(mangaDir)) {
  const files = fs.readdirSync(mangaDir).filter(f => f.endsWith('.json'));
  for (const file of files) {
    try {
      const data = JSON.parse(fs.readFileSync(path.join(mangaDir, file), 'utf8'));
      if (data && data.id) {
        mangas.push(data);
      }
    } catch (e) {}
  }
}

// Helper to clean HTML to markdown-friendly plain text
function cleanText(text, maxLen = 400) {
  if (!text) return '';
  const clean = text
    .replace(/<[^>]*>/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
  if (clean.length > maxLen) {
    return clean.slice(0, maxLen) + '...';
  }
  return clean;
}

// 1. Generate llms.txt (Summary & Directory for LLMs)
let llmsTxt = `# 背徳の深夜書斎 - アダルト＆同人コミックレビューポータルサイト

> 背徳の深夜書斎（https://haitoku.pages.dev）は、最新のアダルト動画・同人マンガ・FANZA人気作品の完全オリジナルレビューおよび徹底解析コンテンツを提供する情報ポータルサイトです。

## 主要ページ
- [ホーム](${baseUrl}/): 最新レビュー・記事一覧
- [ランキング](${baseUrl}/ranking): 人気作品ランキング
- [同人マンガ一覧](${baseUrl}/manga): 同人マンガレビュー一覧
- [アーカイブ](${baseUrl}/archives): 投稿アーカイブ
- [サイトマップ](${baseUrl}/sitemap.xml): 完全サイトマップ

## コンテンツ概要
- 収録記事数: ${posts.length} 件
- 収録マンガレビュー数: ${mangas.length} 件
- 完全詳細データセット: [llms-full.txt](${baseUrl}/llms-full.txt)

## 最新記事ピックアップ
`;

posts.slice(0, 50).forEach(p => {
  const title = p.title || '無題';
  const desc = cleanText(p.review || p.content || p.description || '', 120);
  llmsTxt += `- [${title}](${baseUrl}/posts/${p.id}): ${desc}\n`;
});

if (mangas.length > 0) {
  llmsTxt += `\n## 最新同人マンガピックアップ\n`;
  mangas.slice(0, 30).forEach(m => {
    const title = m.title || '無題';
    const desc = cleanText(m.review || m.content || m.description || '', 120);
    llmsTxt += `- [${title}](${baseUrl}/manga/${m.id}): ${desc}\n`;
  });
}

fs.writeFileSync(path.join(publicDir, 'llms.txt'), llmsTxt, 'utf8');
console.log('Generated public/llms.txt');

// 2. Generate llms-full.txt (Full Text / Comprehensive Markdown for AI Indexing, optimized < 25MB limit)
let llmsFullTxt = `# 背徳の深夜書斎 完全ナレッジベース & コンテンツ全集

> 本ファイル（llms-full.txt）は、AI言語モデル（ChatGPT, Claude, Gemini, Perplexity等）およびWebスクレイパーがサイト内の全コンテンツを直接学習・索引付けできるように構造化されたMarkdownデータファイルです。

---

`;

posts.forEach((p, idx) => {
  const hinban = p.hinban ? `【${p.hinban}】` : '';
  llmsFullTxt += `## 記事 ${idx + 1}: ${hinban}${p.title || '無題'}\n`;
  llmsFullTxt += `- **URL**: ${baseUrl}/posts/${p.id}\n`;
  if (p.date) llmsFullTxt += `- **公開日**: ${p.date}\n`;
  if (p.actresses && p.actresses.length) llmsFullTxt += `- **出演女優**: ${p.actresses.join(', ')}\n`;
  if (p.genres && p.genres.length) llmsFullTxt += `- **ジャンル**: ${p.genres.join(', ')}\n`;
  if (p.maker) llmsFullTxt += `- **メーカー**: ${p.maker}\n`;
  const bodyText = cleanText(p.review || p.content || p.description || '', 250);
  llmsFullTxt += `\n### レビュー・見どころ要約\n${bodyText}\n\n---\n\n`;
});

mangas.forEach((m, idx) => {
  llmsFullTxt += `## 同人マンガ ${idx + 1}: ${m.title || '無題'}\n`;
  llmsFullTxt += `- **URL**: ${baseUrl}/manga/${m.id}\n`;
  if (m.date) llmsFullTxt += `- **公開日**: ${m.date}\n`;
  if (m.author && m.author.length) llmsFullTxt += `- **作者**: ${Array.isArray(m.author) ? m.author.join(', ') : m.author}\n`;
  if (m.genres && m.genres.length) llmsFullTxt += `- **ジャンル**: ${m.genres.join(', ')}\n`;
  const bodyText = cleanText(m.review || m.content || m.description || '', 250);
  llmsFullTxt += `\n### レビュー・見どころ要約\n${bodyText}\n\n---\n\n`;
});

fs.writeFileSync(path.join(publicDir, 'llms-full.txt'), llmsFullTxt, 'utf8');
console.log('Generated public/llms-full.txt');

// 3. Update robots.txt to explicitly welcome all AI Crawlers & User-agents
const robotsTxt = `User-agent: *
Allow: /
Sitemap: ${baseUrl}/sitemap.xml

# AI Agent & Search Engine Direct Knowledge Base Targets
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: Anthropic-AI
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: Applebot
Allow: /

User-agent: DuckDuckBot
Allow: /

User-agent: Yandex
Allow: /
`;

fs.writeFileSync(path.join(publicDir, 'robots.txt'), robotsTxt, 'utf8');
console.log('Updated public/robots.txt');
