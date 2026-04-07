# Meta Ads — Campaign Parameters

## Level Structure

```
Campaign → Objective + Budget (optional)
  └── Ad Set → Audience + Placement + Budget + Bidding
        └── Ad → Creative + CTA + URL
```

---

## Campaign Level

### Available Objectives

| Objective | When to use | Algorithm optimization |
|---|---|---|
| **Awareness** | Brand awareness, maximum reach | Impressions / Reach |
| **Traffic** | Drive visitors to the site | Link clicks / Landing page views |
| **Engagement** | Interactions, video views, messages | Engagement actions |
| **Leads** | Native Meta forms or site forms | Leads (form or pixel) |
| **App Promotion** | App downloads | App installs / In-app events |
| **Sales** | Site conversions, product catalog | Purchases / Add to cart / other pixel events |

**Rule:** Always choose the objective lowest in the funnel that the budget can properly fuel.
→ If CPA target = 30€ and budget = 10€/day: optimize on "Add to Cart" or "Leads", not "Purchase" (not enough events for the algorithm).
→ **Stability threshold:** 50 events / week on the optimized event.

### Advantage Campaign Budget (ACB)
Automatically distributes budget across ad sets.
→ Use in scale phase only. In testing: fixed budget per ad set to control exposure.

---

## Ad Set Level

### Audience Types

#### Core Audience (Manual targeting)
- **Demographics:** age, gender, location, language
- **Interests:** interest categories, behaviors, liked pages
- **Behaviors:** online purchases, device users, travelers…
- **Tip:** In 2024–2026, broad audiences (country + age) often outperform precise interests thanks to the algorithm. Test both.

#### Custom Audience
Available sources:
| Source | What it targets |
|---|---|
| Website (Pixel) | Visitors, specific pages, events (30/60/90/180d) |
| Video | Views at 25% / 50% / 75% / 95% |
| Instagram account / Facebook Page | Engaged (interactions, messages, profile visited) |
| Lead Form | People who opened / submitted a form |
| Customer list (CRM) | Email / phone uploaded and matched |
| Catalog | People who viewed / added to cart / purchased products |

#### Lookalike Audience
- Based on a source Custom Audience
- Size: 1% (very similar) → 10% (broader)
- **Recommended:** LAL 1–2% buyers or qualified leads
- **Minimum source size:** 100 matched people (recommended: 500–1000+)

#### Advantage+ Audience (Meta AI)
Meta automatically chooses the audience based on the creative and history.
→ Test in parallel with manual audiences on a test budget.

---

### Placements

#### Automatic Placements (Advantage+)
Meta optimizes across all available placements.
→ **Recommended default** — allows the algorithm to find the cheapest inventory.

#### Manual Placements — Meta Inventory

| Placement | Format | Notes |
|---|---|---|
| Facebook Feed | Image, Video, Carousel | Audience 25–45+, high intent |
| Instagram Feed | Image, Video, Carousel | Audience 18–35, very visual |
| Instagram Reels | Video 9:16 | Strong organic reach, low cost |
| Facebook Reels | Video 9:16 | FB audience, good reach |
| Stories IG / FB | Video or Image 9:16 | Immersive, full screen format |
| Audience Network | Image, Video | Third-party apps — low CPM, variable quality |
| Messenger | Image, Video | Less used, can surprise |
| Facebook Marketplace | Image | High shopping intent |

**When to exclude manually:** Audience Network if CPA > target (low traffic quality).

---

### Bidding Strategies

| Strategy | How it works | When to use |
|---|---|---|
| **Lowest Cost** (default) | Meta spends the budget optimizing cost per result | Test phase, discovery |
| **Cost Cap** | Meta targets a CPA — slows spend if cost > cap | Scale phase with stable CPA |
| **Bid Cap** | Cap on each individual bid | Strict control, advanced scale |
| **Highest Value** | Optimizes for highest purchase value | E-commerce with catalog, LTV focus |
| **Minimum ROAS** | Spends only if ROAS meets the threshold | Mature e-commerce, large catalog |

**Starting rule:** Start with Lowest Cost. Switch to Cost Cap only after 50+ conversions / week with stable CPA.

---

### Budget and Scheduling

| Parameter | Recommendation |
|---|---|
| Daily budget | Minimum 5–10× the CPA target to exit the learning phase |
| Total budget (lifetime) | For promotions or tests with a deadline |
| Period | No end date in test phase — avoids CPM spikes at period end |
| Hourly scheduling | Rarely useful — let Meta optimize except specific cases (B2B, precise hours) |

**Learning phase:** 50 optimized events in 7 days. Avoid modifications during this phase.

---

## Ad Level

### Creative Formats and Specs

| Format | Recommended ratio | Min resolution | Max duration | Max size |
|---|---|---|---|---|
| Image Feed | 1:1 or 4:5 | 1080×1080 | — | 30 MB |
| Video Feed | 4:5 or 1:1 | 1080×1350 | 240 min (recommended < 60s) | 4 GB |
| Stories / Reels | 9:16 | 1080×1920 | 60s (Stories) / 90s (Reels) | 4 GB |
| Carousel | 1:1 | 1080×1080 | — per card | 30 MB/card |
| Collection | 1:1 + hero image | 1080×1080 | — | 30 MB |

**Text overlay:** Meta recommends < 20% of image as text. Beyond that: potential reduced reach.
**Primary text:** 125 characters recommended (truncated after)
**Headline:** 40 characters recommended
**Description:** 30 characters recommended

### Available CTAs (selection)

| CTA | Usage |
|---|---|
| Learn More | TOF, discovery |
| Sign Up | Lead gen, event |
| Shop Now | BOF, e-commerce |
| Download | App, resource |
| Get Quote | B2B, service |
| Book Now | Service, event |
| Contact Us | B2B, local |
| Watch More | Content, video |

---

## Pixel and Events

### Standard Events (funnel order)

| Event | Priority | Trigger |
|---|---|---|
| PageView | Always | All pages |
| ViewContent | Recommended | Product page |
| AddToCart | Recommended | Cart button |
| InitiateCheckout | Recommended | Checkout page |
| AddPaymentInfo | Optional | Payment entry |
| Purchase | Critical | Order confirmation |
| Lead | Critical | Form submission |
| CompleteRegistration | Recommended | Account registration |

**Verification:** Use Meta Pixel Helper (Chrome extension) to validate events.

---

## Meta Advertising Policies (Key Points)

- **Health claims:** Before/after body images prohibited. Weight loss claims heavily regulated.
- **Finance:** Mandatory disclaimer for certain financial products. Cryptocurrencies = approval required.
- **Alcohol:** Minimum age targeting required by country.
- **Discriminatory text:** Prohibited to target or exclude based on protected characteristics.
- **Artificial urgency:** "Offer expires in 1h" without a real deadline = risk of rejection.
- **Shocking content:** Overly graphic images, gore, nudity = automatic rejection.

**Official resource:** facebook.com/policies/ads
