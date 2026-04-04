---
name: video-production
description: "Turns a validated creative brief into a sequenced technical brief for a human video editor or creator. Use after creative-brief and hook-writing when the format is video. Trigger on: 'brief vidéo', 'brief monteur', 'script vidéo', 'séquence de scènes'. Produces a scene-by-scene production brief ready to hand to the production team."
metadata:
  version: 1.0.0
  status: beta
  tags: [production, video, script, brief, editing]
  inputs: [creative-brief validé, hook sélectionné, assets disponibles (footage, UGC, produit)]
  outputs: [brief technique vidéo — scène par scène]
  depends-on: [creative-brief, hook-writing]
---

# Video Production

## Before Starting

Confirme avant de commencer :
- [ ] Brief créatif validé
- [ ] Hook sélectionné (top 1 du hook bank)
- [ ] Durée cible définie (15s / 30s / 45s / 60s / 90s)
- [ ] Assets disponibles inventoriés (footage UGC, footage produit, images, voix off)
- [ ] Style défini (UGC natif / talking head / B-roll produit / montage dynamique)

---

## Phase 1 : Définir la Structure Narrative

Toute vidéo publicitaire suit une structure de tension-résolution :

```
Hook (0–3s) → Tension (3–15s) → Pivot (15–X s) → Résolution (X–fin) → CTA
```

**Pour 15s :** Hook (3s) → Tension courte (7s) → CTA direct (5s)
**Pour 30s :** Hook (3s) → Tension (12s) → Résolution (10s) → CTA (5s)
**Pour 60s :** Hook (3s) → Tension (20s) → Mécanisme (20s) → Preuve (10s) → CTA (7s)

---

## Phase 2 : Séquencer les Scènes

Pour chaque scène, définir :

| Champ | Contenu |
|---|---|
| Durée | En secondes |
| Visuel | Ce qu'on voit à l'écran |
| Audio | Voix off / dialogue / son ambiance / silence |
| Texte overlay | Texte affiché à l'écran (si applicable) |
| Émotion cible | Ce que le spectateur doit ressentir |
| Note de montage | Rythme, transition, effet |

---

## Phase 3 : Écrire le Brief Technique

```markdown
## Brief Vidéo — [Marque] — [Creative ID] — [Date]

### Contexte
Objectif : [Ce que la vidéo doit produire]
Persona ciblé : [Prénom fictif + awareness stage]
Ton : [Naturel UGC / Professionnel / Éducatif / Émotion]
Plateforme principale : [Meta Feed / Reels / Stories]

### Specs
Durée : [Xs]
Ratio : [9:16 / 4:5]
Son : [Voix on / Voix off / Silent]
Sous-titres : [Oui / Non — style si oui]

### Assets Disponibles
- [Liste des éléments fournis]
- [Éléments à trouver / filmer]

### Structure Scène par Scène

**Scène 1 — Hook [0–3s]**
Visuel : [Description]
Audio : [Voix / Son]
Texte overlay : "[Texte]"
Émotion : [Ce qu'on doit ressentir]
Note : [Instructions montage]

**Scène 2 — [Nom] [3–Xs]**
[Même structure]

[...]

**Scène finale — CTA [X–fin]**
Visuel : [Produit / CTA visuel]
Audio : "[Voix off CTA]"
Texte overlay : "[CTA exact]"

### Contraintes
[Compliance, visuels interdits, claims à éviter]

### Références
[Liens vers creatives de référence dans le même style]
```

---

## Related Skills

- `03-strategy/creative-brief` — prérequis
- `03-strategy/hook-writing` — hook sélectionné = première scène
- `04-production/ai-video-production` — alternative IA pour le même brief
- `04-production/campaign-setup` — après production
- `05-analysis/ad-analysis` — après diffusion
