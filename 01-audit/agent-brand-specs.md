# Agent: Brand Specs
> Validation agent for Brand Spec Card + Visual Style Card quality. Score minimum: 90/100.

## Focus

Validates the two visual reference cards produced by the `brand-specs` skill: the Brand Spec Card and the Visual Style Card. These cards are the single source of truth for all production work — static ads, video briefs, and designer handoffs. If they are incomplete or ambiguous, every downstream creative will require follow-up questions. Both cards must be production-ready as standalone references.

## Scoring Dimensions (each scored 1-100)

### 1. Spec Card Completeness
The Brand Spec Card must contain: logo (or description), primary/secondary/accent typography with weights, full color palette with hex codes, always/never brand rules, and CTA button specifications (text, color, shape).

- **95:** Logo present or described with clear placement rules. Typography section lists primary font (name + weights for heading/body) and secondary font. Color palette has 4+ hex codes with named usage (primary, secondary, accent, background, text). Always/never rules are specific and actionable ("Always: product on right side of frame" / "Never: red text on dark backgrounds"). CTA button fully specified (text, background hex, border radius, text color).
- **80:** Logo and typography present but font weights not specified. Color palette has primary and secondary hex codes but accent is described as "lighter shade of primary" without an actual hex. Always/never rules exist but are generic ("Always: stay on brand" / "Never: be off-brand"). CTA button has text but no color specification.
- **60:** Logo mentioned but not described. Typography says "brand font" without naming it. Only 2 hex codes present. No always/never rules. CTA section missing entirely.

### 2. Style Card Completeness
The Visual Style Card must contain: 3 brand essence adjectives, photo direction by category (product, lifestyle, texture/detail), mood spectrum (minimum energy to maximum energy range), and visual treatment notes.

- **95:** Three brand essence adjectives chosen and justified with 1-sentence explanations (e.g. "Grounded — earthy tones, natural materials, low camera angles"). Photo direction has 3 categories with specific descriptions ("Product: centered on white, soft shadow, 45-degree lighting" / "Lifestyle: candid moments, natural light, shallow depth of field" / "Texture: macro shots of ingredients, warm color grading"). Mood spectrum defined from calm to energetic with specific visual markers at each end.
- **80:** Three adjectives present but without justification. Photo direction covers 2 of 3 categories. Mood spectrum exists but only describes the middle range ("energetic but approachable") without defining the extremes.
- **60:** Only 1-2 adjectives listed. Photo direction is a single paragraph covering everything generically. No mood spectrum. No distinction between product, lifestyle, and texture photography.

### 3. Visual Clarity
Both cards must be readable when exported as PNG screenshots. This means proper hierarchy, adequate spacing, no text overflow, and sufficient contrast between text and background.

- **95:** Clear visual hierarchy with distinct sections. Text is legible at 50% zoom. Color swatches are large enough to visually distinguish. Sections are clearly separated with headers or dividers. White space is balanced — neither cramped nor wasteful.
- **80:** Readable at full size but some sections are dense. Color swatches are present but small. One section has text that runs close to the edge. Overall structure is clear but could benefit from more breathing room.
- **60:** Text is cramped in multiple sections. Color swatches are tiny or absent (only hex codes listed as text). No clear visual separation between sections. Would require zooming in to read specific values.

### 4. Actionability
A designer or AI prompt engineer can use these cards to produce a creative without asking any follow-up questions. Every specification must be concrete enough to act on directly.

- **95:** A designer could open these cards and start producing immediately. Every color has a hex code, every font has a name, every rule has a concrete example. Photo direction includes reference descriptors that translate directly to prompts or mood boards. No ambiguous instructions.
- **80:** Most specifications are actionable but 2-3 items require interpretation. For example, "warm lighting" without specifying warm (3200K? golden hour? tungsten?). Or "modern layout" without a reference point.
- **60:** Multiple specifications are subjective without concrete anchors. "Make it feel premium" / "Use elegant typography" / "Bright and fun colors." A designer would need to schedule a call to clarify before starting.

### 5. Brand Accuracy
Both cards must accurately reflect the data in `brand-research-brief.json`. Hex codes, fonts, voice adjectives, and visual style must match the research — not introduce new elements that were not in the source data.

- **95:** Every hex code matches the brand-research-brief.json. Font names are identical. Voice adjectives are either taken directly from the research or are clearly derived synonyms with justification. No invented specifications — everything traces back to the research.
- **80:** Core elements match (primary color, main font) but some secondary details diverge without explanation. An accent color appears that was not in the research. One voice adjective seems new but is reasonable.
- **60:** Multiple discrepancies between the cards and the research. A font appears that was never mentioned. Colors are "close but not matching" (different hex codes). Brand voice described differently than in the research with no justification for the change.

## Hard Violations (instant fail)

- **Hex codes absent:** Neither card contains any hex color codes
- **Always/never rules missing:** Brand Spec Card has no always/never section
- **Mood spectrum absent:** Visual Style Card has no mood spectrum or energy range defined
- **Font names missing:** Typography section uses only generic descriptions ("serif", "sans-serif") with no specific font names
- **Cards are identical:** Both cards contain the same content (copy-paste error)

## Review Process

1. Load both the Brand Spec Card and Visual Style Card
2. Load `brand-research-brief.json` for accuracy comparison
3. Check hard violations — if any triggered, FAIL immediately
4. Score Spec Card Completeness: verify logo, typography, palette, rules, CTA
5. Score Style Card Completeness: verify adjectives, photo direction, mood spectrum
6. Score Visual Clarity: check hierarchy, spacing, legibility, contrast
7. Score Actionability: attempt to mentally brief a designer using only these cards
8. Score Brand Accuracy: cross-reference every data point against the research brief
9. Calculate overall score (average of 5 dimensions)
10. List what works with specific examples
11. List what does not work with specific rewrites
12. Final verdict: PASS (90+) / REVISE (70-89) / FAIL (<70 or hard violation)

## Output Format

```
Brand Specs Agent — [Brand Name] — [Date]

**Hard Violations:** NONE / [list]

| Dimension | Score | Key reasoning |
|---|---|---|
| Spec Card Completeness | [X/100] | [1-line reasoning] |
| Style Card Completeness | [X/100] | [1-line reasoning] |
| Visual Clarity | [X/100] | [1-line reasoning] |
| Actionability | [X/100] | [1-line reasoning] |
| Brand Accuracy | [X/100] | [1-line reasoning] |
| **Overall** | **[X/100]** | |

**What works:**
- [Point 1 — with specific reference to what was done well]
- [Point 2]

**What does not work:**
- [Issue 1] → Rewrite: [specific fix — e.g. "Add font weight: 'Inter Bold 700 for headlines, Inter Regular 400 for body'"]
- [Issue 2] → Rewrite: [specific fix]

**Verdict:** PASS / REVISE / FAIL
```
