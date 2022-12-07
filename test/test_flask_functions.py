import flask_functions


class TestFlaskFunctions:
    def test_get_event(self):
        token = "fd583fc3-6b83-4056-873e-307c028ae8b3"
        wrong_token = "something random"
        date = "11-17-22"
        date_empty = "11-10-22"
        result = flask_functions.get_event(token, date)
        assert len(result) == 2
        result = flask_functions.get_event(token, date_empty)
        assert len(result) == 0
        result = flask_functions.get_event(wrong_token, date)
        assert result == "User token error"

    def test_add_event(self):
        token = "fd583fc3-6b83-4056-873e-307c028ae8b3"
        wrong_token = "something random"
        data = {
            "time": "2022/11/20 10:30:00",
            "title": "Test event",
            "urgency": "high",
        }

        result = flask_functions.add_event(wrong_token, data)
        assert result == "User token error"
        result = flask_functions.add_event(token, data)
        assert result

    def test_register(self):
        data = {
            "username": "test_user",
            "password": "password123",
        }
        data_duplicate = {
            "username": "test_user",
            "password": "password123",
        }

        result = flask_functions.register(data)
        assert type(result) == str
        result = flask_functions.register(data_duplicate)
        assert result == "User already exist"

    def test_login(self):
        data = {
            "username": "patrick",
            "password": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f",
        }
        data_wrong_pass = {
            "username": "test_user",
            "password": "something_wrong",
        }
        data_wrong_user = {
            "username": "some_wrong_user",
            "password": "password123",
        }

        result = flask_functions.login(data)
        assert result == "fd583fc3-6b83-4056-873e-307c028ae8b3"
        result = flask_functions.login(data_wrong_pass)
        assert result == "Password error"
        result = flask_functions.login(data_wrong_user)
        assert result == "User doesn't exist"
