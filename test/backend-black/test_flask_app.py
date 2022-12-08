import flask_app
import json
import pytest
from flask import url_for


class TestFlask:
    def test_get_events(self):
        client = flask_app.app.test_client()

        # Good retrieve with data
        result = client.get("http://localhost:5000/events/fd583fc3-6b83-4056-873e-307c028ae8b3/11-17-22")
        assert result.status_code == 200
        assert len(json.loads(result.data)) == 2

        # Good retrieve with no data
        result = client.get("http://localhost:5000/events/fd583fc3-6b83-4056-873e-307c028ae8b3/11-17-21")
        assert result.status_code == 200
        assert len(json.loads(result.data)) == 0

        # Wrong UID with data
        result = client.get("http://localhost:5000/events/fd583fc3-6b83-4056-873e/11-17-22")
        assert result.status_code == 403

        # Wrong UID with no data
        result = client.get("http://localhost:5000/events/fd583fc3-6b83-4056-873e/11-17-21")
        assert result.status_code == 403

        # Missing arguments
        result = client.get("http://localhost:5000/events/fd583fc3-6b83-4056-873e-307c028ae8b3")
        assert result.status_code == 404

        # Wrong format of date
        result = client.get("http://localhost:5000/events/fd583fc3-6b83-4056-873e-307c028ae8b3/11-17-")
        assert result.status_code == 400

        # Wrong end point
        result = client.get("http://localhost:5000/event/fd583fc3-6b83-4056-873e-307c028ae8b3/11-17-22")
        assert result.status_code == 404

    def add_event(self):
        client = flask_app.app.test_client()

        json_data = {"time": "2022/11/20 10:30:00", "title": "Test event", "urgency": "high"}
        json_data_wrong_content = {"time": "2022/11/22 10:3", "title": "Test event", "urgency": "high"}
        json_data_wrong_format = {"time": "2022/11/20 10:30:00", "title": "Test event"}

        # Post with good data
        result = client.post("http://localhost:5000/events/fd583fc3-6b83-4056-873e-307c028ae8b3", json=json_data)
        assert result.status_code == 200

        # Post with wrong UID
        result = client.post("http://localhost:5000/events/fd583fc3-6b83-4056-873e", json=json_data)
        assert result.status_code == 403

        # Post with wrong end point
        result = client.post("http://localhost:5000/event/fd583fc3-6b83-4056-873e-307c028ae8b3", json=json_data)
        assert result.status_code == 404

        # Post with missing argument
        result = client.post("http://localhost:5000/events", json=json_data)
        assert result.status_code == 404

        # Post with wrong content format
        result = client.post("http://localhost:5000/events/fd583fc3-6b83-4056-873e-307c028ae8b3", json=json_data_wrong_content)
        assert result.status_code == 400

        # Post with wrong json format
        result = client.post("http://localhost:5000/events/fd583fc3-6b83-4056-873e-307c028ae8b3", json=json_data_wrong_format)
        assert result.status_code == 400

    def test_login(self):
        client = flask_app.app.test_client()

        json_data = {"username": "patrick", "password": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"}
        json_data_wrong_content = {"username": "patrick", "password": "something wrong"}
        json_data_wrong_format = {"username": "patrick"}

        # Post with good data
        result = client.post("http://localhost:5000/login", json=json_data)
        assert result.status_code == 200
        assert result.data.decode() == "fd583fc3-6b83-4056-873e-307c028ae8b3"

        # Post with wrong content
        result = client.post("http://localhost:5000/login", json=json_data_wrong_content)
        assert result.status_code == 403

        # Post with wrong json format
        result = client.post("http://localhost:5000/login", json=json_data_wrong_format)
        assert result.status_code == 400

        # Post with wrong end point
        result = client.post("http://localhost:5000/logi", json=json_data)
        assert result.status_code == 404

    def test_register(self):
        client = flask_app.app.test_client()

        json_data = {"username": "test_user_10", "password": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"}
        json_data_wrong_content = {"username": "patrick", "password": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"}
        json_data_wrong_format = {"username": "test_user_10"}

        # Post with good data
        result = client.post("http://localhost:5000/register", json=json_data)
        assert result.status_code == 200

        # Post with wrong content
        result = client.post("http://localhost:5000/register", json=json_data_wrong_content)
        assert result.status_code == 403

        # Post with wrong json format
        result = client.post("http://localhost:5000/register", json=json_data_wrong_format)
        assert result.status_code == 400

        # Post with wrong end point
        result = client.post("http://localhost:5000/regi", json=json_data)
        assert result.status_code == 404
