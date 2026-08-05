from .base_page import BasePage
from selenium.webdriver.common.by import By
from login_page import LoginPage

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link").click()
        return LoginPage(browser = self.browser, url = self.browser.current_url)
        #Разобрать что это дает!
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, '#login_link'), 'login link is not present'

    # Забыл про селекторы как они выглядтят, оказывается решетка помогла