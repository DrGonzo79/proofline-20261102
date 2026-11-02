# Architecture

The static Next.js client demonstrates consent, evidence review, deterministic scoring, and share-state with shared JSON fixtures. FastAPI loads the same fixture schema and exposes a tested `POST /proof-packs` domain operation. GitHub Pages hosts only the frontend; Python is runnable locally/CI and is not deployed.

Production should split into: (1) an open, signed local extractor; (2) a metadata API holding consent, minimal evidence, versioned rubrics, and expiring links; (3) a reviewer console; and (4) an append-only audit log. Raw code, filenames, commit messages, repository URLs, and client identifiers must never cross the device boundary. Snapshot signatures, reviewer authentication, revocation, deletion, rate limits, structured logs, request IDs, and alerts are launch gates.

Failures must fail closed: no consent means no pack; stale or unsigned evidence is visibly invalid; unavailable reviewer state leaves a draft; deletion revokes all links. Score components are observable separately so drift and reviewer disagreement can be measured.
