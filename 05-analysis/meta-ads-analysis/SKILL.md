---
name: meta-ads-analysis
description: "Runs a full Meta Ads account analysis in 7 steps using Windsor.ai as MCP data bridge. Pulls live campaign/creative/audience data directly into Claude and produces an actionable audit report: account health, campaign audit, creative lifecycle, angle & format performance, audience analysis, and prioritized action plan. Trigger on: 'analyse mon compte Meta', 'audit Meta Ads', 'quelles pubs tuner', 'creative analysis Meta', 'analyse Windsor'. Requires Windsor.ai MCP connection."
metadata:
  version: 1.0.0
  status: stable
  tags: [analysis, meta-ads, performance, creative, windsor, mcp, account-audit]
  inputs: [Compte Meta Ads connecté via Windsor.ai MCP, convention de nommage appliquée (optionnel mais recommandé)]
  outputs: [Rapport 7 sections : santé compte + audit campagnes + lifecycle créatives + angles & formats + audiences + plan d'action priorisé]
  depends-on: [brand-guidelines, ad-analysis]
---

# Meta Ads Analysis — Système Complet (Claude + Windsor.ai)

## Before Starting

Confirme avant de commencer :
- [ ] Windsor.ai MCP connecté et fonctionnel dans Claude Desktop
- [ ] Accès au compte Meta Ads cible (via Windsor.ai)
- [ ] Période d'analyse définie (recommandé : 30 derniers jours minimum)
- [ ] KPI cible connu (CPA cible, CPL, ROAS)
- [ ] Convention de nommage appliquée (voir [references/windsor-setup.md](references/windsor-setup.md)) — fortement recommandée pour l'analyse créative

Si Windsor.ai n'est pas encore configuré : voir [references/windsor-setup.md](references/windsor-setup.md) — setup en 4 étapes.

---

## Phase 0 : Setup & Connexion

Avant toute analyse, initialiser la connexion et définir le contexte.

**Prompt :**
```
Connecte-toi à mon compte Meta Ads via Windsor.ai.
Liste tous les comptes publicitaires disponibles.
Je veux analyser [NOM DU COMPTE] sur les [X] derniers jours.
Mon objectif principal est [acquisition / lead gen / awareness].
Mon KPI cible est [CPA cible X€ / CPL cible X€ / ROAS cible X].
```

**Résultat attendu :**
- Confirmation de connexion
- Liste des comptes disponibles
- Période et contexte de l'analyse confirmés

---

## Phase 1 : Santé du Compte

Obtenir une vue macro de la santé globale du compte avant d'entrer dans les détails.

**Prompt :**
```
Donne-moi un résumé global de la santé du compte [NOM] sur les [X] derniers jours :
- Dépense totale et évolution vs période précédente
- CPA / CPL / ROAS global vs ma cible ([X€])
- Nombre de campagnes actives, d'adsets, de creatives en diffusion
- Répartition du budget par campagne (% de la dépense totale)
- Top 3 campagnes en dépense et leur performance respective
- Signaux d'alerte : budget concentration, fréquence élevée, fatigue détectée
```

**Ce qu'on cherche :**
- Identifier si le compte est sain ou en dérive
- Repérer les campagnes qui monopolisent le budget sans performer
- Avoir une baseline avant l'analyse détaillée

---

## Phase 2 : Audit Campagnes

Analyser chaque campagne en détail pour identifier les maillons faibles et les gagnantes.

**Prompt :**
```
Pour chaque campagne active sur les [X] derniers jours, donne-moi :
- Nom de la campagne
- Objectif (awareness / traffic / conversion / etc.)
- Dépense totale
- Impressions, Reach, Fréquence moyenne
- CTR (link click-through rate)
- CPA / CPL / ROAS selon l'objectif
- Statut : Winner / Learner / Loser (par rapport à ma cible [X€])
- Recommandation : Scaler / Maintenir / Optimiser / Couper

Trie par dépense décroissante.
```

**Règles de verdict :**
- **Winner :** KPI primaire ≤ cible × 0.9
- **Learner :** KPI primaire entre cible × 0.9 et cible × 1.3, ou dépense insuffisante
- **Loser :** KPI primaire > cible × 1.5 avec dépense suffisante (>200€)

---

## Phase 3 : Lifecycle des Créatives

Identifier l'état de vie de chaque creative : montante, au pic, en fatigue, ou morte.

**Prompt :**
```
Analyse le lifecycle de chaque creative active sur les [X] derniers jours.
Pour chaque creative :
- Nom / ID
- Dépense totale et date de lancement
- Évolution du CPA semaine par semaine (ou période par période)
- Hook Rate (ThruPlay / Impressions si vidéo)
- Fréquence actuelle
- Phase de vie estimée : Montante / Pic / Déclin / Fatiguée / Morte
- Action recommandée : Laisser tourner / Booster budget / Ralentir / Couper

Identifie les 3 creatives qui montrent des signes de fatigue les plus marqués.
Identifie les 3 creatives avec la meilleure dynamique récente.
```

**Signaux de fatigue :**
- CPA en hausse de >20% sur 7 jours consécutifs
- CTR en baisse de >30% vs première semaine
- Fréquence > 3.5 sur audience froide

---

## Phase 4 : Performance par Angle & Format

Analyser quelle mécanique créative et quel format performent le mieux — pour orienter les prochaines productions.

**Prompt :**
```
En utilisant les noms des creatives, analyse les performances par angle et par format.

Par angle créatif (codes dans le nom : PR / RS / ED / ID — voir convention) :
- Dépense totale par angle
- CPA moyen par angle
- CTR moyen par angle
- Nombre de creatives testées par angle
- Angle le plus rentable vs angle le moins rentable

Par format (codes dans le nom : VID / STA / CAR — voir convention) :
- Même métriques que ci-dessus
- Hook Rate moyen (vidéo uniquement)
- Durée optimale (vidéo : 15s / 30s / 60s+)

Conclusion : quels angles et formats prioriser pour les prochaines créations ?
```

**Note :** Si la convention de nommage n'est pas appliquée, cette analyse sera manuelle. Voir [references/windsor-setup.md](references/windsor-setup.md) pour adopter la convention.

---

## Phase 5 : Analyse Audiences

Identifier quelle audience répond le mieux et détecter les problèmes de ciblage.

**Prompt :**
```
Analyse les performances par audience sur les [X] derniers jours :

Par adset / audience :
- Nom de l'audience
- Type : Prospection froide / Lookalike / Retargeting / Warm
- Dépense totale
- CPA / CPL / ROAS
- Fréquence
- Taille d'audience estimée
- Statut : Winner / Learner / Loser

Questions spécifiques :
- Y a-t-il des overlaps d'audience suspects ?
- Quelle audience cold fonctionne le mieux ?
- Le retargeting performe-t-il mieux que la prospection ?
- Y a-t-il des signaux de saturation d'audience (fréquence > 4 + CPA en hausse) ?
```

---

## Phase 6 : Plan d'Action Priorisé

Synthétiser tous les constats en un plan d'action concret, priorisé par impact potentiel.

**Prompt :**
```
Sur la base de toute l'analyse précédente (santé compte, campagnes, lifecycle, angles, formats, audiences), génère un plan d'action priorisé pour les 7 prochains jours.

Format :
## Actions Immédiates (à faire aujourd'hui)
- [Action] → [Raison] → [Impact attendu]

## Actions Cette Semaine
- [Action] → [Raison] → [Impact attendu]

## Prochaines Productions Recommandées
Basé sur les angles qui performent et ceux qui manquent :
- Creative à tester #1 : [Angle / Format / Mécanique recommandée]
- Creative à tester #2 : [Angle / Format / Mécanique recommandée]
- Creative à tester #3 : [Angle / Format / Mécanique recommandée]

## Hypothèses à Valider
- H1 : Si on [X], alors [KPI] devrait [direction] parce que [signal].
- H2 : [Même structure]
- H3 : [Même structure]
```

---

## Output Format

```markdown
# Meta Ads Analysis — [Marque] — [Période] — [Date]
*Outil : Windsor.ai MCP | Compte : [ID] | Dépense analysée : [X€]*

## Phase 0 — Contexte
- Compte : [Nom]
- Période : [Du XX au XX]
- KPI cible : [CPA X€ / CPL X€ / ROAS X]
- Objectif : [Acquisition / Lead / Awareness]

## Phase 1 — Santé du Compte
[Tableau récapitulatif + signaux d'alerte]

## Phase 2 — Audit Campagnes
[Tableau Winner / Learner / Loser par campagne]

## Phase 3 — Lifecycle Créatives
[Top 3 en déclin + Top 3 en croissance + tableau complet]

## Phase 4 — Angles & Formats
[Performance par angle + par format + conclusion prochaines créas]

## Phase 5 — Audiences
[Tableau par audience + overlaps + saturation]

## Phase 6 — Plan d'Action
[Actions immédiates + cette semaine + prochaines productions + hypothèses]
```

---

## Références

- [references/windsor-setup.md](references/windsor-setup.md) — Installation Windsor.ai MCP + convention de nommage complète
- [../ad-analysis/references/kpi-benchmarks.md](../ad-analysis/references/kpi-benchmarks.md) — Benchmarks de référence par plateforme et objectif

## Related Skills

- `05-analysis/ad-analysis` — analyse d'une creative individuelle (complément micro)
- `05-analysis/account-audit` — audit stratégique macro du compte
- `05-analysis/strategy-gap` — si l'analyse révèle des angles manquants
- `03-strategy/creative-brief` — pour briefer les prochaines productions issues du plan d'action
- `04-production/campaign-setup` — pour paramétrer les nouvelles campagnes post-analyse
