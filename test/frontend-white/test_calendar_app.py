import calendar_app
from textual.app import App
from textual.widgets import Static, Button
import datetime
import pytest
import asyncio
import random


class FakeButtonEvent:
    def __init__(self, id: str):
        self.button = Button("", id=id)


class TestCalendar:
    @pytest.mark.asyncio
    async def test_compose(self):
        target = calendar_app.Calendar()
        async with target.run_test() as pilot:
            await asyncio.sleep(3)
            assert pilot.app.query_one('#right_side').id == 'right_side'

    @pytest.mark.asyncio
    async def test_on_button_pressed(self):
        today = datetime.datetime.now()

        month = today.month
        year = today.year

        target = calendar_app.Calendar()
        async with target.run_test() as pilot:

            # Next month button
            await asyncio.sleep(1)
            pilot.app.on_button_pressed(FakeButtonEvent("next_month"))
            assert pilot.app.month == month % 12 + 1
            await asyncio.sleep(1)
            pilot.app.on_button_pressed(FakeButtonEvent("next_month"))
            assert pilot.app.month == (month + 1) % 12 + 1

            # Last month button
            await asyncio.sleep(1)
            pilot.app.on_button_pressed(FakeButtonEvent("last_month"))
            assert pilot.app.month == month % 12 + 1
            await asyncio.sleep(1)
            pilot.app.on_button_pressed(FakeButtonEvent("last_month"))
            assert pilot.app.month == month

            # Register button
            pilot.app.query_one('#username').value = "testuser"
            pilot.app.query_one('#password').value = "password123"
            await asyncio.sleep(1)
            pilot.app.on_button_pressed(FakeButtonEvent("register_button"))
            await asyncio.sleep(3)
            assert pilot.app.uid != ""

            # Login button
            pilot.app.query_one('#username').value = "patrick"
            pilot.app.query_one('#password').value = "password123"
            await asyncio.sleep(1)
            pilot.app.on_button_pressed(FakeButtonEvent("login_button"))
            await asyncio.sleep(3)
            assert pilot.app.uid == "fd583fc3-6b83-4056-873e-307c028ae8b3"

            # Select date button
            for i in range(5):
                r = random.randint(1, 28)
                pilot.app.on_button_pressed(FakeButtonEvent("date_" + str(r)))
                await asyncio.sleep(3)

            pilot.app.on_button_pressed(FakeButtonEvent("date_1"))
            await asyncio.sleep(3)

            # Add event button
            pilot.app.query_one('#input_time').value = "2022-12-16 10:00:00"
            pilot.app.query_one('#input_title').value = "Test"
            pilot.app.query_one('#input_urgency').value = "None"
            await asyncio.sleep(1)
            pilot.app.on_button_pressed(FakeButtonEvent("addevent"))
            await asyncio.sleep(3)
