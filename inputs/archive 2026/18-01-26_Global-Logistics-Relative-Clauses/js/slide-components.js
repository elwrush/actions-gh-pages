/**
 * Modular Slide Card System for Reveal.js
 * Enforces strict layout boundaries to prevent content overflow ("explosions").
 * 
 * Usage:
 * <slide-segue title="Phase 1" subtitle="The Beginning"></slide-segue>
 * <slide-task title="Task 1" timer="5">Instructions...</slide-task>
 */

// Global Sound Effects (Singleton)
const AudioFX = {
    blip: new Audio('audio/blip.mp3'),       // Seconds tick
    bell: new Audio('audio/bell.mp3'),       // Timer end
    warning: new Audio('audio/30-seconds.mp3'), // 30-second warning
    init: function () {
        this.blip.load();
        this.bell.load();
        this.warning.load();
    }
};


// Initialize Audio on user interaction (first click)
document.addEventListener('click', () => AudioFX.init(), { once: true });

// Shared Styles Registry - GOLD STANDARD LAYOUT PATTERNS
const COMPONENT_STYLES = `
    /* ============================================
       CUSTOM ELEMENT DISPLAY FIX
       ============================================ */
    slide-segue, slide-task, slide-answer, slide-split, slide-media {
        display: block;
        width: 100%;
    }

    .slide-canvas {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    /* ============================================
       THEME TOKENS (Override in presentation CSS)
       ============================================ */
    :root {
        /* Colors - Cyber-Gamer Palette (Override per-project in PALETTES.md) */
        --primary: #00F2FF;      /* Cyan */
        --secondary: #ff0055;    /* Maroon/Pink (for shadows) */
        --bg-dark: #050811;      /* Deep navy */
        --glass: rgba(10, 10, 20, 0.95);
        --text-primary: white;
        --text-accent: #FFD700;  /* Gold */
        
        /* Layout Constants - DO NOT CHANGE */
        --container-width: 900px;
        --gap: 40px;
        --box-padding: 25px;
        --box-padding: 25px;
        --border-width: 2px;
        
        /* Functional Colors */
        --danger: #ef4444;
    }

    /* ============================================
       TYPOGRAPHY (Gold Standard Sizes)
       ============================================ */
    .reveal h1, .reveal h2, .reveal h3 {
        text-transform: uppercase;
        font-weight: 800;
        margin: 0 0 20px 0;
    }
    
    .reveal h2 { 
        color: white !important; /* RULE: Headers must contrast with slide background */
        font-size: 1.6em !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.9), 0 0 10px rgba(0, 0, 0, 0.5);
    }
    .reveal h3 { 
        color: var(--text-accent); 
        font-size: 1.2em !important; /* Prevent overflow */
    }

    /* Body text: Readable sizes for classroom projection */
    .text-lg { font-size: 32px !important; }
    .text-md { font-size: 28px !important; }
    .text-sm { font-size: 24px !important; }
    .text-xs { font-size: 22px !important; }

    /* ============================================
       LAYOUT SYSTEM (Gold Standard)
       ============================================ */
    
    /* Slide Canvas - Simple centering wrapper */
    .slide-canvas {
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    /* Row Container - THE key layout primitive */
    .row-container {
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap; /* CRITICAL: Do not wrap for title slides */
        justify-content: center;
        align-items: center;
        gap: var(--gap);
        width: var(--container-width);
        max-width: 100%;
    }

    /* Column System - Explicit flex basis */
    .col-40 { flex: 0 0 40%; max-width: 40%; }
    .col-50 { flex: 0 0 50%; max-width: 50%; }
    .col-60 { flex: 0 0 60%; max-width: 60%; }

    /* ============================================
       COMPONENTS (Gold Standard Patterns)
       ============================================ */
    
    /* Glass Box - Content container */
    .glass-box {
        background: var(--glass);
        border: var(--border-width) solid var(--primary);
        padding: var(--box-padding);
        box-shadow: 6px 6px 0px rgba(0, 0, 0, 0.3);
        text-align: left;
    }
    
    /* Centered box variant */
    .glass-box.centered {
        width: 800px;
        margin: 0 auto;
        text-align: center;
    }

    /* Stage Badge - Skewed cyber pill */
    .stage-badge {
        background: var(--primary);
        color: black;
        padding: 5px 15px;
        font-weight: 800;
        transform: skew(-10deg);
        display: inline-block;
        margin-bottom: 20px;
        font-size: 0.6em;
    }

    /* Header Strap - Position indicator */
    .header-strap {
        position: absolute;
        top: 20px;
        left: 20px;
        background: rgba(5, 8, 17, 0.9);
        border: 1px solid var(--primary);
        border-radius: 50px;
        padding: 8px 25px;
        font-family: 'Courier Prime', monospace;
        font-weight: 700;
        letter-spacing: 2px;
        font-size: 14px;
        color: var(--primary);
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.5);
        z-index: 10;
    }

    /* Teacher Tip */
    .teacher-tip {
        border: 2px dashed var(--secondary);
        background: black;
        padding: 15px;
        margin-top: 15px;
        font-size: 0.7em;
        color: white;
    }

    /* ============================================
       MEDIA HANDLING (Safe Constraints)
       ============================================ */
    .constrained-media {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 0 auto;
    }

    .inset-media {
        max-height: 400px;
        max-width: 100%;
        border: 3px solid var(--primary);
        box-shadow: 0 0 30px rgba(0, 0, 0, 0.5);
    }

    /* 16:9 Video Container */
    .video-wrapper {
        position: relative;
        padding-bottom: 56.25%;
        height: 0;
        overflow: hidden;
        border: 2px solid var(--primary);
    }
    .video-wrapper iframe {
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
    }

    /* ============================================
       TITLE SLIDE (Gold Standard Style)
       ============================================ */
    .title-main-header {
        font-size: 80px !important;
        color: white !important;
        text-shadow: 6px 6px 0px var(--secondary);
        line-height: 1;
        margin-bottom: 30px !important;
        text-align: left;
    }
    .title-subtitle {
        margin: 0 !important;
        text-align: left;
    }
    .title-subtitle span {
        background: var(--secondary);
        color: white;
        padding: 5px 20px;
        font-weight: 800;
        transform: skew(-10deg);
        display: inline-block;
        font-size: 1.1em;
    }
    .title-logo-top {
        position: absolute;
        top: 30px;
        left: 30px;
        height: 80px;
        z-index: 10;
    }

    /* ============================================
       SEGUE TITLE (Gold Standard Style)
       ============================================ */
    .segue-title {
        line-height: 1.1;
        color: var(--text-accent);
        text-transform: uppercase;
        transform: rotate(-3deg) skew(-10deg);
        text-shadow: 6px 6px 0px var(--secondary), 0 0 20px var(--primary);
        margin: 0;
        padding: 20px;
        position: relative;
        z-index: 2;
    }

    /* ============================================
       TIMER (Monospace Display)
       ============================================ */
    .timer-pill {
        display: flex;
        align-items: center;
        gap: 15px;
        background: rgba(0, 0, 0, 0.5);
        border: 1px solid var(--primary);
        padding: 10px 20px;
        margin-top: 20px;
    }
    .timer-display {
        font-family: 'Courier Prime', monospace;
        font-size: 2em;
        color: white;
        min-width: 100px;
        text-align: center;
    }
    .start-btn {
        background: var(--primary);
        color: black;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        cursor: pointer;
    }
    .start-btn.pause { background: var(--secondary); color: white; }
    .start-btn:disabled { opacity: 0.5; cursor: not-allowed; }

    /* ============================================
       UTILITY CLASSES
       ============================================ */
    .highlight { color: var(--text-accent); font-weight: 800; }
    .mt-20 { margin-top: 20px; }
    .mt-40 { margin-top: 40px; }
    .text-center { text-align: center; }
    .text-left { text-align: left; }
`;

