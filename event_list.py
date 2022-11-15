from __future__ import annotations

from rich import box
from rich.table import Table
from rich.text import Text

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import (
    Static,
)

from_markup = Text.from_markup


class EventTable(Static):
    events = Table(
        show_edge=False,
        show_header=True,
        expand=True,
        row_styles=["none", "dim"],
        box=box.SIMPLE,
    )

    def __init__(self):
        # Adding titles
        super().__init__()
        self.add_title()

    def add_title(self):
        self.events.add_column(from_markup("[green]Time"), style="green", no_wrap=True)
        self.events.add_column(from_markup("[blue]Title"), style="blue")
        self.events.add_column(
            from_markup("[magenta]Urgency"),
            style="magenta",
            justify="right",
            no_wrap=True,
        )

    def add_event(self, time: str, title: str, urgency: str):
        self.events.add_row(
            time,
            title,
            urgency,
        )

    def to_table(self) -> Table:
        return self.events

    # TODO: Implement this
    def fetch_events(self, date):
        pass


class EventList(Container):
    event_table = EventTable()

    def compose(self) -> ComposeResult:
        # self.event_table.fetch_events()
        if self.event_table.events.row_count == 0:
            self.event_table.add_event("None", "None", "None")

        yield Static('Daily events', classes='daily_events_banner')
        yield Static(self.event_table.to_table())


class EventListTest(App):
    def compose(self) -> ComposeResult:
        yield EventList()


if __name__ == '__main__':
    EventListTest().run()
