const fs = require('fs');
const path = require('path');
const fsPromises = fs.promises;

async function copyDir(src, dest, filter = () => true) {
    await fsPromises.mkdir(dest, { recursive: true });
    const entries = await fsPromises.readdir(src, { withFileTypes: true });

    for (let entry of entries) {
        const srcPath = path.join(src, entry.name);
        const destPath = path.join(dest, entry.name);

        if (!filter(srcPath)) continue;

        if (entry.isDirectory()) {
            await copyDir(srcPath, destPath, filter);
        } else {
            await fsPromises.copyFile(srcPath, destPath);
        }
    }
}

async function emptyDir(dir) {
    if (!fs.existsSync(dir)) return;
    const entries = await fsPromises.readdir(dir, { withFileTypes: true });
    for (let entry of entries) {
        const fullPath = path.join(dir, entry.name);
        if (entry.isDirectory()) {
            await fsPromises.rm(fullPath, { recursive: true, force: true });
        } else {
            await fsPromises.unlink(fullPath);
        }
    }
}

async function build() {
    const projectRoot = process.cwd();
    const distRoot = path.join(projectRoot, 'dist');
    const tempRepo = path.join(projectRoot, 'temp_reveal_repo');
    const inputsDir = path.join(projectRoot, 'inputs');

    console.log('🚀 Starting build process...');

    // 1. Clean dist directory
    try {
        if (fs.existsSync(distRoot)) {
            await emptyDir(distRoot);
            console.log('🧹 Cleaned dist directory.');
        } else {
            await fsPromises.mkdir(distRoot, { recursive: true });
        }
    } catch (err) {
        console.error('❌ Error cleaning dist:', err);
    }

    // 2. Copy Shared Reveal.js Engine
    console.log('📦 Copying shared Reveal.js engine...');
    const engineFolders = ['dist', 'plugin', 'css'];
    for (const folder of engineFolders) {
        const src = path.join(tempRepo, folder);
        const dest = path.join(distRoot, folder);
        if (fs.existsSync(src)) {
            await copyDir(src, dest, (srcPath) => !srcPath.includes('desktop.ini') && !srcPath.includes('.git'));
            console.log(`   ✅ Copied ${folder}/`);
        } else {
            console.warn(`   ⚠️  Warning: ${folder} not found in ${tempRepo}`);
        }
    }

    // 3. Aggregate Presentations
    console.log('📂 Aggregating presentations from inputs/...');
    const lessons = [];
    const folders = await fsPromises.readdir(inputsDir);

    for (const folder of folders) {
        const lessonPath = path.join(inputsDir, folder);
        const stat = await fsPromises.stat(lessonPath);
        if (!stat.isDirectory()) continue;

        let presentationSrc = path.join(lessonPath, 'published');
        if (!fs.existsSync(path.join(presentationSrc, 'index.html'))) {
            presentationSrc = lessonPath;
        }

        const indexHtml = path.join(presentationSrc, 'index.html');
        if (fs.existsSync(indexHtml)) {
            console.log(`   ✨ Processing lesson: ${folder}`);
            const destLessonDir = path.join(distRoot, folder);
            await fsPromises.mkdir(destLessonDir, { recursive: true });

            let content = await fsPromises.readFile(indexHtml, 'utf-8');

            // --- PATH FIXING LOGIC ---
            // Ensure assets reference the shared root engine at ../dist/ and ../plugin/
            // Match href="dist/ or src="dist/ or href='dist/ or src='dist/
            content = content.replace(/(href|src)=["']dist\//g, '$1="../dist/');
            content = content.replace(/(href|src)=["']plugin\//g, '$1="../plugin/');
            
            // Also handle any absolute-style paths that might have been accidentally used
            // e.g. /dist/ or /plugin/ should also point to ../
            content = content.replace(/(href|src)=["']\/dist\//g, '$1="../dist/');
            content = content.replace(/(href|src)=["']\/plugin\//g, '$1="../plugin/');

            await fsPromises.writeFile(path.join(destLessonDir, 'index.html'), content);

            for (const assetFolder of ['images', 'audio']) {
                const srcAsset = path.join(presentationSrc, assetFolder);
                const destAsset = path.join(destLessonDir, assetFolder);
                if (fs.existsSync(srcAsset)) {
                    await copyDir(srcAsset, destAsset, (srcPath) => !srcPath.includes('desktop.ini'));
                }
            }

            const titleMatch = content.match(/<title>(.*?)<\/title>/);
            const title = titleMatch ? titleMatch[1] : folder;

            lessons.push({
                folder: folder,
                title: title
            });
        }
    }

    // 4. Generate Dashboard
    console.log('📊 Generating dashboard...');
    const dashboardHtml = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bell Language Centre | Presentations Library</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #1a1a1a; color: white; padding: 40px; }
        h1 { color: #8B1538; border-bottom: 2pt solid #8B1538; padding-bottom: 10px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; margin-top: 30px; }
        .card { background: #2a2a2a; border-radius: 8px; padding: 20px; transition: transform 0.2s; border: 1px solid #444; text-decoration: none; color: white; display: block; }
        .card:hover { transform: translateY(-5px); border-color: #8B1538; }
        .card h3 { margin-top: 0; color: #FFD700; }
        .card p { font-size: 0.9em; color: #ccc; }
    </style>
</head>
<body>
    <h1>📚 Presentations Library</h1>
    <div class="grid">
        ${lessons.map(l => `
            <a href="${l.folder}/" class="card">
                <h3>${l.title}</h3>
                <p>${l.folder}</p>
            </a>
        `).join('')}
    </div>
</body>
</html>
    `;
    await fsPromises.writeFile(path.join(distRoot, 'index.html'), dashboardHtml);

    console.log('🏁 Build complete! Ready for deployment.');
}

build().catch(err => {
    console.error('💥 Build failed:', err);
    process.exit(1);
});
