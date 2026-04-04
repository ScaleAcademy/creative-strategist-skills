# TikTok Ads — Paramètres de Campagne

## Structure des Niveaux

```
Campagne → Objectif + Budget
  └── Ad Group → Audience + Placement + Budget + Enchère + Planning
        └── Ad → Creative + CTA + URL + Profil TikTok
```

---

## Niveau Campagne

### Objectifs Disponibles

| Objectif | Catégorie | Quand l'utiliser |
|---|---|---|
| **Reach** | Notoriété | Maximiser les impressions uniques |
| **Video Views** | Notoriété | Maximiser les vues vidéo (2s ou 6s) |
| **Community Interaction** | Considération | Followers, visites de profil |
| **Traffic** | Considération | Clics vers site |
| **App Promotion** | Considération | Téléchargements / events in-app |
| **Lead Generation** | Conversion | Formulaires natifs TikTok |
| **Website Conversions** | Conversion | Conversions trackées via Pixel |
| **Product Sales** | Conversion | Catalogue produits TikTok Shop |

**Particularité TikTok :** L'algo TikTok est très puissant sur les audiences larges. Les intérêts fins fonctionnent moins bien que sur Meta — laisser l'algo faire avec des creatives fortes.

---

## Niveau Ad Group

### Types d'Audiences

#### Audience Automatique (Broad)
TikTok cible automatiquement selon la creative et l'objectif.
→ **Recommandé en test** sur TikTok — l'algo excelle en ciblage large.

#### Custom Audience
| Source | Ce que ça cible |
|---|---|
| Pixel site | Visiteurs, événements (7/14/30/60/180j) |
| Engagement vidéo | Vues 2s / 6s / 25% / 50% / 75% / 100% |
| Profil TikTok | Followers, interactions, visites |
| Fichier client | Email / IDFA uploadé |
| App activity | Événements in-app |
| Lead gen | Personnes ayant soumis un formulaire |

#### Lookalike
- Taille : 1% / 2% / 5% / 10% / 15% / 20%
- Source recommandée : acheteurs ou leads qualifiés
- Taille source minimale : 100 personnes (recommandé 1 000+)

#### Targeting Manuel
| Paramètre | Options |
|---|---|
| Âge | 13–17 / 18–24 / 25–34 / 35–44 / 45–54 / 55+ |
| Genre | Tous / Homme / Femme |
| Localisation | Pays, région, ville |
| Langue | Langue du device |
| Intérêts | Catégories larges (beauté, finance, fitness, gaming…) |
| Comportements | Interactions avec créateurs, hashtags, sons |
| Appareils | iOS / Android, opérateurs, connexion |

---

### Placements

| Placement | Description |
|---|---|
| **TikTok Feed** | Principal — vidéo plein écran dans le For You Page |
| **TikTok Search** | Résultats de recherche TikTok |
| **Pangle** | Réseau de partenaires (apps tierces) |
| **Global App Bundle** | Inventory hors TikTok |

**Recommandation :** TikTok Feed uniquement en test. Ajouter Pangle en scale si CPM TikTok augmente.

---

### Stratégies d'Enchères

| Stratégie | Fonctionnement | Quand l'utiliser |
|---|---|---|
| **Lowest Cost** (défaut) | Dépense le budget au coût minimum | Phase test |
| **Cost Cap** | Vise un CPA ou CPM cible | Scale avec CPA stable |
| **Bid Cap** | Plafond sur chaque enchère | Contrôle strict avancé |
| **Value Optimization** | Maximise la valeur des achats | E-commerce avec catalogue |

**Phase d'apprentissage TikTok :** 50 événements optimisés en 7 jours. Plus sensible aux modifications que Meta.

---

### Budget

| Paramètre | Minimum | Recommandé |
|---|---|---|
| Budget journalier campagne | 50€ | 100€+ en test |
| Budget journalier ad group | 20€ | 50€+ |
| Budget total (lifetime) | — | Pour promos datées |

**Important :** TikTok nécessite des budgets plus élevés que Meta pour sortir de l'apprentissage rapidement. Budget trop bas = données peu fiables.

---

## Niveau Ad

### Formats et Specs

| Format | Ratio | Résolution | Durée | Poids max |
|---|---|---|---|---|
| In-Feed Video | 9:16 (recommandé) / 1:1 / 16:9 | 720×1280 min | 5–60s (recommandé 15–30s) | 500 MB |
| TopView | 9:16 | 720×1280 min | 5–60s | 500 MB |
| Spark Ads | Reprend le format du post organique | — | Durée du post original | — |
| Collection Ads | 9:16 + carte produits | 720×1280 | 5–60s | 500 MB |
| Lead Gen | 9:16 | 720×1280 | 5–60s | 500 MB |

**Texte :** Description : 1–100 caractères (55 recommandés avant coupure)
**Hashtags :** Autorisés dans la description (optionnel)
**Profil affiché :** Compte TikTok Business requis et associé

### Spark Ads — Boosting Organique
Permet de booster une vidéo organique existante (ton compte ou un créateur partenaire).
→ **Avantage majeur :** conserve les commentaires, likes, partages du post original = preuve sociale visible.
→ Nécessite un code d'autorisation du créateur (valable 30 ou 60 jours).
→ Idéal pour UGC Creator Partnerships.

### CTAs Disponibles

| CTA | Usage |
|---|---|
| Shop Now | E-commerce |
| Learn More | TOF, découverte |
| Sign Up | Lead gen |
| Download | App |
| Book Now | Service |
| Contact Us | B2B, local |
| Get Quote | Service |
| Subscribe | Contenu, SaaS |

---

## Pixel TikTok et Événements

### Installation
Via TikTok Events Manager — pixel JS sur le site + API Conversions (Server-Side) recommandée.

### Événements Standard

| Événement | Priorité |
|---|---|
| PageView | Toujours |
| ViewContent | Recommandé |
| AddToCart | Recommandé |
| InitiateCheckout | Recommandé |
| PlaceAnOrder | Critique |
| CompletePayment | Critique |
| SubmitForm | Critique (lead gen) |

**API Conversions :** Fortement recommandée — améliore le matching et réduit l'impact de l'iOS 14+.

---

## Spécificités Créatives TikTok

### Ce qui Performe
- **Native first :** La vidéo doit ressembler à du contenu organique TikTok — pas à une pub.
- **Hook < 3s :** TikTok est encore plus brutal que Meta sur la rétention des premières secondes.
- **Son ON :** 93% des utilisateurs TikTok regardent avec le son. Concevoir pour le son d'abord.
- **Vertical natif :** Toujours 9:16. Jamais de letterbox ou de bordures noires.
- **Texte overlay natif :** Style TikTok (sous-titres, captions dynamiques) > style "publicité".
- **Creators UGC :** Les Spark Ads via créateurs performent souvent mieux que les pubs brand.

### Ce qui Échoue
- Vidéo trop produite / trop "corporate"
- Logo en watermark visible (signale une pub)
- Call-to-action trop agressif dans les 5 premières secondes
- Recycler une vidéo Meta en 4:5 sur TikTok sans l'adapter

---

## Règles Publicitaires TikTok (Points Clés)

- **Alcool, tabac, jeux d'argent :** Très encadrés — approbation requise selon pays.
- **Santé / médicaments :** Claims stricts, before/after corporel très risqué.
- **Finance :** Disclaimer obligatoire selon produit et pays.
- **Mineurs :** Ciblage 13–17 ans interdit pour de nombreuses catégories.
- **Droits musicaux :** Utiliser uniquement la Commercial Music Library TikTok pour les pubs.

**Ressource officielle :** ads.tiktok.com/help/
