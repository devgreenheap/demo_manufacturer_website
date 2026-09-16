"""
Static export for platforms with no Python/MySQL backend (e.g. Netlify).

Renders every public page to plain HTML using Flask's own test client, and
copies the static/ folder alongside it. Auth pages (login/signup/account/
logout) are intentionally NOT rendered — they need a live backend and are
excluded on purpose, not just hidden from navigation.

Run:
    python freeze.py

Output goes to netlify_build/ — drag that folder straight into Netlify.
"""
import os
import shutil

os.environ["STATIC_BUILD"] = "1"

from app import app  # noqa: E402
import data  # noqa: E402

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "netlify_build")

PAGES = [
    ("/", "index.html"),
    ("/about", "about/index.html"),
    ("/products", "products/index.html"),
    ("/services", "services/index.html"),
    ("/manufacturing", "manufacturing/index.html"),
    ("/quality", "quality/index.html"),
    ("/industries", "industries/index.html"),
    ("/contact", "contact/index.html"),
    ("/request-quote", "request-quote/index.html"),
]


def write(rel_path, content_bytes):
    full_path = os.path.join(OUTPUT_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "wb") as f:
        f.write(content_bytes)


def main():
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

    app.config["TESTING"] = True
    client = app.test_client()
    failures = []
    page_count = 0

    for url, out_path in PAGES:
        resp = client.get(url)
        if resp.status_code != 200:
            failures.append((url, resp.status_code))
            continue
        write(out_path, resp.data)
        page_count += 1

    for product in data.PRODUCTS:
        url = f"/products/{product['slug']}"
        resp = client.get(url)
        if resp.status_code != 200:
            failures.append((url, resp.status_code))
            continue
        write(f"products/{product['slug']}/index.html", resp.data)
        page_count += 1

    # Netlify auto-serves a top-level 404.html for unmatched routes.
    resp = client.get("/this-page-does-not-exist")
    write("404.html", resp.data)
    page_count += 1

    static_src = os.path.join(BASE_DIR, "static")
    static_dest = os.path.join(OUTPUT_DIR, "static")
    shutil.copytree(
        static_src, static_dest,
        ignore=shutil.ignore_patterns("uploads"),
    )

    print(f"Built {page_count} pages into {OUTPUT_DIR}")
    if failures:
        print("FAILURES:")
        for url, code in failures:
            print(f"  {url} -> {code}")


if __name__ == "__main__":
    main()
