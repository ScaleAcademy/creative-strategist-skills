# Meta Ads — Paramètres de Campagne

## Structure des Niveaux

```
Campagne → Objectif + Budget (optionnel)
  └── Ad Set → Audience + Placement + Budget + Enchère
        └── Ad → Creative + CTA + URL
```

---

## Niveau Campagne

### Objectifs Disponibles

| Objectif | Quand l'utiliser | Optimisation algorithme |
|---|---|---|
| **Notoriété** | Brand awareness, reach maximum | Impressions / Reach |
| **Trafic** | Amener des visiteurs sur le site | Link clicks / Landing page views |
| **Engagement** | Interactions, vues vidéo, messages | Actions d'engagement |
| **Leads** | Formulaires natifs Meta ou site | Leads (formulaire ou pixel) |
| **Promotion d'app** | Téléchargements d'application | App installs / Events in-app |
| **Ventes** | Conversions site, catalogue produits | Purchases / Add to cart / autres événements pixel |

**Règle :** Toujours choisir l'objectif le plus bas dans le funnel que le budget permet d'alimenter correctement.
→ Si CPA cible = 30€ et budget = 10€/jour : optimiser sur "Ajouter au panier" ou "Leads", pas "Achat" (pas assez d'événements pour l'algo).
→ **Seuil de stabilité :** 50 événements / semaine sur l'événement optimisé.

### Advantage Campaign Budget (ACB)
Distribue le budget automatiquement entre les ad sets.
→ Utiliser en phase de scale uniquement. En test : budget fixe par ad set pour contrôler l'exposition.

---

## Niveau Ad Set

### Types d'Audiences

#### Core Audience (Ciblage manuel)
- **Démographie :** âge, genre, localisation, langue
- **Intérêts :** centres d'intérêt, comportements, pages likées
- **Comportements :** achats en ligne, utilisateurs d'appareils, voyageurs…
- **Conseil :** En 2024–2026, les audiences larges (pays + âge) surpassent souvent les intérêts précis grâce à l'algo. Tester les deux.

#### Custom Audience (Audience personnalisée)
Sources disponibles :
| Source | Ce que ça cible |
|---|---|
| Site web (Pixel) | Visiteurs, pages spécifiques, événements (30/60/90/180j) |
| Vidéo | Vues 25% / 50% / 75% / 95% |
| Compte Instagram / Page Facebook | Engagés (interactions, messages, profil visité) |
| Formulaire Lead | Personnes ayant ouvert / soumis un formulaire |
| Liste clients (CRM) | Email / téléphone uploadé et matché |
| Catalogue | Personnes ayant vu / ajouté au panier / acheté des produits |

#### Lookalike Audience
- Basée sur une Custom Audience source
- Taille : 1% (très similaire) → 10% (plus large)
- **Recommandé :** LAL 1–2% acheteurs ou leads qualifiés
- **Taille source minimale :** 100 personnes matchées (recommandé : 500–1000+)

#### Advantage+ Audience (Meta IA)
Meta choisit l'audience automatiquement en se basant sur la creative et l'historique.
→ À tester en parallèle des audiences manuelles sur budget test.

---

### Placements

#### Automatic Placements (Advantage+)
Meta optimise sur tous les placements disponibles.
→ **Par défaut recommandé** — permet à l'algo de trouver l'inventaire le moins cher.

#### Placements Manuels — Inventaire Meta

| Placement | Format | Notes |
|---|---|---|
| Facebook Feed | Image, Vidéo, Carousel | Audience 25–45+, forte intention |
| Instagram Feed | Image, Vidéo, Carousel | Audience 18–35, très visuel |
| Instagram Reels | Vidéo 9:16 | Reach organique fort, coût bas |
| Facebook Reels | Vidéo 9:16 | Audience FB, bon reach |
| Stories IG / FB | Vidéo ou Image 9:16 | Immersif, format plein écran |
| Audience Network | Image, Vidéo | Apps tierces — CPM bas, qualité variable |
| Messenger | Image, Vidéo | Moins utilisé, peut surprendre |
| Facebook Marketplace | Image | Intent shopping élevé |

**Quand exclure manuellement :** Audience Network si CPA > cible (qualité de trafic faible).

