---
name: customer-reality
description: "Maps the emotional reality of the target persona: dominant emotion, private vs social pain, acute vs chronic pain, and triggering micro-moments. Use after review-audit and audience-research to go deeper than demographics. Trigger on: 'cartographie émotionnelle', 'micro-moments', 'réalité client', 'ce que ressent vraiment l'audience'. Produces an emotional map that directly informs hook direction and creative tone."
metadata:
  version: 1.0.0
  status: stable
  tags: [research, emotion, micro-moments, persona, psychology]
  inputs: [persona-[nom].md, verbatim library (review-audit)]
  outputs: [emotional-map-[persona].md — cartographie émotionnelle complète]
  depends-on: [brand-guidelines, audience-research, review-audit]
---

# Customer Reality

## Before Starting

Confirme avant de commencer :
- [ ] `persona-[nom].md` disponible (audience-research exécuté)
- [ ] Verbatim library disponible (review-audit exécuté) ou au moins 10 verbatims bruts
- [ ] Produit et contexte d'usage clairement définis

Ce skill ne produit rien de valeur sans données réelles du persona. Ne pas improviser les émotions — les extraire.

---

## Phase 1 : Identifier l'Émotion Dominante

À partir des verbatims du Bucket 1 (douleurs) et Bucket 4 (transformations), identifier l'émotion la plus présente.

**Émotions à détecter :**

| Émotion | Signaux verbatims |
|---|---|
| Frustration | "j'en ai marre", "j'ai tout essayé", "rien ne marche" |
| Peur | "j'ai peur que", "et si", "je risque de" |
| Honte | "je n'ose pas en parler", "les gens pensent que" |
| Espoir | "j'aimerais tellement", "je rêve de", "si seulement" |
| Colère | "c'est scandaleux", "personne ne dit la vérité" |
| Confusion | "je ne comprends pas pourquoi", "tout le monde dit X mais" |
| Résignation | "j'ai appris à vivre avec", "c'est comme ça" |

Pour la cartographie complète : voir [references/emotional-mapping.md](references/emotional-mapping.md)

---

## Phase 2 : Qualifier la Douleur

### Q2A — Privée ou Sociale ?

**Douleur privée :** Vécue en silence. La personne n'en parle pas.
→ Tone : intime, confidentiel. Formats : texte overlay, voix off calme, confession face caméra.

**Douleur sociale :** Liée au regard des autres. La personne craint le jugement.
→ Tone : de soutien, non-jugeant. Formats : testimonial, communauté, "tu n'es pas seul(e)".

**Indices dans les verbatims :**
- Pronoms "je / moi" = privée
- Mentions "les gens / mon entourage / ma famille / au travail" = sociale

### Q2B — Aiguë ou Chronique ?

**Douleur aiguë :** Déclenchée récemment. Intense et urgente.
→ Indicateurs temporels : "ce matin", "la semaine dernière", "depuis l'accident"
→ Hook : ancrer dans le moment précis. Urgence naturelle.

**Douleur chronique :** Présente depuis longtemps. Normalisée, presque acceptée.
→ Indicateurs : "depuis toujours", "j'ai appris à vivre avec", "ça a toujours été comme ça"
→ Hook : révéler que ce n'est pas une fatalité. "Tu n'as pas à continuer à..."

---

## Phase 3 : Identifier le Micro-Moment Déclencheur

Extraire du Bucket 2 (déclencheurs) le micro-moment le plus fréquent ou le plus intense.

**4 types de micro-moments :**
1. **Limite** — un événement a tout déclenché ("le jour où j'ai réalisé que...")
2. **Récurrent** — une boucle régulière ("chaque lundi matin", "à chaque fin de mois")
3. **Comparaison** — un écart perçu ("mon collègue venait d'acheter...", "j'ai vu que X...")
4. **Anticipation** — une peur projetée ("si ça continue dans 5 ans...")

Pour le cadre complet : voir [references/micro-moments.md](references/micro-moments.md)

---

## Phase 4 : Dériver la Direction Créative

À partir de la cartographie, formuler :
- Le ton adapté (intime / collectif / urgent / éducatif)
- Le format recommandé
- La direction du hook (amorce émotionnelle vs situationnelle vs identitaire)
- L'awareness stage confirmé ou révisé

---

## Output Format

```markdown
# Emotional Map — [Persona] — [Produit] — [Date]

## Émotion Dominante
[Émotion] — [2 verbatims qui la confirment]

## Qualification de la Douleur
- Privée ou Sociale : [Private / Social] — [Raison]
- Aiguë ou Chronique : [Acute / Chronic] — [Raison]

## Micro-Moment Principal
Type : [Limite / Récurrent / Comparaison / Anticipation]
Description : [Situation précise]
Verbatim associé : "[Citation exacte]"

## Direction Créative
→ Ton : [intime / collectif / urgent / éducatif]
→ Format recommandé : [format ou type]
→ Hook direction : [description de l'amorce]
→ Awareness confirmé : [Niveau 1–5]
→ Mécanique recommandée : [M1–M8]
```

---

## Related Skills

- `02-research/review-audit` — source des verbatims
- `02-research/audience-research` — source du persona
- `03-strategy/creative-brief` — emotional map → angle et ton du brief
- `03-strategy/hook-writing` — micro-moment → première ligne du hook
