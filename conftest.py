import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose language: ru/es/ko/fr etc.")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()        
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})        
        options.add_argument("--log-level=3") # Hide console logs
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")
    yield browser
    browser.quit()
