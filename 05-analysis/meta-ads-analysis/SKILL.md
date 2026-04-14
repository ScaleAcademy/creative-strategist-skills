---
name: meta-ads-analysis
description: "Runs a full Meta Ads account analysis in 7 steps using Windsor.ai as MCP data bridge. Pulls live campaign/creative/audience data directly into Claude and produces an actionable audit report: account health, campaign audit, creative lifecycle, angle & format performance, audience analysis, and prioritized action plan. Trigger on: 'analyze my Meta account', 'Meta Ads audit', 'which ads to tune', 'creative analysis Meta', 'Windsor analysis'. Requires Windsor.ai MCP connection."
metadata:
  version: 1.0.0
  status: stable
  tags: [analysis, meta-ads, performance, creative, windsor, mcp, account-audit]
  inputs: [Meta Ads account connected via Windsor.ai MCP, naming convention applied (optional but recommended)]
  outputs: [7-section report: account health + campaign audit + creative lifecycle + angles & formats + audiences + prioritized action plan]
  depends-on: [brand-guidelines, ad-analysis]
---

# Meta Ads Analysis — Complete System (Claude + Windsor.ai)

## Before Starting

Confirm before starting:
- [ ] Windsor.ai MCP connected and functional in Claude Desktop
- [ ] Access to target Meta Ads account (via Windsor.ai)
- [ ] Analysis period defined (recommended: minimum last 30 days)
- [ ] Target KPI known (target CPA, CPL, ROAS)
- [ ] Naming convention applied (see [references/windsor-setup.md](references/windsor-setup.md)) — strongly recommended for creative analysis

If Windsor.ai is not yet configured: see [references/windsor-setup.md](references/windsor-setup.md) — setup in 4 steps.

---

## Phase 0: Setup & Connection

Before any analysis, initialize the connection and define the context.

**Prompt:**
```
Connect to my Meta Ads account via Windsor.ai.
List all available ad accounts.
I want to analyze [ACCOUNT NAME] over the last [X] days.
My primary objective is [acquisition / lead gen / awareness].
My target KPI is [target CPA X€ / target CPL X€ / target ROAS X].
```

**Expected result:**
- Connection confirmation
- List of available accounts
- Period and analysis context confirmed

---

## Phase 1: Account Health

Get a macro view of the account's overall health before going into detail.

**Prompt:**
```
Give me an overall health summary of account [NAME] over the last [X] days:
- Total spend and change vs. previous period
- Global CPA / CPL / ROAS vs. my target ([X€])
- Number of active campaigns, ad sets, and creatives running
- Budget breakdown by campaign (% of total spend)
- Top 3 campaigns by spend and their respective performance
- Warning signals: budget concentration, high frequency, detected fatigue
```

**What we're looking for:**
- Identify if the account is healthy or drifting
- Spot campaigns monopolizing budget without performing
- Get a baseline before detailed analysis

---

## Phase 2: Campaign Audit

Analyze each campaign in detail to identify weak links and winners.

**Prompt:**
```
For each active campaign over the last [X] days, give me:
- Campaign name
- Objective (awareness / traffic / conversion / etc.)
- Total spend
- Impressions, Reach, Average Frequency
- CTR (link click-through rate)
- CPA / CPL / ROAS depending on objective
- Status: Winner / Learner / Loser (relative to my target [X€])
- Recommendation: Scale / Maintain / Optimize / Cut

Sort by spend descending.
```

**Verdict rules:**
- **Winner:** Primary KPI ≤ target × 0.9
- **Learner:** Primary KPI between target × 0.9 and target × 1.3, or insufficient spend
- **Loser:** Primary KPI > target × 1.5 with sufficient spend (>200€)

---

## Phase 3: Creative Lifecycle

Identify the life state of each creative: rising, at peak, in fatigue, or dead.

**Prompt:**
```
Analyze the lifecycle of each active creative over the last [X] days.
For each creative:
- Name / ID
- Total spend and launch date
- Week-over-week (or period-over-period) CPA evolution
- Hook Rate (ThruPlay / Impressions for video)
- Current frequency
- Estimated life phase: Rising / Peak / Declining / Fatigued / Dead
- Recommended action: Let it run / Boost budget / Slow down / Cut

Identify the 3 creatives showing the most marked signs of fatigue.
Identify the 3 creatives with the best recent momentum.
```

