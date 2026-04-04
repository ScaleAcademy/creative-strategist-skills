# Snapchat Ads — Paramètres de Campagne

## Contexte

Snapchat Ads est pertinent pour les audiences 13–34 ans (cœur de cible).
En France, Snapchat touche ~20M d'utilisateurs actifs mensuels, très concentrés sur les 15–30 ans.
CPM généralement plus bas que Meta — bonne option pour le reach TOF à budget maîtrisé.

---

## Structure des Niveaux

```
Campagne → Objectif + Budget
  └── Ad Set → Audience + Placement + Budget + Enchère
        └── Ad → Creative + CTA + URL
```

---

## Niveau Campagne

### Objectifs Disponibles

| Objectif | Catégorie | Quand l'utiliser |
|---|---|---|
| **Brand Awareness** | Notoriété | Impressions maximales |
| **Video Views** | Notoriété | Vues 2s ou 15s |
| **Traffic** | Considération | Clics vers site |
| **App Installs** | Considération | Téléchargements app |
| **Engagement** | Considération | Interactions avec le contenu |
| **Lead Generation** | Conversion | Formulaires natifs Snap |
| **Conversions** | Conversion | Pixel Snapchat — achats / leads |
| **Catalog Sales** | Conversion | Catalogue produits |

---

## Niveau Ad Set

### Types d'Audiences

#### Predefined Audiences (Snap)
Audiences pré-construites par Snapchat basées sur le comportement in-app :
- Lifestyle (fitness, beauté, gaming, mode, food…)
- Life Moments (mariage, déménagement, naissance…)
- Shopper (comportements d'achat)
- Viewer (types de contenus consommés)

#### Custom Audiences
| Source | Ce que ça cible |
|---|---|
| Pixel site | Visiteurs, événements (7/14/28/60/90/180j) |
| Engagement Snap | Interactions avec tes Stories payantes |
| Lookalike Snap | Similaires à une Custom Audience source |
| Customer List | Email / numéros uploadés |
| App Activity | Événements in-app (via SDK) |

#### Lookalike
- Taille : Narrow / Balanced / Broad
- Source recommandée : acheteurs ou leads
- Taille source minimale : 300 matchés (recommandé 1000+)

#### Targeting Manuel
| Paramètre | Options |
|---|---|
| Âge | 13–17 / 18–20 / 21–24 / 25–34 / 35+ / Personnalisé |
| Genre | Tous / Homme / Femme |
| Localisation | Pays, région, ville, rayon |
| Langue | Langue du device |
| Appareil | iOS / Android |
| Opérateur | Réseau mobile |
| Intérêts | Catégories Snap |

---

### Placements

| Placement | Description |
|---|---|
| **Snap Ads (Between Stories)** | Plein écran entre les Stories des amis / publishers |
| **Story Ads** | Vignette dans la section Discover — ouvre une mini-Story |
| **Collection Ads** | Carrousel produits sous une vidéo |
| **Dynamic Ads** | Catalogue produits automatisé |
| **Commercials** | Non-skippable 6s dans les Shows Snap (publishers sélectionnés) |
| **AR Lenses** | Filtres RA sponsorisés (budget élevé, branding) |

**Recommandé pour paid social :** Snap Ads (Between Stories) — format le plus répandu et le plus testé.

---

### Stratégies d'Enchères

| Stratégie | Fonctionnement | Quand |
|---|---|---|
| **Auto-Bid** (défaut) | Optimise automatiquement | Test, démarrage |
| **Target Cost** | Vise un CPA ou CPM cible | Scale avec CPA stable |
| **Max Bid** | Plafond sur chaque enchère | Contrôle strict |

---

### Budget

| Paramètre | Minimum |
|---|---|
| Budget journalier | 5€ (recommandé 20€+ pour données fiables) |
| Budget total | Pour promos datées |

---

## Niveau Ad

### Formats et Specs

| Format | Ratio | Résolution | Durée | Poids max |
|---|---|---|---|---|
| Snap Ad (vidéo) | 9:16 | 1080×1920 | 3–180s (recommandé 3–15s) | 1 GB |
| Snap Ad (image) | 9:16 | 1080×1920 | — | 5 MB |
| Story Ad | 9:16 | 1080×1920 | 3–180s par carte | 1 GB |
| Collection | 9:16 + miniatures | 1080×1920 | 3–180s | 1 GB |
| Commercial | 9:16 | 1080×1920 | 6s (non-skip) / 3–180s (skip) | 1 GB |

**Zones Safe :** Éviter le texte critique dans les 15% hauts et bas de l'image (UI Snap recouvre ces zones).
**CTA Swipe-Up :** Lien attaché — swipe up déclenche l'ouverture du site ou de l'app.

### Headline et CTA

| Champ | Limite |
|---|---|
| Brand Name | 25 caractères |
| Headline | 34 caractères |
| CTA | Sélection dans une liste prédéfinie |

### CTAs Disponibles
Découvrir / Acheter / Réserver / Télécharger / En savoir plus / S'inscrire / Regarder / Installer

---

## Pixel Snapchat et Événements

### Événements Standard

| Événement | Déclencheur |
|---|---|
| PAGE_VIEW | Toutes les pages |
| VIEW_CONTENT | Page produit |
| ADD_TO_CART | Bouton panier |
| START_CHECKOUT | Page checkout |
| PURCHASE | Confirmation commande |
| SIGN_UP | Inscription |
| LEAD | Formulaire soumis |

**API Conversions Snap :** Recommandée pour améliorer le matching post-iOS 14.

---

## Spécificités Créatives Snapchat

### Ce qui Performe
- **Plein écran natif 9:16** : aucune barre noire, remplir tout l'écran
- **Hook < 2s** : l'audience Snap swipe encore plus vite que TikTok
- **Son ON** : format immersif, concevoir avec musique et voix
- **Style UGC natif** : ressembler à du contenu Snap organique — pas à une pub TV
- **Swipe-up clair** : mentionner verbalement "swipe up" ou afficher une flèche
- **Sous-titres** : toujours, pour les secondes sans son

### Ce qui Échoue
- Vidéo en 16:9 ou avec letterbox
- Pas de CTA clairement identifiable
- Trop de texte (audience jeune, consommation très rapide)
- Ton trop corporate ou trop "publicité classique"

---

## Règles Publicitaires Snapchat (Points Clés)

- **Alcool / tabac / vaping :** Très encadré — ciblage 18+ obligatoire, approbation requise.
- **Contenu adulte :** Interdit sauf catégories spéciales très encadrées.
- **Mineurs :** Ciblage 13–17 = restrictions fortes (pas de ciblage comportemental, pas d'alcool, pas de jeux d'argent).
- **Finance / Crypto :** Approbation requise.
- **Claims santé :** Mêmes restrictions que Meta.

**Ressource officielle :** businesshelp.snapchat.com/s/article/ad-policies