---

### Stratégies d'Enchères

| Stratégie | Fonctionnement | Quand l'utiliser |
|---|---|---|
| **Lowest Cost** (défaut) | Meta dépense le budget en optimisant le coût par résultat | Phase test, découverte |
| **Cost Cap** | Meta vise un CPA cible — ralentit la dépense si coût > cap | Phase scale avec CPA stable |
| **Bid Cap** | Plafond sur chaque enchère individuelle | Contrôle strict, scale avancé |
| **Highest Value** | Optimise pour la valeur d'achat la plus élevée | E-commerce avec catalogue, LTV focus |
| **Minimum ROAS** | Dépense uniquement si ROAS atteint le seuil | E-commerce mature, catalogue large |

**Règle de démarrage :** Commencer en Lowest Cost. Passer en Cost Cap uniquement après 50+ conversions / semaine avec CPA stable.

---

### Budget et Planning

| Paramètre | Recommandation |
|---|---|
| Budget journalier | Minimum 5–10× le CPA cible pour sortir de la phase d'apprentissage |
| Budget total (lifetime) | Si promotion ou test avec deadline |
| Période | Sans date de fin en phase test — évite les pics de CPM en fin de période |
| Programmation horaire | Rarement utile — laisser Meta optimiser sauf cas spécifiques (B2B, horaires précis) |

**Phase d'apprentissage :** 50 événements optimisés en 7 jours. Éviter les modifications pendant cette phase.

---

## Niveau Ad

### Formats Créatifs et Specs

| Format | Ratio recommandé | Résolution min | Durée max | Poids max |
|---|---|---|---|---|
| Image Feed | 1:1 ou 4:5 | 1080×1080 | — | 30 MB |
| Vidéo Feed | 4:5 ou 1:1 | 1080×1350 | 240 min (recommandé < 60s) | 4 GB |
| Stories / Reels | 9:16 | 1080×1920 | 60s (Stories) / 90s (Reels) | 4 GB |
| Carousel | 1:1 | 1080×1080 | — par carte | 30 MB/carte |
| Collection | 1:1 + image hero | 1080×1080 | — | 30 MB |

**Texte overlay :** Meta recommande < 20% de l'image en texte. Au-delà : reach réduit potentiel.
**Texte principal (Primary text) :** 125 caractères recommandés (tronqué après)
**Titre (Headline) :** 40 caractères recommandés
**Description :** 30 caractères recommandés

### CTAs Disponibles (sélection)

| CTA | Usage |
|---|---|
| En savoir plus | TOF, découverte |
| S'inscrire | Lead gen, événement |
| Acheter maintenant | BOF, e-commerce |
| Télécharger | App, ressource |
| Obtenir un devis | B2B, service |
| Réserver | Service, événement |
| Contacter | B2B, local |
| Voir plus | Contenu, vidéo |

---

## Pixel et Événements

### Événements Standard (ordre funnel)

| Événement | Priorité | Déclencheur |
|---|---|---|
| PageView | Toujours | Toutes les pages |
| ViewContent | Recommandé | Page produit |
| AddToCart | Recommandé | Bouton panier |
| InitiateCheckout | Recommandé | Page checkout |
| AddPaymentInfo | Optionnel | Saisie paiement |
| Purchase | Critique | Confirmation commande |
| Lead | Critique | Soumission formulaire |
| CompleteRegistration | Recommandé | Inscription compte |

**Vérification :** Utiliser Meta Pixel Helper (extension Chrome) pour valider les événements.

---

## Règles Publicitaires Meta (Points Clés)

- **Claims de santé :** Interdiction des before/after corporels. Claims de perte de poids très encadrés.
- **Finance :** Disclaimer obligatoire pour certains produits financiers. Cryptomonnaies = approbation requise.
- **Alcool :** Ciblage âge minimum requis par pays.
- **Texte discriminatoire :** Interdit de cibler ou exclure sur base de caractéristiques protégées.
- **Urgence artificielle :** "Offre expire dans 1h" sans réelle deadline = risque de rejet.
- **Contenu choquant :** Images trop graphiques, gore, nudité = rejet automatique.

**Ressource officielle :** facebook.com/policies/ads
