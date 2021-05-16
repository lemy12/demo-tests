import pytest

from pages.input_form import DemoInputFormPage

# Parametrize globals
TEXTBOX = [{"input_type": "first_name", "text": "Smith", "stringLength": "none", "notEmpty": "none"},
           {"input_type": "first_name", "text": "", "stringLength": "none", "notEmpty": "block"}]
FNAME = [{"text": "John", "stringLength": "none", "notEmpty": "none"},
         {"text": "", "stringLength": "none", "notEmpty": "block"},
         {"text": "A", "stringLength": "block", "notEmpty": "none"}]
LNAME = [{"text": "Smith", "stringLength": "none", "notEmpty": "none"},
         {"text": "", "stringLength": "none", "notEmpty": "block"},
         {"text": "A", "stringLength": "block", "notEmpty": "none"}]
EMAIL = [{"text": "abc@gmail.com", "emailAddress": "none", "notEmpty": "none"},
         {"text": "", "emailAddress": "none", "notEmpty": "block"},
         {"text": "abc@gmail.", "emailAddress": "block", "notEmpty": "none"}]


def textbox(browser, textbox_dict, input_type):
    page = DemoInputFormPage(browser)

    # Load webpage
    page.load()

    # Assert that chosen name is either correct or displays associated error
    errors = page.check_errors(textbox_dict["text"], input_type)
    for keys in errors:
        assert errors[keys] == textbox_dict[keys]


@pytest.mark.input_form_fname
@pytest.mark.parametrize('fname_dict', FNAME)
def test_first_name(browser, fname_dict):
    textbox(browser, fname_dict, "first_name")


@pytest.mark.input_form_lname
@pytest.mark.parametrize('lname_dict', LNAME)
def test_last_name(browser, lname_dict):
    textbox(browser, lname_dict, "last_name")


@pytest.mark.input_form_email
@pytest.mark.parametrize('email_dict', EMAIL)
def test_email(browser, email_dict):
    textbox(browser, email_dict, "email")


