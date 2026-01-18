/**
 * Build Script for Cloudflare Deployment
 * 
 * Builds a clean `dist/` folder containing ONLY the specified presentation
 * and its required assets.
 * 
 * Usage:
 *   node scripts/build_dist.js <folder-name>
 *   node scripts/build_dist.js QAD-Fight-or-Flight
 * 
 * The folder must exist in `inputs/` and contain an `index.html`.
 */

const fs = require('fs');
const path = require('path');

const PROJECT_ROOT = path.join(__dirname, '..');
const DIST_DIR = path.join(PROJECT_ROOT, 'dist');
const INPUTS_DIR = path.join(PROJECT_ROOT, 'inputs');

// Get folder name from CLI
const folderName = process.argv[2];

if (!folderName) {
    console.error('\n❌ ERROR: No folder name provided.');
    console.error('\nUsage: node scripts/build_dist.js <folder-name>');
    console.error('Example: node scripts/build_dist.js QAD-Fight-or-Flight\n');
    console.error('Available folders in inputs/:');

    // List available folders with index.html
    const folders = fs.readdirSync(INPUTS_DIR).filter(f => {
        const indexPath = path.join(INPUTS_DIR, f, 'index.html');
        return fs.existsSync(indexPath);
    });
    folders.forEach(f => console.error(`  - ${f}`));

    process.exit(1);
}

// Validate source folder
const srcPath = path.join(INPUTS_DIR, folderName);
const srcIndex = path.join(srcPath, 'index.html');

if (!fs.existsSync(srcPath)) {
    console.error(`\n❌ ERROR: Folder not found: inputs/${folderName}`);
    process.exit(1);
}

if (!fs.existsSync(srcIndex)) {
    console.error(`\n❌ ERROR: No index.html in inputs/${folderName}`);
    process.exit(1);
}

// Clean and create dist
console.log('\n🧹 Cleaning dist/ folder...');
if (fs.existsSync(DIST_DIR)) {
    fs.rmSync(DIST_DIR, { recursive: true, force: true });
}
fs.mkdirSync(DIST_DIR);

// Copy presentation to dist root (not a subfolder - for simpler URLs)
console.log(`📦 Copying inputs/${folderName}/ to dist/...`);
fs.cpSync(srcPath, DIST_DIR, { recursive: true });

// Copy shared JS components
const skillsJs = path.join(PROJECT_ROOT, 'skills/creating-html-presentation/js');
if (fs.existsSync(skillsJs)) {
    const destJs = path.join(DIST_DIR, 'skills/creating-html-presentation/js');
    fs.mkdirSync(destJs, { recursive: true });
    fs.cpSync(skillsJs, destJs, { recursive: true });
    console.log('📦 Copied shared JS components.');
}

// Validation: Check for key assets
const requiredFiles = ['index.html'];
const missingFiles = requiredFiles.filter(f => !fs.existsSync(path.join(DIST_DIR, f)));

if (missingFiles.length > 0) {
    console.error(`\n❌ BUILD FAILED: Missing required files: ${missingFiles.join(', ')}`);
    process.exit(1);
}

// Check for images folder (warning only)
if (!fs.existsSync(path.join(DIST_DIR, 'images'))) {
    console.warn('\n⚠️  WARNING: No images/ folder found. Presentation may have missing visuals.');
}

console.log('\n✅ Build complete!');
console.log(`   Output: dist/`);
console.log(`   Source: inputs/${folderName}/`);
console.log('\nNext: Run `npx wrangler pages deploy dist/` to deploy.\n');
