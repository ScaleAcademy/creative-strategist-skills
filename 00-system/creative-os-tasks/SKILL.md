---
name: creative-os-tasks
description: Convention de synchronisation des tâches du Creative OS (Notion). À déclencher dès qu'une action importante est posée sur un client / une création (par Maxime, Mailys ou Claude) OU quand on signale qu'une tâche est faite ("j'ai fini X", "X c'est bon", "marque X en terminé", "passe X en cours"). Crée/met à jour une tâche dans la DB Tasks Creative OS, rattachée au client, avec Réalisé par + Statut. Tout skill branché sur une base Creative OS doit appeler cette convention plutôt que de réécrire sa logique de tâches.
---

# creative-os-tasks

Skill **système / pivot** du suivi de tâches dans le **Creative OS** (Notion). Le suivi vit dans **Notion** (vue linéaire par client), pas dans l'agent. Objectif : voir par client ce qui est en cours / terminé et **qui l'a fait**.

> ⚠️ Les IDs ci-dessous pointent vers le workspace Creative OS de référence (MX Marketing). Dans un autre workspace, retrouver les DB équivalentes via `notion-search` et adapter.

## DB cible : Tasks Creative OS
- Data source `collection://11f5824e-1911-4a57-9856-e1a352ec56dc` (database `d3bcfe12-f6b0-40af-8e45-8e45cbf2aad3`). Vue par défaut groupée par **Client**.
- Propriétés :
  - `Task` (title)
  - `Client` (relation → DB Clients, `collection://33538550-814d-822a-809c-879c3d9f8819`) — **toujours rattacher**.
  - `Réalisé par` (select : **Maxime / Mailys / Claude / Externe**) — qui exécute.
  - `Status` (status : **Pas commencé / En cours / Terminé**).
  - `Priority` (Haute / Moyenne / Basse), `Type` (Script / Brief créa / Shooting / Éditing vidéo / Static / Motion graphics / Audio · voix / Review / Autre).
  - `Due Date` (passer `date:Due Date:start`), `Notes`, relations `Brief` / `Concept`, `Assignee` (person, optionnel = responsable humain).

## Trouver la fiche client
`Client` est une relation. Récupérer l'ID de la fiche dans la DB Clients via `notion-search` (data_source_url `collection://33538550-814d-822a-809c-879c3d9f8819`) avec le nom du client, puis passer son URL de page (JSON array). Repères transcription : Human/Yuman/Mohamed/Meij → @Yuman · Victor → Autotrade · Netione/Guillaume → Netione.

## Mode WRITE — créer / upserter une tâche
Déclenché quand une **action significative** est posée (livrable ou décision concrète à suivre : créer un brief/concept, lancer/programmer des ads, produire des statiques, modifier une landing/popup, MAJ d'un numéro/lien, construire un calendrier de tests…). Pas le small talk ni les micro-étapes.

Règle de validation :
- **Action exécutée par l'agent (Claude)** → créer la tâche **automatiquement** : `Réalisé par = Claude`, `Status` = `En cours` puis `Terminé` une fois fini.
- **Action humaine** (Maxime / Mailys / Externe) → **proposer d'abord** la liste (titre + client + date + Réalisé par), attendre l'OK. `Status` par défaut = `Pas commencé`.

Avant de créer : vérifier qu'une tâche équivalente n'existe pas (éviter les doublons) → si oui, **mettre à jour** plutôt que dupliquer.

## Mode UPDATE — clôture / avancement dynamique
Déclencheurs : "j'ai fini / terminé X", "X c'est bon / c'est fait", "marque X en terminé", "passe X en cours", "X est bloqué".
Action : retrouver la tâche (titre + client) et mettre à jour `Status` (Terminé / En cours), `Réalisé par` si pertinent. Confirmer en une ligne.

## Pour les autres skills du Creative OS
Tout skill produisant un livrable lié à une base Creative OS (briefs, concepts, landing pages, ads, personas…) appelle cette convention **en fin d'exécution** pour journaliser la tâche correspondante (client + `Réalisé par` + `Status`), au lieu de réimplémenter sa propre logique. Un seul endroit à maintenir. Voir aussi `references/notion-output-protocol.md`.

## Autres DB Creative OS avec `Réalisé par`
- `Tâches Scale Academy` : data source `collection://97546354-adbd-4d64-8cab-fc0d5d657bc6` (mêmes options Réalisé par).
