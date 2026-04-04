---
name: brand-guidelines
description: "Runs a structured brand intake interview then researches the brand to build a complete brand context document. Use whenever starting work on a new brand or when no brand-context.md exists in the project. Trigger on: 'run brand intake', 'build brand context', 'I'm working on a new client', or any creative strategy workflow where brand context is missing. Must run BEFORE any downstream skill (creative-brief, hook-writing, review-audit). This is the prerequisite context layer for all creative strategy work."
metadata:
  version: 1.0.0
  status: stable
  tags: [audit, brand, foundation, prerequisite]
  inputs: [URL de la marque, entretien client]
  outputs: [brand-context-[brandname].md]
  depends-on: []
---

# Brand Guidelines

## Before Starting

Aucun prérequis — ce skill est le point d'entrée de toute stratégie créative.

Confirme avant de commencer :
- [ ] Tu as accès à l'URL de la marque
- [ ] Tu peux échanger avec le client ou un brief est disponible
- [ ] Aucun `brand-context.md` n'existe déjà dans le projet (si oui, le charger plutôt que le recréer)

---

This skill does two things in sequence:
1. **Interviews** the user to collect seed information about the brand
2. **Researches** the brand to build a comprehensive `brand-context.md`

The output feeds all downstream skills.

---

## Phase 1: Intake Interview

Ask all questions at once — do not drip them one by one.

**Brand basics:**
1. Brand name and website URL?
2. What product(s) are you running ads for?
3. Is there a specific product or line to focus on, or the full brand?

**What you already know:**
4. What do you know about the audience? (age, pain points, lifestyle, values)
5. Main competitors?
6. Any brand constraints? (compliance, tone, sensitive category)

**Creative context:**
7. Existing creative or messaging to keep in mind?

After answers: confirm and proceed to Phase 2.

---

## Phase 2: Research

Use web_search and web_fetch to fill the brand context document.

**Research checklist:**
- Brand story & origin (About page, founder story)
- Full product catalog (hero product, SKUs, bundles)
- Unique mechanism or differentiator
- Competitor landscape (3–5 competitors, positioning gaps)
- The alternative solution (what did customers do before this product?)
- Core audience(s) (primary + secondary)
- Brand voice & tone (adjectives, patterns, what they avoid)
- Creative constraints (confirmed vs. inferred)
- Must-know strategic context

---

## Phase 3: Build brand-context.md

```markdown
# Brand Context: [Brand Name]
*Generated: [Date] | Focus: [Product or Full Brand]*

## Brand Overview
## Brand Story & Origin
## Product Catalog
| Product | Key Differentiator | Audience |
## What Makes Them Different
## Competitor Landscape
| Competitor | Their Positioning | How This Brand Differs |
## The Alternative Solution
## Core Audience(s)
## Brand Voice & Tone
## Creative Constraints
| Constraint | Confirmed/Inferred | Notes |
## Must-Know Strategic Context
## Research Notes — Sources + Gaps
```

---

## Phase 4: Deliver & Confirm

Save as `brand-context-[brandname].md`, present to user, flag gaps, ask:

> "Does anything look off or need to be added? Once confirmed, this becomes the working context for all creative strategy on this brand."

---

## Related Skills

- `02-research/review-audit` — next step after brand context confirmed
- `02-research/audience-research` — deepen persona work
- `03-strategy/creative-brief` — downstream output using brand context

For compliance checklist: See [references/checklist.md](references/checklist.md)
