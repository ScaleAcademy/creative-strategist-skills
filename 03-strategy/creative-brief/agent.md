# Agent: Creative Brief
> Validation agent for creative brief coherence and production readiness. Score minimum: 90/100.

## Focus

Validates the creative brief output from the `creative-brief` skill. The brief is the central strategic document — nothing goes to production without it. This agent checks that the awareness stage is precisely assigned, the angle (C1-C4) is justified, the target emotion is engineered (not just named), all elements are internally coherent, and the brief contains enough detail for production without follow-up questions.

## Scoring Dimensions (each scored 1-100)

### 1. Awareness Precision
The Schwartz awareness stage must be explicitly assigned with a creative implication — not just labeled. The stage must match the persona data and dictate the angle, hook direction, and CTA friction level.

- **95:** Awareness stage stated with label and number ("Problem Aware — Stage 2"). Justification references specific persona evidence: "She Googles 'why does my back hurt after sitting' but has never searched for an ergonomic chair — she doesn't know a product category exists for her problem." Creative implication is concrete: "We cannot mention the product in the hook. Lead with the problem. Use C1 or C3 angle. CTA should be soft — 'learn more' not 'buy now.'" The stage drives every subsequent decision in the brief.
- **80:** Awareness stage labeled correctly. Justification is reasonable but generic ("she knows she has the problem"). Creative implication exists but does not cascade through the brief — the CTA says "Shop now" despite a Problem Aware assignment.
- **60:** Awareness stage named but feels arbitrary. No justification from persona data. No creative implication. The rest of the brief does not reflect the assigned stage — a Product Aware stage with an education-heavy body and no product mention.

### 2. Angle Justification
The chosen angle (C1 Problem / C2 Result / C3 Education / C4 Identity) must be justified relative to both the persona's awareness stage and their psychological profile. "C1 because it's a pain angle" is not a justification.

- **95:** Angle stated and justified in context: "C1 — Problem angle. Justified: Persona is Problem Aware and her dominant emotion is frustration (Layer 2). She has tried 3 solutions that failed — she needs to feel understood before she'll consider another product. C1 agitates the specific pain of 'nothing works' and positions us as the first to truly diagnose the problem." The justification explains why this angle and not the others.
- **80:** Angle stated and justified but the justification does not address why alternatives were rejected. "C1 because the persona has pain" — correct but incomplete. Does not explain why C3 (education) would not work equally well for this Problem Aware persona.
- **60:** Angle stated without justification. Or justified with a tautology: "C2 — Result angle because we want to show results." No connection to persona psychology, awareness stage, or competitive context.

### 3. Emotional Engineering
The target emotion must be produced by the creative — not just named in the brief. "Target emotion: hope" is naming. "The persona sees a woman her age running a 5K, and the thought 'that could be me' activates aspiration mixed with mild envy" is engineering.

- **95:** The brief describes the emotional sequence: "First, recognition (she sees herself in the situation). Then, agitation (the pain intensifies as we name what she couldn't articulate). Then, relief (the solution exists and it's simpler than she thought). The CTA captures the relief moment — 'start here.'" The emotional arc is specific to this persona and this pain. A reader feels the intended emotion while reading the brief.
- **80:** Target emotion named and supported with a general mechanism: "We want her to feel frustrated, so we'll show the problem getting worse." The emotion is identified and the approach is reasonable, but the brief does not describe the specific moment where the emotion activates. It names the emotion and describes a general tactic, not a precise trigger.
- **60:** Target emotion is listed as a single word in a field: "Emotion: hope." No description of how the creative produces this emotion. No emotional arc. The brief treats emotion as metadata rather than the core design principle.

### 4. Internal Coherence
The hook direction, visual concept, body message, and CTA must all serve the same strategic intention. An education hook with a fear-based visual and a "Buy now" CTA is incoherent.

