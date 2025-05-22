# Сервис Найма для сотрудников Яндекс Практикума

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
1. Заполнить файл .env по примеру:
```
TOKEN=TG_BOT_TOKEN
APP_TITLE='Сервис найма'
APP_SECRET=secret
APP_DB_HOST=localhost
APP_DB_PORT=5432
APP_DB_NAME=recruitment_service
APP_DB_USER=admin
APP_DB_PASSWORD=password
APP_DATABASE_URL=sqlite+aiosqlite:///../src/recruitment_service.db
APP_POSTGRES_URL=postgresql+asyncpg://{}:{}@{}:{}/{}
APP_ENABLE_DOCS=true
APP_DEBUG=true
BOT_NAME=you_bot_name
REDIS_URL=redis://<redis_container>:6379/0
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=db_example
FLOWER_URL=http://localhost:5555
```
2. Склонировать репозиторий и перейти в директорию проекта.
```bash
git@github.com:Studio-Yandex-Practicum/recruit_service_team_2.git
cd recruit_service_team_2
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

5. Перейти в директорию infra и развернуть контейнеры.

```bash
cd ..
cd infra
docker compose -f docker-compose.prod.yml up -d(при запуске на сервере) 
docker compose -f docker-compose.dev.yml up -d(при разработке)
```

6. Применение миграций в контейнере recruit-service-back.

```bash
docker exec -it recruit-service-backend bash
alembic upgrade head
```

7. Создание суперадмина.
В этом же контейнере выполнить команду со своими данными
```bash
python cli.py --username username --tg-id your_tg_id --tg-username tg_username --birth-date your_birth_date --email yourmail@mail.com --phone +79999998844 --password password -d
```

## Команда проекта:
- [тимлид Роман Баньков](https://github.com/BulkaInside)
- [Артем Козлов](https://github.com/arteick)
- [Ольга Богданова](https://github.com/pitbul892)
- [Герман Деев](https://github.com/germynic31)
- [Дамир Сулейменов](https://github.com/DamirSul)
- [Артур Ачкасов](https://github.com/ArturAchkasov/)
- [Андрей Черепанов](https://github.com/skullikk) 
