import requests
import json

backend_url = "http://localhost:5000"


def login(username: str, password: str) -> str:
    r = requests.post(backend_url + "/login", json={"username": username, "password": password})
    if r.status_code != 200:
        raise Exception("Error: " + r.content.decode())

    return r.content.decode()


def add_event(time: str, title: str, urgency: str, uid: str) -> str:
    r = requests.post(backend_url + "/add/" + uid, json={"time": time, "title": title, "urgency": urgency})

    if r.status_code != 200:
        raise Exception("Error: " + r.content.decode())

    return r.content.decode()


def get_events(year: int, month: int, date: int, uid: str) -> list:
    url = backend_url + "/events/" + uid + "/" + str(month) + "-" + str(date) + "-" + str(year-2000)

    r = requests.get(url)

    if r.status_code != 200:
        raise Exception("Error: " + r.content.decode())

    return json.loads(r.content)


def register(username: str, password: str) -> str:
    r = requests.post(backend_url + "/register", json={"username": username, "password": password})
    if r.status_code != 200:
        raise Exception("Error: " + r.content.decode())

    return r.content.decode()
