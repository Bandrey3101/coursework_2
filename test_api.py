import pytest

from app import app

def test_app():
    response = app.test_client().get('/api/', follow_redirects=True)
    assert response.status_code == 200

    assert isinstance(response.json, list)

    needed_keys = {'content', 'poster_name', 'poster_avatar', 'pic', 'views_count', 'likes_count', 'pk'}

    for el in response.json:
        assert el.keys() == needed_keys


def test_app2():
    response = app.test_client().get('/api/1', follow_redirects=True)
    assert response.status_code == 200
    needed_keys = {'content', 'poster_name', 'poster_avatar', 'pic', 'views_count', 'likes_count', 'pk'}

    for key in needed_keys:
        assert key in response.json.keys()
