# 📋 [DB] Concepts — Notion Schema

> Reference schema for the `Concepts` database used by the Creative Strategist OS.

## Purpose

**1 Concept = 1 Audience (Persona) × 1 Angle**, applied to a client's offer. The substance of
the message: what we say, to whom. Mid-level of the 3-level creative hierarchy:

```
Concept (Persona × Angle)  →  N Briefs (1 per style/hook tactic)  →  N Ads
```

Never create N concepts for N hooks — hooks vary at Brief level. The concept page body holds
the narrative (French, ~15–25 lines, no dates); the DB properties hold everything trackable.

## Database location (template)

- Teamspace : `MX Marketing` · Parent page : `[DB] DATABASES`
- Database title : `📋 [DB] Concepts` — icon 📋

## Properties

| Property | Type | Required | Options / Format | Notes |
|---|---|---|---|---|
| `Name` | Title | ✅ | Concept name — NO batch info in the name | |
| `Concept No.` | Text | ✅ | `#019` | Stable sequential ID per client, never reused |
| `Client` | Relation → `[DB] Clients` | ✅ | — | |
| `Persona` | Relation → `[DB] Personas` | ✅ | — | The targeted audience |
| `Angle` | Relation → Angles Library | ✅ | — | The advertising angle template |
| `Creative Type` | Select | ✅ | `Ideation` · `Imitation` · `Iteration` | Where the concept comes from |
| `Status` | Status | ✅ | `💡 Idea` → `🧪 Exploration` → `🎬 Active` → `🔧 To rework` / `⏸️ On hold` → `🏆 Winner` / `❌ Loser` / `🗄️ Archive` | |
| `Priority` | Select | — | `Urgent` · `High` · `Medium` · `Low` | |
| `Batch` | Number | — | Production batch | Property only — never in the Name |
| `Briefs` | Relation → `[DB] Briefs` | auto | — | 1 concept → N briefs |
| `Winners Count` | Rollup (sum of Briefs `Is Winner`) | auto | — | How many winning creatives this concept produced |
| `Strategist` | Person | — | — | |
| `Tasks` | Relation | — | — | |

## Hard rules

- Every concept must trace back to a **hypothesis** in the Roadmap DB (via the Learnings loop).
- Concept No. numbering is strict, sequential, per client.
- Page body: concept narrative only — properties are the single source of truth for status/IDs.

## Relations map

```
Persona ─┐
         ├──→ Concept ──→ Briefs ──→ Ads
Angle ───┘        └──→ Business Learnings · Roadmap (hypothesis loop)
```
