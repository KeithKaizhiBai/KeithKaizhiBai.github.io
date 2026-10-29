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

## Current update — 2026-10-29

The homepage now presents two related FFLO research projects and active work on
quantum algorithms:

- Personal Info: revised biography covering topological phases, transport,
  superconductivity, the altermagnetic FFLO preprint, FFLO active learning,
  and current quantum algorithm studies.
- Experience: separate cards for the altermagnetic FFLO collaboration and the
  reliability-aware active-learning project, with repository, manuscript and
  PDF links. Project start dates are not inferred from publication dates.
- Publications: two new 2026 records, explicitly labeled **arXiv preprint** and
  **GitHub manuscript · v9 (initial draft)**. The latter is not a journal paper
  or a submission-ready manuscript.
- Interests: ongoing quantum algorithm research, linked to the existing notes
  and PennyLane companion. These are numerical studies, not hardware results.
- Narrow screens: a wrapping, sticky navigation bar and stacked personal card
  prevent the navigation and contact details from hiding the main content.
  Local anchor targets leave space below the navigation.

### Sources and scientific scope

- [arXiv:2607.15720](https://arxiv.org/abs/2607.15720): *First-Order Topological
  FFLO Transition and Superconducting Diode Sign Reversal in Altermagnetic
  Nanowires*, Bo Fu, Kaizhi Bai, Chang-An Li and Shun-Qing Shen; submitted
  July 17, 2026.
- [FFLO_AL](https://github.com/KeithKaizhiBai/FFLO_AL) and
  [manuscript v9](https://github.com/KeithKaizhiBai/FFLO_AL/tree/main/reports/manuscript/v9):
  *Reliability-aware active learning for FFLO phase spaces*, Kai-Zhi Bai (2026).
  Title, author, methods and status were checked against the repository README,
  manuscript TeX and author-review record on October 29, 2026.

The project description distinguishes numerical reliability from phase
identity and restricts topology evaluation to reliable, gapped FFLO states.
It does not claim a complete three-dimensional phase atlas, a measured
wall-clock speedup, or a new open-source license grant.

### Maintaining publication records

`data/publications.json` remains the source displayed by `script.js`.
Both new records use `"manual": true`. The optional Scholar refresh retains
these curated records, deduplicates matches by normalized title or canonical
arXiv/DOI/URL identifiers, and sorts by year in descending order. Curated
metadata takes precedence when a matching Scholar record appears. Unmarked
records continue to be replaced by the Scholar refresh.

Offline regression checks (no Scholar requests):

```sh
python3 -B -m unittest discover -s scripts -p 'test_fetch_publications.py' -v
node --check script.js
git -c core.whitespace=cr-at-eol diff --check
```

### Validation

- Five offline publication refresh tests passed, including manual retention,
  title/identifier deduplication and stable year ordering.
- JavaScript syntax and Git whitespace checks passed.
- Both HTML pages were checked for local resource paths, duplicate IDs and
  local anchors; all 31 unique referenced local resources and the publication
  JSON returned HTTP 200 through the local preview.
- All five newly added GitHub/arXiv destination URLs returned HTTP 200.
- The local browser rendered all 10 publication cards, both project cards,
  the revised biography and the quantum algorithm interest entry. Browser
  console checks found no warnings or errors.
- Changes are prepared for review; this update does not record a production
  deployment. The October 16 deployment described below is historical.

## Previous update — 2026-10-16

The current task connects the probability, statistics, stochastic processes and
machine learning note to the existing SPAI PDF, and makes the public quantum
algorithms companion link explicit in the homepage HTML.

The checkout started at `4d4dc266f32fb2532d8c3c93a340474ae2724883` on `main`.
The user explicitly authorized committing these four files and pushing to
`main` on October 16, 2026. Website changes were published in commit
`26367fca967cee01c7ab09213cfba7109f7a7b59`; production-link verification passed.
The follow-up documentation commit records the completed verification.

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
- GitHub Pages [deployment run 38855327362](https://github.com/KeithKaizhiBai/KeithKaizhiBai.github.io/actions/runs/38855327362)
  completed successfully for website commit `26367fc`.
- Production homepage, script, SPAI PDF and quantum companion HTML returned
  HTTP 200 and matched the committed bytes. Hash checks used `?verify=26367fc`
  to avoid stale CDN responses observed immediately after deployment.
- All 30 unique local resource URLs referenced by the two HTML pages returned
  HTTP 200 at their ordinary public URLs.
- The live Notes entry was checked in the browser: **In progress**, linking to
  `https://keithkaizhibai.github.io/note_pdfs/spai.pdf`. The downloaded PDF hash
  matches the source snapshot recorded above. Browser PDF rendering remains
  unverified as noted above; file availability and integrity passed.
- No task work remains. Future substantive note updates require a new snapshot
  and another deployment check; the source folder is not synchronized automatically.

### Change record

2026-10-16: Replaced the SPAI placeholder with a real PDF and a draft-status
description. Moved the already-working public quantum companion URL from a
JavaScript rewrite into HTML and removed that redundant rewrite, so the link
also works without JavaScript. Other biography, publication records, note files,
styles and quantum experiment assets were retained.

2026-10-16: Following explicit user authorization, committed the four reviewed
files and pushed to `main`, then verified Pages deployment, the live Notes entry,
the PDF hash, and all referenced local resources. Git author information was
reused from the preceding repository commit for these commit commands only;
no persistent Git identity setting was changed.