**Fatigue signals:**
- CPA rising >20% over 7 consecutive days
- CTR dropping >30% vs. first week
- Frequency > 3.5 on cold audience

---

## Phase 4: Performance by Angle & Format

Analyze which creative mechanic and format perform best — to guide next productions.

**Prompt:**
```
Using creative names, analyze performance by angle and by format.

By creative angle (codes in the name: PR / RS / ED / ID — see convention):
- Total spend by angle
- Average CPA by angle
- Average CTR by angle
- Number of creatives tested by angle
- Most profitable angle vs. least profitable angle

By format (codes in the name: VID / STA / CAR — see convention):
- Same metrics as above
- Average Hook Rate (video only)
- Optimal duration (video: 15s / 30s / 60s+)

Conclusion: which angles and formats to prioritize for next productions?
```

**Note:** If the naming convention is not applied, this analysis will be manual. See [references/windsor-setup.md](references/windsor-setup.md) to adopt the convention.

---

## Phase 5: Audience Analysis

Identify which audience responds best and detect targeting issues.

**Prompt:**
```
Analyze performance by audience over the last [X] days:

By ad set / audience:
- Audience name
- Type: Cold prospecting / Lookalike / Retargeting / Warm
- Total spend
- CPA / CPL / ROAS
- Frequency
- Estimated audience size
- Status: Winner / Learner / Loser

Specific questions:
- Are there suspicious audience overlaps?
- Which cold audience works best?
- Does retargeting outperform prospecting?
- Are there audience saturation signals (frequency > 4 + rising CPA)?
```

---

## Phase 6: Prioritized Action Plan

Synthesize all findings into a concrete action plan, prioritized by potential impact.

**Prompt:**
```
Based on all previous analysis (account health, campaigns, lifecycle, angles, formats, audiences), generate a prioritized action plan for the next 7 days.

Format:
## Immediate Actions (to do today)
- [Action] → [Reason] → [Expected impact]

## Actions This Week
- [Action] → [Reason] → [Expected impact]

## Recommended Next Productions
Based on performing angles and missing ones:
- Creative to test #1: [Recommended Angle / Format / Mechanic]
- Creative to test #2: [Recommended Angle / Format / Mechanic]
- Creative to test #3: [Recommended Angle / Format / Mechanic]

## Hypotheses to Validate
- H1: If we [X], then [KPI] should [direction] because [signal].
- H2: [Same structure]
- H3: [Same structure]
```

---

## Output Format

```markdown
# Meta Ads Analysis — [Brand] — [Period] — [Date]
*Tool: Windsor.ai MCP | Account: [ID] | Spend analyzed: [X€]*

## Phase 0 — Context
- Account: [Name]
- Period: [From XX to XX]
- Target KPI: [CPA X€ / CPL X€ / ROAS X]
- Objective: [Acquisition / Lead / Awareness]

## Phase 1 — Account Health
[Summary table + warning signals]

## Phase 2 — Campaign Audit
[Winner / Learner / Loser table by campaign]

## Phase 3 — Creative Lifecycle
[Top 3 declining + Top 3 growing + full table]

## Phase 4 — Angles & Formats
[Performance by angle + by format + conclusion for next creatives]

## Phase 5 — Audiences
[Table by audience + overlaps + saturation]

## Phase 6 — Action Plan
[Immediate actions + this week + next productions + hypotheses]
```

---

## References

- [references/windsor-setup.md](references/windsor-setup.md) — Windsor.ai MCP installation + complete naming convention
- [../ad-analysis/references/kpi-benchmarks.md](../ad-analysis/references/kpi-benchmarks.md) — Reference benchmarks by platform and objective

## Related Skills

- `05-analysis/ad-analysis` — individual creative analysis (micro complement)
- `05-analysis/account-audit` — macro strategic account audit
- `05-analysis/strategy-gap` — if the analysis reveals missing angles
- `03-strategy/creative-brief` — to brief next productions from the action plan
- `04-production/campaign-setup` — to set up new campaigns post-analysis
