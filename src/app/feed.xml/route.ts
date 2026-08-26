import { NextResponse } from 'next/server';
import { getAllSummaryPosts } from '@/lib/posts';

export const dynamic = 'force-static';

export async function GET() {
  const baseUrl = 'https://haitoku.pages.dev';
  const posts = getAllSummaryPosts();

  const items = posts.slice(0, 50).map(post => `
    <item>
      <title><![CDATA[${post.title}]]></title>
      <link>${baseUrl}/posts/${post.id}</link>
      <guid>${baseUrl}/posts/${post.id}</guid>
      <pubDate>${new Date(post.date || Date.now()).toUTCString()}</pubDate>
      <description><![CDATA[${(post.review || '').replace(/<[^>]*>/g, '').slice(0, 200)}...]]></description>
    </item>`).join('\n');

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>背徳の深夜書斎</title>
    <link>https://haitoku.pages.dev</link>
    <description>AV・アダルト動画・漫画レビューまとめ</description>
    <language>ja</language>
    <atom:link href="https://haitoku.pages.dev/feed.xml" rel="self" type="application/rss+xml" />
    ${items}
  </channel>
</rss>`;

  return new NextResponse(xml, {
    headers: {
      'Content-Type': 'application/xml; charset=utf-8',
      'Cache-Control': 's-maxage=3600, stale-while-revalidate',
    },
  });
}
