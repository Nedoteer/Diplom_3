import pytest
from selenium import webdriver

from urls import Urls


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        browser = webdriver.Firefox(options=options)
    elif request.param == 'chrome':
        browser = webdriver.Chrome()

    browser.get(Urls.STELLAR)

    yield browser

    browser.quit()


