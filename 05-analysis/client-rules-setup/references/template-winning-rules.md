# TEMPLATE — winning-rules.md client
> Généré par le skill `client-rules-setup`. Remplacer chaque `{{placeholder}}` par la valeur calibrée.

---

# Winning Rules — {{Client}} (Meta Ads)
**Type :** Règles client — détection et promotion des créas gagnantes. Miroir de `kill-rules.md`.
**Client :** {{Client}} · **Créé le :** {{date}} · **Version :** v1
**Base de calibration :** {{A. Données réelles | B. Reporting client | C. Hypothèses}} · **Révision :** {{cadence + règle de bascule}}

## Principe
Alertes positives, mêmes cadences de revue que les kill rules, même fenêtre minimale (72 h ET dépense), même hiérarchie KPI. Le danger symétrique du kill trop tôt = le **scale trop tôt** : une créa brillante sur le KPI amont peut être une fausse gagnante sur le KPI aval ({{exemple client chiffré si dispo}}).

## Étape 1 — CANDIDATE (sortie de test, ~{{2X}} €)
TOUTES les conditions réunies :

| # | Critère | Seuil |
|---|---|---|
| 1 | Cycles de test complétés | {{n}} cycles de {{X}} € (≥ {{2X}} € dépensés, ≥ 72 h) |
| 2 | {{KPI principal}} cumulé | ≤ {{cible}} € |
| 3 | Volume minimal | ≥ {{n}} {{résultats}} (en dessous, pas de lecture) |
| 4 | CPL | ≤ cible funnel ({{rappel valeurs}}) |
| 5 | Santé créative | CTR sortant unique ≥ baseline funnel ET hook rate ≥ {{x}} % — sinon elle ne survivra pas au scaling |

## Étape 2 — CONFIRMÉE (check qualité aval obligatoire)
[SI KPI aval trackable :] Export {{CRM}} sur les {{résultats}} de la candidate : {{critères qualité aval + seuils}}. En dessous → **fausse gagnante** : retour en itération message, pas de scale.
[SI KPI aval PAS encore trackable :] ⏳ Tracking {{KPI aval}} pas en place. Règle intérimaire : promotion sur {{KPI principal}} seul, MAIS scaling prudent (+{{x}} % max, un seul palier) tant que le check aval n'est pas possible. Redevient bloquant dès que le tracking existe.

## Étape 3 — WINNER (statut durable)
- ≥ {{n}} {{résultats}} cumulés, {{KPI qualité}} tenu sur **2 semaines glissantes** en scale
- Perf stable après la première montée de budget (pas de décrochage > 1,3x CPL cible sur 3 j)
→ Statut `Winner` dans la DB Concepts Notion · learning BL/CL avec Week tag · hypothèse Roadmap liée validée.

## Protocole de promotion (test → scale)
```
1. NE JAMAIS toucher l'ad set de test gagnant (il continue tel quel)
2. DUPLIQUER la créa vers la campagne de scale ({{CBO/structure client}})
3. Vertical : +{{x}} % de budget max par palier, 72 h entre paliers
4. Horizontal : itérations hooks sur la gagnante (2-3 par batch, jamais 5 d'un coup,
   chacune repasse par les kill rules TEST)
5. Surveillance : garde-fous SCALE de kill-rules.md
```
**Règle d'itération :** pas de chasse à la nouvelle gagnante tant que l'actuelle n'a pas été déclinée. Une gagnante = un filon, pas un one-shot.

## Ce qu'on extrait d'une winner
1. Notion : statut Winner (DB Concepts) + learning BL/CL (angle × persona × hook, avec les chiffres aval)
2. Hypothèses : l'hypothèse validée en génère 2-3 nouvelles (déclinaisons du filon)
3. Anatomie : hook / structure / style documentés dans le brief pour réplication

## Template de log (à chaque passage d'étape)
```
Date · Ad set/Créa · Funnel · Étape (Candidate | Confirmée | Winner | Fausse gagnante)
Dépense cumulée · Leads / {{résultats}} / {{résultats aval}} · CPL · {{KPI principal}} · {{KPI qualité}}
CTR sortant unique · Hook rate · Décision (scale +x % | itérations | retour message | Winner)
```

## Changelog
- **{{date}}** — v1 · Création ({{auteur}}), en miroir de kill-rules.
