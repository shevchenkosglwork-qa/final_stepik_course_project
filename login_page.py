from pages.base_page import BasePage
from locators import LoginPageLocators
from pages.main_page import MainPage

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
    # понять что не так с этим методом и переписать след. два
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'Login url is not correct'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Form not found'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER), 'Login register not found'

