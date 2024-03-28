import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser: WebDriver):
    browser.get(link)
    time.sleep(5)
    assert is_element_present(browser), \
        "Add to basket button does not exists"

def is_element_present(browser):
    try:
        browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    except NoSuchElementException:
        return False
    return True
