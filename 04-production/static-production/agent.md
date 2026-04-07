# Agent: Static Production
> Validation agent for Nano Banana prompt before image generation. Score minimum: 90/100.

## Focus

Validates the Nano Banana image generation prompt and designer brief before execution. Nano Banana (NB2) is a zero-assumption image generator — if a detail is not in the prompt, it will not appear in the image. This agent ensures safe zones are specified, the prompt has sufficient depth, spec cards are referenced, copy complies with word counts, and the visual concept reinforces the headline concept. Catching errors here saves generation credits and iteration cycles.

## Scoring Dimensions (each scored 1-100)

### 1. Safe Zones
On a 1080x1920 canvas (9:16), the top 270px and bottom 340px are covered by platform UI elements (username, caption, CTA overlay). Critical content — faces, headline text, product — must not fall in these zones. The prompt must explicitly address safe zone placement.

- **95:** Prompt explicitly states: "Keep the top 270px and bottom 340px clear of critical content. Main subject positioned in the center-to-upper-center zone (y: 270-1580px). Headline text placed between y: 400-900px. CTA and logo positioned above the 1580px line." Safe zones are treated as a hard constraint, not a suggestion. Specific pixel ranges referenced.
- **80:** Prompt mentions safe zones generally: "Leave space at the top and bottom for platform UI." No pixel values specified. The intent is correct but a literal-minded image generator might not leave enough space. The designer brief includes safe zone markings but the AI prompt does not.
- **60:** No mention of safe zones anywhere in the prompt. The main subject could end up behind the username overlay or the CTA button. The prompt assumes the generator knows about platform constraints — NB2 does not.

### 2. Prompt Depth
NB2 makes zero assumptions. An 800-1000 word prompt is the minimum for consistent results. Every visual element must be described: subject, position, expression, lighting, color palette, background, texture, text placement, brand elements, mood, and camera angle.

- **95:** Prompt is 800-1000+ words. Every element explicitly described. Subject has: position in frame, body language, facial expression, clothing color and style, skin tone, age markers. Background has: setting, depth of field, color palette, time of day, atmospheric elements. Lighting specified: direction, quality (soft/hard), color temperature. Text has: exact content, font style, size relative to frame, color, position, shadow/outline if any. Mood described with specific references ("the warmth of a Wes Anderson interior scene, not a clinical product shot").
- **80:** Prompt is 500-799 words. Major elements described but some rely on implications. Subject described in detail but background says "clean, modern kitchen" without specifying lighting, color palette, or depth of field. NB2 will fill these gaps with its defaults, which may not match brand specs. Prompt is functional but will likely need 1-2 regeneration cycles.
- **60:** Prompt is under 400 words. Multiple elements left undescribed. "A woman holding the product in a bright setting with the headline text visible." NB2 will make assumptions about everything: the woman's age, clothing, expression, the setting's color palette, the text's font and position. Results will be unpredictable.

### 3. Spec Card Reference
The Brand Spec Card and Visual Style Card must be explicitly referenced in the prompt. This means: hex codes used for colors, font names used for text, mood spectrum position identified, and brand rules (always/never) respected.

- **95:** Prompt references both cards by name. Hex codes from the Spec Card used for text color, background accents, and CTA button. Font names specified for headline and body text. Visual Style Card's mood spectrum position stated ("this creative sits at 7/10 energy on the brand's calm-to-energetic spectrum"). Always/never rules explicitly respected ("per brand guidelines: product always on right side, never use red as a background color"). Photo direction from Style Card reflected in the visual description.
- **80:** One card referenced explicitly. Hex codes present for primary brand color but secondary and accent colors described by name rather than hex ("a light blue accent" instead of "#A8D8EA"). Font name mentioned for headline but not for body text. Brand rules followed but not explicitly cited.
- **60:** Neither card referenced. Colors described generically ("brand colors"). No hex codes in the prompt. Font described as "brand font" or "clean sans-serif." The prompt could produce an image in any brand's visual identity — there is nothing anchoring it to this specific brand.

### 4. Copy Compliance
Every copy zone must respect the word count limits defined by the format template. For headline-style statics: headline 3-12 words, subtitle 5-20 words, CTA 2-5 words. Word counts must be verified before generation.

