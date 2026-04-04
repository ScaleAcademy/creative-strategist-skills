---
name: hook-writing
description: "Writes 10 psychologically-driven hooks calibrated to a specific awareness stage, persona, and creative mechanic. Use after creative-brief is validated. Trigger on: 'écris des hooks', 'génère des accroches', 'première ligne de la pub', 'hook pour [persona]'. Produces a scored hook bank ready for brief integration or direct testing."
metadata:
  version: 1.1.0
  status: stable
  tags: [strategy, hooks, copywriting, psychology, awareness]
  inputs: [creative-brief validé, persona-[nom].md, emotional-map-[persona].md]
  outputs: [10 hooks scorés et classés par awareness + tactic + trigger]
  depends-on: [creative-brief, audience-research, customer-reality]
---

# Hook Writing

## Before Starting

Confirme avant de commencer :
- [ ] Brief créatif validé (`creative-brief.md`)
- [ ] Persona connu avec au moins un verbatim Layer 3
- [ ] Émotion dominante du persona identifiée (customer-reality)
- [ ] Awareness stage ciblé clairement défini
- [ ] Mécanique créative choisie (M1–M8)
- [ ] Medium connu (vidéo ou statique) — un hook vidéo s'entend, un hook statique se lit
- [ ] Format visuel retenu (F01–F45) — le hook doit être cohérent avec le format

**Règle absolue :** Ne jamais écrire de hooks sans brief validé. Un hook sans stratégie est du bruit.

---

## Phase 1 : Charger le Contexte

Avant d'écrire, relire dans l'ordre :
1. L'angle créatif du brief (C1/C2/C3/C4)
2. L'émotion dominante du persona + micro-moment déclencheur
3. La mécanique choisie (M1–M8)
4. Les verbatims Layer 3 disponibles (Bucket 5 du review-audit si disponible)
5. Le format visuel retenu (F01–F45)

Le meilleur hook est souvent une reformulation directe d'un verbatim Layer 3.

---

## Phase 2 : Identifier le Trigger Psychologique

Avant de choisir une tactic, identifier le trigger dominant.

Pour la chaîne complète trigger → tactic → voice pattern : voir [references/psychological-triggers.md](references/psychological-triggers.md)

| Émotion dominante | Trigger prioritaire |
|---|---|
| Frustration | TR3 Pain Agitation |
| Peur | TR8 Urgency / Stakes |
| Honte | TR2 Identity Call-Out |
| Espoir | TR7 Aspiration |
| Colère | TR6 Contrarian |
| Confusion | TR4 Curiosity Gap |
| Résignation | TR1 Pattern Interrupt |

---

## Phase 3 : Sélectionner 3–4 Tactics

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

## Phase 4 : Sélectionner des Voice Patterns

Choisir 2–3 patterns du swipe file qui correspondent au ton voulu.

Pour le swipe file : voir [references/hook-voice-patterns.md](references/hook-voice-patterns.md)

---

## Phase 5 : Écrire les 10 Hooks

### Standards d'écriture

**À faire :**
- Maximum 2 lignes (15–20 mots pour une vidéo, 25 pour un statique)
- Premier mot : verbe d'action, chiffre précis, ou mot exact du persona
- Utiliser les mots exacts du persona (Layer 3 verbatims, Bucket 5)
- 1 hook = 1 tension ouverte — ne pas résoudre dans le hook
- Tester à voix haute (vidéo) : est-ce que ça se dit naturellement ?
- Tester à la lecture rapide (statique) : lisible en < 2s ?

**À éviter :**
- Commencer par "Vous", "Votre", "Notre produit"
- Résoudre la tension dans le hook lui-même
- Utiliser du vocabulaire marketing ("révolutionnaire", "innovant", "unique")
- Poser une question rhétorique sans vraie curiosité gap derrière
- Écrire pour toutes les audiences — 1 hook = 1 persona précis

### Format de production

Produire 10 hooks en variant :
- 3–4 triggers différents
- 3–4 tactics correspondantes
- 2–3 voice patterns différents
- Ton direct vs ton narratif
- Question vs affirmation

---

## Phase 6 : Scorer et Sélectionner

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
**Trigger :** [TR#]
**Tactic :** [T##]
**Voice Pattern :** [Cluster #]
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

## Références

- [references/psychological-triggers.md](references/psychological-triggers.md) — Les 8 triggers avec chaîne trigger → tactic → voice pattern
- [references/hook-tactics.md](references/hook-tactics.md) — 35+ tactics avec templates et exemples FR
- [references/hook-voice-patterns.md](references/hook-voice-patterns.md) — Swipe file de patterns natifs du feed

## Related Skills

- `03-strategy/creative-brief` — prérequis absolu
- `02-research/customer-reality` — source de l'émotion dominante et du micro-moment
- `02-research/review-audit` — source des verbatims Layer 3 (Bucket 5)
- `04-production/video-production` — les hooks Top 3 alimentent le brief de production
- `04-production/static-production` — adaptation des hooks pour le format statique
