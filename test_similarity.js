const fs = require('fs');
const path = require('path');

const mangaJsonPath = path.join(__dirname, 'public', 'data', 'manga.json');
const allManga = JSON.parse(fs.readFileSync(mangaJsonPath, 'utf-8'));

function getSimilarManga(currentManga, limit = 4) {
  const currentAuthors = (currentManga.author || []).map(a => a.trim()).filter(Boolean);
  const currentGenres = currentManga.genres || [];
  const scored = [];

  for (const m of allManga) {
    if (m.id === currentManga.id) continue;
    let score = 0;
    let matchReason = "";
    const seed = (currentManga.id + m.id).split("").reduce((acc, char) => acc + char.charCodeAt(0), 0);

    if (currentAuthors.length > 0 && m.author) {
      const commonAuthor = currentAuthors.filter(a => m.author.includes(a));
      if (commonAuthor.length > 0) {
        score += 20;
        matchReason = `✍️ ${commonAuthor[0]}先生の他作品`;
      }
    }

    if (currentGenres.length > 0 && m.genres) {
      const commonGenres = currentGenres.filter(g => m.genres.includes(g));
      if (commonGenres.length > 0) {
        score += commonGenres.length * 4;
        if (!matchReason) {
          matchReason = `同ジャンル「${commonGenres[0]}」`;
        }
      }
    }

    if (score > 0) {
      scored.push({ manga: m, score, matchReason });
    }
  }

  scored.sort((a, b) => b.score - a.score);
  return scored.slice(0, limit);
}

// 最初の5作品についてレコメンド結果をテスト
for (let i = 0; i < 5; i++) {
  const m = allManga[i];
  console.log(`\n=== [${m.id}] ${m.title} (Genres: ${m.genres?.slice(0,3).join(',')}) ===`);
  const similar = getSimilarManga(m, 4);
  similar.forEach(s => {
    console.log(`   -> [Score ${s.score}] ${s.manga.title} (${s.matchReason})`);
  });
}
