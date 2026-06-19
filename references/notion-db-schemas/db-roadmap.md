# 🗺️ [DB] Roadmap — Notion Schema

> Reference schema for the `Roadmap` database used by the Creative Strategist OS.

## Purpose

The **prioritized hypothesis backlog**. Separates *learnings* (what we know — BL/CL DBs) from
*hypotheses* (what we'll test next — this DB). Every creative produced must trace back to one
of these items — a creative without a hypothesis is impossible to learn from.

**Title rule:** the title IS the hypothesis, phrased as an actionable sentence
("Tester l'angle X sur le persona Y pour réduire le CPA"). The operational to-do lives in `Action`.

**Prioritization rules:** high-awareness audiences (PRA/MA) first · never test a new persona
AND a new angle in the same hypothesis · `Objective` is mandatory.

## Database location (template)

- Teamspace : `MX Marketing` · Parent page : `[DB] DATABASES`
- Database title : `🗺️ [DB] Roadmap` — icon 🗺️

## Properties

| Property | Type | Required | Options / Format | Notes |
|---|---|---|---|---|
| `Hypothesis` | Title | ✅ | Actionable sentence | |
| `ID` | Auto-increment | auto | — | |
| `Type` | Select | ✅ | `Business` · `Creative` | Mirrors the BL/CL split |
| `Client` | Relation → `[DB] Clients` | ✅ | — | |
| `Objective` | Select | ✅ | `💰 Boost CA` · `📉 Reduce CPA` · `📈 Increase conversion` · `🎯 New audience` · `🚀 Scale volume` · `🔄 Reduce fatigue` | Mandatory — why we test |
| `Priority` | Select | ✅ | `P0` · `P1` · `P2` | Battle order |
| `Probability` | Number (%) | ✅ | 0–100% | Chance of success |
| `Impact (1-10)` | Number | ✅ | — | Business impact |
| `Effort (1-5)` | Number | ✅ | — | Production effort |
| `Score` | Formula | auto | `Impact × Probability ÷ Effort` | Simplified RICE — sort descending |
| `Status` | Status | ✅ | `Idea` · `To Test` → `Running` · `Paused` → `Validated` · `Rejected` | |
| `Action` | Text | — | The concrete to-do | Separate from the hypothesis statement |
| `Validated Insight` | Text | — | What we concluded | Filled at close |
| `Origine` | Select | — | `📊 Audit ads` · `🧪 Test interne` · `💡 Recommandation` · `📚 Théorie` · `👤 Client` · `🔍 Veille concurrent` | |
| `Week` | Text | — | `S23`… | |
| `Currency` | Select | — | `🟢 Current` · `🟡 Outdated` · `🔴 Replaced` | |
| `Planned Test Date` / `End Date` | Dates | — | — | |
| `Validation` | Select | — | `🤖 AI - To Validate` · `✅ Reviewed` | |
| `Source Learning Business` / `Source Learning Creative` | Relations → BL / CL | — | — | Where the hypothesis comes from |
| `Persona` / `Angle` / `Style` / `Concept` / `Brief` | Relations | — | — | What it touches / how it gets tested |

## Relations map

```
Business Learnings ─┐
                    ├──→ Roadmap (hypothesis, scored & prioritized) ──→ Concept / Brief (test)
Creative Learnings ─┘            └──→ results feed back as new Learnings
```
