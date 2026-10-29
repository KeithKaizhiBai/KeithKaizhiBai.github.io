"""
Fetch publications from Google Scholar and write publications.json.
Run from project root: python scripts/fetch_publications.py

Requires: pip install scholarly
Google Scholar user ID is read from SCHOLAR_ID or default below.
Existing records marked manual: true are retained when refreshing.
"""

import json
import os
import re
import sys
import unicodedata
from urllib.parse import urlsplit, urlunsplit

# Default: from https://scholar.google.com/citations?user=LZcqZqYAAAAJ
SCHOLAR_ID = os.environ.get("SCHOLAR_ID", "LZcqZqYAAAAJ")
OUTPUT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "publications.json",
)


def load_manual_publications(path=OUTPUT_PATH):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8-sig") as stream:
        return [entry for entry in json.load(stream) if entry.get("manual") is True]


def publication_keys(entry):
    """Match title variants and canonical identifiers without changing records."""
    keys = set()
    title = unicodedata.normalize("NFKC", str(entry.get("title") or "")).casefold()
    title = "".join(character for character in title if character.isalnum())
    if title:
        keys.add(("title", title))

    arxiv_id = str(entry.get("arxiv_id") or "").strip().lower()
    doi = str(entry.get("doi") or "").strip().lower()
    url = str(entry.get("url") or "").strip()
    if url:
        parts = urlsplit(url)
        canonical_url = urlunsplit((parts.scheme.lower(), parts.netloc.lower(),
                                   parts.path.rstrip("/"), parts.query, ""))
        keys.add(("url", canonical_url))
        if parts.netloc.lower() in {"arxiv.org", "www.arxiv.org"}:
            arxiv_id = re.sub(r"^/(abs|pdf)/", "", parts.path).removesuffix(".pdf")
        elif parts.netloc.lower() in {"doi.org", "dx.doi.org"}:
            doi = parts.path.lstrip("/").lower()
    if arxiv_id:
        arxiv_id = re.sub(r"^arxiv:\s*", "", arxiv_id)
        keys.add(("arxiv", re.sub(r"v\d+$", "", arxiv_id)))
    if doi:
        keys.add(("doi", re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", doi)))
    return keys


def merge_publications(manual_publications, fetched_publications):
    """Prefer curated entries and preserve input order within each year."""
    merged = []
    seen = set()
    for entry in [*manual_publications, *fetched_publications]:
        keys = publication_keys(entry)
        if not keys.intersection(seen):
            merged.append(entry)
        seen.update(keys)

    def year(entry):
        value = str(entry.get("year") or "")
        return int(value) if value.isdigit() else 0

    return sorted(merged, key=year, reverse=True)


def fetch_publications():
    manual_publications = load_manual_publications()
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

    publications = merge_publications(manual_publications, publications)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(publications, f, ensure_ascii=False, indent=2)
    print("Wrote", len(publications), "publications to", OUTPUT_PATH)


if __name__ == "__main__":
    fetch_publications()
