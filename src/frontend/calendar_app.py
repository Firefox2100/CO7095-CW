from __future__ import annotations
import datetime
import hashlib

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.reactive import var
from textual.widgets import (
    Button,
    Header,
    Static,
)

import event_list
import add_event
import dates
import login
import backend_functions as bf


class Calendar(App):
    CSS_PATH = "calendar.css"
    TITLE = "CALENDAR"
    host = "localhost"
    user = ""
    password = ""
    uid = ""

    today = datetime.datetime.now()

    month = var(today.month)
    year = today.year
    selected_date = 1

    def compose(self) -> ComposeResult:
        yield Container(
            Header(show_clock=True, classes='app_header'),
            Container(
                Container(
                    event_list.EventList(),
                    Static("Message: None", id='messagebox'),
                    login.Login(),
                    id='right_side'
                ),
                Container(
                    dates.Dates(self.month, self.year, id='dates'),
                    add_event.AddEvent(),
                    id='left_side'
                ))

        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        assert button_id is not None
        if button_id == 'last_month':
            if self.month == 1:
                self.year -= 1
                self.month = 12
            else:
                self.month -= 1
        elif button_id == 'next_month':
            if self.month == 12:
                self.year += 1
                self.month = 1
            else:
                self.month += 1
        elif button_id.startswith('date_'):
            if self.uid == "":
                self.show_error(Exception("Please login first"))
            else:
                self.selected_date = int(button_id[5:])
                self.fetch_events(year=self.year, month=self.month, date=self.selected_date)
        elif button_id == 'login_button':
            self.user = self.query_one('#username').value
            self.password = hashlib.sha256(self.query_one('#password').value.encode())
            try:
                self.uid = bf.login(self.user, self.password.hexdigest())
            except Exception as e:
                self.show_error(e)
        elif button_id == 'register_button':
            self.user = self.query_one('#username').value
            self.password = hashlib.sha256(self.query_one('#password').value.encode())
            try:
                self.uid = bf.register(self.user, self.password.hexdigest())
            except Exception as e:
                self.show_error(e)
        elif button_id == 'addevent':
            if self.uid == "":
                self.show_error(Exception("Please login first"))
            else:
                time = self.query_one('#input_time').value
                title = self.query_one('#input_title').value
                urgency = self.query_one('#input_urgency').value
                try:
                    bf.add_event(time, title, urgency, self.uid)
                except Exception as e:
                    self.show_error()

    def show_error(self, e: Exception):
        self.query_one('#messagebox').update("Message: " + str(e))
        pass

    def watch_month(self, month: int) -> None:
        self.query_one("#month_name").update(dates.month_name.get(month))
        self.query_one('#clickable_dates').remove()
        self.query_one('#dates').mount(dates.ClickableDates(self.month, self.year, id='clickable_dates'))

    def fetch_events(self, year: int, month: int, date: int):
        events = event_list.generate_header()

        try:
            eventl = bf.get_events(year, month, date, self.uid)

            for r in eventl:
                events.add_row(r[1][17:26], r[2], r[3])

            self.query_one('#event_table').update(events)
            self.query_one('#daily_events_banner').update('Daily events on ' + str(self.selected_date) + '/' + str(self.month))
        except Exception as e:
            self.show_error(e)


if __name__ == '__main__':
    app = Calendar()
    app.run()
