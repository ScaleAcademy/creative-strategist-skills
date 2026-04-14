# RÉFÉRENCE — Kill Rules
**Type :** Référence générique  
**Usage :** Consulté par SKILL_media_buyer.md — Étape 2  
**Applicable à :** Lead Generation (ajuster les seuils CPA pour e-com)

---

## Principe fondamental

Les kill rules retirent l'émotion des décisions d'optimisation. Quand une métrique franchit un seuil sur une période définie, on coupe — sans débat, sans "encore un jour".

> **Règle d'application :** Les kill rules se définissent AVANT le lancement. Jamais après. Les seuils spécifiques au client remplacent ceux-ci — voir `clients/[CLIENT]/kill_rules.md`.

---

## Protection phase d'apprentissage

Avant d'appliquer toute kill rule, vérifier où on en est :

| Dépenses vs CPA cible | Statut |
|---|---|
| < 1x CPA cible | Ne pas couper — trop tôt |
| 1x – 2x CPA cible | Surveiller — couper uniquement si Hook Rate < 15% |
| > 2x CPA cible | Kill rules pleinement actives |

---

## Niveau Annonce (Ad)

| Métrique | Seuil de coupe | Délai | Exception |
|---|---|---|---|
| Hook Rate (vues 3s) | < 20% | Après 1 000 impressions | Aucune |
| CTR (lien) | < 1,0% | Après 2 000 impressions | Retargeting BOF : vérifier CPA d'abord |
| CPC | > 2x moyenne compte | Après 500 clics | High-ticket : tolérable si CPA dans la cible |
| CPA | > 1,5x CPA cible | Après 2x CPA dépensé | Nouvelles annonces : attendre fin apprentissage |
| 0 conversion | 0 conversion | Après 2x CPA dépensé | Aucune |
| Complétion vidéo 15s | < 5% | Après 1 000 vues | Vidéos longues : ajuster proportionnellement |
| Fréquence | > 3,0 | Rolling 7 jours | Si performance maintenue : surveiller sans couper |

**Point d'arrêt précoce (avant 2x CPA dépensé) :**
> CPC > 2x moyenne compte ET dépenses > 0,5x CPA cible → Désactiver immédiatement

---

## Niveau Ad Set

| Métrique | Seuil de coupe | Délai | Action |
|---|---|---|---|
| CPA | > 2x CPA cible | Après 3x CPA dépensé | Pause. Revoir audience ou créa. |
| 0 conversion | 0 conversion | Après 2x CPA dépensé | Pause. Combo audience/créa inefficace. |
| CTR en chute | Baisse 50%+ vs 3 premiers jours | Rolling 7 jours | Fatigue créative. Remplacer avant relance. |
| CPM spike | > 2x moyenne compte | Pendant 3+ jours consécutifs | Audience trop étroite. Élargir le ciblage. |

---

## Niveau Campagne

| Métrique | Seuil de coupe | Délai | Action |
|---|---|---|---|
| CPA global | > 2x CPA cible | Pendant 7+ jours | Restructurer. Revoir ciblage, mix créatif, funnel. |
| Livraison budget | < 50% du budget journalier | 3 jours consécutifs | Audience trop petite ou enchère trop basse. |
| Learning Limited | Bloqué en apprentissage | 7+ jours après lancement | Consolider ad sets. Élargir audience. Augmenter budget par ad set. |

---

## Chemin d'escalade

Quand une kill rule est déclenchée, suivre cet ordre :

```
1. PAUSE (ne pas supprimer — conserver les données)
2. DOCUMENTER : métrique, valeur, seuil, dépenses au moment de la coupe
3. DIAGNOSTIQUER la cause racine :
   - Hook raté       → Nouveaux hooks, même body + offre
   - Body raté       → Réécrire le body, conserver le hook gagnant
   - Audience ratée  → Même créa, ciblage différent
   - Offre ratée     → Nouvelle offre/CTA, même créa
   - Tout raté       → Nouveau concept créatif from scratch
4. CORRIGER et relancer
5. APPLIQUER les mêmes kill rules sur la nouvelle version
```

---

## Ajustements saisonniers

| Période | Tolérance CPA | CPM attendu | CPC attendu |
|---|---|---|---|
| Normal | 1,5x cible | Baseline | Baseline |
| Q4 (Nov–Déc) | 2x cible | +30 à +60% | +50 à +100% |
| Janvier (faible concurrence) | 1,2x cible | -20 à -30% | -20 à -30% |
| Lancement produit | 2x cible (2 premières semaines) | Élevé attendu | Élevé attendu |
