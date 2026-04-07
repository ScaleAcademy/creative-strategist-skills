# LinkedIn Ads — Campaign Parameters

## Context

LinkedIn Ads is the go-to platform for B2B and precise professional targeting.
Highest CPM of all ad platforms (often 30–80€ CPM) — only justified if client LTV is high.
FR audience: 26M members, active in professional fields (tech, finance, HR, marketing, consulting, professional training).

**When to use LinkedIn Ads:**
- Target = professional decision-makers (job title, company size, industry)
- B2B product / service with deal > 1,000€
- Professional training, certification, recruiting
- Professional events

**When to avoid:** B2C, small basket, broad general public audiences — use Meta instead.

---

## Level Structure

```
Campaign Group → Objective + Budget + Dates
  └── Campaign → Audience + Format + Budget + Bidding
        └── Creative → Visual + Text + CTA + URL
```

---

## Available Objectives

| Objective | Category | When to use |
|---|---|---|
| **Brand Awareness** | Awareness | CPM — maximum impressions |
| **Video Views** | Awareness | Video views (ThruPlay) |
| **Engagement** | Consideration | Interactions, followers, shares |
| **Website Visits** | Consideration | Clicks to landing page |
| **Lead Generation** | Conversion | Native LinkedIn forms (Lead Gen Forms) |
| **Website Conversions** | Conversion | LinkedIn Pixel — tracked actions |
| **Job Applicants** | Recruiting | Job listings |

---

## Audience Targeting

### Professional Attributes (LinkedIn's Strength)

| Attribute | Options |
|---|---|
| **Industry** | 150+ industries (Tech, Finance, Health, Marketing, Consulting…) |
| **Company size** | 1–10 / 11–50 / 51–200 / 201–500 / 501–1000 / 1001–5000 / 5001–10000 / 10000+ |
| **Job title** | Exact title or category |
| **Function** | Marketing / Finance / HR / IT / Sales / Leadership / Operations… |
| **Seniority** | Intern / Junior / Senior / Manager / Director / VP / C-Suite / Owner |
| **Skills** | Skills listed in the profile |
| **Degrees** | Level and field of study |
| **Schools** | Universities / Specific schools |
| **Years of experience** | 1–2 / 3–5 / 6–10 / 10+ |
| **Specific companies** | Target specific companies (account-based) |
| **LinkedIn groups** | Members of thematic groups |

### LinkedIn Predefined Audiences
LinkedIn offers pre-built audiences:
- Influencers / Decision-Makers / C-Suite
- Specific industries (e.g. "Tech Professionals")

### Retargeting and Custom Audiences
| Source | Description |
|---|---|
| Site pixel | Visitors (7/30/90/180d) |
| Lead Gen Forms | Contacts who opened or submitted a form |
| Video | Views at 25% / 50% / 75% / 97% |
| Company account | Engaged with the page |
| Contact list | Uploaded email |
| Company list | Uploaded domains or company names (ABM) |

### LinkedIn Lookalike
- Based on a Custom Audience
- Minimum source size: 300 members

---

## Creative Formats

### Single Image Ad (Sponsored Content)
Most common format. Appears in the feed.

| Spec | Value |
|---|---|
| Image ratio | 1.91:1 (horizontal, recommended) or 1:1 (square) |
| Min resolution | 1200×628 (1.91:1) / 1200×1200 (1:1) |
| Max size | 5 MB |
| Intro text | 150 characters recommended (600 max) |
| Headline | 70 characters recommended (200 max) |
| Description | 100 characters (optional) |

### Video Ad
| Spec | Value |
|---|---|
| Ratio | 16:9 / 1:1 / 9:16 (vertical recommended on mobile) |
| Duration | 3s–30min (recommended 15–30s) |
| Max size | 200 MB |
| Subtitles | Required (majority watches without sound) |
| Intro text | 150 characters recommended |

### Carousel Ad
- 2–10 cards
- 1:1 ratio per card
- Title per card: 45 characters max

### Lead Gen Forms (LGF)
Native LinkedIn form — pre-filled with profile data.
→ Completion rate far superior to external forms.
→ Available fields: first name, last name, work email, company, title, phone, company size, industry, seniority.
→ Up to 3 custom questions.

### Message Ads (Sponsored InMail)
Direct message in the LinkedIn inbox.
→ Billed per send (CPS).
→ High open rate (50%+) but limited to 1 message / member / 30 days.
→ Text: 500 characters. CTA: 1 button.

### Conversation Ads
Interactive message with multiple choice buttons.
→ Allows conditional paths (if X → show Y).

### Document Ads
Shareable document (PDF, presentation) available for download.
→ Ideal for lead magnets (white paper, guide, case study).

### Text Ads
Small text + 100×100px image ads in the sidebar.
→ Low CPM but low visibility format — limited ROI.

---

## Bidding Strategies

| Strategy | Description | When |
|---|---|---|
| **Maximum Delivery** (default) | LinkedIn automatically optimizes | Testing, start |
| **Manual CPC** | Cost-per-click cap | Cost control |
| **Manual CPM** | Cost-per-1000-impressions cap | Controlled awareness |
| **Target CPL** | Targets a cost per lead | Scale Lead Gen Forms |

**Minimum budget:** 10€/day per campaign.
**Reality:** LinkedIn is expensive. CPC often 5–15€, CPL often 50–200€. Only justified if LTV > 1,000€ or complex B2B.

---

## LinkedIn Insight Tag (Pixel)

### Events to Track
| Event | Trigger |
|---|---|
| Page view | All pages |
| Lead | Form submitted |
| Purchase | Order confirmation |
| Key page view | Strategic pages (pricing, contact) |

**Conversion Tracking:** Link conversions to the Insight Tag to measure real CPL.

---

## LinkedIn Creative Specifics

### What Performs
- **Numbers and data**: the professional audience is analytical — "3× more leads in 90 days"
- **B2B social proof**: client company logos, decision-maker testimonials
- **Education + value**: insights, case studies, benchmarks — content that teaches something
- **Direct and professional tone**: not mass-market — speak as a peer
- **Short subtitled video**: majority watches without sound at the office
- **Lead Gen Forms**: minimal friction = often better CPL

### What Fails
- Too promotional / "salesy" tone
- No added value in the content
- Too aggressive CTA for an audience that doesn't yet have trust
- Too broad targeting for the LinkedIn CPM (budget burned quickly)

---

## LinkedIn Advertising Policies (Key Points)

- **Discriminatory content:** Prohibited (gender, race, religion, origin).
- **Unproven claims:** "The best", "number 1" without a source = risk of rejection.
- **Personal data:** GDPR compliance required on Lead Gen Forms.
- **Adult / offensive content:** Zero tolerance.

**Official resource:** linkedin.com/legal/ads-policy
