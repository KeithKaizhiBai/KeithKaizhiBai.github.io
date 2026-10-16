# Personal website

Static personal website for Kaizhi Bai, served by GitHub Pages from this
repository. `.nojekyll` keeps the prebuilt files unchanged.

## Active files and preview

- `index.html`, `style.css`, `script.js`: personal homepage.
- `data/publications.json`: displayed publication records.
- `note_pdfs/`: downloadable note snapshots.
- `quantum-algorithms/`: public companion with retained numerical results.

From the repository root, run `python -m http.server 8766 --bind 127.0.0.1`
and open `http://127.0.0.1:8766/`. Use HTTP so the publication JSON can load.
No package installation or build is required for this static site.

## Current state — 2026-10-16

The current task connects the probability, statistics, stochastic processes and
machine learning note to the existing SPAI PDF, and makes the public quantum
algorithms companion link explicit in the homepage HTML.

The checkout started at `4d4dc266f32fb2532d8c3c93a340474ae2724883` on `main`.
The user explicitly authorized committing these four files and pushing to
`main` on October 16, 2026. Publication and production-link verification are in
progress; completion will be recorded below after the deployed files are checked.

### SPAI snapshot provenance

- Original: `E:\CosmosWork\Notes_Previous\SPMLAI\spai.pdf`.
- Website copy: `note_pdfs/spai.pdf` (58 pages, dated October 14, 2026).
- SHA-256: `ae409ce98c6d8064092b35d8a32cd422b42191a965b4341d71201dbec392a873`.
- The original PDF and its LaTeX sources were not modified or recompiled.
- The note is marked **In progress** because several chapters remain outlines.

A public page links to a repository-relative PDF; visitors cannot open a local
Windows directory. This is a retained snapshot, not an automatic synchronization
with the source folder. For future updates, copy the intended compiled PDF to
the same website path, compare hashes, and update the date and this record.
Never substitute a `file:` URL or a local drive path into the public HTML.

### Validation and remaining work

- Homepage and companion HTML: 33 local resource references checked, including
  exact filename casing; static anchors checked; no missing resources found.
- `node --check script.js` passed. The Git whitespace check passed with existing
  CRLF line endings treated as line endings.
- The published SPAI copy is byte-for-byte identical to the original. All 58
  pages parsed with pypdf; one probability page was rendered and visually checked.
- The updated homepage Notes section was inspected in the in-app browser using
  a local HTTP preview. The SPAI PDF URL was opened in the browser, but the in-app
  PDF viewer displayed a blank surface; its browser rendering is not verified.
  The PDF itself was parsed and rendered independently as described above.
- No LaTeX compilation, full scientific review, full PDF visual review, mobile
  regression test, or comprehensive external-link audit was performed.
- Next: commit and push the authorized changes, then verify the deployed Notes
  entry, SPAI PDF hash, and public quantum algorithms companion URL.

### Change record

2026-10-16: Replaced the SPAI placeholder with a real PDF and a draft-status
description. Moved the already-working public quantum companion URL from a
JavaScript rewrite into HTML and removed that redundant rewrite, so the link
also works without JavaScript. Other biography, publication records, note files,
styles and quantum experiment assets were retained.
