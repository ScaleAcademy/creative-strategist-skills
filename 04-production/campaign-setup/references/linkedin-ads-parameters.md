# LinkedIn Ads — Paramètres de Campagne

## Contexte

LinkedIn Ads est la régie de référence pour le B2B et le ciblage professionnel précis.
CPM le plus élevé de toutes les régies (souvent 30–80€ CPM) — justifié uniquement si le LTV client est élevé.
Audience FR : 26M de membres, actifs dans les domaines professionnels (tech, finance, RH, marketing, conseil, formation pro).

**Quand utiliser LinkedIn Ads :**
- Cible = décideurs professionnels (titre de poste, taille d'entreprise, secteur)
- Produit / service B2B avec deal > 1 000€
- Formation professionnelle, certification, recrutement
- Événements professionnels

**Quand éviter :** B2C, petit panier, audiences larges grand public — utiliser Meta à la place.

---

## Structure des Niveaux

```
Groupe de Campagnes → Objectif + Budget + Dates
  └── Campagne → Audience + Format + Budget + Enchère
        └── Créative → Visuel + Texte + CTA + URL
```

---

## Objectifs Disponibles

| Objectif | Catégorie | Quand l'utiliser |
|---|---|---|
| **Notoriété de la marque** | Notoriété | CPM — impressions maximales |
| **Vues de vidéo** | Notoriété | Vues vidéo (ThruPlay) |
| **Engagement** | Considération | Interactions, followers, partages |
| **Visites du site web** | Considération | Clics vers landing page |
| **Génération de leads** | Conversion | Formulaires natifs LinkedIn (Lead Gen Forms) |
| **Conversions sur le site** | Conversion | Pixel LinkedIn — actions trackées |
| **Candidats** | Recrutement | Offres d'emploi |

---

## Ciblage Audience

### Attributs Professionnels (Force LinkedIn)

| Attribut | Options |
|---|---|
| **Secteur** | 150+ secteurs (Tech, Finance, Santé, Marketing, Conseil…) |
| **Taille d'entreprise** | 1–10 / 11–50 / 51–200 / 201–500 / 501–1000 / 1001–5000 / 5001–10000 / 10000+ |
| **Titre du poste** | Intitulé exact ou catégorie |
| **Fonction** | Marketing / Finance / RH / IT / Ventes / Direction / Opérations… |
| **Ancienneté** | Stagiaire / Junior / Senior / Manager / Directeur / VP / C-Suite / Propriétaire |
| **Compétences** | Compétences listées dans le profil |
| **Diplômes** | Niveau et domaine d'études |
| **Établissements** | Universités / Écoles spécifiques |
| **Années d'expérience** | 1–2 / 3–5 / 6–10 / 10+ |
| **Entreprises spécifiques** | Cibler des entreprises précises (account-based) |
| **Groupes LinkedIn** | Membres de groupes thématiques |

### Audiences LinkedIn Prédéfinies
LinkedIn propose des audiences préconstruites :
- Influenceurs / Décideurs / C-Suite
- Secteurs spécifiques (ex : "Professionnels de la Tech")

### Retargeting et Custom Audiences
| Source | Description |
|---|---|
| Pixel site | Visiteurs (7/30/90/180j) |
| Lead Gen Forms | Contacts ayant ouvert ou soumis un formulaire |
| Vidéo | Vues 25% / 50% / 75% / 97% |
| Compte entreprise | Engagés avec la page |
| Liste contacts | Email uploadé |
| Liste entreprises | Domaines ou noms d'entreprise uploadés (ABM) |

### Lookalike LinkedIn
- Basé sur une Custom Audience
- Taille source minimale : 300 membres

---

## Formats Créatifs

### Single Image Ad (Sponsored Content)
Format le plus courant. Apparaît dans le feed.

| Specs | Valeur |
|---|---|
| Ratio image | 1.91:1 (horizontal, recommandé) ou 1:1 (carré) |
| Résolution min | 1200×628 (1.91:1) / 1200×1200 (1:1) |
| Poids max | 5 MB |
| Texte intro | 150 caractères recommandés (600 max) |
| Titre | 70 caractères recommandés (200 max) |
| Description | 100 caractères (optionnel) |

### Video Ad
| Specs | Valeur |
|---|---|
| Ratio | 16:9 / 1:1 / 9:16 (vertical recommandé mobile) |
| Durée | 3s–30min (recommandé 15–30s) |
| Poids max | 200 MB |
| Sous-titres | Obligatoires (majorité regarde sans son) |
| Texte intro | 150 caractères recommandés |

### Carousel Ad
- 2–10 cartes
- Ratio 1:1 par carte
- Titre par carte : 45 caractères max

### Lead Gen Forms (LGF)
Formulaire natif LinkedIn — prérempli avec les données du profil.
→ Taux de complétion bien supérieur aux formulaires externes.
→ Champs disponibles : nom, prénom, email pro, entreprise, titre, téléphone, taille entreprise, secteur, ancienneté.
→ Jusqu'à 3 questions personnalisées.

### Message Ads (InMail Sponsorisé)
Message direct dans la boîte LinkedIn.
→ Facturé au CPS (coût par envoi).
→ Taux d'ouverture élevé (50%+) mais limité à 1 message / membre / 30 jours.
→ Texte : 500 caractères. CTA : 1 bouton.

### Conversation Ads
Message interactif avec plusieurs boutons de choix.
→ Permet des parcours conditionnels (si X → afficher Y).

### Document Ads
Partage d'un document (PDF, présentation) téléchargeable.
→ Idéal pour lead magnets (livre blanc, guide, étude de cas).

### Text Ads
Petites annonces texte + image 100×100px en sidebar.
→ CPM bas mais format peu visible — ROI limité.

---

## Stratégies d'Enchères

| Stratégie | Description | Quand |
|---|---|---|
| **Diffusion maximale** (défaut) | LinkedIn optimise automatiquement | Test, démarrage |
| **CPC manuel** | Plafond de coût par clic | Contrôle du coût |
| **CPM manuel** | Plafond de coût pour 1000 impressions | Notoriété contrôlée |
| **CPL cible** | Vise un coût par lead | Scale Lead Gen Forms |

**Budget minimum :** 10€/jour par campagne.
**Réalité :** LinkedIn est cher. CPC souvent 5–15€, CPL souvent 50–200€. Ne justifié que si LTV > 1 000€ ou B2B complexe.

---

## LinkedIn Insight Tag (Pixel)

### Événements à Tracker
| Événement | Déclencheur |
|---|---|
| Page view | Toutes les pages |
| Lead | Formulaire soumis |
| Purchase | Confirmation commande |
| Key page view | Pages stratégiques (pricing, contact) |

**Conversion Tracking :** Lier les conversions à l'Insight Tag pour mesurer le CPL réel.

---

## Spécificités Créatives LinkedIn

### Ce qui Performe
- **Chiffres et données** : l'audience pro est analytique — "3× plus de leads en 90 jours"
- **Social proof B2B** : logos d'entreprises clientes, témoignages de décideurs
- **Éducation + valeur** : insights, études de cas, benchmarks — contenu qui apprend quelque chose
- **Ton direct et professionnel** : pas de registre grand public — parler d'égal à égal
- **Vidéo courte sous-titrée** : majorité regarde sans son au bureau
- **Lead Gen Forms** : friction minimale = CPL souvent meilleur

### Ce qui Échoue
- Ton trop promotionnel / "salesy"
- Aucune valeur ajoutée dans le contenu
- CTA trop agressif pour une audience qui n'a pas encore confiance
- Ciblage trop large pour le CPM LinkedIn (budget dilapidé rapidement)

---

## Règles Publicitaires LinkedIn (Points Clés)

- **Contenu discriminatoire :** Interdit (genre, race, religion, origine).
- **Claims non prouvés :** "Le meilleur", "n°1" sans source = risque de rejet.
- **Données personnelles :** Conformité RGPD obligatoire sur les Lead Gen Forms.
- **Contenu adulte / offensant :** Tolérance zéro.

**Ressource officielle :** linkedin.com/legal/ads-policy
