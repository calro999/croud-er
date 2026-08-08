import slugsData from "./slugs.json";

const actressToSlugMap: Record<string, string> = slugsData.actresses || {};
const genreToSlugMap: Record<string, string> = slugsData.genres || {};

// 逆引き用（スラッグ -> 元の日本語名）
const slugToActressMap: Record<string, string> = {};
Object.entries(actressToSlugMap).forEach(([name, slug]) => {
  if (!slugToActressMap[slug]) {
    slugToActressMap[slug] = name;
  }
});

const slugToGenreMap: Record<string, string> = {};
Object.entries(genreToSlugMap).forEach(([name, slug]) => {
  if (!slugToGenreMap[slug]) {
    slugToGenreMap[slug] = name;
  }
});

export function getActressSlug(name: string): string {
  return actressToSlugMap[name] || encodeURIComponent(name);
}

export function getActressNameBySlug(slug: string): string {
  return slugToActressMap[slug] || decodeURIComponent(slug);
}

export function getGenreSlug(genre: string): string {
  return genreToSlugMap[genre] || encodeURIComponent(genre);
}

export function getGenreNameBySlug(slug: string): string {
  return slugToGenreMap[slug] || decodeURIComponent(slug);
}
