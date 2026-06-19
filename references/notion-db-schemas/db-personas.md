# 👥 [DB] Personas — Notion Schema

> Reference schema for the `Personas` database used by the Creative Strategist OS.

## Purpose

One entry per persona, per client. A persona here is **not a classic demographic sheet** —
it is built around a distinctive psycho-behavioral trait (story, biases, register), enriched
in 3 layers: ID card (selects) → what they say → what they really want.
Personas are grounded in evidence via the `Real Customers` relation and activated via
Angles → Concepts → Briefs.

## Database location (template)

- Teamspace : `MX Marketing` · Parent page : `[DB] DATABASES`
- Database title : `👥 [DB] Personas` — icon 👥

## Properties

### Identity & classification

| Property | Type | Options / Notes |
|---|---|---|
| `Name` | Title | Persona name (trait-based, e.g. "L'hypersensible fatiguée") |
| `Numéro` | Text | Stable persona number (used in naming, e.g. `P304`) |
| `Client` | Relation → `[DB] Clients` | ✅ required |
| `Type de profil` | Select | `Avatar Acheteur` · `Avatar Winner` · `Avatar Idéal` · `Avatar Actuel` |
| `Source` | Select | `Recherche audience` · `Imitation concurrent` · `Real Customer` · `Idéation` · `Hypothèse client` · `Audit ads` |

### Layer 1 — ID card (sociodemographic selects, chart-friendly)

| Property | Type | Options |
|---|---|---|
| `Genre` | Select | `Femme` · `Homme` · `Non-binaire / autre` · `Non précisé` |
| `Âge` | Number | exact age if known |
| `Tranche d'âge` | Select | `18–24` · `25–34` · `35–44` · `45–54` · `55+` |
| `Génération` | Select | `Gen Z` · `Millennial` · `Gen X` · `Boomer` |
| `CSP / Profession` | Select | `Entrepreneur` · `Salarié` · `Indépendant` · `Étudiant` · `Sans activité` · `Autre` |
| `Statut familial` | Select | `Célibataire` · `En couple` · `Parent` · `Parent solo` |

### Layers 2–3 — psychology (the real substance)

| Property | Type | Notes |
|---|---|---|
| `Layer 2 — Ce qu'ils disent` | Text | Expressed want ("je veux perdre du poids") |
| `Layer 3 — Ce qu'ils veulent vraiment` | Text | Deep motivation / job-to-be-done |
| `Problématiques` | Text | Pains |
| `Objections` | Text | |
| `Vocabulaire-clé` | Text | Their exact words (copy mining) |
| `Registre d'adresse` | Multi-select | `Entrepreneur` · `Maman` · `Hypersensible` · `Fatigué` · `TDAH` · `Stressé` · `Procrastinateur` |
| `Niveau Awareness` | Select | `Unaware` → `Most Aware` (Schwartz) |

### Activation & tracking

| Property | Type | Notes |
|---|---|---|
| `Real Customers` | Relation | Evidence base for this persona |
| `Angles probables` / `Angles validés` | Relations → Angles Library | Hypothesis vs proven |
| `Concepts` | Relation → `[DB] Concepts` | |
| `Business Learnings` / `Roadmap` / `Knowledge Base` | Relations | Closed loop |
| `# Briefs` / `# Concepts` | Formulas (count) | Usage tracking |
| `Work Status` | Formula | 🟢 Travaillé / ⚪ À démarrer |

## Relations map

```
Real Customers ──→ Personas ──→ Angles (probables/validés) ──→ Concepts ──→ Briefs
                      └──→ Business Learnings · Roadmap · Knowledge Base
```
