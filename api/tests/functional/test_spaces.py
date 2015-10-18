import json


def test_get_spaces_get_ok(client):
    response = client.get('/spaces')

    assert response.status_code == 200
    assert type(response.data) == str

    data_struct = json.loads(response.data)
    assert type(data_struct) == list


def test_get_spaces_post_ok(client):
    wrong_data = client.post('/spaces', data=json.dumps({'test': 'nok'}), content_type='application/json')
    assert wrong_data.status_code == 500
    assert "Missing mandatory" in wrong_data.data


def test_get_spaces_nok(client):
    assert client.put('/spaces').status_code == 405
    assert client.delete('/spaces').status_code == 405
