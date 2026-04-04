---
name: campaign-setup
description: "Structures the Meta campaign for validated creatives: naming convention, campaign/ad set/ad architecture, budget allocation, and kill rules. Use after creative production is complete and assets are ready to upload. Trigger on: 'structure la campagne', 'setup Meta', 'nomenclature', 'comment organiser les campagnes'. Produces a ready-to-launch campaign structure."
metadata:
  version: 1.0.0
  status: beta
  tags: [production, meta-ads, campaign, setup, nomenclature]
  inputs: [creatives validées prêtes à uploader, objectif campagne, budget]
  outputs: [structure campagne Meta + nomenclature + kill rules]
  depends-on: [creative-brief, static-production, video-production]
---

# Campaign Setup

## Before Starting

Confirme avant de commencer :
- [ ] Creatives finales prêtes (fichiers vidéo / images exportés aux bons formats)
- [ ] Objectif de campagne défini : Conversions / Leads / Trafic / Notoriété
- [ ] Budget journalier ou total défini
- [ ] Pixel Meta installé et événements vérifiés
- [ ] URL de destination / landing page prête et trackée
- [ ] KPI cible défini (CPA, CPL, ROAS)

---

## Phase 1 : Architecture de Campagne

### Structure en 4 Phases

**P1 — Test Créatif**
- Objectif : Identifier les creatives qui performent
- Budget : 20–40€/jour par ad set
- Audience : Froide (intérêts larges ou lookalike 1–3%)
- Creatives : 3–5 ads par ad set (1 ad set par angle testé)
- Durée avant décision : 3–5 jours minimum, 50€+ dépensés

**P2 — Retargeting**
- Objectif : Récupérer les engagés et visiteurs
- Budget : 10–20€/jour
- Audience : Visiteurs site (30j), engagés page/profil (30j), vues vidéo 25%+ (14j)
- Creatives : 2–3 ads BOF (objection / offre directe)

**P3 — Scale Winners**
- Objectif : Amplifier ce qui a prouvé ses performances en P1
- Budget : 2–5× le budget de test initial
- Audience : Lookalike 1% des acheteurs ou leads
- Creatives : Top 1–2 winners uniquement

**P4 — Re-engage**
- Objectif : Réactiver les anciens prospects et clients
- Budget : 10€/jour
- Audience : Leads anciens (90j+), clients (180j+), engagés anciens
- Creatives : Nouveauté / offre exclusive / contenu de valeur

---

## Phase 2 : Nomenclature

Nommer systématiquement pour pouvoir analyser et filtrer rapidement.

**Format Campagne :**
`[Marque]_[Phase]_[Objectif]_[Date]`
Exemple : `SA_P1_Conversion_2026-04`

**Format Ad Set :**
`[Audience]_[Awareness]_[Angle]`
Exemple : `Cold-FR_ProblemAware_C1-Douleur`

**Format Ad :**
`[Format]_[Hook-ID]_[Creative-ID]`
Exemple : `VID30s_H03_CRE-007`

---

## Phase 3 : Kill Rules

Définir à l'avance les critères d'arrêt pour éviter les décisions émotionnelles.

| Métrique | Kill Rule |
|---|---|
| CPA | > [cible × 1.5] après 50€ dépensés |
| CTR | < 0.8% après 30€ dépensés (statique) |
| Hook Rate | < 15% après 20€ dépensés (vidéo) |
| CPL | > [cible × 2] après 3 leads |
| Fréquence | > 3 en 7 jours → renouveler creative |

**Règle des 72h :** Ne pas killer une ad avant 72h sauf si le CPA est > 3× la cible. Laisser l'algorithme apprendre.

---

## Output Format

```markdown
# Campaign Setup — [Marque] — [Date]

## Architecture

### P1 — Test Créatif
Nom campagne : [Nom]
Budget : [X€/jour]
Ad Sets :
  - [Nom ad set 1] → [Creatives : ID1, ID2, ID3]
  - [Nom ad set 2] → [Creatives : ID4, ID5, ID6]

### P2 — Retargeting
[Même structure]

### P3 — Scale (à activer si P1 winner)
[Même structure]

### P4 — Re-engage
[Même structure]

## Kill Rules Actives
| Métrique | Seuil | Action |
[tableau]

## Checklist Avant Lancement
- [ ] Pixel vérifié
- [ ] Événements trackés (PageView, InitiateCheckout, Purchase / Lead)
- [ ] URL UTMs configurées
- [ ] Budget journalier total ≤ budget mensuel / 30
- [ ] Creatives approuvées Meta (format + compliance)
- [ ] Kill rules documentées dans le tracker
```

---

## Related Skills

- `04-production/static-production` — source des assets
- `04-production/video-production` — source des assets
- `05-analysis/ad-analysis` — après 3–5 jours de diffusion
- `01-audit/brand-health` — benchmark pour les kill rules
