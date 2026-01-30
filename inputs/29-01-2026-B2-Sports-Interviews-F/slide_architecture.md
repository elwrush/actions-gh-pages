# Slide Architecture - Sports Interviews (B1 Speaking)

| Slide # | Title / Phase | Layout Pattern | Media Requirement | Pedagogical Goal |
| :--- | :--- | :--- | :--- | :--- |
| **1** | Sports Interviews | `title` | Full-screen Background (Sports Action) | Engagement & Context |
| **2** | Ice Hockey | `video` | Pixabay Video (Ice Hockey) | Discussion: Merits/Disadvantages |
| **3** | Badminton | `video` | Pixabay Video (Badminton) | Discussion: Merits/Disadvantages |
| **4** | Basketball | `video` | Pixabay Video (Basketball) | Discussion: Merits/Disadvantages |
| **5** | Today's Mission | `impact` | Mission Background Video (Clipped) | Objective: 1-Min Interview + Pronunciation |
| **6** | Meet the Athletes | `segue` | Gradient Background (Noir) | Transition to Task 5 |
| **7** | Petra (14) | `split_task` | Full-screen Image (Tennis Academy) | Gist: Tennis, Pressure, USA |
| **8** | Holly (16) | `split_task` | Full-screen Image (Soccer Action) | Gist: Confidence, Coaching goal |
| **9** | Newman (18) | `split_task` | Full-screen Image (Wheelchair Basketball) | Gist: Resilience, Paralympics |
| **10** | Reporting the Action | `segue` | Gradient Background (Noir) | Transition to Task 6 |
| **11** | Reporting Verbs | `matching` | None (Glass-box UI) | Match verbs (Admit, Deny, etc.) to 6 quotes |
| **12** | Answer Key | `matching` | None (Glass-box UI) | Auto-animate answers |
| **13** | The Interviewer's Craft | `strategy` | Full-screen Image (Microphone/Journalist) | Task 7: Prep questions + Pronunciation Drill |
| **14** | THE MISSION: 1-Min Roleplay | `split_task` | Full-screen Image (Interview Scene) | Task 8: 1-minute timed role-play |
| **15** | Reflection | `segue` | Gradient Background (Noir) | Teacher feedback on pronunciation |

### Architecture Constraints:
- **Core**: Lightweight Developer Standard.
- **Images**: ALL images will be full-bleed `data-background`.
- **Gating**: Task 9 (Writing) is EXCLUDED as per instructions.
- **Mission Video**: `https://elwrush.github.io/lesson-plan-agent/images/mission_bg_clipped.mp4`.
