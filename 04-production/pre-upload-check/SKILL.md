---
name: pre-upload-check
description: "Contrôle qualité 'traffic manager' AVANT d'uploader/créer des ads sur Meta. Déroule ~15 vérifications (fichiers, nommage, UTM, copy, ad set, technique), va chercher chaque info une par une, et produit un RAPPORT-TABLEAU (✅/⚠️/❌ + détail). Rien ne part tant que tout n'est pas au vert (ou que l'humain a validé les ⚠️). Trigger on: 'vérifie avant d'uploader', 'checklist avant upload', 'preflight', 'contrôle avant de créer les ads', 'est-ce que tout est clean', 'rapport de vérification'. Produit: un tableau de contrôle prêt à valider."
metadata:
  version: 1.0.0
  status: beta
  tags: [meta, ads, quality-check, preflight, traffic-manager, upload]
  inputs: [lot de vidéos nommées + manifeste UTM, structure ad set voulue, compte Meta]
  outputs: [rapport-tableau de vérification (✅/⚠️/❌)]
  depends-on: [export-naming-utm, MCP Facebook, MCP Notion]
---

# Pre-Upload Check (Traffic Manager Preflight)

Avant d'uploader des vidéos ou de créer des ads sur Meta, on ne se fie pas à « ça a l'air bon ». On déroule une **checklist de traffic manager** et on produit un **rapport-tableau** où chaque ligne est explicitement vérifiée. **Rien ne s'uploade tant qu'une ligne est ❌** ; les ⚠️ demandent une validation humaine.

## Comment ça marche
1. Aller chercher chaque info **une par une** (fichiers, manifeste, Notion, compte Meta) — ne jamais supposer.
2. Cocher chaque ligne : **✅ OK** · **⚠️ à confirmer** · **❌ bloquant**.
3. Rendre le tableau. Si tout est ✅ (ou ⚠️ validés) → feu vert pour `meta-launch`.

## Le rapport-tableau (modèle)

| # | Vérification | Statut | Détail |
|---|---|---|---|
| **— Fichiers & nommage —** | | | |
| 1 | Nombre de vidéos = matrice attendue (ex 2×2×3=12) | | compter vs plan |
| 2 | Aucun intrus (autre client/projet) | | contenu lu, pas le nom |
| 3 | Aucun export raté / doublon (durée anormale) | | ffprobe |
| 4 | Toutes nommées selon la nomenclature | | `CODE-W##_hook_variante_titre` |
| 5 | Aucun `#` ni caractère qui casse l'UTM | | hashtags interdits |
| **— UTM —** | | | |
| 6 | Manifeste généré, 1 URL par vidéo | | `[ID]_UTM-manifest.md` |
| 7 | `utm_content = {{ad.name}}` (nom d'ad = nom fichier) | | |
| 8 | Destination **confirmée avec le client** (quiz/vsl…) | | ne pas déduire de la durée |
| 9 | `utm_lp` / `utm_page` cohérents avec la destination | | |
| 10 | IDs présents : concept · brief · angle · persona | | filtrables |
| 11 | `utm_style` = code **Notion** (ex Pixar = s701) | | pas le code Excel |
| **— Copy —** | | | |
| 12 | Texte principal = repris de l'ad qui tourne | | pas 50 variantes |
| 13 | **Titre (headline) rempli** | | |
| 14 | **Description = vide** (volontaire) | | |
| 15 | CTA défini (ex En savoir plus / LEARN_MORE) | | |
| **— Ad set & structure —** | | | |
| 16 | Nomenclature ad set validée (IDs, sans #, mix entre parenthèses) | | |
| 17 | Répartition A/B correcte (quel ad dans quel ad set) | | |
| 18 | Ciblage + budget clonés du dernier ad set publié | | |
| 19 | Pixel + événement corrects (ex LEAD) | | |
| **— Technique —** | | | |
| 20 | Vidéos uploadées sur Meta (video_id dispo) OU plan d'upload | | |
| 21 | Statut **PAUSED** par défaut | | jamais ACTIVE sans validation |

*(Adapter le nombre de lignes au contexte — viser 12-15 pertinentes minimum.)*

## Règles
- **Le contenu prime sur le nom** (relire les vidéos si doute — cf `export-naming-utm`).
- **Ne jamais uploader avec un ❌.** Un ⚠️ = on montre le point et on attend le OK humain.
- **PAUSED par défaut**, l'humain active après revue dans Ads Manager.
- Pièges Meta à re-vérifier au lancement : WhatsApp auto-coché, budget auto-ajusté, ads auto-ajoutées.

## Enchaînement
`export-naming-utm` (nommer + UTM) → **`pre-upload-check`** (ce skill) → `meta-launch` (créer les ads en PAUSED via MCP).
