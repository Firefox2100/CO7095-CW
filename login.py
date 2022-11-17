from textual.app import App, ComposeResult

from textual.containers import Container
from textual.widgets import Button, Input


class Login(Container):
    def compose(self) -> ComposeResult:
        yield Container(
            Input(placeholder="Username", id="username"),
            Input(placeholder="Password", id="password", password=True),
            classes="login_input"
        )

        yield Button(label="Login", variant="primary", id="login_button")
