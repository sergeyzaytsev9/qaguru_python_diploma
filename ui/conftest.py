import pytest
import os
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = float(os.getenv('selene.timeout', '3'))
    yield browser
    browser.quit()
