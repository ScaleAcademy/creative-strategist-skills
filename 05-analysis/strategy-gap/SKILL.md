---
name: strategy-gap
description: "Identifies missing angles, untested personas, uncovered awareness stages, and format gaps in the current creative strategy. Use after account-audit or when performance plateaus. Trigger on: 'what are we not testing', 'missing angles', 'strategic gap', 'going in circles'. Produces a prioritized gap report with sprint recommendations."
metadata:
  version: 1.0.0
  status: stable
  tags: [analysis, strategy, gaps, testing, planning]
  inputs: [current campaign data, account-audit report or ad-analysis reports]
  outputs: [gap report — top 3 prioritized gaps + sprint recommendation]
  depends-on: [account-audit]
---

# Strategy Gap

## Before Starting

Confirm before starting:
- [ ] At least one recent `account-audit` available, or multiple individual `ad-analysis` reports
- [ ] Test history available (which angles / formats / personas have already been tested)
- [ ] `brand-context.md` available for context
- [ ] Next sprint business objective defined

This skill doesn't create new angles from scratch — it identifies what's missing from what exists.

For the complete grid: see [references/gap-matrix.md](references/gap-matrix.md)

---

## Phase 1: Map What Exists

Build an inventory of what has been tested:

**Awareness gaps:**
Which awareness levels have active creatives? Which don't?

**Angle gaps:**
Which C1/C2/C3/C4 angles have been tested? Which are absent?

**Persona gaps:**
How many distinct personas have been directly addressed? Which are ignored?

**Format gaps:**
Which formats have been tested? Which formats have never been launched?

**Mechanic gaps:**
Which creative mechanics (M1–M8) are present in the account? Which are absent?

---

## Phase 2: Qualify the Gaps

For each identified gap, evaluate:

| Criterion | Score 1–3 |
|---|---|
| Potential audience volume reached | |
| Ease of producing the test | |
| Preliminary signal justifying the test | |
| Alignment with sprint objective | |

Score > 9 = high priority.

---

## Phase 3: Formulate Sprint Recommendations

Convert the top 3 gaps into concrete recommendations:
- Gap description
- Hypothesis of what filling this gap could produce
- Specific creative to produce to test
- Priority (High / Medium)

---

## Output Format

```markdown
# Strategy Gap Report — [Brand] — [Date]

## Inventory — What Has Been Tested
| Dimension | Tested | Not tested |
|---|---|---|
| Awareness | | |
| Angles | | |
| Personas | | |
| Formats | | |
| Mechanics | | |

## Top 3 Identified Gaps

### Gap 1 — [Title]
**Dimension:** [Awareness / Angle / Persona / Format / Mechanic]
**Description:** [What's missing]
**Hypothesis:** [What filling this gap could produce]
**Recommended test:** [1 specific creative to produce]
**Score:** [X/12] — Priority: High

### Gap 2
[Same structure]

### Gap 3
[Same structure]

## Sprint Recommendation
→ [X] briefs to launch this sprint to cover the priority gaps
→ Recommended test budget: [X€]
→ Briefs to create: see `03-strategy/creative-brief`
```

---

## Related Skills

- `05-analysis/account-audit` — primary data source
- `05-analysis/ad-analysis` — to dig deeper into each gap with individual data
- `03-strategy/creative-brief` — to brief the recommended tests
- `03-strategy/message-sequencing` — if the gap concerns an entire funnel phase
