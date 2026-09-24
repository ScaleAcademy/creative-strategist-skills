# EXEMPLE — kill-rules.md rempli (anonymisé)
> À quoi ressemble le fichier généré par `client-rules-setup` pour un client réel.
> Cas : lead generation coaching B2C, 2 funnels actifs, RDV trackés dans Meta, show-up pas encore tracké.
> Données fictives mais réalistes. Même logique pour `winning-rules.md` et `warning-alerts.md`.

---

# Alert Rules (Kill) — CoachPro (Meta Ads)
**Type :** Règles client — remplace les seuils génériques des skills
**Client :** CoachPro (coaching bien-être B2C — ciblage CSP+ uniquement, jamais les < 30 ans non solvables)
**Créé le :** 2026-09-01 · **Version :** v1
**Trilogie analyse :** `kill-rules.md` · `winning-rules.md` · `warning-alerts.md`
**Base de calibration :** A. Données réelles — compte Meta act_XXXX, 30 jours au 2026-09-01 (~6 000 €)
**Révision :** mensuelle par défaut · immédiate si une baseline bouge de > 30 %

## Principe — des ALERTES, jamais des coupes automatiques
Aucune règle automatisée Meta, jamais. Chaque seuil franchi = une alerte ; la décision reste humaine, en revue.
**Cadence :** J+1 (check technique) · tous les 3 jours (revue complète) · hebdo (show-up + logs Notion).
**Fenêtre minimale — les DEUX ensemble :** rien ne se juge avant **72 h** ET le seuil de dépense de la règle.

## Hiérarchie des KPI
1. **Coût par RDV planifié** — le juge de paix (pixel `Schedule`, visible dans Ads Manager)
2. **CPL** — alerte précoce uniquement (écart observé jusqu'à 1/30 entre CPL et coût/RDV : le CPL seul ment)
3. **CTR sortant unique sur le lien + hook rate** — diagnostic créa, jamais un motif de coupe isolé
4. **Show-up** — ⏳ tracking pas en place (CRM seulement, export à venir) : règles dormantes.
   Règle intérimaire : décision sur coût/RDV planifié + scaling prudent (un seul palier +20 %).

## Cibles & seuils PAR FUNNEL

| Métrique | 🧩 QUIZ | 🎬 VSL | 📺 WEBI |
|---|---|---|---|
| CPL cible | 1,50 € | 5,50 € | à calibrer au 1er lancement |
| CPL max (alerte) | **3 €** | **7 €** | — |
| CTR sortant unique — baseline | 3,5 – 6 % | 2,5 – 4 % | — |
| CTR sortant unique — alerte | **< 3,5 %** | **< 2,5 %** | — |
| CTR sortant unique — critique | < 2,5 % | < 1,5 % | — |
| CPM attendu | 4 – 8 € | 13 – 15 € | — |
| Hook rate baseline (3s/imp.) | 40 – 55 % | 33 – 39 % | — |

**Seuils absolus tous funnels** : CTR sortant unique < 0,8 % après 1 000 imp. · Hook rate < 20 % après 1 000 imp. → créa morte, alerte STOP.

> ⚠️ CTR = **clics sortants uniques sur le lien**, JAMAIS le CTR tous clics (qui gonfle de 1-2+ points et avait faussé la première calibration de ce client).

**Coût par RDV :** cible **75 €** · alerte 1,5x (112 €) · critique 2x (150 €).

## Protocole TEST (ABO) — cycles de 120 €
120 € ≈ 1,6x le CPA RDV cible. Jamais plus de 2 cycles.

```
Cycle 1 — 0 à 120 € (et ≥ 72 h)
├── Avant : APPRENTISSAGE. Alertes précoces seulement :
│   · CTR critique funnel après 1 000 imp. → STOP · Hook < 20 % → STOP
│   · ≥ 2x CPL cible dépensé et 0 lead → KILL · ≥ 3x et CPL > 1,5x → STOP
├── À 120 € : 0 RDV → ALERTE KILL (même si le CPL est bon — attrape les leads de mauvaise qualité)
└── À 120 € : ≥ 1 RDV → Cycle 2
Cycle 2 — À 240 € : coût/RDV > 75 € OU 0 RDV sur le cycle → KILL · sinon → winning-rules.md
```

## Protocole SCALE (CBO) — garde-fous dégradation
CPL > 1,3x cible (3 j glissants) · coût/RDV > 1,5x (7 j) · fréquence > 3,0 · CTR -30 % vs 7 premiers jours · CPM > 2x baseline (3 j).
**Règle d'or :** jamais de coupe brutale d'une gagnante — budget -20 %/jour, itérations, remplacement. Couper = après 2 revues consécutives en alerte.

## Chantier nomenclature (prérequis)
Tag funnel obligatoire (QUIZ/VSL/WEBI) dans noms d'ad sets + UTM. État des lieux 2026-09-01 : 4 ad sets sans tag (dont 2 homonymes « Adset Principal 3ce ») → liste de renommage validée, en cours.

## Escalade + log
Pause manuelle → documenter → diagnostiquer (hook/body/audience/funnel) → corriger → relancer → learning Notion BL/CL.
```
Date · Ad set/Ad · Funnel · Phase (TEST c1/c2 | SCALE) · Alerte : [métrique]=[valeur] vs [seuil]
Dépense au kill · Leads / RDV · Hypothèse cause racine · Prochaine action
```

## Changelog
- **2026-09-01** — v1 · Création, calibrée sur 30 j de compte (base A).
