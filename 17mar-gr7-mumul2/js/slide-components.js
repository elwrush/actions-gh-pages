/**
 * PHASE 17.4 - NATIVE LAYOUT & AUDIO ALIGNMENT
 */

// GLOBAL AUDIO CONTROLLER (Hard Primed via Pre-loaded <audio> tags)
window.AudioFX = {
    sounds: {},
    ready: false,
    init: function() {
        if (this.ready) return;
        this.sounds.blip = document.getElementById('audio-blip');
        this.sounds.bell = document.getElementById('audio-bell');
        this.sounds.warning = document.getElementById('audio-warning');
        this.ready = true;
        console.log("🔊 AudioFX Initialized");
    },
    play: function(key) {
        if (!this.ready) this.init();
        const s = this.sounds[key];
        if (s) {
            s.currentTime = 0;
            s.play().catch(e => console.warn(`Audio play failed for ${key}:`, e));
        } else {
            console.error(`Audio key not found: ${key}`);
        }
    }
};

class TimerPill extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
        this.timer = null;
        if (!window._timerState) window._timerState = {};
    }

    get stateId() { return this.closest('section')?.id || 'timer-' + (this.getAttribute('duration') || 'global'); }
    get state() {
        if (!window._timerState[this.stateId]) {
            const dur = parseInt(this.getAttribute('duration')) || 5;
            window._timerState[this.stateId] = { timeLeft: dur * 60, duration: dur, isPaused: true, isDone: false };
        }
        return window._timerState[this.stateId];
    }

    connectedCallback() { this.render(); if (!this.state.isPaused) this.start(); }
    disconnectedCallback() { clearInterval(this.timer); }

    render() {
        const s = this.state;
        this.shadowRoot.innerHTML = `
            <style>
                :host { display: block; width: fit-content; margin: 20px auto 0 auto; }
                .p { display: flex; align-items: center; gap: 10px; padding: 5px 15px; background: rgba(0,0,0,0.8); border: 1px solid #FFD700; border-radius: 30px; }
                .d { font-family: monospace; font-size: 1.2em; color: ${s.isDone ? '#ff4444' : '#FFD700'}; font-weight: bold; min-width: 60px; }
                button { background: #FFD700; color: black; border: none; padding: 3px 10px; font-weight: bold; cursor: pointer; border-radius: 15px; font-size: 0.55em; text-transform: uppercase; }
                button.pause { background: #ff4444; color: white; }
                button.reset { background: rgba(255,255,255,0.1); color: white; border: 1px solid white; }
                button:disabled { opacity: 0.5; }
            </style>
            <div class="p">
                <div class="d">${this.fmt(s.timeLeft)}</div>
                <button class="s ${!s.isPaused ? 'pause' : ''}" ${s.isDone ? 'disabled' : ''}>
                    ${s.isDone ? 'DONE' : (s.isPaused ? (s.timeLeft < s.duration * 60 ? 'RESUME' : 'START') : 'PAUSE')}
                </button>
                <button class="r reset">RESET</button>
            </div>
        `;
        this.shadowRoot.querySelector('.s').onclick = (e) => { e.stopPropagation(); this.toggle(); };
        this.shadowRoot.querySelector('.r').onclick = (e) => { e.stopPropagation(); this.reset(); };
    }

    fmt(s) { return `${Math.floor(s/60).toString().padStart(2,'0')}:${(s%60).toString().padStart(2,'0')}`; }

    reset() {
        clearInterval(this.timer);
        this.state.isPaused = true;
        this.state.isDone = false;
        this.state.timeLeft = this.state.duration * 60;
        this.render();
    }

    toggle() {
        if (window.AudioFX && !window.AudioFX.unlocked) {
            window.AudioFX.init();
            // Unlock ALL sounds to satisfy browser policies
            ['blip', 'bell', 'warning'].forEach(key => {
                const s = window.AudioFX.sounds[key];
                if (s) {
                    s.play().then(() => {
                        s.pause();
                        s.currentTime = 0;
                    }).catch(e => console.warn(`Audio unlock failed for ${key}:`, e));
                }
            });
            window.AudioFX.unlocked = true;
        }

        if (!this.state.isPaused) {
            clearInterval(this.timer);
            this.state.isPaused = true;
        } else {
            this.state.isPaused = false;
            this.start();
        }
        this.render();
    }

    start() {
        clearInterval(this.timer);
        this.timer = setInterval(() => {
            const s = this.state;
            if (s.timeLeft > 0) {
                s.timeLeft--;
                this.shadowRoot.querySelector('.d').textContent = this.fmt(s.timeLeft);
                if (s.timeLeft === 30) window.AudioFX?.play('warning');
                if (s.timeLeft < 10 && s.timeLeft > 0) window.AudioFX?.play('blip');
            } else {
                clearInterval(this.timer);
                s.isPaused = true;
                s.isDone = true;
                window.AudioFX?.play('bell');
                this.render();
            }
        }, 1000);
    }
}

customElements.define('timer-pill', TimerPill);
console.log('✅ PHASE 17.4 Components Ready');
