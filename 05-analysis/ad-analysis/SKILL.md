---
name: ad-analysis
description: "Deconstructs an ad's performance data to identify why it worked or failed, extract learnings, and generate 3 test hypotheses. Use after a creative has accumulated significant spend. Trigger on: 'analyse cette pub', 'pourquoi ça marche', 'déconstruction créative', 'qu'est-ce qu'on apprend de ce résultat'. Produces a learning report and 3 actionable next test hypotheses."
metadata:
  version: 1.0.0
  status: stable
  tags: [analysis, performance, creative, testing, hypotheses]
  inputs: [données performance creative (métriques Meta), accès visuel ou description de la creative]
  outputs: [rapport déconstruction + 3 hypothèses de test actionnables]
  depends-on: [brand-health]
---

# Ad Analysis

## Before Starting

Confirme avant de commencer :
- [ ] Données de performance disponibles : minimum Impressions, CTR, Hook Rate (si vidéo), CPA ou CPL
- [ ] Dépense suffisante pour des données fiables (minimum 100€ dépensés, idéalement 300€+)
- [ ] Accès visuel à la creative (lien, screenshot, ou description détaillée)
- [ ] Brief original disponible ou contexte d'origine connu (sinon, analyser sans brief = hypothèses à labeler)
- [ ] Période définie et audience ciblée connues

Pour les benchmarks de référence : voir [references/kpi-benchmarks.md](references/kpi-benchmarks.md)

---

## Phase 1 : Lire les Données

Collecter et organiser les métriques clés :

| Métrique | Valeur | Benchmark | Status |
|---|---|---|---|
| Hook Rate (vidéo) | | 20–30% | |
| Hold Rate 50% | | 20–35% | |
| CTR (link click) | | 1–2% | |
| CPM | | 8–15€ | |
| CPA / CPL | | [cible] | |
| Fréquence | | < 3 | |
| Dépense totale | | — | |

Identifier immédiatement : est-ce un winner, un learner, ou un loser ?
- **Winner :** KPI primaire ≤ cible + volume significatif
- **Learner :** Données insuffisantes ou KPI proche de la cible — à continuer
- **Loser :** KPI primaire > cible × 1.5 avec dépense suffisante — à killer

---

## Phase 2 : Déconstruire la Creative

Analyser la structure de la creative sur 4 couches :

### Hook (Première seconde / Premier frame)
- Qu'est-ce qui a été utilisé comme amorce ?
- Tactic identifiée (T01–T35) ?
- Trigger psychologique ?
- Pourquoi ça a fonctionné ou pas au regard du Hook Rate ?

### Corps du Message
- Quelle mécanique créative (M1–M8) ?
- Quelle promesse centrale ?
- Quel proof point ?
- Objection adressée ou non ?

### CTA
- Clarté et alignement avec l'awareness stage ?
- Friction du CTA adaptée au niveau d'engagement ?

### Format & Production
- Format adapté à la plateforme et à l'audience ?
- Qualité de production appropriée (ni trop, ni trop peu) ?
- Ratio et durée optimaux ?

---

## Phase 3 : Formuler le Diagnostic

Identifier la cause principale de la performance — bonne ou mauvaise.

**Si winner :**
- Qu'est-ce qui a le plus contribué ? (hook / angle / mécanique / format / audience)
- Ce résultat est-il reproductible ou contextuel (période, budget) ?
- Qu'est-ce qu'on peut extraire comme principe pour les prochaines créas ?

**Si loser :**
- Où s'est perdu l'audience ? (Hook Rate faible = hook / CTR faible = corps ou CTA / CPA élevé = landing page ou offre)
- L'angle était-il juste mais l'exécution mauvaise ? Ou l'angle lui-même ne fonctionnait pas ?
- Qu'est-ce que ce résultat révèle sur le persona ou le marché ?

---

## Phase 4 : Générer 3 Hypothèses de Test

Chaque hypothèse doit être :
- **Testable** : une seule variable changée
- **Motivée** : basée sur un signal dans les données, pas une intuition seule
- **Actionnable** : la prochaine creative à produire est claire

**Format d'une hypothèse :**
> "Si on [change X], alors [KPI Y] devrait [augmenter/diminuer] parce que [raison issue des données]."

---

## Output Format

```markdown
# Ad Analysis — [Marque] — [Nom Creative] — [Date]

## Données Performance
| Métrique | Valeur | Benchmark | Status |
[tableau]

## Verdict
[ ] Winner  [ ] Learner  [ ] Loser

## Déconstruction

### Hook
Tactic : [T##] — Trigger : [biais/LF]
Analyse : [Pourquoi ça a marché / pas marché au regard du Hook Rate]

### Corps du Message
Mécanique : [M#] — Angle : [C#]
Analyse : [Lecture du Hold Rate et du CTR]

### CTA
Analyse : [Alignement awareness / clarté / friction]

### Format
Analyse : [Format, ratio, durée — adéquation]

## Diagnostic Principal
[1 phrase : ce qui explique principalement le résultat]

## Ce qu'on Apprend
[2–3 insights généralisables pour les prochaines créas]

## 3 Hypothèses de Test

**H1 :**
Si on [change X], alors [KPI] devrait [direction] parce que [raison].
Creative à produire : [description courte]

**H2 :**
[Même structure]

**H3 :**
[Même structure]
```

---

## Related Skills

- `01-audit/brand-health` — baseline avant analyse
- `05-analysis/account-audit` — vue macro après plusieurs analyses individuelles
- `05-analysis/strategy-gap` — si l'analyse révèle des angles non testés
- `03-strategy/creative-brief` — pour briefe les hypothèses de test
