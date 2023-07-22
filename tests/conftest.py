from selene import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_width = 1440
    browser.config.window_height = 2160

    yield

    browser.quit()