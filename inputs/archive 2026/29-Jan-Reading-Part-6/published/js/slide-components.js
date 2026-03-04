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
        
        /* Layout Constants - Projector Standard (16:9 Optimized) */
        --container-width: 1200px;
        --gap: 40px;
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

    /* Body text: Projector-Standard readability (18pt floor) */
    .text-lg { font-size: 32pt !important; }
    .text-md { font-size: 24pt !important; }
    .text-sm { font-size: 20pt !important; }
    .text-xs { font-size: 18pt !important; }

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
        flex-wrap: nowrap;
        justify-content: center;
        align-items: center; /* Changed from stretch to center */
        gap: 20px;
        width: var(--container-width);
        max-width: 100%;
        margin: 0 auto;
    }

    /* Column System - Width optimized for large fonts */
    .col-25 { flex: 0 0 25%; max-width: 25%; }
    .col-30 { flex: 0 0 30%; max-width: 30%; }
    .col-35 { flex: 0 0 35%; max-width: 35%; }
    .col-40 { flex: 0 0 40%; max-width: 40%; }
    .col-50 { flex: 0 0 50%; max-width: 50%; }
    .col-60 { flex: 0 0 60%; max-width: 60%; }
    .col-65 { flex: 0 0 65%; max-width: 65%; }
    .col-70 { flex: 0 0 70%; max-width: 70%; }
    .col-75 { flex: 0 0 75%; max-width: 75%; }

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
    
    /* Centered box variant - Wider for 16:9 */
    .glass-box.centered {
        width: 1000px;
        max-width: 95%;
        margin: 0 auto;
        text-align: center;
    }

    /* ============================================
       HORIZONTAL LAYOUTS - USE FULL WIDTH (16:9)
       ============================================ */
    .layout-horizontal {
        display: flex !important;
        flex-direction: row !important;
        justify-content: space-between !important;
        align-items: stretch !important;
        width: 100% !important;
        height: 100% !important;
        padding: 40px !important;
        box-sizing: border-box !important;
    }

    .layout-horizontal > * {
        flex: 1;
        min-width: 0; /* Prevent flex overflow */
    }

    /* SPLIT LAYOUTS */
    .layout-split-40-60 {
        display: grid !important;
        grid-template-columns: 40% 60% !important;
        gap: 60px;
        width: 100% !important;
        height: 100% !important;
        padding: 60px !important;
        box-sizing: border-box !important;
        align-items: center;
    }

    .layout-split-50-50 {
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
        gap: 60px;
        width: 100% !important;
        height: 100% !important;
        padding: 60px !important;
        box-sizing: border-box !important;
        align-items: center;
    }

    .layout-split-60-40 {
        display: grid !important;
        grid-template-columns: 60% 40% !important;
        gap: 60px;
        width: 100% !important;
        height: 100% !important;
        padding: 60px !important;
        box-sizing: border-box !important;
        align-items: center;
    }

    /* OVERRIDE CENTERING FOR THESE LAYOUTS */
    section.layout-horizontal,
    section.layout-split-40-60,
    section.layout-split-50-50,
    section.layout-split-60-40 {
        justify-content: flex-start !important;
        align-items: stretch !important;
        flex-direction: row !important; /* Safety */
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
        text-shadow: 0 0 20px var(--text-accent), 0 0 40px var(--primary), 6px 6px 0px rgba(0,0,0,0.5);
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
    /* Soft Atmospheric Glow Layer */
    .reveal .slides > section::before {
        content: "";
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        width: 1500px; height: 1500px;
        background: radial-gradient(circle, rgba(0, 242, 255, 0.08) 0%, transparent 60%);
        pointer-events: none;
        z-index: -1;
        filter: blur(120px);
        border-radius: 50%;
    }
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
        const title = this.getAttribute('title') || 'SEGUE';
        const section = this.closest('section');
        if (section) section.setAttribute('data-background-gradient', 'var(--grad-segue)');

        this.innerHTML = `
            <div class="slide-canvas">
                <h1 class="segue-title" style="font-size: 80px !important;">${title}</h1>
            </div>
        `;
        if (window.Reveal) Reveal.layout();
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

        // Force a 40/60 Horizontal Split for 16:9 utilization
        this.innerHTML = `
            <div class="layout-split-40-60">
                <div style="display: flex; flex-direction: column; justify-content: center; text-align: left;">
                    ${badge ? `<div class="stage-badge">${badge}</div>` : ''}
                    <h2 style="font-size: 55pt !important; margin: 0;">${title}</h2>
                    ${duration ? `<timer-pill duration="${duration}" style="margin-top: 40px;"></timer-pill>` : ''}
                </div>
                <div class="glass-box" style="display: flex; flex-direction: column; justify-content: center; height: fit-content; align-self: center;">
                    <div style="font-size: 24pt; line-height: 1.4;">${content}</div>
                </div>
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
        const duration = this.getAttribute('timer');

        // Robust extraction
        const container = document.createElement('div');
        container.innerHTML = this.innerHTML;
        const img = container.querySelector('img');
        const imgHTML = img ? img.outerHTML : '';
        if (img) img.remove();

        // Handle attribution
        const attrDiv = container.querySelector('.attribution');
        const attrHTML = attrDiv ? attrDiv.outerHTML : '';
        if (attrDiv) attrDiv.remove();

        const contentHTML = container.innerHTML;

        this.innerHTML = `
            <div class="layout-split-40-60">
                <div style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
                    ${badge ? `<div class="stage-badge" style="align-self: flex-start; margin-bottom: 20px;">${badge}</div>` : ''}
                    <div style="width: 100%; text-align: center;">${imgHTML}</div>
                    ${attrHTML}
                    ${duration ? `<timer-pill duration="${duration}" style="margin-top: 30px;"></timer-pill>` : ''}
                </div>
                <div style="display: flex; flex-direction: column; justify-content: center;">
                    ${title ? `<h2 style="font-size: 45pt !important; margin-bottom: 30px; text-align: left;">${title}</h2>` : ''}
                    <div class="glass-box" style="font-size: 26pt; line-height: 1.3;">
                        ${contentHTML}
                    </div>
                </div>
            </div>
        `;

        const newImg = this.querySelector('img');
        if (newImg) {
            newImg.classList.add('constrained-media');
            newImg.style.maxHeight = '500px';
            newImg.style.width = 'auto';
            newImg.style.border = '4px solid var(--primary)';
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
                        <iframe src="${src}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share; fullscreen" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen playsinline></iframe>
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
        this.timer = null;
    }

    connectedCallback() {
        this.duration = parseInt(this.getAttribute('duration')) || 5;
        this.timeLeft = this.duration * 60;

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
            AudioFX.blip.play().catch(e => console.log("Audio play failed", e)); // Blip on start

            this.timer = setInterval(() => {
                if (this.timeLeft > 0) {
                    this.timeLeft--;
                    this.updateDisplay();

                    // Audio Triggers
                    if (this.timeLeft === 30) {
                        AudioFX.warning.play().catch(e => console.error(e));
                    }

                    // Blip only during final 29 seconds (29 to 1)
                    if (this.timeLeft <= 29 && this.timeLeft >= 1) {
                        AudioFX.blip.currentTime = 0;
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

/**
 * <grammar-transform before="..." after="..." highlight="...">
 * Auto-animated grammar transformation component
 * Shows before/after sentence with smooth morphing animation
 * 
 * Usage:
 * <grammar-transform 
 *   before="Michelangelo, who was a brilliant sculptor, carved..."
 *   after="Michelangelo, a brilliant sculptor, carved..."
 *   highlight="who was">
 * </grammar-transform>
 */
class GrammarTransform extends HTMLElement {
    connectedCallback() {
        const before = this.getAttribute('before') || '';
        const after = this.getAttribute('after') || '';
        const highlight = this.getAttribute('highlight') || '';
        const title = this.getAttribute('title') || 'Grammar Transformation';

        // Create two auto-animated sections
        const beforeSlide = document.createElement('section');
        beforeSlide.setAttribute('data-auto-animate', '');
        beforeSlide.setAttribute('data-auto-animate-duration', '1.5');
        beforeSlide.setAttribute('data-auto-animate-easing', 'ease-in-out');
        beforeSlide.setAttribute('data-background-gradient', 'var(--grad-main)');

        const afterSlide = document.createElement('section');
        afterSlide.setAttribute('data-auto-animate', '');
        afterSlide.setAttribute('data-auto-animate-duration', '1.5');
        afterSlide.setAttribute('data-auto-animate-easing', 'ease-in-out');
        afterSlide.setAttribute('data-background-gradient', 'var(--grad-main)');

        // Highlight the part to be removed in the before slide
        let beforeHTML = before;
        if (highlight) {
            beforeHTML = before.replace(
                highlight,
                `<span data-id="remove" style="color: #ef4444; font-weight: bold; text-decoration: underline;">${highlight}</span>`
            );
        }

        beforeSlide.innerHTML = `
            <h2>${title}</h2>
            <div style="margin-top: 60px;">
                <p data-id="sentence" style="font-size: 36px; font-style: italic; text-align: center;">
                    ${beforeHTML}
                </p>
            </div>
            <p style="font-size: 24px; margin-top: 40px; color: #ef4444;">⬇ Watch the underlined words disappear ⬇</p>
            <aside class="notes">
                **Advice**: Point out the highlighted part - this is what we'll remove. Advance slowly to show the animation.
                **Next**: Auto-animate to show the transformation.
            </aside>
        `;

        afterSlide.innerHTML = `
            <h2>${title}</h2>
            <div style="margin-top: 60px;">
                <p data-id="sentence" style="font-size: 36px; font-style: italic; text-align: center; color: var(--text-accent);">
                    ${after}
                </p>
            </div>
            <p style="font-size: 32px; margin-top: 40px; color: var(--text-accent);">✓ We removed: <strong>${highlight}</strong></p>
            <aside class="notes">
                **Advice**: The sentence morphs smoothly over 1.5 seconds - the highlighted part disappears!
                **Next**: Continue with explanation.
            </aside>
        `;

        // Replace this element with the two sections
        this.parentNode.insertBefore(beforeSlide, this);
        this.parentNode.insertBefore(afterSlide, this);
        this.remove();
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
customElements.define('grammar-transform', GrammarTransform);

console.log('✅ Modular Slide Components Loaded');
