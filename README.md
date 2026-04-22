# GreenCity Events Page Tests

## Опис проєкту
Автоматизоване тестування сторінки новин GreenCity з використанням Python, Selenium WebDriver та unittest.

## Посилання на тестову сторінку
[https://www.greencity.cx.ua/#/greenCity/events](https://www.greencity.cx.ua/#/greenCity/events)

## Як запустити тести
1. Встановіть залежності:
```bash
pip install -r requirements.txt
python -m unittest discover tests

## Посилання на сторінку
https://www.greencity.cx.ua/#/greenCity/events

# GreenCity UI Tests (Selenium + Python)

## Опис

Автоматизовані UI тести для сайту GreenCity, написані з використанням Selenium та Page Object Model.

## Покриті тест-кейси

### Test Case 1: Open News Page

* Перевірка відкриття сторінки новин
* Перевірка наявності списку новин

### Test Case 2: Open News Details

* Відкриття першої новини
* Перевірка заголовка
* Перевірка контенту

### Test Case 3: Back Navigation

* Перехід назад через браузер
* Перевірка списку новин

---

Технології

* Python
* Selenium WebDriver
* unittest
* Page Object Model

---

Структура проєкту

```
pages/       → Page Objects
tests/       → Тести
```

---


## Автор
Nataliia Martynyshyn
