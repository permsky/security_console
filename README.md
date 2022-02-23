# Пульт охраны банка.
Код позволяет просматривать в браузере:
- данные об активных картах доступа в хранилище;
- список пользователей, находящихся в хранилище;
- список посещений хранилища для конкретного пользователя.

## Запуск

- Скачайте код
- Настройте окружение. Для этого выполните следующие действия:
  - установите Python3.x;
  - создайте виртуальное окружение [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта и активируйте его.
  - установите необходимые зависимости:

    ```
    pip install -r requirements.txt
    ```
- Создайте файл .env в корне проекта. Сохраните настройки django и базы данных в следующих переменных окружения:
  ```
  DJANGO_SECRET_KEY=django_secret_key
  DB_HOST=database_hostname
  DB_PORT=database_port
  DB_NAME=database_name
  DB_USER=database_user
  DB_PASSWORD=database_password
  DJANGO_DEBUG=True or False
  ```
- Введите команду:

```
python manage.py runserver 0.0.0.0:8000
```
- Результат работы кода в браузере по адресу:
```
localhost:8000
```
## Цели проекта
Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
