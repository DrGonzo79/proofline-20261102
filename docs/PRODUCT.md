# Product plan

## ICP and JTBD
The first ICP is an active-job-search senior developer with 2+ years of meaningful private work and permission to summarize it. Their job: “Help me prove what I owned without revealing my former employer’s IP.” The initial buyer is the candidate; recruiter SaaS waits until packs change hiring behavior.

## MVP
1. Candidate consent and employer-policy checklist.
2. Local extractor producing counts, time ranges, contribution continuity, and signed hashes—never code or commit text.
3. Candidate claims mapped to evidence boundaries.
4. Structured oral defense scored on architecture, tradeoffs, and ownership.
5. Expiring proof pack with reviewer identity, freshness, revocation, and limitations.

The prototype ships steps 1, 3, and deterministic scoring over demo fixtures. It deliberately does not pretend to verify git or identity.

## Data model
`Candidate` owns `ConsentRecord`, `EvidenceSnapshot`, and `Claim`; a `DefenseSession` has rubric scores and a reviewer; a `ProofPack` references immutable evidence/defense versions, status, expiry, and revocation. Raw repositories are never server entities.

## AI strategy
No model is needed for the trust boundary. Deterministic extraction and human review are the product. Later, a local model may redact claim drafts and suggest oral-defense questions; all outputs require review and must be labeled.

## Economics and offer
Start at $99 per defense; target under $35 reviewer cost and under $10 acquisition cost through communities. The report’s recruiter anchor is $149/month or $1,490/year versus HackerRank Pro at $4,490/year. The reported ceiling is $2M–$4M ARR, but a 90-day target is merely 5 paid packs and 2 recruiter pilots.

## Validation and moat
Run 10 concierge extractions, 5 blind recruiter comparisons, and a $99 CTA. The moat—if earned—is reviewer calibration, consented outcome data, credential recognition, and a trusted candidate network, not parsing git.

## Risks
IP/NDA breach, false attribution, reviewer inconsistency, privacy law, cold-start trust, candidate gaming, discriminatory proxy signals, and incumbent bundling. Require employer-policy attestation, minimal fields, signed snapshots, appeal/revocation, reviewer calibration, retention limits, and legal review.

## Roadmap
- **0–30 days:** concierge packs, policy checklist, rubric calibration, $99 CTA.
- **31–60 days:** signed local extractor, expiring links, reviewer QA, five TA design partners.
- **61–90 days:** paid recruiter pilot, ATS-export format, outcome measurement, go/no-go against repeat requests.
