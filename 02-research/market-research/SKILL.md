---
name: market-research
description: "Maps the competitive landscape and market sophistication level for a product category. Use before building any creative strategy. Trigger on: 'research the market', 'what are competitors doing', 'sophistication level of this market'. Requires brand context from brand-guidelines."
metadata:
  version: 1.0.0
  status: stable
---

# Market Research

This skill maps the competitive landscape and market sophistication before any creative strategy begins.

**Input:** Brand context doc + product category
**Output:** Market sophistication level + competitor map + positioning gaps + creative implications

---

## Step 1: Competitive Audit

For each of the 3–5 main competitors:
- Primary claim (what they say they are)
- Awareness level they target (Unaware → Most Aware)
- Dominant creative formats (video / static / UGC)
- Angles used (pain / proof / education / identity)
- What's missing from their messaging

**Where to look:**
- Meta Ad Library (facebook.com/ads/library)
- Competitor websites — hero section, product pages
- Review platforms (Trustpilot, Amazon, Google)
- TikTok and Instagram for organic signals

For research sources: See [references/competitors.md](references/competitors.md)

---

## Step 2: Market Sophistication Level

Assess the Schwartz sophistication level for the category.
Key question: **What claims are already cliché in this category?**

For sophistication framework: See [references/sophistication.md](references/sophistication.md)

---

## Step 3: Positioning Map

Plot the category on two axes relevant to the product.
Find the white space — where no competitor is positioned.

For positioning frameworks: See [references/positioning.md](references/positioning.md)

---

## Step 4: Output

```
## Market Research Report — [Category] — [Date]

### Sophistication Level
Level [1–5] — [Rationale in 2–3 sentences]

### Saturated Claims (avoid)
- [Claim 1]

### Competitor Map
| Competitor | Primary Claim | Awareness Target | Dominant Format | Gap |

### White Space Opportunities
[2–3 positioning opportunities not currently occupied]

### Creative Implications
[What this means for angle, hook strategy, and awareness stage targeting]
```

---

## Related Skills

- `01-audit/brand-guidelines` — prerequisite
- `02-research/audience-research` — run in parallel
- `03-strategy/creative-brief` — market research feeds angle selection
