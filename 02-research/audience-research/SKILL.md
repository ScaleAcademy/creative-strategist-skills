---
name: audience-research
description: "Builds a 3-layer persona from existing data and research. Use after brand-guidelines to deepen audience understanding before brief writing. Trigger on: 'qui est notre audience', 'construis un persona', 'deep dive audience', 'à qui on parle vraiment'. Produces a complete persona document ready to feed creative-brief and hook-writing."
metadata:
  version: 1.0.0
  status: stable
  tags: [research, persona, audience, psychology]
  inputs: [brand-context.md, données client existantes (CRM / interviews / reviews)]
  outputs: [persona-[nom].md — Layer 1/2/3 complet]
  depends-on: [brand-guidelines]
---

# Audience Research

## Before Starting

Confirme avant de commencer :
- [ ] `brand-context.md` disponible
- [ ] Au moins une source de données audience disponible (CRM, interviews, reviews, analytics)
- [ ] Persona cible identifié ou à déterminer (primaire vs secondaire)
- [ ] Awareness stage dominant connu ou à déterminer

Sans données réelles, ce skill produit des hypothèses — les labeler clairement comme telles.

---

## Phase 1 : Identifier le Persona à Construire

Poser ces questions avant de commencer :
1. Y a-t-il déjà un persona documenté ? Si oui, le charger et l'enrichir plutôt que repartir de zéro.
2. Quel est le produit / l'offre principale ciblée par ce persona ?
3. Quel est le niveau d'awareness présumé de ce persona ?

---

## Phase 2 : Construire le Layer 1 — Démographique

À extraire des données existantes ou à rechercher :

- Âge et genre (dominant dans les achats ou la base client)
- Situation professionnelle et niveau de revenus
- Localisation (urbain / péri-urbain / rural ; région ou pays)
- Plateformes sociales actives (Meta, TikTok, YouTube, LinkedIn)
- Comportement d'achat : impulsif vs réfléchi, prix-sensible vs valeur-sensible

**Sources :** Analytics Facebook/Instagram, Google Analytics démographies, CRM client.

Pour le cadre Layer 1/2/3 : voir [references/persona-layers.md](references/persona-layers.md)

---

## Phase 3 : Construire le Layer 2 — Psychographique

À extraire via interviews, reviews longues, Reddit, forums de niche.

- Valeur prioritaire (liberté, sécurité, statut, performance, famille)
- Identité perçue : "Je suis quelqu'un qui..."
- Identité aspirationnelle : "Je veux être quelqu'un qui..."
- Peurs profondes (souvent non dites en public)
- Rapport à l'échec et au risque
- Références culturelles : influenceurs suivis, marques admirées

Pour le cadre LF8 : voir [references/life-force-8.md](references/life-force-8.md)
Pour les biais actifs : voir [references/marketing-psychology.md](references/marketing-psychology.md)

---

## Phase 4 : Construire le Layer 3 — Situationnel

C'est le layer le plus précieux et le plus difficile à obtenir sans données réelles.

Questions à poser en interview ou à extraire dans les reviews :
- "Décris-moi la journée où tu as décidé de chercher une solution."
- "Qu'est-ce que tu faisais exactement quand tu as réalisé que tu avais ce problème ?"
- "Quelle était ta principale hésitation avant d'acheter ?"
- "Qu'est-ce qui t'a finalement convaincu ?"
- "Que dirais-tu à quelqu'un qui hésite encore ?"

Extraire :
- Le micro-moment déclencheur (situation précise, heure, contexte)
- La phrase exacte utilisée pour décrire la douleur
- L'objection principale avant achat
- L'émotion dominante au moment de l'achat

---

## Phase 5 : Mapper l'Awareness

Sur la base du Layer 3, situer le persona sur l'échelle d'awareness.

Pour le cadre complet : voir [references/awareness-levels.md](../market-research/references/awareness-levels.md)

---

## Output Format

Sauvegarder sous `persona-[prenom-fictif].md` dans le dossier du projet.

```markdown
# Persona — [Prénom fictif] — [Produit]
*Généré le [date] | Awareness dominant : [niveau]*

## Layer 1 — Démographique
- Âge / Genre :
- Situation pro :
- Revenus approximatifs :
- Localisation :
- Plateformes actives :

## Layer 2 — Psychographique
- Valeur n°1 :
- Identité actuelle : "Je suis quelqu'un qui..."
- Identité aspirationnelle : "Je veux être..."
- Peur profonde :
- LF dominant : [LF1–LF8]
- Biais principal actif : [biais]

## Layer 3 — Situationnel
- Micro-moment déclencheur :
- Phrase exacte (verbatim) :
- Objection principale :
- Ce qui a convaincu :
- Émotion dominante :

## Awareness Stage
[Niveau 1–5] — [Rationale]

## Direction Créative
→ Angle recommandé :
→ Ton :
→ Format :
→ Hook direction :
```

---

## Related Skills

- `01-audit/brand-guidelines` — prérequis
- `02-research/review-audit` — source Layer 3
- `02-research/customer-reality` — enrichit micro-moments et mapping émotionnel
- `03-strategy/creative-brief` — output direct de ce skill
- `03-strategy/hook-writing` — utilise Layer 3 pour calibrer les hooks
