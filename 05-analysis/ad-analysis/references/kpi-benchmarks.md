# KPI Benchmarks — Meta Ads FR

## Avertissement

Ces benchmarks sont des références de marché — pas des vérités absolues.
Toujours comparer d'abord contre ton propre historique de compte.
Un CTR de 1.5% peut être excellent dans une niche B2B et faible en e-commerce impulse.

---

## Métriques Primaires

### Hook Rate (Taux d'accroche vidéo)
**Définition :** % de personnes qui regardent les 3 premières secondes de la vidéo.
**Calcul :** ThruPlay 3s / Impressions × 100

| Performance | Taux |
|---|---|
| Faible | < 15% |
| Moyen | 15–25% |
| Fort | 25–40% |
| Exceptionnel | > 40% |

**Signal :** Un Hook Rate faible = le premier frame ou la première seconde ne retient pas. Problème de hook visuel/audio, pas forcément de message.

---

### Hold Rate (Taux de rétention)
**Définition :** % de personnes qui regardent jusqu'au 50% ou 75% de la vidéo.
**Calcul :** Video views at 50% / Video views at 3s

| Performance | Taux (50%) |
|---|---|
| Faible | < 20% |
| Moyen | 20–35% |
| Fort | > 35% |

**Signal :** Hook Rate fort + Hold Rate faible = le début accroche, mais le contenu ne tient pas la promesse. Problème de corps de message.

---

### CTR (Click-Through Rate)
**Définition :** % de personnes qui cliquent sur le lien après avoir vu l'ad.
**Calcul :** Link Clicks / Impressions × 100

| Type | Faible | Moyen | Fort |
|---|---|---|---|
| Feed vidéo | < 0.8% | 1–2% | > 2.5% |
| Feed statique | < 0.5% | 0.8–1.5% | > 1.8% |
| Stories | < 0.4% | 0.6–1.2% | > 1.5% |
| Reels | < 0.6% | 0.8–1.5% | > 2% |

**Signal :** CTR fort = l'ad crée le désir de savoir plus. CTR faible après bon Hook Rate = le corps du message ne convertit pas l'attention en intention.

---

### CPM (Coût pour 1000 impressions)
**Définition :** Coût de l'enchère — dépend de l'audience, la période, la concurrence.

| Contexte FR | Fourchette typique |
|---|---|
| Audience large (TOF) | 5–12€ |
| Audience intermédiaire | 8–18€ |
| Retargeting (BOF) | 12–30€ |
| B2B / niche premium | 20–50€+ |

**Signal :** CPM élevé ≠ mauvaise créa. CPM élevé = audience compétitive ou période de forte enchère (Q4, rentrée).

---

### CPA / CPL (Coût par acquisition ou lead)
**Pas de benchmark universel** — dépend entièrement du secteur, de la marge et du LTV.

**Méthode :** Établir le CPA cible à partir du LTV ou de la marge brute.
- E-commerce : CPA cible ≤ marge brute × (1 / nombre d'achats pour rentabiliser)
- Formation / SaaS : CPA cible ≤ LTV × 30–40%
- Lead gen : CPL cible = CA par lead fermé × taux de closing × (1 - marge souhaitée)

---

### ROAS (Return On Ad Spend)
**Définition :** CA généré / Budget publicitaire dépensé

| Stage | ROAS de référence |
|---|---|
| Test (cold traffic) | 1.5–2.5× |
| Scaling (warm) | 2.5–4× |
| Retargeting (hot) | 4–8×+ |

**Note :** Le ROAS seul est insuffisant. Une campagne à ROAS 5× avec 50€/jour ne scale pas. Regarder le volume + le ROAS ensemble.

---

## Métriques de Diagnostic Créatif

### Fréquence
**Seuil d'alerte :** > 3 en 7 jours pour une même audience
**Signal :** Au-delà de 3, les performances commencent à se dégrader. Rafraîchir la créa ou élargir l'audience.

### Relevance Score (Quality Ranking)
- Above Average = créa bien reçue par l'audience
- Average = normal
- Below Average = mauvaise expérience utilisateur, CPM pénalisé

### Scroll Stop Rate (si disponible)
Certains outils tiers (TripleWhale, Northbeam) mesurent le taux d'arrêt sur le premier frame.
Référence : > 5% = bon premier frame visuel.

---

## Tableau de Lecture Rapide

| Symptôme | KPI en cause | Hypothèse créative |
|---|---|---|
| Peu d'impressions malgré budget | CPM trop élevé | Audience trop restreinte ou période compétitive |
| Impressions OK, peu de clics | CTR faible | Body copy ou CTA insuffisant |
| Beaucoup de clics, peu de conversions | CPA élevé | Problème landing page ou promesse vs réalité |
| Bonne vidéo vue, peu de clics | Hook Rate OK / CTR faible | La vidéo engage mais ne donne pas envie d'agir |
| Performances dégradées semaine 3+ | Fréquence > 3 | Fatigue créative — rafraîchir |

---

## Cadre d'Analyse en 3 Étapes

1. **Trier par dépense** — les créas qui ont le plus dépensé ont les données les plus fiables.
2. **Segmenter par KPI primaire** — selon l'objectif de la campagne (CPL, CPA, ROAS).
3. **Identifier les patterns** — qu'ont en commun les 3 meilleures créas ? Les 3 pires ?
