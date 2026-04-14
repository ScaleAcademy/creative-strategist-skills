---
name: hook-writing
description: "Writes 10 psychologically-driven hooks calibrated to a specific awareness stage, persona, and creative mechanic. Use after creative-brief is validated. Trigger on: 'write hooks', 'generate hooks', 'first line of the ad', 'hook for [persona]'. Produces a scored hook bank ready for brief integration or direct testing."
metadata:
  version: 1.1.0
  status: stable
  tags: [strategy, hooks, copywriting, psychology, awareness]
  inputs: [validated creative-brief, persona-[name].md, emotional-map-[persona].md]
  outputs: [10 hooks scored and ranked by awareness + tactic + trigger]
  depends-on: [creative-brief, audience-research, customer-reality]
---

# Hook Writing

## Before Starting

Confirm before starting:
- [ ] Validated creative brief (`creative-brief.md`)
- [ ] Persona known with at least one Layer 3 verbatim
- [ ] Persona's dominant emotion identified (customer-reality)
- [ ] Target awareness stage clearly defined
- [ ] Creative mechanic chosen (M1–M8)
- [ ] Medium known (video or static) — a video hook is heard, a static hook is read
- [ ] Visual format chosen (F01–F45) — the hook must be coherent with the format

**Absolute rule:** Never write hooks without a validated brief. A hook without strategy is noise.

---

## Phase 1: Load the Context

Before writing, re-read in order:
1. The brief's creative angle (C1/C2/C3/C4)
2. The persona's dominant emotion + triggering micro-moment
3. The chosen mechanic (M1–M8)
4. Available Layer 3 verbatims (Bucket 5 from review-audit if available)
5. The chosen visual format (F01–F45)

The best hook is often a direct reformulation of a Layer 3 verbatim.

---

## Phase 2: Identify the Psychological Trigger

Before choosing a tactic, identify the dominant trigger.

For the full trigger → tactic → voice pattern chain: See [references/psychological-triggers.md](references/psychological-triggers.md)

| Dominant emotion | Priority trigger |
|---|---|
| Frustration | TR3 Pain Agitation |
| Fear | TR8 Urgency / Stakes |
| Shame | TR2 Identity Call-Out |
| Hope | TR7 Aspiration |
| Anger | TR6 Contrarian |
| Confusion | TR4 Curiosity Gap |
| Resignation | TR1 Pattern Interrupt |

---

## Phase 3: Select 3–4 Tactics

Choose complementary tactics that match the awareness stage.

For the full list: See [references/hook-tactics.md](references/hook-tactics.md)

| Awareness | Recommended tactics |
|---|---|
| Unaware | T01 Aspirational, T26 Storytelling, T31 What If, T06 Curiosity Gap |
| Problem Aware | T17 Pain Agitation, T09 Empathy, T20 Problem-First, T15 Myth-Busting |
| Solution Aware | T03 Bold Claim, T02 Authority, T34 Comparison, T12 How-To |
| Product Aware | T25 Social Proof, T23 Risk Reversal, T27 Transformation, T08 Direct Address |
| Most Aware | T29 Urgency, T10 Exclusivity, T11 FOMO, T35 Future Pacing |

---

## Phase 4: Select Voice Patterns

Choose 2–3 patterns from the swipe file that match the desired tone.

For the swipe file: See [references/hook-voice-patterns.md](references/hook-voice-patterns.md)

---

## Phase 5: Write the 10 Hooks

### Writing Standards

**Do:**
- Maximum 2 lines (15–20 words for video, 25 for static)
- First word: action verb, precise number, or persona's exact word
- Use the persona's exact words (Layer 3 verbatims, Bucket 5)
- 1 hook = 1 open tension — do not resolve it in the hook
- Test aloud (video): does it sound natural?
- Test speed-read (static): readable in < 2s?

**Avoid:**
- Starting with "You", "Your", "Our product"
- Resolving the tension in the hook itself
- Using marketing vocabulary ("revolutionary", "innovative", "unique")
- Asking a rhetorical question without a real curiosity gap behind it
- Writing for all audiences — 1 hook = 1 precise persona

### Production Format

Produce 10 hooks varying:
- 3–4 different triggers
- 3–4 corresponding tactics
- 2–3 different voice patterns
- Direct tone vs narrative tone
- Question vs statement

---

## Phase 6: Score and Select

For each hook, evaluate on 3 criteria (score 1–5):

| Criterion | Question |
|---|---|
| Scroll stop | Does this hook force a stop? |
| Recognition | Does the persona immediately recognize themselves? |
| Open curiosity | Does it make you want to see more? |

Total score max = 15. Recommend the 3 hooks with score > 11.

---

## Output Format

```markdown
# Hook Bank — [Brand] — [Persona] — [Awareness] — [Date]

## Context
- Angle: [C1/C2/C3/C4]
- Mechanic: [M1–M8]
- Awareness: [Level]
- Dominant tone: [intimate / direct / educational / narrative]

## The 10 Hooks

### Hook 1
**Text:** "[Full hook]"
**Trigger:** [TR#]
**Tactic:** [T##]
**Voice Pattern:** [Cluster #]
**Score:** [X/15] — Scroll [X] · Recognition [X] · Curiosity [X]

### Hook 2
[Same structure]

[...]

## Top 3 Recommended
1. Hook [#] — Score [X/15] — Reason
2. Hook [#] — Score [X/15] — Reason
3. Hook [#] — Score [X/15] — Reason

## Production Notes
[Specific indications: rhythm, voice tone, recommended first visual frame]
```

---

## References

- [references/psychological-triggers.md](references/psychological-triggers.md) — The 8 triggers with trigger → tactic → voice pattern chain
- [references/hook-tactics.md](references/hook-tactics.md) — 42 tactics with templates and examples
- [references/hook-voice-patterns.md](references/hook-voice-patterns.md) — Swipe file of native feed patterns

## Related Skills

- `03-strategy/creative-brief` — absolute prerequisite
- `02-research/customer-reality` — source of dominant emotion and micro-moment
- `02-research/review-audit` — source of Layer 3 verbatims (Bucket 5)
- `04-production/video-production` — Top 3 hooks feed the production brief
- `04-production/static-production` — hook adaptation for static format
