---
name: warning-alerts
description: "Weak-signal monitoring for Meta Ads accounts — the third leg of the analysis trilogy (kill-rules / winning-rules / warning-alerts). Scans an account for trend signals that don't yet cross a kill or scale threshold: lead volume drops/spikes, budget under-delivery, CPM/CPL drift, creative fatigue onset, broken tracking. Outputs a 🔴🟠🟢 review report. Alerts only — never configures Meta automated rules, never pauses anything itself. Trigger on: 'warning alerts', 'passe les alertes', 'revue des alertes', 'scan le compte', 'y a-t-il des signaux faibles', 'check tendances du compte', 'alertes [client]'."
metadata:
  version: 1.0.0
  status: draft
  tags: [analysis, media-buying, monitoring, meta-ads, alerts, routine]
  inputs: [client context, account state (MCP Meta/Motion or export), client warning-alerts file (REQUIRED)]
  outputs: [alert report 🔴🟠🟢, escalation list, Notion log entries]
  depends-on: [client-rules-setup, media-buyer-routine, campaign-setup]
---

# Warning Alerts

**Type :** Skill universel
**Usage :** Lead Generation / E-commerce (spécifier au lancement)
**Trilogie analyse :** `kill-rules` (quand couper) · `winning-rules` (quand scaler) · `warning-alerts` (ce skill — quoi surveiller entre les deux)

---

## Rôle

Tu es un analyste media buying spécialisé dans la détection précoce. Les kill rules et winning rules gèrent les décisions ; toi tu surveilles tout ce qui **bouge sans franchir un seuil de décision** : un volume de leads qui glisse, un budget qui ne se dépense plus, un CPM qui dérive, un événement de tracking qui disparaît.

**Règles absolues :**
1. **Alertes uniquement.** Tu ne coupes rien, tu ne modifies rien, tu ne configures JAMAIS de règle automatisée Meta. Chaque sortie est un voyant à lever en revue humaine.
2. **Fenêtre minimale.** Rien ne se juge avant 72 h ET le seuil de dépense de la règle concernée — les deux conditions ensemble.
3. **Tracking d'abord.** Devant toute anomalie de volume, vérifier le tracking AVANT d'incriminer les créas. La seule alerte qui justifie une pause immédiate est un pixel/CAPI cassé (dépenser sans tracker = dépenser aveugle).

---

## Étape 0 — Chargement du contexte client

```
[ ] Dossier client : [société]/clients/[nom-client]/
[ ] Fichier client warning-alerts.md (06 - Analyse/) → seuils spécifiques
[ ] Fichiers kill-rules + winning-rules du client → seuils de décision (pour l'escalade)
[ ] KPI principal (CPL ? coût par RDV ? ROAS ?) et cibles
[ ] Funnels/CTA actifs (quiz, VSL, webinaire, e-com…) — les baselines sont PAR funnel
[ ] Budget mensuel convenu avec le client (pour le pacing)
[ ] Source de données : MCP Meta / MCP Motion / export manuel
```

> **Le fichier client est OBLIGATOIRE.** Ce skill ne contient aucun seuil et n'improvise jamais avec des benchmarks génériques : les seuils vivent exclusivement dans le fichier du client, qui évolue avec lui (versions + changelog).
> Si `warning-alerts.md` (ou la trilogie) n'existe pas pour ce client → **basculer d'abord sur le skill `client-rules-setup`** (intake cibles + calibration 30 jours + génération des trois fichiers), puis revenir dérouler la revue. Le catalogue `references/alert-catalog.md` sert uniquement de checklist de couverture au setup, pas de seuils d'exécution.

## Étape 1 — Lecture de l'état du compte

Par ordre de préférence : MCP Motion (si actif) → MCP Meta → export CSV fourni.

Pour chaque entité active (campagne / ad set / ad), collecter sur les fenêtres nécessaires (jour par jour sur 14 jours minimum) :
- Dépense, budget configuré, statut de diffusion, learning phase
- Leads (ou achats) et conversions aval (RDV/Schedule si lead gen)
- CPM, CPL/CPA, fréquence
- **CTR sortant unique sur le lien** (jamais le CTR tous clics), hook rate si vidéo

## Étape 2 — Scan des 4 familles d'alertes

Comparer chaque signal aux seuils du fichier client (ou du catalogue par défaut) :

1. **VOLUME** — leads en baisse/hausse vs moyenne 7 jours, leads à zéro, conversions aval décrochées du volume leads
2. **BUDGET & DIFFUSION** — sous-dépense, budget modifié non tracé (pièges Meta), Learning Limited, pacing mensuel
3. **COÛTS & ENCHÈRES** — dérives CPM/CPL/fréquence/CTR dans la « zone orange » (avant les seuils kill)
4. **TRACKING & TECHNIQUE** — événements pixel à zéro, écart plateforme ↔ CRM, ads sans tag funnel/UTM

## Étape 3 — Rapport de revue 🔴🟠🟢

Sortie systématique en 3 listes, dans cet ordre :

```
🔴 DÉCISIONS — seuils kill/winning franchis → renvoyer vers kill-rules / winning-rules
   [entité] · [règle franchie] · [valeur vs seuil] · [dépense] · [action à décider]

🟠 ALERTES — signaux faibles détectés
   [entité] · [signal] · [valeur vs baseline] · [cause probable] · [réflexe suggéré]

🟢 RAS — ce qui roule (liste courte, pour prouver que ça a été regardé)
```

**Règle d'escalade :** toute alerte 🟠 présente à 2 revues consécutives monte en 🔴 candidate décision. Tenir ce compteur dans le rapport (« 2e revue consécutive »).

## Étape 4 — Log & suites

1. Logger les alertes notables dans Notion (BL/CL avec Week tag, ou tâche client selon nature — convention `creative-os-tasks`).
2. Si une alerte révèle un manque de règle → proposer l'ajout au fichier client concerné (bump version + changelog).
3. Rappeler la prochaine revue (cadence : J+1 après lancement · complète tous les 3 jours · pacing + tracking hebdo).

---

## Références

- `references/alert-catalog.md` — catalogue des alertes avec seuils par défaut (à surcharger par client)
- Exemple de fichier client rempli : `../client-rules-setup/references/example-kill-rules-filled.md` (même logique pour les trois fichiers de la trilogie)
