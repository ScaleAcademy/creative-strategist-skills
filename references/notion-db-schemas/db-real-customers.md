# 👥 [DB] Real Customers — Notion Schema

> Reference schema for the `Real Customers` database used by the Creative Strategist OS.
> Anyone replicating this structure in their own Notion workspace can run all skills that depend on it.

## Purpose

Capture every real prospect/customer interaction (sales calls, DM threads, intake forms, signed clients) as **one entry per person**, then progressively enrich each entry through three phases:

1. **Client input** — raw intake (filled by import skills or by hand)
2. **AI extracted** — analytical layer (filled by a Notion AI agent triggered on demand)
3. **Activation** — strategic linking to Personas, Angles, Hook tactics (filled by the strategist)

## Database location (template)

- Teamspace : `MX Marketing` (or any client-facing workspace)
- Parent page : `[DB] DATABASES`
- Database title : `👥 [DB] Real Customers`
- Default icon : 👥

## Views

| View | Filter | Group by | Purpose |
|---|---|---|---|
| `Default view` | — | Client | Full table |
| `📥 Client input` | — | Client | Ingestion phase (skills + hand entry) |
| `🧠 AI extracted` | `AI last run is not empty` | Client | Entries the Notion AI agent has processed |
| `🎯 Activation` | — | Client | Final strategic linking (Persona / Angles) |

Sort default: `First interaction date` descending.

---

## Properties

### Phase 1 — Client input (filled by skill `import-transcripts-to-real-customers` or by hand)

| Property | Type | Required | Options / Format | Notes |
|---|---|---|---|---|
| `Name` | Title | ✅ | Free text | Anonymize: `FirstName + Initial. - City` (e.g. `Marie L. - Lyon`) |
| `Client` | Relation → `[DB] Clients` | ✅ | — | Single relation; identifies which of the agency's clients this customer belongs to |
| `Transcript` | Text | ✅ | Raw, verbatim | Full conversation content, no summary, no reformat |
| `Status` | Select | — | `Lead` · `Active customer` · `Churned` | Default `Lead` |
| `First interaction date` | Date | — | `DD/MM/YYYY` | Date of first known touchpoint |
| `Acquisition source` | Select | — | `Ads` · `Organic` · `Word of mouth` · `Cold` · `Referral` · `Other inbound` | How they entered the funnel |
| `Age range` | Select | — | `18-24` · `25-34` · `35-44` · `45-54` · `55+` | Only if explicitly stated |
| `Gender` | Select | — | `Woman` · `Man` · `Other` | Only if explicit/clearly inferable |
| `Work situation` | Select | — | `Employee` · `Freelancer` · `Entrepreneur` · `Job seeker` · `Student` · `Retired` · `Other` | Only if stated |
| `LTV / AOV` | Number (€) | — | Euro format | Lifetime value or average order value, if known |
| `Important details (intake)` | Text | — | Free text | Context the AI might miss (referrals, special arrangements) |
| `Notes / verbatims` | Text | — | Free text | 1-3 raw quotes, no paraphrase |
| `📎 Recording` | File | — | — | Audio/video file of the original interaction if available |

### Phase 2 — AI extracted (filled by Notion AI agent, NEVER by import skills)

| Property | Type | Options / Format | Filled by |
|---|---|---|---|
| `Customer Sentiment` | Select | `Très négatif` · `Négatif` · `Neutre` · `Positif` · `Très positif` | Notion AI |
| `Awareness level (Schwartz)` | Select | `UN - Unaware` · `PA - Problem Aware` · `SA - Solution Aware` · `MA - Most Aware` · `BA - Brand/Product Aware` | Notion AI |
| `LF8 dominant` | Select | LF1 → LF8 (Cabot's Life Force 8) | Notion AI |
| `Trigger event` | Text | Free text | Notion AI |
| `Stated problem` | Text | Free text | Notion AI |
| `Desired outcome` | Text | Free text | Notion AI |
| `Main objection` | Text | Free text | Notion AI |
| `Solutions tried` | Text | Free text | Notion AI |
| `Summary` | Text | Free text | Notion AI |
| `AI last run` | Date | ISO timestamp | Notion AI (auto) |
| `Trigger AI` | Checkbox | `__YES__` / `__NO__` | Trigger to launch the agent |

### Phase 3 — Activation (filled manually by the strategist)

| Property | Type | Notes |
|---|---|---|
| `Persona` | Relation → `[DB] Personas` | Attribute customer to 1-N personality archetypes |
| `Angles used` | Relation → `[DB] Angles` | Which creative angles converted this customer (when known) |
| `Micro-moments` | Text | Decision-trigger moments distilled from the conversation |
| `Hooks identified` | Text | Hook hypotheses derived from this customer's language |

---

## Related databases (relations)

| Property | Target DB | Cardinality |
|---|---|---|
| `Client` | `[DB] Clients` | Single |
| `Persona` | `[DB] Personas` | Multiple |
| `Angles used` | `[DB] Angles` | Multiple |

---

## Workflow (typical lifecycle of one entry)

1. **Intake** — skill `import-transcripts-to-real-customers` ingests a call/transcript → creates the page with Client input fields filled (Name, Client, Transcript, dates, demographics if explicit).
2. **AI extraction** — strategist opens the page and checks `Trigger AI` (or clicks the agent button). Notion AI reads `Transcript` + `Notes / verbatims` and populates the analytical fields. `AI last run` timestamp is set.
3. **Persona attribution** — strategist reviews the AI output, attributes the entry to 1-N Personas, links to converting Angles, distills Micro-moments and Hooks.
4. **Persona DB rollup** — the linked Persona pages count how many Real Customers map to them → priority sorting for which Personas deserve deep work.

---

## Anonymization rule

All `Name` values must be anonymized: `FirstName + Initial. - City` (e.g. `Marie L. - Lyon`).
The `Transcript` field can stay verbatim (it's internal) but should not include phone numbers, emails, full last names, addresses. Strip those before pushing.

---

## Skills that depend on this schema

| Skill | Role |
|---|---|
| `import-transcripts-to-real-customers` (01-audit) | Phase 1 ingestion |
| `audience-research` (02-research) | Reads `Phase 2 + 3` fields to build personas |
| `persona-attribution` (planned) | Bulk assigns Personas from AI-extracted fields |

---

## Changelog

- `v1.0` — 2026-06-03 — Initial schema documentation (matches Notion state of 2026-05-26 refactor, ref. memory `project_mx_real_customers`)
