#!/usr/bin/env python3
"""
Template de génération d'un manifeste UTM pour un lot de vidéos.
Adapter le bloc CONFIG + la liste ROWS par batch, puis :  python3 gen-manifest.py
"""

# ===== CONFIG (à adapter par batch) =====
OUT = "/chemin/vers/[BATCH]/_export/[AAMMJJ]/[ID]_UTM-manifest.md"
DESTINATION = "https://www.exemple.com/landing"          # URL de destination (par type de LP)
UTM_BASE = ("utm_source=facebook&utm_medium=cpc"
            "&utm_campaign={{campaign.name}}_{{adset.name}}"
            "&utm_content={{ad.name}}")                  # format fourni par le client
COMMON = ("&utm_concept=yu-15&utm_brief=yu-15-b2&utm_angle=c3-03&utm_anglecat=c3"
          "&utm_persona=p1&utm_awareness=pa&utm_funnel=tofu"
          "&utm_style=s701&utm_creatype=iteration&utm_lp=vsl")  # slugs constants du batch

# Une ligne par vidéo : (nom_sans_ext, hook, talent, variant, ffmsg, len)
ROWS = [
    ("YU06-W39_cafe_sarah-machine_t1-grignotage-emotionnel", "cafe", "sarah", "machine", "t1-grignotage", "148s"),
    # ... ajouter les autres
]
# =========================================

def url(hook, talent, variant, ffmsg, length):
    return (f"{DESTINATION}?{UTM_BASE}{COMMON}"
            f"&utm_hook={hook}&utm_talent={talent}&utm_variant={variant}"
            f"&utm_ffmsg={ffmsg}&utm_len={length}")

def main():
    L = ["# Manifeste UTM\n\n",
         "| Vidéo (= nom d'ad) | Hook | Perso | Variante | Titre | Durée |\n",
         "|---|---|---|---|---|---|\n"]
    for n, h, t, v, f, l in ROWS:
        L.append(f"| `{n}` | {h} | {t} | {v} | {f} | {l} |\n")
    L.append("\n---\n\n## URLs finales taguées\n")
    for n, h, t, v, f, l in ROWS:
        L.append(f"\n### {n}\n```\n{url(h, t, v, f, l)}\n```\n")
    with open(OUT, "w") as fh:
        fh.write("".join(L))
    print("Écrit:", OUT, f"({len(ROWS)} vidéos)")

if __name__ == "__main__":
    main()
