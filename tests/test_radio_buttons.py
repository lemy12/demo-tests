import pytest

from pages.radio_buttons import DemoRadioButtonsPage


@pytest.mark.radio_button
def test_radio_button(browser):
    page = DemoRadioButtonsPage(browser)

    # Load webpage
    page.load()

    # Assert that every radios text is in given result
    for each in page.check_radio_button():
        assert each[0] in each[1]



