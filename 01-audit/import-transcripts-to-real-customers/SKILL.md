---
name: import-transcripts-to-real-customers
description: "Imports raw transcripts (Fathom, Telegram, WhatsApp, email, free-form text — any format) into the Notion 'Real Customers' database. Creates one entry per external speaker identified, fills the 'Client input' phase properties (Name, Client relation, Transcript, dates, demographics if available), and leaves the 'AI extracted' fields for the Notion AI agent to populate. Use when the user pastes/uploads a call transcript, conversation log, sales call recording, or any customer interaction artifact they want ingested for downstream Persona work. Trigger on: 'import this transcript', 'ingest this call', 'add this prospect to Real Customers', 'push this Fathom into Notion'. Requires Notion MCP authenticated. Does NOT extract insights (sentiment, pain points, objections, summary) — that's the Notion AI agent's job, triggered separately."
license: Proprietary
metadata:
  version: 1.0.0
  status: beta
  tags: [audit, notion, real-customers, transcripts, ingest]
  inputs: [transcript file or pasted text, optional client name hint]
  outputs: [1-N Notion pages in '👥 [DB] Real Customers']
  depends-on: [notion-mcp]
  notion-db: references/notion-db-schemas/db-real-customers.md
---

# Import Transcripts to Real Customers

Ingests raw conversation material (sales call, DM thread, intake form, anything) and creates structured entries in the `👥 [DB] Real Customers` Notion database — limited to the **Client input** phase fields. The downstream Notion AI agent (triggered manually or via the `Trigger AI` checkbox) will then extract the analytical fields.

**Input:** transcript text or file (any format) + optional hint about which client (Yuman, Autotrade, Netione…) the call belongs to.
**Output:** 1 page per external speaker in the Real Customers DB, with Client relation set, transcript stored, basic metadata filled where extractable.

---

## Before Starting

Confirm before running:
- [ ] Notion MCP is authenticated (test with a quick `notion-search` if uncertain)
- [ ] User has provided the transcript (pasted, attached file, or file path)
- [ ] The target DB exists in the user's workspace (default: `👥 [DB] Real Customers` — see `references/notion-db-schemas/db-real-customers.md` for the expected schema)

If any of the above fails, stop and ask the user.

---

## Phase 1 — Locate the target DB

1. Run `notion-search` with query `[DB] Real Customers` (filter to type=database).
2. Pick the database matching `👥 [DB] Real Customers`. If multiple matches, ask the user which one.
3. Fetch the database to get its data source ID (the `collection://...` URL).
4. Locate the relation targets:
   - **Clients DB** — fetch the `Client` property relation to get the Clients data source URL
   - **Personas DB** and **Angles DB** — not used by this skill (Maxime fills manually later)

---

## Phase 2 — Parse the transcript

Read the raw input and identify:

