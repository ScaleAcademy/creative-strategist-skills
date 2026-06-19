---
name: meta-launch
description: "Pilots the actual LAUNCH of ads on Meta via the official Meta/Facebook MCP, with hard guardrails at every step: full plan validated before any API call, everything created PAUSED, strict URL/UTM/creative rules, and a post-publication diff against the validated plan to catch Meta's silent auto-mutations. Use when assets are final and the campaign structure exists (see campaign-setup). Trigger on: 'launch these ads', 'push to Meta', 'publie les ads', 'mise en ligne campagne', 'put the campaign live'. Requires Meta MCP. Launching ads without this skill's checklist is how expensive Meta mistakes happen."
metadata:
  version: 1.0.0
  status: beta
  tags: [production, meta-ads, launch, implementation, guardrails, mcp, notion]
  inputs: [approved creative brief, final ad assets (hosted), client naming convention, campaign objective + budget]
  outputs: [launch plan (validated before execution), launched entities report (post-verification diff)]
  notion-reads: [db-briefs.md, db-clients.md]
  notion-writes: [db-briefs.md]
  depends-on: [creative-brief, campaign-setup]
---

# Meta Launch

This skill executes what `campaign-setup` designed. Campaign architecture, naming convention,
budgets-per-phase, and kill rules are defined there — do not redesign them here.
Meta-launch owns one thing: **getting the entities onto Meta safely and verifiably**.

> **Requires the official Meta/Facebook MCP** (`ads_create_campaign`, `ads_create_ad_set`,
> `ads_create_creative`, `ads_create_ad`, `ads_update_entity`, `ads_get_ad_entities`).
> No MCP = no launch. Fall back to producing the launch plan as a manual checklist.

## Output Routing (Dual-Mode)

This skill follows [references/notion-output-protocol.md](../../references/notion-output-protocol.md).
Run the routing logic before producing output.

| Standalone output | Connected-mode target |
|---|---|
| `launch-plan-[brand]-[date].md` + `launch-report-[brand]-[date].md` (local files) | Update the existing `📝 [DB] Briefs` entries: set `Link` (final ad URL/preview) + `Publish Date`. Read `📋 [DB] Clients` for naming convention + client defaults, `📝 [DB] Briefs` for the approved briefs being launched. |

Connected-mode rules (hard):
- **Never touch `Status`** on Briefs — it is automation-driven (checkboxes + dates). Writing `Publish Date` is what triggers the automation `✅ Approved → 📅 Scheduled` (ads are created PAUSED = scheduled, not live yet — `🚀 Published` comes later, when you manually activate them).
- Update only the Brief entries for ads that **passed Phase 4 verification** — a created-but-diverged ad is not "scheduled".
- Never create new Brief entries here — launching is an update to existing briefs, not a creation event.

---

## Before Starting

Confirm before starting — **all of them**, no exceptions:

- [ ] Meta MCP available and connected to the correct ad account (`ads_get_ad_accounts` — confirm account name with the user)
- [ ] Creative brief approved (from `creative-brief`)
- [ ] Campaign structure + naming convention + kill rules defined (from `campaign-setup`)
- [ ] Final assets hosted/uploaded (image hashes or video IDs available, correct ratios)
- [ ] **Client context loaded** — the client's CLAUDE.md / `📋 [DB] Clients` entry, for client-specific defaults (language, page ID, pixel, UTM template, domain). If no client context exists, ASK before building the plan.
- [ ] Destination URL confirmed — and whether an A/B test is currently running on the landing page
- [ ] Campaign objective + budget confirmed by the user

Missing input = stop and ask. Never "fill in something reasonable" on a live ad account.

---

## Phase 1: Plan Before Anything

**No API write call happens before the user explicitly validates the full plan.** Not one.

Build and present the COMPLETE plan as a tree:

```markdown
# Launch Plan — [Brand] — [Date]

## Account
Ad account: [name + ID] · Page: [name + ID] · Pixel/Dataset: [ID]

## Tree
CAMPAIGN [name per client convention] — Objective: [X] — Budget: [X€/day CBO | ABO]
└── AD SET [name] — Budget: [X€/day if ABO] — Audience: [definition] — Placements: [list]
    — Language: [client default] — Optimization: [event]
    ├── AD [name] — Asset: [file/ID] — Hook variant: [#]
    │     Website URL: [full URL incl. path]
    │     Display Link: [root domain only]
    │     URL Parameters (UTMs): [utm string]
    │     CTA: [button + copy]
    └── AD [name] — [same fields]

## Status at creation: ALL PAUSED
## Kill rules in effect: [from campaign-setup]
```

