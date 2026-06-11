# 📝 [DB] Briefs — Notion Schema

> Reference schema for the `Briefs` database used by the Creative Strategist OS.

## Purpose

**1 Brief = 1 creative to produce** (one style execution of a concept). The production
contract: format, hook direction, specs, pipeline status, people, deadlines, result.
Hook variants live INSIDE the brief body (a brief can carry 5 hook options) — never one
brief per hook variant.

ID convention: `#019-B1` (concept number + brief index).

## Database location (template)

- Teamspace : `MX Marketing` · Parent page : `[DB] DATABASES`
- Database title : `📝 [DB] Briefs` — icon 📝
- Page templates: `Brief Standard MX`, `IMG`, `CAR`, `VID`, `UGC Problem/Solution`

## Properties

### Identity & strategy

| Property | Type | Options / Notes |
|---|---|---|
| `Name` | Title | `#019-B1 — short label` |
| `Concept` | Relation → `[DB] Concepts` | ✅ — parent concept |
| `Concept #` | Rollup (Concept No.) | for naming |
| `Client` | Rollup via Concept | display |
| `Client (direct)` | Relation → `[DB] Clients` (limit 1) | for filters & dashboards |
| `Numéro` / `Variant` / `Batch` | Numbers | sequencing; Batch = property only |
| `Type` | Select | `New` · `Itération` |
| `Format` | Select | `Image` · `GIF` · `Carousel` · `Video Short` · `Long Video` |
| `Angle Category` | Select | `C1 — Demonstration` · `C2 — Educational` · `C3 — Pain` · `C4 — Identity` |
| `Awareness Level` | Select | `UN` → `MA` (Schwartz) |
| `Hook Type` | Select | `Pain` · `Question` · `Stat` · `Social Proof` · `Pattern Interrupt` · `Transformation` · `Contrarian` — ⚠️ see Known issues |
| `Hypothesis` | Text | the tested hypothesis (link the Roadmap item too) |
| `Hypothesis Result` | Select | `✅ Validated` · `❌ Invalidated` · `⏳ Inconclusive` |
| `🎨 Style(s)` | Relation → Styles Library | creative style reference |
| `🎯 Angles & Hooks Library` | Relation | |
| `Inspirations` | Relation | reference creatives |

### Production pipeline

| Property | Type | Notes |
|---|---|---|
| `Status` | Status | `🧠 Draft` → `📝 Scripting` → `🎬 In Production` → `✂️ In Editing` → `✅ Approved` → `📅 Scheduled` → `🚀 Published`. **Driven by automations (checkboxes + dates) — never set by hand or by skills.** |
| `Script Done` / `Script Approved` / `Filming Done` / `Edit Done` / `Edit Approved` | Checkboxes | these drive the Status automations |
| `Scripting Due` / `Filming Due` / `Editing Due` / `Delivery Due` / `Filming Delivered` / `Delivered` / `Publish Date` / `Date Creation` | Dates | |
| `Creative Strategist` / `Creator` / `Editor` / `Reviewer` / `Traffic Manager` | Person | |
| `Talent` | Relation → Creators | human or AI avatar on screen |
| `Rushs` / `Link` | URL | footage + final asset |
| `Priority` | Select | `Urgent` · `High` · `Medium` · `Low` |

### Results

| Property | Type | Notes |
|---|---|---|
| `Result` | Select | `🏆 Winner` · `🧪 Testing` · `⏸ Untested` · `❌ Loser` |
| `Is Winner` | Formula | feeds Concept's Winners Count rollup |
| `Learning` | Relation → Business Learnings | what this creative taught us |

## Known issues / planned changes

- `Hook Type` as a DB property is misleading when a brief contains N hook variants —
  house rule says hook types belong in the page body. Property kept for single-hook briefs;
  do not rely on it for multi-hook briefs.

## Relations map

```
Concept ──→ Brief ──→ Ad (published creative)
              ├──→ Style(s) · Angles & Hooks · Talent · Inspirations
              └──→ Creative/Business Learnings · Roadmap (hypothesis)
```
