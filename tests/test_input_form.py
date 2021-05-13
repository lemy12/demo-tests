import pytest

from pages.input_form import DemoInputFormPage

# Parametrize globals
NAME = [('Smith', "none", "none"),           # (name, valid, no_char)
        ('', "none", "block"),               # block = shown
        ('A', "block", "none"),              # none = hidden
        ('123', "none", "none")]
EMAIL = [('abc@gmail.com', "none", "none"),
        ('', "none", "block"),
        ('@outlook.com', "block", "none"),
        ('abc@hotmail.', "block", "none")]


@pytest.mark.input_form
@pytest.mark.input_form_fname
@pytest.mark.parametrize('name,valid,no_char', NAME)
def test_first_name(browser, name, valid, no_char):
    page = DemoInputFormPage(browser)

    # Load webpage
    page.load()

    # Assert that chosen name is either correct or displays associated error
    err_valid, err_no_char = page.check_fname(name)
    assert err_valid == valid and err_no_char == no_char


@pytest.mark.input_form
@pytest.mark.input_form_lname
@pytest.mark.parametrize('name,valid,no_char', NAME)
def test_last_name(browser, name, valid, no_char):
    page = DemoInputFormPage(browser)

    # Load webpage
    page.load()

    # Assert that chosen name is either correct or displays associated error
    err_valid, err_no_char = page.check_lname(name)
    assert err_valid == valid and err_no_char == no_char


@pytest.mark.input_form
@pytest.mark.input_form_email
@pytest.mark.parametrize('email,valid,no_char', EMAIL)
def test_email(browser, email, valid, no_char):
    page = DemoInputFormPage(browser)

    # Load webpage
    page.load()

    # Assert that chosen name is either correct or displays associated error
    err_no_char, err_valid = page.check_email(email)
    assert err_valid == valid and err_no_char == no_char
