# 🧠 [DB] Business Learnings — Notion Schema

> Reference schema for the `Business Learnings` database used by the Creative Strategist OS.

## Purpose

What we **learn about the client/market** by testing at the strategic level: persona bets,
angle bets, segment/positioning insights. Tested over 1+ weeks via 1 concept × N styles.
Paired with `Creative Learnings` (execution-level) — together they feed the `Roadmap`
(hypotheses), closing the loop: Knowledge Base → Learnings → Roadmap → Concepts/Briefs → results → Learnings.

**Temporal traceability rule:** learnings are never deleted. They age via `Currency` and the
`Replaces` / `Replaced By` chain, stamped by `Week`.

## Database location (template)

- Teamspace : `MX Marketing` · Parent page : `[DB] DATABASES`
- Database title : `🧠 [DB] Business Learnings` — icon 🧠

## Properties

| Property | Type | Required | Options / Format | Notes |
|---|---|---|---|---|
| `Learning` | Title | ✅ | Actionable sentence | e.g. "X est l'angle pilier pour P304" |
| `ID` | Auto-increment | auto | global, never reset | |
| `Client` | Relation → `[DB] Clients` | ✅ | — | |
| `Type` | Select | ✅ | `Persona` · `Angle` | What the learning is about |
| `Status` | Status | ✅ | `Idea` · `To Test` → `Running` · `Paused` → `Validated` · `Rejected` | |
| `Origine` | Select | ✅ | `📊 Audit ads` · `Veille Concurrentielle` · `👤 Client` · `🧪 Test interne` · `💡 Recommandation` | |
| `Key Learnings` | Text | — | The substance | |
| `Week` | Text | ✅ | `S21`, `S22`… | When it was established |
| `Currency` | Select | ✅ | `🟢 Current` · `🟡 Outdated` · `🔴 Replaced` | Freshness |
| `Replaces` / `Replaced By` | Self-relations | — | — | Version chain, never delete |
| `Validation` | Select | — | `🤖 AI - To Validate` · `✅ Reviewed` | AI-generated entries need human review |
| `Concept` | Relation → `[DB] Concepts` | — | — | Where it was tested |
| `Persona` / `Angle` | Relations | — | — | What it concerns |
| `Roadmap items` | Relation → `[DB] Roadmap` | — | — | Hypotheses derived from it |

## Relations map

```
Knowledge Base ──→ Business Learnings ──→ Roadmap (hypotheses) ──→ Concepts
                          ↑ (results feed back after analysis)
```
