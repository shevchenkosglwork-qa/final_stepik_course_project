from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

link = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_open_shop(browser):
    #Переходим по ссылке
    browser.get(link)
    #Находим элемент и ждем, когда появится кнопка добавить в корзину
    put_in_the_basket = (WebDriverWait(browser, 10)
                         .until(EC.presence_of_element_located(
        (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket"))))

    #Кликаем по кнопке
    put_in_the_basket.click()

    #Находим текст, что товар добавлен
    result = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "alertinner")))

    assert result.is_displayed(), 'Товар не добавился'
    print("\n --- Товар успешно добавился и отображается на экране! --- \n")