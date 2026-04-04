# Ad Formats & Specs — Référence Cross-Plateforme

## Image

| Plateforme | Format | Ratio recommandé | Résolution min | Poids max | Texte overlay |
|---|---|---|---|---|---|
| **Meta** | Feed Image | 4:5 ou 1:1 | 1080×1350 / 1080×1080 | 30 MB | < 20% image |
| **Meta** | Stories / Reels | 9:16 | 1080×1920 | 30 MB | Éviter top/bottom 14% |
| **TikTok** | Spark Image | 9:16 | 1080×1920 | 5 MB | Natif TikTok |
| **Snapchat** | Snap Ad | 9:16 | 1080×1920 | 5 MB | Éviter top/bottom 15% |
| **Pinterest** | Standard Pin | 2:3 | 1000×1500 | 10 MB | Léger, intégré |
| **LinkedIn** | Sponsored Content | 1.91:1 ou 1:1 | 1200×628 / 1200×1200 | 5 MB | Professionnel |
| **Google Display** | Responsive | 1.91:1 + 1:1 | 1200×628 + 1200×1200 | 5 MB | Selon format |
| **Google Display** | Banner fixe | Multiple | Selon format | 150 KB | — |

---

## Vidéo

| Plateforme | Format | Ratio | Résolution min | Durée recommandée | Durée max | Poids max | Son |
|---|---|---|---|---|---|---|---|
| **Meta** | Feed Video | 4:5 ou 1:1 | 1080×1350 | 15–30s | 240 min | 4 GB | Opt. (sous-titres) |
| **Meta** | Reels | 9:16 | 1080×1920 | 15–30s | 90s | 4 GB | ON fort |
| **Meta** | Stories | 9:16 | 1080×1920 | 5–15s | 60s | 4 GB | Opt. |
| **TikTok** | In-Feed | 9:16 | 1080×1920 | 15–30s | 60s | 500 MB | ON fort |
| **TikTok** | TopView | 9:16 | 1080×1920 | 5–60s | 60s | 500 MB | ON fort |
| **Snapchat** | Snap Ad | 9:16 | 1080×1920 | 3–10s | 180s | 1 GB | ON fort |
| **Snapchat** | Commercial | 9:16 | 1080×1920 | 6s (non-skip) | 180s | 1 GB | ON fort |
| **Pinterest** | Standard Video | 2:3 ou 9:16 | 1080×1920 | 6–15s | 15 min | 2 GB | Opt. |
| **LinkedIn** | Video Ad | 16:9 / 1:1 / 9:16 | 1920×1080 | 15–30s | 30 min | 200 MB | OFF (sous-titres) |
| **YouTube** | In-Stream Skip | 16:9 | 1920×1080 | 15–30s | 3 min | — | ON fort |
| **YouTube** | Bumper | 16:9 | 1920×1080 | 6s | 6s | — | ON |

---

## Texte et Copy

| Plateforme | Champ | Limite affichée | Limite absolue |
|---|---|---|---|
| **Meta** | Primary Text | ~125 chars | 2200 chars |
| **Meta** | Headline | ~27 chars | 255 chars |
| **Meta** | Description | ~27 chars | 255 chars |
| **TikTok** | Description | ~55 chars | 100 chars |
| **Snapchat** | Brand Name | 25 chars | 25 chars |
| **Snapchat** | Headline | 34 chars | 34 chars |
| **Pinterest** | Titre | ~30 chars (preview) | 100 chars |
| **Pinterest** | Description | ~50 chars (feed) | 500 chars |
| **LinkedIn** | Intro Text | ~150 chars | 600 chars |
| **LinkedIn** | Headline | ~70 chars | 200 chars |
| **Google Display** | Headline | 30 chars | 30 chars |
| **Google Display** | Description | 90 chars | 90 chars |
| **YouTube** | Titre annonce | — | 15 chars |

---

## Zones Sécurisées (Safe Zones)

Zones à éviter pour les éléments critiques (texte, logo, CTA) :

| Plateforme | Zone à éviter |
|---|---|
| **Meta Feed** | Bandes inférieure et supérieure (UI Meta) |
| **Meta Stories / Reels** | 15% haut (barre de progression) + 25% bas (CTA / profil) |
| **TikTok** | 15% haut + 35% bas (UI TikTok + CTA + profil + description) |
| **Snapchat** | 15% haut + 20% bas (bouton swipe-up + interface) |
| **YouTube Reels** | 20% haut + 30% bas |

**Règle universelle :** Placer tout texte critique (hook, titre, CTA) entre 15% et 65% de la hauteur totale sur les formats verticaux 9:16.

---

## Sous-Titres et Accessibilité

| Plateforme | Sous-titres | Recommandé |
|---|---|---|
| Meta | Génération auto disponible | Oui — 85% des vues sans son |
| TikTok | Auto-captions disponibles | Oui — stylisés natif |
| LinkedIn | Manuels (SRT) recommandés | Obligatoire — audience bureau |
| YouTube | Auto-générés par Google | Recommandé |
| Snapchat | Manuels ou burn-in | Recommandé |

**Format sous-titres :** Brûlés dans la vidéo (burn-in) = plus fiable cross-plateforme. Fichier SRT = plus flexible mais dépend du player.

---

## Codes Couleur de Validation

| Status | Signification |
|---|---|
| ✅ Validé | Specs respectées — prêt à uploader |
| ⚠️ À vérifier | Proche des limites — tester avant lancement |
| ❌ Hors specs | Risque de rejet ou dégradation performance |

---

## Checklist Avant Upload

Pour chaque creative :
- [ ] Ratio et résolution conformes à la plateforme cible
- [ ] Texte critique dans la safe zone
- [ ] Sous-titres présents (si vidéo)
- [ ] Poids de fichier sous la limite
- [ ] Son testé (avec ET sans)
- [ ] CTA visible et lisible en < 2s
- [ ] Nom de fichier clair : `[marque]_[format]_[ratio]_[hook-id]_[date]`
