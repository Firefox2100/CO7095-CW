from __future__ import annotations

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import (
    Button,
    Input,
    Static,
)


class AddEvent(Container):
    def compose(self) -> ComposeResult:
        yield Container(
            Input(placeholder="Time", id='input_time'),
            Input(placeholder="Title", id='input_title'),
            Input(placeholder="Urgency", id='input_urgency'),
            id='event_inputs',
            classes='event_inputs',
        )
        yield Button("Add", variant="primary", classes="addevent", id='addevent')
