import pytest

from pages.input_form import DemoInputFormPage

# Parametrize globals
TEMP = [{"input_type": "first_name", "text": "Smith", "stringLength": "none", "notEmpty": "none"},
        {"input_type": "first_name", "text": "", "stringLength": "none", "notEmpty": "block"},
        {"input_type": "last_name", "text": "Smith", "stringLength": "none", "notEmpty": "none"},
        {"input_type": "last_name", "text": "A", "stringLength": "block", "notEmpty": "none"},
        {"input_type": "email", "text": "abc@gmail.com", "emailAddress": "none", "notEmpty": "none"},
        {"input_type": "email", "text": "abc@gmail.", "emailAddress": "block", "notEmpty": "none"}]


@pytest.mark.input_form_temp
@pytest.mark.parametrize('info_dict', TEMP)
def test_temp(browser, info_dict):
    page = DemoInputFormPage(browser)

    # Load webpage
    page.load()

    # Assert that chosen name is either correct or displays associated error
    errors = page.check_errors(info_dict["text"], info_dict["input_type"])
    for keys in errors:
        assert errors[keys] == info_dict[keys]
