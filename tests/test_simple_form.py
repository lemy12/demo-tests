import pytest

from pages.simple_form import DemoSimpleFormPage


@pytest.mark.parametrize('phrase', ['yes', 'no', '123', ''])
def test_single_input(browser, phrase):
    page = DemoSimpleFormPage(browser)

    page.load()

    result = page.check_single_input(phrase)

    assert phrase == result
