# Headline

## What this format is

The most common static format. A single dominant headline carries the entire message. The visual and the headline work together as equal partners -- neither makes sense without the other. This format wins through compression: one idea, stated perfectly, with an image that amplifies it.

## Styles

### Style A: Product hero with headline

The product commands the frame. The headline gives the viewer a reason to care about what they're looking at. Clean, direct, commercial.

#### Copy template
```
[HEADLINE]    - 3-12 words. One core idea. Must work as a standalone statement.
                If you covered the image, the headline alone should make someone curious.

[SUBHEAD]     - Optional. 5-15 words. Adds a new dimension: proof, specificity, or urgency.
                Must not repeat the headline.

[CTA]         - Optional. 2-5 words.
```

#### Image generation prompt
```
Create a static ad for [BRAND NAME]'s [PRODUCT NAME]. [ASPECT RATIO].

COMPOSITION:
One continuous image filling the entire frame. The brand's product from the uploaded product reference image is the visual hero, positioned [PRODUCT POSITION from variation selection] and occupying roughly 40-60% of the visual frame. The product should be beautifully lit and accurately represented.

The headline "[HEADLINE]" is rendered as the dominant text element, positioned [TEXT POSITION from variation selection]. The headline and the product should feel like they're in conversation -- the headline explains what the product delivers, and the product proves the headline is real.

[If SUBHEAD present]: Render "[SUBHEAD]" directly below or near the headline at roughly 40-50% of the headline's visual weight. It should feel like a natural continuation, not a separate element.

[If CTA present]: Render "[CTA]" styled per the brand spec sheet's CTA treatment rules at the bottom of the frame.

TYPOGRAPHY:
Reference the uploaded brand spec sheet for all fonts, weights, and colors. The headline should use the brand's headline font at a size that balances with the product -- large enough to be the first or second thing the eye reads, but not so large it overwhelms the product.

SAFE ZONES:
Top [TOP SAFE ZONE]px and bottom [BOTTOM SAFE ZONE]px of the frame kept clear of critical content. The headline should not be placed where platform UI elements would obscure it.

COLOR AND TREATMENT:
Background should use colors from the brand spec sheet. The product and headline both need clear contrast against the background. [BACKGROUND from variation selection]. Lighting should be [LIGHTING from variation selection].

BRAND IDENTITY:
Logo per brand spec sheet rules (optional -- include only when the ad needs brand identification at first glance).

PHOTOGRAPHY DIRECTION:
[PHOTOGRAPHY DIRECTION from brand brief]. The product must look premium and desirable. This is a commercial image first and foremost.

MOOD:
[ENERGY from variation selection]. The overall feeling should be: one idea, perfectly executed.
```

#### Variation vectors
**Product position**: center with headline above | left side with headline right | bottom half with headline top | angled/dynamic positioning | flat lay from above

**Text position**: top third of frame | overlaid on a clean area of the image | bottom third above CTA | centered vertically beside product

**Background**: solid brand color | lifestyle context related to the persona | clean white/neutral surface | textured surface from brand world | environmental setting

**Lighting**: soft natural light with gentle shadows | studio lighting, clean and commercial | warm golden hour | bright and even | dramatic with contrast

**Energy**: confident and direct | warm and inviting | bold and attention-grabbing | premium and restrained | playful and energetic

---

### Style B: Lifestyle context with headline

A person or scene using/experiencing the product. The headline provides the meaning layer that turns a lifestyle image into an argument. The viewer sees themselves in the scene; the headline tells them why they should want to be there.

#### Copy template
```
[HEADLINE]    - 3-12 words. Should resonate with the persona's identity or desire.
                The "photograph test" applies: if you read this headline, you should
                picture the exact person it's for.

[SUBHEAD]     - Optional. 5-15 words.

[CTA]         - Optional. 2-5 words.
```

