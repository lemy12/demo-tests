import pytest

from pages.radio_buttons import DemoRadioButtonsPage

SEX = ['male', 'female', '']
GROUPS = [('male', '0 to 5'), ('female', '5 to 15'), ('male', '15 to 50')]


@pytest.mark.radio_button
@pytest.mark.parametrize('sex', SEX)
def test_radio_button(browser, sex):
    page = DemoRadioButtonsPage(browser)

    # Load webpage
    page.load()

    # Assert that chosen radio gives assumed result
    if sex:
        assert sex in page.check_radio_button(sex).lower()
    else:
        assert page.check_radio_button(sex) == "Radio button is Not checked"


@pytest.mark.group_radio_buttons
@pytest.mark.parametrize('sex,age', GROUPS)
def test_group_radio_buttons(browser, sex, age):
    page = DemoRadioButtonsPage(browser)

    # Load webpage
    page.load()

    # Assert that chosen radios give assumed result
    text = page.check_group_radio_buttons(sex, age).lower().replace('-', 'to')
    assert sex in text and age in text

