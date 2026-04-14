# Windsor.ai — MCP Setup + Naming Convention

## What is Windsor.ai?

Windsor.ai is a marketing data aggregator that directly connects Meta Ads (and other platforms) to Claude via the MCP (Model Context Protocol). It allows Claude to query performance data in real time without manual exports.

**Result:** Claude can analyze your Meta Ads account like an analyst with direct interface access — no copy-pasting data.

---

## Section 1: Connecting Windsor.ai MCP to Claude

### Step 1 — Create a Windsor.ai account

- Go to [windsor.ai](https://windsor.ai)
- Create an account (free plan available with limits)
- Connect your Meta Ads account in the Windsor.ai dashboard

### Step 2 — Get your Windsor API key

In the Windsor.ai dashboard:
- Go to **Settings > API**
- Copy the API key (format: `wai_xxxxxxxxxxxx`)

### Step 3 — Configure Claude Desktop

Open the Claude Desktop configuration file:
- **Mac:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Add the MCP configuration:

```json
{
  "mcpServers": {
    "windsor": {
      "command": "npx",
      "args": ["-y", "@windsor-ai/mcp-server"],
      "env": {
        "WINDSOR_API_KEY": "wai_YOUR_API_KEY_HERE"
      }
    }
  }
}
```

### Step 4 — Restart Claude Desktop

Fully close and relaunch Claude Desktop.
A Windsor icon should appear in the toolbar.

**Connection test:**
```
List the Meta Ads accounts available via Windsor.ai
```

If Claude lists your accounts → connection successful.

---

## Section 2: Naming Convention

The naming convention is **optional but strongly recommended**. It allows Claude to analyze performance by angle, format, and mechanic directly from campaign/ad set/creative names — without manual categorization.

For the complete naming convention reference: see [references/naming-convention.md](../../../references/naming-convention.md)

### Quick Reference

**Campaign:** `[BRAND]_[OBJECTIVE]_[BUDGET_TYPE]`
Example: `MARCA_ACQ_CBO`

**Ad Set:** `[BRAND]_[AUDIENCE_TYPE]_[AUDIENCE_DESCRIPTION]`
Example: `MARCA_COLD_BROAD-25-45F`

**Ad:** `[BRAND]_[ANGLE]_[FORMAT]_[STYLE]_[RATIO]_v[X]_[YYYYMM]`
Example: `MARCA_PR_VID30_UGC_916_v1_202604`

### Angle Codes
| Code | Meaning |
|---|---|
| PR | Problem (C1) |
| RS | Result / Proof (C2) |
| ED | Education (C3) |
| ID | Identity (C4) |

### Format Codes
| Code | Meaning |
|---|---|
| VID15 | 15-second video |
| VID30 | 30-second video |
| VID60 | 60-second video |
| STA | Static (image) |
| CAR | Carousel |

### Style Codes
| Code | Meaning |
|---|---|
| UGC | User Generated Content |
| TH | Talking Head |
| BROLL | B-Roll + voiceover |
| TEXT | Animated text |
| SKIT | Skit / Staged scene |

### Why this convention?

When the convention is applied, Claude can:
- Calculate the average CPA by angle (PR vs RS vs ED vs ID) in a single query
- Compare formats (VID15 vs VID30 vs STA) without manual sorting
- Identify which style produces the best results
- Track an angle's progression over time (v1 → v2 → v3)

Without convention → creative analysis = manual sorting = wasted time.

---

## Compatible Platforms with Windsor.ai

Windsor.ai also supports (in addition to Meta):
- Google Ads
- TikTok Ads
- Snapchat Ads
- Pinterest Ads
- LinkedIn Ads

The same analysis logic can be applied to these platforms by adapting the key metrics (see the reference files in `04-production/campaign-setup/references/`).