#### Image generation prompt
```
Create a static ad for [BRAND NAME]'s [PRODUCT NAME]. [ASPECT RATIO].

COMPOSITION:
One continuous image filling the entire frame. Show a scene that the target persona ([PERSONA SUMMARY]) would immediately recognize as their life or aspiration. The brand's product should be present in the scene naturally -- being used, held, or visible in context. The product should not feel staged or forced.

The headline "[HEADLINE]" is rendered as text overlay, positioned [TEXT POSITION from variation selection] in an area of the image with enough visual calm to maintain legibility. The headline should feel like it's speaking directly to the person in the scene -- or directly to the viewer who sees themselves in that scene.

[If SUBHEAD present]: "[SUBHEAD]" rendered below the headline at secondary scale.

[If CTA present]: "[CTA]" styled per brand spec sheet at the bottom.

TYPOGRAPHY:
Reference the uploaded brand spec sheet. The headline font and color must maintain legibility against the lifestyle imagery. If the image area behind the text is busy, use a subtle text treatment (slight shadow, semi-transparent backing, or place text in a naturally calm area of the composition) to ensure readability without adding heavy graphic overlays.

SAFE ZONES:
Top [TOP SAFE ZONE]px and bottom [BOTTOM SAFE ZONE]px clear. Headlines should avoid the extreme edges of the frame.

COLOR AND TREATMENT:
The scene should feel authentic and aspirational, not stock-photo generic. Color grading should align with the brand's visual world from the spec sheet. The product should be recognizable but not artificially highlighted.

BRAND IDENTITY:
Logo per brand spec sheet rules (optional -- include only when the ad needs brand identification at first glance).

PHOTOGRAPHY DIRECTION:
[PHOTOGRAPHY DIRECTION from brand brief]. The scene should feel candid and real, as if captured in the moment rather than staged. The persona ([PERSONA SUMMARY]) should see this image and think "that's me" or "that's who I want to be."

MOOD:
[ENERGY from variation selection].
```

#### Variation vectors
**Text position**: top third | bottom third | left-aligned with image right | centered overlay on calm area

**Scene context**: morning routine | outdoor/active | social gathering | quiet personal moment | work/productivity

**Energy**: aspirational and warm | confident and direct | relatable and casual | premium and elevated | energetic and dynamic

---

### Style C: Typography-dominant

Minimal or no imagery. The headline IS the creative. The words, set in the brand's typography at scale, are the visual. Works when the headline is strong enough to carry the entire ad alone.

#### Copy template
```
[HEADLINE]    - 3-10 words. Must be powerful enough to be the entire visual.
                Short, punchy, and rhythmic. Every word earns its place.

[SUBHEAD]     - Optional. 5-15 words. Secondary scale.

[CTA]         - Optional. 2-5 words.
```

#### Image generation prompt
```
Create a static ad for [BRAND NAME]'s [PRODUCT NAME]. [ASPECT RATIO].

COMPOSITION:
One continuous image filling the entire frame. This is a typography-driven ad where the headline "[HEADLINE]" is the dominant visual element, occupying the center of the frame at maximum scale. The words themselves are the creative -- they should feel like a bold statement, a declaration, or a provocation.

The brand's product from the uploaded product reference image may appear [PRODUCT TREATMENT from variation selection] -- small in a corner, at the bottom, or entirely absent if the headline alone carries the message. The product is secondary to the statement.

[If SUBHEAD present]: "[SUBHEAD]" rendered below the headline at clearly secondary scale.

[If CTA present]: "[CTA]" at the bottom per brand spec sheet rules.

TYPOGRAPHY:
Reference the uploaded brand spec sheet. The headline should be rendered in the brand's most impactful headline font at the largest feasible scale. [TYPE TREATMENT from variation selection]. The typography itself should feel intentional and designed, not just text placed on a background.

SAFE ZONES:
Top [TOP SAFE ZONE]px and bottom [BOTTOM SAFE ZONE]px clear.

COLOR AND TREATMENT:
Background should be [BACKGROUND from variation selection]. The headline color should create maximum contrast and impact. Keep the palette tight -- this is about the power of the words and the brand's visual identity, not decorative elements.

BRAND IDENTITY:
Logo per brand spec sheet rules (optional -- include only when the ad needs brand identification at first glance).

MOOD:
[ENERGY from variation selection]. The feeling should be: these words demanded to be said in this way.
```

#### Variation vectors
**Product treatment**: small in bottom-right corner | small centered below headline | absent entirely | subtly integrated into background

**Type treatment**: all caps (if brand guidelines allow) | mixed case with key word emphasized through size | stacked with line breaks for rhythm | single line at maximum width