Every ad shows its **final URL, UTMs, display link, naming, and CTA** — the exact values that
will hit the API. Then ask: **"Validate this plan for creation (everything PAUSED)?"**
and wait for an explicit yes. Any change request = regenerate the plan, re-validate.

---

## Phase 2: Create Everything PAUSED

Create top-down: campaign → ad sets → creatives → ads. **`status: PAUSED` on every entity** —
campaign, ad set, AND ad. No exceptions, even if the user says "launch it live directly".

Activation is a **separate human decision**, made after Phase 4 verification, by the user,
entity by entity (`ads_activate_entity`). This skill never activates anything as a side effect.

If any creation call fails: stop, report, fix, and re-validate the affected branch — do not
improvise a workaround on a live account.

---

## Phase 3: Hard Rules at Creation

These are non-negotiable, learned from real (expensive) mistakes:

| # | Rule | Why |
|---|---|---|
| 1 | **UTMs go in the ad's URL Parameters field** (via `ads_update_entity`), NEVER pasted into the link URL | Pasted UTMs break A/B test routing and get stripped/duplicated by Meta |
| 2 | **Ad URL = the A/B test URL** when a landing test is running — not the page URL directly | Sending traffic straight to one variant silently kills the test |
| 3 | **`multi_advertiser_ads.enroll_status = OPT_OUT`** in every creative spec | Impossible to change after creation — opt-in shows your ad next to competitors |
| 4 | **Display Link = root domain only** (e.g. `domain.com/`) — full path stays in Website URL | Full paths in display link look spammy and can be rejected |
| 5 | **Client defaults from the client's CLAUDE.md / Clients DB are mandatory** (e.g. one client requires ad set language = NL) | Defaults forgotten at creation = re-doing the whole ad set |
| 6 | **CTA sells the NEXT step only** — the immediate honest action ("See how it works"), never the end goal ("Get rich") | Trust is built step by step; over-promising CTAs burn the funnel |

Rules 1–4 are encoded INTO the plan in Phase 1, so validation already covers them.
If a rule cannot be satisfied (e.g. unknown A/B test status), stop and ask — don't guess.

---

## Phase 4: Post-Publication Verification (anti Meta-mutations)

Meta silently mutates entities at/after creation. **Never trust the creation response.**

Re-fetch EVERY created entity (`ads_get_ad_entities` with full fields) and **diff against
the validated Phase 1 plan**, field by field. Known auto-mutations to hunt for:

- [ ] **WhatsApp auto-checked** on the ad (messaging destination added without asking)
- [ ] **Budget auto-adjusted** (campaign or ad set budget differs from the plan)
- [ ] **Ads auto-added to the ad set** (entities you did not create — Advantage+ / existing-post clones)
- [ ] **Placements changed** (manual selection silently expanded to Advantage+ placements)
- [ ] Plus: status still PAUSED · UTMs intact in URL Parameters · Display Link unchanged · `multi_advertiser_ads` still OPT_OUT

Output the diff report:

```markdown
# Launch Report — [Brand] — [Date]

## Created entities
| Entity | ID | Status | Diff vs plan |
|---|---|---|---|
| Campaign [name] | [id] | PAUSED | ✅ none |
| Ad set [name] | [id] | PAUSED | ⚠️ placements expanded by Meta → [detail] |
| Ad [name] | [id] | PAUSED | ✅ none |

## Action needed before activation
[List every diff + the fix applied or proposed]
```

**Any diff = report it and fix it BEFORE handing back.** Only then tell the user the launch
is ready for activation. Activation remains their call.

---

## Phase 5: Connected Mode (Notion Write-Back)

If connected mode is active (see Output Routing), after Phase 4 passes:

1. Find each launched creative's entry in `📝 [DB] Briefs` (by `#NNN-B1` ID from the brief).
2. Set `Link` → the final ad URL (or ad preview link) and `Publish Date` → launch date.
3. **Do NOT touch `Status`** — the automations derive it from checkboxes + dates.
4. Confirm: "Updated [N] briefs in `📝 [DB] Briefs` (Link + Publish Date)."

Standalone mode: append the launched entity IDs + dates to the local launch report instead.

---

## Related Skills

- `03-strategy/creative-brief` — the approved brief this launch executes
- `05-analysis/campaign-setup` — companion skill: architecture, naming, budgets, kill rules (designed there, executed here)
- `05-analysis/ad-analysis` — after 3–5 days of delivery
- `04-production/static-production` / `04-production/video-production` — asset sources
