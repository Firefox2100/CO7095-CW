import dates
from textual.app import App
import datetime
import pytest


class TestDates:
    def test_leap_year(self):
        assert dates.leap_year(2000)
        assert not dates.leap_year(2001)
        assert dates.leap_year(2004)
        assert not dates.leap_year(2100)

    def test_days_in_month(self):
        assert dates.days_in_month(1, 2022) == 31
        assert dates.days_in_month(2, 2022) == 28
        assert dates.days_in_month(4, 2022) == 30
        assert dates.days_in_month(2, 2000) == 29

    @pytest.mark.asyncio
    async def test_compose(self):
        async with App().run_test() as pilot:
            today = datetime.datetime.now()

            month = today.month
            year = today.year
            child = dates.Dates(month, year, 'dates')
            await pilot.app.mount(child)
            assert pilot.app.query_one('#date_banner').id == 'date_banner'
            assert pilot.app.query_one('#clickable_dates').id == 'clickable_dates'

        assert True
