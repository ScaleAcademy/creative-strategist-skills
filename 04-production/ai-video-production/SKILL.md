---
name: ai-video-production
description: "Turns a validated creative brief into scene-by-scene prompts for AI video generation tools (VEO3, Kling, Runway). Use when producing video with AI tools instead of human editors. Trigger on: 'prompts VEO3', 'prompt Kling', 'génère une vidéo IA', 'AI video brief'. Produces a scene-by-scene prompt pack ready to execute in the chosen AI tool."
metadata:
  version: 1.0.0
  status: beta
  tags: [production, ai-video, VEO3, Kling, prompts]
  inputs: [creative-brief validé, hook sélectionné, images de référence si disponibles]
  outputs: [pack de prompts scène par scène pour VEO3 / Kling]
  depends-on: [creative-brief, hook-writing]
---

# AI Video Production

## Before Starting

Confirme avant de commencer :
- [ ] Brief créatif validé
- [ ] Hook sélectionné
- [ ] Outil IA défini : VEO3 (Google) ou Kling (Kuaishou) ou Runway
- [ ] Durée cible par scène définie (recommandé : 3–8s par scène)
- [ ] Images de référence disponibles si cohérence visuelle requise (character consistency)
- [ ] Style visuel défini (réaliste / cinématique / UGC simulé / animé)

---

## Principes de Prompting Vidéo IA

### Structure d'un Prompt Scène

```
[Sujet] [Action] [Setting] [Angle caméra] [Mouvement caméra] [Éclairage] [Style] [Ambiance / Émotion] [Durée]
```

**Règles :**
- 1 scène = 1 prompt. Ne pas combiner deux actions dans le même prompt.
- Nommer l'action avant le contexte : "Une femme ouvre [objet]" pas "Dans une cuisine, une femme..."
- Préciser le mouvement caméra : statique / lent zoom / tracking / handheld / drone
- Préciser l'éclairage : naturel / golden hour / studio / low key / overcast
- Éviter les mots abstraits : "magnifique", "incroyable" — décrire le concret

### Cohérence Visuelle Inter-Scènes

Pour garder le même personnage entre les scènes :
- Décrire physiquement le personnage à chaque prompt (âge, genre, tenue, couleur cheveux)
- Utiliser une image de référence si l'outil le permet (Kling = image + prompt)
- Garder le même setting / décor entre les scènes liées

---

## Phase 1 : Découper le Brief en Scènes

Reprendre la structure narrative du brief (Hook → Tension → Résolution → CTA) et la convertir en scènes de 3–8 secondes.

**Nombre de scènes recommandé :**
- 15s → 3–4 scènes
- 30s → 5–6 scènes
- 60s → 8–10 scènes

---

## Phase 2 : Écrire les Prompts

Pour chaque scène :

```markdown
**Scène [#] — [Nom / Rôle dans la structure]**
Durée : [3–8s]
Outil : [VEO3 / Kling / Runway]

Prompt :
"[Description complète selon la structure : sujet + action + setting + caméra + lumière + style + émotion]"

Image de référence : [Oui / Non — lien si oui]
Note de production : [Conseil spécifique à cet outil]
```

---

## Phase 3 : Assembler et Tester

Après génération de toutes les scènes :
1. Visionner chaque scène individuellement
2. Vérifier la cohérence visuelle (personnage, setting, style)
3. Assembler dans l'ordre narratif
4. Ajouter texte overlay, sous-titres, musique en post (CapCut / Premiere / DaVinci)
5. Vérifier : la séquence tient-elle sans son ? (silent viewing test)

---

## Output Format

```markdown
# AI Video Prompt Pack — [Marque] — [Creative ID] — [Date]

## Contexte
Outil principal : [VEO3 / Kling / Runway]
Durée totale : [Xs]
Style : [Réaliste UGC / Cinématique / Animé]
Personnage principal : [Description physique complète]

## Scènes

### Scène 1 — Hook [0–3s]
Prompt : "[Prompt complet]"
Image réf : [Lien / Non]

### Scène 2 — [Nom] [3–Xs]
[Même structure]

[...]

## Post-Production
- Texte overlay à ajouter : "[Hook textuel]" — [Position, police, timing]
- Sous-titres : [Oui / Non]
- Musique : [Style / Référence]
- CTA final : "[Texte]" — [Timing d'apparition]
```

---

## Related Skills

- `03-strategy/creative-brief` — prérequis
- `03-strategy/hook-writing` — hook → première scène
- `04-production/video-production` — version brief monteur humain du même concept
- `04-production/campaign-setup` — après production
