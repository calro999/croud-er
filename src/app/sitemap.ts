import { MetadataRoute } from 'next';
import fs from 'fs';
import path from 'path';

export const dynamic = 'force-static';

interface Post {
  id: string;
  date?: string;
  actresses?: string[];
  genres?: string[];
}

export default function sitemap(): MetadataRoute.Sitemap {
  const baseUrl = 'https://haitoku.pages.dev';

  const routes: MetadataRoute.Sitemap = [
    {
      url: `${baseUrl}`,
      lastModified: new Date(),
      changeFrequency: 'daily',
      priority: 1.0,
    },
    {
      url: `${baseUrl}/ranking`,
      lastModified: new Date(),
      changeFrequency: 'weekly',
      priority: 0.9,
    },
    {
      url: `${baseUrl}/archives`,
      lastModified: new Date(),
      changeFrequency: 'daily',
      priority: 0.8,
    },
    {
      url: `${baseUrl}/genre/lesbian`,
      lastModified: new Date(),
      changeFrequency: 'daily',
      priority: 0.9,
    },
    {
      url: `${baseUrl}/manga`,
      lastModified: new Date(),
      changeFrequency: 'daily',
      priority: 0.9,
    },
  ];

  let posts: Post[] = [];

  try {
    const postsDir = path.join(process.cwd(), 'src', 'data', 'posts');
    if (fs.existsSync(postsDir)) {
      const files = fs.readdirSync(postsDir).filter(f => f.endsWith('.json'));
      posts = files.map(file => {
        try {
          const content = fs.readFileSync(path.join(postsDir, file), 'utf-8');
          return JSON.parse(content) as Post;
        } catch {
          return null;
        }
      }).filter(Boolean) as Post[];
    }
  } catch (error) {
    console.error('Error reading posts for sitemap:', error);
  }

  // 記事ページ（新着 = 高priority）
  const now = Date.now();
  posts.forEach((post) => {
    if (!post?.id) return;
    const postDate = post.date ? new Date(post.date).getTime() : 0;
    const ageInDays = (now - postDate) / (1000 * 60 * 60 * 24);
    // 30日以内: 0.9、90日以内: 0.8、180日以内: 0.7、それ以降: 0.6
    const priority = ageInDays < 30 ? 0.9 : ageInDays < 90 ? 0.8 : ageInDays < 180 ? 0.7 : 0.6;

    routes.push({
      url: `${baseUrl}/posts/${post.id}`,
      lastModified: post.date ? new Date(post.date) : new Date(),
      changeFrequency: 'monthly',
      priority,
    });
  });

  // 女優別ページ（重複除去）
  const actresses = Array.from(new Set(posts.flatMap(p => p.actresses || [])));
  actresses.forEach((actress) => {
    if (!actress) return;
    routes.push({
      url: `${baseUrl}/actress/${encodeURIComponent(actress)}`,
      lastModified: new Date(),
      changeFrequency: 'weekly',
      priority: 0.85,
    });
  });

  // ジャンル別ページ（重複除去）
  const genres = Array.from(new Set(posts.flatMap(p => p.genres || [])));
  genres.forEach((genre) => {
    if (!genre) return;
    routes.push({
      url: `${baseUrl}/genre/${encodeURIComponent(genre)}`,
      lastModified: new Date(),
      changeFrequency: 'weekly',
      priority: 0.85,
    });
  });

  // 漫画ページ
  const mangaDir = path.join(process.cwd(), 'src', 'data', 'manga');
  if (fs.existsSync(mangaDir)) {
    const mangaFiles = fs.readdirSync(mangaDir).filter(f => f.endsWith('.json'));
    mangaFiles.forEach(file => {
      try {
        const manga = JSON.parse(fs.readFileSync(path.join(mangaDir, file), 'utf-8'));
        if (!manga?.id) return;
        routes.push({
          url: `${baseUrl}/manga/${manga.id}`,
          lastModified: manga.date ? new Date(manga.date) : new Date(),
          changeFrequency: 'monthly',
          priority: 0.85,
        });
      } catch {}
    });
  }

  return routes;
}
