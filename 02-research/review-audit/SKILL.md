---
name: review-audit
description: "Mines customer reviews to extract verbatims, pain points, triggers, objections, and ad-ready phrases. Use after brand-guidelines to build the raw material for hooks and copy. Trigger on: 'mine reviews', 'customer verbatims', 'what are customers really saying', 'language mining'. Produces a structured verbatim library organized by theme."
metadata:
  version: 1.0.0
  status: stable
  tags: [research, verbatims, voc, copywriting, hooks]
  inputs: [Amazon / Trustpilot / Google product URL, or raw verbatims pasted directly]
  outputs: [verbatim library — 5 buckets, ad-ready phrases highlighted]
  depends-on: [brand-guidelines]
---

# Review Audit

## Before Starting

Confirm before starting:
- [ ] Access to reviews (Trustpilot / Amazon / Google URL or verbatims pasted directly)
- [ ] Product or targeted category clearly defined
- [ ] Minimum 20 reviews available (ideally 50+)
- [ ] `brand-context.md` available to contextualize extractions

If fewer than 20 reviews available: also use Meta comments (see alternative sources in the reference).

For full sources: See [references/sources.md](references/sources.md)

---

## Phase 1: Raw Collection

Collect all available reviews.
**Do not filter now.** Copy-paste raw.

Prioritize long reviews (200+ words) — they contain the most Layer 3 content.

---

## Phase 2: Scoring

Assign a score to each review:

| Score | Criteria |
|---|---|
| 5 — Gold | Long, emotional, specific, contains a before/after |
| 4 — Strong | Detailed, mentions a specific situation or emotion |
| 3 — Medium | Generic but useful to confirm a pattern |
| 2 — Weak | Short, vague, not actionable |
| 1 — Useless | "Great product", "fast delivery", no content |

**Analyze only scores 4–5.** Scores 2–3 serve to confirm patterns, not to extract.

---

## Phase 3: Extraction by Bucket

Classify each 4–5 verbatim into one of the 5 buckets:

### Bucket 1 — Pain Before
What the customer was experiencing BEFORE buying.
> Signal: "before", "I couldn't take it anymore", "I had tried everything", "for years"

### Bucket 2 — Purchase Triggers
What triggered the decision to act.
> Signal: "the day", "I decided", "when I saw", "someone recommended"

### Bucket 3 — Pre-Purchase Objections
What almost prevented them from buying.
> Signal: "I was afraid that", "I hesitated because", "I thought it wouldn't work"

### Bucket 4 — Transformations
How their life changed after.
> Signal: "now", "since", "I never would have believed", "it changed everything"

### Bucket 5 — Ad-Ready Phrases ⭐
Formulations directly usable in a hook or headline — with little or no modification.

**Qualification criteria for Bucket 5:**
A phrase deserves Bucket 5 if it meets at least 3 of these 5 criteria:
- [ ] Reads like something a human would say to a friend (not marketing speak)
- [ ] Contains a named emotion or strongly implied one
- [ ] Is specific to a concrete situation (not generic)
- [ ] Creates natural curiosity or tension
- [ ] Uses the persona's exact language — no marketing words

**Placement rule:** Phrases that meet these criteria go ONLY in Bucket 5, not scattered in other buckets. They can be extracted from any source bucket (1, 2, 3, or 4).

**Examples of Bucket 5 phrases:**
- ✅ "I couldn't take getting up in the morning wondering what the point was."
- ✅ "It's the first time I don't feel judged for what I eat."
- ✅ "I was so ashamed to talk about it with my doctor."
- ❌ "The product is excellent and I recommend it to everyone." → Bucket 3 or discard
- ❌ "Fast delivery, very satisfied." → Score 1, discard

---

## Phase 4: Identify Patterns

After extraction, note:
- Which pain points recur most often? (top 3)
- Which trigger is most frequent?
- Which objection is most blocking?
- Which transformation is most desired?
- Are there recurring words or expressions?

---

## Output Format

```markdown
# Verbatim Library — [Product] — [Date]
*Sources: [Trustpilot / Amazon / etc.] | Reviews analyzed: [X] | Scores 4–5: [Y]*

## Bucket 1 — Pain Before
- "[Exact verbatim]" — Score [4/5]
- "[Exact verbatim]" — Score [4/5]

## Bucket 2 — Purchase Triggers
- "[Exact verbatim]" — Score [4/5]

## Bucket 3 — Pre-Purchase Objections
- "[Exact verbatim]" — Score [4/5]

## Bucket 4 — Transformations
- "[Exact verbatim]" — Score [4/5]

## Bucket 5 — Ad-Ready Phrases ⭐
- "[Formulation directly usable as a hook]"
- "[Formulation directly usable as a hook]"

## Identified Patterns
Dominant pain: [summary]
Most frequent trigger: [summary]
Main objection: [summary]
Most desired transformation: [summary]
Recurring words: [list]
```

---

## Related Skills

- `01-audit/brand-guidelines` — prerequisite
- `02-research/audience-research` — verbatims feed the persona's Layer 3
- `02-research/customer-reality` — triggers feed micro-moment mapping
- `03-strategy/hook-writing` — Bucket 5 directly usable as hook base
- `03-strategy/creative-brief` — Buckets 1 and 4 feed the brief angle and promise