**Background**: solid brand primary color | solid brand accent color | black or very dark | white or very light | textured surface

**Energy**: bold and declarative | quiet and confident | provocative and edgy | warm and personal | minimal and sophisticated

---

## Global rules for headline format

### Visual-headline coherence (CRITICAL)

The image must visually reinforce the headline's concept — not just accompany it. If the headline makes a claim, paints a picture, or names a scenario, the image must SHOW that claim, picture, or scenario. A generic product-on-dark-background shot fails this test unless the headline is itself generic (which it shouldn't be).

**The coherence test:** Cover the headline. Does the image alone hint at the same idea? Cover the image. Does the headline alone conjure a visual that matches? If both answers are yes, the ad has coherence. If either answer is no, the visual and headline are working independently — which means the ad is working at half power.

**Examples:**
- Headline: "Your Morning Shouldn't Start with a Fight." (coffee brand) → Image must show the frustrating morning scenario, not just a coffee cup on marble. The "fight" is the concept and it must be visible.
- Headline: "Finally, a Bag You Don't Hide at Check-In." (luggage brand) → Image should show the bag in an airport or travel context as a statement piece, not on a white studio backdrop.
- Headline: "10,000 Five-Star Reviews. Zero Returns." → Image should emphasize durability or satisfaction -- the product in pristine condition after visible use, or multiple happy contexts.
- Headline: "Stop Rebooking. Start Arriving." (travel brand) → Image should show the contrast between chaos and calm -- not just a destination photo.

**When the headline contains a metaphor, scene, or narrative (e.g., "graveyard," "fight," "stop rebooking"), the image must stage that metaphor, scene, or narrative literally.** The visual is not a decoration — it is the other half of the argument.

### Agent 7: Copy Editor / Proofreader (REQUIRED)

Every ad brief must pass through a dedicated copy-editing agent before final approval. This agent checks ONLY for mechanical correctness -- it is not a strategy or creative review. It has veto power: any error it finds blocks approval regardless of other agents' scores.

**Checklist:**
1. **Grammar**: Subject-verb agreement, tense consistency, dangling modifiers, pronoun-antecedent agreement. Every headline is a sentence -- it must be grammatically correct even if it uses fragments for style.
2. **Spelling**: Every word checked. Brand names verified against official capitalization and spacing (e.g., if the brand uses "ProCook" not "Procook" or "pro-cook").
3. **Punctuation**: Periods, commas, apostrophes, quotation marks. Verify possessives vs. plurals. Verify contractions.
4. **Banned characters**: NO em dashes (--). Use hyphens (-) for compound words only. If a pause is needed, use a period, comma, or ellipsis. NO en dashes. NO semicolons in headlines.
5. **Number consistency**: Dollar signs, decimals, and commas in numbers must follow a single convention throughout the brief. Use whole dollars (e.g., "$49") not "$49.00" unless cents matter.
6. **Duplicate content**: The same data point (price, stat, claim) must not appear in more than one text element. If the price is in the headline, it cannot also appear as a separate price display.
7. **Word count compliance**: Every text element must be recounted against the format spec limits. No rounding, no "close enough."
8. **Brand name capitalization**: Verified against the brand's official usage in every instance.

**Scoring**: Pass/Fail. Any single error is a fail. The agent must list every error found with the exact text, the rule violated, and the corrected version.

### Price is not a default element

Price is not a default element. Include price only when the context makes sense for the specific execution. Not every ad needs a price. Adding price to every ad dilutes its impact and adds unnecessary copy.

### Fewer elements by default

Default to fewer elements, not more. Every text element must earn its place. If removing an element does not weaken the ad, remove it. Optional slots (CTA, headline, price, logo) should be left empty unless they meaningfully strengthen the specific execution.

### What to avoid
- Headlines that could apply to any product in the category
- Product and headline fighting for attention (one leads, one supports)
- Text placed over busy image areas without sufficient contrast
- Subheads that repeat the headline in different words
- Generic lifestyle imagery that doesn't connect to the specific persona
- **Product-on-dark-background shots that could work with ANY headline (visual-headline disconnect)**
- **Visuals that illustrate the product but not the headline's concept**
