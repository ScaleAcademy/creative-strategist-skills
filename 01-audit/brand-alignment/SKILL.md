---
name: brand-alignment
description: "Aligns creative strategy with the brand's real business objectives, growth stage, and team constraints. Use before starting any sprint or client engagement. Trigger on: 'what should we focus on', 'real objectives', 'business context'. Requires conversation with founder or decision-maker."
metadata:
  version: 1.0.0
  status: beta
  tags: [audit, strategy, objectives, constraints]
  inputs: [conversation avec founder ou media buyer]
  outputs: [rapport d'alignement — objectifs réels, stage de croissance, capacité production]
  depends-on: [brand-guidelines]
---

# Brand Alignment

## Before Starting

Confirme avant de commencer :
- [ ] Accès à une conversation avec le founder, CMO, ou media buyer (pas un intermédiaire)
- [ ] `brand-context.md` disponible ou `brand-guidelines` lancé en parallèle
- [ ] Contexte business minimum connu : secteur, produit principal, budget approximatif

Si le décideur n'est pas disponible : ce skill perd sa valeur — ne pas le remplacer par des hypothèses.

---

This skill surfaces the real objectives and constraints before creative work begins.

**Input:** Conversation with founder, media buyer, or marketing lead
**Output:** Alignment report — real objectives, growth stage, media buyer optimization target, production capacity

---

## Questions to Ask

### Business Stage
- What stage is the business in? (validating / scaling / optimizing)
- What's the primary growth lever right now?
- What does "success" look like in 90 days?

### Real Objectives
- What is the media buyer optimizing for? (leads / purchases / ROAS / CAC)
- Is there a specific CPA or CPL target?
- What's the budget trajectory?

### Constraints
- What has been tried and killed? Why?
- Are there creative constraints not documented elsewhere?
- What's the realistic production capacity per week?

### Strategic Alignment
- Are marketing objectives aligned with sales/product objectives?
- Any launch, event, or promotion in the next 30–60 days?
- Who approves creative? What slows that process?

---

## Output Format

```
## Alignment Report — [Brand] — [Date]

### Growth Stage
[Validating / Scaling / Optimizing + rationale]

### Real Objective (next 90 days)
[1 sentence — the actual goal]

### Media Buyer Optimization Target
[What the algorithm optimizes for + cost target]

### Production Capacity
Creatives per week: [realistic number]
Approval bottleneck: [who + avg time]

### What's Been Tried & Killed
| Creative / Angle / Format | Why Killed |

### Constraints
[List — budget, compliance, team, platform]
```

For alignment signals reference: See [references/brand-alignment.md](references/brand-alignment.md)

---

## Related Skills

- `01-audit/brand-health` — run alongside for full audit
- `03-strategy/creative-brief` — alignment context feeds the brief
