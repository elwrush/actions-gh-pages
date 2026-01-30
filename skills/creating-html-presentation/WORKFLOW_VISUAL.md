
graph TD
    subgraph Discovery
        A[Start: Refined User Plan] --> B[Skill Activation: creating-html-presentation]
    end

    subgraph Linguistic_Alignment
        B --> C[CEFR B1 Protocol: High-Engagement Visuals]
        C --> D[Identify Assets: Petra, Holly, Newman, Sports Clips]
    end

    subgraph Template_Regeneration
        D --> E[Base Template: Zero-Overlap Native Reveal]
        E --> F[Title: Gradient Left-Align]
        F --> G[Video Slides: Observation Logic]
        G --> H[Mission Slide: Non-Looping Video + Badges]
        H --> I[Task Slides: Centered Bullets + Dimming]
        I --> J[Answer Key: Native Table Logic]
        J --> K[Strategy: Blockquote Skills]
        K --> L[Final Task: Timer with Sound/Reset]
    end

    subgraph Compilation
        L --> M[Generate presentation.json]
        M --> N[Run python generate_presentation.py]
        N --> O[Final Quality Check: published/index.html]
    end
