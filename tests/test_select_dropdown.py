import pytest

from pages.select_dropdown import DemoSelectDropdownPage

# Parametrize globals
DAY = ['Sunday', 'Saturday']
CITY = [(['California'], 'first'),
        (['Pennsylvania', 'Washington'], 'first'),
        (['Florida', 'Ohio', 'Texas'], 'all')]


@pytest.mark.select_list
@pytest.mark.parametrize('day', DAY)
def test_select_list(browser, day):
    page = DemoSelectDropdownPage(browser)

    # Load webpage
    page.load()

    # Assert that chosen day is in result message
    assert day in page.check_select_list(day)


@pytest.mark.multi_select_list
@pytest.mark.parametrize('city,choice', CITY)
def test_multi_select_list(browser, city, choice):
    page = DemoSelectDropdownPage(browser)

    # Load webpage
    page.load()

    # Assert that chosen day is in result message
    result = page.check_multi_select_list(city, choice)

    if choice == "first":
        assert "First selected option is :" in result
        assert city[0] in result
    elif choice == "all":
        assert "Options selected are :" in result
        for each in city:
            assert each in result
