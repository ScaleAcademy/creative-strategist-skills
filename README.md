# Creative Strategist Skills

> A systematic skill library for Creative Strategists building 
> high-performance paid social campaigns.

Built by [Scale Academy](https://scale-academy.fr) — the training 
platform for Creative Strategists.

**Scale Academy** trains Creative Strategists in the profession of tomorrow: 
understanding why a creative works, building solid hypotheses, producing 
ads that convert.

3 pillars: **Psychological** (Schwartz) · **Creative** (Da Vinci) · 
**Analysis** (Hopkins)

---

## Community

Join the Scale Academy community to access courses, templates, 
and AI prompts to become a world-class Creative Strategist.

| Language | Community |
|---|---|
| 🇫🇷 Français | [Scale Academy — FR](https://www.skool.com/scale-academy-6184) |
| 🇬🇧 English | *Coming soon* |
| 🇪🇸 Español | *Coming soon* |

---

## How Skills Work
```
brand-guidelines (prerequisite — read by all skills first)
         │
         ├── 01-audit
         ├── 02-research  
         ├── 03-strategy
         ├── 04-production
         └── 05-analysis
```

Skills cross-reference each other:
- [`brand-guidelines`](01-audit/brand-guidelines/SKILL.md) → [`brand-research`](01-audit/brand-research/SKILL.md) → [`brand-specs`](01-audit/brand-specs/SKILL.md) → [`static-production`](04-production/static-production/SKILL.md)
- [`review-audit`](02-research/review-audit/SKILL.md) → [`hook-writing`](03-strategy/hook-writing/SKILL.md), [`creative-brief`](03-strategy/creative-brief/SKILL.md)
- [`audience-research`](02-research/audience-research/SKILL.md) → [`creative-brief`](03-strategy/creative-brief/SKILL.md), [`hook-writing`](03-strategy/hook-writing/SKILL.md)
- [`creative-brief`](03-strategy/creative-brief/SKILL.md) ↔ [`hook-writing`](03-strategy/hook-writing/SKILL.md) ↔ [`message-sequencing`](03-strategy/message-sequencing/SKILL.md)
- [`campaign-setup`](05-analysis/campaign-setup/SKILL.md) → [`ad-analysis`](05-analysis/ad-analysis/SKILL.md) → [`strategy-gap`](05-analysis/strategy-gap/SKILL.md)

---

## 00 — System

| File | Usage |
|---|---|
| [`create-agent`](00-system/create-agent.md) | Generate a validation agent for any workflow step |

---

## 01 — Audit

**Skills**
| Skill | Input | Output |
|---|---|---|
| [`brand-guidelines`](01-audit/brand-guidelines/SKILL.md) | URL + client interview | brand-context.md |
| [`brand-research`](01-audit/brand-research/SKILL.md) | Brand URL + name + hero product | brand-research-brief.json |
| [`brand-specs`](01-audit/brand-specs/SKILL.md) | brand-research-brief.json | brand-spec-card.png + visual-style-card.png |
| [`brand-health`](01-audit/brand-health/SKILL.md) | Ads dashboard access | Baseline KPI report |
| [`brand-alignment`](01-audit/brand-alignment/SKILL.md) | Founder conversation | Real objectives + constraints |

**References**
- [`checklist.md`](01-audit/brand-guidelines/references/checklist.md) — Brand guidelines checklist
- [`brand-spec-card-prompt.md`](01-audit/brand-specs/references/brand-spec-card-prompt.md) — HTML prompt for Brand Spec Card
- [`visual-style-card-prompt.md`](01-audit/brand-specs/references/visual-style-card-prompt.md) — HTML prompt for Visual Style Card
- [`brand-health.md`](01-audit/brand-health/references/brand-health.md) — Meta Ads benchmarks
- [`brand-alignment.md`](01-audit/brand-alignment/references/brand-alignment.md) — Growth stage → creative implication

**Agents de validation**
| Agent | Validates | Min score |
|---|---|---|
| [`agent-brand-research.md`](01-audit/brand-research/agent.md) | brand-research-brief.json completeness | 90/100 |
| [`agent-brand-specs.md`](01-audit/brand-specs/agent.md) | Spec Card + Style Card quality | 90/100 |

---

## 02 — Research

**Skills**
| Skill | Input | Output |
|---|---|---|
| [`market-research`](02-research/market-research/SKILL.md) | Market + competitors | Sophistication + positioning gaps |
| [`audience-research`](02-research/audience-research/SKILL.md) | Client data | Persona Deep Dive Layer 1/2/3 |
| [`review-audit`](02-research/review-audit/SKILL.md) | Raw verbatims | Library of 30+ verbatims by theme |
| [`customer-reality`](02-research/customer-reality/SKILL.md) | Persona + verbatims | Micro-moments + emotional mapping |

**References**
- [`sophistication.md`](02-research/market-research/references/sophistication.md) — 5 Schwartz levels
- [`positioning.md`](02-research/market-research/references/positioning.md) — Competitor map, white spaces
- [`competitors.md`](02-research/market-research/references/competitors.md) — Sources + research method
- [`awareness-levels.md`](02-research/market-research/references/awareness-levels.md) — Unaware → Most Aware + creative implications
- [`life-force-8.md`](02-research/audience-research/references/life-force-8.md) — 8 innate desires (Whitman)
- [`persona-layers.md`](02-research/audience-research/references/persona-layers.md) — Layer 1 / 2 / 3
- [`generational-insights.md`](02-research/audience-research/references/generational-insights.md) — Generational context
- [`content-consumption.md`](02-research/audience-research/references/content-consumption.md) — Platforms + register by channel
- [`marketing-psychology.md`](02-research/audience-research/references/marketing-psychology.md) — Applied cognitive biases
- [`sources.md`](02-research/review-audit/references/sources.md) — Amazon / Reddit / Meta comments / surveys
- [`micro-moments.md`](02-research/customer-reality/references/micro-moments.md) — Trigger situations
- [`emotional-mapping.md`](02-research/customer-reality/references/emotional-mapping.md) — Q1 emotion / Q2 private-social / Q3 acute-chronic

**Agents de validation**
| Agent | Validates | Min score |
|---|---|---|
| [`agent-audience-research.md`](02-research/audience-research/agent.md) | Persona Deep Dive Layer 1/2/3 | 90/100 |
| [`agent-review-audit.md`](02-research/review-audit/agent.md) | Verbatim library (30+ quotes) | 90/100 |

---

## 03 — Strategy

**Skills**
| Skill | Input | Output |
|---|---|---|
| [`creative-brief`](03-strategy/creative-brief/SKILL.md) | Persona + awareness + objective | Complete creative brief |
| [`message-sequencing`](03-strategy/message-sequencing/SKILL.md) | Brief + starting awareness | 4–5 touchpoint plan × awareness × CTA |
| [`hook-writing`](03-strategy/hook-writing/SKILL.md) | Brief + persona + biases | 10 hooks calibrated by awareness stage |

**References**
- [`ad-angles.md`](03-strategy/creative-brief/references/ad-angles.md) — C1/C2/C3/C4 matrix
- [`creative-mechanics.md`](03-strategy/hook-writing/references/creative-mechanics.md) — 8 mechanics (Implied Answer, Reframe, Trojan Horse…)
- [`psych-biases.md`](03-strategy/creative-brief/references/psych-biases.md) — Biases (FOMO, loss, social proof…)
- [`persuasion-principles.md`](03-strategy/creative-brief/references/persuasion-principles.md) — 7 Cialdini principles
- [`emotional-drivers.md`](03-strategy/creative-brief/references/emotional-drivers.md) — LF8 + FROM → TO
- [`ad-formulas.md`](03-strategy/creative-brief/references/ad-formulas.md) — PAS / BAB / FAB / OCR
- [`visual-formats.md`](03-strategy/creative-brief/references/visual-formats.md) — 45+ formats (Yapper, VSL, Before/After…)
- [`styles-library.md`](03-strategy/creative-brief/references/styles-library.md) — S101 → S403 (Canva link)
- [`hook-tactics.md`](03-strategy/hook-writing/references/hook-tactics.md) — 42 hook types
- [`hook-voice-patterns.md`](03-strategy/hook-writing/references/hook-voice-patterns.md) — Swipe file — native feed structures
- [`copy-frameworks.md`](03-strategy/hook-writing/references/copy-frameworks.md) — Headline + CTA formulas
- [`sequencing-plan.md`](03-strategy/message-sequencing/references/sequencing-plan.md) — TOF / MOF / BOF / Re-engage

**Agents de validation**
| Agent | Validates | Min score |
|---|---|---|
| [`agent-creative-brief.md`](03-strategy/creative-brief/agent.md) | Creative brief coherence + readiness | 90/100 |
| [`agent-hook-writing.md`](03-strategy/hook-writing/agent.md) | Hook calibration + scroll-stop power | 90/100 |

---

## 04 — Production

**Skills**
| Skill | Input | Output |
|---|---|---|
| [`static-production`](04-production/static-production/SKILL.md) | Validated brief | Nano Banana prompt + designer brief |
| [`animate-statics`](04-production/animate-statics/SKILL.md) | Winning static + spec cards | 3-4s animated GIF/MP4 (manual or MCP) |
| [`video-production`](04-production/video-production/SKILL.md) | Validated brief | Sequenced technical brief for editor |
| [`ai-video-production`](04-production/ai-video-production/SKILL.md) | Brief + reference images | VEO3 / Kling scene-by-scene prompts |

**References**
- [`templates.md`](04-production/static-production/references/templates.md) — Static format library (S101–S105)
- [`headline-template.md`](04-production/static-production/references/headline-template.md) — Headline templates for static ads
- [`hook-structure.md`](04-production/video-production/references/hook-structure.md) — Visual / audio / text / first frame hook
- [`pacing.md`](04-production/video-production/references/pacing.md) — Rhythm, transitions, animated subtitles
- [`sounds.md`](04-production/video-production/references/sounds.md) — Music styles by format + sources
- [`scene-structure.md`](04-production/video-production/references/scene-structure.md) — Duration, camera angle, motion, lighting
- [`character-bible.md`](04-production/video-production/references/character-bible.md) — SCOTT (AutoTrades robot)

**Agents de validation**
| Agent | Validates | Min score |
|---|---|---|
| [`agent-static-production.md`](04-production/static-production/agent.md) | Nano Banana prompt before generation | 90/100 |
| [`agent-copy-editor.md`](04-production/static-production/agent-copy-editor.md) | Final copy — grammar + compliance (pass/fail) | 90/100 |

---

## 05 — Analysis

**Skills**
| Skill | Input | Output |
|---|---|---|
| [`ad-analysis`](05-analysis/ad-analysis/SKILL.md) | Creative + metrics | Deconstruction + hypotheses + 3 tests |
| [`account-audit`](05-analysis/account-audit/SKILL.md) | Meta account access + period | Macro report — top performers + gaps |
| [`strategy-gap`](05-analysis/strategy-gap/SKILL.md) | Current campaign data | Missing angles + uncovered personas |
| [`campaign-setup`](05-analysis/campaign-setup/SKILL.md) | Validated creatives | Ready-to-launch Meta campaign structure |
| [`meta-ads-analysis`](05-analysis/meta-ads-analysis/SKILL.md) | Meta dashboard data | Detailed Meta account analysis |
| [`media-buyer-routine`](05-analysis/media-buyer-routine/SKILL_media_buyer.md) | Active campaigns | Daily / weekly / monthly buyer routine |

**References**
- [`kpi-benchmarks.md`](05-analysis/ad-analysis/references/kpi-benchmarks.md) — Hook Rate / CTR / CPA by platform
- [`pattern-library.md`](05-analysis/ad-analysis/references/pattern-library.md) — Winning patterns (living document)
- [`analysis-framework.md`](05-analysis/ad-analysis/references/analysis-framework.md) — Key metrics, how to read the data
- [`gap-matrix.md`](05-analysis/strategy-gap/references/gap-matrix.md) — Uncovered awareness / untested angles
- [`naming-convention.md`](references/naming-convention.md) — Campaign / ad set / ad naming convention (global)
- [`kill-rules.md`](05-analysis/campaign-setup/references/kill-rules.md) — CPC > 2.50€ / CTR < 1.5% / CPA > target…
- [`campaign-structure.md`](05-analysis/campaign-setup/references/campaign-structure.md) — P1 test / P2 retarget / P3 scale / P4 re-engage
- [`meta-ads-parameters.md`](05-analysis/campaign-setup/references/meta-ads-parameters.md) — Meta Ads setup parameters
- [`google-ads-parameters.md`](05-analysis/campaign-setup/references/google-ads-parameters.md) — Google Ads setup parameters
- [`tiktok-ads-parameters.md`](05-analysis/campaign-setup/references/tiktok-ads-parameters.md) — TikTok Ads setup parameters
- [`linkedin-ads-parameters.md`](05-analysis/campaign-setup/references/linkedin-ads-parameters.md) — LinkedIn Ads setup parameters
- [`pinterest-ads-parameters.md`](05-analysis/campaign-setup/references/pinterest-ads-parameters.md) — Pinterest Ads setup parameters
- [`snapchat-ads-parameters.md`](05-analysis/campaign-setup/references/snapchat-ads-parameters.md) — Snapchat Ads setup parameters
- [`ad-formats-specs.md`](05-analysis/campaign-setup/references/ad-formats-specs.md) — Ad formats specs by platform
- [`windsor-setup.md`](05-analysis/meta-ads-analysis/references/windsor-setup.md) — Windsor.ai setup for Meta analysis

**Agents de validation**
| Agent | Validates | Min score |
|---|---|---|
| [`agent-ad-analysis.md`](05-analysis/ad-analysis/agent.md) | Creative deconstruction + test design | 90/100 |

---

## Installation
```bash
git clone https://github.com/ScaleAcademy/creative-strategist-skills.git
cp -r creative-strategist-skills/ .agents/skills/
```

---

## Foundational References

- Eugene Schwartz — *Breakthrough Advertising*
- Drew Eric Whitman — *Ca$hvertising* (Life Force 8)
- Claude Hopkins — *Scientific Advertising*
- Robert Cialdini — *Influence*

---

## License

MIT — Maxime Capelle / Scale Academy
