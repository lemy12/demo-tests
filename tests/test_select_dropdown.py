import pytest

from pages.select_dropdown import DemoSelectDropdownPage

# Parametrize globals
DAY = ['Sunday', 'Saturday']
CITY = [(['California']),
        (['Pennsylvania', 'Washington']),
        (['Florida', 'Ohio', 'Texas'])]


@pytest.mark.select_list
@pytest.mark.parametrize('day', DAY)
def test_select_list(browser, day):
    page = DemoSelectDropdownPage(browser)

    # Load webpage
    page.load()

    # Assert that chosen day is in result message
    assert day in page.check_select_list(day)


@pytest.mark.multi_select_list
@pytest.mark.multi_select_list_first
@pytest.mark.parametrize('city', CITY)
def test_multi_select_list_first(browser, city):
    page = DemoSelectDropdownPage(browser)

    # Load webpage
    page.load()

    # Assert that first chosen city is in result
    result = page.check_multi_select_list(city, "first")
    assert "First selected option is :" in result
    assert city[0] in result


@pytest.mark.multi_select_list
@pytest.mark.multi_select_list_all
@pytest.mark.parametrize('city', CITY)
def test_multi_select_list_all(browser, city):
    page = DemoSelectDropdownPage(browser)

    # Load webpage
    page.load()

    # Assert that chosen cities are in result
    result = page.check_multi_select_list(city, "all")
    assert "Options selected are :" in result
    for each in city:
        assert each in result
