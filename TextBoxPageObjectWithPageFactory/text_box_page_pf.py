from seleniumpagefactory.Pagefactory import PageFactory

# pip install selenium-page-factory

class TextBoxPage(PageFactory):
    URL = "https://qa-guru.github.io/one-page-form/text-box.html" # Частный случай
    
    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "full_name_input": ('ID', "userName"),
            "email_input": ('ID', "userEmail"),
            "current_address_input": ('ID', "currentAddress"),
            "permanent_address_input": ('ID', "permanentAddress"),
            "submit_button": ('ID', "submit"),
            "output_box": ('ID', "output"),
            "output_name": ('ID', "name"),
            "output_email": ('ID', "email"),
            "output_current_address": ('CSS', "#output #currentAddress"),
            "output_permnent_address": ('CSS', "#output #permanentAddress")
        }

    def open(self):
        self.driver.get(self.URL)
        return self  # Возвращаем self для Fluent Interface

    def fill_form(self, name=None, email=None, cur_addr=None, perm_addr=None):
        if name is not None:
            # ИСПОЛЬЗУЕМ PageFactory: set_text() сначала очищает поле, потом вводит текст
            self.full_name_input.set_text(name)
        if email is not None:
            self.email_input.set_text(email)
        if cur_addr is not None:
            self.current_address_input.set_text(cur_addr)
        if perm_addr is not None:
            self.permanent_address_input.set_text(perm_addr)
        return self

    def submit(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.submit_button)
        # ИСПОЛЬЗУЕМ PageFactory: click_button() ждет, пока кнопка станет кликабельной
        self.submit_button.click_button()
        return self

    def is_email_error_present(self):
        field_class = self.email_input.get_attribute("class")
        if field_class is None:
            return False
        return "field-error" in field_class or "error" in field_class

    def get_output_data(self):
        # Возвращает текст из блока вывода, если он появился
        try:
            # PageFactory выбросит исключение, если элемента нет на странице
            if not self.output_box.is_displayed():
                return None
        except Exception:
            # Если элемента нет, ловим ошибку и возвращаем None
            return None

        # Парсинг строк (удаляем префиксы вроде 'Name:')
        name = self.output_name.text.replace("Name:", "").strip()
        email = self.output_email.text.replace("Email:", "").strip()
        cur_addr = self.output_current_address.text.replace("Current Address :", "").strip()
        perm_addr = self.output_permnent_address.text.replace("Permananet Address :", "").strip()

        return {"name": name, "email": email, "cur_addr": cur_addr, "perm_addr": perm_addr}

# Ответ:Количество падений разное, потому что selenium-page-factory использует механизм неявного ожидания(WebDriverWait)
# для каждого элемента из словаря locators. Если элемента нет, она ждет таймаут и выбрасывает ElementNotVisibleException,
# в то время как обычный find_element выбрасывает NoSuchElementException мгновенно. Чтобы PageFactory вел себя так же,
# нужно оборачивать вызовы в try/except


