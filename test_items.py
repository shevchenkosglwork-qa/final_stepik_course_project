from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from conftest import browser

link = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_open_shop(browser):
    browser.get(link)
    put_in_the_basket = (WebDriverWait(browser, 10)
                         .until(EC.presence_of_element_located(
        (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket"))))
    put_in_the_basket.click()
    result = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            browser.find_element(By.CLASS_NAME, "alertinner")))
    #result = browser.find_element(By.ID, "write_review")

    assert result.is_displayed(), 'Товар не добавился'
    print("\n Товар успешно добавился и отображается на экране!")