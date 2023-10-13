import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_width = 1660
    browser.config.window_height = 1020
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()
