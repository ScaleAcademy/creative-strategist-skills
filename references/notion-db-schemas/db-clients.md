# 📂 [DB] Clients — Notion Schema

> Reference schema for the `Clients` database used by the Creative Strategist OS.
> This is the **hub DB**: every other DB relates back to it. Replicate it FIRST.

## Purpose

One entry per client (or internal entity treated as a client). Holds the commercial frame
(type, status, budget, goal) and acts as the central node every other DB links to —
filtering anything "per client" anywhere in the OS goes through this relation.

## Database location (template)

- Teamspace : `MX Marketing` (or any client-facing workspace)
- Parent page : `[DB] DATABASES`
- Database title : `📂 [DB] Clients` — icon 📂
- Page template: `Client — MX Marketing (Template)` (client home page structure)

## Properties

| Property | Type | Required | Options / Format | Notes |
|---|---|---|---|---|
| `Client` | Title | ✅ | Client name | Use a codename if confidentiality requires it |
| `Code` | Text | ✅ | Short code (e.g. `YUM`, `AUT`) | Used in IDs and file naming |
| `Type` | Select | ✅ | `Interne` · `Externe` · `Partenaire` | |
| `Status` | Select | ✅ | `Actif` · `Inactif` | |
| `Platform` | Multi-select | — | `Meta Ads` · `Google Ads` · `Instagram` · `TikTok` · `YouTube` | Active ad platforms |
| `Main Goal` | Text | — | Free text | Primary business objective |
| `Monthly Budget` | Number (€) | — | — | Ad spend |
| `Monthly Revenue` | Number (€) | — | — | |
| `Monthly Target` | Number | — | — | |
| `Contract End Date` | Date | — | — | |
| `Internal Owner` | Person | — | — | |
| `Brand Guidelines URL` / `Drive URL` / `URL` | URL | — | — | External pointers |

## Relations (auto-created when the other DBs are replicated)

`Personas` · `Knowledge Base` · `Real Customers` · `Learnings` (Business Learnings) ·
`Creative Learnings` · `Roadmap` · `Assets` (Asset Library) · `Creators` · `People` · `Tasks`

## Relations map

```
                 ┌── Personas ── Concepts ── Briefs
[DB] Clients ────┼── Knowledge Base
   (hub)         ├── Real Customers
                 ├── Business / Creative Learnings ── Roadmap
                 └── Asset Library ── Micro-Moments
```
