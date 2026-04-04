---
name: strategy-gap
description: "Identifies missing angles, untested personas, uncovered awareness stages, and format gaps in the current creative strategy. Use after account-audit or when performance plateaus. Trigger on: 'qu'est-ce qu'on ne teste pas', 'angles manquants', 'gap stratégique', 'on tourne en rond'. Produces a prioritized gap report with sprint recommendations."
metadata:
  version: 1.0.0
  status: stable
  tags: [analysis, strategy, gaps, testing, planning]
  inputs: [données campagne actuelle, account-audit report ou ad-analysis reports]
  outputs: [gap report — top 3 gaps priorisés + recommandation sprint]
  depends-on: [account-audit]
---

# Strategy Gap

## Before Starting

Confirme avant de commencer :
- [ ] Au minimum un `account-audit` récent disponible, ou plusieurs `ad-analysis` individuels
- [ ] Historique de test disponible (quels angles / formats / personas ont déjà été testés)
- [ ] `brand-context.md` disponible pour contexte
- [ ] Objectif business du prochain sprint défini

Ce skill ne crée pas de nouveaux angles depuis rien — il identifie ce qui manque dans ce qui existe.

Pour la grille complète : voir [references/gap-matrix.md](references/gap-matrix.md)

---

## Phase 1 : Cartographier l'Existant

Construire un inventaire de ce qui a été testé :

**Awareness gaps :**
Quels niveaux d'awareness ont des creatives actives ? Lesquels n'en ont pas ?

**Angle gaps :**
Quels angles C1/C2/C3/C4 ont été testés ? Lesquels sont absents ?

**Persona gaps :**
Combien de personas distincts ont été adressés directement ? Lesquels sont ignorés ?

**Format gaps :**
Quels formats ont été testés ? Quels formats n'ont jamais été lancés ?

**Mechanic gaps :**
Quelles mécaniques créatives (M1–M8) sont présentes dans le compte ? Lesquelles sont absentes ?

---

## Phase 2 : Qualifier les Gaps

Pour chaque gap identifié, évaluer :

| Critère | Score 1–3 |
|---|---|
| Volume d'audience potentiel touché | |
| Facilité de production du test | |
| Signal préliminaire justifiant le test | |
| Alignement avec objectif sprint | |

Score > 9 = priorité haute.

---

## Phase 3 : Formuler les Recommandations de Sprint

Convertir les top 3 gaps en recommendations concrètes :
- Description du gap
- Hypothèse de ce que combler ce gap pourrait produire
- Creative spécifique à produire pour tester
- Priorité (Haute / Moyenne)

---

## Output Format

```markdown
# Strategy Gap Report — [Marque] — [Date]

## Inventaire — Ce qui a Été Testé
| Dimension | Testé | Non testé |
|---|---|---|
| Awareness | | |
| Angles | | |
| Personas | | |
| Formats | | |
| Mécaniques | | |

## Top 3 Gaps Identifiés

### Gap 1 — [Titre]
**Dimension :** [Awareness / Angle / Persona / Format / Mécanique]
**Description :** [Ce qui manque]
**Hypothèse :** [Ce que combler ce gap pourrait produire]
**Test recommandé :** [1 creative précise à produire]
**Score :** [X/12] — Priorité : Haute

### Gap 2
[Même structure]

### Gap 3
[Même structure]

## Recommandation Sprint
→ [X] briefs à lancer ce sprint pour couvrir les gaps prioritaires
→ Budget de test recommandé : [X€]
→ Briefs à créer : voir `03-strategy/creative-brief`
```

---

## Related Skills

- `05-analysis/account-audit` — source principale des données
- `05-analysis/ad-analysis` — pour approfondir chaque gap avec des données individuelles
- `03-strategy/creative-brief` — pour briefe les tests recommandés
- `03-strategy/message-sequencing` — si le gap concerne une phase funnel entière
