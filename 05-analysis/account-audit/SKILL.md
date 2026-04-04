---
name: account-audit
description: "Reviews the full Meta ad account performance over a defined period to identify top performers, underperformers, creative patterns, and structural gaps. Use quarterly or when performance drops unexpectedly. Trigger on: 'audit du compte', 'vue d'ensemble des performances', 'analyse macro', 'qu'est-ce qui marche dans le compte'. Produces a macro performance report with strategic recommendations."
metadata:
  version: 1.0.0
  status: stable
  tags: [analysis, account, performance, meta-ads, macro]
  inputs: [accès compte Meta Ads, période minimum 30 jours recommandé 90 jours]
  outputs: [rapport d'audit compte — top performers, patterns, gaps, recommandations]
  depends-on: [brand-health]
---

# Account Audit

## Before Starting

Confirme avant de commencer :
- [ ] Accès Meta Ads Manager (Campaigns, Ad Sets, Ads)
- [ ] Période définie : minimum 30 jours, recommandé 90 jours
- [ ] KPI primaire du compte connu (CPA / CPL / ROAS)
- [ ] `brand-context.md` disponible pour contexte produit et audience
- [ ] Données de spend suffisantes (compte avec < 1 000€ sur la période = données peu fiables)

Pour les benchmarks : voir [references/kpi-benchmarks.md](../ad-analysis/references/kpi-benchmarks.md)

---

## Phase 1 : Vue d'Ensemble Compte

Analyser au niveau campagne :

- Budget total dépensé sur la période
- Répartition du budget : testing / scaling / retargeting (%) 
- Nombre de campagnes actives vs pausées
- Évolution des performances semaine sur semaine (tendance haussière ou baissière)
- CPM moyen du compte (signal de compétitivité du compte)

---

## Phase 2 : Analyse des Creatives

Trier toutes les ads actives sur la période par dépense décroissante.

**Top 5 Performers :** Ads avec le meilleur KPI primaire ET dépense significative.
**Bottom 5 :** Ads avec le pire KPI primaire avec dépense significative.
**Ads non testées suffisamment :** Ads avec < 100€ de dépense — données non fiables.

Pour chaque top performer, noter :
- Format (vidéo / statique / carousel)
- Angle créatif (C1/C2/C3/C4)
- Awareness stage ciblé
- Hook tactic utilisée
- Mécanique créative

---

## Phase 3 : Identifier les Patterns

Comparer les top performers vs bottom performers :

- Y a-t-il un format dominant parmi les winners ?
- Y a-t-il un angle dominant parmi les winners ?
- Y a-t-il un awareness stage sur-représenté ?
- Y a-t-il des mécaniques absentes du compte ?
- Y a-t-il des personas non adressés ?

---

## Phase 4 : Identifier les Gaps Structurels

Analyser la structure du compte :

- Distribution TOF / MOF / BOF : est-elle équilibrée ?
- Fréquence des audiences chaudes : signal de saturation ?
- Rotation des creatives : quand la dernière nouvelle creative a-t-elle été lancée ?
- Budget testing : y a-t-il un budget dédié au test de nouveaux concepts ?

---

## Phase 5 : Recommandations

Structurer les recommandations en 3 catégories :
1. **Optimiser** — ce qui marche et peut être amplifié (augmenter budget, itérer)
2. **Killer** — ce qui consomme du budget sans résultat (stop immédiat)
3. **Tester** — ce qui manque et devrait être testé ce sprint

---

## Output Format

```markdown
# Account Audit — [Marque] — [Période] — [Date]

## Vue d'Ensemble
- Dépense totale : [X€]
- Répartition budget : TOF [%] / MOF [%] / BOF [%]
- KPI primaire moyen : [valeur] vs cible [valeur]
- Tendance : [Haussière / Stable / Baissière]

## Top 5 Performers
| Creative | Format | Angle | Awareness | KPI | Dépense |
[tableau]

## Bottom 5
| Creative | Format | Angle | Awareness | KPI | Dépense |
[tableau]

## Patterns Identifiés
**Ce qui marche :** [Format / Angle / Mécanique dominant]
**Ce qui échoue :** [Pattern commun des losers]

## Gaps Structurels
- Awareness non couverts :
- Formats non testés :
- Personas non adressés :
- Mécaniques absentes :

## Recommandations

### Optimiser
[Ce qu'on scale ou itère]

### Killer
[Ce qu'on stoppe — avec raison]

### Tester ce sprint
[3 nouveaux concepts prioritaires avec brief direction]
```

---

## Related Skills

- `01-audit/brand-health` — baseline initiale
- `05-analysis/ad-analysis` — pour aller plus loin sur chaque creative
- `05-analysis/strategy-gap` — pour approfondir les gaps identifiés
- `03-strategy/creative-brief` — pour briefe les nouveaux tests recommandés