// Inject Styles
const styleSheet = document.createElement("style");
styleSheet.innerText = COMPONENT_STYLES;
document.head.appendChild(styleSheet);


// --- COMPONENTS ---

/**
 * <slide-title title="" badge="" subtitle="">
 * Gold Standard Title Slide: 40% Image (rotated/glow) + 60% Text (Badge, Title, Subtitle).
 */
class SlideTitle extends HTMLElement {
    connectedCallback() {
        requestAnimationFrame(() => {
            const title = this.getAttribute('title') || 'TITLE';
            const badge = this.getAttribute('badge') || '';
            const subtitle = this.getAttribute('subtitle') || '';

            // Capture image
            const img = this.querySelector('img');
            const imgHTML = img ? img.outerHTML : '';

            this.innerHTML = `
                <div class="row-container" style="height: 500px;">
                    <div class="col-40" style="display: flex; justify-content: center; align-items: center;">
                        ${imgHTML}
                    </div>
                    <div class="col-60" style="text-align: left; padding-left: 20px;">
                        <div class="stage-badge">${badge}</div>
                        <h1 class="title-main-header">${title}</h1>
                        ${subtitle ? `<p class="title-subtitle"><span>${subtitle}</span></p>` : ''}
                    </div>
                </div>
            `;

            // Style the hero image
            const newImg = this.querySelector('.col-40 img');
            if (newImg) {
                newImg.style.maxHeight = '400px';
                newImg.style.transform = 'rotate(-2deg)';
                newImg.style.border = '3px solid var(--primary)';
                newImg.style.boxShadow = '0 0 30px rgba(0, 0, 0, 0.5)';
                newImg.classList.add('constrained-media');
            }
            if (window.Reveal) Reveal.layout();
        });
    }
}

