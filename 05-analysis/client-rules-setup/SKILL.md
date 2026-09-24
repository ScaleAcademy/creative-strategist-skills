---
name: client-rules-setup
description: "Generates and maintains the per-client analysis rules trilogy for Meta Ads: kill-rules.md (when to cut), winning-rules.md (when to scale), warning-alerts.md (weak signals). The runtime skills (media-buyer-routine, warning-alerts) contain NO thresholds — they only read these client files. This skill runs the intake (main KPI, targets, funnels, budget), pulls 30 days of account data to calibrate baselines PER FUNNEL, and writes the three dedicated files into the client folder. Re-run it to recalibrate (bump version, never overwrite). Trigger on: 'génère les règles pour [client]', 'setup les kill rules de [client]', 'calibre les règles', 'crée la trilogie analyse', 'recalibre les seuils de [client]', 'nouveau client à équiper en règles'."
metadata:
  version: 1.0.0
  status: draft
  tags: [analysis, media-buying, setup, meta-ads, calibration, rules]
  inputs: [client context, targets (CPA/CPL/KPI), 30-day account data per funnel]
  outputs: [clients/[client]/0X - Analyse/kill-rules.md + winning-rules.md + warning-alerts.md]
  depends-on: [media-buyer-routine, warning-alerts]
---

# Client Rules Setup

**Type :** Skill de génération (setup + recalibration)
**Principe :** les skills d'exécution ne contiennent AUCUN seuil. Toute la connaissance client vit dans trois fichiers dédiés, dans le dossier du client. Ce skill les crée et les maintient.

---

## Rôle

Tu génères la trilogie de règles d'analyse d'un client Meta Ads, calibrée sur SES données et SES cibles — jamais sur des benchmarks génériques. Un seuil générique est presque toujours faux : le CTR sortant unique « normal » varie de 0,8 % à 6 % selon la niche et le funnel.

