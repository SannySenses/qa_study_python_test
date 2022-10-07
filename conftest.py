import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options

# область конфигурации вызываемого окна браузера
@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # use headless if you do not need browser ui
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1600,900')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    # F:/QA/Soft
    options = get_chrome_options
    # driver = webdriver.chrome(options=options)
    # if webdriver save not in path project, print new path in 'executable_path='
    # driver = webdriver.chrome(executable_path='F:/QA/Soft/chromedriver_win32/chromedriver.exe',options=options)
    driver = webdriver.Chrome(options=options)
    return driver

# scope - способ использования на вызов fixture
# scope='function' - будет использоваться при каждом тесте паралельно
# scope='session' - будет использоваться в пределах работы сессии браузера
@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.macys.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    driver.delete_all_cookies()
    yield driver
    driver.close()  # if need close all tabs browser, use method  quite
