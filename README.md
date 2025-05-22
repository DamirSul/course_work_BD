# Корпоративный Сервис Найма

## Цели и задачи проекта:
Разработка Telegram-бота для автоматизации работы сотрудников Сервиса найма.

## Используемый стек и технологии:
* [Pyhton](https://www.python.org/)  ![Python](https://img.shields.io/badge/Python-3.11-blue)
* [PostgreSQL](https://www.postgresql.org/)
* [Docker](https://www.docker.com/)
* [Nginx](https://nginx.org/ru/)
* [python-telegram-bot](https://python-telegram-bot.org/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Pydantic](https://docs.pydantic.dev/latest/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [spaCy](https://spacy.io/)
* [Uvicorn](https://www.uvicorn.org/)
* [Celery](https://docs.celeryq.dev/en/stable/)
* [Redis](https://github.com/redis/redis-py)

## Структура и назначение папок и файлов проекта:
  ```
├── README.md                        Файл с описанием проекта
├── requirements_style.txt           Зависимости для стилизации кода
├── ruff.toml                        Файл правил для стилизации кода
├── .github                          Папка с конфигурационными файлами CI/CD
├── infra                            Папка с конфигурационными файлами инфраструктуры
│   └── nginx
└── src
    ├── alembic                      Папка с миграциями данных для базы данных
    ├── backend
    │   ├── api
    │   │   ├── endpoints            Папка с эндпоинтами
    │   ├── core                     Папка с основными функциями
    │   ├── crud                     Папка с CRUD
    │   ├── logs                     Папка с логами
    │   ├── models                   Папка с моделями
    │   ├── schemas                  Папка со схемами
    │   ├── service                  Папка с сервисными функциями
    │   ├── templates                Папка с шаблонами страниц
    │   └── utils                    Папка с утилитами для работы проекта
    ├── bot_v2                       Папка с основными функциями для работы телеграм-бота
    │   ├── celery_beat
    │   ├── handlers
    │   ├── keyboards
    │   ├── services
    │   └── validators
    ├── media                        Папка для хранения картинов
        └── images 

  ```

## Порядок развертывания, настройки и запуска проекта локально:

1. Склонировать репозиторий и перейти в директорию проекта.
```bash
git clone https://github.com/DamirSul/course_work_BD.git
cd recruit_service_team_2
```

1. Создать в src и заполнить файл .env по примеру:
```
APP_TITLE=Сервис найма
APP_SECRET=SECRET
APP_DB_HOST=localhost
APP_DB_PORT=5432
APP_DB_NAME=recruitment_service
APP_DB_USER=postgres
APP_DB_PASSWORD=postgres
APP_DATABASE_URL=postgresql+asyncpg:///recruitment_service.db
TOKEN=

```

3. Развернуть и активировать виртуальное окружение.

```bash
python -m venv venv
source venv/Scripts/activate
```

4. Перейти в директорию src и установить пакеты из файла requirements.txt.

```bash
cd src
pip install -r requirements.txt
```

5. Применение миграций

```bash
alembic upgrade head
```

6. Создание суперадмина.
Из директории src:
```bash
python cli.py --username username --tg-id your_tg_id --tg-username tg_username --birth-date your_birth_date --email yourmail@mail.com --phone +79999998844 --password password -d
```
6. Запуск проекта.
```bash
Uvicorn: из директории src: uvicorn main:app --reload
telegram-bot: из директории src/bot_v2: python main.py
```

## Команда проекта:
- [Дамир Сулейменов](https://github.com/DamirSul)
