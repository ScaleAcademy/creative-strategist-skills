# TEMPLATE — warning-alerts.md client
> Généré par le skill `client-rules-setup`. Remplacer chaque `{{placeholder}}` par la valeur calibrée.
> Base : catalogue générique `05-analysis/warning-alerts/references/alert-catalog.md` — n'inclure que les alertes pertinentes pour le client, avec SES seuils.

---

# Warning Alerts — {{Client}} (Meta Ads)
**Type :** Règles client — signaux faibles. 3e volet de la trilogie analyse.
**Trilogie :** `kill-rules.md` · `winning-rules.md` · `warning-alerts.md` (ce fichier)
**Client :** {{Client}} · **Créé le :** {{date}} · **Version :** v1
**Base de calibration :** {{A. Données réelles | B. Reporting client | C. Hypothèses}} · **Révision :** {{cadence + règle de bascule}}

## Principe
Tout ce qui bouge **sans franchir un seuil de décision**. Aucune action automatique — des voyants oranges levés en revue, qui préparent une décision kill/win ou révèlent un problème technique. Chaque alerte a : un signal, une fenêtre, une cause probable, un réflexe.

## Cadences
| Moment | Ce qu'on vérifie |
|---|---|
| **J+1 après lancement** | Livraison démarrée, pas d'erreur, CPM pas aberrant (> 3x baseline), UTM/tag funnel présents |
| **Tous les 3 jours** | Toutes les alertes tendance, sur tout ce qui est actif |
| **Hebdo** | Pacing budget mensuel ({{budget convenu}} €/mois), santé tracking, fréquences, synthèse → Notion |

## Alertes VOLUME
| Signal | Seuil | Fenêtre | Cause probable → réflexe |
|---|---|---|---|
| 📉 {{Résultats}} en baisse | < -30 % vs moyenne 7 j | 2 jours consécutifs | Fatigue, CPM, ou tracking → vérifier le pixel AVANT les ads |
| 📉 {{Résultats}} à zéro | 0 sur 1 jour si moyenne 7 j ≥ {{n}}/j | 1 jour | Quasi toujours technique → landing + Events Manager immédiat |
| 📈 Hausse anormale | > +50 % vs moyenne 7 j sans hausse budget | 2 jours | Vérifier la qualité aval ({{CRM}}) avant de se réjouir |
| 🗓️ {{Résultat aval}} décroché | {{résultats}} stables mais {{aval}} -50 % vs semaine préc. | 7 j glissants | Problème funnel post-lead, PAS ads → ne rien couper côté Meta |

## Alertes BUDGET & DIFFUSION
| Signal | Seuil | Fenêtre | Réflexe |
|---|---|---|---|
| 💸 Sous-dépense | < 80 % du budget quotidien | 2 jours consécutifs | Check diffusion par ad |
| 💸 Sous-dépense sévère | < 50 % | 3 jours consécutifs | = seuil kill rules campagne → préparer la décision |
| 💸 Budget modifié non tracé | budget actuel ≠ budget loggé | — | Pièges Meta → historique de modifs du compte |
| ⏱️ Learning Limited | bloqué 7+ jours | — | Consolider / élargir / augmenter budget par ad set |
| 📅 Pacing mensuel | projection > ±15 % du budget convenu | hebdo | Ajuster maintenant, pas en fin de mois |

## Alertes COÛTS & ENCHÈRES (zone orange, avant les seuils kill)
| Signal | Seuil | Fenêtre | Réflexe |
|---|---|---|---|
| CPM en dérive | > +30 % vs baseline funnel ({{rappel baselines}}) | 3 j glissants | Surveiller ; > 2x = kill rules |
| CPL en glissement | entre 1,2x cible et la limite kill du funnel | 3 j glissants | Préparer les itérations avant le franchissement |
| Fréquence en montée | 2,5 – 3,0 (kill à > 3,0) | 7 j glissants | Lancer la prod de la variante MAINTENANT |
| CTR sortant unique en glissement | -20 % vs moyenne 7 premiers jours (kill fatigue à -30 %) | 3 j glissants | Début de fatigue créative |

## Alertes TRACKING & TECHNIQUE
| Signal | Seuil | Réflexe |
|---|---|---|
| 🔌 Événement principal ({{event}}) à zéro, ads actives | 12 h | **Seule alerte à pause immédiate** : dépenser sans tracker = aveugle |
| 🔌 Événement aval ({{event aval}}) à zéro avec du volume amont | 7 jours | Étape cassée ou event désinstallé |
| 🏷️ Ad sans tag funnel ({{tags client}}) ou sans UTM | à chaque revue | Corriger immédiatement |
| 🧾 Écart Meta ↔ {{CRM}} | > 20 % sur 7 jours | Déduplication, spam, CAPI double → audit tracking |

## Format de la revue (tous les 3 jours)
```
🔴 DÉCISIONS (seuils kill/winning franchis → kill-rules / winning-rules)
🟠 ALERTES (préventif — avec compteur de revues consécutives)
🟢 RAS (liste courte, pour prouver que ça a été regardé)
```
Escalade : 🟠 × 2 revues consécutives → 🔴 candidate décision. Alertes notables → Notion (BL/CL ou tâche client).

## Changelog
- **{{date}}** — v1 · Création ({{auteur}}). Baselines issues du compte au {{date}}.
