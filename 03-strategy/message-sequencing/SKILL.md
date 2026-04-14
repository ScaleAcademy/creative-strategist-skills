---
name: message-sequencing
description: "Plans a full-funnel message sequence: 4–5 touchpoints mapped to awareness stages, with angle, format, and CTA for each. Use after creative-brief when the campaign spans multiple awareness stages. Trigger on: 'sequence plan', 'creative funnel', 'ad journey', 'TOF MOF BOF', 'touchpoint sequence'. Produces a sequencing plan ready to brief the production team."
metadata:
  version: 1.0.0
  status: stable
  tags: [strategy, sequencing, funnel, planning, retargeting]
  inputs: [creative-brief.md, persona's starting awareness stage]
  outputs: [sequencing-plan-[brand]-[date].md — 4–5 touchpoint plan]
  depends-on: [creative-brief, audience-research]
---

# Message Sequencing

## Before Starting

Confirm before starting:
- [ ] Creative brief available for at least 1 touchpoint
- [ ] Persona's starting awareness stage known
- [ ] Budget available to test multiple phases (not useful on single-phase small budget)
- [ ] Meta campaign structure defined or to be defined

This skill is only useful if the brand has the means to deploy 3+ touchpoints. On a test budget < €1,000/month, prioritize 1 strong angle rather than a sequence.

---

## Sequencing Principle

The audience moves along the awareness scale across touchpoints.
Each touchpoint must move the prospect one level forward — not sell at every stage.

```
Unaware → TOF: educate / awaken
Problem Aware → TOF/MOF: validate the pain / show a solution exists
Solution Aware → MOF: differentiate / prove the mechanism
Product Aware → MOF/BOF: remove objections / reinforce proof
Most Aware → BOF: direct offer / urgency
```

---

## Phase 1: Define the Entry Point

Identify the persona's dominant awareness stage at the top of the funnel.
→ This is where the sequence begins.

---

## Phase 2: Build the Touchpoints

For each funnel stage, define:

| Field | Content |
|---|---|
| Target awareness stage | Level 1–5 |
| Touchpoint objective | Awaken / Educate / Differentiate / Remove objection / Convert |
| Creative angle | C1 / C2 / C3 / C4 |
| Recommended format | Video / Static / Carousel |
| Duration (if video) | 15s / 30s / 60s / 90s |
| Hook direction | Emotional, situational, or identity opening |
| CTA | Soft / Medium / Direct |
| Meta audience | Cold / Engaged / Visitors / Cart / Customers |

---

## Phase 3: Recommended Sequence Plan

### Standard 5-Touchpoint Structure

**TP1 — TOF Cold: Awaken**
- Audience: Cold (broad interests or lookalike)
- Target awareness: Unaware or Problem Aware
- Objective: Spark awareness
- Angle: C1 (pain) or C3 (education)
- CTA: "Learn more" / "Discover"
- Format: Video 30–60s or Reel

**TP2 — TOF/MOF: Qualify**
- Audience: TP1 engaged (25%+ video views, interactions)
- Target awareness: Problem Aware → Solution Aware
- Objective: Show that a solution exists and it's different
- Angle: C3 (mechanism) or C2 (result)
- CTA: "See how it works"
- Format: Video 45–90s or educational Carousel

**TP3 — MOF: Prove**
- Audience: Product page visitors or TP2 engaged
- Target awareness: Solution Aware → Product Aware
- Objective: Convince that this product is the right choice
- Angle: C2 (social proof) or C4 (identity)
- CTA: "See results" / "Join"
- Format: Video testimonial or static proof

**TP4 — BOF: Remove Objections**
- Audience: Product page visitors without conversion (warm retargeting)
- Target awareness: Product Aware → Most Aware
- Objective: Eliminate the last barrier to purchase
- Angle: C2 (guarantee / risk reversal) or C1 (cost of inaction)
- CTA: "Try risk-free" / "See offer"
- Format: Short video 15–30s or offer static

**TP5 — Re-engage: Urgency**
- Audience: Abandoned cart or unconverted leads
- Target awareness: Most Aware
- Objective: Trigger the final action
- Angle: Direct offer + urgency
- CTA: "Buy now" / "Join before [date]"
- Format: Offer static or video < 15s

---

## Output Format

```markdown
# Sequencing Plan — [Brand] — [Date]

## Starting Awareness: [Level]
## Final Objective: [Conversion / Lead / Registration]

| # | Phase | Audience | Awareness | Angle | Format | CTA |
|---|---|---|---|---|---|---|
| TP1 | TOF Cold | Cold | [1–2] | [C#] | [Format] | [CTA] |
| TP2 | TOF/MOF | TP1 Engaged | [2–3] | [C#] | [Format] | [CTA] |
| TP3 | MOF | Visitors | [3–4] | [C#] | [Format] | [CTA] |
| TP4 | BOF | Retargeting | [4–5] | [C#] | [Format] | [CTA] |
| TP5 | Re-engage | Cart / Leads | [5] | Direct offer | [Format] | [CTA] |

## Production Notes
[Production priority, suggested budget per phase, kill rules per touchpoint]

## Briefs to Produce
- [ ] Brief TP1 → launch `creative-brief`
- [ ] Brief TP2 → launch `creative-brief`
- [...]
```

---

## Related Skills

- `03-strategy/creative-brief` — one brief per touchpoint
- `04-production/campaign-setup` — corresponding Meta campaign structure
- `05-analysis/ad-analysis` — creative analysis per touchpoint
- `05-analysis/strategy-gap` — identify uncovered funnel phases
