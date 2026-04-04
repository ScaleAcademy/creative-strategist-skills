# Google Ads — Paramètres de Campagne

## Types de Campagnes

| Type | Réseau | Usage principal |
|---|---|---|
| **Search** | Résultats Google (texte) | Intent fort — prospect qui cherche activement |
| **Performance Max** | Tous les canaux Google | Campagne unifiée IA — scale avancé |
| **Display** | Sites partenaires (GDN) | Retargeting, notoriété |
| **YouTube** | YouTube (vidéo) | TOF vidéo, awareness |
| **Shopping** | Google Shopping | E-commerce, catalogue produits |
| **App** | Toutes surfaces | Acquisition app |
| **Smart** | Automatique | Local, simplifié (non recommandé pour paid social) |

**Contexte Creative Strategist :** YouTube Ads et Display sont les plus pertinents pour le paid social. Search = intent pur, géré par le media buyer. Performance Max = les deux combinés.

---

## YouTube Ads

### Formats Vidéo

| Format | Skippable | Durée | Placement | Facturé |
|---|---|---|---|---|
| **In-Stream Skippable** | Après 5s | 12s–3min (recommandé 15–30s) | Avant / pendant / après vidéo | CPV (vue 30s ou interaction) |
| **In-Stream Non-Skippable** | Non | 15–20s max | Avant / pendant vidéo | CPM |
| **Bumper Ads** | Non | Max 6s | Avant vidéo | CPM |
| **In-Feed (Discovery)** | — | Tout | Résultats YouTube, page d'accueil | CPC (clic sur miniature) |
| **Outstream** | — | — | Sites partenaires (hors YouTube) | CPM visible |
| **Masthead** | — | Jusqu'à 30s | Page d'accueil YouTube | CPD (réservation) |

**Le plus utilisé en paid social :** In-Stream Skippable (15–30s) et Bumper 6s.

### Structure de l'In-Stream Skippable

```
0–5s → Hook absolu (avant le bouton "Ignorer")
5–15s → Tension / développement
15–25s → Pivot / solution
25–30s → CTA
```

**Règle des 5 premières secondes :** Si le hook ne capte pas avant le skip, la vue ne sera jamais mesurée comme view. Même logique que Meta mais avec le bouton "Ignorer" visible.

---

## Audiences Google

### Types d'Audiences

| Type | Description |
|---|---|
| **Affinités** | Groupes d'intérêts larges (ex : "Amateurs de cuisine") |
| **Intentions personnalisées** | Mots-clés que l'audience a cherchés récemment |
| **Audiences sur le marché** | Personnes en recherche active d'achat dans une catégorie |
| **Remarketing** | Visiteurs site / vues vidéo / liste CRM |
| **Audiences similaires** | Lookalike basé sur tes audiences de remarketing |
| **Données démographiques détaillées** | Situation familiale, propriétaire, niveau d'études, revenus |
| **Combinaisons personnalisées** | Superposition de plusieurs critères |

### Audiences les Plus Efficaces par Phase

| Phase | Audience recommandée |
|---|---|
| TOF | Affinités + Intentions personnalisées (mots-clés catégorie) |
| MOF | Sur le marché + Intentions personnalisées (marque + concurrents) |
| BOF | Remarketing visiteurs (30j) + liste CRM |

---

## Performance Max (PMax)

Campagne IA qui couvre Search, Display, YouTube, Gmail, Discover, Shopping simultanément.

### Ce qu'on Fournit
- **Assets créatifs :** images (15–20), logos (1–5), vidéos (1–5), headlines (3–5), descriptions (2–5)
- **Audience signals :** liste CRM, visiteurs site, intentions personnalisées
- **Objectif de conversion :** achat, lead, etc.

### Ce que Google Fait
- Assemble les assets automatiquement
- Teste les combinaisons
- Distribue sur tous les canaux

**Avantage :** Portée maximale avec peu de gestion.
**Inconvénient :** Peu de contrôle sur où et comment les assets sont utilisés. Reporting créatif limité.

**Conseil :** Créer des Asset Groups thématiques (1 angle = 1 asset group) pour isoler les performances.

---

## Stratégies d'Enchères Google

| Stratégie | Fonctionnement | Quand |
|---|---|---|
| **Maximiser les clics** | Max de clics dans le budget | Test trafic, début |
| **Maximiser les conversions** | Max de conversions dans le budget | CPA libre |
| **CPA cible** | Vise un coût par conversion | CPA fixé, volume stable |
| **ROAS cible** | Vise un retour sur dépense | E-commerce mature |
| **CPM cible** | Coût pour 1000 impressions | YouTube awareness |
| **CPV max** | Coût max par vue | YouTube engagement |

**Phase d'apprentissage Google :** 30–50 conversions en 30 jours pour les stratégies automatiques (CPA cible / ROAS cible).

---

## Display Ads — Specs

### Responsive Display Ads (RDA)
Google assemble automatiquement les assets :
- Images : jusqu'à 15 (ratio 1.91:1 et 1:1)
- Logos : jusqu'à 5
- Headlines : jusqu'à 5 (30 caractères max)
- Descriptions : jusqu'à 5 (90 caractères max)
- Vidéos YouTube : jusqu'à 5 (optionnel)

### Formats Display Fixes (Legacy)
| Format | Dimensions |
|---|---|
| Leaderboard | 728×90 |
| Medium Rectangle | 300×250 |
| Large Rectangle | 336×280 |
| Half Page | 300×600 |
| Billboard | 970×250 |
| Mobile Banner | 320×50 |

---

## Pixel Google (Google Tag / GA4)

### Événements Clés à Tracker

| Événement | Déclencheur |
|---|---|
| page_view | Toutes les pages |
| view_item | Page produit |
| add_to_cart | Bouton panier |
| begin_checkout | Page checkout |
| purchase | Confirmation commande |
| generate_lead | Soumission formulaire |

**Outil :** Google Tag Manager recommandé pour la gestion centralisée.
**Conversion Import :** Possibilité d'importer les conversions GA4 dans Google Ads.

---

## Règles Publicitaires Google (Points Clés)

- **Finance :** Certification obligatoire pour certains produits (crédits, investissements, cryptos).
- **Santé :** Claims stricts sur les médicaments et compléments. Approbation pays par pays.
- **Alcool :** Réglementé par pays — opt-in requis.
- **Claims trompeurs :** Interdiction stricte — "le meilleur", "le n°1" sans preuve = risque de rejet.
- **Contrefaçon :** Tolérance zéro.

**Ressource officielle :** support.google.com/adspolicy
