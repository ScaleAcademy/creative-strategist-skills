---
name: campaign-setup
description: "Structures paid social campaigns (Meta, TikTok, Google, Snapchat, Pinterest, LinkedIn): naming convention, campaign/ad set/ad architecture, audience setup, budget allocation, and kill rules. Use after creative production is complete and assets are ready to upload. Trigger on: 'structure the campaign', 'setup Meta / TikTok / Google', 'naming convention', 'how to organize campaigns', 'platform parameters'. Produces a ready-to-launch campaign structure."
metadata:
  version: 1.1.0
  status: beta
  tags: [production, paid-social, campaign, setup, naming, meta, tiktok, google, snapchat, pinterest, linkedin]
  inputs: [validated creatives ready to upload, campaign objective, budget, target platform]
  outputs: [campaign structure + naming convention + kill rules for the chosen platform]
  depends-on: [creative-brief, static-production, video-production]
---

# Campaign Setup

## Before Starting

Confirm before starting:
- [ ] Final creatives ready (video / image files exported in correct formats)
- [ ] Campaign objective defined: Conversions / Leads / Traffic / Awareness
- [ ] Daily or total budget defined
- [ ] Meta Pixel installed and events verified
- [ ] Destination URL / landing page ready and tracked
- [ ] Target KPI defined (CPA, CPL, ROAS)

---

## Phase 1: Campaign Architecture

### 4-Phase Structure

**P1 — Creative Testing**
- Objective: Identify performing creatives
- Budget: 20–40€/day per ad set
- Audience: Cold (broad interests or lookalike 1–3%)
- Creatives: 3–5 ads per ad set (1 ad set per angle tested)
- Time before decision: 3–5 days minimum, 50€+ spent

**P2 — Retargeting**
- Objective: Recover engaged users and site visitors
- Budget: 10–20€/day
- Audience: Site visitors (30d), page/profile engaged (30d), video views 25%+ (14d)
- Creatives: 2–3 BOF ads (objection / direct offer)

**P3 — Scale Winners**
- Objective: Amplify what proved performance in P1
- Budget: 2–5× the initial test budget
- Audience: Lookalike 1% of buyers or leads
- Creatives: Top 1–2 winners only

**P4 — Re-engage**
- Objective: Reactivate old prospects and customers
- Budget: 10€/day
- Audience: Old leads (90d+), customers (180d+), old engaged
- Creatives: New content / exclusive offer / value content

---

## Phase 2: Naming Convention

Name systematically to be able to analyze and filter quickly.

**Campaign Format:**
`[Brand]_[Objective]_[Budget Type]`
Example: `SA_ACQ_CBO`

**Ad Set Format:**
`[Brand]_[Audience Type]_[Audience Description]`
Example: `SA_COLD_BROAD-25-45F`

**Ad Format:**
`[Brand]_[Angle]_[Format]_[Style]_[Ratio]_v[X]_[YYYYMM]`
Example: `SA_PR_VID30_UGC_916_v1_202604`

For the complete naming convention: See [references/naming-convention.md](../../references/naming-convention.md)

---

## Phase 3: Kill Rules

Define stop criteria in advance to avoid emotional decisions.

| Metric | Kill Rule |
|---|---|
| CPA | > [target × 1.5] after 50€ spent |
| CTR | < 0.8% after 30€ spent (static) |
| Hook Rate | < 15% after 20€ spent (video) |
| CPL | > [target × 2] after 3 leads |
| Frequency | > 3 in 7 days → refresh creative |

**72h Rule:** Do not kill an ad before 72h unless CPA is > 3× target. Let the algorithm learn.

---

## Output Format

```markdown
# Campaign Setup — [Brand] — [Date]

## Architecture

### P1 — Creative Testing
Campaign name: [Name]
Budget: [X€/day]
Ad Sets:
  - [Ad set name 1] → [Creatives: ID1, ID2, ID3]
  - [Ad set name 2] → [Creatives: ID4, ID5, ID6]

### P2 — Retargeting
[Same structure]

### P3 — Scale (activate if P1 winner)
[Same structure]

### P4 — Re-engage
[Same structure]

## Active Kill Rules
| Metric | Threshold | Action |
[table]

## Pre-Launch Checklist
- [ ] Pixel verified
- [ ] Events tracked (PageView, InitiateCheckout, Purchase / Lead)
- [ ] UTM URLs configured
- [ ] Total daily budget ≤ monthly budget / 30
- [ ] Creatives approved by Meta (format + compliance)
- [ ] Kill rules documented in the tracker
```

---

## Platform References

- [meta-ads-parameters.md](references/meta-ads-parameters.md) — Objectives, audiences, bidding, placements, Meta pixel
- [tiktok-ads-parameters.md](references/tiktok-ads-parameters.md) — TikTok Ads structure, Spark Ads, targeting, bidding
- [google-ads-parameters.md](references/google-ads-parameters.md) — YouTube Ads, Performance Max, Display, Google Ads
- [snapchat-ads-parameters.md](references/snapchat-ads-parameters.md) — Snap Ads, audiences, formats, specs
- [pinterest-ads-parameters.md](references/pinterest-ads-parameters.md) — Pinterest Ads, keyword targeting, visual formats
- [linkedin-ads-parameters.md](references/linkedin-ads-parameters.md) — LinkedIn Ads B2B, Lead Gen Forms, professional targeting
- [ad-formats-specs.md](references/ad-formats-specs.md) — Cross-platform specs image / video / text / safe zones

## Related Skills

- `04-production/static-production` — asset source
- `04-production/video-production` — asset source
- `05-analysis/ad-analysis` — after 3–5 days of delivery
- `01-audit/brand-health` — benchmark for kill rules
