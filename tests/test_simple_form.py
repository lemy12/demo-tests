import pytest

from pages.simple_form import DemoSimpleFormPage

PHRASE = ['text']
NUMBER = [('1', '2', '3'), ('-1', '2', '1')]


@pytest.mark.single_input
@pytest.mark.parametrize('phrase', PHRASE)
def test_single_input(browser, phrase):
    page = DemoSimpleFormPage(browser)

    # Load webpage
    page.load()

    # Assert that form shows written phrase
    assert page.check_single_input(phrase) == phrase

    # Assert that form changes to new message
    assert page.check_single_input("message") == "message"

    # Assert that textbox has placeholder message
    assert page.placeholder_message() and page.placeholder_message() != ""


@pytest.mark.two_input
@pytest.mark.parametrize('a,b,expected', NUMBER)
def test_single_input(browser, a, b, expected):
    page = DemoSimpleFormPage(browser)

    # Load webpage
    page.load()

    # Assert that total show correct sum
    assert page.check_two_input(a, b) == expected
