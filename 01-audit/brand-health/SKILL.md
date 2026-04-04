---
name: brand-health
description: "Establishes a performance baseline from existing ad account data. Use when starting work on a brand that has been running ads. Trigger on: 'audit the account', 'what's our baseline', 'how are we performing'. Requires dashboard or account access."
metadata:
  version: 1.0.0
  status: beta
  tags: [audit, performance, baseline, meta-ads]
  inputs: [accès dashboard Meta Ads, période minimum 30 jours]
  outputs: [rapport baseline KPIs — top/bottom performers, gaps stratégiques]
  depends-on: [brand-guidelines]
---

# Brand Health

## Before Starting

Confirme avant de commencer :
- [ ] Accès au dashboard Meta Ads (Business Manager ou Ads Manager)
- [ ] Période définie — minimum 30 jours, recommandé 90 jours
- [ ] `brand-context.md` disponible (sinon lancer `brand-guidelines` d'abord)
- [ ] KPI principal connu : optimisation sur leads, purchases, ou ROAS ?

Si l'accès dashboard n'est pas disponible : demander un export CSV des données de campagne.

---

This skill produces a baseline performance report before any new creative strategy is deployed.

**Input:** Meta Ads dashboard access + period (minimum 30 days, recommended 90 days)
**Output:** Baseline report — KPIs, benchmarks, production capacity, constraints

---

## What to Audit

### 1. Media Performance
- CPM, CPC, CTR, Hook Rate (ThruPlay / Impressions)
- CPA / CPL (cost per acquisition or lead)
- Top 3 and bottom 3 creatives by primary KPI

### 2. Creative Production Capacity
- How many creatives launched in the period?
- Average time from brief to launch?
- Formats used (static / video / carousel)?

### 3. Account Constraints
- Active campaigns — what's already running?
- Budget distribution — testing vs. scaling vs. retargeting?

### 4. Industry Benchmarks
Compare current KPIs against category benchmarks.

For benchmark reference: See [references/brand-health.md](references/brand-health.md)

---

## Output Format

```
## Baseline Report — [Brand] — [Period]

### Key KPIs
| Metric | Current | Benchmark | Status |

### Top Performers
| Creative | Format | Primary KPI | Why It Works (hypothesis) |

### Bottom Performers
| Creative | Format | Primary KPI | Failure Hypothesis |

### Production Capacity
Creatives launched: [X] / [period]
Avg brief-to-launch: [X days]

### Strategic Gaps
[What's missing — formats, angles, awareness stages not covered]
```

---

## Related Skills

- `01-audit/brand-alignment` — run alongside for strategic alignment
- `05-analysis/account-audit` — deeper creative analysis after baseline set
