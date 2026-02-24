"""
Fetch publications from Google Scholar and write publications.json.
Run from project root: python scripts/fetch_publications.py

Requires: pip install scholarly
Google Scholar user ID is read from SCHOLAR_ID or default below.
"""

import json
import os
import sys

# Default: from https://scholar.google.com/citations?user=LZcqZqYAAAAJ
SCHOLAR_ID = os.environ.get("SCHOLAR_ID", "LZcqZqYAAAAJ")
OUTPUT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "publications.json",
)


def fetch_publications():
    try:
        from scholarly import scholarly
    except ImportError:
        print("Install scholarly: pip install scholarly", file=sys.stderr)
        sys.exit(1)

    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["publications"], sortby="year", publication_limit=100)

    publications = []
    for pub in author.get("publications") or []:
        try:
            filled = scholarly.fill(pub)
            bib = filled.get("bib", {})
            entry = {
                "title": bib.get("title", ""),
                "authors": bib.get("author", ""),
                "venue": bib.get("venue", ""),
                "year": str(bib.get("year", "")),
                "volume": bib.get("volume", ""),
                "pages": bib.get("pages", ""),
                "url": filled.get("pub_url") or filled.get("eprint_url") or "",
            }
            # Normalize authors: can be string or list
            if isinstance(entry["authors"], list):
                entry["authors"] = ", ".join(entry["authors"])
            publications.append(entry)
        except Exception as e:
            print("Skip publication:", e, file=sys.stderr)
            continue

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(publications, f, ensure_ascii=False, indent=2)
    print("Wrote", len(publications), "publications to", OUTPUT_PATH)


if __name__ == "__main__":
    fetch_publications()
