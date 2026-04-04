---
name: creative-brief
description: "Builds a complete creative brief from research outputs. The brief defines the angle, awareness stage, hook direction, creative mechanic, format, specs, and success criteria. Use after audience-research and customer-reality. Trigger on: 'fait un brief', 'brief créatif', 'on prépare une campagne', 'je veux lancer des pubs'. This is the central strategic document — nothing goes to production without it."
metadata:
  version: 1.0.0
  status: stable
  tags: [strategy, brief, angle, creative, planning]
  inputs: [brand-context.md, persona-[nom].md, emotional-map-[persona].md, objectif campagne]
  outputs: [creative-brief-[marque]-[date].md]
  depends-on: [brand-guidelines, audience-research, customer-reality]
---

# Creative Brief

## Before Starting

Confirme avant de commencer :
- [ ] `brand-context.md` disponible
- [ ] `persona-[nom].md` disponible (audience-research exécuté)
- [ ] `emotional-map-[persona].md` disponible (customer-reality exécuté) OU verbatims disponibles
- [ ] Objectif business clair : acquisition / lead / awareness / retargeting ?
- [ ] KPI principal défini : CPA cible, CPL, ou ROAS ?
- [ ] Budget et capacité de production définis

Sans ces inputs, le brief sera basé sur des hypothèses — à labeler clairement.

---

## Phase 1 : Définir le Contexte Stratégique

Synthétiser depuis les documents disponibles :

1. **Persona ciblé** — Qui ? Quel layer dominant ?
2. **Awareness stage** — Où en est l'audience par rapport au problème et au produit ?
3. **Objectif de la creative** — Que doit-elle produire comme action ?
4. **Phase funnel** — TOF / MOF / BOF / Re-engage

---

## Phase 2 : Sélectionner l'Angle

Choisir parmi les 4 catégories d'angles.

Pour le cadre complet : voir [references/ad-angles.md](references/ad-angles.md)

| Angle | Quand l'utiliser |
|---|---|
| C1 — Problème | Audience Problem Aware, douleur forte et identifiable |
| C2 — Résultat | Audience Solution/Product Aware, preuve sociale disponible |
| C3 — Éducation | Marché sophistiqué ou audience Unaware/Problem Aware |
| C4 — Identité | Marché très sophistiqué ou audience Most Aware |

**Formuler l'angle en 1 phrase :** "Cette creative parle à [persona] qui [situation] et lui montre [promesse] via [angle]."

---

## Phase 3 : Choisir la Mécanique Créative

Sélectionner la mécanique qui correspond à l'angle et à l'émotion dominante.

Pour le cadre des 8 mécaniques : voir [references/creative-mechanics.md](../hook-writing/references/creative-mechanics.md)

---

## Phase 4 : Définir le Format et les Specs

| Décision | Options |
|---|---|
| Medium | Vidéo / Statique / Carousel |
| Durée (si vidéo) | 15s / 30s / 60s / 90s+ |
| Ratio | 9:16 (Stories/Reels) / 4:5 (Feed) / 1:1 (Multi) |
| Style | UGC / Talking head / Produit / B-roll / Animation |
| Son | Avec voix / Musique seule / Silent (sous-titres) |

---

## Phase 5 : Écrire le Brief

```markdown
# Creative Brief — [Marque] — [Date]
*Statut : Draft / Validé*

## Contexte
- Persona : [Prénom fictif] — [Awareness stage]
- Objectif : [Acquisition / Lead / Awareness / Retargeting]
- Phase funnel : [TOF / MOF / BOF]
- KPI primaire : [CPA / CPL / CTR / ROAS cible]

## Angle Créatif
[C1 / C2 / C3 / C4] — [Intitulé de l'angle en 1 phrase]

## Promesse Centrale
[Ce que la creative promet — 1 phrase, langage client]

## Proof Point Principal
[La preuve qui rend la promesse crédible]

## Objection à Lever
[Ce qui pourrait empêcher l'action — et comment on l'adresse]

## Mécanique
[M1–M8] — [Nom de la mécanique] — [Comment elle s'applique ici]

## Hook Direction
[Direction de la première ligne / première seconde — ne pas écrire le hook ici]
Tactic recommandée : [T01–T35]
Trigger psychologique : [biais ou désir LF]

## Format
- Medium : [Vidéo / Statique / Carousel]
- Durée : [Xs]
- Ratio : [9:16 / 4:5 / 1:1]
- Style : [UGC / Talking head / etc.]
- Son : [Voix on / off / silent]

## CTA
[Texte du call-to-action — précis et adapté à l'awareness]

## Contraintes
[Compliance, ton, visuels interdits, claims à éviter]

## Succès = ?
[Ce qui définit une bonne performance pour ce brief]
CPA cible : [X€] / CTR cible : [X%] / Autre :
```

---

## Phase 6 : Valider Avant Production

Poser ces questions avant de passer à la production :

- Est-ce que le persona se reconnaîtrait dans cette creative ?
- La promesse est-elle crédible sans chercher à en savoir plus ?
- L'objection principale est-elle adressée quelque part ?
- Le format est-il adapté à la plateforme et au moment du scroll ?
- L'angle n'a-t-il pas déjà été saturé par les concurrents ?

---

## Related Skills

- `02-research/audience-research` — persona
- `02-research/customer-reality` — émotion + micro-moment
- `02-research/market-research` — angle vs concurrence
- `03-strategy/hook-writing` — prochaine étape après brief validé
- `03-strategy/message-sequencing` — si la campagne est multi-touchpoints
- `04-production/static-production` — brief → exécution statique
- `04-production/video-production` — brief → exécution vidéo
