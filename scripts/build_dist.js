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
// function to robustly delete folder with retries
function robustClean(dir) {
    if (!fs.existsSync(dir)) return;

    let retries = 5;
    while (retries > 0) {
        try {
            fs.rmSync(dir, { recursive: true, force: true });
            console.log('🧹 Cleaned dist/ folder.');
            return;
        } catch (e) {
            console.warn(`⚠️ EBUSY/Locked file in ${dir}. Retrying in 1s... (${retries} left)`);
            const start = Date.now();
            while (Date.now() - start < 1000) { } // Busy wait
            retries--;
        }
    }
    console.warn(`❌ Could not fully clean ${dir}. Proceeding with overwrite...`);
}

// Targeted build check
const targetFolder = process.argv[2];

// Clean and create dist
if (targetFolder) {
    console.log(`🎯 Targeted build for: ${targetFolder} (Incremental Mode)`);
} else {
    robustClean(DIST_DIR);
    
    // Copy shared JS components
    const skillsJs = path.join(PROJECT_ROOT, 'skills/creating-html-presentation/js');
    if (fs.existsSync(skillsJs)) {
        const destJs = path.join(DIST_DIR, 'skills/creating-html-presentation/js');
        fs.mkdirSync(destJs, { recursive: true });
        fs.cpSync(skillsJs, destJs, {
            recursive: true,
            filter: (src) => !path.basename(src).startsWith('.') && path.basename(src).toLowerCase() !== 'desktop.ini'
        });
        console.log('📦 Copied shared JS components.');
    }

    // Global images
    const globalImages = path.join(PROJECT_ROOT, 'images');
    if (fs.existsSync(globalImages)) {
        const destImages = path.join(DIST_DIR, 'images');
        fs.cpSync(globalImages, destImages, {
            recursive: true,
            filter: (src) => !path.basename(src).startsWith('.') && path.basename(src).toLowerCase() !== 'desktop.ini'
        });
        console.log('📦 Copied global images.');
    }

    // Global Reveal.js Engine (for shared hosting)
    const revealRepo = path.join(PROJECT_ROOT, 'temp_reveal_repo');
    ['dist', 'plugin', 'css'].forEach(folder => {
        const src = path.join(revealRepo, folder);
        const dest = path.join(DIST_DIR, folder);
        if (fs.existsSync(src)) {
            fs.cpSync(src, dest, {
                recursive: true,
                filter: (src) => !path.basename(src).startsWith('.') && path.basename(src).toLowerCase() !== 'desktop.ini'
            });
            console.log(`📦 Copied global Reveal engine: ${folder}`);
        }
    });
}

if (!fs.existsSync(DIST_DIR)) {
    fs.mkdirSync(DIST_DIR);
}


// Find presentations
const folders = fs.readdirSync(INPUTS_DIR).filter(f => {
    if (f.startsWith('.')) return false;

    // If a target folder is specified, only include it
    if (targetFolder && f !== targetFolder) return false;

    const publishedIndex = path.join(INPUTS_DIR, f, 'published/index.html');
    const rootIndex = path.join(INPUTS_DIR, f, 'index.html');
    return fs.existsSync(publishedIndex) || fs.existsSync(rootIndex);
});

if (folders.length === 0) {
    console.error('❌ No matching presentations found.');
    process.exit(1);
}

console.log(`\n📂 Processing ${folders.length} presentation(s):`);

const presentationData = [];

folders.forEach(f => {
    const publishedPath = path.join(INPUTS_DIR, f, 'published');
    const hasPublished = fs.existsSync(path.join(publishedPath, 'index.html'));

    // If published folder exists, use it as source to keep dist/ clean
    const srcPath = hasPublished ? publishedPath : path.join(INPUTS_DIR, f);
    const destPath = path.join(DIST_DIR, f);

    console.log(`  - Copying ${f}${hasPublished ? ' (from published/)' : ''}...`);
    fs.cpSync(srcPath, destPath, {
        recursive: true,
        filter: (src) => {
            const base = path.basename(src).toLowerCase();
            if (base.endsWith('.pdf')) return false; // GLOBAL PDF BAN

            const isGit = src.includes('.git');
            const isHidden = base.startsWith('.');
            const isLegacy = src.includes('reveal_presentation');
            const isSystem = base === 'desktop.ini';
            // Exclude Reveal engine folders if we are in a subfolder to use the global ones
            const isEngine = ['dist', 'plugin', 'css'].includes(base);
            // also exclude source artifacts like .typ and .json and .txt
            const isSource = base.endsWith('.typ') || base.endsWith('.json') || base.endsWith('.txt');
            return !isGit && !isHidden && !isLegacy && !isSystem && !isEngine && (!hasPublished || !isSource);
        }
    });

    // Update index.html to point to global Reveal engine (../dist etc)
    const indexPath = path.join(destPath, 'index.html');
    if (fs.existsSync(indexPath)) {
        let content = fs.readFileSync(indexPath, 'utf8');
        content = content.replace(/href="dist\//g, 'href="../dist/');
        content = content.replace(/src="dist\//g, 'src="../dist/');
        content = content.replace(/href="css\//g, 'href="../css/');
        content = content.replace(/src="plugin\//g, 'src="../plugin/');
        fs.writeFileSync(indexPath, content);
    }

    // Extract title from index.html if possible
    let title = f;
    try {
        const indexToRead = path.join(srcPath, 'index.html');
        const content = fs.readFileSync(indexToRead, 'utf8');
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
console.log('\nNext: Push to GitHub to deploy to GitHub Pages.\n');
