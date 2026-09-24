# TEMPLATE — kill-rules.md client
> Généré par le skill `client-rules-setup`. Remplacer chaque `{{placeholder}}` par la valeur calibrée.
> Les blocs `[SI …]` ne sont inclus que si la condition s'applique au client.

---

# Alert Rules (Kill) — {{Client}} (Meta Ads)
**Type :** Règles client — remplace les seuils génériques des skills
**Client :** {{Client}} ({{niche}} — {{contraintes ciblage non négociables}})
**Créé le :** {{date}} · **Version :** v1
**Trilogie analyse :** `kill-rules.md` · `winning-rules.md` · `warning-alerts.md`
**Base de calibration :** {{A. Données réelles 30 j | B. Reporting client | C. Hypothèses}} — compte {{ad_account_id}}, {{période}} (~{{dépense}} €)
**Révision :** {{mensuelle par défaut}} · immédiate si une baseline bouge de > 30 % · {{[SI base B/C :] recalibration obligatoire dès {{condition de bascule}}}}
[SI base C :] > ⚠️ Tous les seuils marqués `(hypothèse)` — aucune décision agressive avant la première recalibration sur données réelles.

## Principe — des ALERTES, jamais des coupes automatiques
Aucune règle automatisée Meta, jamais. Chaque seuil franchi = une alerte ; la décision reste humaine, en revue.
**Cadence :** J+1 (check technique) · tous les 3 jours (revue complète) · hebdo ({{KPI aval}} + logs Notion).
**Fenêtre minimale — les DEUX ensemble :** rien ne se juge avant **72 h** ET le seuil de dépense de la règle.

## Hiérarchie des KPI
1. **{{KPI principal}}** — le juge de paix ({{où il est tracké}})
2. **CPL** — alerte précoce uniquement (le CPL seul peut mentir d'un facteur énorme vs le KPI aval)
3. **CTR sortant unique sur le lien + hook rate** — diagnostic créa, jamais un motif de coupe isolé
[SI KPI aval non trackable :] 4. **{{KPI dormant}}** — ⏳ tracking pas en place, règles dormantes + règle intérimaire : {{règle intérimaire}}

## Cibles & seuils PAR FUNNEL

| Métrique | {{Funnel A}} | {{Funnel B}} | {{Funnel C}} |
|---|---|---|---|
| CPL cible | {{x}} € | {{x}} € | à calibrer au 1er lancement |
| CPL max (alerte) | **{{x}} €** | **{{x}} €** | — |
| CTR sortant unique — baseline | {{x–y}} % | {{x–y}} % | — |
| CTR sortant unique — alerte | **< {{x}} %** | **< {{x}} %** | — |
| CTR sortant unique — critique | < {{x}} % | < {{x}} % | — |
| CPM attendu | {{x–y}} € | {{x–y}} € | — |
| Hook rate baseline (3s/imp.) | {{x–y}} % | {{x–y}} % | — |

**Seuils absolus tous funnels** (créa morte, alerte STOP dès la fenêtre atteinte) :
- CTR sortant unique < {{x}} % après 1 000 impressions · Hook rate < {{x}} % après 1 000 impressions

> ⚠️ CTR = **clics sortants uniques sur le lien** (colonne Ads Manager « CTR sortant unique »), JAMAIS le CTR tous clics. Recalibrer à la première revue depuis la colonne exacte.

**{{KPI principal}} :** cible **{{x}} €** · alerte à 1,5x ({{x}} €) · critique à 2x ({{x}} €).

## Protocole TEST ({{ABO/structure test client}}) — cycles de {{X}} €
{{X}} € ≈ {{ratio}}x le {{KPI principal}} cible. Jamais plus de {{n}} cycles.

```
Cycle 1 — 0 à {{X}} € (et ≥ 72 h)
├── Avant {{X}} € ou 72 h : APPRENTISSAGE — aucune alerte CPA.
│   Alertes précoces (dès 72 h ET seuil indiqué) :
│   · CTR sortant unique < critique funnel après 1 000 imp. → ALERTE STOP
│   · Hook rate < {{x}} % après 1 000 imp. → ALERTE STOP
│   · Dépense ≥ 2x CPL cible funnel et 0 lead → ALERTE KILL
│   · Dépense ≥ 3x CPL cible funnel et CPL > 1,5x cible → ALERTE STOP
├── À {{X}} € : 0 {{résultat principal}} → ALERTE KILL (même si le CPL est bon —
│   attrape les créas à leads de mauvaise qualité)
└── À {{X}} € : ≥ 1 {{résultat principal}} → Cycle 2
Cycle 2 — {{X}} à {{2X}} €
├── À {{2X}} € : {{KPI principal}} cumulé > cible OU 0 sur le cycle → ALERTE KILL
└── À {{2X}} € : ≤ cible → candidate gagnante → winning-rules.md
```

**Niveaux :** Ad = CTR/hook/CPL (diagnostic, une ad peut être stoppée dans un ad set qui continue) · Ad set = cycles + {{KPI principal}} (la décision) · Fréquence > 3,0 sur 7 j = alerte fatigue aux deux niveaux.

## Protocole SCALE ({{CBO/structure scale client}}) — garde-fous dégradation
Une gagnante ne se juge pas avec les seuils de test. On surveille la dégradation :

| Signal | Alerte | Fenêtre | Action suggérée |
|---|---|---|---|
| CPL | > 1,3x cible funnel | 3 j glissants | Vérifier {{KPI principal}} avant toute action |
| {{KPI principal}} | > 1,5x cible | 7 j glissants | Préparer les itérations hooks |
| Fréquence | > 3,0 | 7 j glissants | Nouvelle variante avant de couper |
| CTR sortant unique | -30 % vs moyenne 7 premiers jours de scale | 3 j glissants | Fatigue créative |
| CPM | > 2x baseline funnel | 3 j consécutifs | Problème enchère/audience, pas créa |

**Règle d'or :** jamais de coupe brutale d'une gagnante — budget -20 %/jour, itérations, remplacement progressif. Couper = dernier recours après 2 revues consécutives en alerte.

[SI KPI aval dans CRM :]
## {{KPI aval}} (hors Meta — export {{CRM}} hebdo)
{{règles aval + statut dormant/actif + seuils}}

## Chantier nomenclature — identifier le funnel (prérequis)
Tag funnel obligatoire dans le nom d'ad set ET en UTM : {{liste tags}}. État des lieux {{date}} : {{entités sans tag à renommer}}.

## Escalade quand une alerte est confirmée
```
1. PAUSE manuelle (jamais supprimer) → 2. DOCUMENTER (template ci-dessous)
3. DIAGNOSTIQUER : hook raté → nouveaux hooks · body raté → réécrire, garder le hook ·
   audience ratée → même créa autre ciblage · leads sans {{résultat aval}} → promesse/qualification funnel
4. CORRIGER, relancer, mêmes règles → 5. Logger le learning Notion (BL/CL + Week tag)
```

## Template de log
```
Date · Ad set/Ad · Funnel · Phase (TEST c1/c2 | SCALE) · Alerte : [métrique]=[valeur] vs [seuil]
Dépense au kill · Leads / {{résultats}} · Hypothèse cause racine · Prochaine action
```

## Changelog
- **{{date}}** — v1 · Création ({{auteur}}), calibrée sur {{période}} du compte.
