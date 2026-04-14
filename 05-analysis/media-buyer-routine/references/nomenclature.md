# RÉFÉRENCE — Nomenclature Meta Ads
**Version :** 1.0 — À retravailler  
**Agence :** GoScale (code : GS)  
**Usage :** Consulté par SKILL_media_buyer.md + agent de vérification nomenclature

> ⚠️ Document de travail — structure validée, séparateurs et détails à affiner.

---

## Structure générale

```
CAMPAGNE  →  GS - 01 - P1 - LEADS
AD SET    →  001 - PA - A1 - C1-01 - W14
AD        →  001 - A1 - S300 - VID - 30s - CTRL - 0414
```

---

## Niveau Campagne

```
GS - [NUM] - [PHASE] - [OBJECTIF]

Éléments :
- GS       → ID agence GoScale (fixe)
- NUM      → ordre chronologique (01, 02, 03...)
- PHASE    → P1 / P2 / P3 / P4
- OBJECTIF → LEADS / TRAFFIC / SCALE
```

**Exemples :**
```
GS - 01 - P1 - LEADS
GS - 02 - P2 - LEADS
GS - 03 - P3 - LEADS
GS - 04 - P4 - SCALE
```

---

## Niveau Ad Set

```
[NUM] - [AWARENESS] - [PERSONA] - [ANGLE] - [SEMAINE]

Éléments :
- NUM       → ordre chronologique (001, 002, 003...)
- AWARENESS → UN / PA / SA / MA / BA
- PERSONA   → A1 / A2 / A3 / A4 (définis dans le dossier client)
- ANGLE     → C1-01 / C1-05 / C3-08... (catégorie + concept)
- SEMAINE   → W01 / W02... / W52
```

**Exemples :**
```
001 - PA - A1 - C1-01 - W14
002 - UN - A2 - C3-08 - W14
003 - SA - A1 - C2-04 - W15
```

---

## Niveau Ad

```
[NUM] - [PERSONA] - [STYLE] - [FORMAT] - [LONGUEUR] - [TYPE] - [DATE]

Éléments :
- NUM      → ordre chronologique (001, 002, 003...)
- PERSONA  → A1 / A2 / A3 / A4
- STYLE    → S100 / S200 / S300 / S400
- FORMAT   → VID / IMG / GIF / CAR
- LONGUEUR → 15s / 30s / 60s / 90s / 120s (VID uniquement, omis pour IMG)
- TYPE     → CTRL (version de référence) / ITR (itération)
- DATE     → MMJJ (ex : 0414 = 14 avril)
```

**Exemples :**
```
001 - A1 - S300 - VID - 30s - CTRL - 0414
002 - A1 - S300 - VID - 30s - ITR - 0414
003 - A2 - S100 - IMG - CTRL - 0414
004 - A1 - S400 - VID - 60s - CTRL - 0421
```

---

## Codes de référence

### Awareness (niveaux de conscience)
| Code | Libellé |
|---|---|
| UN | Unaware |
| PA | Problem Aware |
| SA | Solution Aware |
| MA | Most Aware |
| BA | Brand Aware |

### Angles (catégories)
| Code | Libellé |
|---|---|
| C1 | Démonstration / Preuve (Logique × Aspiration) |
| C2 | Éducatif (Logique × Problème) |
| C3 | Douleur (Émotion × Problème) |
| C4 | Identité (Émotion × Aspiration) |

### Concepts par angle
| Code | Libellé | Catégorie |
|---|---|---|
| 01 | Avant / Après | C1 |
| 02 | Résultat Chiffré | C1 |
| 03 | Chiffres Transformés | C2 |
| 04 | Mécanisme Unique | C2 |
| 05 | Comparaison Directe | C1 |
| 06 | Témoignage Résultat | C1 |
| 07 | Question Rhétorique | C3 |
| 08 | Douleur Directe | C3 |
| 09 | Peur de Rater | C4 |
| 10 | Identité Aspirationnelle | C4 |

### Styles (S-codes)
| Code | Libellé |
|---|---|
| S100 | Statique |
| S200 | Carousel |
| S300 | Courte vidéo |
| S400 | Longue vidéo |

### Formats
| Code | Libellé |
|---|---|
| VID | Vidéo |
| IMG | Image statique |
| GIF | GIF / animation courte |
| CAR | Carousel |

### Types
| Code | Libellé |
|---|---|
| CTRL | Version de référence (original) |
| ITR | Itération (variation d'une CTRL) |

---

## Règles générales

- Le séparateur est le tiret ` - ` (tiret avec espaces)
- Les majuscules sont obligatoires sur tous les codes
- Le NUM est toujours sur 3 chiffres minimum (001, 002...)
- Le DATE est toujours sur 4 chiffres MMJJ (0414, 1203...)
- La longueur est omise pour les formats non-vidéo (IMG, CAR)
- Une itération (ITR) garde le même NUM que sa CTRL de référence + suffixe version si nécessaire

---

## À retravailler (v2)

- Valider le séparateur final (tiret avec espaces vs underscore)
- Ajouter les personas par client dans le dossier client
- Valider la liste complète des concepts (01→10+)
- Définir la gestion des hooks (H1/H2/H3) au niveau ad si nécessaire
- Intégrer la longueur audio (voiceover / music / none)
