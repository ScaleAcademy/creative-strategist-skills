---
name: review-audit
description: "Mines customer reviews to extract verbatims, pain points, triggers, objections, and ad-ready phrases. Use after brand-guidelines to build the raw material for hooks and copy. Trigger on: 'mine les reviews', 'verbatims clients', 'qu'est-ce que les clients disent vraiment', 'language mining'. Produces a structured verbatim library organized by theme."
metadata:
  version: 1.0.0
  status: stable
  tags: [research, verbatims, voc, copywriting, hooks]
  inputs: [URL produit Amazon / Trustpilot / page Google, ou verbatims bruts en paste]
  outputs: [bibliothèque verbatims — 5 buckets, phrases ad-ready surlignées]
  depends-on: [brand-guidelines]
---

# Review Audit

## Before Starting

Confirme avant de commencer :
- [ ] Accès aux reviews (URL Trustpilot / Amazon.fr / Google ou verbatims collés directement)
- [ ] Produit ou catégorie ciblée clairement définie
- [ ] Minimum 20 reviews disponibles (idéalement 50+)
- [ ] `brand-context.md` disponible pour contextualiser les extractions

Si moins de 20 reviews disponibles : utiliser aussi les commentaires Meta (voir sources alternatives dans la référence).

Pour les sources complètes : voir [references/sources.md](references/sources.md)

---

## Phase 1 : Collecte Brute

Collecter toutes les reviews disponibles.
**Ne pas filtrer maintenant.** Copier-coller brut.

Priorité aux reviews longues (200+ mots) — elles contiennent le plus de Layer 3.

---

## Phase 2 : Scoring

Attribuer un score à chaque review :

| Score | Critères |
|---|---|
| 5 — Or | Longue, émotionnelle, spécifique, contient un avant/après |
| 4 — Fort | Détaillée, mentionne une situation ou une émotion précise |
| 3 — Moyen | Générique mais utile pour confirmer un pattern |
| 2 — Faible | Courte, vague, peu actionnable |
| 1 — Inutile | "Super produit", "livraison rapide", aucun contenu |

**Analyser uniquement les scores 4–5.** Les 2–3 servent à confirmer des patterns, pas à extraire.

---

## Phase 3 : Extraction par Bucket

Classer chaque verbatim 4–5 dans l'un des 5 buckets :

### Bucket 1 — Douleurs Avant
Ce que le client vivait AVANT d'acheter.
> Signal : "avant", "j'en pouvais plus", "j'avais tout essayé", "depuis des années"

### Bucket 2 — Déclencheurs d'Achat
Ce qui a provoqué le passage à l'acte.
> Signal : "le jour où", "j'ai décidé", "quand j'ai vu", "quelqu'un m'a conseillé"

### Bucket 3 — Objections Avant Achat
Ce qui avait failli les empêcher d'acheter.
> Signal : "j'avais peur que", "j'hésitais à cause de", "je pensais que ça ne marcherait pas"

### Bucket 4 — Transformations
Comment leur vie a changé après.
> Signal : "maintenant", "depuis que", "je n'aurais jamais cru", "ça a tout changé"

### Bucket 5 — Phrases Ad-Ready ⭐
Formulations directement utilisables dans un hook ou une accroche — sans modification ou presque.

**Critères de qualification pour le Bucket 5 :**
Une phrase mérite le Bucket 5 si elle répond à au moins 3 de ces 5 critères :
- [ ] Se lit comme quelque chose qu'un humain dirait à un ami (pas du marketing)
- [ ] Contient une émotion nommée ou fortement implicite
- [ ] Est spécifique à une situation concrète (pas générique)
- [ ] Crée une curiosité ou une tension naturelle
- [ ] Utilise la langue exacte du persona — aucun mot marketé

**Règle de placement :** Les phrases qui remplissent ces critères vont UNIQUEMENT en Bucket 5, pas dispersées dans les autres buckets. Elles peuvent être extraites de n'importe quel bucket source (1, 2, 3 ou 4).

**Exemples de phrases Bucket 5 :**
- ✅ "J'en pouvais plus de me lever le matin en me demandant à quoi ça sert."
- ✅ "C'est la première fois que je me sens pas jugée pour ce que je mange."
- ✅ "J'avais tellement honte d'en parler à mon médecin."
- ❌ "Le produit est excellent et je le recommande à tous." → Bucket 3 ou discard
- ❌ "Livraison rapide, très satisfait." → Score 1, discard

---

## Phase 4 : Identifier les Patterns

Après extraction, noter :
- Quelles douleurs reviennent le plus souvent ? (top 3)
- Quel déclencheur est le plus fréquent ?
- Quelle objection est la plus bloquante ?
- Quelle transformation est la plus désirée ?
- Y a-t-il des mots ou expressions récurrents ?

---

## Output Format

```markdown
# Verbatim Library — [Produit] — [Date]
*Sources : [Trustpilot / Amazon / etc.] | Reviews analysées : [X] | Scores 4–5 : [Y]*

## Bucket 1 — Douleurs Avant
- "[Verbatim exact]" — Score [4/5]
- "[Verbatim exact]" — Score [4/5]

## Bucket 2 — Déclencheurs d'Achat
- "[Verbatim exact]" — Score [4/5]

## Bucket 3 — Objections Avant Achat
- "[Verbatim exact]" — Score [4/5]

## Bucket 4 — Transformations
- "[Verbatim exact]" — Score [4/5]

## Bucket 5 — Phrases Ad-Ready ⭐
- "[Formulation directement utilisable comme hook]"
- "[Formulation directement utilisable comme hook]"

## Patterns Identifiés
Douleur dominante : [résumé]
Déclencheur le plus fréquent : [résumé]
Objection principale : [résumé]
Transformation la plus désirée : [résumé]
Mots récurrents : [liste]
```

---

## Related Skills

- `01-audit/brand-guidelines` — prérequis
- `02-research/audience-research` — les verbatims alimentent le Layer 3 du persona
- `02-research/customer-reality` — les déclencheurs alimentent le micro-moment mapping
- `03-strategy/hook-writing` — Bucket 5 directement utilisable comme base de hooks
- `03-strategy/creative-brief` — Bucket 1 et 4 alimentent l'angle et la promesse du brief
