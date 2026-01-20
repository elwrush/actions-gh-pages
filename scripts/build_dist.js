/**
 * Build Script for Cloudflare Deployment (Multi-Presentation Support)
 * 
 * Builds a clean `dist/` folder containing ALL presentations in `inputs/`
 * and a central dashboard.
 * 
 * Usage:
 *   node scripts/build_dist.js
 */

const fs = require('fs');
const path = require('path');

const PROJECT_ROOT = path.join(__dirname, '..');
const DIST_DIR = path.join(PROJECT_ROOT, 'dist');
const INPUTS_DIR = path.join(PROJECT_ROOT, 'inputs');

// Clean and create dist
console.log('\n🧹 Cleaning dist/ folder...');
if (fs.existsSync(DIST_DIR)) {
    fs.rmSync(DIST_DIR, { recursive: true, force: true });
}
fs.mkdirSync(DIST_DIR);

// Copy shared JS components
const skillsJs = path.join(PROJECT_ROOT, 'skills/creating-html-presentation/js');
if (fs.existsSync(skillsJs)) {
    const destJs = path.join(DIST_DIR, 'skills/creating-html-presentation/js');
    fs.mkdirSync(destJs, { recursive: true });
    fs.cpSync(skillsJs, destJs, { recursive: true });
    console.log('📦 Copied shared JS components.');
}

// Global images
const globalImages = path.join(PROJECT_ROOT, 'images');
if (fs.existsSync(globalImages)) {
    const destImages = path.join(DIST_DIR, 'images');
    fs.cpSync(globalImages, destImages, { recursive: true });
    console.log('📦 Copied global images.');
}

// Find all presentations
const folders = fs.readdirSync(INPUTS_DIR).filter(f => {
    const indexPath = path.join(INPUTS_DIR, f, 'index.html');
    return fs.existsSync(indexPath);
});

console.log(`\n📂 Found ${folders.length} presentations:`);

const presentationData = [];

folders.forEach(f => {
    const srcPath = path.join(INPUTS_DIR, f);
    const destPath = path.join(DIST_DIR, f);

    console.log(`  - Copying ${f}...`);
    fs.cpSync(srcPath, destPath, { recursive: true });

    // Extract title from index.html if possible
    let title = f;
    try {
        const content = fs.readFileSync(path.join(srcPath, 'index.html'), 'utf8');
        const match = content.match(/<title>(.*?)<\/title>/);
        if (match) title = match[1];
    } catch (e) { }

    presentationData.push({
        folder: f,
        title: title,
        date: new Date().toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })
    });
});

// Generate Dashboard index.html
const dashboardHtml = `
<!DOCTYPE html>
<html>
<head>
    <title>Bell Presentations Library</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: #0f172a;
            color: white;
            padding: 50px;
            text-align: center;
        }
        h1 {
            color: #8b1538;
            text-transform: uppercase;
            margin-bottom: 40px;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .card {
            background: #1e293b;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #334155;
            transition: 0.3s;
            text-decoration: none;
            color: white;
            display: block;
            text-align: left;
        }
        .card:hover {
            transform: translateY(-5px);
            border-color: #00f2ff;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
        }
        .date {
            color: #94a3b8;
            font-size: 0.9em;
            margin-bottom: 10px;
            display: block;
        }
        .title {
            font-size: 1.2em;
            font-weight: bold;
            color: #00f2ff;
        }
    </style>
</head>
<body>
    <h1>Bell Presentations Library</h1>
    <div class="grid">
        ${presentationData.map(p => `
        <a href="./${p.folder}/" class="card">
            <span class="date">${p.date}</span>
            <span class="title">${p.title}</span>
        </a>
        `).join('')}
    </div>
</body>
</html>
`;

fs.writeFileSync(path.join(DIST_DIR, 'index.html'), dashboardHtml);
console.log('\n✅ Dashboard generated.');

console.log('\n✅ Build complete!');
console.log(`   Output: dist/`);
console.log('\nNext: Run `npx wrangler pages deploy dist/` to deploy.\n');
