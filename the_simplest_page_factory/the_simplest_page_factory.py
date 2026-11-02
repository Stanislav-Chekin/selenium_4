import time
from selenium import webdriver
from seleniumpagefactory.Pagefactory import PageFactory


# TODO: Это лишь абстрактный пример, переписать хотя бы один тест с хотя бы одним PageObject на PageFactory
# РЕШЕНИЕ: Переписали на реальную страницу логина QA-Guru
class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5  # PageFactory использует неявное ожидание (по умолчанию 5 сек)

        self.locators = {
            "login_input": ('ID', 'login-input'),
            "password_input": ('ID', 'password-input'),
            "submit_button": ('ID', 'submit-button')
        }

    def login(self, user, password):
        # TODO: Постараться использовать в своем проекте расширенные возможности PageFactory
        # РЕШЕНИЕ: Используем set_text (очищает поле и вводит текст) и click_button (ждет кликабельности)
        self.login_input.set_text(user)
        self.password_input.set_text(password)
        self.submit_button.click_button()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qa-guru.github.io/one-page-form/login.html")

    login_page = LoginPage(driver)

    # Вызываем логику (неверные данные, чтобы увидеть ошибку на экране)
    login_page.login("user1", "wrong_password")

    time.sleep(5)  # Пауза, чтобы увидеть результат
    driver.quit()

# Запустить python the_simplest_page_factory/the_simplest_page_factory.py

