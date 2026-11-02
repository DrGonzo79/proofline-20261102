from fastapi.testclient import TestClient
from api.main import app
client=TestClient(app)
def test_health(): assert client.get("/health").json()=={"status":"ok"}
def test_proof_pack_is_deterministic():
    body=client.post("/proof-packs",json={"candidate_id":"maya","consent":True}).json()
    assert body=={"candidate_id":"maya","score":92,"band":"verified","credential_id":"PF-MAYA-92","simulated":True}
def test_consent_required():
    response=client.post("/proof-packs",json={"candidate_id":"maya","consent":False})
    assert response.status_code==422 and "consent" in response.json()["detail"].lower()
def test_unknown_candidate(): assert client.post("/proof-packs",json={"candidate_id":"missing","consent":True}).status_code==404
