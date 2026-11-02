import os
import pytest
from selenium import webdriver
import automation_practice_form_po

URL = "https://qa-guru.github.io/one-page-form/automation-practice-form.html"


# Фикстура с autouse=True
# Она автоматически запустится ПЕРЕД каждым тестом и выполнится ПОСЛЕ него
@pytest.fixture(autouse=True)
def setup():
    # 1. Подготовка (Arrange)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)

    # Создаем Page Object и передаем ему готовый driver
    page = automation_practice_form_po.AutomationPracticeFormPO(driver, URL)

    # Создаем временный файл
    file_path = os.path.abspath('test_file.jpg')
    with open(file_path, 'w') as file:
        file.write("Test")

    # Отдаем данные тесту
    yield page, file_path

    # 2. Уборка (Teardown) - выполнится, даже если тест упал
    if os.path.exists(file_path):
        os.remove(file_path)
    driver.quit()


# ==========================================
# ТЕСТЫ стали чище
# ==========================================

def test_form_positive01(setup):
    # Получаем page и путь к файлу из фикстуры
    page, file_path = setup

    page.fill_in_form(
        file_path, "Dmitry", "Bugaev", "bugaev@example.com", "Male", "1234567890",
        ("1988", "4", "22"), ("Maths", "English"), ("Sports", "Music"),
        "г. Санкт-Петербург, ул. Невский проспект, д 101", "NCR", "Noida"
    )
    page.assert_form(
        file_path, "Dmitry", "Bugaev", "bugaev@example.com", "Male", "1234567890",
        ("1988", "4", "22"), ("Maths", "English"), ("Sports", "Music"),
        "г. Санкт-Петербург, ул. Невский проспект, д 101", "NCR", "Noida"
    )


def test_form_positive02(setup):
    page, file_path = setup

    page.fill_in_form(
        file_path, "Ivan", "Ivanov", "ivan@example.com", "Female", "9876543210",
        ("1995", "1", "15"), ("Physics",), ("Reading",),
        "г. Москва, ул. Арбат, д 1", "Uttar Pradesh", "Agra"
    )
    page.assert_form(
        file_path, "Ivan", "Ivanov", "ivan@example.com", "Female", "9876543210",
        ("1995", "1", "15"), ("Physics",), ("Reading",),
        "г. Москва, ул. Арбат, д 1", "Uttar Pradesh", "Agra"
    )

# Запустить pytest automation_practice_form/automation_practice_form_test_suite.py -v
