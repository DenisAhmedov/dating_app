﻿# DATING_APP

### Бэкенд для сайта (приложения) знакомств

---

#### Установка

1) Клонируем репозиторий `https://github.com/DenisAhmedov/dating_app.git`
2) Устанавливаем зависимости `pip install -r requirements.txt`
3) Запускаем миграции `python manage.py makemigrations && python manage.py migrate`
4) Создаем суперпользователя `python manage.py createsuperuser`
5) Собираем весь статичный контент в каталоге /static/ `python manage.py collectstatic`
6) Запустите отладочный сервер `python manage.py runserver 0.0.0.0:8000`

---
#### Стек

1) Django
2) Django Rest Framework
3) MySQLite DB

#### Дополнительная информация

Отправка писем участникам реализована через `filebased.EmailBackend`. Отправленные письма хранятся в папке **/sent_emails/**.
