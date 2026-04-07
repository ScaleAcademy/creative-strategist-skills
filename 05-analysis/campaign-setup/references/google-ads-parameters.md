# Google Ads — Campaign Parameters

## Campaign Types

| Type | Network | Primary usage |
|---|---|---|
| **Search** | Google results (text) | High intent — prospect actively searching |
| **Performance Max** | All Google channels | Unified AI campaign — advanced scale |
| **Display** | Partner sites (GDN) | Retargeting, awareness |
| **YouTube** | YouTube (video) | TOF video, awareness |
| **Shopping** | Google Shopping | E-commerce, product catalog |
| **App** | All surfaces | App acquisition |
| **Smart** | Automatic | Local, simplified (not recommended for paid social) |

**Creative Strategist context:** YouTube Ads and Display are most relevant for paid social. Search = pure intent, managed by the media buyer. Performance Max = both combined.

---

## YouTube Ads

### Video Formats

| Format | Skippable | Duration | Placement | Billed |
|---|---|---|---|---|
| **In-Stream Skippable** | After 5s | 12s–3min (recommended 15–30s) | Before / during / after video | CPV (30s view or interaction) |
| **In-Stream Non-Skippable** | No | 15–20s max | Before / during video | CPM |
| **Bumper Ads** | No | Max 6s | Before video | CPM |
| **In-Feed (Discovery)** | — | Any | YouTube results, homepage | CPC (thumbnail click) |
| **Outstream** | — | — | Partner sites (outside YouTube) | Viewable CPM |
| **Masthead** | — | Up to 30s | YouTube homepage | CPD (reservation) |

**Most used in paid social:** In-Stream Skippable (15–30s) and Bumper 6s.

### In-Stream Skippable Structure

```
0–5s → Absolute hook (before the "Skip" button)
5–15s → Tension / development
15–25s → Pivot / solution
25–30s → CTA
```

**5-second rule:** If the hook doesn't capture before the skip, the view will never be counted as a view. Same logic as Meta but with the visible "Skip" button.

---

## Google Audiences

### Audience Types

| Type | Description |
|---|---|
| **Affinity** | Broad interest groups (e.g. "Cooking enthusiasts") |
| **Custom Intent** | Keywords the audience has recently searched |
| **In-Market** | People actively looking to purchase in a category |
| **Remarketing** | Site visitors / video views / CRM list |
| **Similar Audiences** | Lookalike based on your remarketing audiences |
| **Detailed Demographics** | Family status, homeowner, education level, income |
| **Custom Combinations** | Overlay of multiple criteria |

### Most Effective Audiences by Phase

| Phase | Recommended audience |
|---|---|
| TOF | Affinity + Custom Intent (category keywords) |
| MOF | In-Market + Custom Intent (brand + competitors) |
| BOF | Visitor remarketing (30d) + CRM list |

---

## Performance Max (PMax)

AI campaign covering Search, Display, YouTube, Gmail, Discover, Shopping simultaneously.

### What We Provide
- **Creative assets:** images (15–20), logos (1–5), videos (1–5), headlines (3–5), descriptions (2–5)
- **Audience signals:** CRM list, site visitors, custom intents
- **Conversion objective:** purchase, lead, etc.

### What Google Does
- Automatically assembles assets
- Tests combinations
- Distributes across all channels

**Advantage:** Maximum reach with minimal management.
**Disadvantage:** Little control over where and how assets are used. Limited creative reporting.

**Tip:** Create thematic Asset Groups (1 angle = 1 asset group) to isolate performance.

---

## Google Bidding Strategies

| Strategy | How it works | When |
|---|---|---|
| **Maximize Clicks** | Max clicks within budget | Traffic testing, beginning |
| **Maximize Conversions** | Max conversions within budget | Free CPA |
| **Target CPA** | Targets a cost per conversion | Fixed CPA, stable volume |
| **Target ROAS** | Targets a return on spend | Mature e-commerce |
| **Target CPM** | Cost per 1000 impressions | YouTube awareness |
| **Max CPV** | Maximum cost per view | YouTube engagement |

**Google learning phase:** 30–50 conversions in 30 days for automated strategies (Target CPA / Target ROAS).

---

## Display Ads — Specs

### Responsive Display Ads (RDA)
Google automatically assembles assets:
- Images: up to 15 (ratio 1.91:1 and 1:1)
- Logos: up to 5
- Headlines: up to 5 (30 characters max)
- Descriptions: up to 5 (90 characters max)
- YouTube videos: up to 5 (optional)

### Fixed Display Formats (Legacy)
| Format | Dimensions |
|---|---|
| Leaderboard | 728×90 |
| Medium Rectangle | 300×250 |
| Large Rectangle | 336×280 |
| Half Page | 300×600 |
| Billboard | 970×250 |
| Mobile Banner | 320×50 |

---

## Google Pixel (Google Tag / GA4)

### Key Events to Track

| Event | Trigger |
|---|---|
| page_view | All pages |
| view_item | Product page |
| add_to_cart | Cart button |
| begin_checkout | Checkout page |
| purchase | Order confirmation |
| generate_lead | Form submission |

**Tool:** Google Tag Manager recommended for centralized management.
**Conversion Import:** Possible to import GA4 conversions into Google Ads.

---

## Google Advertising Policies (Key Points)

- **Finance:** Mandatory certification for certain products (credit, investments, crypto).
- **Health:** Strict claims on medications and supplements. Country-by-country approval.
- **Alcohol:** Regulated by country — opt-in required.
- **Misleading claims:** Strict prohibition — "the best", "number 1" without proof = risk of rejection.
- **Counterfeiting:** Zero tolerance.

**Official resource:** support.google.com/adspolicy