/**
 * <slide-segue title="">
 * Full screen segue slide with rotated title (Gold Standard Pattern)
 */
class SlideSegue extends HTMLElement {
    connectedCallback() {
        requestAnimationFrame(() => {
            const title = this.getAttribute('title') || 'SEGUE';
            this.innerHTML = `
                <div class="slide-canvas">
                    <h1 class="segue-title" style="font-size: 80px !important; text-shadow: 6px 6px 0px var(--secondary), 0 0 20px var(--primary) !important;">${title}</h1>
                </div>
            `;
            if (window.Reveal) Reveal.layout();
        });
    }
}

/**
 * <slide-task title="" timer="5">
 * Task slide with stage badge, title, and optional timer
 * Gold Standard: Automatically wraps content in a centered glass-box.
 */
class SlideTask extends HTMLElement {
    connectedCallback() {
        requestAnimationFrame(() => this._render());
    }
    _render() {
        const title = this.getAttribute('title') || 'TASK';
        const badge = this.getAttribute('badge') || '';
        const duration = this.getAttribute('timer');
        const content = this.innerHTML;

        this.innerHTML = `
            <div class="slide-canvas">
                ${badge ? `<div class="stage-badge">${badge}</div>` : ''}
                <h2>${title}</h2>
                <div class="glass-box centered">
                    ${content}
                </div>
                ${duration ? `<timer-pill duration="${duration}"></timer-pill>` : ''}
            </div>
        `;
    }
}

/**
 * <slide-answer title="">
 * Answer slide with themed title and auto glass-box
 */
class SlideAnswer extends HTMLElement {
    connectedCallback() {
        requestAnimationFrame(() => this._render());
    }
    _render() {
        const title = this.getAttribute('title') || 'ANSWER';
        const content = this.innerHTML;

        this.innerHTML = `
            <div class="slide-canvas">
                <h2 style="color: var(--primary);">${title}</h2>
                <div class="glass-box centered" style="border-color: var(--primary);">
                    ${content}
                </div>
            </div>
        `;
    }
}

/**
 * <slide-split title="">
 * 2-Column Layout using row-container + col-XX
 * Gold Standard: Image on left, Text in glass-box on right.
 */
class SlideSplit extends HTMLElement {
    connectedCallback() {
        requestAnimationFrame(() => this._render());
    }
    _render() {
        const title = this.getAttribute('title') || '';
        const badge = this.getAttribute('badge') || '';

        // Robust extraction: Clone children, find img, then get remaining
        const container = document.createElement('div');
        container.innerHTML = this.innerHTML;
        const img = container.querySelector('img');
        const imgHTML = img ? img.outerHTML : '';
        if (img) img.remove();
        const contentHTML = container.innerHTML;

        this.innerHTML = `
            <div class="slide-canvas">
                ${badge ? `<div class="stage-badge">${badge}</div>` : ''}
                ${title ? `<h2>${title}</h2>` : ''}
                <div class="row-container" style="align-items: center;">
                    <div class="col-40">
                        ${imgHTML}
                    </div>
                    <div class="col-60 glass-box">
                        ${contentHTML}
                    </div>
                </div>
            </div>
        `;

        // Apply constrained-media class to img
        const newImg = this.querySelector('img');
        if (newImg) {
            newImg.classList.add('constrained-media');
            newImg.style.maxHeight = '450px';
        }
    }
}

