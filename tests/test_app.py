import pytest

from app import app


@pytest.fixture
def client():
    app.config.update(TESTING=True)
    return app.test_client()


def test_index_returns_service_info(client):
    response = client.get("/")
    assert response.status_code == 200
    body = response.get_json()
    assert body["service"] == "Back-py"
    assert "version" in body


def test_health_endpoint_reports_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_greet_uses_the_name_in_the_path(client):
    response = client.get("/api/greet/Kachi")
    assert response.status_code == 200
    assert response.get_json()["greeting"] == "Hello, Kachi!"


def test_sum_adds_two_integers(client):
    response = client.get("/api/sum?a=2&b=3")
    assert response.status_code == 200
    assert response.get_json()["sum"] == 5


@pytest.mark.parametrize("query", ["", "?a=2", "?a=two&b=3", "?a=2&b=3.5"])
def test_sum_rejects_missing_or_non_integer_input(client, query):
    response = client.get(f"/api/sum{query}")
    assert response.status_code == 400
    assert "error" in response.get_json()
