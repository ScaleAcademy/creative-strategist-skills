---
name: animate-statics
description: "Turns a winning static ad into a 3-4 second animation using start frame / end frame interpolation. Use when a static creative has proven performance and needs a motion variant for video placements. Trigger on: 'animate this static', 'make a GIF from this ad', 'static to video', 'interpolation', 'motion variant'. Supports manual (NB2 + Flow) and automated (fal.ai MCP) workflows."
metadata:
  version: 1.0.0
  status: beta
  tags: [production, animation, static, GIF, interpolation, nano-banana, veo3, fal-ai, mcp]
  inputs: [winning static ad image, brand-spec-card.png, visual-style-card.png]
  outputs: [3-4 second animated GIF or MP4]
  depends-on: [static-production, brand-specs]
---

# Animate Statics

Turn a winning static ad into a 3-4 second animation using a start frame / end frame interpolation method.

**Two paths to the same output:**
- **Manual** — copy-paste prompts into Claude, generate frames in Nano Banana 2 (fal.ai), animate in Flow (Veo 3.1). Full control, no setup required.
- **MCP (automated)** — fal.ai exposes an MCP that lets Claude Code call NB2 and Veo 3.1 directly. No copy-paste, no manual uploads. End-to-end pipeline in one session.

Both paths use the same prompts and the same logic. Manual is the entry point. MCP is the production-scale version.

## Before Starting

Confirm before starting:
- [ ] Static ad has proven performance (CTR > benchmark or approved by strategist)
- [ ] Original static image available in high resolution
- [ ] Brand Spec Card + Visual Style Card available (from `brand-specs`)
- [ ] Animation goal defined: subtle motion (product reveal, text entrance) or dynamic (scene transition, transformation)

---

## Step 1: Analyse the Static

Look at the winning static and identify:
- **What should move?** — the element that would benefit most from motion (product, text, background, person)
- **What should stay fixed?** — brand elements, logo, layout structure
- **What's the story in 3 seconds?** — the micro-narrative the animation tells

**Rule:** The animation must reinforce the same message as the static. Motion is not decoration — it's amplification.

---

## Step 2: Define Start Frame and End Frame

The static you have = one of the two frames (usually the end frame).

**Generate the missing frame:**
- If static = end state → generate the "before" (start frame)
- If static = hero shot → generate a context/reveal setup (start frame)

The missing frame must:
- Match the exact visual style, colors, and typography of the original
- Be different enough to create visible motion when interpolated
- Tell a coherent micro-story when played as start → end

---

## Step 3: Generate the Missing Frame (Nano Banana 2)

Use the static as reference. Write a prompt for the missing frame:

```
Create an image that serves as the [START/END] frame for an animation.
The [END/START] frame is the uploaded reference image.

MATCH EXACTLY:
- Same aspect ratio: [RATIO]
- Same color palette: [HEX codes from spec card]
- Same typography style and placement
- Same overall composition structure

WHAT CHANGES:
- [Describe the specific difference: product position, text state, background, lighting]

WHAT STAYS FIXED:
- [List fixed elements: logo position, brand colors, layout grid]

Upload brand-spec-card.png and visual-style-card.png as references.
```

---

## Step 4: Animate with Veo 3.1 (Flow)

With both frames ready, create the interpolation:

```json
{
  "start_frame": "[start frame image]",
  "end_frame": "[end frame image]",
  "duration": "3-4 seconds",
  "motion_type": "smooth interpolation",
  "style": "commercial, clean transitions",
  "constraints": "no morphing artifacts, maintain text legibility throughout"
}
```

**Quality checks:**
- Text remains readable throughout the animation
- No warping or morphing artifacts on brand elements
- Motion feels intentional, not AI-glitchy
- Loop-friendly if intended for social placements

---

## Step 5: Export and Deliver

**Formats:**
- GIF — for preview and social placements
- MP4 — for ad platforms (Meta, TikTok)

**Specs:**
- Duration: 3-4 seconds
- Loop: yes for GIF, optional for MP4
- Resolution: match original static dimensions

---

## Critical Rules

- **Never animate text in a way that makes it unreadable** — if text moves, it must be fully readable at every frame
- **The animation must work without sound** — this is a static-to-motion conversion, not a video ad
- **Keep it subtle** — the best static animations feel like "the image came alive," not "someone made a video"
- **Safe zones still apply** — top 270px and bottom 340px on 1080x1920 remain clear of critical content
- **Test the loop** — if the GIF doesn't loop smoothly, the end frame and start frame need better alignment

---

## Automatisation via MCP

fal.ai expose un MCP officiel qui permet à Claude Code d'appeler Nano Banana 2 et Veo 3.1 directement — sans passer par l'interface manuelle.

**Ce que ça change :**
- Claude Code reçoit la static → génère le prompt → appelle NB2 via MCP → récupère le missing frame → appelle Veo 3.1 → retourne le GIF
- Zéro copier-coller, zéro upload manuel
- Pipeline complet en une seule session Claude Code

**Setup MCP fal.ai :**

```bash
# Installer le MCP fal.ai
npm install -g @fal-ai/mcp

# Ajouter dans la config Claude Code (claude_desktop_config.json)
{
  "mcpServers": {
    "fal": {
      "command": "npx",
      "args": ["-y", "@fal-ai/mcp"],
      "env": {
        "FAL_KEY": "YOUR_FAL_API_KEY"
      }
    }
  }
}
```

**Clé API fal.ai :** `fal.ai/dashboard` → API Keys → Create key

**Modèles à appeler :**
- Missing frame generation → `fal-ai/flux/dev` ou `fal-ai/ideogram/v2` (NB2 = Flux Dev sur fal.ai)
- Animation → `fal-ai/veo3` (Veo 3.1 Fast)

**Workflow Claude Code :**

```
1. Upload static → Claude Code analyse l'image
2. Claude Code génère le concept + le prompt missing frame
3. Appel MCP fal.ai → NB2 génère le missing frame → retourné automatiquement
4. Claude Code génère le JSON Veo 3.1
5. Appel MCP fal.ai → Veo 3.1 génère l'animation → GIF retourné
6. Si problème → Claude Code itère le prompt → nouvel appel MCP
```

**Note :** Le workflow manuel (Steps 1–5) reste la référence pour comprendre la logique et débugger. Le MCP automatise l'exécution, pas la réflexion.

---

## Related Skills

- `04-production/static-production` — produces the winning static that feeds this skill
- `01-audit/brand-specs` — spec cards used as references in every generation prompt
- `04-production/ai-video-production` — for full AI video production (not interpolation)
- `05-analysis/ad-analysis` — test animated variant vs original static
