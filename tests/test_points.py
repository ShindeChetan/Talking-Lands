def test_create_point(client):
    response = client.post("/points/", json={"name": "Test Point", "coordinates": [10.0, 20.0]})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Point"

def test_get_points(client):
    response = client.get("/points/")
    assert response.status_code == 200
    assert len(response.json()) > 0
