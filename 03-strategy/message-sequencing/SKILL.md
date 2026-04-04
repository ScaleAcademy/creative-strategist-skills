---
name: message-sequencing
description: "Plans a full-funnel message sequence: 4–5 touchpoints mapped to awareness stages, with angle, format, and CTA for each. Use after creative-brief when the campaign spans multiple awareness stages. Trigger on: 'plan de séquence', 'funnel créatif', 'parcours publicitaire', 'TOF MOF BOF', 'séquence de touchpoints'. Produces a sequencing plan ready to brief the production team."
metadata:
  version: 1.0.0
  status: stable
  tags: [strategy, sequencing, funnel, planning, retargeting]
  inputs: [creative-brief.md, awareness stage de départ du persona]
  outputs: [sequencing-plan-[marque]-[date].md — plan 4–5 touchpoints]
  depends-on: [creative-brief, audience-research]
---

# Message Sequencing

## Before Starting

Confirme avant de commencer :
- [ ] Brief créatif disponible pour au moins 1 touchpoint
- [ ] Awareness stage de départ du persona connu
- [ ] Budget disponible pour tester plusieurs phases (pas utile sur petit budget mono-phase)
- [ ] Structure de campagne Meta définie ou à définir

Ce skill n'est utile que si la marque a les moyens de déployer 3+ touchpoints. Sur un budget test < 1 000€/mois, prioriser 1 seul angle fort plutôt qu'une séquence.

---

## Principe de Séquencement

L'audience se déplace sur l'échelle d'awareness au fil des touchpoints.
Chaque touchpoint doit faire avancer le prospect d'un niveau — pas vendre à chaque étape.

```
Unaware → TOF : éduquer / éveiller
Problem Aware → TOF/MOF : valider la douleur / montrer une solution existe
Solution Aware → MOF : différencier / prouver le mécanisme
Product Aware → MOF/BOF : lever les objections / renforcer la preuve
Most Aware → BOF : offre directe / urgence
```

---

## Phase 1 : Définir le Point d'Entrée

Identifier l'awareness stage dominant du persona à l'entrée du funnel.
→ C'est de là que commence la séquence.

---

## Phase 2 : Construire les Touchpoints

Pour chaque étape du funnel, définir :

| Champ | Contenu |
|---|---|
| Awareness stage ciblé | Niveau 1–5 |
| Objectif du touchpoint | Éveiller / Éduquer / Différencier / Lever objection / Convertir |
| Angle créatif | C1 / C2 / C3 / C4 |
| Format recommandé | Vidéo / Statique / Carousel |
| Durée (si vidéo) | 15s / 30s / 60s / 90s |
| Hook direction | Amorce émotionnelle, situationnelle, ou identitaire |
| CTA | Soft / Medium / Direct |
| Audience Meta | Cold / Engagés / Visiteurs / Panier / Clients |

---

## Phase 3 : Plan de Séquence Recommandé

### Structure Standard 5 Touchpoints

**TP1 — TOF Cold : Éveiller**
- Audience : Froide (intérêts, lookalike)
- Awareness ciblé : Unaware ou Problem Aware
- Objectif : Faire naître la prise de conscience
- Angle : C1 (douleur) ou C3 (éducation)
- CTA : "En savoir plus" / "Découvrir"
- Format : Vidéo 30–60s ou Reel

**TP2 — TOF/MOF : Qualifier**
- Audience : Engagés TP1 (vues vidéo 25%+, interactions)
- Awareness ciblé : Problem Aware → Solution Aware
- Objectif : Faire comprendre qu'une solution existe et qu'elle est différente
- Angle : C3 (mécanisme) ou C2 (résultat)
- CTA : "Voir comment ça marche"
- Format : Vidéo 45–90s ou Carousel éducatif

**TP3 — MOF : Prouver**
- Audience : Visiteurs page produit ou engagés TP2
- Awareness ciblé : Solution Aware → Product Aware
- Objectif : Convaincre que ce produit est le bon choix
- Angle : C2 (preuve sociale) ou C4 (identité)
- CTA : "Voir les résultats" / "Rejoindre"
- Format : Témoignage vidéo ou statique proof

**TP4 — BOF : Lever les Objections**
- Audience : Visiteurs page produit sans conversion (retargeting chaud)
- Awareness ciblé : Product Aware → Most Aware
- Objectif : Éliminer le dernier frein à l'achat
- Angle : C2 (garantie / risk reversal) ou C1 (coût de l'inaction)
- CTA : "Essayer sans risque" / "Voir l'offre"
- Format : Vidéo courte 15–30s ou statique offre

**TP5 — Re-engage : Urgence**
- Audience : Panier abandonné ou leads non convertis
- Awareness ciblé : Most Aware
- Objectif : Déclencher l'action finale
- Angle : Offre directe + urgence
- CTA : "Acheter maintenant" / "Rejoindre avant [date]"
- Format : Statique offre ou vidéo < 15s

---

## Output Format

```markdown
# Sequencing Plan — [Marque] — [Date]

## Awareness de Départ : [Niveau]
## Objectif Final : [Conversion / Lead / Inscription]

| # | Phase | Audience | Awareness | Angle | Format | CTA |
|---|---|---|---|---|---|---|
| TP1 | TOF Cold | Froide | [1–2] | [C#] | [Format] | [CTA] |
| TP2 | TOF/MOF | Engagés TP1 | [2–3] | [C#] | [Format] | [CTA] |
| TP3 | MOF | Visiteurs | [3–4] | [C#] | [Format] | [CTA] |
| TP4 | BOF | Retargeting | [4–5] | [C#] | [Format] | [CTA] |
| TP5 | Re-engage | Panier / Leads | [5] | Offre directe | [Format] | [CTA] |

## Notes de Production
[Priorité de production, budget suggéré par phase, kill rules par touchpoint]

## Briefs à Produire
- [ ] Brief TP1 → `creative-brief` à lancer
- [ ] Brief TP2 → `creative-brief` à lancer
- [...]
```

---

## Related Skills

- `03-strategy/creative-brief` — un brief par touchpoint
- `04-production/campaign-setup` — structure campagne Meta correspondante
- `05-analysis/ad-analysis` — analyse creative par touchpoint
- `05-analysis/strategy-gap` — identifier les phases non couvertes
