# Ad Naming Convention

A consistent naming convention lets you analyze performance by angle, format, style, and audience directly from campaign names — without any manual sorting.

**The logic: each level of the account structure carries its own information.**

---

## Account Structure & What Each Level Names

```
Campaign     → Objective + Budget type
  └── Ad Set → Targeting / Audience concept
        └── Ad → Creative: angle + format + style + ratio + version + date
```

---

## Campaign Level

**What it names:** The objective and how budget is managed.

```
[BRAND]_[OBJECTIVE]_[BUDGET_TYPE]
```

| Segment | Codes | Description |
|---|---|---|
| BRAND | e.g. MARCA | Brand shortcode (2–6 chars) |
| OBJECTIVE | ACQ / LEA / RET / AWA | Acquisition / Lead gen / Retargeting / Awareness |
| BUDGET_TYPE | CBO / ABO | Campaign Budget Optimization / Ad Set Budget Optimization |

**Examples:**
```
MARCA_ACQ_CBO
MARCA_LEA_ABO
MARCA_RET_CBO
```

> No date at campaign level. Campaigns run continuously — the date lives on the ad.

---

## Ad Set Level

**What it names:** Who you're targeting and with what audience strategy.

```
[BRAND]_[AUDIENCE_TYPE]_[AUDIENCE_DESCRIPTION]
```

| Segment | Codes | Description |
|---|---|---|
| BRAND | e.g. MARCA | Same brand shortcode |
| AUDIENCE_TYPE | COLD / WARM / RET / LAL | Cold broad / Warm interest / Retargeting / Lookalike |
| AUDIENCE_DESCRIPTION | Free text, no spaces | Describe the targeting concept: persona name, interest cluster, source audience |

**Examples:**
```
MARCA_COLD_BROAD-25-45F
MARCA_LAL_1PCT-PURCHASERS
MARCA_LAL_3PCT-INITCHECKOUT
MARCA_RET_30D-VISITORS
MARCA_RET_7D-ADDTOCART
MARCA_WARM_INTEREST-WELLNESS
```

> No date at ad set level. Audiences are reused — versioning happens at the ad level.

---

## Ad Level

**What it names:** The full creative identity — angle, format, style, ratio, version, and date.

```
[BRAND]_[ANGLE]_[FORMAT]_[STYLE]_[RATIO]_v[X]_[YYYYMM]
```

| Segment | Codes | Description |
|---|---|---|
| BRAND | e.g. MARCA | Same brand shortcode |
| ANGLE | PR / RS / ED / ID | See Angle Codes below |
| FORMAT | VID15 / VID30 / VID60 / STA / CAR | See Format Codes below |
| STYLE | UGC / TH / BROLL / TEXT / SKIT | See Style Codes below |
| RATIO | 916 / 45 / 11 | 9:16 / 4:5 / 1:1 |
| VERSION | v1, v2, v3... | Iteration number for the same concept |
| DATE | YYYYMM | Month of creation (e.g. 202604 = April 2026) |

**Examples:**
```
MARCA_PR_VID30_UGC_916_v1_202604
MARCA_RS_STA_TEXT_45_v2_202604
MARCA_ED_VID60_TH_916_v1_202605
MARCA_ID_CAR_TEXT_11_v1_202604
```

---

## Angle Codes

| Code | Full Name | Awareness Match | Description |
|---|---|---|---|
| PR | Problem | Problem Aware | Leads with a pain point the audience already feels |
| RS | Result | Solution / Product Aware | Leads with proof, transformation, or outcome |
| ED | Education | Unaware / Problem Aware | Teaches something — reframes the problem or the solution |
| ID | Identity | Unaware / Most Aware | Speaks to who the person is or wants to become |

These map directly to the C1–C4 creative angles in the creative-brief skill.

---

## Format Codes

| Code | Format | Medium |
|---|---|---|
| VID15 | Video 15s | Video |
| VID30 | Video 30s | Video |
| VID60 | Video 60s+ | Video |
| STA | Static image | Static |
| CAR | Carousel | Carousel |

---

## Style Codes

| Code | Style | Description |
|---|---|---|
| UGC | User Generated Content | Raw, native, shot by creator or actor |
| TH | Talking Head | Direct-to-camera, presenter-led |
| BROLL | B-Roll + VO | Product/lifestyle footage with voiceover |
| TEXT | Text-based | Animated text, minimal or no visual |
| SKIT | Skit / Scene | Scripted scenario or situation |

---

## Why This Structure Works

With this convention applied, Claude (via Windsor.ai) can answer:
- "Which angle performs best?" → compare all `PR` vs `RS` vs `ED` vs `ID` ads
- "Does VID30 beat VID15 on CPA?" → filter by FORMAT code
- "Is UGC outperforming TH?" → filter by STYLE code
- "What's our best ratio for cold?" → filter COLD ad sets + RATIO code

Without this convention → creative analysis requires manual tagging.

---

## Related Skills

- `04-production/campaign-setup` — where to apply this when building campaigns
- `05-analysis/meta-ads-analysis` — Windsor.ai analysis relies on this convention for angle & format breakdowns
