# Kill Rules — When to Stop an Ad, Ad Set, or Campaign

Kill rules remove emotion from optimization decisions. When a metric crosses a threshold for a defined period, the ad is paused — no debate, no "let's give it one more day."

**Usage rule:** Set kill rules BEFORE launching. Agree on thresholds with the client. Document them. Apply them consistently.

---

## Ad-Level Kill Rules

| Metric | Kill Threshold | Timeframe | Exception |
|---|---|---|---|
| **Hook Rate** | < 20% | After 1,000 impressions | None — if the hook doesn't work at 1,000 impressions, it won't work at 10,000 |
| **CTR** | < 1.0% | After 2,000 impressions | BOF retargeting may have lower CTR but higher conversion rate — check CPA |
| **CPC** | > €2.50 | After 500 clicks | B2B or high-ticket products may tolerate higher CPC if CPA is on target |
| **CPA** | > 1.5x target CPA | After 2x target CPA in spend | First 24-48h of a new ad may have inflated CPA — wait for learning phase |
| **ROAS** | < 0.5x target ROAS | After 2x target CPA in spend | New campaigns need 50+ conversions for accurate ROAS measurement |
| **Video completion** | < 5% (15s video) | After 1,000 views | Longer videos naturally have lower completion — adjust threshold proportionally |
| **Frequency** | > 3.0 | Rolling 7-day period | If performance is still strong at high frequency, monitor but don't kill |

---

## Ad Set-Level Kill Rules

| Metric | Kill Threshold | Timeframe | Action |
|---|---|---|---|
| **CPA** | > 2x target CPA | After spending 3x target CPA | Pause ad set. Review audience or creative. |
| **No conversions** | 0 conversions | After spending 2x target CPA | Pause. The audience or creative combination is not working. |
| **CTR declining** | CTR drops 50%+ from first 3 days | Rolling 7-day comparison | Creative fatigue. Replace creatives before unpausing. |
| **CPM spike** | CPM > 2x account average | Sustained for 3+ days | Audience is too small or too competitive. Broaden targeting. |

---

## Campaign-Level Kill Rules

| Metric | Kill Threshold | Timeframe | Action |
|---|---|---|---|
| **Overall CPA** | > 2x target for 7+ days | 7-day rolling | Restructure. Review targeting, creative mix, and funnel. |
| **Budget delivery** | < 50% of daily budget spent | 3+ consecutive days | Audience too small or bid too low. Adjust. |
| **Learning phase stuck** | "Learning Limited" for 7+ days | 7 days after launch | Consolidate ad sets. Broaden audience. Increase budget per ad set. |

---

## Platform-Specific Benchmarks

### Meta Ads

| Metric | Poor | Acceptable | Good | Excellent |
|---|---|---|---|---|
| Hook Rate (3s views) | < 20% | 20-30% | 30-40% | > 40% |
| CTR (link clicks) | < 1.0% | 1.0-2.0% | 2.0-3.5% | > 3.5% |
| CPC | > €3.00 | €1.50-3.00 | €0.70-1.50 | < €0.70 |
| CPM | > €25 | €12-25 | €6-12 | < €6 |
| Frequency (7-day) | > 4.0 | 2.5-4.0 | 1.5-2.5 | < 1.5 |
| Video completion (15s) | < 8% | 8-15% | 15-25% | > 25% |

### Google Ads (Search)

| Metric | Poor | Acceptable | Good | Excellent |
|---|---|---|---|---|
| CTR | < 2% | 2-5% | 5-8% | > 8% |
| CPC | > €5.00 | €2.00-5.00 | €0.80-2.00 | < €0.80 |
| Conversion Rate | < 2% | 2-5% | 5-10% | > 10% |
| Quality Score | < 5 | 5-6 | 7-8 | 9-10 |

### Google Ads (Display/YouTube)

| Metric | Poor | Acceptable | Good | Excellent |
|---|---|---|---|---|
| CTR | < 0.3% | 0.3-0.8% | 0.8-1.5% | > 1.5% |
| View Rate (YouTube) | < 15% | 15-25% | 25-35% | > 35% |
| CPV (YouTube) | > €0.10 | €0.05-0.10 | €0.02-0.05 | < €0.02 |
| CPM | > €15 | €8-15 | €3-8 | < €3 |

---

## Escalation Path

When a kill rule is triggered:

```
1. PAUSE the ad/ad set (don't delete — you may want the data later)
2. DOCUMENT why it was killed (metric, threshold, timeframe)
3. DIAGNOSE the root cause using analysis-framework.md
4. DECIDE next action:
   a. Hook failed → Write new hooks, same body/offer
   b. Body failed → Rewrite body, keep winning hook
   c. Audience failed → Test different targeting, same creative
   d. Offer failed → Test different offer/CTA, same creative
   e. Multiple failures → New creative concept from scratch
5. RELAUNCH with the fix applied
6. TRACK the new version against the same kill rules
```

---

## Special Cases

### Learning Phase Protection
New ads need data before kill rules apply. Grace period:

| Spend level | Grace period |
|---|---|
| < 1x target CPA | No kill — too early to judge |
| 1-2x target CPA | Monitor but don't kill unless Hook Rate < 15% |
| > 2x target CPA | Kill rules fully active |

### Seasonal Adjustments
During high-competition periods (Black Friday, Q4, January), adjust thresholds:

| Period | CPC threshold | CPM expectation | CPA tolerance |
|---|---|---|---|
| Normal | Baseline | Baseline | 1.5x target |
| Q4 (Nov-Dec) | +50-100% | +30-60% | 2x target |
| January (low comp.) | -20-30% | -20-30% | 1.2x target |
| Product launch | N/A | Expect higher | 2x target for first 2 weeks |

---

## Kill Rule Documentation Template

When pausing an ad, log:

```
Date: [YYYY-MM-DD]
Ad name: [per naming-convention.md]
Metric violated: [metric] = [value] vs threshold [threshold]
Spend at kill: €[amount]
Impressions: [number]
Root cause hypothesis: [brief diagnosis]
Next action: [what you'll test next]
```
