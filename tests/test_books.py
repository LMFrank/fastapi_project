# -*- coding: utf-8 -*-
import json
import pytest
from app.api.api_1_0 import crud
from app.configs import API_PREFIX


def test_create_book(test_app, monkeypatch):
    test_request_payload = {"book": "aaa", "author": "bbb"}
    test_response_payload = {"id": 1, "book": "aaa", "author": "bbb"}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    response = test_app.post(API_PREFIX + "/book", data=json.dumps(test_request_payload))
    assert response.status_code == 201
    assert response.json() == test_response_payload

def test_create_book_invalid_json(test_app):
    response = test_app.post(API_PREFIX + "/book", data=json.dumps({"book": "smart"}))
    assert response.status_code == 422

    response = test_app.post(API_PREFIX + "/book", data=json.dumps({"book": "1"*33, "author": "1"*33}))
    assert response.status_code == 422

def test_get_book_by_id(test_app, monkeypatch):
    test_data = {
        "id": 1,
        "book": "aaa",
        "author": "bbb"
    }

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get(API_PREFIX + "/book/1")

    assert response.status_code == 200
    assert response.json() == test_data

def test_get_book_by_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get(API_PREFIX + "/book/9999")
    print(response.json())
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"

    response = test_app.get(API_PREFIX + "/book/0")
    assert response.status_code == 422

def test_get_all_books(test_app, monkeypatch):
    test_data = [
        {"book": "aaa", "author": "bbb", "id": 1},
        {"book": "ccc", "author": "ddd", "id": 1}
    ]

    async def mock_get_all():
        return test_data

    monkeypatch.setattr(crud, "get_all", mock_get_all)

    response = test_app.get(API_PREFIX + "/book")
    assert response.status_code == 200
    assert response.json() == test_data

def test_update_book(test_app, monkeypatch):
    test_update_data = {"book": "aaa", "author": "bbb", "id": 1}

    async def mock_get(id):
        return True

    monkeypatch.setattr(crud, "get", mock_get)

    async def mock_put(id, payload):
        return 1

    monkeypatch.setattr(crud, "put", mock_put)

    response = test_app.put(API_PREFIX + "/book/1", data=json.dumps(test_update_data))
    assert response.status_code == 200
    assert response.json() == test_update_data

@pytest.mark.parametrize(
    "id, payload, status_code",
    [
        [1, {}, 422],
        [1, {"author": "bbb"}, 422],
        [9999, {"book": "aaa", "author": "bbb"}, 404],
        [1, {"book": "a", "author": "bbb"}, 422],
        [1, {"book": "aaa", "author": "b"}, 422],
        [0, {"book": "aaa", "author": "bbb"}, 422],
    ]
)
def test_update_book_invalid(test_app, monkeypatch, id, payload, status_code):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.put(API_PREFIX + f"/book/{id}", data=json.dumps(payload))
    assert response.status_code == status_code

def test_remove_book(test_app, monkeypatch):
    test_data = {"book": "aaa", "author": "bbb", "id": 1}

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    async def mock_delete(id):
        return id

    monkeypatch.setattr(crud, "delete", mock_delete)

    response = test_app.delete(API_PREFIX + "/book/1")
    assert response.status_code == 200
    assert response.json() == test_data

def test_remove_book_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.delete(API_PREFIX + "/book/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"

    response = test_app.delete(API_PREFIX + "/book/0")
    assert response.status_code == 422