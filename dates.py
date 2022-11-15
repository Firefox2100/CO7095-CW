from __future__ import annotations

import datetime

from rich import box
from rich.console import RenderableType
from rich.json import JSON
from rich.markdown import Markdown
from rich.pretty import Pretty
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Horizontal
from textual.reactive import reactive, watch
from textual.reactive import var
from textual.widgets import (
    Button,
    Checkbox,
    DataTable,
    Footer,
    Header,
    Input,
    Static,
    TextLog,
)

month_name = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}


def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def days_in_month(month, year):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month == 2:
        if leap_year(year):
            return 29
        return 28
    return 30


class DatesBanner(Container):

    def __init__(self, month: int, id: str):
        super().__init__()
        self.month = month
        self.id = id

    def compose(self) -> ComposeResult:
        yield Button("<-", variant="primary", classes="last month button", id='last_month')
        yield Static(month_name.get(10), classes='month name', id='month_name')
        yield Button("->", variant="primary", classes="next month button", id='next_month')


class ClickableDates(Container):
    month: int
    year: int

    def __init__(self, month: int, year: int, id: str):
        super().__init__()
        self.month = month
        self.year = year
        self.id = id

    def compose(self) -> ComposeResult:
        calendar_date = datetime.datetime(year=self.year, month=self.month, day=1)
        daysinmonth = days_in_month(self.month, self.year)

        yield Static('Mon')
        yield Static('Tue')
        yield Static('Wed')
        yield Static('Thu')
        yield Static('Fri')
        yield Static('Sat')
        yield Static('Sun')

        for i in range(calendar_date.weekday()):
            yield Static(' ', classes='calendar_place_holder')

        for i in range(1, daysinmonth + 1):
            yield Button(str(i), id=('date_' + str(i)), classes='dates')


class Dates(Container):
    month: int
    year: int

    def __init__(self, month: int, year: int, id: str):
        super().__init__()
        self.month = month
        self.year = year
        self.id = id

    def compose(self) -> ComposeResult:
        yield DatesBanner(self.month, id='date_banner')
        yield ClickableDates(self.month, self.year, id='clickable_dates')


class DatesTest(App):
    month = var(7)

    def compose(self) -> ComposeResult:
        # yield DatesBanner(11, id='date_banner')
        yield Dates(11, 2022, id='dates')

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        assert button_id is not None
        if button_id == 'last_month':
            self.month -= 1
        elif button_id == 'next_month':
            self.month += 1

    def watch_month(self, month: int) -> None:
        self.query_one("#month_name").update(month_name.get(month))


if __name__ == '__main__':
    DatesTest().run()
