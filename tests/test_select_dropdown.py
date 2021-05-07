import pytest

from pages.select_dropdown import DemoSelectDropdownPage

# Parametrize globals
DAY = ['Sunday', 'Saturday']


@pytest.mark.select_dropdown
@pytest.mark.parametrize('day', DAY)
def test_radio_button(browser, day):
    page = DemoSelectDropdownPage(browser)

    # Load webpage
    page.load()

    # Assert that chosen day is in result message
    assert day in page.check_select_list(day)


