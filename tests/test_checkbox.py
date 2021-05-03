import pytest

from pages.checkbox import DemoCheckboxPage


@pytest.mark.single_checkbox
def test_single_checkbox(browser):
    page = DemoCheckboxPage(browser)

    # Load webpage
    page.load()

    # Assert that the message is shown after clicking button
    assert page.check_single_checkbox() == 'block'

    # Assert that the message is hidden after clicking button again
    assert page.check_single_checkbox() == 'none'


@pytest.mark.multiple_checkbox
@pytest.mark.multiple_checkbox_button
def test_multiple_checkbox_button(browser):
    page = DemoCheckboxPage(browser)

    # Load webpage
    page.load()

    # Assert that checkboxes become checked after clicking button
    hidden, check_value = page.check_multiple_checkall_button()
    assert hidden == "true" and check_value == "Uncheck All"

    # Assert that checkboxes become unchecked after clicking button again
    hidden, check_value = page.check_multiple_checkall_button()
    assert hidden == "false" and check_value == "Check All"


@pytest.mark.multiple_checkbox
@pytest.mark.multiple_checkbox_manual
def test_multiple_checkbox_manual(browser):
    page = DemoCheckboxPage(browser)

    # Load webpage
    page.load()

    # Assert that checkboxes become checked after clicking button
    hidden, check_value = page.check_multiple_checkall_manual()
    assert hidden == "true" and check_value == "Uncheck All"

    # Assert that checkboxes become unchecked after clicking button again
    hidden, check_value = page.check_multiple_checkall_manual()
    assert hidden == "false" and check_value == "Check All"
