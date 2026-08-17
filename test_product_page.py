from pages.product_page import ProductPage
from pages.main_page import MainPage

def test_add_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_check_url()
    page.add_to_basket_click()
    page.click_to_button()