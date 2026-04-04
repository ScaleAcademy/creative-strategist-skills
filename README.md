# Creative Strategist Skills

> A systematic skill library for Creative Strategists building 
> high-performance paid social campaigns.

Built by [Scale Academy](https://scale-academy.fr) — the francophone 
training platform for Creative Strategists.

---

## How Skills Work Together

Skills reference each other and build on shared context.
**brand-guidelines** is the foundation — every skill checks it first.

                    ┌─────────────────────────────────┐
                    │         brand-guidelines         │
                    │  (read by all other skills first)│
                    └────────────────┬────────────────┘
                                     │
     ┌──────────────┬────────────────┼────────────────┬──────────────┐
     ▼              ▼                ▼                ▼              ▼
┌──────────┐ ┌──────────┐  ┌──────────────┐  ┌──────────┐  ┌──────────────┐
│  Audit   │ │ Research │  │   Strategy   │  │Production│  │  Analysis    │
├──────────┤ ├──────────┤  ├──────────────┤  ├──────────┤  ├──────────────┤
│brand-    │ │market-   │  │creative-     │  │static-   │  │ad-analysis   │
│guidelines│ │research  │  │brief         │  │production│  │account-audit │
│brand-    │ │audience- │  │message-      │  │video-    │  │strategy-gap  │
│health    │ │research  │  │sequencing    │  │production│  │              │
│brand-    │ │review-   │  │hook-writing  │  │ai-video- │  │              │
│alignment │ │audit     │  │              │  │production│  │              │
│          │ │customer- │  │              │  │campaign- │  │              │
│          │ │reality   │  │              │  │setup     │  │              │
└────┬─────┘ └────┬─────┘  └──────┬───────┘  └────┬─────┘  └──────┬───────┘
     │            │               │               │               │
     └────────────┴───────┬───────┴───────────────┴───────────────┘
                          │
        Skills cross-reference each other:
          brand-guidelines → all skills (prerequisite)
          review-audit → hook-writing, creative-brief
          audience-research → creative-brief, hook-writing
          customer-reality → creative-brief, hook-writing
          creative-brief ↔ hook-writing ↔ message-sequencing
          campaign-setup → ad-analysis → strategy-gap

---

## Workflow

Audit → Research → Strategy → Production → Analysis

Each phase feeds the next. No brief without research.
No campaign without a validated brief.

---

## Available Skills

| Phase | Skill | Description |
|---|---|---|
| 01-audit | brand-guidelines | Brand intake + context document |
| 01-audit | brand-health | Performance baseline from ad account |
| 01-audit | brand-alignment | Business objectives + constraints |
| 02-research | market-research | Competitive landscape + sophistication |
| 02-research | audience-research | Persona Deep Dive — 3 layers |
| 02-research | review-audit | Verbatim mining from customer reviews |
| 02-research | customer-reality | Micro-moments + emotional mapping |
| 03-strategy | creative-brief | Complete brief — angle, hook, specs |
| 03-strategy | message-sequencing | Full-funnel sequence plan |
| 03-strategy | hook-writing | Psychologically-driven hooks |
| 04-production | static-production | Nano Banana prompts + designer briefs |
| 04-production | video-production | Technical brief for human editors |
| 04-production | ai-video-production | VEO3 + Kling scene prompts |
| 04-production | campaign-setup | Meta campaign structure + nomenclature |
| 05-analysis | ad-analysis | Creative deconstruction + next tests |
| 05-analysis | account-audit | Full account performance review |
| 05-analysis | strategy-gap | Missing angles, personas, stages |

---

## Installation
```bash
# Clone the repo
git clone https://github.com/ScaleAcademy/creative-strategist-skills.git

# Copy skills into your project
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
