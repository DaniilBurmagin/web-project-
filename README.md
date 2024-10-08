## Описание

Простой веб-сервис, который отвечает на POST запрос `/HelloWorld` и возвращает JSON.


## Сборка и запуск приложения локально

1. Клонируйте репозиторий: 
bash
   git clone https://github.com/DaniilBurmagin/web-project-
   cd web_project
2.  Создайте виртуальное окружение и установите зависимости:
bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
3. Запустите приложение:
bash
   python manage.py runserver
   


## CI/CD и деплой

Процесс CI/CD настроен с помощью GitHub Actions.
После каждого коммита в основную ветку выполняется автоматическая сборка Docker-образа
и его тегирование.
Деплой осуществляется на локальную сеть (127.0.0.1:8000) в фоновом режиме
с использованием Docker Compose.