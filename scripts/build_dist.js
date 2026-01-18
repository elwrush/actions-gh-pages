const fs = require('fs');
const path = require('path');

const PROJECT_ROOT = path.join(__dirname, '..');
const DIST_DIR = path.join(PROJECT_ROOT, 'dist');

// Define which presentations to include in the build
const presentations = [
    { source: 'slideshow-fight-or-flight', target: '18-01-26_Fight-or-Flight' }
];

// Ensure dist exists and is clean
if (fs.existsSync(DIST_DIR)) {
    fs.rmSync(DIST_DIR, { recursive: true, force: true });
}
fs.mkdirSync(DIST_DIR);

presentations.forEach(pres => {
    const srcPath = path.join(PROJECT_ROOT, pres.source);
    const destPath = path.join(DIST_DIR, pres.target);

    if (fs.existsSync(srcPath)) {
        console.log(`Building ${pres.source} to dist/${pres.target}...`);
        fs.mkdirSync(destPath, { recursive: true });
        fs.cpSync(srcPath, destPath, { recursive: true });

        // Also ensure images/brain_alarm.png specifically exists there
        if (fs.existsSync(path.join(destPath, 'images/brain_alarm.png'))) {
            console.log("Success: brain_alarm.png found in dist destination.");
        } else {
            console.error("CRITICAL ERROR: brain_alarm.png NOT FOUND in dist destination!");
            process.exit(1);
        }
    } else {
        console.error(`Error: Source directory not found: ${srcPath}`);
        process.exit(1);
    }
});

console.log('Build complete.');
