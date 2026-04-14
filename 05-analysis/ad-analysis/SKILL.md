---
name: ad-analysis
description: "Deconstructs an ad's performance data to identify why it worked or failed, extract learnings, and generate 3 test hypotheses. Use after a creative has accumulated significant spend. Trigger on: 'analyze this ad', 'why is it working', 'creative deconstruction', 'what do we learn from this result'. Produces a learning report and 3 actionable next test hypotheses."
metadata:
  version: 1.0.0
  status: stable
  tags: [analysis, performance, creative, testing, hypotheses]
  inputs: [creative performance data (Meta metrics), visual access or description of the creative]
  outputs: [deconstruction report + 3 actionable test hypotheses]
  depends-on: [brand-health]
---

# Ad Analysis

## Before Starting

Confirm before starting:
- [ ] Performance data available: minimum Impressions, CTR, Hook Rate (if video), CPA or CPL
- [ ] Sufficient spend for reliable data (minimum 100€ spent, ideally 300€+)
- [ ] Visual access to the creative (link, screenshot, or detailed description)
- [ ] Original brief available or origin context known (otherwise, analyze without brief = hypotheses to label)
- [ ] Period defined and targeted audience known

For reference benchmarks: see [references/kpi-benchmarks.md](references/kpi-benchmarks.md)

---

## Phase 1: Read the Data

Collect and organize key metrics:

| Metric | Value | Benchmark | Status |
|---|---|---|---|
| Hook Rate (video) | | 20–30% | |
| Hold Rate 50% | | 20–35% | |
| CTR (link click) | | 1–2% | |
| CPM | | 8–15€ | |
| CPA / CPL | | [target] | |
| Frequency | | < 3 | |
| Total spend | | — | |

Identify immediately: is it a winner, a learner, or a loser?
- **Winner:** Primary KPI ≤ target + significant volume
- **Learner:** Insufficient data or KPI close to target — continue
- **Loser:** Primary KPI > target × 1.5 with sufficient spend — kill

---

## Phase 2: Deconstruct the Creative

Analyze the creative structure across 4 layers:

### Hook (First second / First frame)
- What was used as the opener?
- Tactic identified (T01–T42)?
- Psychological trigger?
- Why did it work or not in light of the Hook Rate?

### Body of the Message
- What creative mechanic (M1–M8)?
- What is the central promise?
- What proof point?
- Objection addressed or not?

### CTA
- Clarity and alignment with the awareness stage?
- CTA friction adapted to engagement level?

### Format & Production
- Format adapted to the platform and audience?
- Appropriate production quality (not too much, not too little)?
- Optimal ratio and duration?

---

## Phase 3: Formulate the Diagnosis

Identify the primary cause of performance — good or bad.

**If winner:**
- What contributed most? (hook / angle / mechanic / format / audience)
- Is this result reproducible or contextual (period, budget)?
- What principle can be extracted for future creatives?

**If loser:**
- Where did the audience drop off? (Low Hook Rate = hook / Low CTR = body or CTA / High CPA = landing page or offer)
- Was the angle right but the execution poor? Or did the angle itself not work?
- What does this result reveal about the persona or market?

---

## Phase 4: Generate 3 Test Hypotheses

Each hypothesis must be:
- **Testable**: one single variable changed
- **Motivated**: based on a signal in the data, not intuition alone
- **Actionable**: the next creative to produce is clear

**Hypothesis format:**
> "If we [change X], then [KPI Y] should [increase/decrease] because [reason from the data]."

---

## Output Format

```markdown
# Ad Analysis — [Brand] — [Creative Name] — [Date]

## Performance Data
| Metric | Value | Benchmark | Status |
[table]

## Verdict
[ ] Winner  [ ] Learner  [ ] Loser

## Deconstruction

### Hook
Tactic: [T##] — Trigger: [bias/LF]
Analysis: [Why it worked / didn't work in light of the Hook Rate]

### Body of the Message
Mechanic: [M#] — Angle: [C#]
Analysis: [Reading of Hold Rate and CTR]

### CTA
Analysis: [Awareness alignment / clarity / friction]

### Format
Analysis: [Format, ratio, duration — adequacy]

## Primary Diagnosis
[1 sentence: what mainly explains the result]

## What We Learn
[2–3 generalizable insights for future creatives]

## 3 Test Hypotheses

**H1:**
If we [change X], then [KPI] should [direction] because [reason].
Creative to produce: [short description]

**H2:**
[Same structure]

**H3:**
[Same structure]
```

---

## Related Skills

- `01-audit/brand-health` — baseline before analysis
- `05-analysis/account-audit` — macro view after multiple individual analyses
- `05-analysis/strategy-gap` — if the analysis reveals untested angles
- `03-strategy/creative-brief` — to brief the test hypotheses
