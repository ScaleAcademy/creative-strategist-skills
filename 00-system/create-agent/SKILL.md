---
name: create-agent
description: "Generates a validation agent .md file for any workflow step. The agent scores outputs 1-100 across 5 dimensions, provides actionable rewrites, and enforces hard violations. Use when adding quality gates to new or existing skills. Trigger on: 'create a validation agent', 'build a QA agent', 'I need a quality gate for [step]'. Output is a standalone agent-[name].md file ready for Project Knowledge upload."
metadata:
  version: 1.0.0
  status: stable
  tags: [system, meta, validation, quality, agent]
  inputs: [step name, validation focus]
  outputs: [agent-[name].md]
  depends-on: []
---

# Create Agent

## Before Starting

Confirm before starting:
- [ ] Step name identified (e.g. "brand-research", "hook-writing", "copy-editor")
- [ ] Validation focus defined (what the agent checks)
- [ ] The skill or output being validated exists or is well-defined
- [ ] You know the downstream consumers of the validated output

---

This meta-skill generates validation agents for any workflow step. Each agent is a standalone .md file that can be uploaded to Project Knowledge and used as a quality gate before any output moves downstream.

**Input:** Step name + validation focus
**Output:** `agent-[name].md` — ready for Project Knowledge upload

---

## Phase 1: Define the Validation Scope

Ask the user:

1. **What step does this agent validate?** (e.g. "creative brief", "hook bank", "Nano Banana prompt")
2. **What does "good" look like?** What are the non-negotiable quality markers?
3. **What are the most common failure modes?** What goes wrong when this step is rushed?
4. **Who consumes the output?** What downstream skill or person needs this to be right?
5. **What frameworks apply?** Which Scale Academy frameworks are relevant?

Relevant frameworks to consider:
- **Schwartz** — 5 awareness levels (Unaware, Problem Aware, Solution Aware, Product Aware, Most Aware)
- **LF8** — Whitman's 8 innate desires (survival, food, freedom from fear, sexual companionship, comfortable living, superiority, care for loved ones, social approval)
- **C1-C4 matrix** — Demonstration / Education / Pain / Identity angles
- **Cialdini** — 7 principles (reciprocity, commitment, social proof, authority, liking, scarcity, unity)
- **Creative mechanics** — M1-M8 (Implied Answer, Reframe, Trojan Horse, etc.)

---

## Phase 2: Design the 5 Scoring Dimensions

Each dimension must be:
- **Specific** to the step being validated (not generic quality metrics)
- **Observable** — the evaluator can check it without subjective judgment
- **Graduated** — clear difference between a 60, 80, and 95

For each dimension, define:
1. Name and description
2. What a 95 score looks like (example)
3. What an 80 score looks like (example)
4. What a 60 score looks like (example)

The final score is the average of all 5 dimensions. **Nothing ships below 90.**

---

## Phase 3: Define Hard Violations

Hard violations are instant fails regardless of score. They represent errors so fundamental that no amount of quality elsewhere compensates.

Good hard violations are:
- **Objective** — anyone can verify them (yes/no, not a judgment call)
- **Critical** — they break the output for the downstream consumer
- **Non-compensable** — a perfect score on everything else doesn't fix them

Typical categories:
- Missing required data (empty fields, absent sections)
- Framework misapplication (wrong awareness stage, no angle justification)
- Accuracy failures (paraphrased verbatims, invented data)
- Compliance breaches (banned words, grammar errors in final copy)

---

## Phase 4: Write Calibration Examples

For each of the 5 dimensions, write concrete examples at three score levels:
- **95** — excellent, ships immediately
- **80** — good but needs a specific fix
- **60** — significant issues, requires rework

These examples are the calibration tool. Without them, scoring is subjective.

---

## Phase 5: Define the Review Process

Write the step-by-step process the agent follows:

1. Load the output to validate
2. Check hard violations first (if any → instant fail, stop here)
3. Score each dimension 1-100 with reasoning
4. Calculate overall score (average of 5 dimensions)
5. List what works and why
6. List what does not work and why
7. For each issue: provide a specific rewrite ("change X to Y because Z")
8. Final verdict: PASS (90+) / REVISE (70-89) / FAIL (<70 or hard violation)

---

## Phase 6: Generate the Agent File

Use this template to produce the final `agent-[name].md`:

```markdown
# Agent: [Name]
> Validation agent for [what it validates]. Score minimum: 90/100.

## Focus
[What this agent validates — 2-3 sentences]

## Scoring Dimensions (each scored 1-100)

### 1. [Dimension Name]
[Description + what good looks like]
- **95:** [concrete example]
- **80:** [concrete example]
- **60:** [concrete example]

### 2. [Dimension Name]
[Same structure]

### 3. [Dimension Name]
[Same structure]

### 4. [Dimension Name]
[Same structure]

### 5. [Dimension Name]
[Same structure]

## Hard Violations (instant fail)
- [Violation 1 — objective, verifiable]
- [Violation 2]
- [Violation 3]

## Review Process
1. Load the output to validate
2. Check hard violations first — if any triggered, FAIL immediately
3. Score each dimension 1-100 with written reasoning
4. Calculate overall score (average of 5 dimensions)
5. List what works and why (be specific)
6. List what does not work and why (be specific)
7. For each issue: specific rewrite — "change X to Y because Z"
8. Final verdict: PASS (90+) / REVISE (70-89) / FAIL (<70 or hard violation)

## Output Format
[Agent name] — [Output being validated] — [Date]

**Hard Violations:** NONE / [list]

| Dimension | Score | Key reasoning |
|---|---|---|
| [Dim 1] | [X/100] | [1-line reasoning] |
| [Dim 2] | [X/100] | [1-line reasoning] |
| [Dim 3] | [X/100] | [1-line reasoning] |
| [Dim 4] | [X/100] | [1-line reasoning] |
| [Dim 5] | [X/100] | [1-line reasoning] |
| **Overall** | **[X/100]** | |

**What works:**
- [Point 1]
- [Point 2]

**What does not work:**
- [Issue 1] → Rewrite: [specific fix]
- [Issue 2] → Rewrite: [specific fix]

**Verdict:** PASS / REVISE / FAIL
```

Save as `agent-[name].md` in the relevant category folder.

---

## Deliver

Present the generated agent file and confirm:

> "Here's your validation agent for [step]. It scores across 5 dimensions, enforces [N] hard violations, and requires a minimum of 90/100 to pass. Upload it to Project Knowledge to activate it as a quality gate."

---

## Related Skills

- All skills in the repository — any skill output can have a validation agent
- `01-audit/brand-research` — example: agent-brand-research.md validates the brief
- `03-strategy/creative-brief` — example: agent-creative-brief.md validates the brief
- `04-production/static-production` — example: agent-static-production.md validates the prompt
