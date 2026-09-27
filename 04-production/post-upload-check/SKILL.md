---
name: post-upload-check
description: "Après la création des ads sur Meta (en PAUSED), génère un RAPPORT DE VÉRIFICATION (.md, exportable PDF) destiné à la personne qui va activer. Liste toutes les ads créées, leurs liens d'aperçu Ads Manager, la config, et une checklist de validation à cocher. Rien ne s'active tant que tout n'est pas coché. Trigger on: 'rapport post upload', 'rapport des ads lancées', 'document de vérification', 'preview PDF pour valider', 'récap des ads créées', 'post-upload check'. Produit: [ID]_post-upload-report.md."
metadata:
  version: 1.0.0
  status: beta
  tags: [meta, ads, report, verification, post-launch, handoff]
  inputs: [ads créées via meta-launch (ad_ids, ad set ids, campagne), config commune]
  outputs: [rapport de vérification .md avec liens d'aperçu + checklist valideur]
  depends-on: [meta-launch, MCP Facebook]
---

# Post-Upload Check (Rapport de vérification)

Après `meta-launch` (ads créées en **PAUSED**), on ne dit pas « c'est bon, active ». On produit un **document de passation** : un rapport où la personne qui active ouvre chaque ad, vérifie, coche, puis active. C'est la trace « quelqu'un a checké ».

## Ce que le rapport contient
1. **En-tête** : compte · campagne · date · statut (PAUSED) · total ads / ad sets.
2. **Config commune** : objectif, pixel/événement, ciblage, budget, titre, CTA, destination, texte.
3. **Par ad set** : tableau des ads → nom · statut · **lien d'aperçu Ads Manager** (`…/manage/ads/edit?act=<compte>&selected_ad_ids=<ad_id>`).
4. **Checklist du valideur** (cases à cocher) — au minimum :
   - [ ] La bonne vidéo sur chaque ad
   - [ ] Titre correct
   - [ ] Texte principal correct
   - [ ] CTA correct
   - [ ] Le lien mène à la bonne destination (quiz / vsl / …)
   - [ ] Les UTM se remplissent (`utm_content = {{ad.name}}`)
   - [ ] Ciblage + budget conformes
   - [ ] Pas de doublon / pas d'intrus
   - [ ] Pièges Meta : WhatsApp non coché, budget non auto-ajusté, pas d'ads auto-ajoutées

## Règle
- **Tant qu'une case est vide → rester en PAUSED.** Activation seulement quand tout est coché.
- Le rapport est **transmissible** (un collègue, un client) — c'est le point de passation « traffic manager → activateur ».
- Format `.md` par défaut ; exportable en PDF pour l'envoi.

## Génération
Récupérer les `ad_id` / ad set / campagne renvoyés par `meta-launch`, puis assembler le tableau + la checklist (script simple, cf. exemple réel `Yuman YU-06 / _export/270926/YU-06_post-upload-report.md`).

## Place dans le pipeline
`export-naming-utm` (nommer + UTM) → `pre-upload-check` (preflight) → `meta-launch` (créer en PAUSED) → **`post-upload-check`** (rapport de passation) → *humain vérifie & active*.
