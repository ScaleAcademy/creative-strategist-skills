# Agent: Audience Research
> Validation agent for Persona Deep Dive Layer 1/2/3. Score minimum: 90/100.

## Focus

Validates the Persona Deep Dive output from the `audience-research` skill. The persona must cover all three layers (demographic, psychographic, micro-moments), map to at least 2 LF8 innate desires, assign a Schwartz awareness stage, and include raw verbatims. A validated persona is specific enough that a copywriter can write a hook for this exact person without additional research.

## Scoring Dimensions (each scored 1-100)

### 1. Layer Coverage
All three layers must be present and substantive. Layer 1 (demographic) provides the facts. Layer 2 (psychographic) reveals the motivations. Layer 3 (micro-moments) captures the exact situations where the pain is most acute.

- **95:** Layer 1 includes age range, gender split, income bracket, location type, job title or industry, family status. Layer 2 includes values, fears, aspirations, identity statements ("I'm the kind of person who..."), media consumption habits, and trust sources. Layer 3 includes 3+ specific micro-moments with situational detail ("It's 11pm, she's scrolling Instagram after putting the kids to bed, sees a friend's vacation photo, and feels a wave of 'I never do anything for myself'").
- **80:** All three layers present. Layer 1 is complete. Layer 2 covers values and fears but misses identity statements or media habits. Layer 3 has 1-2 micro-moments but they are described generally ("feels stressed at work") rather than cinematically.
- **60:** Layer 1 and Layer 2 present but Layer 3 is a single sentence or a list of emotions without situational context. Layer 2 reads like a marketing brief ("health-conscious millennials who value authenticity") rather than a psychological portrait.

### 2. LF8 Mapping
At least 2 of Whitman's 8 innate desires (Life Force 8) must be explicitly identified and justified with evidence from the persona's psychology. The mapping should explain why this desire is activated, not just name it.

- **95:** 2-3 LF8 desires identified with clear justification. Example: "LF8 #3 — Freedom from fear, pain, and danger: Justified by Layer 3 micro-moment where persona reads ingredient labels obsessively after a health scare. The fear is not abstract — it manifests in daily scanning behavior." Each desire links back to specific persona data.
- **80:** 2 LF8 desires identified and named correctly. Justification exists but is surface-level: "LF8 #8 — Social approval: the persona wants to look good." The connection to specific persona behavior or verbatim is missing.
- **60:** 1 LF8 desire named without justification, or desires are listed as a checklist without explanation of why they apply to this specific persona. Feels copy-pasted from a template.

### 3. Awareness Assignment
A Schwartz awareness stage must be explicitly assigned with justification explaining why this persona is at this stage — not another. The assignment must include creative implications (what this means for how we speak to them).

- **95:** Awareness stage clearly stated: "Problem Aware — Stage 2." Justification cites specific evidence: "She knows her skin is aging faster than her peers (problem recognized) but has tried 3 moisturizers that didn't work and doesn't believe another product will be different (not yet solution aware). She's searching 'why does my skin look tired' not 'best anti-aging serum.'" Creative implication stated: "Lead with the problem, not the product. Use education angle (C3) to shift her to Solution Aware."
- **80:** Awareness stage assigned with a correct label and a general justification ("She's Problem Aware because she knows she has the problem but hasn't found a solution"). Creative implication is present but generic ("speak to the pain first").
- **60:** Awareness stage named but no justification. Or the stage is assigned incorrectly — for example, calling someone "Unaware" when the persona description clearly states they are actively searching for solutions. No creative implication.

### 4. Verbatim Quality
Raw verbatims must be present — actual words from real people in the target audience. These are not paraphrases, summaries, or AI-generated quotes. They must sound like a real person typed or said them, complete with informal grammar, slang, or emotional language.

