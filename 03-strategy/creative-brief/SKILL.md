---
name: creative-brief
description: "Builds a complete creative brief from research outputs. The brief defines the angle, awareness stage, hook direction, creative mechanic, format, specs, and success criteria. Use after audience-research and customer-reality. Trigger on: 'build a brief', 'creative brief', 'we're preparing a campaign', 'I want to run ads'. This is the central strategic document — nothing goes to production without it."
metadata:
  version: 1.1.0
  status: stable
  tags: [strategy, brief, angle, creative, planning, notion]
  inputs: [brand-context.md, persona-[name].md, emotional-map-[persona].md, campaign objective]
  outputs: [creative-brief-[brand]-[date].md]
  notion-reads: [db-clients.md, db-personas.md, db-knowledge-base.md, db-roadmap.md]
  notion-writes: [db-concepts.md, db-briefs.md, db-roadmap.md]
  depends-on: [brand-guidelines, audience-research, customer-reality]
---

# Creative Brief

## Output Routing (Dual-Mode)

This skill follows [references/notion-output-protocol.md](../../references/notion-output-protocol.md).
Run the routing logic before producing output.

| Standalone output | Connected-mode target |
|---|---|
| `creative-brief-[brand]-[date].md` | 1 entry in `📋 [DB] Concepts` (Persona relation × Angle relation, next `Concept No.` in the client's sequence, `Creative Type`) **+** 1..N entries in `📝 [DB] Briefs` (`#NNN-B1` naming, `Format`, `Angle Category`, `Awareness Level`, Concept relation, `Client (direct)`) |

Connected-mode rules (hard):
- **Hypothesis first** — ask which `🗺️ [DB] Roadmap` hypothesis this concept tests. If none exists, create it (Type, `Objective` mandatory, Probability/Impact/Effort scored) BEFORE creating the concept. A creative without a hypothesis cannot be learned from.
- **1 Concept = 1 Persona × 1 Angle.** N hook variants live INSIDE one brief's page body — never one brief per hook, never the `Hook Type` property for multi-hook briefs.
- **Never touch `Status`** on Briefs — it is automation-driven (checkboxes + dates).
- Reuse: search Concepts for an existing Persona × Angle combo before creating a new one (an iteration belongs on the existing concept).
- Page body = narrative only (brief content, hooks, references); properties are the single source of truth for IDs/status/relations.

## Before Starting

Confirm before starting:
- [ ] `brand-context.md` available
- [ ] `persona-[name].md` available (audience-research completed)
- [ ] `emotional-map-[persona].md` available (customer-reality completed) OR verbatims available
- [ ] Business objective clear: acquisition / lead / awareness / retargeting?
- [ ] Primary KPI defined: target CPA, CPL, or ROAS?
- [ ] Budget and production capacity defined

Without these inputs, the brief will be based on hypotheses — label them clearly.

---

## Phase 1: Map Pain × Persona

Before choosing an angle, build the pain × persona matrix.

**Many-to-many principle:** The same pain can resonate with several different personas. The same persona can have several pains. Each pain × persona combination is a potentially distinct brief.

### Step 1A — List available pains
From Buckets 1 & 3 of the review-audit and the persona's Layer 2:
- Pain 1: [short description]
- Pain 2: [short description]
- Pain 3: [short description]

### Step 1B — List available personas
One or more personas from audience-research:
- Persona A: [Fictional first name] — Awareness [#]
- Persona B: [Fictional first name] — Awareness [#]

### Step 1C — Choose the brief's combination
Select the most priority pain × persona combination for this brief.

> **This brief targets:** [Persona X] suffering from [Pain Y] at awareness level [Z].

This sentence is the strategic anchor of the brief. Everything else follows from it.

---

## Phase 2: Define Strategic Context

Synthesize from available documents:

1. **Target persona** — Who? Which dominant layer?
2. **Pain addressed** — Which specific pain does this brief address?
3. **Awareness stage** — Where is this persona relative to the problem and the product?
4. **Creative objective** — What action should the creative produce?
5. **Funnel phase** — TOF / MOF / BOF / Re-engage

---

## Phase 3: Select the Angle

Choose from the 4 angle categories.

For the full framework: See [references/ad-angles.md](references/ad-angles.md)

| Angle | When to use |
|---|---|
| C1 — Problem | Problem Aware audience, strong and identifiable pain |
| C2 — Result | Solution/Product Aware audience, social proof available |
| C3 — Education | Sophisticated market or Unaware/Problem Aware audience |
| C4 — Identity | Very sophisticated market or Most Aware audience |

**Frame the angle in 1 sentence:** "This creative speaks to [persona] who [situation] and shows them [promise] via [angle]."

---

## Phase 4: Choose the Creative Mechanic

Select the mechanic that matches the angle and dominant emotion.

For the 8 mechanics framework: See [references/creative-mechanics.md](../hook-writing/references/creative-mechanics.md)

---

## Phase 5: Define Format and Specs

Choose the visual format in coherence with the mechanic and awareness stage.

For the full library: See [references/visual-formats.md](references/visual-formats.md)

| Decision | Options |
|---|---|
| Visual format | F01–F45 (see visual-formats.md) |
| Medium | Video / Static / Carousel |
| Duration (if video) | 15s / 30s / 60s / 90s+ |
| Ratio | 9:16 (Stories/Reels) / 4:5 (Feed) / 1:1 (Multi) |
| Style | UGC / Talking head / Product / B-roll / Animation |
| Sound | With voice / Music only / Silent (subtitles) |

---

## Phase 6: Write the Brief

```markdown
# Creative Brief — [Brand] — [Date]
*Status: Draft / Validated*

## Strategic Anchor
> "[Persona X] suffering from [Pain Y] at awareness level [Z]."

## Context
- Persona: [Fictional first name] — [Awareness stage]
- Pain addressed: [Specific pain from the pain × persona mapping]
- Objective: [Acquisition / Lead / Awareness / Retargeting]
- Funnel phase: [TOF / MOF / BOF]
- Primary KPI: [CPA / CPL / CTR / ROAS target]

## Creative Angle
[C1 / C2 / C3 / C4] — [Angle statement in 1 sentence]

## Core Promise
[What the creative promises — 1 sentence, customer language]

## Main Proof Point
[The proof that makes the promise credible]

## Objection to Address
[What might prevent action — and how we address it]

## Mechanic
[M1–M8] — [Mechanic name] — [How it applies here]

## Hook Direction
[Direction of the first line / first second — do not write the hook here]
Dominant trigger: [TR1–TR8]
Recommended tactic: [T01–T42]

## Format
- Visual format: [F##] — [Format name]
- Medium: [Video / Static / Carousel]
- Duration: [Xs]
- Ratio: [9:16 / 4:5 / 1:1]
- Style: [UGC / Talking head / etc.]
- Sound: [Voice on / off / silent]

## CTA
[Call-to-action text — precise and adapted to awareness level]

## Constraints
[Compliance, tone, forbidden visuals, claims to avoid]

## Success = ?
[What defines good performance for this brief]
Target CPA: [X€] / Target CTR: [X%] / Other:
```

---

## Phase 7: Validate Before Production

Ask these questions before moving to production:

- Would the persona recognize themselves in this creative?
- Is the promise credible without needing to know more?
- Is the main objection addressed somewhere?
- Is the format adapted to the platform and the scroll moment?
- Has the angle already been saturated by competitors?

---

## Related Skills

- `02-research/audience-research` — persona
- `02-research/customer-reality` — emotion + micro-moment
- `02-research/market-research` — angle vs competition
- `03-strategy/hook-writing` — next step after validated brief
- `03-strategy/message-sequencing` — if the campaign is multi-touchpoint
- `04-production/static-production` — brief → static execution
- `04-production/video-production` — brief → video execution
