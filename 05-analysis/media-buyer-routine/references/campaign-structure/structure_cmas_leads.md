# RÉFÉRENCE — Structure Campagne CMAS — Lead Generation
**Type :** Référence générique  
**Usage :** Consulté par SKILL_media_buyer.md — Étape 4  
**Méthode :** CMAS (Creative, Message, Audience, Scale)  
**Objectif campagne :** LEADS

---

## Vue d'ensemble

| Phase | Nom | Ce qu'on teste | Ce qu'on fixe | Prérequis |
|---|---|---|---|---|
| P1 | Wow Idea | Créatif, hook, format | Audience large connue | Aucun |
| P2 | Message Testing | Titres, accroches, variations | Créa prouvée + meilleure audience | 1 créa prouvée P1 |
| P3 | Audience Testing | Nouvelles audiences | Créa + copy prouvées | 1 créa prouvée P1/P2 |
| P4 | Scale | Budget, duplication | Créa + audience prouvées | 10+ conversions, CPA dans cible |

> **Règle d'or :** Ne jamais tester deux variables simultanément. Ne jamais scaler ce qui n'est pas prouvé. Ne jamais sauter une phase.

---

## Phase 1 — Wow Idea (Test Créatif)

### Objectif
Identifier une créa qui atteint le CPA cible avec 10+ conversions.

### Configuration
| Paramètre | Valeur |
|---|---|
| Type de budget | ABO |
| Budget | 25€/jour par ad set |
| Nb d'annonces | 2 annonces, 1 variation (copy OU créa — pas les deux) |
| Objectif campagne | LEADS |
| Placements | Facebook Feed + Instagram Feed uniquement |
| Ciblage | Large (broad) ou 1 grand intérêt — France |
| Options désactivées | Advantage+, test A/B Meta, texte IA Meta |

### Ordre de test des variables
1. Hook (impact maximal sur les performances)
2. Angle (C1 Démonstration / C2 Éducatif / C3 Douleur / C4 Identité)
3. Format (vidéo / statique / carousel)
4. Body / script
5. CTA (impact minimal — tester en dernier)

### Kill rules P1
| Déclencheur | Condition | Action |
|---|---|---|
| Point d'arrêt précoce | CPC > 2x moyenne + dépenses > 0,5x CPA cible | Désactiver |
| Point d'arrêt standard | Dépenses > 1x–2x CPL cible sans conversion | Désactiver |
| Point d'arrêt absolu | Dépenses > 2x CPA cible, 0 conversion | Tuer l'ad set |

### Critères de validation (passage P1 → P4)
```
[ ] Portée : 6 000+ impressions
[ ] Clics : 200+ clics sur le lien
[ ] Conversions : 10+ leads
[ ] CPA : dans la fourchette cible
[ ] CVR : ≥ 2%
[ ] Durée : CPA dans la cible 3 jours consécutifs
```

---

## Phase 2 — Message Testing

### Objectif
Optimiser les éléments de l'annonce gagnante. Identifier les titres et accroches qui améliorent les performances.

### Configuration
| Paramètre | Valeur |
|---|---|
| Type de budget | ABO |
| Budget | 25€/jour par ad set |
| Nb de variations | 10 max (titres, accroches, vignettes) |
| Seuil de décision | 400 impressions par annonce |
| Audience | Meilleure audience connue uniquement |
| Placements | Facebook Feed + Instagram Feed uniquement |

### Règles P2
- Tester UNE variable à la fois : titre OU accroche OU créa
- 80% du concept doit rester prouvé — micro-variations seulement
- Si CPM + CPC élevés dès le départ : couper — la créa ne capte pas l'attention
- Règle de coupe : dépenses > 2x CPA moyen + conversions < 1 → désactiver

### Priorité des éléments à tester
1. Accroche (première ligne du texte) — impact direct sur le CPC
2. Titre (headline de l'annonce)
3. Vignette / première frame vidéo
4. Transformation de format (carousel → GIF, vidéo → statique)

---

## Phase 3 — Audience Testing

### Objectif
Identifier les audiences qui performent avec les créas et copy prouvées.

### Configuration
| Paramètre | Valeur |
|---|---|
| Type de budget | ABO |
| Budget | 1x–2x CPA cible par ad set |
| Annonces | 3 meilleures annonces prouvées uniquement |
| Audiences | Nouvelles uniquement — intérêts non encore testés |
| Seuil de décision | 2x–3x CPA dépensé par audience |

### Règle de coupe P3
```
Dépenses > 2x–3x CPA cible sur l'audience → couper l'annonce d'abord, puis l'ad set
```

### Types d'audiences à tester
1. Nouveaux intérêts proches des audiences prouvées
2. LAL acheteurs / leads existants (pas pixel LAL dans un premier temps)
3. Audiences larges sans intérêt (broad — laisser l'algorithme optimiser)

---

## Phase 4 — Scale

### Objectif
Maximiser le volume sur les créas et audiences prouvées.

### Configuration
| Paramètre | Valeur |
|---|---|
| Type de budget | CBO (budget au niveau campagne) |
| Activation | 5+ créas prouvées avec CPA ≤ cible + min. 10 conversions chacune |
| Audiences | Prouvées en P3 + broad |
| Annonces | Uniquement des créas prouvées — aucune créa non testée |

### Règles de scale
```
[ ] Augmenter de 20% maximum tous les 2–3 jours
[ ] Ne jamais doubler le budget d'un coup
[ ] Si CPA spike après augmentation : attendre 48h avant de corriger
[ ] Dupliquer les ad sets gagnants plutôt qu'augmenter un seul indéfiniment
[ ] Surveiller la fréquence : si > 2,5 en broad → audience commence à saturer
[ ] Toujours avoir P1 actif en parallèle pour alimenter de nouvelles créas
```

### Quand P4 s'essoufle
Cause n°1 : fatigue créative — pas l'audience, pas le budget, pas les enchères.
Action : retourner en P1, trouver de nouvelles créas gagnantes, les injecter en P4.
Le cycle est continu : **Test → Message → Audience → Scale → Test...**

---

## Nomenclature campagnes

```
[MARQUE]_[PHASE]_[OBJECTIF]_[DATE]

Exemples :
CLIENT_P1-CREA_HOOKS_2026-04
CLIENT_P2-MSG_TITRES_2026-04
CLIENT_P3-AUD_INTERET-TRADING_2026-04
CLIENT_P4-SCALE_WINNERS_2026-04
```
