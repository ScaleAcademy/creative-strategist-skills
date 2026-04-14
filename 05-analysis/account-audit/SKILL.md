---
name: account-audit
description: "Reviews the full Meta ad account performance over a defined period to identify top performers, underperformers, creative patterns, and structural gaps. Use quarterly or when performance drops unexpectedly. Trigger on: 'account audit', 'performance overview', 'macro analysis', 'what's working in the account'. Produces a macro performance report with strategic recommendations."
metadata:
  version: 1.0.0
  status: stable
  tags: [analysis, account, performance, meta-ads, macro]
  inputs: [Meta Ads account access, minimum 30-day period, recommended 90 days]
  outputs: [account audit report — top performers, patterns, gaps, recommendations]
  depends-on: [brand-health]
---

# Account Audit

## Before Starting

Confirm before starting:
- [ ] Meta Ads Manager access (Campaigns, Ad Sets, Ads)
- [ ] Period defined: minimum 30 days, recommended 90 days
- [ ] Primary account KPI known (CPA / CPL / ROAS)
- [ ] `brand-context.md` available for product and audience context
- [ ] Sufficient spend data (account with < 1,000€ over the period = unreliable data)

For benchmarks: see [references/kpi-benchmarks.md](../ad-analysis/references/kpi-benchmarks.md)

---

## Phase 1: Account Overview

Analyze at the campaign level:

- Total budget spent over the period
- Budget breakdown: testing / scaling / retargeting (%)
- Number of active vs. paused campaigns
- Week-over-week performance trends (upward or downward)
- Account average CPM (account competitiveness signal)

---

## Phase 2: Creative Analysis

Sort all active ads over the period by spend descending.

**Top 5 Performers:** Ads with the best primary KPI AND significant spend.
**Bottom 5:** Ads with the worst primary KPI with significant spend.
**Insufficiently tested ads:** Ads with < 100€ spend — unreliable data.

For each top performer, note:
- Format (video / static / carousel)
- Creative angle (C1/C2/C3/C4)
- Targeted awareness stage
- Hook tactic used
- Creative mechanic

---

## Phase 3: Identify Patterns

Compare top performers vs. bottom performers:

- Is there a dominant format among winners?
- Is there a dominant angle among winners?
- Is there an over-represented awareness stage?
- Are there mechanics absent from the account?
- Are there unaddressed personas?

---

## Phase 4: Identify Structural Gaps

Analyze account structure:

- TOF / MOF / BOF distribution: is it balanced?
- Warm audience frequency: signal of saturation?
- Creative rotation: when was the last new creative launched?
- Testing budget: is there a dedicated budget for testing new concepts?

---

## Phase 5: Recommendations

Structure recommendations into 3 categories:
1. **Optimize** — what's working and can be amplified (increase budget, iterate)
2. **Kill** — what's consuming budget without results (immediate stop)
3. **Test** — what's missing and should be tested this sprint

---

## Output Format

```markdown
# Account Audit — [Brand] — [Period] — [Date]

## Overview
- Total spend: [X€]
- Budget breakdown: TOF [%] / MOF [%] / BOF [%]
- Average primary KPI: [value] vs target [value]
- Trend: [Upward / Stable / Downward]

## Top 5 Performers
| Creative | Format | Angle | Awareness | KPI | Spend |
[table]

## Bottom 5
| Creative | Format | Angle | Awareness | KPI | Spend |
[table]

## Identified Patterns
**What works:** [Dominant Format / Angle / Mechanic]
**What fails:** [Common pattern among losers]

## Structural Gaps
- Awareness not covered:
- Formats not tested:
- Personas not addressed:
- Absent mechanics:

## Recommendations

### Optimize
[What to scale or iterate]

### Kill
[What to stop — with reason]

### Test This Sprint
[3 priority new concepts with brief direction]
```

---

## Related Skills

- `01-audit/brand-health` — initial baseline
- `05-analysis/ad-analysis` — to go deeper on each creative
- `05-analysis/strategy-gap` — to dig deeper into identified gaps
- `03-strategy/creative-brief` — to brief the recommended new tests
