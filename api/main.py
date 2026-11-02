from pathlib import Path
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
app = FastAPI(title="Proofline API", version="0.1.0")
CANDIDATES = {c["id"]: c for c in json.loads((Path(__file__).parents[1] / "data/demo_candidates.json").read_text())}
class ProofRequest(BaseModel):
    candidate_id: str = Field(min_length=1, max_length=80)
    consent: bool
def assess(candidate: dict) -> dict:
    repo, defense = candidate["repo"], candidate["defense"]
    score = round(min(30, repo["active_weeks"] / 4) + min(25, (repo["merged_prs"] + repo["reviewed_prs"] * .35) / 5) + min(15, repo["months"] * .6) + sum(defense.values()) / 15 * 30)
    band = "verified" if score >= 78 else "review" if score >= 60 else "insufficient"
    return {"candidate_id": candidate["id"], "score": score, "band": band, "credential_id": f"PF-{candidate['id'].upper()}-{score}", "simulated": True}
@app.get("/health")
def health(): return {"status": "ok"}
@app.post("/proof-packs")
def create_proof(req: ProofRequest):
    candidate = CANDIDATES.get(req.candidate_id)
    if not candidate: raise HTTPException(404, "Unknown demo candidate")
    if not req.consent: raise HTTPException(422, "Candidate consent is required")
    return assess(candidate)
