# 🚀 Selenium & Pytest: Advanced Automation (Lesson 5)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Selenium-4.22.0-43B02A?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium">
  <img src="https://img.shields.io/badge/Pytest-8.4-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest">
  <img src="https://img.shields.io/badge/Selene-2.0-white?style=for-the-badge&logo=selene&logoColor=black" alt="Selene">
  <img src="https://img.shields.io/badge/PageFactory-2.8-orange?style=for-the-badge" alt="PageFactory">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-completed-success?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/architecture-POM%20%7C%20PageElement%20%7C%20PageFactory-blueviolet?style=flat-square" alt="Architecture">
</p>

---

## 📖 О проекте

Домашнее задание по углубленному изучению паттернов автоматизации. В рамках работы были изучены и переписаны несколько проектов: от «решения в лоб» до профессиональных архитектур с использованием **Page Object Model (POM)**, **Page Factory**, **Page Elements** и фреймворка **Selene**.

**Протестированные формы (AUT):**
- 🔐 [Login Form](https://qa-guru.github.io/one-page-form/login.html)
- 📝 [Text Box Form](https://qa-guru.github.io/one-page-form/text-box.html)
- 🎓 [Student Registration Form](https://qa-guru.github.io/one-page-form/automation-practice-form.html)
- 📊 [Tables](https://the-internet.herokuapp.com/tables)

---

## 🛠️ Что было сделано (по папкам)

### 1. 📦 `automation_practice_form` (Основы POM)
- Изучен и запущен `initial.py` (монолитный скрипт).
- Проведен рефакторинг в полноценный **Page Object Model** (`po.py` + `test_suite.py`).
- Переведено на современные фикстуры Pytest.
- **Написаны собственные негативные тесты**: проверка отправки пустой формы и формы без обязательных полей.

### 2. 📦 `TextBoxPageObject` (Классический Page Object)
- Реализован паттерн **Fluent Interface** (цепочки вызовов: `page.open().fill_form().submit()`).
- **Исправлены баги (TODO):**
  - Добавлена защита от `NoneType` при проверке валидации Email.
  - Избавление от `if/elif` в тестах с помощью `**kwargs`.
  - Обнаружен баг слабой HTML5 валидации (пропуск `john@missing-dot`) и помечен как `xfail`.
  - Исправлена проверка XSS-инъекций (сайт удаляет теги, проверяем на их отсутствие).

### 3. 📦 `TextBoxPageObjectWithPageFactory` (Page Factory)
- Реализован **Page Factory** (словарь локаторов вместо констант).
- Проведено сравнение с классическим POM: код стал короче, но появились неявные ожидания, которые пришлось обрабатывать через `try/except`.
- Использованы расширенные методы: `set_text()`, `click_button()`.

### 4. 📦 `the_simplest_page_factory` (Задание со звездочкой)
- Разобрана абстрактная реализация PageFactory на странице логина.
- Изучены методы `select_element_by_text()` и `hover()`.

### 5. 📦 `calendar_page_element_with_selene` (Selene Framework)
- Исправлена проблема совместимости (откат Selenium до `4.22.0`).
- Реализовано закрытие всплывающего баннера в Selene (в одну строчку).
- Написан аналог на «голом» Selenium для демонстрации разницы в объеме кода.
- Исправлен баг с форматированием дня (добавление ведущего нуля для классов календаря).

### 6. 📦 `table_page_element_example` (Page Element)
- Реализован паттерн **Page Element** для работы с таблицами (класс `TableElement`).
- **Решены TODO:** добавлена вторая таблица, написан тест на сравнение данных (заголовков и email) между двумя таблицами.

### 7. 📦 `example_from_student` (Анализ чужого кода)
- Изучен проект с правильной архитектурой: `BasePage`, вынос `Calendar` в `elements`, использование `conftest.py` и генераторов данных (`randint`).
- Разобрана работа с системными сообщениями валидации браузера (`validationMessage`).

---

## 📂 Структура проекта

<details>
<summary><b>Нажмите, чтобы развернуть дерево проекта</b> 🔽</summary>

```text
selenium_4/
├── automation_practice_form/      # POM, фикстуры, негативные тесты
├── TextBoxPageObject/             # Классический POM, Fluent Interface
├── TextBoxPageObjectWithPageFactory/ # PageFactory
├── the_simplest_page_factory/     # Пример PageFactory
├── calendar_page_element_with_selene/ # Selene + Selenium
├── table_page_element_example/    # Работа с таблицами
├── example_from_student/          # Чужой POM проект (BasePage, Pages, Tests)
├── requirements.txt               # Зависимости (selenium==4.22.0)
└── README.md                      # Этот файл
