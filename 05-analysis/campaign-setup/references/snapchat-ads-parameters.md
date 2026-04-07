# Snapchat Ads — Campaign Parameters

## Context

Snapchat Ads is relevant for audiences aged 13–34 (core target).
Snapchat reaches ~20M monthly active users in France, heavily concentrated on the 15–30 age group.
Generally lower CPM than Meta — a good option for TOF reach on a controlled budget.

---

## Level Structure

```
Campaign → Objective + Budget
  └── Ad Set → Audience + Placement + Budget + Bidding
        └── Ad → Creative + CTA + URL
```

---

## Campaign Level

### Available Objectives

| Objective | Category | When to use |
|---|---|---|
| **Brand Awareness** | Awareness | Maximum impressions |
| **Video Views** | Awareness | 2s or 15s views |
| **Traffic** | Consideration | Clicks to site |
| **App Installs** | Consideration | App downloads |
| **Engagement** | Consideration | Content interactions |
| **Lead Generation** | Conversion | Native Snap forms |
| **Conversions** | Conversion | Snapchat Pixel — purchases / leads |
| **Catalog Sales** | Conversion | Product catalog |

---

## Ad Set Level

### Audience Types

#### Predefined Audiences (Snap)
Pre-built audiences by Snapchat based on in-app behavior:
- Lifestyle (fitness, beauty, gaming, fashion, food…)
- Life Moments (wedding, moving, birth…)
- Shopper (purchasing behaviors)
- Viewer (types of content consumed)

#### Custom Audiences
| Source | What it targets |
|---|---|
| Site pixel | Visitors, events (7/14/28/60/90/180d) |
| Snap engagement | Interactions with your paid Stories |
| Snap Lookalike | Similar to a source Custom Audience |
| Customer List | Uploaded emails / phone numbers |
| App Activity | In-app events (via SDK) |

#### Lookalike
- Size: Narrow / Balanced / Broad
- Recommended source: buyers or leads
- Minimum source size: 300 matched (recommended 1000+)

#### Manual Targeting
| Parameter | Options |
|---|---|
| Age | 13–17 / 18–20 / 21–24 / 25–34 / 35+ / Custom |
| Gender | All / Male / Female |
| Location | Country, region, city, radius |
| Language | Device language |
| Device | iOS / Android |
| Carrier | Mobile network |
| Interests | Snap categories |

---

### Placements

| Placement | Description |
|---|---|
| **Snap Ads (Between Stories)** | Full screen between friends' / publishers' Stories |
| **Story Ads** | Thumbnail in the Discover section — opens a mini-Story |
| **Collection Ads** | Product carousel under a video |
| **Dynamic Ads** | Automated product catalog |
| **Commercials** | Non-skippable 6s in Snap Shows (selected publishers) |
| **AR Lenses** | Sponsored AR filters (high budget, branding) |

**Recommended for paid social:** Snap Ads (Between Stories) — most common and most tested format.

---

### Bidding Strategies

| Strategy | How it works | When |
|---|---|---|
| **Auto-Bid** (default) | Optimizes automatically | Testing, start |
| **Target Cost** | Targets a CPA or CPM | Scale with stable CPA |
| **Max Bid** | Cap on each bid | Strict control |

---

### Budget

| Parameter | Minimum |
|---|---|
| Daily budget | 5€ (recommended 20€+ for reliable data) |
| Total budget | For dated promotions |

---

## Ad Level

### Formats and Specs

| Format | Ratio | Resolution | Duration | Max size |
|---|---|---|---|---|
| Snap Ad (video) | 9:16 | 1080×1920 | 3–180s (recommended 3–15s) | 1 GB |
| Snap Ad (image) | 9:16 | 1080×1920 | — | 5 MB |
| Story Ad | 9:16 | 1080×1920 | 3–180s per card | 1 GB |
| Collection | 9:16 + thumbnails | 1080×1920 | 3–180s | 1 GB |
| Commercial | 9:16 | 1080×1920 | 6s (non-skip) / 3–180s (skip) | 1 GB |

**Safe Zones:** Avoid critical text in the top and bottom 15% of the image (Snap UI covers these areas).
**CTA Swipe-Up:** Attached link — swipe up triggers opening the site or app.

### Headline and CTA

| Field | Limit |
|---|---|
| Brand Name | 25 characters |
| Headline | 34 characters |
| CTA | Selection from a predefined list |

### Available CTAs
Discover / Shop / Book / Download / Learn More / Sign Up / Watch / Install

---

## Snapchat Pixel and Events

### Standard Events

| Event | Trigger |
|---|---|
| PAGE_VIEW | All pages |
| VIEW_CONTENT | Product page |
| ADD_TO_CART | Cart button |
| START_CHECKOUT | Checkout page |
| PURCHASE | Order confirmation |
| SIGN_UP | Registration |
| LEAD | Form submitted |

**Snap Conversions API:** Recommended to improve matching post-iOS 14.

---

## Snapchat Creative Specifics

### What Performs
- **Native full screen 9:16**: no black bars, fill the entire screen
- **Hook < 2s**: the Snap audience swipes even faster than TikTok
- **Sound ON**: immersive format, design with music and voice
- **Native UGC style**: look like organic Snap content — not a TV ad
- **Clear swipe-up**: verbally say "swipe up" or display an arrow
- **Subtitles**: always, for the soundless seconds

### What Fails
- Video in 16:9 or with letterbox
- No clearly identifiable CTA
- Too much text (young audience, very fast consumption)
- Too corporate or "classic advertising" tone

---

## Snapchat Advertising Policies (Key Points)

- **Alcohol / tobacco / vaping:** Heavily regulated — 18+ targeting required, approval needed.
- **Adult content:** Prohibited except very regulated special categories.
- **Minors:** Targeting 13–17 = strong restrictions (no behavioral targeting, no alcohol, no gambling).
- **Finance / Crypto:** Approval required.
- **Health claims:** Same restrictions as Meta.

**Official resource:** businesshelp.snapchat.com/s/article/ad-policies
