from __future__ import annotations

from importlib_metadata import version
from pathlib import Path

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

import event_list


class Calendar(App):
    CSS_PATH = "calendar.css"
    TITLE = "Textual Demo"

    def compose(self) -> ComposeResult:
        yield Container(
            Header(show_clock=True),
            event_list.EventList()
        )