/**
 * <slide-media title="" type="video|audio" src="">
 * Media wrapper with proper aspect ratio handling (Gold Standard Pattern)
 */
class SlideMedia extends HTMLElement {
    connectedCallback() {
        const title = this.getAttribute('title') || 'MEDIA';
        const type = this.getAttribute('type') || 'video';
        const src = this.getAttribute('src');

        let mediaHTML = '';
        if (type === 'video') {
            // Use 16:9 video-wrapper for YouTube embeds
            if (src.includes('youtube') || src.includes('youtu.be')) {
                mediaHTML = `
                    <div class="video-wrapper">
                        <iframe src="${src}" frameborder="0" allowfullscreen></iframe>
                    </div>
                `;
            } else {
                mediaHTML = `<video controls src="${src}" class="constrained-media" style="max-height: 450px;"></video>`;
            }
        } else if (type === 'audio') {
            mediaHTML = `
                <div class="glass-box" style="padding: 40px; text-align: center;">
                    <div style="font-size: 60pt; margin-bottom: 20px;">🎵</div>
                    <audio controls src="${src}" style="width: 500px;"></audio>
                </div>
            `;
        }

        this.innerHTML = `
            <h2>${title}</h2>
            <div style="width: 800px; margin-top: 20px;">
                ${mediaHTML}
            </div>
        `;
    }
}

/**
 * <timer-pill duration="5">
 * Interactive Timer Component
 */
class TimerPill extends HTMLElement {
    constructor() {
        super();
        this.duration = parseInt(this.getAttribute('duration')) || 5;
        this.timeLeft = this.duration * 60;
        this.timer = null;
    }

    connectedCallback() {
        this.innerHTML = `
            <div class="timer-pill">
                <div class="timer-display">${this.formatTime(this.timeLeft)}</div>
                <button class="start-btn">START</button>
            </div>
        `;

        this.btn = this.querySelector('.start-btn');
        this.display = this.querySelector('.timer-display');
        this.pill = this.querySelector('.timer-pill');

        this.btn.onclick = (e) => {
            e.stopPropagation(); // Prevent reveal.js nav
            this.toggle();
        };
    }

    formatTime(seconds) {
        const m = Math.floor(seconds / 60).toString().padStart(2, '0');
        const s = (seconds % 60).toString().padStart(2, '0');
        return `${m}:${s} `;
    }

    updateDisplay() {
        this.display.textContent = this.formatTime(this.timeLeft);
    }

    toggle() {
        // Initialize Audio context if needed
        AudioFX.init();

        if (this.timer) {
            // PAUSE
            clearInterval(this.timer);
            this.timer = null;
            this.btn.textContent = 'RESUME';
            this.btn.classList.remove('pause');
        } else {
            // START
            this.btn.textContent = 'PAUSE';
            this.btn.classList.add('pause');
            AudioFX.blip.play().catch(e => console.log("Audio play failed", e)); // Start blip

            this.timer = setInterval(() => {
                if (this.timeLeft > 0) {
                    this.timeLeft--;
                    this.updateDisplay();

                    // Audio Triggers
                    if (this.timeLeft === 30) {
                        AudioFX.warning.play().catch(e => console.error(e));
                    }

                    // Blip on every second in last 10 seconds
                    if (this.timeLeft < 10 && this.timeLeft > 0) {
                        AudioFX.blip.play().catch(() => { });
                    }

                } else {
                    // FINISH
                    clearInterval(this.timer);
                    this.timer = null;
                    this.pill.style.borderColor = 'var(--danger)';
                    this.display.style.color = 'var(--danger)';
                    this.btn.textContent = 'DONE';
                    this.btn.disabled = true;
                    AudioFX.bell.play().catch(e => console.error(e));
                }
            }, 1000);
        }
    }
}

// Register Components
customElements.define('slide-title', SlideTitle);
customElements.define('slide-segue', SlideSegue);
customElements.define('slide-task', SlideTask);
customElements.define('slide-answer', SlideAnswer);
customElements.define('slide-split', SlideSplit);
customElements.define('slide-media', SlideMedia);
customElements.define('timer-pill', TimerPill);

console.log('✅ Modular Slide Components Loaded');
