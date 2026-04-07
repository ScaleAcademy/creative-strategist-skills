---
name: brand-specs
description: "Generates two visual spec cards (Brand Spec Card + Visual Style Card) as HTML then PNG from the brand-research-brief.json. These cards are uploaded to Project Knowledge and used as reference images in every Nano Banana or AI image generation prompt. Trigger on: 'generate spec cards', 'build brand spec', 'brand spec card', 'visual style card'. Requires brand-research-brief.json. Output dramatically improves AI image generation accuracy (from ~60-70% to ~90-95% hit rate)."
metadata:
  version: 1.0.0
  status: beta
  tags: [audit, brand, visual, spec-card, production, nano-banana]
  inputs: [brand-research-brief.json]
  outputs: [brand-spec-card.png, visual-style-card.png]
  depends-on: [brand-research]
---

# Brand Specs

## Before Starting

Confirm before starting:
- [ ] `brand-research-brief.json` exists in Project Knowledge (otherwise launch `brand-research` first)
- [ ] Access to a browser or tool that can render HTML and take screenshots
- [ ] If brand guidelines PDF exists → ensure it was uploaded before `brand-research` ran

---

This skill generates two reference cards that are uploaded alongside every AI image generation prompt. They eliminate guesswork for tools like Nano Banana and dramatically improve output consistency.

**Input:** `brand-research-brief.json`
**Output:** `brand-spec-card.png` + `visual-style-card.png` — uploaded to Project Knowledge

**Impact:** Hit rate without spec cards: ~60–70% / with spec cards: ~90–95%

---

## Phase 1: Generate Brand Spec Card

Using the brand-research-brief.json, generate a clean HTML page to screenshot as a Brand Spec Card.

**The card must include:**

1. **Logo & Wordmark** — brand name rendered in exact fonts and colors from the brief, with black and white versions and usage notes
2. **Typography System** — sample text rendered in each font role (headlines, body, accents/labels) with font names labeled
3. **Color Palette** — visual swatches of all brand colors with hex codes and names (primary, secondary, accent, background)
4. **Design Rules** — 4–5 "always do" and 4–5 "never do" rules specific to this brand
5. **CTA Button Style** — actual CTA button rendered (color, shape, text treatment) based on what was found on the site

**Quality check:** Every detail must be visually explicit, not just described in text. This card is uploaded as a reference image to an AI image generator.

For the full prompt template: See [references/brand-spec-card-prompt.md](references/brand-spec-card-prompt.md)

---

## Phase 2: Generate Visual Style Card

Using the same brand-research-brief.json, generate a second HTML page to screenshot as a Visual Style Card.

**The card must include:**

1. **Brand Essence** — 3 adjectives that define the brand voice, with short descriptions
2. **Founder Quote** — one defining quote that captures the brand's philosophy
3. **Photography Direction** — separate visual blocks for: product photography, skin/model photography, lifestyle/context shots, and background/surface preferences. Each with keyword tags
4. **Always/Never Rules** — specific to how this brand portrays people, skin, products, and environments
5. **Product Styling Notes** — how the hero product should be photographed
6. **Mood Spectrum** — where the brand sits on scales: loud vs quiet, youthful vs timeless, clinical vs warm

For the full prompt template: See [references/visual-style-card-prompt.md](references/visual-style-card-prompt.md)

---

## Phase 3: Export & Upload

1. Screenshot each HTML page as PNG
2. Save as `brand-spec-card.png` and `visual-style-card.png`
3. Upload both to Project Knowledge

---

## How to Use in Production

For every Nano Banana or AI image generation prompt, upload these 3 files:
1. `brand-spec-card.png`
2. `visual-style-card.png`
3. Hero product reference photo

Nano Banana 2 does not make assumptions — a prompt of 800–1000 words is normal when using these spec cards.

---

## Tips

- If brand guidelines exist as PDF → convert to Markdown first: `"convert this to a Markdown file"`
- To extract fonts: inspect the brand's HTML, copy the `font` section, paste into Claude → `"update the spec cards accordingly"`
- Regenerate spec cards whenever the brand identity or product line changes

---

## Related Skills

- `01-audit/brand-research` — prerequisite: generates the brand-research-brief.json
- `04-production/static-production` — uses spec cards as reference for every image prompt
- `04-production/ai-video-production` — uses spec cards for video generation consistency
