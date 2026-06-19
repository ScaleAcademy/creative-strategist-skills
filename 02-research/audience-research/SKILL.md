---
name: audience-research
description: "Builds a 3-layer persona from existing data and research. Use after brand-guidelines to deepen audience understanding before brief writing. Trigger on: 'who is our audience', 'build a persona', 'deep dive audience', 'who are we really talking to'. Produces a complete persona document ready to feed creative-brief and hook-writing."
metadata:
  version: 1.1.0
  status: stable
  tags: [research, persona, audience, psychology, notion]
  inputs: [brand-context.md, existing audience data (CRM / interviews / reviews)]
  outputs: [persona-[name].md — full Layer 1/2/3]
  notion-reads: [db-clients.md, db-real-customers.md, db-knowledge-base.md]
  notion-writes: [db-personas.md, db-knowledge-base.md]
  depends-on: [brand-guidelines]
---

# Audience Research

## Output Routing (Dual-Mode)

This skill follows [references/notion-output-protocol.md](../../references/notion-output-protocol.md).
Run the routing logic before producing output.

| Standalone output | Connected-mode target |
|---|---|
| `persona-[name].md` (full document) | Entry in `👥 [DB] Personas` — Layer 1 selects (Genre, Tranche d'âge, Génération, CSP, Statut familial), `Layer 2 — Ce qu'ils disent`, `Layer 3 — Ce qu'ils veulent vraiment`, `Problématiques`, `Objections`, `Vocabulaire-clé`, `Niveau Awareness`, `Source`, `Client` relation |
| — | Entry in `📚 [DB] Knowledge Base` (Type `Persona`, Phase `Phase 1 — Research`, Block `👥 Audience Research`) pointing to the full document via `Drive URL` / `Repo Path` — page body holds the doc's role only, content lives in the doc |

Connected-mode rules:
- If the persona was mined from real interactions, link the `Real Customers` entries used as evidence.
- Enrich an existing persona entry rather than creating a duplicate (search by name + client first).
- Persona = a distinctive psycho-behavioral trait, not a demographic sheet — the trait drives the `Name`.

## Before Starting

Confirm before starting:
- [ ] `brand-context.md` available
- [ ] At least one audience data source available (CRM, interviews, reviews, analytics)
- [ ] Target persona identified or to be determined (primary vs secondary)
- [ ] Dominant awareness stage known or to be determined

Without real data, this skill produces hypotheses — label them clearly as such.

---

## Phase 1: Identify the Persona to Build

Ask these questions before starting:
1. Is there an existing documented persona? If yes, load and enrich it rather than starting from scratch.
2. What is the product / main offer targeted by this persona?
3. What is the presumed awareness level of this persona?

---

## Phase 2: Build Layer 1 — Demographic

To extract from existing data or to research:

- Age and gender (dominant in purchases or customer base)
- Professional situation and income level
- Location (urban / suburban / rural; region or country)
- Active social platforms (Meta, TikTok, YouTube, LinkedIn)
- Purchasing behavior: impulsive vs deliberate, price-sensitive vs value-sensitive

**Sources:** Facebook/Instagram Analytics, Google Analytics demographics, CRM data.

For the Layer 1/2/3 framework: See [references/persona-layers.md](references/persona-layers.md)

---

## Phase 3: Build Layer 2 — Psychographic

To extract via interviews, long reviews, Reddit, niche forums.

- Priority value (freedom, security, status, performance, family)
- Perceived identity: "I am someone who..."
- Aspirational identity: "I want to be someone who..."
- Deep fears (often not stated publicly)
- Relationship with failure and risk
- Cultural references: followed influencers, admired brands

For the LF8 framework: See [references/life-force-8.md](references/life-force-8.md)
For active biases: See [references/marketing-psychology.md](references/marketing-psychology.md)

---

## Phase 4: Build Layer 3 — Situational

This is the most valuable and hardest layer to obtain without real data.

Questions to ask in interviews or to extract from reviews:
- "Describe the day you decided to look for a solution."
- "What were you doing exactly when you realized you had this problem?"
- "What was your main hesitation before buying?"
- "What finally convinced you?"
- "What would you tell someone who is still hesitating?"

Extract:
- The triggering micro-moment (specific situation, time, context)
- The exact phrase used to describe the pain
- The main pre-purchase objection
- The dominant emotion at the time of purchase

---

## Phase 5: Map Awareness

Based on Layer 3, locate the persona on the awareness scale.

For the full framework: See [references/awareness-levels.md](../market-research/references/awareness-levels.md)

---

## Output Format

Save as `persona-[first-name].md` in the project folder.

```markdown
# Persona — [Fictional first name] — [Product]
*Generated on [date] | Dominant awareness: [level]*

## Layer 1 — Demographic
- Age / Gender:
- Professional situation:
- Approximate income:
- Location:
- Active platforms:

## Layer 2 — Psychographic
- Priority value:
- Current identity: "I am someone who..."
- Aspirational identity: "I want to be..."
- Deep fear:
- Dominant LF: [LF1–LF8]
- Main active bias: [bias]

## Layer 3 — Situational
- Triggering micro-moment:
- Exact phrase (verbatim):
- Main objection:
- What convinced them:
- Dominant emotion:

## Awareness Stage
[Level 1–5] — [Rationale]

## Creative Direction
→ Recommended angle:
→ Tone:
→ Format:
→ Hook direction:
```

---

## Related Skills

- `01-audit/brand-guidelines` — prerequisite
- `02-research/review-audit` — Layer 3 source
- `02-research/customer-reality` — enriches micro-moments and emotional mapping
- `03-strategy/creative-brief` — direct output of this skill
- `03-strategy/hook-writing` — uses Layer 3 to calibrate hooks
