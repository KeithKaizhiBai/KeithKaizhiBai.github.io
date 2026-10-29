"""Offline tests for retaining curated publications during Scholar refreshes."""

import json
from pathlib import Path
import tempfile
import unittest

from fetch_publications import load_manual_publications, merge_publications


class PublicationMergeTests(unittest.TestCase):
    def test_manual_records_survive_and_unmarked_records_are_refreshed(self):
        manual = {"title": "GitHub manuscript", "year": "2026", "manual": True}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "publications.json"
            path.write_text(json.dumps([
                manual, {"title": "Old Scholar record", "year": "2025"}
            ]), encoding="utf-8")
            curated = load_manual_publications(path)
        fetched = {"title": "Refreshed Scholar record", "year": "2025"}
        self.assertEqual(merge_publications(curated, [fetched]), [manual, fetched])

    def test_title_variants_keep_manual_metadata(self):
        manual = {"title": "Reliability-aware active learning: FFLO phase spaces",
                  "authors": "Kai-Zhi Bai", "year": "2026", "manual": True}
        fetched = {"title": "RELIABILITY–AWARE ACTIVE LEARNING — FFLO PHASE SPACES",
                   "authors": "Incomplete metadata", "year": "2026"}
        self.assertEqual(merge_publications([manual], [fetched]), [manual])

    def test_identifiers_remove_duplicates_even_when_titles_differ(self):
        cases = [
            ({"arxiv_id": "2607.15720"}, {"arxiv_id": "2607.15720"}),
            ({"arxiv_id": "2607.15720"},
             {"url": "https://arxiv.org/abs/2607.15720v1"}),
            ({"url": "https://github.com/owner/repo"},
             {"url": "https://github.com/owner/repo/#readme"}),
            ({"doi": "10.1234/example"}, {"doi": "https://doi.org/10.1234/EXAMPLE"}),
            ({"doi": "10.1234/example"}, {"url": "https://doi.org/10.1234/EXAMPLE"}),
        ]
        for manual_id, fetched_id in cases:
            with self.subTest(identifier=manual_id):
                manual = dict(title="Curated title", year="2026", manual=True,
                              **manual_id)
                fetched = dict(title="Scholar title", year="2026", **fetched_id)
                self.assertEqual(merge_publications([manual], [fetched]), [manual])

    def test_year_sort_is_descending_and_stable(self):
        entries = [
            {"title": "Older", "year": "2024"},
            {"title": "First new", "year": "2026"},
            {"title": "Second new", "year": 2026},
            {"title": "Undated", "year": ""},
            {"title": "Recent", "year": "2025"},
        ]
        self.assertEqual(merge_publications([], entries),
                         [entries[index] for index in [1, 2, 4, 0, 3]])

    def test_missing_existing_file_has_no_manual_records(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(load_manual_publications(Path(directory) / "missing.json"), [])


if __name__ == "__main__":
    unittest.main()
