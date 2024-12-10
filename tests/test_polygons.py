def test_create_polygon(client):
    response = client.post("/polygons/", json={"name": "Test Polygon", "coordinates": [[10.0, 20.0], [20.0, 30.0], [30.0, 10.0], [10.0, 20.0]]})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Polygon"

def test_get_polygons(client):
    response = client.get("/polygons/")
    assert response.status_code == 200
    assert len(response.json()) > 0
