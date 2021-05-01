import pytest

from pages.checkbox import DemoCheckboxPage


@pytest.mark.single_checkbox
def test_single_checkbox(browser):
    page = DemoCheckboxPage(browser)

    # Load webpage
    page.load()

    # Assert that the message is shown
    assert page.check_single_checkbox().value_of_css_property('display') == 'block'

    # Assert that the message is hidden
    assert page.check_single_checkbox().value_of_css_property('display') == 'none'
