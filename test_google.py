from time import sleep


def test_open_google(browser):
    # Открываем сайт
    browser.get("https://www.google.com")

    # Проверяем, что в заголовке страницы есть слово Google
    assert "Google" in browser.title

sleep(5)