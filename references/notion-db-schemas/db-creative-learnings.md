# 🖼️ [DB] Creative Learnings — Notion Schema

> Reference schema for the `Creative Learnings` database used by the Creative Strategist OS.

## Purpose

What we learn at the **execution level**: hook, CTA, visual, format, length, music, voiceover.
Operational iterations on existing creatives, tested in days (vs weeks for Business Learnings).
Linked to `Brief` (the creative iterated on), feeds the `Roadmap` like its Business sibling.

Same temporal traceability rules: never delete — `Week` stamp + `Currency` + `Replaces`/`Replaced By` chain.

## Database location (template)

- Teamspace : `MX Marketing` · Parent page : `[DB] DATABASES`
- Database title : `🖼️ [DB] Creative Learnings` — icon 🖼️

## Properties

| Property | Type | Required | Options / Format | Notes |
|---|---|---|---|---|
| `Learning` | Title | ✅ | Actionable sentence | |
| `ID` | Auto-increment | auto | global, never reset | |
| `Client` | Relation → `[DB] Clients` | ✅ | — | |
| `Type` | Select | ✅ | `New Hook` · `New CTA` · `New Visual` · `New Format` · `New Length` · `New Music` · `New Voiceover` | The iteration lever |
| `Status` | Status | ✅ | `Idea` · `To Test` → `Running` · `Paused` → `Validated` · `Rejected` | |
| `Origine` | Select | ✅ | `📊 Audit ads` · `🧪 Test interne` · `💡 Recommandation` · `📚 Théorie` · `👤 Client` | |
| `Key Learnings` | Text | — | The substance | |
| `Hook Rate` | Number (%) | — | — | Key creative metric when relevant |
| `Week` | Text | ✅ | `S21`, `S22`… | |
| `Currency` | Select | ✅ | `🟢 Current` · `🟡 Outdated` · `🔴 Replaced` | |
| `Replaces` / `Replaced By` | Self-relations | — | — | Version chain |
| `Validation` | Select | — | `🤖 AI - To Validate` · `✅ Reviewed` | |
| `Brief` | Relation → `[DB] Briefs` | ✅ | — | The creative this learning comes from |
| `Concept` | Relation → `[DB] Concepts` | — | — | |
| `Style` | Relation → Styles Library | — | — | |
| `Roadmap items` | Relation → `[DB] Roadmap` | — | — | |

## Relations map

```
Brief ──→ Creative Learnings ──→ Roadmap (creative hypotheses) ──→ new Briefs (iterations)
```
