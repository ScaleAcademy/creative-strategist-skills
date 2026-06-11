# 📚 [DB] Knowledge Base — Notion Schema

> Reference schema for the `Knowledge Base` database used by the Creative Strategist OS.

## Purpose

Hosts every audit/research deliverable (brand context, audience research, market analysis,
competitor analysis, kill rules…). Its single job: **feed hypotheses**. One entry per document,
organized by Phase (the 5-phase workflow) and Block (thematic grouping).

**Content rule:** the Notion page body holds only the document's *generic role* (what it is,
how it's used). The actual filled content lives in a linked Google Doc (`Drive URL`) or a
local repo file (`Repo Path`). Notion = meta + role; Drive/repo = content.

**Template/instance pattern:** conceptual templates carry no `Client`; client instances are
linked to their client and may hold content directly in the body when short-lived.

## Database location (template)

- Teamspace : `MX Marketing` · Parent page : `[DB] DATABASES`
- Database title : `📚 [DB] Knowledge Base` — icon 📚

## Properties

| Property | Type | Required | Options / Format | Notes |
|---|---|---|---|---|
| `Doc` | Title | ✅ | Document name | |
| `Client` | Relation → `[DB] Clients` | instance only | — | Empty = conceptual template |
| `Phase` | Select | ✅ | `Phase 0 — Audit` · `Phase 1 — Research` · `Phase 2 — Strategy` · `Phase 3 — Production` · `Phase 4 — Analysis` | The 5-phase workflow |
| `Block` | Select | ✅ | `🎯 Market Analysis` · `👥 Audience Research` · `💼 Business` · `🎨 Brand` · `🧭 Strategy` · `📊 Analysis` | Thematic grouping (6 blocks) |
| `Type` | Select | ✅ | 26 doc types: `Market Context` · `Market Sophistication` · `Market Positioning` · `Competitor Analysis` · `Generational Insight` · `Verbatims` · `Persona` · `Real Customers` · `Business Brief` · `Offer Analysis` · `Ad Account Audit` · `Creative Performance Audit` · `Content Audit` · `Compliance & Claims` · `Performance Targets` · `Kill Rules` · `Brand Health` · `Brand Alignment` · `Brand Guidelines` · `Tone of Voice` · `Visual Identity` · `Roadmap` · `Strategy Brief` · `Performance Report — Business` · `Performance Report — Créa` · `Analysis Brief` | The doc taxonomy |
| `Status` | Status | ✅ | To-do: `Pas commencé` · `À faire` / In progress: `En cours` · `À mettre à jour` / Done: `Terminé` · `Validé` | |
| `Order #` | Number | — | 01–31 | Position in the Discovery process |
| `Fréquence de review` | Select | — | `Une fois` · `Hebdo` · `Mensuel` · `Trimestriel` · `Semestriel` · `Annuel` · `Ad hoc` | |
| `Prochaine review` | Date | — | — | |
| `Version` | Number | — | v1.0, v1.2… | Bump on every major rework, never overwrite |
| `In Agent` | Checkbox | — | — | Doc integrated into an AI agent's context |
| `Drive URL` | URL | — | — | The filled Google Doc |
| `Repo Path` | Text | — | `clients/[client]/…` | Local .md path |
| `Personas` | Relation → `[DB] Personas` | — | — | |
| `🤖 Prompts Library` | Relation | — | — | Prompts that generate this doc type |

## Relations map

```
[DB] Clients ←── Knowledge Base ──→ Personas · Prompts Library
       (feeds) ──→ Business / Creative Learnings (hypotheses)
```
