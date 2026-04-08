---
name: static-production
description: "Turns a validated creative brief into a Nano Banana image generation prompt and a structured designer brief. Use after creative-brief is validated and the format is static. Trigger on: 'generate an image', 'designer brief', 'static ad', 'Nano Banana prompt', 'static creative'. Produces a ready-to-execute production package."
metadata:
  version: 1.0.0
  status: beta
  tags: [production, static, design, prompt, image]
  inputs: [validated creative-brief, selected hook (hook-writing)]
  outputs: [Nano Banana prompt + structured designer brief]
  depends-on: [creative-brief, hook-writing]
---

# Static Production

## Before Starting

Confirm before starting:
- [ ] Validated creative brief
- [ ] Selected hook (top 1–3 from the hook bank)
- [ ] Format defined: ratio (9:16 / 4:5 / 1:1), usage (Feed / Story / Reels cover)
- [ ] Visual style defined or to be chosen (see style reference)
- [ ] Access to Nano Banana or image tool available

---

## Phase 1: Define the Visual Structure

A good static has 3 zones:

**Zone 1 — Visual hook (60% of attention)**
What the eye sees first. Must stop the scroll without text.
→ Face / emotion / recognizable situation / strong contrast / shocking first frame

**Zone 2 — Text (headline + subtitle)**
Maximum 7 words in headline. Readable in 1 second at scroll speed.
→ The text hook goes here — short version of the selected hook

**Zone 3 — CTA + Logo**
Subtle. Don't overload. CTA must be clear but not aggressive.

---

## Phase 2: Select the Style Template

Each static format has dedicated style templates with copy structure, image prompt, and variation vectors. Select the right one based on the brief's S-code.

**Available templates** (see `references/` folder):
- `headline-template.md` — Headline format (most common static)
  - Style A: Product hero with headline
  - Style B: Lifestyle context with headline
  - Style C: Typography-dominant

> More templates to come: Screenshot, Checklist, Avant/Après, Mème, etc.

### How to use a style template

1. **Pick the style** (A/B/C) based on the brief's visual direction
2. **Fill the copy template** with the selected hook and brief data
3. **Fill the image prompt** with brand spec, persona, and variation choices
4. **Choose variation vectors** — pick one option per vector to create a unique combination
5. **Run the coherence test** (see template global rules)

---

## Phase 3: Write the Image Generation Prompt

Use the prompt from the selected style template. Fill all variables:
- `[BRAND NAME]`, `[PRODUCT NAME]`, `[ASPECT RATIO]`
- `[HEADLINE]`, `[SUBHEAD]`, `[CTA]` from Phase 2
- `[PERSONA SUMMARY]` from the brief
- Variation selections (product position, background, lighting, energy)

**What a good prompt avoids:**
- Too many competing details (1 main subject max)
- Style inconsistent with brand tone
- Text embedded in the image (add in post-production unless using typography-dominant style)

---

## Phase 4: Write the Designer Brief

For assets produced by a human designer or for review handoff:

```markdown
## Designer Brief — [Brand] — [Creative ID] — [Date]

### Format
Ratio: [9:16 / 4:5 / 1:1]
Dimensions: [px]
Usage: [Feed / Story / Cover]

### Concept
[Description in 2–3 sentences of what the creative must convey]

### Style Template
Template: [headline / screenshot / checklist / ...]
Style: [A / B / C]
Variation: [chosen vectors]

### Zone 1 — Main Visual
[Precise description: subject, position, emotion, context]

### Zone 2 — Text
Headline: "[Exact text — max 7 words]"
Subtitle: "[Exact text — max 15 words]" (optional)

### Zone 3 — CTA + Logo
CTA: "[Exact text]"
Logo position: [Top left / Top right / Bottom]

### Visual Style
[S-code from Styles Library + description]

### Coherence Check
- [ ] Cover headline → does image hint at the idea? ✓/✗
- [ ] Cover image → does headline conjure matching visual? ✓/✗

### Copy Editor Check
- [ ] Grammar, spelling, punctuation ✓
- [ ] Word count within spec ✓
- [ ] Brand name capitalization ✓
- [ ] No duplicate content across elements ✓

### References
[Link to reference creative or moodboard if available]
```

---

## Phase 5: Brief → Score → Generate (Production Loop)

Once the system is set up (brand extraction, spec cards, format templates, agents), these are the prompts you run every time you create an ad.

### 5a. Starter Prompt — Briefing

```
I want to create a [FORMAT TEMPLATE] ad for [PRODUCT NAME].

Persona: [e.g. Sensitive Skin Sufferer]
Angle: [e.g. Transformation]
Emotion: [e.g. Relief]

Use my brand bible and format template to write the full brief: headline, subhead, 
copy, creative direction, everything. Follow the format template exactly.
```

### 5b. Starter Prompt — Agent Review

```
Please have the agents review the copy.

Please iterate on the copy until every agent gives it a 90+ / 100.
```

This triggers `agent.md` (static production) and `agent-copy-editor.md` (copy validation). Nothing moves to generation until both pass 90+.

### 5c. Convert Approved Copy to Nano Banana 2 Prompt

```
Convert this into a ready-to-paste Nano Banana 2 image generation prompt.

The prompt must include:
- Exact dimensions (1080x1920, 9:16 vertical)
- Every piece of approved copy rendered verbatim in the image
- Product position, angle, and scale from the creative direction
- Background treatment from the creative direction
- Typography: exact font names, weights, and color from the brand spec card
- Safe zones (top 270px, bottom 340px clear of critical content)
- Lighting and energy direction
- Logo placement per brand spec sheet
- All 10 universal rules (no panels, no text under 24px, 
  sufficient contrast, photorealistic product, etc.)
- A note that I will upload the brand spec card, visual style 
  card, and product photo as reference images
```

---

## Phase 6: Multiply Across Format Templates

When a brief wins (proven by performance data or strategic confidence), multiply it across all available format templates.

### Multiply Prompt

```
I have a winning ad brief that I want to multiply across different format templates. 
The original brief is below.

Here are my format templates: [upload or list your .md template files]

For EACH format template, rewrite the brief to fit that format exactly:
- Keep the same persona, angle, emotion, and core product truth
- Rewrite the copy to match the new format's structure 
  (headline lengths, copy slots, required elements)
- Follow the format template's copy rules and variation vectors
- Adjust the creative direction to match the new format's 
  visual requirements
- Write a complete Nano Banana 2 image generation prompt for each

Do not change the strategic foundation. Only change the packaging.

The original brief:
[paste your winning brief here]
```

**Key principle:** Same strategy, different packaging. The persona, angle, emotion, and product truth stay constant. Only the format, copy structure, and visual treatment change.

---

## Related Skills

- `03-strategy/creative-brief` — prerequisite
- `03-strategy/hook-writing` — selected hook becomes the main text
- `04-production/animate-statics` — turn winning static into animated GIF
- `05-analysis/campaign-setup` — after production, campaign setup
- `05-analysis/ad-analysis` — after delivery
