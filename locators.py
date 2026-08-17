from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_LINK = (By.ID, 'login_link')

    LOGIN_FORM = (By.ID, 'login_form')

    LOGIN_REGISTER = (By.ID, 'register_form')

class AddToBasketLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')