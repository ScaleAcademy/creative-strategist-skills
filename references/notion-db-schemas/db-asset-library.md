# 📦 [DB] Asset Library — Notion Schema

> Reference schema for the `Asset Library` database used by the Creative Strategist OS.
> Anyone replicating this structure in their own Notion workspace can run all skills that depend on it.

## Purpose

Catalog of every production asset (b-roll, music, SFX, voice, images, overlays, motion graphics,
templates) across clients. This is the **lightweight DAM** (Digital Asset Management) of the OS:
heavy files live in Google Drive / Milanote; this DB holds the metadata that makes them
**findable by any axis** (client, type, mood, micro-moment, source).

Don't pay for a dedicated DAM (Iconik etc.) until volume genuinely hurts —
several hundred clips or external collaborators searching without you.

## Database location (template)

- Teamspace : `MX Marketing` (or any client-facing workspace)
- Parent page : `[DB] DATABASES`
- Database title : `📦 [DB] Asset Library`
- Default icon : 📦

## Properties

| Property | Type | Required | Options / Format | Notes |
|---|---|---|---|---|
| `Name` | Title | ✅ | Free text | Follow the client's file naming convention |
| `Client` | Relation → `[DB] Clients` | ✅ | — | Which client the asset belongs to |
| `Type` | Select | ✅ | `B-roll` · `SFX` · `Music` · `Voice` · `Image` · `Overlay` · `Motion graphic` · `Template` | Main asset category |
| `Source` | Select | — | `UGC creator` · `AI gen` · `Stock library` · `Client archives` · `In-house shot` | Provenance — also encodes the rights situation |
| `Mood / Style` | Multi-select | — | `Energetic` · `Emotional` · `Action` · `Calm` · `Tension` · `Reveal` (+ legacy: `Micro-moment`, `Talking head`, `Screen recording`) | Qualitative search tags. ⚠️ See Known issues |
| `Micro-Moments` | Relation → `[DB] Micro-Moments` (two-way `Assets`) | — | — | Which inner-voice moments this asset can visualize |
| `Status` | Select | — | `Active` · `Archived` | Active = visible day-to-day |
| `Drive URL` | URL | — | — | Direct link to the file on Google Drive |
| `Duration (s)` | Number | — | seconds | For video and audio |
| `Preview` | Files | — | — | Thumbnail visible in Notion |
| `Notes` | Text | — | Free text | When to use it, restrictions, context |
| `Created` | Created time | auto | — | — |

## Suggested views

| View | Type | Group by | Filter | Purpose |
|---|---|---|---|---|
| `Default view` | Table | Client | — | Full catalog |
| `🎞️ B-rolls` | Gallery (Preview) | Client | `Type = B-roll` | Visual browse |
| `🔌 Unlinked` | Table | Client | `Type = B-roll` AND `Micro-Moments is empty` | B-rolls not yet mapped to a moment |

## Known issues / planned changes

- `Mood / Style` currently mixes three dimensions: emotions (`Emotional`, `Calm`, `Tension`),
  formats (`Talking head`, `Screen recording`) and the `Micro-moment` concept itself.
  **Target state:** emotions stay (or move to a dedicated `Émotion` select aligned with
  Micro-Moments), formats move to `Type` or a `Format` property, and the `Micro-moment` tag is
  replaced by the `Micro-Moments` relation. Migrate only after checking which assets carry the
  legacy tags (destructive otherwise).
- Community template ships the **clean** version directly.

## Relations map

```
[DB] Clients ←── Asset Library ──→ [DB] Micro-Moments (two-way)
```
