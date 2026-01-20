# Component Library & Style Guide

> [!IMPORTANT]
> **GOLD STANDARD (Jan 2026)**: All presentations must use `slide-components.js` and the palette system from `PALETTES.md`. No hardcoded hex colors allowed.

## Quick Start

```html
<head>
    <!-- Fonts (REQUIRED) -->
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Courier+Prime:wght@700&display=swap" rel="stylesheet">
    
    <!-- Component Library -->
    <script src="../../skills/creating-html-presentation/js/slide-components.js"></script>
</head>
```

---

## Layout Patterns (Gold Standard)

### Core Container Width
All content fits within **1100px** using `row-container` (Wider for classroom visibility):

```html
<div class="row-container">
    <div class="col-35"><!-- 35% width --></div>
    <div class="col-65"><!-- 65% width --></div>
</div>
```

### Font Sizes (Projector Standard)
| Class | Size | Use Case |
|-------|------|----------|
| `.text-lg` | 32pt | Headlines / Hero Text |
| `.text-md` | 24pt | Major Body Text |
| `.text-sm` | 20pt | Dense content |
| `.text-xs` | 18pt | MINIMUM (Fine print) |

> [!CAUTION]
> **NEVER** use font sizes smaller than 18pt. They are invisible on classroom projectors.

---

## Components

### `<slide-segue>`
Full-screen phase transition with rotated title.

**CRITICAL**: Segue slides MUST use a high-contrast dark gradient (not palette-dependent):

```html
<section data-background-gradient="radial-gradient(circle, #1a1a2e 0%, #0f0f1a 100%)">
    <slide-segue title="PHASE 1: ANALYSIS"></slide-segue>
</section>
```

### `<slide-task>`
Task slide with optional stage badge and timer.

> [!IMPORTANT]
> Components do NOT auto-add borders. Add `class="glass-box"` in YOUR content when you need a bordered container.

```html
<section data-background-image="images/cyber_bg.png" data-background-opacity="0.1">
    <slide-task title="THE CHALLENGE" badge="TASK 1" timer="5">
        <!-- YOU add glass-box when needed -->
        <div class="glass-box" style="width: 800px; margin: 0 auto; text-align: center;">
            <p class="text-md">Write an article about what makes you laugh.</p>
            <div class="teacher-tip">Check all 3 questions!</div>
        </div>
    </slide-task>
</section>
```

### `<slide-answer>`
Answer slide with themed title (uses `--primary` for header and border).

```html
<section data-background-color="var(--bg-dark)">
    <slide-answer title="TASK 1: ANSWER 1">
        <div class="glass-box" style="width: 800px; margin: 0 auto;">
            <p class="text-sm">"The car <span class="highlight">which I bought</span>..."</p>
        </div>
    </slide-answer>
</section>
```

### `<slide-split>`
Two-column layout: Image (40%) + Content (60%).

```html
<section>
    <slide-split title="CONTEXT" badge="WARM UP">
        <img src="images/map.jpg">
        <!-- Content goes in col-60, add glass-box if you want a border -->
        <div class="glass-box">
            <p class="text-md">This map shows global trade routes.</p>
        </div>
    </slide-split>
</section>
```

### `<slide-media>`
Video/Audio with proper aspect ratio handling.

```html
<section>
    <slide-media title="LISTENING" type="video" src="https://youtube.com/embed/..."></slide-media>
</section>
```

---

## Special Slide Types

### Boss Level / Final Task
Use a **distinctive background color** for the final creative task:

```html
<section data-background-color="var(--secondary)">
    <slide-task title="BOSS LEVEL" badge="FINAL TASK" timer="20">
        <p>Write your tech article!</p>
    </slide-task>
</section>
```

---

## Reveal.js Config (Required)

```javascript
Reveal.initialize({
    width: 960,
    height: 700,
    margin: 0.1,
    transition: 'convex', // IMPORTANT: Cool transition effect
    // ...other options
});
```

---

## Theme Tokens (CSS Variables)

Override these in your presentation's `<style>` block. See `PALETTES.md` for 10 ready-to-use themes.

```css
:root {
    --primary: #78909C;      /* Blue Grey 400 */
    --secondary: #90A4AE;    /* Blue Grey 300 */
    --bg-dark: #263238;      /* Blue Grey 900 */
    --text-accent: #FFFFFF;  /* White */
    --glass: rgba(38, 50, 56, 0.95);
    --danger: #ef4444;       /* Timer expiration */
}
```

> [!NOTE]
> Headers are always white for projector contrast. See `PALETTES.md` for the Header Contrast Rule.
