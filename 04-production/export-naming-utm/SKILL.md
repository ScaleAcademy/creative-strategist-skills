---
name: export-naming-utm
description: "Prend un lot de vidéos fraîchement exportées de Premiere Pro (souvent mal nommées), les analyse par leur CONTENU (pas leur nom), les renomme selon la nomenclature du client, génère un manifeste UTM prêt pour Meta, et les fait avancer dans le pipeline Production → Upload → Terminé. Trigger on: 'j'ai exporté les vidéos', 'nomme les exports', 'fais-moi les UTM', 'range les exports', 'prépare l'upload Meta', 'scanne le dossier export'. Produit: fichiers renommés + [ID]_UTM-manifest.md."
metadata:
  version: 1.0.0
  status: beta
  tags: [production, post-export, naming, utm, meta, pipeline]
  inputs: [dossier d'export Premiere avec .mp4, contexte client/batch/concept, accès Notion (codes taxonomie), format UTM de base du client]
  outputs: [vidéos renommées selon nomenclature, manifeste UTM avec URLs taguées, fichiers déplacés vers 05 - Upload]
  depends-on: [ffmpeg/ffprobe, MCP Notion (Styles Library / Concepts / Angles)]
---

# Export → Naming → UTM

Transforme un dossier d'exports Premiere bruts en lot **nommé + taggé UTM + rangé**, prêt à uploader sur Meta. Le principe central : **on identifie chaque vidéo par son contenu visuel, jamais par son nom de fichier** (les exports Premiere sortent souvent avec le template de nommage non rempli — `Client - Batch - Concept Name - ... - Variation_1_2.mp4` — ou des noms résiduels d'un autre projet).

## Before Starting

Confirm before starting:
- [ ] Chemin du **dossier d'export** (convention : `04 - Production/01 - Ad/[BATCH]/_export/[AAMMJJ]/`)
- [ ] **Client · Batch · Concept** (ID Concept, ID Brief) — sinon les récupérer dans Notion
- [ ] **Format UTM de base** du client (ex : `utm_source=facebook&utm_medium=cpc&utm_campaign={{campaign.name}}_{{adset.name}}&utm_content={{ad.name}}`)
- [ ] **Destination(s)** (URL par type de landing : quiz / vsl / …)
- [ ] Accès **Notion** pour les codes taxonomie (concept, angle, persona, style, awareness)

---

## Workflow

### 1. Scanner le dossier
```bash
find "$DIR" -maxdepth 1 -type f -iname "*.mp4" | sort | while IFS= read -r f; do
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  printf "%-70s %ss\n" "$(basename "$f")" "${dur%.*}"
done
```
Note le **nombre attendu** (ex : 2 scènes × 2 variantes × 3 titres = 12) et compare.

### 2. Écarter les anomalies AVANT de nommer
- **Intrus** (vidéo d'un autre client / projet) → `mkdir _hors-sujet` et l'y déplacer. Ne jamais la taguer avec ce client.
- **Exports ratés** (durée anormale : 6 min au lieu de 2 min, doublons) → suffixer `_360s-RAW` et signaler à l'utilisateur pour qu'il relise/ré-exporte. Ne pas deviner.
> ⚠️ Si le contenu contredit le nom du fichier (nom = client A, image = client B), **le contenu fait foi** — surface-le, ne procède pas à l'aveugle.

### 3. Lire le CONTENU (identification visuelle)
Extraire une frame vers 2 s (le titre/texte à l'écran est là), redimensionnée pour lecture rapide, puis la lire :
```bash
ffmpeg -y -ss 2 -i "$f" -frames:v 1 -vf scale=380:-1 "frame.jpg"
```
Pour chaque vidéo, identifier : **scène/décor** (ex machine à café / salle de réunion), **titre à l'écran** (le hook texte), **variante** (montage/perso), **personnage**. Croiser les frames pour dédupliquer les similaires.

### 4. Récupérer les codes taxonomie dans Notion
Via MCP Notion (`notion-search`) sur les DBs Creative OS :
- **Concept / Brief** (DB Concepts / Briefs) — ex `YU-15` / `YU-15-B2`.
- **Style** (🎨 Styles Library) — ⚠️ **le code Notion, pas celui du fichier Excel** (ex Pixar = `S701` dans la Styles Library Notion).
- **Angle** (DB Angles), **Persona**, **Awareness**, **Funnel**.
> Voir `references/nomenclature-and-utm.md` pour le mapping complet des slugs.

### 5. Établir la matrice + nommer
Nom = **le nom d'ad** = `utm_content` dynamique. Il doit être lisible ET encoder les dimensions :
```
[CODE]-[W##]_[hook]_[variante]_[titre].mp4
ex : YU06-W39_cafe_sarah-machine_t1-grignotage-emotionnel.mp4
```
- `hook` = la scène (reunion / cafe / …)
- `variante` = le décor/perso distinctif (machine / couloir / dossiers / …)
- `titre` = le hook texte (t1 / t2 / t3 + libellé court)
Renommer par `mv`, jamais écraser une version — si refonte, garder l'ancienne (suffixe / archive).

### 6. Générer le manifeste UTM
`[ID]_UTM-manifest.md` : tableau (vidéo · hook · perso · variante · titre · durée) + **une URL taguée par vidéo**.
URL = `[DESTINATION]?[UTM_BASE]&[SLUGS_PERSO]` où :
- **UTM_BASE** = le format du client (source/medium/campaign/content).
- **SLUGS_PERSO** = `utm_concept · utm_brief · utm_angle · utm_anglecat · utm_persona · utm_awareness · utm_funnel · utm_style · utm_creatype · utm_hook · utm_talent · utm_variant · utm_ffmsg · utm_len · utm_lp`.
Générer par script (voir `references/gen-manifest.py`).

### 7. Faire avancer le pipeline
- Depuis `04 - Production/.../\_export/` → déplacer vers `05 - Upload/01 - À faire/[ID] - [Nom]/` quand prêt à uploader.
- Après upload Meta effectué → déplacer vers `05 - Upload/02 - Terminé/AAAA-MM-JJ - [ID] - [Nom]/` (préfixe = **date d'upload**, format ISO, tri chronologique).

---

## Règles critiques (à ne jamais violer)
1. **Le contenu prime sur le nom de fichier** — toujours lire les vidéos.
2. **Type de créa par la DURÉE** (règle client, ex Yuman) : long = VSL / short = Quiz → détermine `utm_lp`, `utm_page` et la destination.
3. **Style = code de la Styles Library Notion** (Pixar = S701), pas le code du fichier Excel taxonomie (référentiels distincts).
4. **Ne jamais écraser une version** — ajouter/archiver.
5. **Dates en ISO** `AAAA-MM-JJ` dans les noms de dossiers Terminé.
6. **Écarter intrus + ratés** avant de nommer, et les signaler.
7. **PAUSED / vérif humaine** : le skill prépare, l'humain uploade et vérifie.

## Références
- `references/nomenclature-and-utm.md` — nomenclature détaillée + tous les slugs UTM + mapping Notion.
- `references/gen-manifest.py` — script de génération du manifeste (à adapter par batch).
- Exemple réel de sortie : Yuman `YU-06 / _export/270926/YU-06_UTM-manifest.md`.
