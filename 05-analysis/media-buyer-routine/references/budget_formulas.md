# RÉFÉRENCE — Formules Budget
**Type :** Référence générique  
**Usage :** Consulté par SKILL_media_buyer.md — Étapes 3, 4  
**Applicable à :** Lead Generation + E-commerce

---

## Formule 1 — Budget journalier optimal (sortie apprentissage)

Objectif : donner à l'algorithme assez de budget pour atteindre 50 conversions en 7 jours — seuil minimal pour sortir de la phase d'apprentissage.

```
Budget journalier = (CPA cible × 50) / 7

Exemples :
CPA cible 10€  → (10 × 50) / 7  = 71€/jour
CPA cible 25€  → (25 × 50) / 7  = 178€/jour
CPA cible 50€  → (50 × 50) / 7  = 357€/jour
CPA cible 100€ → (100 × 50) / 7 = 714€/jour
```

> Cette formule est un idéal théorique. En pratique, ajuster selon le budget disponible et lancer avec le minimum viable (voir Formule 2).

---

## Formule 2 — Budget de démarrage (phase de test)

Pour les nouveaux comptes ou nouvelles campagnes avec budget limité :

```
Budget de départ = 25€/jour par ad set (ABO)
Structure max recommandée en P1 : 2–3 ad sets simultanés
Budget total P1 = 25€ × nombre d'ad sets
```

> Ne pas dépasser 3 ad sets en simultané en phase de test. L'objectif est d'isoler les variables, pas de distribuer le budget.

---

## Formule 3 — Règle de scale (+20%)

Augmentation progressive du budget sur les ad sets gagnants :

```
Nouveau budget = Budget actuel × 1,20

Conditions requises avant d'appliquer :
[ ] 10+ conversions sur l'ad set
[ ] CPA dans la cible depuis 3 jours consécutifs
[ ] Dernière augmentation il y a 2–3 jours minimum

Fréquence maximale : 1 augmentation tous les 2–3 jours
Augmentation maximale par palier : 20% (jamais doubler d'un coup)
```

---

## Formule 4 — Seuil de dépense avant décision

Définit à partir de combien on peut prendre une décision fiable sur une annonce :

```
Décision trop tôt  : < 1x CPA cible dépensé     → Ne pas couper
Surveillance       : 1x – 2x CPA cible dépensé   → Surveiller
Kill rules actives : > 2x CPA cible dépensé       → Décision fiable

Point d'arrêt précoce (exception) :
CPC > 2x moyenne compte ET dépenses > 0,5x CPA → Couper immédiatement
```

---

## Formule 5 — Répartition budget par phase (compte mature)

Répartition indicative du budget total entre les phases actives :

| Phase | Allocation | Condition |
|---|---|---|
| P1 — Test créa | 40–50% | Toujours actif — alimenter le pipeline |
| P2 — Message Testing | Inclus dans P1 | Même structure, variations sur créas prouvées |
| P3 — Audience Testing | 20–25% | Activé après 1 créa prouvée |
| P4 — Scale | 25–30% | Activé après 5+ créas prouvées avec CPA ≤ cible |
| Re-engage | 5–10% | Activé après 1 000 leads cumulés |

---

## Formule 6 — Point d'arrêt par phase

| Phase | Dépense max avant décision | Logique |
|---|---|---|
| P1 | 2x CPA cible par annonce | Au-delà : la créa ne fonctionne pas |
| P2 | 2x CPA moyen par variation | Au-delà sans conversion : élément non performant |
| P3 | 2x–3x CPA par audience testée | Au-delà : audience non viable |
| P4 | CPA surveiller en continu | Kill si +30% CPA pendant 3 jours consécutifs |
