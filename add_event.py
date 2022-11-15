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
            id='event_inputs'
        )
        yield Button("Add", variant="primary", classes="add_event_button", id='addevent')

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
