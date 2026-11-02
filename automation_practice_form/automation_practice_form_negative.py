import pytest
from selenium import webdriver
import automation_practice_form_po

URL = "https://qa-guru.github.io/one-page-form/automation-practice-form.html"


# Фикстура: открывает браузер и отдает готовый Page Object
@pytest.fixture(autouse=True)
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    page = automation_practice_form_po.AutomationPracticeFormPO(driver, URL)
    yield page
    driver.quit()


# ==========================================
# НЕГАТИВНЫЕ ТЕСТЫ для этого добавил новый метод в Page Object: automation_practice_form_po.py
# ==========================================

def test_submit_empty_form(setup):
    """Негативный тест: нажимаем Submit, не заполняя обязательные поля"""
    page = setup

    # 1. Закрываем баннер, чтобы он не мешал нажать Submit
    page._close_commercial_banner()

    # 2. Просто нажимаем Submit, ничего не заполняя!
    page._click_submit_button()

    # 3. Проверяем, что модальное окно с успехом НЕ появилось
    assert not page.is_result_form_displayed(), "БАГ: Форма отправилась пустой!"
    print("✅ Тест пройден: пустая форма не отправилась.")


def test_submit_without_last_name(setup):
    """Негативный тест: заполняем все, КРОМЕ обязательного поля Фамилия"""
    page = setup

    # Заполняем только имя, email и телефон (остальное пропускаем)
    page._close_commercial_banner()
    page._fill_first_name("Ivan")
    page._fill_email("ivan@example.com")
    page._fill_user_number("1234567890")

    # Нажимаем Submit
    page._click_submit_button()

    # Проверяем, что форма не отправилась (окно не появилось)
    assert not page.is_result_form_displayed(), "БАГ: Форма отправилась без фамилии!"
    print("✅ Тест пройден: форма без фамилии не отправилась.")

# Запустить pytest automation_practice_form/automation_practice_form_negative.py -v
