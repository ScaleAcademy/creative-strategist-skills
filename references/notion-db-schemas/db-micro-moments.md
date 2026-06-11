# 🎯 [DB] Micro-Moments — Notion Schema

> Reference schema for the `Micro-Moments` database used by the Creative Strategist OS.
> Anyone replicating this structure in their own Notion workspace can run all skills that depend on it.

## Purpose

A micro-moment is a **psychological truth written in first person** — the prospect's inner voice
at a precise instant: *"I look in the mirror and look away"*, *"It's midnight and I'm opening the
fridge again"*. It is media-independent: one micro-moment can be visualized by N assets
(b-roll, screen recording, 3D animation, creator footage).

This DB is the bridge between **research** (where micro-moments are mined from reviews,
sales-call transcripts, customer language) and **production** (where each micro-moment gets
sourced/shot as footage). It doubles as the **sourcing to-do list**.

**Naming rule:** the title is the raw first-person thought, never a flat label.
❌ "When you can't take it anymore" → ✅ "I look at myself in the mirror and look away."

## The matrix (organizing principle)

All micro-moments live on ONE horizontal axis with three simultaneous readings:

```
PAIN / PROBLEM ──────────────────────────────────────► ASPIRATION / RESULT
Problem → Failed solutions → Intro → Demo → Benefits → Desired result → Proof   (narrative arc)
Problem Aware ───────────────────────────────────────► Most Aware               (awareness)
```

- **Left side (pain):** sub-group by EMOTION (shame / pain / frustration / fear) — pain is emotional.
- **Right side (solution/product):** sub-group by FUNCTION (demo / benefits / result) — proof is rational.
- Each client *inhabits a zone*: a weight-loss coach covers the full arc anchored left (Problem Aware
  audience); a trading-bot product sits right (Product/Most Aware — you demo the working product,
  Problem columns stay nearly empty, and that's correct).
- Hooks overwhelmingly target the Problem zone — expect it to be the most populated.

## Database location (template)

- Teamspace : `MX Marketing` (or any client-facing workspace)
- Parent page : `[DB] DATABASES`
- Database title : `🎯 [DB] Micro-Moments`
- Default icon : 🎯

## Properties

| Property | Type | Required | Options / Format | Notes |
|---|---|---|---|---|
| `Micro-Moment` | Title | ✅ | First-person sentence | The inner voice, raw and specific |
| `Client` | Relation → `[DB] Clients` | ✅ | — | Each client has its own micro-moments |
| `Bloc / Phase` | Select | ✅ | `Problème` (red) · `Solutions échouées` (orange) · `Intro / Solution` (blue) · `Démo produit` (blue) · `Bénéfices` (yellow) · `Buying / Unboxing` (brown) · `Résultat désiré` (green) · `Preuve-Lifestyle` (purple) | Position on the narrative arc. `Buying / Unboxing` is for physical e-commerce products only — leave unused for services |
| `Émotion` | Select | ✅ | `Douleur` (red) · `Honte` (brown) · `Frustration` (orange) · `Peur` (purple) · `Espoir` (blue) · `Soulagement` (green) · `Fierté` (yellow) · `Neutre` (gray) | Emotional charge — distinct from visual style |
| `Niveau d'awareness` | Select | — | `UN — Unaware` · `PA — Problem Aware` · `SA — Solution Aware` · `PRA — Product Aware` · `MA — Most Aware` | Eugene Schwartz scale; aligned with the `NC` property of the Styles Library |
| `Statut sourcing` | Select | ✅ | `À sourcer` (gray) · `En cours` (yellow) · `Sourcé` (green) | Makes the DB a sourcing to-do list |
| `Hook-ready` | Checkbox | — | — | Strong enough to open a video. Hook is a POSITION (edit-time decision), never a folder |
| `Assets` | Relation → `[DB] Asset Library` (two-way) | — | — | The clips that visualize this micro-moment (many-to-many) |
| `Notes` | Text | — | Free text | Where the insight comes from (review, sales call, competitor ad) |

## Suggested views

| View | Type | Group by | Filter | Purpose |
|---|---|---|---|---|
| `🗺️ Matrix` | Board | `Bloc / Phase` | per Client | The horizontal arc, Milanote-mirror |
| `📥 To source` | Table | `Bloc / Phase` | `Statut sourcing = À sourcer` | Sourcing to-do |
| `🔥 Hooks` | Gallery | Émotion | `Hook-ready = true` | Hook bank per client |

## Workflow

1. **Define top-down** — mine micro-moments from existing research (reviews, setting-call
   transcripts, persona docs). Never start by collecting footage.
2. **Source targeted** — per micro-moment, find 3–5 clips (TikTok / Reels / Meta Ad Library / stock).
   Sourcing order: Problem → Desired result (both ends of the arc) → middle blocks.
3. **Capture opportunistic** — great clip found outside the list → create its micro-moment, add it.
4. **Rights flag** — competitor/TikTok clips are fine as *references in a brief*; for ads in
   production, re-shoot the moment or use licensed stock.

## Relations map

```
[DB] Clients ←── Micro-Moments ──→ [DB] Asset Library (two-way "Micro-Moments")
```
