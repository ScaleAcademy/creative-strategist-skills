---
name: hook-writing
description: "Writes 10 psychologically-driven hooks calibrated to a specific awareness stage, persona, and creative mechanic. Use after creative-brief is validated. Trigger on: 'écris des hooks', 'génère des accroches', 'première ligne de la pub', 'hook pour [persona]'. Produces a scored hook bank ready for brief integration or direct testing."
metadata:
  version: 1.0.0
  status: stable
  tags: [strategy, hooks, copywriting, psychology, awareness]
  inputs: [creative-brief validé, persona-[nom].md, emotional-map-[persona].md]
  outputs: [10 hooks scorés et classés par awareness + tactic]
  depends-on: [creative-brief, audience-research, customer-reality]
---

# Hook Writing

## Before Starting

Confirme avant de commencer :
- [ ] Brief créatif validé (`creative-brief.md`)
- [ ] Persona connu avec au moins un verbatim Layer 3
- [ ] Awareness stage ciblé clairement défini
- [ ] Mécanique créative choisie (M1–M8)
- [ ] Medium connu (vidéo ou statique) — un hook vidéo s'entend, un hook statique se lit

**Règle absolue :** Ne jamais écrire de hooks sans brief validé. Un hook sans stratégie est du bruit.

---

## Phase 1 : Charger le Contexte

Avant d'écrire, relire :
1. L'angle créatif du brief (C1/C2/C3/C4)
2. L'émotion dominante du persona
3. Le micro-moment déclencheur
4. La mécanique choisie (M1–M8)
5. Les verbatims Layer 3 disponibles

Le meilleur hook est souvent une reformulation directe d'un verbatim Layer 3.

---

## Phase 2 : Sélectionner 3–4 Tactics

Choisir des tactics complémentaires qui correspondent à l'awareness stage.

Pour la liste complète : voir [references/hook-tactics.md](references/hook-tactics.md)

| Awareness | Tactics recommandées |
|---|---|
| Unaware | T01 Aspirational, T26 Storytelling, T31 What If, T06 Curiosity Gap |
| Problem Aware | T17 Pain Agitation, T09 Empathy, T20 Problem-First, T15 Myth-Busting |
| Solution Aware | T03 Bold Claim, T02 Authority, T34 Comparison, T12 How-To |
| Product Aware | T25 Social Proof, T23 Risk Reversal, T27 Transformation, T08 Direct Address |
| Most Aware | T29 Urgency, T10 Exclusivity, T11 FOMO, T35 Future Pacing |

---

## Phase 3 : Sélectionner des Voice Patterns

Choisir 2–3 patterns du swipe file qui correspondent au ton voulu.

Pour le swipe file : voir [references/hook-voice-patterns.md](references/hook-voice-patterns.md)

---

## Phase 4 : Écrire les 10 Hooks

**Règles d'écriture :**
- Maximum 2 lignes (15–20 mots max pour une vidéo, 25 pour un statique)
- Premier mot : verbe, chiffre, ou mot du persona — jamais "vous" ou "votre produit"
- Tester à voix haute : si ça sonne comme une pub, recommencer
- Utiliser les mots exacts du persona quand possible (Layer 3 verbatims)
- 1 hook = 1 tension ouverte — ne pas tout résoudre dans le hook

**Format de production :**
Produire 10 hooks en variant :
- 3–4 tactics différentes
- 2–3 voice patterns différents
- Ton direct vs ton narratif
- Question vs affirmation

---

## Phase 5 : Scorer et Sélectionner

Pour chaque hook, évaluer sur 3 critères (score 1–5) :

| Critère | Question |
|---|---|
| Arrêt du scroll | Est-ce que ce hook force à s'arrêter ? |
| Reconnaissance | Le persona se reconnaît-il immédiatement ? |
| Curiosité ouverte | Est-ce que ça donne envie de voir la suite ? |

Score total max = 15. Recommander les 3 hooks avec score > 11.

---

## Output Format

```markdown
# Hook Bank — [Marque] — [Persona] — [Awareness] — [Date]

## Contexte
- Angle : [C1/C2/C3/C4]
- Mécanique : [M1–M8]
- Awareness : [Niveau]
- Ton dominant : [intime / direct / éducatif / narratif]

## Les 10 Hooks

### Hook 1
**Texte :** "[Hook complet]"
**Tactic :** [T##]
**Trigger :** [Biais / LF]
**Score :** [X/15] — Scroll [X] · Reconnaissance [X] · Curiosité [X]

### Hook 2
[Même structure]

[...]

## Top 3 Recommandés
1. Hook [#] — Score [X/15] — Raison
2. Hook [#] — Score [X/15] — Raison
3. Hook [#] — Score [X/15] — Raison

## Notes de Production
[Indications spécifiques : rythme, ton de voix, premier frame visuel recommandé]
```

---

## Related Skills

- `03-strategy/creative-brief` — prérequis absolu
- `02-research/customer-reality` — source du micro-moment et de l'émotion
- `02-research/review-audit` — source des verbatims Layer 3
- `04-production/video-production` — les hooks Top 3 alimentent le brief de production
- `04-production/static-production` — adaptation des hooks pour le format statique
