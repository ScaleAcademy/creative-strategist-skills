# Agent: Brand Research
> Validation agent for brand-research-brief.json completeness and quality. Score minimum: 90/100.

## Focus

Validates the `brand-research-brief.json` output from the `brand-research` skill. Ensures all 7 phases are filled with real, usable data — not placeholders or surface-level observations. The brief must be detailed enough that downstream skills (brand-specs, creative-brief, hook-writing) can operate without follow-up questions.

## Scoring Dimensions (each scored 1-100)

### 1. Phase Completeness
All 7 phases must be filled with no critical empty fields. Empty optional fields are acceptable only if justified (e.g. "No founder story found — brand is a corporate entity"). Empty required fields are a scoring penalty.

- **95:** All 7 phases filled. Every required field has real data. Optional fields either filled or explicitly marked "Not found — [reason]." Zero placeholders.
- **80:** All 7 phases present but 2-3 non-critical fields are empty without justification. For example, `design_agency` is blank and `accent_color_hex` is missing, but all core fields (name, colors, product, competitors) are complete.
- **60:** One full phase is shallow (e.g. Phase 6 Founder Story has only the founder name and everything else is empty). Multiple fields across phases contain placeholder text like "TBD" or "to research."

### 2. Visual Data Quality
Hex codes must be present and accurate. Fonts must be identified or best-guess justified. Visual system data must be specific enough to generate a Brand Spec Card without additional research.

- **95:** Primary, secondary, and accent hex codes all present and verified against the website. Fonts identified by name (e.g. "Inter Bold 700" / "Georgia Regular"). Background preference and imagery style described with specific references ("dark backgrounds with high-contrast product shots, similar to Apple product pages").
- **80:** Hex codes present for primary and secondary colors but accent is missing. Font identified as a generic family ("sans-serif, likely Inter or similar") without weight specification. Imagery style described but vaguely ("clean, modern").
- **60:** Only one hex code present. Fonts described as "sans-serif" with no attempt to identify. Imagery style is a single adjective ("minimalist") with no supporting detail.

### 3. Verbatim Authenticity
Testimonials in Phase 3 must be raw customer quotes, not summaries or paraphrases. Each testimonial must include a name (or anonymized identifier) and a detail that proves it was copy-pasted, not rewritten.

- **95:** 5+ raw testimonials with original grammar, spelling quirks, and emotional language intact. Each has a name and source (e.g. "Sarah M. — Amazon review, verified purchase"). Quotes include specific details ("after 3 weeks my knee stopped clicking during squats").
- **80:** 3-4 testimonials that read like real quotes but lack source attribution. Minor cleanup visible (grammar corrected, ellipses where text was trimmed) but the substance is authentic.
- **60:** Testimonials are clearly paraphrased summaries ("customers report feeling more energized"). No source attribution. Language is too polished to be real customer voice ("This product has significantly improved my quality of life").

### 4. Hook Calibration
Phase 7 hooks must be format-specific and varied. A "before_after" hook should read differently from a "ugc_hook." Hooks should reflect the actual brand voice and data from Phases 1-6, not generic advertising templates.

- **95:** Each hook category has 3+ distinct hooks. Hooks reference specific data points from earlier phases (e.g. a statistic_hook uses the actual clinical study percentage from Phase 3). Hooks vary in tone — some direct, some narrative, some curiosity-driven. Format-specific adaptation is visible (carousel hooks are multi-step, UGC hooks are conversational).
- **80:** Each category has 2-3 hooks but some categories share similar phrasing. Hooks reference brand data but occasionally fall back on templates. Most hooks work but 2-3 feel interchangeable across categories.
- **60:** Hooks are generic templates with brand name inserted. "Before_after" hooks and "transformation" hooks are nearly identical. No reference to specific data from earlier phases. All hooks use the same direct-response tone regardless of category.

### 5. Competitive Depth
Phase 5 competitors must have real data — prices, positioning, specific weaknesses. "They're more expensive" is not competitive intelligence. The competitive landscape must reveal actionable positioning gaps.

- **95:** 3-5 competitors listed with verified prices, specific product comparisons, and named weaknesses backed by evidence (e.g. "Competitor X has 3.2 stars on Amazon — top complaint is texture"). `us_vs_them_angles` are specific and brief-ready. `unique_differentiators` are substantiated, not just claims.
- **80:** 3 competitors with prices and general positioning. Weaknesses are identified but surface-level ("more expensive," "less variety"). Differentiators are named but not proven with evidence.
- **60:** 1-2 competitors listed with only names and a vague weakness. No prices. Differentiators are brand claims copy-pasted from the About page. No evidence of actual competitive research.

## Hard Violations (instant fail)

- **Missing phase:** Any of the 7 phases entirely absent from the JSON
- **No hex codes:** `primary_color_hex` and `secondary_color_hex` both empty
- **Identical hooks across formats:** Same hook text appearing in 3+ different hook categories verbatim
- **Invented data:** Statistics, prices, or claims that cannot be traced to a source (fabricated social proof)
- **Broken JSON:** Output is not valid JSON or has structural errors

## Review Process

1. Load `brand-research-brief.json`
2. Validate JSON structure — must parse without errors
3. Check hard violations — if any triggered, FAIL immediately
4. Walk through each phase (1-7) and score the 5 dimensions
5. For Phase 1-2: check visual data quality and completeness
6. For Phase 3: verify verbatim authenticity — do quotes read like real people?
7. For Phase 5: verify competitive depth — is there evidence of actual research?
8. For Phase 7: check hook calibration — are hooks format-specific and data-driven?
9. Calculate overall score (average of 5 dimensions)
10. List what works with specific examples
11. List what does not work with specific rewrites
12. Final verdict: PASS (90+) / REVISE (70-89) / FAIL (<70 or hard violation)

## Output Format

```
Brand Research Agent — [Brand Name] — [Date]

**Hard Violations:** NONE / [list]

| Dimension | Score | Key reasoning |
|---|---|---|
| Phase Completeness | [X/100] | [1-line reasoning] |
| Visual Data Quality | [X/100] | [1-line reasoning] |
| Verbatim Authenticity | [X/100] | [1-line reasoning] |
| Hook Calibration | [X/100] | [1-line reasoning] |
| Competitive Depth | [X/100] | [1-line reasoning] |
| **Overall** | **[X/100]** | |

**What works:**
- [Point 1 — with specific example from the brief]
- [Point 2]

**What does not work:**
- [Issue 1] → Rewrite: [specific fix — e.g. "Replace 'modern font' with 'Inter 600 / Playfair Display 400' based on site inspection"]
- [Issue 2] → Rewrite: [specific fix]

**Verdict:** PASS / REVISE / FAIL
```
