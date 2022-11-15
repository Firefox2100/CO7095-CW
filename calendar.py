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


class Calendar(App):
    CSS_PATH = "calendar.css"
    TITLE = "Textual Demo"

    today = datetime.datetime.now()

    month = var(today.month)
    year = today.year

    def compose(self) -> ComposeResult:
        yield Container(
            Header(name='Puppy',show_clock=True, classes='app_header'),
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

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        assert button_id is not None
        if button_id == 'last_month':
            self.month -= 1
        elif button_id == 'next_month':
            self.month += 1

        # TODO: Implement the buttons of dates, add event and login
        pass

    def watch_month(self, month: int) -> None:
        self.query_one("#month_name").update(dates.month_name.get(month))
        self.query_one('#clickable_dates').remove()
        self.query_one('#dates').mount(dates.ClickableDates(self.month, self.year, id='clickable_dates'))


if __name__ == '__main__':
    app = Calendar()
    app.run()
