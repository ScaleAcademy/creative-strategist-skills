---
name: brand-research
description: "Extracts complete brand intelligence via web search across 7 phases and outputs a structured brand-research-brief.json. Use after brand-guidelines when you need deep competitive, product, and founder data to fuel creative production. Trigger on: 'research the brand', 'build a research brief', 'brand deep dive', 'I need brand intelligence'. Requires brand URL and hero product. Output uploads to Project Knowledge and feeds brand-specs, audience-research, and creative-brief."
metadata:
  version: 1.0.0
  status: beta
  tags: [audit, brand, research, intelligence, web-search]
  inputs: [brand URL, brand name, hero product name]
  outputs: [brand-research-brief.json]
  depends-on: [brand-guidelines]
---

# Brand Research

## Before Starting

Confirm before starting:
- [ ] `brand-context.md` exists (otherwise launch `brand-guidelines` first)
- [ ] Brand URL available
- [ ] Hero product identified (or use "FLAGSHIP" as default)
- [ ] If brand guidelines PDF exists → upload to Project Knowledge before running this skill

---

This skill extracts every piece of usable information from a brand's public presence so that downstream skills (creative briefs, hooks, static production) can operate without needing follow-up questions.

**Input:** Brand URL + brand name + hero product
**Output:** `brand-research-brief.json` — uploaded to Project Knowledge

---

## Phase 1: Brand Identity & Visual System

Search the web for:
- `"[Brand] brand guidelines pdf"`
- `"[Brand] press kit"` or `"media kit"`
- `"[Brand] design agency case study"`
- `"[Brand] font"`
- `"[Brand] hex color codes"`

Visit the brand URL and analyze.

**Output JSON block:**
```json
{
  "brand_identity": {
    "name": "",
    "tagline": "",
    "mission_statement": "",
    "design_agency": "",
    "voice_adjectives": [],
    "tone_notes": "",
    "banned_language": ""
  },
  "visual_system": {
    "primary_font": "",
    "secondary_font": "",
    "primary_color_hex": "",
    "secondary_color_hex": "",
    "accent_color_hex": "",
    "background_preference": "",
    "imagery_style": "",
    "ui_shapes": "",
    "logo_url_or_description": ""
  }
}
```

---

## Phase 2: Product Intelligence

Search the web for:
- `"[Brand] [Product] ingredients"` or `"[Brand] [Product] specs"`
- `"[Brand] vs [competitor]"`
- `"[Brand] review"` on Reddit, Amazon, TrustPilot

**Output JSON block:**
```json
{
  "product_details": {
    "product_name": "",
    "product_type": "",
    "price": "",
    "price_per_unit_or_serving": "",
    "hero_claim": "",
    "how_it_works": "",
    "key_ingredients_or_specs": [{"name": "", "benefit": ""}],
    "form_factor": "",
    "usage_instructions": "",
    "offer_details": {
      "current_offer": "",
      "subscription_discount": "",
      "free_shipping_threshold": "",
      "guarantee": ""
    }
  }
}
```

---

## Phase 3: Proof Points & Social Proof

Search the web for:
- `"[Brand] clinical study"`
- `"[Brand] reviews"`
- `"[Brand] before and after"`
- `"[Brand] featured in"`

**Output JSON block:**
```json
{
  "statistics_and_data": [{"stat": "", "source": "", "context": ""}],
  "press_mentions": [{"publication": "", "quote_or_headline": "", "date": ""}],
  "testimonials": [{"quote": "", "name": "", "detail": ""}],
  "review_metrics": {"average_rating": "", "total_reviews": "", "platform": ""},
  "notable_endorsements": [],
  "certifications_or_badges": []
}
```

---

## Phase 4: Transformation & Pain Points

No specific search required — synthesize from Phases 1–3 and brand URL analysis.

**Output JSON block:**
```json
{
  "customer_pain_points": [{"pain": "", "intensity": "mild/moderate/severe", "current_bad_solution": ""}],
  "transformation_claims": [{"before_state": "", "after_state": "", "timeframe": "", "proof_type": ""}],
  "emotional_triggers": [],
  "target_audience": {"primary_demo": "", "psychographic": "", "life_stage": ""}
}
```

---

## Phase 5: Competitive Positioning

Search the web for:
- `"[Brand] vs"`
- `"[Brand] alternative"`

**Output JSON block:**
```json
{
  "competitive_landscape": {
    "top_competitors": [{"name": "", "price": "", "key_weakness": "", "common_comparison_point": ""}],
    "unique_differentiators": [],
    "category_conventions": "",
    "us_vs_them_angles": [{"them": "", "us": "", "why_it_matters": ""}]
  }
}
```

---

## Phase 6: Founder & Origin Story

Search the web for:
- `"[Brand] founder"`
- `"[Brand] founder interview"`
- `"[Brand] origin story"`

**Output JSON block:**
```json
{
  "founder_story": {
    "founder_name": "",
    "founder_title": "",
    "origin_hook": "",
    "personal_pain_point": "",
    "credibility_marker": "",
    "quotable_moment": "",
    "mission_beyond_product": ""
  }
}
```

---

## Phase 7: Ad-Ready Hooks & Angles

Synthesize all previous phases into pre-formatted hook banks by ad format.

**Output JSON block:**
```json
{
  "ad_hooks": {
    "before_after": [],
    "bullet_points": [],
    "negative_marketing": [],
    "news_hooks": [],
    "handwriting_hooks": [],
    "us_vs_them_hooks": [],
    "statistic_hooks": [],
    "social_proof_hooks": [],
    "press_hooks": [],
    "testimonial_hooks": [],
    "founder_story_hooks": [],
    "features_benefits_hooks": [],
    "ugc_hooks": [],
    "carousel_angles": [],
    "new_format_hooks": []
  }
}
```

---

## Deliver

Merge all 7 phase outputs into a single `brand-research-brief.json` and upload to Project Knowledge.

> "Here's your Brand Research Brief. It covers identity, product, proof, pain points, competitive positioning, founder story, and pre-built hooks across 15 formats. Ready for brand-specs generation or creative briefing."

---

## Related Skills

- `01-audit/brand-guidelines` — prerequisite: brand context must exist first
- `01-audit/brand-specs` — next step: generate visual spec cards from this brief
- `02-research/audience-research` — deepen persona work using pain points and audience data
- `03-strategy/creative-brief` — downstream: uses brand intelligence for brief creation
