from collector_backend import create_app


def test_config():
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def read_test_file(filename):
    fp = open(filename)
    data = fp.read()
    fp.close()

    return data


def test_event_report(client):
    response = client.get("/event/report/")
    assert response.status_code == 404  # NOT FOUND

    response = client.get("/event/report")
    assert response.status_code == 405  # NOT ALLOWED

    data = read_test_file('./tests/json/correct.json')
    response = client.post("/event/report", data=data, content_type='application/json')
    assert response.status_code == 200

    data = read_test_file('./tests/json/incorrect_format.json')
    response = client.post("/event/report", data=data, content_type='application/json')
    assert response.status_code == 422

    data = read_test_file('./tests/json/broken_format.json')
    response = client.post("/event/report", data=data, content_type='application/json')
    assert response.status_code == 400
