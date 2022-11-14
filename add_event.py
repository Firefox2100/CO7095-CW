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
        yield Static("Time", classes="label")
        yield Input(placeholder="Time", id='input_time')
        yield Static("Title", classes="label")
        yield Input(placeholder="Title", id='input_title')
        yield Static("Urgency", classes="label")
        yield Input(placeholder="Urgency", id='input_urgency')
        yield Button("Add", variant="primary", classes="add event button", id='addevent')

    def get_value(self) -> dict:
        result = {'time': self.query_one("#input_time").value, 'title': self.query_one("#input_title").value,
                  'urgency': self.query_one("#input_urgency").value}
        return result

    def add_event(self):
        pass


class AddEventTest(App):
    def compose(self) -> ComposeResult:
        yield AddEvent()


if __name__ == '__main__':
    AddEventTest().run()