- **95:** 5+ raw verbatims sourced from real platforms (Reddit, Amazon reviews, Facebook comments, forums). Each is attributed ("Reddit r/SkincareAddiction, March 2026"). Verbatims include emotional language, informal grammar, and specific details that could not be fabricated: "honestly i gave up on finding something that actually works. spent like $400 on serums last year and my skin looks the same. my dermatologist just wants to sell me retinol."
- **80:** 3-4 verbatims that sound authentic but lack source attribution. Language is natural but slightly cleaned up (perfect punctuation, complete sentences). Still useful for hook writing but the raw edge is softened.
- **60:** Verbatims read like AI-generated placeholder quotes: "I've been struggling to find a product that truly meets my needs." Too polished, too generic, no specific details. Could apply to any product in any category.

### 5. Actionability
The persona must be specific enough that a copywriter can immediately write a hook targeting this exact person. Test: can you write a first line of an ad that would make this persona stop scrolling? If the persona is too broad, you cannot.

- **95:** Reading the persona, a specific person comes to mind. You could describe what they look like, what app they are scrolling, what they just searched on Google. A copywriter could write 5 different hooks from this persona without additional research. The micro-moments are so specific they are practically hook starters.
- **80:** The persona is specific enough to target but would benefit from one more layer of detail. A copywriter could write 2-3 hooks but would need to make assumptions for the rest. The general direction is clear but the micro-moments need sharpening.
- **60:** The persona describes a demographic segment, not a person. "Women 25-45 who care about their health" is a segment. A copywriter reading this would ask "but who specifically?" before writing anything. Hooks written from this persona would be generic.

## Hard Violations (instant fail)

- **Layer 3 absent:** No micro-moments section at all, or micro-moments are just a list of emotions without situational context
- **No raw verbatim:** Zero actual customer quotes — only paraphrases or summaries
- **Awareness stage not assigned:** No explicit Schwartz awareness stage label anywhere in the persona
- **Contradictory data:** Layer 2 psychographics contradict Layer 1 demographics (e.g. "budget-conscious" persona with "$200k+ income and luxury lifestyle")
- **Single-source persona:** All data comes from a single source with no cross-referencing (entire persona built from one Reddit thread)

## Review Process

1. Load the Persona Deep Dive document
2. Check hard violations — if any triggered, FAIL immediately
3. Verify Layer 1 presence and completeness (demographic data)
4. Verify Layer 2 presence and depth (psychographic portrait)
5. Verify Layer 3 presence and specificity (micro-moments with cinematic detail)
6. Check LF8 mapping — are innate desires named, justified, and linked to persona data?
7. Check awareness assignment — is the stage labeled, justified, and creatively interpreted?
8. Evaluate verbatim quality — do quotes sound like real people?
9. Test actionability — could you write a hook right now from this persona alone?
10. Calculate overall score (average of 5 dimensions)
11. List what works with specific examples
12. List what does not work with specific rewrites
13. Final verdict: PASS (90+) / REVISE (70-89) / FAIL (<70 or hard violation)

## Output Format

```
Audience Research Agent — [Persona Name] — [Brand] — [Date]

**Hard Violations:** NONE / [list]

| Dimension | Score | Key reasoning |
|---|---|---|
| Layer Coverage | [X/100] | [1-line reasoning] |
| LF8 Mapping | [X/100] | [1-line reasoning] |
| Awareness Assignment | [X/100] | [1-line reasoning] |
| Verbatim Quality | [X/100] | [1-line reasoning] |
| Actionability | [X/100] | [1-line reasoning] |
| **Overall** | **[X/100]** | |

**What works:**
- [Point 1 — with specific example from the persona]
- [Point 2]

**What does not work:**
- [Issue 1] → Rewrite: [specific fix — e.g. "Replace the generic micro-moment 'feels stressed about skin' with a situational scene: 'She catches her reflection in the bathroom mirror at 7am, notices the lines around her eyes are deeper than last month, and thinks: I look 10 years older than I am'"]
- [Issue 2] → Rewrite: [specific fix]

**Verdict:** PASS / REVISE / FAIL
```