- **95:** Every element traces back to the strategic anchor. Hook direction (curiosity gap via education) matches the C3 angle. Visual concept (diagram showing the hidden cause) supports the education mechanic. Body delivers the "aha moment." CTA ("See how it works") matches the Solution Aware transition intent. A reader can draw a straight line from awareness stage through angle through mechanic through hook through visual through CTA.
- **80:** Core elements are coherent (hook and angle align, CTA matches awareness) but one element is slightly off. For example, the visual concept is "lifestyle aspiration" while the angle is C1 (problem) — the visual should show the problem, not the aspiration. The misalignment is fixable with one change.
- **60:** Multiple elements conflict. Hook is pain-focused (C1) but the body is education-heavy (C3) and the CTA is urgency-driven ("Limited time" — Most Aware tactic). The brief reads like three different strategies stitched together. A production team would need to ask which direction to follow.

### 5. Production Readiness
The brief must contain enough detail for a designer, editor, or AI prompt engineer to produce the creative without follow-up questions. Format, ratio, style, duration, copy zones, and constraints must all be specified.

- **95:** Format specified (e.g. "F12 — Headline Static"). Ratio and dimensions stated ("9:16, 1080x1920"). Style template referenced ("Style B — Lifestyle context with headline"). Copy zones filled: headline (exact text, word count verified), subtitle (exact text), CTA (exact text and color). Visual direction described concretely ("30-year-old woman in a modern kitchen, morning light, looking at phone with frustrated expression, cluttered counter with supplements in background"). Constraints listed ("No before/after claims — compliance"). A producer can start immediately.
- **80:** Format, ratio, and style defined. Copy zones have draft text but word counts are not verified against template limits. Visual direction is described but generically ("lifestyle setting, natural feel"). A producer can start but will need to make 2-3 interpretation decisions.
- **60:** Format mentioned ("static ad") but no specific template, ratio, or dimensions. Copy is "to be written by hook-writing skill" — the brief delegates rather than specifying. Visual direction is "on brand." A producer cannot start without a follow-up call.

## Hard Violations (instant fail)

- **Awareness stage absent:** No Schwartz awareness stage assigned anywhere in the brief
- **Angle not justified:** C1/C2/C3/C4 is named but has zero justification connecting it to the persona or awareness stage
- **Emotion only named, not engineered:** The brief contains only a single-word emotion label with no description of how the creative produces it
- **No strategic anchor:** The brief lacks the "This brief targets [Persona X] suffering from [Pain Y] at awareness level [Z]" statement or equivalent
- **Copy-paste brief:** The brief is clearly a template with fields unfilled or filled with placeholder text ("[insert here]", "TBD")

## Review Process

1. Load the creative brief
2. Check hard violations — if any triggered, FAIL immediately
3. Locate the strategic anchor — is the persona x pain x awareness combination stated?
4. Evaluate awareness precision — is the stage justified and creatively interpreted?
5. Evaluate angle justification — does the C1-C4 choice follow from the persona and awareness?
6. Evaluate emotional engineering — does the brief describe how the emotion is produced?
7. Test internal coherence — draw a line from awareness through angle through hook through visual through CTA
8. Test production readiness — could a producer start work today with only this brief?
9. Calculate overall score (average of 5 dimensions)
10. List what works with specific examples
11. List what does not work with specific rewrites
12. Final verdict: PASS (90+) / REVISE (70-89) / FAIL (<70 or hard violation)

## Output Format

```
Creative Brief Agent — [Brand] — [Brief ID] — [Date]

**Hard Violations:** NONE / [list]

| Dimension | Score | Key reasoning |
|---|---|---|
| Awareness Precision | [X/100] | [1-line reasoning] |
| Angle Justification | [X/100] | [1-line reasoning] |
| Emotional Engineering | [X/100] | [1-line reasoning] |
| Internal Coherence | [X/100] | [1-line reasoning] |
| Production Readiness | [X/100] | [1-line reasoning] |
| **Overall** | **[X/100]** | |

**What works:**
- [Point 1 — with specific reference to brief content]
- [Point 2]

**What does not work:**
- [Issue 1] → Rewrite: [specific fix — e.g. "The CTA 'Buy Now' contradicts the Problem Aware assignment. Change to 'See why it happens' to match C3 education angle and Stage 2 awareness"]
- [Issue 2] → Rewrite: [specific fix]

**Verdict:** PASS / REVISE / FAIL
```
