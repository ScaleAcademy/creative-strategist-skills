---
name: static-production
description: "Turns a validated creative brief into a Nano Banana image generation prompt and a structured designer brief. Use after creative-brief is validated and the format is static. Trigger on: 'produis une image', 'brief designer', 'static ad', 'prompt Nano Banana', 'créa statique'. Produces a ready-to-execute production package."
metadata:
  version: 1.0.0
  status: beta
  tags: [production, static, design, prompt, image]
  inputs: [creative-brief validé, hook sélectionné (hook-writing)]
  outputs: [prompt Nano Banana + brief designer structuré]
  depends-on: [creative-brief, hook-writing]
---

# Static Production

## Before Starting

Confirme avant de commencer :
- [ ] Brief créatif validé
- [ ] Hook sélectionné (top 1–3 du hook bank)
- [ ] Format défini : ratio (9:16 / 4:5 / 1:1), usage (Feed / Story / Reels cover)
- [ ] Style visuel défini ou à choisir (voir référence styles)
- [ ] Accès à Nano Banana ou outil image disponible

---

## Phase 1 : Définir la Structure Visuelle

Un bon statique a 3 zones :

**Zone 1 — Hook visuel (60% de l'attention)**
Ce que l'œil voit en premier. Doit stopper le scroll sans texte.
→ Visage / émotion / situation reconnaissable / contraste fort / premier frame choquant

**Zone 2 — Texte (headline + sous-titre)**
Maximum 7 mots en headline. Lisible en 1 seconde à vitesse de scroll.
→ Le hook textuel va ici — version courte du hook sélectionné

**Zone 3 — CTA + Logo**
Sobre. Ne pas surcharger. Le CTA doit être clair mais pas agressif.

---

## Phase 2 : Écrire le Prompt Nano Banana

Structure d'un prompt Nano Banana efficace :

```
[Sujet principal] [Action ou état] [Contexte / Setting] [Style visuel] [Émotion / Ambiance] [Ratio] [Contraintes]
```

**Variables à remplir depuis le brief :**
- Sujet : persona ou représentation du résultat
- Contexte : micro-moment du persona (Layer 3)
- Style : adapté à l'angle (UGC = naturel ; autorité = propre ; identité = aspirationnel)
- Émotion : alignée avec l'émotion dominante du persona

**Ce qu'un bon prompt évite :**
- Trop de détails concurrents (1 sujet principal max)
- Style incohérent avec le ton de la marque
- Texte intégré dans l'image (à ajouter en post-production)

---

## Phase 3 : Écrire le Brief Designer

Pour les assets produits par un designer humain :

```markdown
## Brief Designer — [Marque] — [Creative ID] — [Date]

### Format
Ratio : [9:16 / 4:5 / 1:1]
Dimensions : [px]
Usage : [Feed / Story / Cover]

### Concept
[Description en 2–3 phrases de ce que doit transmettre la creative]

### Zone 1 — Visuel Principal
[Description précise : sujet, position, émotion, contexte]

### Zone 2 — Texte
Headline : "[Texte exact — max 7 mots]"
Sous-titre : "[Texte exact — max 15 mots]" (optionnel)

### Zone 3 — CTA + Logo
CTA : "[Texte exact]"
Position logo : [Haut gauche / Haut droit / Bas]

### Style Visuel
[S-code ou description : couleurs, typographie, mood]

### Contraintes
[Compliance, éléments interdits, couleurs à éviter]

### Références
[Lien vers creative de référence ou moodboard si disponible]
```

---

## Related Skills

- `03-strategy/creative-brief` — prérequis
- `03-strategy/hook-writing` — le hook sélectionné devient le texte principal
- `04-production/campaign-setup` — après production, setup campagne
- `05-analysis/ad-analysis` — après diffusion
