from fastapi.testclient import TestClient # Use TestClient to make mock HTTP requests to the API.
from app.main import app  

# Instantiate the application itself
client = TestClient(app)

def test_get_uf_current_date():
    valid_date = "01-01-2023"

    # We make a simulated HTTP request to the route /api/v1/uf/{date}
    response = client.get(f"/api/v1/uf/{valid_date}")

    # Verify that the response has a status code 200 (OK), in format JSON and match the UfResponse model
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert "date" in response.json()
    assert "uf_value" in response.json()

