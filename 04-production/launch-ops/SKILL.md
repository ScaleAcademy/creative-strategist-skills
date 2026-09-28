---
name: launch-ops
description: "The traffic-manager operational chain that wraps a Meta launch end to end: takes freshly exported videos (often mis-named), identifies them by CONTENT, renames them to convention, builds the UTM manifest, runs a preflight quality-check report, hands the actual upload to meta-launch (everything PAUSED), then produces a post-upload verification report for the person who activates. Four phases: A Export→Naming→UTM · B Pre-Upload Check · C Upload (via meta-launch) · D Post-Upload Check. Use it as the wrapper around a launch, from raw exports to an activation-ready handoff. Trigger on: 'j'ai exporté les vidéos', 'nomme les exports', 'fais-moi les UTM', 'prépare l'upload Meta', 'vérifie avant d'uploader', 'preflight', 'checklist avant upload', 'on lance les ads', 'rapport post upload', 'rapport des ads lancées', 'document de vérification pour activer'. Produit: fichiers renommés + [ID]_UTM-manifest.md + rapport preflight + [ID]_post-upload-report.md."
metadata:
  version: 1.1.0
  status: beta
  tags: [production, launch, ops, naming, utm, preflight, meta-ads, verification, handoff, mcp]
  inputs: [dossier d'export Premiere (.mp4), contexte client/batch/concept, format UTM du client, destination(s), structure ad set voulue, compte Meta]
  outputs: [vidéos renommées, manifeste UTM ([ID]_UTM-manifest.md), rapport-tableau preflight, ads créées PAUSED (via meta-launch), rapport post-upload ([ID]_post-upload-report.md)]
  notion-reads: [db-concepts.md, db-briefs.md, db-personas.md, db-clients.md]
  depends-on: [meta-launch, campaign-setup, ffmpeg/ffprobe, MCP Facebook, MCP Notion]
---

# Launch Ops

Le **maillon opérationnel « traffic manager »** autour d'un lancement Meta. Il ne remplace pas
`meta-launch` (qui possède ses propres garde-fous de création) — il **l'encadre** : préparer les
exports proprement en amont, vérifier avant d'appuyer, déléguer l'upload à `meta-launch`, puis
produire la trace de passation en aval.

```
A. Export → Naming → UTM    B. Pre-Upload Check     C. Upload (meta-launch)    D. Post-Upload Check
(lire le contenu,       →   (preflight ✅/⚠️/❌,  →  (créer les ads          →  (rapport de passation
 renommer, manifeste UTM)    rien ne part au ❌)      TOUTES en PAUSED)          + checklist valideur)
```

> **Principe central** : on identifie chaque vidéo par son **contenu visuel**, jamais par son nom
> de fichier (les exports Premiere sortent souvent avec le template non rempli
> `Client - Batch - Concept Name - ... - Variation_1_2.mp4`, ou un nom résiduel d'un autre projet).
> **Rien ne s'active** : les phases A→D préparent et vérifient ; l'activation reste une décision
> humaine, ad par ad, après lecture du rapport D.

---

## Before Starting

Confirmer avant de démarrer :

- [ ] Chemin du **dossier d'export** (convention : `04 - Production/01 - Ad/[BATCH]/_export/[AAMMJJ]/`)
- [ ] **Client · Batch · Concept** (ID Concept, ID Brief) — sinon les récupérer dans Notion
- [ ] **Format UTM de base** du client (ex : `utm_source=facebook&utm_medium=cpc&utm_campaign={{campaign.name}}_{{adset.name}}&utm_content={{ad.name}}`)
- [ ] **Destination(s) confirmée(s) avec le client** — URL par type de landing (quiz / vsl / …). **Ne jamais déduire la destination de la durée.**
- [ ] Accès **Notion** pour les codes taxonomie (concept, angle, persona, style, awareness)
- [ ] Structure ad set voulue + compte Meta (pour les phases C/D)

Input manquant = on s'arrête et on demande. Jamais « je mets quelque chose de raisonnable » sur un compte pub live.

---

## Phase A — Export → Naming → UTM

Transforme le dossier d'exports bruts en lot **nommé + taggé UTM + rangé**.

### A.1 Scanner le dossier
```bash
find "$DIR" -maxdepth 1 -type f -iname "*.mp4" | sort | while IFS= read -r f; do
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  printf "%-70s %ss\n" "$(basename "$f")" "${dur%.*}"
done
```
Noter le **nombre attendu** (ex : 2 scènes × 2 variantes × 3 titres = 12) et comparer.

### A.2 Écarter les anomalies AVANT de nommer
- **Intrus** (autre client/projet) → `mkdir _hors-sujet` et l'y déplacer. Ne jamais le taguer avec ce client.
- **Exports ratés** (durée anormale : 6 min au lieu de 2, doublons) → suffixer `_360s-RAW` et signaler à l'humain. Ne pas deviner.
> ⚠️ Si le contenu contredit le nom (nom = client A, image = client B), **le contenu fait foi** — le surface, ne procède pas à l'aveugle.

### A.3 Lire le CONTENU (identification visuelle)
Extraire une frame vers 2 s (le titre à l'écran y est), redimensionnée pour lecture rapide :
```bash
ffmpeg -y -ss 2 -i "$f" -frames:v 1 -vf scale=380:-1 "frame.jpg"
```
Pour chaque vidéo : **scène/décor** · **titre à l'écran** (hook texte) · **variante** (montage/perso) · **personnage**. Croiser les frames pour dédupliquer les similaires.

### A.4 Récupérer les codes taxonomie dans Notion
Via MCP Notion sur les DBs Creative OS : **Concept / Brief** · **Style** (⚠️ le code de la 🎨 Styles Library Notion, PAS celui du fichier Excel — Pixar = `S701`) · **Angle** · **Persona** · **Awareness** · **Funnel**. Voir `references/nomenclature-and-utm.md`.

### A.5 Nommer (le nom de fichier EST le nom d'ad = `utm_content`)
```
[CODE]-[W##]_[hook]_[variante]_[titre].mp4
ex : YU06-W39_cafe_sarah-machine_t1-grignotage-emotionnel.mp4
```
`hook` = la scène · `variante` = décor/perso distinctif · `titre` = hook texte (t1/t2/t3 + libellé court).
Renommer par `mv`, **jamais écraser une version** — si refonte, archiver l'ancienne (dossier `_remplaces/`, suffixe explicatif type `_135s-coupures`).

### A.6 Générer le manifeste UTM
`[ID]_UTM-manifest.md` : tableau (vidéo · hook · perso · variante · titre · durée) + **une URL taguée par vidéo**.
`URL = [DESTINATION]?[UTM_BASE]&[SLUGS_PERSO]` — slugs : `utm_concept · utm_brief · utm_angle · utm_anglecat · utm_persona · utm_awareness · utm_funnel · utm_style · utm_creatype · utm_hook · utm_talent · utm_variant · utm_ffmsg · utm_len · utm_lp · utm_page`. Générer par script (`references/gen-manifest.py`).

### A.7 Faire avancer le pipeline
`04 - Production/.../_export/` → `05 - Upload/01 - À faire/[ID] - [Nom]/` (prêt) → après upload → `05 - Upload/02 - Terminé/AAAA-MM-JJ - [ID] - [Nom]/` (préfixe = **date d'upload** ISO).

---

## Phase B — Pre-Upload Check (preflight traffic manager)

On ne se fie pas à « ça a l'air bon ». On déroule une checklist et on rend un **rapport-tableau**.
On va chercher chaque info **une par une** — jamais supposer. **Rien ne s'uploade tant qu'une ligne est ❌** ; les ⚠️ demandent une validation humaine.

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
| 8 | Destination **confirmée avec le client** (quiz/vsl…) | | pas déduite de la durée |
| 9 | `utm_lp` / `utm_page` cohérents avec la destination | | |
| 10 | IDs présents : concept · brief · angle · persona | | filtrables |
| 11 | `utm_style` = code **Notion** (Pixar = s701) | | pas le code Excel |
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
| 20 | Vidéos uploadées sur Meta (video_id) OU plan d'upload | | |
| 21 | Statut **PAUSED** par défaut | | jamais ACTIVE sans validation |

*(Adapter le nombre de lignes au contexte — viser 12-15 pertinentes minimum.)*
Tout ✅ (ou ⚠️ validés par l'humain) → feu vert pour la Phase C.

---

## Phase C — Upload (création sur Meta, via meta-launch)

**C'est ici que ça part sur Meta.** On ne réimplémente pas la création : on **délègue à `meta-launch`**,
qui possède les garde-fous durs (plan validé avant tout appel API, tout créé **PAUSED**, règles
URL/UTM/creative, diff post-publication anti-mutations Meta).

Ce que Launch Ops fournit à `meta-launch` :
- le **lot nommé** (chaque nom de fichier = nom d'ad = `utm_content`),
- le **manifeste UTM** (URL taguée par ad, UTMs → champ *URL Parameters*, jamais collés dans le lien),
- la **structure ad set** validée en Phase B (nomenclature sans `#`, mix entre parenthèses, répartition A/B),
- les **défauts client** (langue ad set, page, pixel/événement, `multi_advertiser_ads` OPT_OUT, Display Link = domaine racine).

Rappels non-négociables (détaillés dans `meta-launch`) :
- **Tout en PAUSED** — campagne, ad set ET ad. L'activation est une décision humaine séparée.
- **UTMs dans *URL Parameters***, pas dans l'URL du lien.
- **Ad URL = l'URL du test A/B** quand un test landing tourne (pas la page en direct).
- Si un `video_id` change (ré-export d'un clip), **swapper la vidéo dans l'ad concernée** — le renommage local ne se propage pas seul sur Meta.

> Pas de MCP Facebook dispo ? → produire le plan de lancement en checklist manuelle, sans écrire sur le compte.

---

## Phase D — Post-Upload Check (rapport de passation)

Après création (en PAUSED), on ne dit pas « c'est bon, active ». On produit un **document de
passation** `[ID]_post-upload-report.md` — la personne qui active ouvre chaque ad, vérifie, coche, active.
C'est la trace « quelqu'un a checké ».

Le rapport contient :
1. **En-tête** : compte · campagne · date · statut (PAUSED) · total ads / ad sets.
2. **Config commune** : objectif, pixel/événement, ciblage, budget, titre, CTA, destination, texte.
3. **Par ad set** : tableau des ads → nom · statut · **lien d'aperçu Ads Manager**
   (`…/manage/ads/edit?act=<compte>&selected_ad_ids=<ad_id>`).
4. **Checklist du valideur** (cases à cocher) — au minimum :
   - [ ] La bonne vidéo sur chaque ad (surtout après un ré-export : le bon `video_id`)
   - [ ] Titre correct · Texte principal correct · CTA correct
   - [ ] Le lien mène à la bonne destination (quiz / vsl / …)
   - [ ] Les UTM se remplissent (`utm_content = {{ad.name}}`)
   - [ ] Ciblage + budget conformes
   - [ ] Pas de doublon / pas d'intrus
   - [ ] Pièges Meta : WhatsApp non coché, budget non auto-ajusté, pas d'ads auto-ajoutées

**Tant qu'une case est vide → rester en PAUSED.** Le rapport est **transmissible** (collègue, client) :
c'est le point de passation « traffic manager → activateur ». Format `.md`, exportable PDF pour l'envoi.

---

## Hard Rules (à ne jamais violer)

1. **Le contenu prime sur le nom de fichier** — toujours lire les vidéos (frame @2s).
2. **Destination = un CHOIX confirmé avec le client**, jamais déduit de la durée. Détermine `utm_lp` / `utm_page`.
3. **Style = code de la 🎨 Styles Library Notion** (Pixar = S701), pas le code du fichier Excel taxonomie.
4. **Jamais écraser une version** — archiver l'ancienne (`_remplaces/`).
5. **Dates en ISO** `AAAA-MM-JJ` dans les dossiers Terminé.
6. **Écarter intrus + ratés** avant de nommer, et les signaler.
7. **Rien ne s'uploade avec un ❌** en Phase B ; un ⚠️ = on montre et on attend le OK humain.
8. **Tout créé PAUSED** en Phase C ; l'activation est une décision humaine après lecture du rapport D.
9. **UTMs dans *URL Parameters*** ; **pas de `#`** dans les noms d'ad/ad set (casse l'UTM).

## Related Skills

- `04-production/meta-launch` — **la Phase C** : création guardrailée des entités Meta (ce skill l'appelle).
- `05-analysis/campaign-setup` — architecture / nomenclature / budgets / kill rules (définis là, exécutés ici).
- `03-strategy/creative-brief` — le brief validé que ce lancement exécute.
- `04-production/video-production` · `ai-video-production` · `static-production` — **amont** : d'où sortent les assets exportés que la Phase A ingère.

## References

### Propres à ce skill (dans `launch-ops/references/`)
- `references/nomenclature-and-utm.md` — nomenclature d'export détaillée + tous les slugs UTM + mapping Notion.
- `references/gen-manifest.py` — script de génération du manifeste UTM (à adapter par batch).
- Exemple réel de sortie : Yuman `YU-06 / _export/270926/` (`YU-06_UTM-manifest.md` + `YU-06_post-upload-report.md`).

### Utilisées ailleurs dans le repo (à ne PAS dupliquer — brancher dessus)
Ce skill s'appuie sur la connaissance déjà formalisée dans le repo. Les phases B/C notamment lisent :
- [`../../05-analysis/campaign-setup/references/meta-ads-parameters.md`](../../05-analysis/campaign-setup/references/meta-ads-parameters.md) — objectifs, ad set, ciblage, bidding, placements Meta (config de référence pour le preflight + l'upload).
- [`../../05-analysis/campaign-setup/references/kill-rules.md`](../../05-analysis/campaign-setup/references/kill-rules.md) — règles de coupure (à avoir en tête avant d'activer).
- [`../../references/naming-convention.md`](../../references/naming-convention.md) — nomenclature **campagne / ad set / ad** (complète la nomenclature *fichier* ci-dessus).
- [`../../references/notion-output-protocol.md`](../../references/notion-output-protocol.md) — protocole dual-mode (standalone ↔ connected Notion), partagé avec `meta-launch`.
- [`../../references/notion-db-schemas/`](../../references/notion-db-schemas/) — schémas des DBs Creative OS lues en Phase A (`db-concepts`, `db-briefs`, `db-personas`, `db-clients`).

> ⚠️ Sur `utm_style` : la source de vérité est la **🎨 Styles Library Notion** (Creative OS, où Pixar = `S701`).
> Le fichier repo `03-strategy/creative-brief/references/styles-library.md` est une **autre grille** (S101→S604,
> catégories Headline/Collage/Lifestyle…) — ne pas le confondre avec les codes Notion utilisés pour l'UTM.
