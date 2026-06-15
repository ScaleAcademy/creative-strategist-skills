---
name: hypothesis-intake
description: "Transforms a raw creative idea into a structured, scored hypothesis in the Roadmap DB. Works for all clients. Triggers naturally on: 'j'ai une idée de créa', 'j'ai cette hypothèse', 'on pourrait tester', 'et si on testait', 'j'aimerais tester', 'une piste', 'j'ai pensé à', 'ça pourrait marcher', 'j'ai un concept', 'tester [X]', 'native ads', 'on lance [format]', 'je veux lancer'."
metadata:
  version: 1.0.0
  status: stable
  tags: [strategy, roadmap, hypothesis, prioritization, planning, notion]
  inputs: [raw idea (verbal or text), client context]
  outputs: [1 entry in 🗺️ [DB] Roadmap]
  notion-reads: [db-roadmap.md, db-clients.md, db-personas.md, db-angles.md]
  notion-writes: [db-roadmap.md]
  depends-on: []
---

# Hypothesis Intake

## Purpose

Entry point for any creative idea — before a concept, before a brief.
Every creative must trace back to a Roadmap hypothesis. This skill creates that hypothesis.

**Trigger patterns (all clients, all languages):**
- "j'ai une idée de créa / de pub / de format"
- "on pourrait tester [X]" / "et si on testait [X]"
- "j'aimerais tester / lancer [format/angle]"
- "j'ai cette hypothèse" / "j'ai pensé à [X]"
- "ça pourrait marcher de" / "une piste que j'ai"
- "native ads", "statiques", "un article", "une vidéo avec [X]"
- "j'ai un concept pour [client]"
- "je veux lancer [format]"

---

## Step 1 — Capture Verbatim

Transcribe the raw idea exactly as expressed, without rewording.

> **Raw idea:** "[verbatim]"

---

## Step 2 — Identify Client

Ask or infer from context:
- Which client? (Autotrade / Yuman / Netione / Scale Academy / other)

---

## Step 3 — Formalize the Hypothesis

Rewrite as a single actionable sentence following the Roadmap title rule:
> "Tester [Angle ou Format] sur [Persona] pour [Objective]"

Examples:
- "Tester des native ads statiques (photo brute → article) sur persona Problem Aware pour réduire le CPL Yuman"
- "Tester une vidéo testimonial résultat chiffré sur persona MA pour booster le CA Autotrade NL"

---

## Step 4 — Qualify the Hypothesis

Fill each required field:

| Field | Value | Options |
|---|---|---|
| `Type` | ? | `Business` · `Creative` |
| `Objective` | ? | `💰 Boost CA` · `📉 Reduce CPA` · `📈 Increase conversion` · `🎯 New audience` · `🚀 Scale volume` · `🔄 Reduce fatigue` |
| `Awareness Level` | ? | `Unaware` · `Problem Aware (PA)` · `Solution Aware (SA)` · `Product Aware (PRA)` · `Most Aware (MA)` |
| `Persona` | ? | Link to existing persona or "new" |
| `Angle` | ? | Link to existing angle or "new" |
| `Format` | ? | Static · Video · Carousel · Native · Article |
| `Probability` | ?% | 0–100% (chance this learns something actionable) |
| `Impact (1-10)` | ? | Business impact if validated |
| `Effort (1-5)` | ? | Production effort required |
| `Action` | ? | The concrete next step (≠ hypothesis statement) |
| `Origine` | ? | `💡 Recommandation` · `📊 Audit ads` · `🧪 Test interne` · `📚 Théorie` · `👤 Client` · `🔍 Veille concurrent` |

**Score** = Impact × Probability ÷ Effort (auto-calculated by Notion formula)

---

## Step 5 — Apply Prioritization Rules

Check before suggesting priority:

1. **Awareness first** — High-awareness audiences (PRA/MA) before Unaware. If Unaware, recommend P2 unless there's a specific strategic reason — state it.
2. **One new variable at a time** — Never test a new Persona AND a new Angle simultaneously. If both are new, flag it and recommend splitting into two hypotheses.
3. **Objective is mandatory** — No hypothesis without an explicit Objective. If unclear, ask before proceeding.

---

## Step 6 — Check Running Hypotheses

Fetch current hypotheses for this client from Notion `🗺️ [DB] Roadmap` (Status = `Running` or `To Test`).

Compare:
- Is this already covered by a running hypothesis?
- Does this replace or extend an existing one?
- Where does it sit in the priority queue relative to current P0/P1 items?

Suggest:
- **Priority**: P0 / P1 / P2
- **Timing**: Now (this week) / Next (next week) / Backlog

---

## Step 7 — Present and Confirm

Show the full card before creating anything:

```
Hypothesis : [formalized sentence]
Type       : [Business / Creative]
Client     : [client name]
Objective  : [option]
Awareness  : [level]
Priority   : [P0/P1/P2]
Timing     : [Now / Next / Backlog]
Probability: [%]
Impact     : [1-10]
Effort     : [1-5]
Score      : [Impact × Probability ÷ Effort]
Action     : [next step]
Origine    : [option]
```

Ask: "Je crée l'hypothèse dans Notion ?" before writing anything.

---

## Output Routing

| Standalone output | Connected-mode target |
|---|---|
| Summary card in conversation | 1 entry in `🗺️ [DB] Roadmap` (client workspace MX Marketing) |

---

## Related Skills

- `03-strategy/creative-brief` — next step once hypothesis is created and concept is defined
- `02-research/audience-research` — if Persona is undefined
- `02-research/market-research` — if Angle is undefined or competitive context is missing
