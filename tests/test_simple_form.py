import pytest

from pages.simple_form import DemoSimpleFormPage

PHRASE = ['text', '!@#abc123 ']
NUMBER = [('1', '2', '3'), ('-1', '2', '1'), ('1', 'one', 'NaN')]


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


@pytest.mark.two_input
@pytest.mark.parametrize('a,b,expected', NUMBER)
def test_two_input(browser, a, b, expected):
    page = DemoSimpleFormPage(browser)

    # Load webpage
    page.load()

    # Assert that total shows correct sum
    assert page.check_two_input(a, b) == expected


@pytest.mark.simple_form
def test_simple_form(browser):
    page = DemoSimpleFormPage(browser)

    # Load webpage
    page.load()

    # Assert that textboxes have placeholder messages
    for each in page.placeholder_message():
        assert each.get_attribute("placeholder") and each.get_attribute("placeholder") != ""
