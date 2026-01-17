const fs = require('fs');
const path = require('path');

const PROJECT_ROOT = path.join(__dirname, '..');
const DIST_DIR = path.join(PROJECT_ROOT, 'dist');

// TARGET SPECIFIC PRESENTATION
// In the future, this could be dynamic, but for now we target the active work.
const PRESENTATION_DIR = path.join(PROJECT_ROOT, '18-01-26_Global-Logistics-Relative-Clauses');

// Ensure dist exists
if (fs.existsSync(DIST_DIR)) {
    fs.rmSync(DIST_DIR, { recursive: true, force: true });
}
fs.mkdirSync(DIST_DIR);

console.log(`Building from ${PRESENTATION_DIR} to ${DIST_DIR}...`);

if (fs.existsSync(PRESENTATION_DIR)) {
    // Copy all contents from the presentation folder to dist
    fs.cpSync(PRESENTATION_DIR, DIST_DIR, { recursive: true });
    console.log(`Copied presentation contents successfully.`);
} else {
    console.error(`Error: Presentation directory not found: ${PRESENTATION_DIR}`);
    process.exit(1);
}

console.log('Build complete.');
