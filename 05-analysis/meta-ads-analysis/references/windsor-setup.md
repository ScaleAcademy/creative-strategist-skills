# Windsor.ai — Setup MCP + Convention de Nommage

## Qu'est-ce que Windsor.ai ?

Windsor.ai est un agrégateur de données marketing qui connecte directement Meta Ads (et d'autres plateformes) à Claude via le protocole MCP (Model Context Protocol). Il permet à Claude d'interroger en temps réel les données de performance sans export manuel.

**Résultat :** Claude peut analyser ton compte Meta Ads comme un analyste qui a accès direct à l'interface — sans copier-coller de données.

---

## Section 1 : Connexion Windsor.ai MCP à Claude

### Étape 1 — Créer un compte Windsor.ai

- Aller sur [windsor.ai](https://windsor.ai)
- Créer un compte (plan gratuit disponible avec limites)
- Connecter ton compte Meta Ads dans le dashboard Windsor.ai

### Étape 2 — Obtenir la clé API Windsor

Dans le dashboard Windsor.ai :
- Aller dans **Settings > API**
- Copier la clé API (format : `wai_xxxxxxxxxxxx`)

### Étape 3 — Configurer Claude Desktop

Ouvrir le fichier de configuration Claude Desktop :
- **Mac :** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows :** `%APPDATA%\Claude\claude_desktop_config.json`

Ajouter la configuration MCP :

```json
{
  "mcpServers": {
    "windsor": {
      "command": "npx",
      "args": ["-y", "@windsor-ai/mcp-server"],
      "env": {
        "WINDSOR_API_KEY": "wai_VOTRE_CLE_API_ICI"
      }
    }
  }
}
```

### Étape 4 — Redémarrer Claude Desktop

Fermer complètement et relancer Claude Desktop.
Un icône Windsor devrait apparaître dans la barre d'outils.

**Test de connexion :**
```
Liste les comptes Meta Ads disponibles via Windsor.ai
```

Si Claude liste tes comptes → connexion réussie.

---

## Section 2 : Convention de Nommage

La convention de nommage est **optionnelle mais fortement recommandée**. Elle permet à Claude d'analyser les performances par angle, format, et mécanique directement depuis les noms de campagnes/adsets/creatives — sans avoir à catégoriser manuellement.

### Structure du Nom

```
[MARQUE]_[OBJECTIF]_[ANGLE]_[FORMAT]_[MECHANIQUE]_[VERSION]_[DATE]
```

### Codes par Segment

#### Objectif
| Code | Signification |
|---|---|
| ACQ | Acquisition / Prospection froide |
| LEA | Lead Generation |
| RET | Retargeting |
| AWA | Awareness |

#### Angle Créatif
| Code | Signification |
|---|---|
| PR | Problème (C1) |
| RS | Résultat / Preuve (C2) |
| ED | Éducation (C3) |
| ID | Identité (C4) |

#### Format
| Code | Signification |
|---|---|
| VID15 | Vidéo 15 secondes |
| VID30 | Vidéo 30 secondes |
| VID60 | Vidéo 60 secondes |
| STA | Statique (image) |
| CAR | Carousel |

#### Mécanique
| Code | Signification |
|---|---|
| UGC | User Generated Content |
| TH | Talking Head |
| BB | B-roll + voix off |
| TEX | Texte animé |
| SKT | Skit / Mise en scène |

### Exemples

**Campagne :**
```
MARCA_ACQ_PR_VID30_UGC_v1_2026-04
```
→ Marque / Acquisition / Angle Problème / Vidéo 30s / UGC / Version 1 / Avril 2026

**Adset :**
```
MARCA_ACQ_LA-1pct-purchasers_FR-25-45
```
→ Lookalike 1% acheteurs / France / 25-45 ans

**Creative :**
```
MARCA_PR_VID30_UGC_douleur-sommeil_v1
```
→ Angle Problème / Vidéo 30s / UGC / Douleur : sommeil / Version 1

### Pourquoi cette convention ?

Quand la convention est appliquée, Claude peut :
- Calculer le CPA moyen par angle (PR vs RS vs ED vs ID) en une seule requête
- Comparer les formats (VID15 vs VID30 vs STA) sans tri manuel
- Identifier quelle mécanique produit les meilleurs résultats
- Tracker la progression d'un angle dans le temps (v1 → v2 → v3)

Sans convention → analyse créative = tri manuel = perte de temps.

---

## Plateformes Compatibles Windsor.ai

Windsor.ai supporte également (en plus de Meta) :
- Google Ads
- TikTok Ads
- Snapchat Ads
- Pinterest Ads
- LinkedIn Ads

La même logique d'analyse peut être appliquée à ces plateformes en adaptant les métriques clés (voir les fichiers de référence dans `04-production/campaign-setup/references/`).
