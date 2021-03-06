# Проект «API для Yatube»

## Описание.
API для социальной сети [Yatube](https://github.com/kirrik/yatube_sn).

## Установка.
Для установки на локальной машине:
- клонируйте репозиторий
- установите виртуальное окружение, активируйте его
- установите зависимости
```python
pip install -r requirements.txt
```
- выполните миграции
```python
python manage.py migrate
```
- запустите сервер
```python
python manage.py runserver
```
- документация доступна по адресу http://127.0.0.1:8000/redoc/

## Примеры.
Примеры возможных запросов к API вы можете найти в документации.
Выполнить запросы можно с помощью, например, программы [Postman](https://www.postman.com/downloads/).