import pytest

from pages.input_form import DemoInputFormPage

# Parametrize globals
NAME = ['John', '', 'A', '123']


@pytest.mark.input_form
@pytest.mark.parametrize('name', NAME)
def test_select_list(browser, name):
    page = DemoInputFormPage(browser)

    # Load webpage
    page.load()

    # Assert that chosen day is in result message
    error1, error2 = page.check_name(name)
    assert error1 == "none" and error2 == "none"
