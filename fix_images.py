"""
Auto-corrects mismatched filenames in static/images/products/ so they match
a product's slug (which is what the site looks up by).

Handles typos, singular/plural mismatches, extra words, etc. by matching
each file's name against the closest product slug. Files that already match
a slug are left alone. Ambiguous or unrecognizable names are skipped and
printed so they can be renamed by hand.

Run this any time after dropping new images in:
    python fix_images.py
"""
import difflib
import os
import re

import data

IMAGE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "images", "products")
EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".avif"}
SLUGS = [p["slug"] for p in data.PRODUCTS]

# Minimum similarity to consider a match at all, and the minimum lead the
# best match must have over the runner-up to be considered unambiguous.
MIN_RATIO = 0.45
MIN_MARGIN = 0.08


def normalize(name):
    name = name.lower()
    name = re.sub(r"[_\s]+", "-", name)
    name = re.sub(r"[^a-z0-9-]", "", name)
    return name


def best_slug_match(stem_norm):
    scored = sorted(
        ((s, difflib.SequenceMatcher(None, stem_norm, s).ratio()) for s in SLUGS),
        key=lambda pair: pair[1],
        reverse=True,
    )
    best_slug, best_ratio = scored[0]
    runner_up_ratio = scored[1][1] if len(scored) > 1 else 0
    if best_ratio < MIN_RATIO:
        return None, scored[:3]
    if best_ratio - runner_up_ratio < MIN_MARGIN:
        return None, scored[:3]
    return best_slug, scored[:3]


def main():
    if not os.path.isdir(IMAGE_DIR):
        print(f"No such directory: {IMAGE_DIR}")
        return

    files = [f for f in os.listdir(IMAGE_DIR) if os.path.splitext(f)[1].lower() in EXTENSIONS]
    fixed, skipped, already_ok = 0, 0, 0

    for filename in files:
        stem, ext = os.path.splitext(filename)
        stem_norm = normalize(stem)

        if stem_norm in SLUGS:
            already_ok += 1
            continue

        target_slug, candidates = best_slug_match(stem_norm)
        if not target_slug:
            top = ", ".join(f"{s} ({r:.2f})" for s, r in candidates)
            print(f"SKIP   {filename}  -> ambiguous/no confident match. Closest: {top}")
            skipped += 1
            continue

        target = f"{target_slug}{ext}"
        target_path = os.path.join(IMAGE_DIR, target)
        if os.path.exists(target_path):
            print(f"SKIP   {filename}  -> target {target} already exists")
            skipped += 1
            continue

        os.rename(os.path.join(IMAGE_DIR, filename), target_path)
        print(f"FIXED  {filename}  ->  {target}")
        fixed += 1

    print(f"\n{fixed} renamed, {already_ok} already correct, {skipped} need manual review.")
    missing = sorted(set(SLUGS) - set(normalize(os.path.splitext(f)[0]) for f in os.listdir(IMAGE_DIR)))
    if missing:
        print(f"Still no image for: {', '.join(missing)}")


if __name__ == "__main__":
    main()
