import pytest
from app import compute_score, app

def test_compute_score():
    assert compute_score(10, 2) == 20

def test_compute_score_zero():
    assert compute_score(0, 999) == 0

def test_compute_score_rejects_negative():
    with pytest.raises(ValueError):
        compute_score(-1, 2)

def test_health_endpoint():
    client = app.test_client()
    res = client.get("/api/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"
