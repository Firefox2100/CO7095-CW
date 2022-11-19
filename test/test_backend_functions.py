import backend_functions as bf
import hashlib
import pytest


class TestBackend:
    def test_login(self):
        username = "patrick"
        password = "password123"
        hashed_pass = hashlib.sha256(password.encode()).hexdigest()

        result = bf.login(username=username, password=hashed_pass)

        assert result == "fd583fc3-6b83-4056-873e-307c028ae8b3"

    @pytest.mark.raises(message="Error: Password error")
    def test_login_wrong_password(self):
        username = "patrick"
        password = "some random thing"
        hashed_pass = hashlib.sha256(password.encode()).hexdigest()

        result = bf.login(username=username, password=hashed_pass)

    @pytest.mark.raises(message="Error: User doesn't exist")
    def test_login_wrong_user(self):
        username = "some user"
        password = "password123"
        hashed_pass = hashlib.sha256(password.encode()).hexdigest()

        result = bf.login(username=username, password=hashed_pass)

    def test_add_event(self):
        time = "2022/11/20 10:30:00"
        title = "Test event"
        urgency = "None"
        uid = "fd583fc3-6b83-4056-873e-307c028ae8b3"

        result = bf.add_event(time=time, title=title, urgency=urgency, uid=uid)
        assert result == "Success"

    @pytest.mark.raises(message="Error: User token error")
    def test_add_event_wrong_user(self):
        time = "2022/11/20 10:30:00"
        title = "Test event"
        urgency = "None"
        uid = "something else"

        result = bf.add_event(time=time, title=title, urgency=urgency, uid=uid)

    def test_register(self):
        username = "test"
        password = "password123"
        hashed_pass = hashlib.sha256(password.encode()).hexdigest()

        result = bf.register(username=username, password=hashed_pass)

        assert not result.startswith("Error")

    @pytest.mark.raises(message="Error: User already exist")
    def test_register_user_exist(self):
        username = "patrick"
        password = "password123"
        hashed_pass = hashlib.sha256(password.encode()).hexdigest()

        result = bf.register(username=username, password=hashed_pass)

    def test_get_events(self):
        year = 2022
        month = 11
        day = 17
        uid = "fd583fc3-6b83-4056-873e-307c028ae8b3"

        result = bf.get_events(year=year, month=month, date=day, uid=uid)

        assert len(result) > 0

    def test_get_events_empty(self):
        year = 2022
        month = 11
        day = 1
        uid = "fd583fc3-6b83-4056-873e-307c028ae8b3"

        result = bf.get_events(year=year, month=month, date=day, uid=uid)

        assert len(result) == 0

    @pytest.mark.raises(message="Error: User token error")
    def test_get_events_wrong_user(self):
        year = 2022
        month = 11
        day = 17
        uid = "some-random-token"

        result = bf.get_events(year=year, month=month, date=day, uid=uid)
