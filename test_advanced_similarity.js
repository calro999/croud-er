const fs = require('fs');
const path = require('path');

const mangaJsonPath = path.join(__dirname, 'public', 'data', 'manga.json');
const allManga = JSON.parse(fs.readFileSync(mangaJsonPath, 'utf-8'));

// ジャンルの希少性マップ
const genreFreq = {};
allManga.forEach(m => {
  (m.genres || []).forEach(g => {
    genreFreq[g] = (genreFreq[g] || 0) + 1;
  });
});

const genericGenres = new Set(["無料作品", "単行本", "単話", "フルカラー", "EROTOON", "独占販売", "先行販売"]);

function getSimilarMangaAdvanced(currentManga, limit = 4) {
  const currentAuthors = (currentManga.author || []).map(a => a.trim()).filter(Boolean);
  const currentGenres = (currentManga.genres || []).filter(g => !genericGenres.has(g));
  const scored = [];

  for (const m of allManga) {
    if (m.id === currentManga.id) continue;
    let score = 0;
    const reasons = [];

    // 1. 同一作者 (最優先 +50点)
    if (currentAuthors.length > 0 && m.author) {
      const commonAuthor = currentAuthors.filter(a => m.author.includes(a));
      if (commonAuthor.length > 0) {
        score += 50;
        reasons.push({ priority: 1, text: `✍️ ${commonAuthor[0]}先生が描くもう一つの傑作！` });
      }
    }

    // 2. 特徴的ジャンルのマッチング（IDFスコア加点）
    if (currentGenres.length > 0 && m.genres) {
      const mGenres = (m.genres || []).filter(g => !genericGenres.has(g));
      const commonGenres = currentGenres.filter(g => mGenres.includes(g));
      
      for (const g of commonGenres) {
        const freq = genreFreq[g] || 1;
        // 出現数が少ない（希少・ニッチ）なジャンルほど超高得点 (例: 頻度5なら +25点, 頻度50なら +5点)
        const idfScore = Math.max(3, Math.round(100 / (Math.sqrt(freq) + 2)));
        score += idfScore;
        reasons.push({ priority: 2, idf: idfScore, text: `💥 『${g}』好き悶絶！快楽に堕ちていく背徳の傑作` });
      }
    }

    // 3. タイトルのキーワード類似度
    const cleanCurrentTitle = currentManga.title.replace(/[【】\[\]（）\(\)\s]/g, "");
    const cleanMTitle = m.title.replace(/[【】\[\]（）\(\)\s]/g, "");
    for (const kw of ["不倫", "人妻", "義母", "百合", "レズ", "NTR", "寝取", "催眠", "調教", "幼なじみ", "女教師", "ギャル"]) {
      if (cleanCurrentTitle.includes(kw) && cleanMTitle.includes(kw)) {
        score += 15;
        reasons.push({ priority: 3, text: `🔥 『${kw}』シチュエーションが最高に刺さる注目作！` });
      }
    }

    if (score > 0) {
      reasons.sort((a, b) => (a.priority - b.priority) || ((b.idf || 0) - (a.idf || 0)));
      scored.push({
        manga: m,
        score,
        matchReason: reasons[0]?.text || "⭐ 読者評価トップクラスの人気漫画！"
      });
    }
  }

  scored.sort((a, b) => b.score - a.score);
  return scored.slice(0, limit);
}

// テスト
for (let i = 0; i < 6; i++) {
  const m = allManga[i];
  console.log(`\n=== [${m.id}] ${m.title} ===`);
  console.log(`Authors: ${m.author.join(',')}, Genres: ${m.genres?.slice(0,5).join(',')}`);
  const similar = getSimilarMangaAdvanced(m, 4);
  similar.forEach(s => {
    console.log(`   -> [Score ${s.score}] ${s.manga.title} (${s.matchReason})`);
  });
}
