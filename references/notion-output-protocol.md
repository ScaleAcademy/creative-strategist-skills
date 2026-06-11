# Notion Output Protocol — Dual-Mode Skills

> Core architecture convention for every skill in this repo.
> A skill must work for **anyone who downloads it** (standalone mode) AND plug into the
> **Creative Strategist OS Notion ecosystem** when available (connected mode).
> Same logic, two output adapters.

## The two modes

| | Standalone mode | Connected mode (Notion OS) |
|---|---|---|
| Requirement | none | Notion MCP authenticated + target DB exists |
| Reads from | local `.md` files in the client folder | Notion DBs (+ local files as fallback) |
| Writes to | local `.md` files in the client folder | Notion DB entries (+ optional local copy) |
| Who it serves | community member without the ecosystem | ecosystem owner — information is never lost, it lands in the right DB, linked |
| Positioning | free / lead magnet | the upsell: "same skill, but your insights compound" |

## Routing logic (every skill runs this BEFORE producing output)

1. **Detect** — is a Notion MCP available in this session? (try a cheap `notion-search` if uncertain)
2. **Check** — does the target DB exist? (search by DB title, compare against the schema file in `references/notion-db-schemas/`)
3. **Route:**
   - MCP + DB found → **connected mode**. Announce it: "Writing to `📋 [DB] X` in Notion."
   - MCP but DB missing → offer: (a) create the DB from the schema file, (b) fall back to local files.
   - No MCP → **standalone mode**, silently. Output local `.md` following the skill's `outputs:` frontmatter.
4. **Never duplicate the source of truth.** Connected mode writes data to Notion; local files then only hold heavy/working material (briefs for editors, raw footage notes). Standalone mode: local files ARE the source of truth.
5. **"Meta in Notion, content in Drive" applies to reference docs — NOT to reports.** Analysis deliverables (Performance Reports, Analysis Briefs, audits) are read in Notion: write the FULL content in the page body (tables included), with `Repo Path`/`Drive URL` as the backup copy. A KB stub that only links out is a routing failure.

## Frontmatter convention

Every skill declares both adapters in its SKILL.md metadata:

```yaml
metadata:
  inputs: [persona-[name].md, brand-context.md]          # standalone inputs
  outputs: [creative-brief-[brand]-[date].md]            # standalone outputs
  notion-reads: [db-personas.md, db-knowledge-base.md]   # connected-mode sources (schema files)
  notion-writes: [db-briefs.md]                          # connected-mode targets (schema files)
  depends-on: [audience-research]                        # other skills
```

`notion-reads` / `notion-writes` reference schema files in `references/notion-db-schemas/` —
never raw DB IDs. IDs are workspace-specific; schemas are replicable.

## Schema files (`references/notion-db-schemas/`)

One file per DB, format established by `db-real-customers.md`:
Purpose → Database location (template) → Views → Properties tables (by phase/group) → Relations → Known issues / planned changes.

A community member replicates the DBs from these files (manually or by asking Claude to create
them via Notion MCP), then every connected-mode skill works in their workspace.

## Hard rules (apply to ALL connected-mode writes)

- **Relations over text** — link to Clients / Personas / Concepts / Hypotheses DBs, never type names as plain text.
- **Every Brief/Concept links to a Hypothesis** (Roadmap DB). If none exists, create it first. A creative without a hypothesis is lost at analysis time.
- **Never overwrite — version.** Major rework = new entry or version bump + changelog line (Date + Updated by Claude + summary).
- **Status fields driven by automations stay read-only** (e.g. Briefs status) — skills must not set them by hand.
- **DB properties are the single source of truth** — don't duplicate property values in the page body. Body = narrative only.
