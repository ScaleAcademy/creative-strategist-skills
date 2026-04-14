---
name: customer-reality
description: "Maps the emotional reality of the target persona: dominant emotion, private vs social pain, acute vs chronic pain, and triggering micro-moments. Use after review-audit and audience-research to go deeper than demographics. Trigger on: 'emotional mapping', 'micro-moments', 'customer reality', 'what the audience really feels'. Produces an emotional map that directly informs hook direction and creative tone."
metadata:
  version: 1.0.0
  status: stable
  tags: [research, emotion, micro-moments, persona, psychology]
  inputs: [persona-[name].md, verbatim library (review-audit)]
  outputs: [emotional-map-[persona].md — full emotional mapping]
  depends-on: [brand-guidelines, audience-research, review-audit]
---

# Customer Reality

## Before Starting

Confirm before starting:
- [ ] `persona-[name].md` available (audience-research completed)
- [ ] Verbatim library available (review-audit completed) or at least 10 raw verbatims
- [ ] Product and usage context clearly defined

This skill produces nothing of value without real persona data. Do not improvise emotions — extract them.

---

## Phase 1: Identify the Dominant Emotion

From the verbatims in Bucket 1 (pains) and Bucket 4 (transformations), identify the most present emotion.

**Emotions to detect:**

| Emotion | Verbatim signals |
|---|---|
| Frustration | "I'm fed up", "I tried everything", "nothing works" |
| Fear | "I'm afraid that", "what if", "I risk" |
| Shame | "I don't dare talk about it", "people think that" |
| Hope | "I would love so much", "I dream of", "if only" |
| Anger | "it's outrageous", "nobody tells the truth" |
| Confusion | "I don't understand why", "everyone says X but" |
| Resignation | "I've learned to live with it", "that's just how it is" |

For full mapping: See [references/emotional-mapping.md](references/emotional-mapping.md)

---

## Phase 2: Qualify the Pain

### Q2A — Private or Social?

**Private pain:** Experienced in silence. The person doesn't talk about it.
→ Tone: intimate, confidential. Formats: text overlay, calm voiceover, face-to-camera confession.

**Social pain:** Linked to others' perception. The person fears judgment.
→ Tone: supportive, non-judgmental. Formats: testimonial, community, "you're not alone."

**Signals in verbatims:**
- "I / me" pronouns = private
- Mentions of "people / my circle / my family / at work" = social

### Q2B — Acute or Chronic?

**Acute pain:** Recently triggered. Intense and urgent.
→ Time indicators: "this morning", "last week", "since the accident"
→ Hook: anchor in the precise moment. Natural urgency.

**Chronic pain:** Present for a long time. Normalized, almost accepted.
→ Indicators: "always", "I've learned to live with it", "it's always been like this"
→ Hook: reveal that it's not inevitable. "You don't have to keep..."

---

## Phase 3: Identify the Triggering Micro-Moment

Extract from Bucket 2 (triggers) the most frequent or most intense micro-moment.

**4 types of micro-moments:**
1. **Breaking point** — an event triggered everything ("the day I realized that...")
2. **Recurring** — a regular loop ("every Monday morning", "at the end of every month")
3. **Comparison** — a perceived gap ("my colleague had just bought...", "I saw that X...")
4. **Anticipation** — a projected fear ("if this continues in 5 years...")

For the full framework: See [references/micro-moments.md](references/micro-moments.md)

---

## Phase 4: Derive the Creative Direction

From the mapping, formulate:
- The appropriate tone (intimate / collective / urgent / educational)
- The recommended format
- The hook direction (emotional vs situational vs identity opening)
- The confirmed or revised awareness stage

---

## Output Format

```markdown
# Emotional Map — [Persona] — [Product] — [Date]

## Dominant Emotion
[Emotion] — [2 verbatims that confirm it]

## Pain Qualification
- Private or Social: [Private / Social] — [Reason]
- Acute or Chronic: [Acute / Chronic] — [Reason]

## Main Micro-Moment
Type: [Breaking point / Recurring / Comparison / Anticipation]
Description: [Specific situation]
Associated verbatim: "[Exact quote]"

## Creative Direction
→ Tone: [intimate / collective / urgent / educational]
→ Recommended format: [format or type]
→ Hook direction: [description of the opening]
→ Confirmed awareness: [Level 1–5]
→ Recommended mechanic: [M1–M8]
```

---

## Related Skills

- `02-research/review-audit` — verbatim source
- `02-research/audience-research` — persona source
- `03-strategy/creative-brief` — emotional map → brief angle and tone
- `03-strategy/hook-writing` — micro-moment → first line of the hook
