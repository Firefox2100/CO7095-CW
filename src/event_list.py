from __future__ import annotations

from rich import box
from rich.table import Table
from rich.text import Text

from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import (
    Static,
)

from_markup = Text.from_markup


def generate_header() -> Table:
    events = Table(
        show_edge=False,
        show_header=True,
        expand=True,
        row_styles=["none", "dim"],
        box=box.SIMPLE,
    )
    events.add_column(from_markup("[green]Time"), style="green", no_wrap=True, ratio=1)
    events.add_column(from_markup("[blue]Title"), style="blue", ratio=3)
    events.add_column(
        from_markup("[red]Urgency"),
        style="magenta",
        justify="right",
        no_wrap=True,
        ratio=1,
    )
    return events


class EventList(Container):
    def compose(self) -> ComposeResult:
        yield Static('Daily events', classes='daily_events_banner', id='daily_events_banner')
        yield Static(generate_header(), classes='event_table', id='event_table')
