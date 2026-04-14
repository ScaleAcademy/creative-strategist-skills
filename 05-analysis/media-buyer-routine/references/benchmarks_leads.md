# RÉFÉRENCE — Benchmarks Meta Ads — Lead Generation
**Type :** Référence générique  
**Usage :** Consulté par SKILL_media_buyer.md — Étapes 2, 3, 4  
**Plateforme :** Meta Ads (Facebook + Instagram)  
**Objectif campagne :** LEADS

> ⚠️ Ces benchmarks sont calibrés pour de la génération de leads. Ils ne s'appliquent pas directement à l'e-commerce (CVR, CPA et ROAS diffèrent). Voir `references/benchmarks_ecom.md` pour l'e-com.

> Les seuils réels d'un client remplacent ces valeurs génériques — voir `clients/[CLIENT]/benchmarks.md`.

---

## Métriques principales

| Métrique | Faible | Acceptable | Bon | Excellent |
|---|---|---|---|---|
| Hook Rate (vues 3s / impressions) | < 20% | 20–30% | 30–40% | > 40% |
| CTR (clics lien / impressions) | < 1,0% | 1,0–2,0% | 2,0–3,5% | > 3,5% |
| CPC (coût par clic lien) | > 3,00€ | 1,50–3,00€ | 0,70–1,50€ | < 0,70€ |
| CPM (coût pour 1 000 impressions) | > 25€ | 12–25€ | 6–12€ | < 6€ |
| Fréquence (rolling 7 jours) | > 4,0 | 2,5–4,0 | 1,5–2,5 | < 1,5 |
| Complétion vidéo 15s | < 8% | 8–15% | 15–25% | > 25% |
| CVR landing page (visiteurs → leads) | < 2% | 2–5% | 5–10% | > 10% |

---

## Lecture combinée des métriques

Les métriques ne se lisent pas en isolation. Voici les combinaisons les plus significatives :

| Combinaison | Diagnostic | Action |
|---|---|---|
| CTR faible + CPM normal | Mauvaise créa ou mauvais hook | Tester nouveaux hooks |
| CTR bon + CPL élevé | Landing page sous-performante | Optimiser la LP |
| CPM élevé + CTR normal | Audience trop compétitive ou trop étroite | Élargir le ciblage |
| Hook Rate bon + CTR faible | Hook capte l'attention mais le body ne convainc pas | Retravailler le body |
| Tout bon en test + CPL élevé à l'échelle | Fatigue ou audience saturée en scale | Rafraîchir la créa |

---

## Critères de validation d'une annonce gagnante (P1 → P4)

Pour qu'une annonce soit considérée comme prouvée et éligible au scale :

```
[ ] Portée minimale : 6 000 impressions
[ ] Clics sur les liens : 200+
[ ] Conversions (leads) : 10+
[ ] CPA : dans la fourchette cible du client
[ ] CVR landing page : ≥ 2%
[ ] Durée : CPA dans la cible pendant 3 jours consécutifs minimum
```

---

## Benchmarks de démarrage — Nouveau compte

Pour un nouveau compte sans historique, les premiers signaux à surveiller :

| Métrique | Cible de départ | Interprétation |
|---|---|---|
| CTR | ≥ 2% | Signal que la créa capte l'attention |
| CPM | < 20€ | Audience accessible et pas trop compétitive |
| CPC | < 2€ | Coût d'acquisition du clic raisonnable |
| Hook Rate | ≥ 25% | Les 3 premières secondes fonctionnent |

> Si CTR < 1% dès les premières 2 000 impressions : ne pas attendre. La créa ou l'accroche ne fonctionne pas. Couper et tester une nouvelle accroche.

---

## Interprétation par phase

### Phase 1 — Wow Idea
Priorité : Hook Rate + CTR. Si ces deux métriques sont dans la fourchette acceptable, laisser tourner jusqu'au seuil de conversion.

### Phase 2 — Message Testing
Priorité : CTR + CPC. On cherche à identifier les éléments (titre, accroche) qui améliorent le coût du clic sur la base d'une créa déjà prouvée.

### Phase 3 — Audience Testing
Priorité : CPM + CPA. On compare les audiences entre elles sur les mêmes créas prouvées. Un CPM plus bas avec un CPA équivalent = audience plus efficace.

### Phase 4 — Scale
Priorité : CPA à l'échelle + Fréquence. Si le CPA reste stable en augmentant le budget, on continue. Si la fréquence dépasse 2,5 en broad, l'audience commence à saturer.
