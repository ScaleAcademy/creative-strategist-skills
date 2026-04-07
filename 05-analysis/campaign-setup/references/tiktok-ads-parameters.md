# TikTok Ads — Campaign Parameters

## Level Structure

```
Campaign → Objective + Budget
  └── Ad Group → Audience + Placement + Budget + Bidding + Schedule
        └── Ad → Creative + CTA + URL + TikTok Profile
```

---

## Campaign Level

### Available Objectives

| Objective | Category | When to use |
|---|---|---|
| **Reach** | Awareness | Maximize unique impressions |
| **Video Views** | Awareness | Maximize video views (2s or 6s) |
| **Community Interaction** | Consideration | Followers, profile visits |
| **Traffic** | Consideration | Clicks to site |
| **App Promotion** | Consideration | Downloads / in-app events |
| **Lead Generation** | Conversion | Native TikTok forms |
| **Website Conversions** | Conversion | Conversions tracked via Pixel |
| **Product Sales** | Conversion | TikTok Shop product catalog |

**TikTok specificity:** TikTok's algorithm is very powerful on broad audiences. Precise interests work less well than on Meta — let the algorithm work with strong creatives.

---

## Ad Group Level

### Audience Types

#### Automatic Audience (Broad)
TikTok automatically targets based on the creative and objective.
→ **Recommended for testing** on TikTok — the algorithm excels at broad targeting.

#### Custom Audience
| Source | What it targets |
|---|---|
| Site pixel | Visitors, events (7/14/30/60/180d) |
| Video engagement | Views at 2s / 6s / 25% / 50% / 75% / 100% |
| TikTok profile | Followers, interactions, visits |
| Customer file | Email / IDFA uploaded |
| App activity | In-app events |
| Lead gen | People who submitted a form |

#### Lookalike
- Size: 1% / 2% / 5% / 10% / 15% / 20%
- Recommended source: buyers or qualified leads
- Minimum source size: 100 people (recommended 1,000+)

#### Manual Targeting
| Parameter | Options |
|---|---|
| Age | 13–17 / 18–24 / 25–34 / 35–44 / 45–54 / 55+ |
| Gender | All / Male / Female |
| Location | Country, region, city |
| Language | Device language |
| Interests | Broad categories (beauty, finance, fitness, gaming…) |
| Behaviors | Interactions with creators, hashtags, sounds |
| Devices | iOS / Android, carriers, connection |

---

### Placements

| Placement | Description |
|---|---|
| **TikTok Feed** | Main — full screen video in the For You Page |
| **TikTok Search** | TikTok search results |
| **Pangle** | Partner network (third-party apps) |
| **Global App Bundle** | Inventory outside TikTok |

**Recommendation:** TikTok Feed only for testing. Add Pangle at scale if TikTok CPM increases.

---

### Bidding Strategies

| Strategy | How it works | When to use |
|---|---|---|
| **Lowest Cost** (default) | Spends budget at minimum cost | Test phase |
| **Cost Cap** | Targets a CPA or CPM | Scale with stable CPA |
| **Bid Cap** | Cap on each bid | Strict advanced control |
| **Value Optimization** | Maximizes purchase value | E-commerce with catalog |

**TikTok learning phase:** 50 optimized events in 7 days. More sensitive to modifications than Meta.

---

### Budget

| Parameter | Minimum | Recommended |
|---|---|---|
| Campaign daily budget | 50€ | 100€+ for testing |
| Ad group daily budget | 20€ | 50€+ |
| Total budget (lifetime) | — | For dated promotions |

**Important:** TikTok requires higher budgets than Meta to exit the learning phase quickly. Budget too low = unreliable data.

---

## Ad Level

### Formats and Specs

| Format | Ratio | Resolution | Duration | Max size |
|---|---|---|---|---|
| In-Feed Video | 9:16 (recommended) / 1:1 / 16:9 | 720×1280 min | 5–60s (recommended 15–30s) | 500 MB |
| TopView | 9:16 | 720×1280 min | 5–60s | 500 MB |
| Spark Ads | Matches organic post format | — | Original post duration | — |
| Collection Ads | 9:16 + product cards | 720×1280 | 5–60s | 500 MB |
| Lead Gen | 9:16 | 720×1280 | 5–60s | 500 MB |

**Text:** Description: 1–100 characters (55 recommended before cutoff)
**Hashtags:** Allowed in description (optional)
**Displayed profile:** Business TikTok account required and associated

### Spark Ads — Organic Boosting
Allows boosting an existing organic video (your account or a partner creator).
→ **Key advantage:** preserves the original post's comments, likes, shares = visible social proof.
→ Requires an authorization code from the creator (valid 30 or 60 days).
→ Ideal for UGC Creator Partnerships.

### Available CTAs

| CTA | Usage |
|---|---|
| Shop Now | E-commerce |
| Learn More | TOF, discovery |
| Sign Up | Lead gen |
| Download | App |
| Book Now | Service |
| Contact Us | B2B, local |
| Get Quote | Service |
| Subscribe | Content, SaaS |

---

## TikTok Pixel and Events

### Installation
Via TikTok Events Manager — JS pixel on the site + Conversions API (Server-Side) recommended.

### Standard Events

| Event | Priority |
|---|---|
| PageView | Always |
| ViewContent | Recommended |
| AddToCart | Recommended |
| InitiateCheckout | Recommended |
| PlaceAnOrder | Critical |
| CompletePayment | Critical |
| SubmitForm | Critical (lead gen) |

**Conversions API:** Strongly recommended — improves matching and reduces the impact of iOS 14+.

---

## TikTok Creative Specifics

### What Performs
- **Native first:** The video must look like organic TikTok content — not an ad.
- **Hook < 3s:** TikTok is even more brutal than Meta on first-second retention.
- **Sound ON:** 93% of TikTok users watch with sound. Design for sound first.
- **Native vertical:** Always 9:16. Never letterbox or black bars.
- **Native text overlay:** TikTok style (subtitles, dynamic captions) > "advertising" style.
- **UGC Creators:** Spark Ads via creators often outperform brand ads.

### What Fails
- Overly produced / too "corporate" video
- Visible watermark logo (signals an ad)
- Too aggressive call-to-action in the first 5 seconds
- Recycling a Meta 4:5 video on TikTok without adapting it

---

## TikTok Advertising Policies (Key Points)

- **Alcohol, tobacco, gambling:** Heavily regulated — approval required by country.
- **Health / medication:** Strict claims, before/after body shots very risky.
- **Finance:** Mandatory disclaimer by product and country.
- **Minors:** Targeting 13–17 prohibited for many categories.
- **Music rights:** Use only TikTok's Commercial Music Library for ads.

**Official resource:** ads.tiktok.com/help/
