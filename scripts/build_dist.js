/**
 * Build Script for GitHub Pages Deployment (Multi-Presentation Support)
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
    
    // SAFETY: Never clean the project root!
    if (dir === PROJECT_ROOT) {
        console.error("❌ SAFETY VIOLATION: Attempted to clean PROJECT_ROOT. Aborting.");
        process.exit(1);
    }

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

// Ensure inputs exists
if (!fs.existsSync(INPUTS_DIR)) {
    console.error('❌ inputs/ directory not found.');
    process.exit(1);
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

console.log(`\n📂 Processing ${folders.length} presentation(s):`);

folders.forEach(folder => {
    const publishedPath = path.join(INPUTS_DIR, folder, 'published');
    const rootPath = path.join(INPUTS_DIR, folder);
    
    // Source priority: published/ folder, then root
    const sourceDir = fs.existsSync(path.join(publishedPath, 'index.html')) ? publishedPath : rootPath;
    const destDir = path.join(DIST_DIR, folder);

    console.log(`  - Copying ${folder} (from ${path.relative(INPUTS_DIR, sourceDir)}/)...`);
    
    if (!fs.existsSync(destDir)) {
        fs.mkdirSync(destDir, { recursive: true });
    }

    // Copy contents
    fs.cpSync(sourceDir, destDir, {
        recursive: true,
        filter: (src) => {
            const name = path.basename(src);
            // Skip system files and source materials
            return !name.startsWith('.') && 
                   name.toLowerCase() !== 'desktop.ini' &&
                   !name.endsWith('.typ') &&
                   !name.endsWith('.pdf') &&
                   name !== 'presentation.json' &&
                   name !== 'slide_architecture.md' &&
                   name !== 'quizzes' &&
                   name !== 'audio'; // Audio is shared at root for efficiency
        }
    });
});

// Generate Dashboard (index.html in dist/)
const dashboardPath = path.join(DIST_DIR, 'index.html');
const presentationCards = folders.map(f => {
    // Attempt to extract title and date from folder name or metadata
    const nameParts = f.split('-');
    let dateStr = "Unknown Date";
    let titleStr = f;

    if (nameParts.length >= 3 && /^\d+$/.test(nameParts[0])) {
        dateStr = `${nameParts[0]} ${getMonthName(nameParts[1])} ${nameParts[2]}`;
        titleStr = nameParts.slice(3).join(' ').replace(/-/g, ' ');
    }

    return `
        <a href="./${f}/" class="card">
            <span class="date">${dateStr}</span>
            <span class="title">${titleStr}</span>
        </a>
    `;
}).join('\n');

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
        ${presentationCards}
    </div>
</body>
</html>
`;

fs.writeFileSync(dashboardPath, dashboardHtml);
console.log('\n✅ Dashboard generated.');

console.log('\n✅ Build complete!');
console.log(`   Output: ${path.relative(PROJECT_ROOT, DIST_DIR)}/`);
console.log('\nNext: Push to GitHub to deploy to GitHub Pages.');

function getMonthName(num) {
    const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    const i = parseInt(num) - 1;
    return (i >= 0 && i < 12) ? months[i] : num;
}