- **95:** Each copy zone lists the exact text with word count noted in parentheses. "Headline: 'The ingredient your serum is hiding' (6 words — within 3-12 limit)." "Subtitle: 'One $3 switch that changed everything for 147K women' (9 words — within 5-20 limit)." "CTA: 'See the ingredient' (3 words — within 2-5 limit)." All counts verified and within spec. No zone exceeds its limit.
- **80:** Copy text present for all zones. Word counts are within limits but not explicitly verified in the prompt. The copywriter would need to count manually. All text is reasonable length but the precision check is missing.
- **60:** Copy text present but at least one zone exceeds its limit. Headline is 15 words (limit is 12). Or the CTA is a full sentence: "Click here to discover our revolutionary new approach to skincare" (10 words, limit is 5). No word count verification present.

### 5. Visual-Headline Coherence
The image concept must reinforce the headline concept. If the headline says "The hidden ingredient," the image should create visual curiosity about something hidden — not show a generic product shot. The visual and the text must tell the same story from two angles.

- **95:** Visual and headline create a unified concept. Headline: "Your trainer's secret recovery hack." Visual: close-up of a gym bag with a mysterious product half-visible, surrounded by familiar gym items. The visual raises the same question the headline does — what is the secret? A "cover test" passes both ways: covering the headline, the image alone makes you curious; covering the image, the headline alone makes you curious. Together they amplify each other.
- **80:** Visual and headline are related but the connection is loose. Headline: "Your trainer's secret recovery hack." Visual: a woman stretching after a workout. The visual is on-topic (fitness) but does not reinforce the "secret" concept. The image could accompany many different headlines about fitness. It supports but does not amplify.
- **60:** Visual and headline tell different stories. Headline: "Your trainer's secret recovery hack." Visual: a flat-lay product shot on a white background. The headline creates intrigue; the image is a generic product display. There is no conceptual link. The visual could be used with any headline about this product.

## Hard Violations (instant fail)

- **Safe zones not mentioned:** No reference to safe zones, platform UI constraints, or content-free margins anywhere in the prompt
- **Prompt under 400 words:** Prompt is too thin for NB2 to produce reliable results
- **No spec card reference:** Neither Brand Spec Card nor Visual Style Card referenced, and no hex codes or font names present in the prompt
- **Text baked into image without instruction:** Prompt asks for text in the image but gives no font, size, color, or position specifications
- **Wrong ratio:** Prompt specifies a ratio that does not match the brief (e.g. brief says 9:16 but prompt describes a square composition)

## Review Process

1. Load the Nano Banana prompt and designer brief
2. Load the validated creative brief for cross-reference
3. Check hard violations — if any triggered, FAIL immediately
4. Check safe zones: are top 270px and bottom 340px explicitly protected?
5. Count prompt word length — is it 800+ words?
6. Check spec card references: are hex codes and font names present?
7. Verify copy zone word counts against template limits
8. Run the coherence test: cover the headline — does the image alone tell the story? Cover the image — does the headline alone work? Together, do they amplify?
9. Calculate overall score (average of 5 dimensions)
10. List what works with specific examples
11. List what does not work with specific rewrites
12. Final verdict: PASS (90+) / REVISE (70-89) / FAIL (<70 or hard violation)

## Output Format

```
Static Production Agent — [Brand] — [Creative ID] — [Date]

**Hard Violations:** NONE / [list]

| Dimension | Score | Key reasoning |
|---|---|---|
| Safe Zones | [X/100] | [1-line reasoning] |
| Prompt Depth | [X/100] | [word count] words — [1-line reasoning] |
| Spec Card Reference | [X/100] | [1-line reasoning] |
| Copy Compliance | [X/100] | [1-line reasoning] |
| Visual-Headline Coherence | [X/100] | [1-line reasoning] |
| **Overall** | **[X/100]** | |

**What works:**
- [Point 1 — with specific reference to prompt content]
- [Point 2]

**What does not work:**
- [Issue 1] → Rewrite: [specific fix — e.g. "Add safe zone constraint: 'Position headline text between y:400-900px. Keep subject's face above y:270px. No critical elements below y:1580px.'"]
- [Issue 2] → Rewrite: [specific fix]

**Verdict:** PASS / REVISE / FAIL
```