1. **Speakers** — who's in the conversation. Classify each as:
   - **Internal** (Maxime, his team, the client's own staff = excluded from creation)
   - **External** (prospect, lead, real customer = create one Real Customer entry)
2. **Client of attachment** — which of Maxime's clients (Yuman, Autotrade, Netione, etc.) this conversation relates to. Sources of truth, in priority order:
   - Explicit hint from the user
   - File name hints (`yuman-call-2026-05-18.txt`, `fathom-autotrade-xyz.md`)
   - Brand/product mentions in the transcript itself
   - If unclear, **ask the user** before proceeding
3. **Date** — first interaction date, if present (file metadata, opening "Hello [date]", Fathom timestamp header). Format: `DD/MM/YYYY`. If not present, leave empty.
4. **Source channel** — Call / Email / WhatsApp / DM / Form. Inferred from format (Fathom = Call, Telegram = DM, etc.).

---

## Phase 3 — For each external speaker, build the page payload

Map to the DB properties (see `references/notion-db-schemas/db-real-customers.md` for full schema). Fields to populate **only when the info is explicit in the source** — do not invent.

### Always set
| Property | Value |
|---|---|
| `Name` (title) | Anonymized: `[FirstName] [Initial]. - [City]` if available, else `[FirstName] [Initial].`, else just `[FirstName]` |
| `Client` (relation) | Page URL of the matching client in the Clients DB |
| `Transcript` (text) | The raw transcript content, **as-is**, no summary, no reformat. If the transcript is multi-speaker and very long, store only the segments where this speaker talks + the immediately preceding/following turns for context. |
| `Status` (select) | `Lead` (default) unless transcript explicitly indicates `Active customer` or `Churned` |
| `Acquisition source` (select) | One of [Ads / Organic / Word of mouth / Cold / Referral / Other inbound] if mentioned. Skip if unclear. |

### Set if extractable
| Property | When to set |
|---|---|
| `First interaction date` | If date present in transcript/filename |
| `Age range` | Only if explicitly stated ("I'm 34" → `25-34`) |
| `Gender` | Only if explicitly stated or clearly inferable from first name |
| `Work situation` | If explicitly stated ("I'm a freelance therapist" → `Freelancer`) |
| `LTV / AOV` | If explicitly mentioned as a number (€) |
| `Notes / verbatims` | 1-3 short raw quotes that stood out (mot-à-mot, no paraphrase) |
| `Important details (intake)` | Context fact the AI agent might miss (e.g. "introduced by Lucas, friend of the family") |
| `📎 Recording` | If a recording file path/URL was provided alongside the transcript |

### NEVER set — reserved for Notion AI agent
`Customer Sentiment`, `LF8 dominant`, `Awareness level (Schwartz)`, `Trigger event`, `Stated problem`, `Desired outcome`, `Main objection`, `Solutions tried`, `Summary`, `AI last run`.

### Reserved for Maxime (manual activation phase)
`Persona`, `Angles used`, `Micro-moments`, `Hooks identified`.

### Trigger AI checkbox
Default: **leave unchecked**. The user (Maxime) decides when to run the agent. Mention in the recap that he can either click `Trigger AI` in Notion OR check the boxes manually.

---

## Phase 4 — Create the pages

1. Use `notion-create-pages` with `parent.data_source_id` = Real Customers data source.
2. One page per external speaker.
3. Page **content** (body) can be empty — the transcript lives in the `Transcript` property, not in the body. Keep body for any future annotations.

If creating more than 5 pages in one go, show the user a quick summary table (Name / Client / Date / Status) and ask for confirmation before pushing.

---

## Phase 5 — Recap to user

After creation, output:

```
✅ X entries created in 👥 [DB] Real Customers

| Name | Client | Date | Status | URL |
|---|---|---|---|---|
| ... | ... | ... | ... | https://notion.so/... |

Next step:
→ Open the entries in Notion and click the "Trigger AI" checkbox
  to extract sentiment, pain points, objections, etc.
→ Or check the boxes manually if you prefer.
→ Persona and Angles relations: fill them yourself once the AI
  has run (use the 🎯 Activation view).
```

---

## Pitfalls

- **Don't invent fields.** If LTV isn't mentioned, leave empty. The AI extracted phase fills the analytical gaps; the manual activation phase fills the strategic links.
- **Don't summarize the transcript.** Store it raw in the `Transcript` field. Notion AI needs the verbatim to extract verbatim quotes.
- **Don't fill `Awareness level (Schwartz)` from your own inference** — that's the AI agent's job, and it has the prompt context to do it consistently.
- **Don't create duplicates.** Before creating, search the DB for an existing entry with the same Name + Client. If found, ask the user: update existing (append transcript to the field, store both with a separator) or create new (different call, different occurrence).
- **Don't push private info.** If the user pastes a transcript that contains full names, emails, phone numbers — anonymize the `Name` (FirstName + Initial). Leave the raw transcript intact in the `Transcript` field (it's internal), but flag in the recap that anonymization was applied.

---

## Verification checklist

After the skill runs, confirm:
- [ ] Number of pages created matches number of external speakers identified
- [ ] Each page has `Name`, `Client`, `Transcript` populated at minimum
- [ ] Each page is correctly grouped under its client in the `📥 Client input` view
- [ ] No analytical fields were touched (Sentiment / LF8 / Summary etc. all empty)
- [ ] Recap message lists every URL for quick navigation
