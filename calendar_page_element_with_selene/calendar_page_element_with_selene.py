import time
from selene import browser, by, be, have

# Настройка Selene
browser.config.timeout = 5
browser.config.browser_name = 'chrome'


class Calendar:
    def __init__(self, base_element):
        self.input_field = base_element

    def select_date(self, day: str, month: str, year: str):
        # 1. Закрываем баннер (в Selene это делается одной строкой)
        try:
            browser.element("#fixedban button").click()
        except Exception:
            pass

        # 2. Открываем календарь
        self.input_field.click()

        # 3. Выбираем месяц и год
        browser.element(".react-datepicker__month-select").click().element(by.text(month)).click()
        browser.element(".react-datepicker__year-select").click().element(by.text(year)).click()

        # 4. Форматируем день (добавляем "0" для однозначных чисел, чтобы 15 стало 015)
        day_padded = f"0{day}"

        # 5. Выбираем сам день
        browser.element(f".react-datepicker__day--{day_padded}:not(.react-datepicker__day--outside-month)").click()


class AutomationPracticeFormPage:
    def __init__(self):
        browser.open("https://qa-guru.github.io/one-page-form/automation-practice-form.html")
        self.birthday_calendar = Calendar(browser.element("#dateOfBirthInput"))


class TestSuite:
    def test_select_birthday_date(self):
        page = AutomationPracticeFormPage()
        page.birthday_calendar.select_date(day="15", month="July", year="2000")

        # ИСПРАВЛЕНИЕ: Используем have.value вместо be.value
        page.birthday_calendar.input_field.should(have.value("15 Jul 2000"))
        print("✅ Тест на Selene успешно пройден!")


if __name__ == "__main__":
    ts = TestSuite()
    ts.test_select_birthday_date()

    time.sleep(3)
    browser.quit()

# Запустить python calendar_page_element_with_selene/calendar_page_element_with_selene.py
