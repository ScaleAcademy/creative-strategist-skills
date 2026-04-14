---
name: video-production
description: "Turns a validated creative brief into a sequenced technical brief for a human video editor or creator. Use after creative-brief and hook-writing when the format is video. Trigger on: 'video brief', 'editor brief', 'video script', 'scene sequence'. Produces a scene-by-scene production brief ready to hand to the production team."
metadata:
  version: 1.0.0
  status: beta
  tags: [production, video, script, brief, editing]
  inputs: [validated creative-brief, selected hook, available assets (footage, UGC, product)]
  outputs: [video technical brief — scene by scene]
  depends-on: [creative-brief, hook-writing]
---

# Video Production

## Before Starting

Confirm before starting:
- [ ] Validated creative brief
- [ ] Selected hook (top 1 from the hook bank)
- [ ] Target duration defined (15s / 30s / 45s / 60s / 90s)
- [ ] Available assets inventoried (UGC footage, product footage, images, voiceover)
- [ ] Style defined (native UGC / talking head / product B-roll / dynamic montage)

---

## Phase 1: Define the Narrative Structure

Every ad video follows a tension-resolution structure:

```
Hook (0–3s) → Tension (3–15s) → Pivot (15–Xs) → Resolution (X–end) → CTA
```

**For 15s:** Hook (3s) → Short tension (7s) → Direct CTA (5s)
**For 30s:** Hook (3s) → Tension (12s) → Resolution (10s) → CTA (5s)
**For 60s:** Hook (3s) → Tension (20s) → Mechanism (20s) → Proof (10s) → CTA (7s)

---

## Phase 2: Sequence the Scenes

For each scene, define:

| Field | Content |
|---|---|
| Duration | In seconds |
| Visual | What is seen on screen |
| Audio | Voiceover / dialogue / ambient sound / silence |
| Text overlay | Text displayed on screen (if applicable) |
| Target emotion | What the viewer should feel |
| Editing note | Rhythm, transition, effect |

---

## Phase 3: Write the Technical Brief

```markdown
## Video Brief — [Brand] — [Creative ID] — [Date]

### Context
Objective: [What the video must produce]
Target persona: [Fictional first name + awareness stage]
Tone: [Natural UGC / Professional / Educational / Emotional]
Primary platform: [Meta Feed / Reels / Stories]

### Specs
Duration: [Xs]
Ratio: [9:16 / 4:5]
Sound: [Voice on / Voice off / Silent]
Subtitles: [Yes / No — style if yes]

### Available Assets
- [List of provided elements]
- [Elements to find / shoot]

### Scene-by-Scene Structure

**Scene 1 — Hook [0–3s]**
Visual: [Description]
Audio: [Voice / Sound]
Text overlay: "[Text]"
Emotion: [What we should feel]
Note: [Editing instructions]

**Scene 2 — [Name] [3–Xs]**
[Same structure]

[...]

**Final Scene — CTA [X–end]**
Visual: [Product / Visual CTA]
Audio: "[CTA voiceover]"
Text overlay: "[Exact CTA]"

### Constraints
[Compliance, forbidden visuals, claims to avoid]

### References
[Links to reference creatives in the same style]
```

---

## Related Skills

- `03-strategy/creative-brief` — prerequisite
- `03-strategy/hook-writing` — selected hook = first scene
- `04-production/ai-video-production` — AI alternative for the same brief
- `04-production/campaign-setup` — after production
- `05-analysis/ad-analysis` — after delivery
