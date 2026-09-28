# Référence — Nomenclature & UTM

## 1. Convention de nommage des exports

```
[CODE]-[SEMAINE]_[hook]_[variante]_[titre].mp4
```

| Segment | Rôle | Exemples |
|---|---|---|
| `CODE` | code batch/concept court | `YU06` |
| `SEMAINE` | semaine de prod | `W39` |
| `hook` | la scène / le hook visuel | `reunion`, `cafe` |
| `variante` | décor ou perso distinctif | `sarah-machine`, `sarah-couloir`, `tailleur-porte` |
| `titre` | le hook texte à l'écran | `t1-grignotage-emotionnel`, `t2-stressee`, `t3-manger` |

> Le nom de fichier **est** le nom d'ad Meta (= `utm_content` dynamique). Il doit rester lisible.

Cas particuliers :
- Export raté (durée anormale) → suffixe `_360s-RAW` en attente de relecture humaine.
- Intrus (autre client) → dossier `_hors-sujet/`.

## 2. UTM — structure

`URL_FINALE = DESTINATION ? UTM_BASE & SLUGS_PERSO`

### UTM de base (variables dynamiques Meta — définies par le client)
```
utm_source=facebook&utm_medium=cpc&utm_campaign={{campaign.name}}_{{adset.name}}&utm_content={{ad.name}}
```
*(Certains clients utilisent la version longue `{{site_source_name}}` + `{{placement}}` + `{{platform}}` — reprendre le format fourni par le client.)*

### Slugs perso (la taxonomie créative)
| Slug | Source | Exemple |
|---|---|---|
| `utm_concept` | DB Concepts Notion | `yu-15` |
| `utm_brief` | DB Briefs Notion | `yu-15-b2` |
| `utm_angle` / `utm_anglecat` | DB Angles | `c3-03` / `c3` |
| `utm_persona` | DB Personas | `p1` |
| `utm_awareness` | Awareness | `pa` (Problem Aware) |
| `utm_funnel` | Funnel | `tofu` |
| `utm_style` | **🎨 Styles Library Notion** | `s701` (Pixar) |
| `utm_creatype` | type de créa | `iteration` / `imitation` / `ideation` |
| `utm_hook` | scène | `cafe` / `reunion` |
| `utm_talent` | perso à l'écran | `sarah` / `tailleur` |
| `utm_variant` | variante | `machine` / `couloir` / `dossiers` / `porte` |
| `utm_ffmsg` | first-frame message (titre) | `t1-grignotage` |
| `utm_len` | durée | `148s` / `135s` |
| `utm_lp` / `utm_page` | landing / page | `vsl` / `page-b` · `quiz` / `page-a` |

## 3. Règle type de créa (exemple Yuman)
- **long ⇒ VSL** → `utm_lp=vsl`, `utm_page=page-b`, destination masterclass.
- **short ⇒ Quiz** → `utm_lp=quiz`, `utm_page=page-a`, destination quiz-optin.
> Le type se déduit de la **durée**, pas du nom de fichier.

## 4. ⚠️ Deux référentiels de codes STYLE (ne pas confondre)
- **Fichier Excel** `assets/Modele_Taxonomie_Creative.xlsx` : `S701 = UGC natif selfie`, `S808 = Vidéo 100% IA`.
- **🎨 Styles Library Notion** (Creative OS) : `S701 = Pixar`, `S702 = Cartoon`, `S703 = Flat 2D`, `S704 = Claymation`, `S705 = Plush/Toy`…
→ Pour l'UTM `utm_style`, utiliser **le code Notion** (celui que le client reconnaît).

## 5. Pipeline dossiers
```
04 - Production/01 - Ad/[BATCH]/_export/[AAMMJJ]/   ← exports Premiere bruts (on nomme ici)
05 - Upload/01 - À faire/[ID] - [Nom]/              ← prêt à uploader (+ manifeste UTM)
05 - Upload/02 - Terminé/AAAA-MM-JJ - [ID] - [Nom]/ ← uploadé (préfixe = date d'upload)
```
