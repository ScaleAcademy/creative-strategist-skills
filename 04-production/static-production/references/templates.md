# Static Format Templates — Overview

Reference of available static ad format templates. Each template provides copy structures, image generation prompts, and variation vectors for a specific ad format type.

**Usage rule:** Select the template AFTER choosing the style code (S-series) and angle (C1-C4). The template provides the production blueprint; the strategy defines what goes into it.

---

## Available Templates

### Headline Template (S101–S105)
**File:** `headline-template.md`
**Status:** Complete
**What it covers:** The most common static format — a dominant headline carrying the entire message with a supporting visual.
**Includes:** 3 styles (Product Hero, Lifestyle Context, Typography Dominant), copy templates, Nano Banana image generation prompts, variation vectors.
**When to use:** Single strong message, product launch, brand awareness, retargeting offers.
**Best awareness stages:** All levels — adapt the headline to the awareness stage.

---

### Collage / Multi-Element Template (S201–S205)
**File:** `collage-template.md`
**Status:** To be created
**What it will cover:** Grid layouts, before/after splits, feature callout compositions, testimonial compilations.
**When to use:** Multiple proof points, product comparisons, feature-rich products.
**Best awareness stages:** Solution Aware, Product Aware

---

### Lifestyle / UGC Template (S301–S305)
**File:** `lifestyle-template.md`
**Status:** To be created
**What it will cover:** Native-feeling stills, flat lay compositions, in-context product shots, candid/street style.
**When to use:** Authenticity-first brands, TOF awareness, younger audiences.
**Best awareness stages:** Unaware, Problem Aware

---

### Typography / Text Template (S401–S403)
**File:** `typography-template.md`
**Status:** To be created
**What it will cover:** Bold statement cards, quote cards, data highlight compositions.
**When to use:** Strong one-liner messages, social proof quotes, striking statistics.
**Best awareness stages:** All levels

---

### Data / Proof Template (S501–S504)
**File:** `data-template.md`
**Status:** To be created
**What it will cover:** Screenshot compositions, chart/graph layouts, press mention formats, review compilations.
**When to use:** Credibility-first campaigns, B2B, high-ticket products.
**Best awareness stages:** Solution Aware → Most Aware

---

### Conceptual / Creative Template (S601–S604)
**File:** `conceptual-template.md`
**Status:** To be created
**What it will cover:** Metaphor visuals, meme adaptations, pattern interrupt compositions, minimal conceptual layouts.
**When to use:** Saturated feeds, brand differentiation, creative testing sprints.
**Best awareness stages:** Unaware (interrupt), Most Aware (brand reinforcement)

---

## Template Selection Guide

| If your brief says... | Use template | Style codes |
|---|---|---|
| Single headline, product focus | Headline | S101–S105 |
| Multiple features or proof points | Collage | S201–S205 |
| Authentic, native feel | Lifestyle/UGC | S301–S305 |
| One powerful statement or stat | Typography | S401–S403 |
| Hard proof — screenshots, reviews, press | Data/Proof | S501–S504 |
| Creative differentiation, pattern interrupt | Conceptual | S601–S604 |

---

## Carousel Templates

Carousels combine multiple templates across slides. Standard patterns:

| Carousel type | Slide 1 template | Middle slides | Final slide |
|---|---|---|---|
| Educational | Typography (S401) | Typography (S103) | Headline (S101) + CTA |
| Social proof | Typography (S402) | Data (S501) | Collage (S204) |
| Product showcase | Headline (S101) | Lifestyle (S304) | Data (S501) + offer |
| Problem → Solution | Typography (S401) | Collage (S202) | Headline (S101) + CTA |

---

## Production Workflow

```
1. Creative brief defines: angle, awareness stage, hook, style code
2. Select matching template from this list
3. Fill in copy template from the template file
4. Generate image using the Nano Banana prompt from the template
5. Apply variation vectors for A/B testing
6. Pass through agent-static-production for validation
7. Pass through agent-copy-editor for grammar/compliance check
```
