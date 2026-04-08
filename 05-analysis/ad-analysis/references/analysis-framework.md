# Ad Analysis Framework

How to read ad performance data and make optimization decisions.

**Usage rule:** Never judge a metric in isolation. Context matters: awareness stage, funnel position, industry, and creative type.

---

## Key Metrics

### Hook Rate (Thumb-Stop Rate)
**Formula:** 3-second video views / Impressions
**What it measures:** First 1-3 seconds effectiveness at stopping the scroll.
**Benchmark:** 25-35% good, >35% strong, <20% failing.
**Depends on:** Visual hook, first frame, text overlay, thumbnail.

### CTR (Click-Through Rate)
**Formula:** Link clicks / Impressions
**What it measures:** Full ad effectiveness at driving clicks.
**Benchmark:** 1.5-3% good, >3% strong, <1% weak.
**Depends on:** Hook + body + CTA + offer alignment.

### CPC (Cost Per Click)
**Formula:** Total spend / Link clicks
**Benchmark:** EUR 0.50-2.50 depending on industry. B2B higher than B2C.

### CPA (Cost Per Acquisition)
**Formula:** Total spend / Conversions
**Benchmark:** Must be below target CPA (based on LTV).

### ROAS (Return on Ad Spend)
**Formula:** Revenue / Ad spend
**Benchmark:** 2-4x healthy for DTC. <1x losing money.

### CPM (Cost Per Mille)
**Formula:** (Total spend / Impressions) x 1,000
**Benchmark:** EUR 5-15 Meta broad, EUR 15-40 Meta retargeting.

### Video Completion Rate
**Formula:** Video completions / Video plays
**Benchmark:** 15-25% for 15s video, 8-15% for 30s+.

---

## Diagnostic: Low Hook Rate (< 20%)

| Check | If No | If Yes |
|---|---|---|
| First frame compelling? | Redesign first frame (face, movement, contrast) | Next check |
| Text overlay in first 1s? | Add bold text hook in top third | Next check |
| Visual native to platform? | Reshoot in native format (phone, raw) | Next check |
| All above fine | Hook message is weak -- rewrite with different tactic (T01-T42) | -- |

---

## Diagnostic: Good Hook Rate, Low CTR (< 1.5%)

| Check | If No | If Yes |
|---|---|---|
| Body delivers on hook promise? | Rewrite body to close the loop | Next check |
| Clear CTA present? | Add explicit CTA (verbal + text) | Next check |
| Ad matches landing page? | Align ad message with LP headline | Next check |
| Offer compelling? | Test stronger offer or incentive | Review targeting |

---

## Diagnostic: Good CTR, High CPA

| Check | If No | If Yes |
|---|---|---|
| LP conversion rate > 2%? | Fix LP: headline, form, speed, trust | Next check |
| Traffic quality right? | Narrow targeting, exclude low-intent | Next check |
| Offer/price OK? | Test offers, payment plans, guarantees | Check attribution |

---

## Diagnostic: High CPA, Low ROAS

| Check | If No | If Yes |
|---|---|---|
| Product-market fit validated? | Stop scaling. Validate PMF. | Next check |
| Targeting right awareness stage? | Move budget to warmer audiences | Next check |
| Creative fatigue (frequency > 3)? | Refresh creatives | Build full funnel |

---

## Metric Relationships

| When this goes up | This should also | If not, check |
|---|---|---|
| Hook Rate up | CTR up | Body not delivering on promise |
| CTR up | CPA down | Landing page not converting |
| Impressions up | CPA stable | Audience saturation (frequency) |
| Frequency up | CTR down | Creative fatigue |
| CPM up | ROAS down | Competition or seasonal spike |

---

## Priority Metrics by Funnel Stage

| Metric | TOF | MOF | BOF |
|---|---|---|---|
| Hook Rate | PRIMARY | Secondary | -- |
| CTR | Secondary | PRIMARY | Secondary |
| CPC | Monitor | Monitor | Monitor |
| CPA | Monitor | Secondary | PRIMARY |
| ROAS | -- | Monitor | PRIMARY |
| CPM | Monitor | -- | -- |
| Completion Rate | Secondary | PRIMARY | -- |

---

## Minimum Data Before Decisions

| Decision | Minimum data |
|---|---|
| Kill a hook | 1,000+ impressions, Hook Rate < 20% |
| Kill an ad | EUR 50-100 spend OR 500+ clicks, 0 conversions |
| Declare a winner | 50+ conversions, >90% statistical significance |
| Scale an ad | 3+ days consistent CPA below target |
| Refresh creative | Frequency > 2.5 AND declining CTR over 5+ days |

---

## Weekly Checklist

1. Pull metrics for all active ads (last 7 days)
2. Flag any ads violating kill rules (see kill-rules.md)
3. Identify top 3 and bottom 3 performers
4. For top performers: what pattern explains the win? (see pattern-library.md)
5. For bottom performers: which metric failed first? Run diagnostic above.
6. Document learnings and next actions
7. Brief new creatives based on insights
