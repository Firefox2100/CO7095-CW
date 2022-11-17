from __future__ import annotations
import datetime

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.reactive import var
from textual.widgets import (
    Button,
    Header,
)

import event_list
import add_event
import dates
import login

import mysql.connector


class Calendar(App):
    CSS_PATH = "calendar.css"
    TITLE = "CALENDAR"
    host = "localhost"
    user = ""
    password = ""
    mydb = None

    today = datetime.datetime.now()

    month = var(today.month)
    year = today.year
    selected_date = 1

    def compose(self) -> ComposeResult:
        yield Container(
            Header(name='Puppy', show_clock=True, classes='app_header'),
            Container(
                Container(
                    event_list.EventList(),
                    login.Login(),
                    id='right_side'
                ),
                Container(
                    dates.Dates(self.month, self.year, id='dates'),
                    add_event.AddEvent(),
                    id='left_side'
                ))

        )

    def login(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            port="3306",
            user=self.user,
            password=self.password,
            database="co7095"
        )

    def add_event(self):
        time = self.query_one('#input_time').value
        title = self.query_one('#input_title').value
        urgency = self.query_one('#input_urgency').value

        mycursor = self.mydb.cursor()

        sql_query = "INSERT INTO `events`(`date`, `title`, `urgency`, `user`) VALUES ( %s , %s , %s , %s );"
        val = (time, title, urgency, self.user)

        mycursor.execute(sql_query, val)
        self.mydb.commit()

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
            self.selected_date = int(button_id[5:])
            self.fetch_events(year=self.year, month=self.month, date=self.selected_date)
        elif button_id == 'login_button':
            self.user = self.query_one('#username').value
            self.password = self.query_one('#password').value
            self.login()
        elif button_id == 'addevent':
            self.add_event()


    def watch_month(self, month: int) -> None:
        self.query_one("#month_name").update(dates.month_name.get(month))
        self.query_one('#clickable_dates').remove()
        self.query_one('#dates').mount(dates.ClickableDates(self.month, self.year, id='clickable_dates'))

    def fetch_events(self, year: int, month: int, date: int):
        events = event_list.generate_header()

        begin_date = "'" + str(year) + "-" + str(month) + "-" + str(date) + "'"
        end_date = "'" + str(year) + "-" + str(month) + "-" + str(date + 1) + "'"

        mycursor = self.mydb.cursor()
        sql_query = "SELECT * FROM events WHERE user = '" + self.user + "' AND date >= " + begin_date + "AND date <" + end_date
        mycursor.execute(sql_query)
        myresult = mycursor.fetchall()

        for r in myresult:
            events.add_row(r[1].strftime("%H:%M"), r[2], r[3])

        self.query_one('#event_table').update(events)
        self.query_one('#daily_events_banner').update('Daily events on ' + str(self.today.day) + '/' + str(self.month))


if __name__ == '__main__':
    app = Calendar()
    app.run()
