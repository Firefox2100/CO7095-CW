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
    0: 'January',
    1: 'February',
    2: 'March',
    3: 'April',
    4: 'May',
    5: 'June',
    6: 'July',
    7: 'August',
    8: 'September',
    9: 'October',
    10: 'November',
    11: 'December'
}


class DatesBanner(Container):
    def compose(self) -> ComposeResult:
        yield Button("<-", variant="primary", classes="last month button", id='last_month')
        yield Static(month_name.get(10), classes='month name', id='month_name')
        yield Button("->", variant="primary", classes="next month button", id='next_month')


class ClickableDates(Container):
    def compose(self) -> ComposeResult:
        yield Static('Mon')
        yield Static('Tue')
        yield Static('Wed')
        yield Static('Thu')
        yield Static('Fri')
        yield Static('Sat')
        yield Static('Sun')


class Dates(Container):
    def compose(self) -> ComposeResult:
        yield DatesBanner(id='date_banner')


class DatesTest(App):
    month = var(7)

    def compose(self) -> ComposeResult:
        yield DatesBanner(id='date_banner')

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        assert button_id is not None
        if button_id == 'last_month':
            self.month -= 1
        elif button_id == 'next_month':
            self.month += 1
    
    def watch_month(self, month: int) -> None:
        self.query_one("#date_banner").query_one("#month_name").update(month_name.get(month))


if __name__ == '__main__':
    DatesTest().run()
