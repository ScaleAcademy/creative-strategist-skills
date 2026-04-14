---
name: ai-video-production
description: "Turns a validated creative brief into scene-by-scene prompts for AI video generation tools (VEO3, Kling, Runway). Use when producing video with AI tools instead of human editors. Trigger on: 'VEO3 prompts', 'Kling prompt', 'generate AI video', 'AI video brief'. Produces a scene-by-scene prompt pack ready to execute in the chosen AI tool."
metadata:
  version: 1.0.0
  status: beta
  tags: [production, ai-video, VEO3, Kling, prompts]
  inputs: [validated creative brief, selected hook, reference images if available]
  outputs: [scene-by-scene prompt pack for VEO3 / Kling]
  depends-on: [creative-brief, hook-writing]
---

# AI Video Production

## Before Starting

Confirm before starting:
- [ ] Validated creative brief
- [ ] Selected hook
- [ ] AI tool defined: VEO3 (Google) or Kling (Kuaishou) or Runway
- [ ] Target duration per scene defined (recommended: 3–8s per scene)
- [ ] Reference images available if visual consistency is required (character consistency)
- [ ] Visual style defined (realistic / cinematic / simulated UGC / animated)

---

## AI Video Prompting Principles

### Scene Prompt Structure

```
[Subject] [Action] [Setting] [Camera angle] [Camera movement] [Lighting] [Style] [Mood / Emotion] [Duration]
```

**Rules:**
- 1 scene = 1 prompt. Do not combine two actions in the same prompt.
- Name the action before the context: "A woman opens [object]" not "In a kitchen, a woman..."
- Specify camera movement: static / slow zoom / tracking / handheld / drone
- Specify lighting: natural / golden hour / studio / low key / overcast
- Avoid abstract words: "beautiful", "amazing" — describe what is concrete

### Visual Consistency Across Scenes

To keep the same character across scenes:
- Physically describe the character in each prompt (age, gender, outfit, hair color)
- Use a reference image if the tool allows it (Kling = image + prompt)
- Keep the same setting / background across linked scenes

---

## Phase 1: Break the Brief into Scenes

Take the narrative structure from the brief (Hook → Tension → Resolution → CTA) and convert it into 3–8 second scenes.

**Recommended number of scenes:**
- 15s → 3–4 scenes
- 30s → 5–6 scenes
- 60s → 8–10 scenes

---

## Phase 2: Write the Prompts

For each scene:

```markdown
**Scene [#] — [Name / Role in structure]**
Duration: [3–8s]
Tool: [VEO3 / Kling / Runway]

Prompt:
"[Complete description following the structure: subject + action + setting + camera + lighting + style + emotion]"

Reference image: [Yes / No — link if yes]
Production note: [Specific advice for this tool]
```

---

## Phase 3: Assemble and Test

After generating all scenes:
1. Watch each scene individually
2. Check visual consistency (character, setting, style)
3. Assemble in narrative order
4. Add text overlay, subtitles, music in post (CapCut / Premiere / DaVinci)
5. Check: does the sequence hold without sound? (silent viewing test)

---

## Output Format

```markdown
# AI Video Prompt Pack — [Brand] — [Creative ID] — [Date]

## Context
Primary tool: [VEO3 / Kling / Runway]
Total duration: [Xs]
Style: [Realistic UGC / Cinematic / Animated]
Main character: [Complete physical description]

## Scenes

### Scene 1 — Hook [0–3s]
Prompt: "[Full prompt]"
Ref image: [Link / None]

### Scene 2 — [Name] [3–Xs]
[Same structure]

[...]

## Post-Production
- Text overlay to add: "[Text hook]" — [Position, font, timing]
- Subtitles: [Yes / No]
- Music: [Style / Reference]
- Final CTA: "[Text]" — [Appearance timing]
```

---

## Related Skills

- `03-strategy/creative-brief` — prerequisite
- `03-strategy/hook-writing` — hook → first scene
- `04-production/video-production` — human editor brief version of the same concept
- `04-production/campaign-setup` — after production
