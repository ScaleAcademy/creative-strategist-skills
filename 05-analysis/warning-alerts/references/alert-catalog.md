# RÉFÉRENCE — Catalogue des Warning Alerts
**Type :** Référence générique
**Usage :** Consulté par SKILL warning-alerts — Étape 2
**Règle :** Les seuils client (fichier `clients/[CLIENT]/warning-alerts.md`) remplacent ceux-ci. Ce catalogue sert de défaut ET de checklist de couverture à la création d'un fichier client.

---

## Principe de calibration

Un seuil d'alerte générique est presque toujours faux : chaque compte a ses baselines (le CTR sortant unique « normal » varie de 0,8 % à 6 % selon la niche et le funnel). À la création du fichier client :
1. Tirer 30 jours de données par funnel/CTA.
2. Baseline = fourchette observée sur les entités saines.
3. Alerte = sortie de fourchette (~±20-30 %) · Décision (kill/win) = les seuils des autres fichiers.

---

## Famille 1 — VOLUME

| Signal | Défaut | Fenêtre | Cause probable → réflexe |
|---|---|---|---|
| Leads/achats en baisse | < -30 % vs moyenne 7j | 2 jours consécutifs | Fatigue créa, CPM, ou tracking → vérifier pixel AVANT les ads |
| Leads à zéro | 0 sur 1 jour si moyenne 7j ≥ 5/j | 1 jour | Quasi toujours technique → landing + Events Manager immédiat |
| Hausse anormale | > +50 % vs moyenne 7j sans hausse budget | 2 jours | Vérifier la qualité aval avant de se réjouir |
| Conversion aval décrochée | étape suivante (RDV, achat…) -50 % avec leads stables | 7 jours | Problème funnel post-lead, PAS ads → ne rien couper côté Meta |

## Famille 2 — BUDGET & DIFFUSION

| Signal | Défaut | Fenêtre | Réflexe |
|---|---|---|---|
| Sous-dépense | < 80 % du budget quotidien | 2 jours consécutifs | Check diffusion par ad (review, audience, enchère) |
| Sous-dépense sévère | < 50 % | 3 jours consécutifs | = seuil kill rules campagne → préparer la décision |
| Budget modifié non tracé | budget actuel ≠ budget loggé au lancement | — | Pièges Meta (ajustement auto, doublons) → historique de modifs |
| Learning Limited | bloqué 7+ jours après lancement | — | Consolider / élargir / augmenter budget par ad set |
| Pacing mensuel | projection > ±15 % du budget convenu | hebdo | Ajuster maintenant, pas en fin de mois |

## Famille 3 — COÛTS & ENCHÈRES (zone orange, avant les seuils kill)

| Signal | Défaut | Fenêtre | Réflexe |
|---|---|---|---|
| CPM en dérive | > +30 % vs baseline funnel | 3 jours glissants | Surveiller ; > 2x = kill rules |
| CPL/CPA en glissement | entre 1,2x cible et le seuil kill | 3 jours glissants | Préparer les itérations avant le franchissement |
| Fréquence en montée | entre 2,5 et 3,0 (kill à > 3,0) | 7 jours glissants | Lancer la prod de la variante MAINTENANT (délai de prod) |
| CTR sortant unique en glissement | -20 % vs moyenne 7 premiers jours (kill fatigue à -30 %) | 3 jours glissants | Début de fatigue créative |

> ⚠️ CTR = **clics sortants uniques sur le lien**, jamais le CTR tous clics (qui gonfle les valeurs de 1 à 2+ points et fausse tous les seuils).

## Famille 4 — TRACKING & TECHNIQUE

| Signal | Défaut | Réflexe |
|---|---|---|
| Événement principal à zéro dans Events Manager, ads actives | 12 h | **Seule alerte à pause immédiate** : dépenser sans tracker = aveugle |
| Événement aval à zéro (Schedule, Purchase…) avec du volume amont | 7 jours | Page/étape cassée ou event désinstallé |
| Ad sans tag funnel ou sans UTM | à chaque revue | Corriger immédiatement — les règles par funnel deviennent illisibles |
| Écart plateforme ↔ CRM | > 20 % sur 7 jours | Déduplication, spam, CAPI en double → audit tracking |

---

## Format de sortie (rappel)

```
🔴 DÉCISIONS (→ kill-rules / winning-rules)
🟠 ALERTES (préventif — avec compteur de revues consécutives)
🟢 RAS
```

Escalade : 🟠 × 2 revues consécutives → 🔴 candidate décision.
