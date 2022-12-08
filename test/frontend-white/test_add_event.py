import add_event
from textual.app import App
import pytest

pytest_plugins = ('pytest_asyncio',)


class TestAddEvent:
    @pytest.mark.asyncio
    async def test_compose(self):
        async with App().run_test() as pilot:
            child = add_event.AddEvent()
            await pilot.app.mount(child)
            assert pilot.app.query_one('#event_inputs').id == 'event_inputs'

        assert True
