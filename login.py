from textual.app import App, ComposeResult

from textual.containers import Container
from textual.widgets import Button, Input


class Login(Container):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Username", id="username")
        yield Button(label="Login", variant="primary", id="login_button")