**Règles absolues :**
1. **Un client = ses trois fichiers**, dans `[société]/clients/[nom-client]/0X - Analyse/` : `kill-rules.md` · `winning-rules.md` · `warning-alerts.md`. (Le chemin racine dépend de la structure de l'agence/société — ne jamais le coder en dur.)
2. **Tout est alertes** : aucune règle automatisée Meta, jamais. La décision reste humaine.
3. **Versioning** : recalibration = bump de version + ligne de changelog. Refonte majeure = nouveau fichier `-v2`, l'ancien reste en archive. Jamais d'écrasement silencieux.
4. **Par funnel/CTA** : CPL, CTR et CPM n'ont aucun sens sans le call-to-action (quiz ≠ VSL ≠ webinaire ≠ e-com). Chaque seuil est défini par funnel.

---

## Étape 1 — Intake en DEUX phases : récupérer d'abord, demander ensuite

### Phase 1A — Récupération (aucune question à ce stade)

Analyser tout ce qui existe déjà et en extraire les réponses :

```
[ ] Dossier client `[société]/clients/[nom-client]/` : contexte.md, docs stratégie,
    audits, briefs, reporting existant, _meta-ads-defaults.md
[ ] Anciens fichiers de règles (kill/winning/warning, même partiels ou informels)
    → à retravailler dans la nouvelle structure, pas à écraser
[ ] Notion : DBs client (Concepts, Briefs, Learnings BL/CL, Roadmap, KB)
[ ] Le compte publicitaire lui-même : funnels visibles (landing pages, nomenclature),
    protocole implicite de coupe (à quelle dépense les entités sont coupées),
    événements de conversion configurés
[ ] Historique de reporting du client (dashboards, exports, ancien prestataire)
```

→ Produire un pré-rempli : ce qu'on SAIT (avec la source) vs ce qui MANQUE.

### Phase 1B — Conversation (uniquement les trous)

Poser uniquement ce que la Phase 1A n'a pas permis de déduire :

```
[ ] KPI principal : CPL ? coût par RDV ? coût par RDV honoré ? ROAS ?
[ ] Où est tracké chaque niveau ? (pixel/CAPI visible Meta · CRM seulement · pas encore)
    → un KPI non trackable = règle marquée « dormante », avec règle intérimaire
[ ] Cible et maximum acceptable pour le KPI principal
    (sinon : taux de conversion étape par étape + valeur client → calcul à rebours)
[ ] Funnels/CTA actifs et leur CPL cible respectif
[ ] Protocole budget de test : fenêtre de dépense avant jugement (ex. cycles de X €),
    nombre de cycles max — proposer X ≈ 1,5-2x le CPA cible si le client n'en a pas
[ ] Budget mensuel convenu (pour le pacing des warning alerts)
[ ] Structure : campagnes de test (ABO) et de scale (CBO) séparées ?
[ ] Contraintes persona/ciblage non négociables (ex. CSP+ uniquement)
```

## Étape 1bis — Choisir et DÉCLARER la base de calibration

Chaque fichier généré indique en en-tête sur quoi reposent ses seuils. Trois bases possibles :

| Base | Quand | Conséquence |
|---|---|---|
| **A. Données réelles** | ≥ 30 jours de données exploitables sur le compte | Calibration complète (Étape 2). La référence. |
| **B. Reporting existant** | Le client a déjà un reporting/historique (dashboard, exports, ancien prestataire) mais le compte est récent ou restructuré | Importer les chiffres du reporting comme baseline provisoire, marquer chaque seuil hérité `(reporting client)` |
| **C. Hypothèses** | Compte neuf, aucune donnée | Seuils posés à rebours depuis l'économie de l'offre (valeur client × taux de conversion estimés) + benchmarks du secteur, TOUS marqués `(hypothèse)` |

**Règles de bascule (à écrire dans le fichier généré) :**
- Base C → recalibration OBLIGATOIRE dès 2 semaines de données OU {{3-4x CPA cible}} € dépensés — au premier atteint.
- Base B → recalibration dès 30 jours de données propres sur le compte.
- Base A → revue **mensuelle** par défaut, ou immédiate si une baseline bouge de > 30 %.
- Chaque recalibration = bump de version + ligne de changelog indiquant la nouvelle base.

## Étape 2 — Nomenclature (GATE bloquant), puis calibration

**D'abord la nomenclature.** Les seuils sont PAR FUNNEL : si le funnel/CTA n'est pas identifiable sur chaque entité, l'analyse est structurellement fausse. Avant toute calibration :

```
[ ] Chaque ad set porte un tag funnel dans son nom (ex. QUIZ / VSL / WEBI) ?
[ ] Chaque ad porte les UTM (dont utm_content identifiant funnel/créa) ?
[ ] Pas de doublons de noms entre entités (deux « Adset Principal 3 » = illisible) ?
```
→ Si NON : produire la **liste de renommage** (nom actuel → nom conforme, le renommage ne reset pas l'apprentissage) et le mapping funnel entité par entité (déduit des landing pages/créas), le faire valider, PUIS calibrer sur ce mapping. Le chantier reste tracé dans le fichier généré tant qu'il n'est pas terminé.

**Ensuite la calibration** (base A ou B). Tirer 30 jours (MCP Motion si actif, sinon MCP Meta, sinon export) au niveau ad set, PAR FUNNEL :

```
[ ] CPL réel : fourchette des entités saines
[ ] CTR sortant unique sur le lien (JAMAIS le CTR tous clics — il gonfle de 1-2+ points)
[ ] CPM par funnel · fréquence · hook rate (3s/impressions) si vidéo
[ ] Les entités récemment coupées par le client → leurs valeurs = validation des planchers
[ ] Dépense typique avant coupe (protocole implicite du client)
[ ] Vérifier la nomenclature : le funnel est-il identifiable dans le nom/UTM de chaque ad set ?
    → sinon, lister les entités à taguer (chantier prérequis dans le fichier généré)
```

**Méthode de seuil :** baseline = fourchette saine observée · alerte ≈ sortie de fourchette (-20/-30 %) · kill ≈ le niveau des entités effectivement coupées, validé avec le client.

## Étape 3 — Génération des trois fichiers

Remplir les templates (références ci-dessous) avec les valeurs calibrées :

1. `kill-rules.md` — hiérarchie KPI, seuils par funnel, protocole cycles de test (ABO), garde-fous de dégradation (CBO), escalade, template de log
2. `winning-rules.md` — étapes Candidate → Confirmée → Winner, checks qualité aval, protocole de promotion et d'itération
3. `warning-alerts.md` — 4 familles (volume, budget, coûts, tracking), cadences, revue 🔴🟠🟢

Chaque fichier porte : client, date, version, référence à la trilogie, **base de calibration (A/B/C) + règle de bascule + cadence de révision**, changelog.

## Étape 4 — Boucle de vie

- **Recalibration** (déclenchement explicite ou proposée quand les baselines ont bougé de > 30 %) : re-dérouler l'Étape 2, mettre à jour les seuils, bump + changelog.
- **Nouveau funnel lancé** : ajouter sa colonne « à calibrer au 1er lancement », calibrer après ~2 semaines de données.
- **KPI dormant activé** (ex. show-up enfin tracké) : basculer les règles dormantes en actives.
- Logger la création/mise à jour en tâche Notion client (convention `creative-os-tasks`).

---

## Références

- `references/template-kill-rules.md`
- `references/template-winning-rules.md`
- `references/template-warning-alerts.md`
- `references/example-kill-rules-filled.md` — exemple rempli et anonymisé (lead gen coaching, 2 funnels)
