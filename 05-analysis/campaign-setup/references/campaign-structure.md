# Campaign Structure — 4-Phase Architecture

A systematic campaign architecture for scaling ad accounts. Four phases, each with distinct objectives, audiences, creative requirements, and graduation criteria.

**Usage rule:** Launch Phase 1 first. Only add Phase 2 when Phase 1 generates enough data. Scale methodically -- never skip phases.

---

## Phase 1 — Test (Creative Testing)

| Element | Detail |
|---|---|
| **Objective** | Find winning creatives. Identify which hooks, angles, and formats resonate with the target audience. |
| **Campaign type** | Meta: CBO or ABO with testing structure. Google: separate test campaigns. |
| **Audience** | Broad or interest-based. Cold audiences only. No retargeting. |
| **Budget allocation** | 40-50% of total ad budget |
| **Creative requirements** | 3-5 new creatives per week. Each tests ONE variable (hook, angle, format, or audience). |
| **KPI targets** | Hook Rate > 25%, CTR > 1.5%, CPC < EUR 2.00 |
| **Graduation criteria** | Creative achieves target CPA for 3+ consecutive days with 50+ conversions total. |

**Structure detail:**
- 1 campaign per product/offer
- 1 ad set per audience segment (2-3 segments max)
- 3-5 ads per ad set (the creatives being tested)
- Daily budget: enough to exit learning phase within 3-5 days

**Testing priority order:**
1. Hook (biggest impact on performance)
2. Angle (C1-C4)
3. Format (video vs static vs carousel)
4. Body/script (after hook is validated)
5. CTA (smallest impact, test last)

---

## Phase 2 — Retarget (Warm Audiences)

| Element | Detail |
|---|---|
| **Objective** | Convert warm prospects who engaged with Phase 1 content but did not purchase. |
| **Campaign type** | Meta: separate retargeting campaign. Google: remarketing lists. |
| **Audience** | Website visitors (30-90 days), video viewers (50-95%), engagement audiences, email lists. |
| **Budget allocation** | 20-25% of total ad budget |
| **Creative requirements** | 2-3 dedicated retargeting creatives. Different message from Phase 1 -- address objections, show proof, make the offer. |
| **KPI targets** | CPA < target CPA, ROAS > 2x, CTR > 2% |
| **Graduation criteria** | Retargeting audiences are saturated (frequency > 3) or CPA rises above 1.5x target. |

**Audience segments (in priority order):**
1. Landing page visitors (no conversion) -- last 14 days
2. Add-to-cart / initiate checkout abandoners -- last 7 days
3. Video viewers 75%+ -- last 30 days
4. All website visitors -- last 30 days
5. Email list (non-purchasers)
6. Social engagers -- last 30 days

**Creative approach:**
- OCR formula (Objection, Counter, Resolution) for objection handling
- Social proof mashups (F33) and testimonials (F36)
- Direct offer with scarcity (if genuine)
- Remind them what they viewed: "Still thinking about [product]?"

---

## Phase 3 — Scale (Amplify Winners)

| Element | Detail |
|---|---|
| **Objective** | Maximize volume from proven creatives and audiences. Scale spend while maintaining CPA. |
| **Campaign type** | Meta: CBO with proven creatives. Advantage+ Shopping if e-commerce. Google: maximize conversions with target CPA. |
| **Audience** | Broad (let the algorithm optimize), lookalikes of converters, expanded interests. |
| **Budget allocation** | 25-30% of total ad budget |
| **Creative requirements** | Only proven winners from Phase 1. No untested creatives in scaling campaigns. Refresh with iterations of winners (new hook on winning body). |
| **KPI targets** | CPA < 1.2x target, ROAS > target, stable at higher spend |
| **Graduation criteria** | Diminishing returns (CPA rises 30%+ despite optimization) or audience saturation. |

**Scaling rules:**
- Increase budget by max 20-30% every 3 days (not overnight)
- If CPA spikes after budget increase, wait 48h before reverting
- Duplicate winning ad sets into new campaigns rather than inflating one campaign
- Monitor frequency -- if >2.5 on broad, audience is saturating
- Always have Phase 1 feeding new winners into Phase 3

**When Phase 3 stops working:**
- Creative fatigue is the #1 cause. Not audience, not budget, not bidding.
- Go back to Phase 1, find new winners, feed them into Phase 3.
- The cycle is continuous: Test -> Retarget -> Scale -> Test again.

---

## Phase 4 — Re-engage (Win-back & Retention)

| Element | Detail |
|---|---|
| **Objective** | Re-activate lapsed prospects and past customers. Maximize LTV. |
| **Campaign type** | Meta: separate campaign with custom audiences. Google: customer match + remarketing. |
| **Audience** | Past purchasers (30-180 days), lapsed website visitors (60-180 days), email unengaged (90+ days). |
| **Budget allocation** | 5-10% of total ad budget |
| **Creative requirements** | 1 new creative per week. Focus on new information, new offers, or updated social proof. |
| **KPI targets** | CPA < 0.8x target (warm audience should convert cheaper), repeat purchase rate |
| **Graduation criteria** | Audience pool refreshes naturally. Ongoing maintenance campaign. |

**Audience segments:**
1. Past purchasers (cross-sell / upsell) -- 30-90 days since purchase
2. Past purchasers (re-purchase) -- 90-180 days since purchase
3. Lapsed high-intent visitors -- 60-180 days, no conversion
4. Email list churned -- opened but stopped engaging

**Creative approach:**
- "We've updated [product/feature]" -- new information trigger
- "X people joined since you last visited" -- social proof FOMO
- Exclusive returning-customer offer
- Personal tone: founder video, direct message format

---

## Full Architecture Overview

| Phase | Objective | Audience | Budget | Key Metric | Creative Volume |
|---|---|---|---|---|---|
| P1 Test | Find winners | Cold / Broad | 40-50% | Hook Rate, CTR | 3-5/week |
| P2 Retarget | Convert warm | Engagers, visitors | 20-25% | CPA, ROAS | 2-3 dedicated |
| P3 Scale | Maximize volume | Broad + Lookalikes | 25-30% | CPA at scale | Winners only |
| P4 Re-engage | Win-back, LTV | Past customers, lapsed | 5-10% | Repeat rate, CPA | 1/week |

---

## Phase Transition Checklist

### P1 to P2
- [ ] At least 1,000 website visitors from P1
- [ ] Video view audiences built (50%, 75%, 95%)
- [ ] 2-3 retargeting creatives produced (different from P1)
- [ ] Retargeting audiences segmented by intent level

### P2 to P3
- [ ] 2+ creatives with CPA below target for 3+ days
- [ ] 50+ total conversions to validate the creative
- [ ] Scaling campaign structure prepared (CBO or Advantage+)
- [ ] Budget increase plan documented (20-30% every 3 days)

### P3 to P4
- [ ] 100+ past customers in the audience pool
- [ ] Re-engagement creatives produced (different from P1/P2/P3)
- [ ] Customer segments defined (by purchase recency and value)

---

## Naming Convention Integration

All campaigns, ad sets, and ads follow the naming convention in `naming-convention.md`. Phase is encoded in the campaign name:

```
[BRAND]_[PHASE]_[OBJECTIVE]_[DATE]
Example: SCOTT_P1-TEST_HOOK-ANGLES_2026-04
Example: SCOTT_P2-RETARGET_OBJECTIONS_2026-04
Example: SCOTT_P3-SCALE_WINNERS_2026-04
Example: SCOTT_P4-REENGAGE_WINBACK_2026-04
```
