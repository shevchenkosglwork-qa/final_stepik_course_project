import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# 1. Регистрируем параметр --language в консоли
def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Выберите язык интерфейса браузера (например, ru, en, fr)"
    )


# 2. Передаем встроенную фикстуру request, чтобы прочитать данные из консоли
@pytest.fixture
def browser(request):
    # 3. Достаем значение --language, которое ввёл пользователь в консоли
    user_language = request.config.getoption("language")

    print(f"\n--- Старт браузера для теста (Язык: {user_language}) ---")

    options = Options()
    # Обязательные флаги для CI/CD и Linux-контейнеров:
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # 4. Настраиваем язык для Chrome
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # 5. Инициализируем драйвер с нашими настройками
    driver = webdriver.Chrome(options=options)

    yield driver

    print("\n--- Закрытие браузера для теста ---")
    driver.quit()