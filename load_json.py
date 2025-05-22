import json
from datetime import datetime
from pathlib import Path

from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)
from sqlalchemy.orm import sessionmaker

DB_PATH = Path("src/recruitment_service.db")
JSON_PATH = Path("data.json")
DATABASE_URL = f"sqlite:///{DB_PATH}"


engine = create_engine(DATABASE_URL)
metadata = MetaData()


def define_tables() -> None:
    """Определение структуры таблиц с автоинкрементом."""
    Table('companies', metadata,
          Column('id',
                 Integer,
                 primary_key=True,
                 autoincrement=True),
          Column('name', String(255), nullable=False),
          Column('location', String(255)),
          Column('created_at', DateTime),
          Column('updated_at', DateTime),
          Column('manager_first_name', String(50)),
          Column('manager_last_name', String(50)),
          Column('manager_phone', String(20)),
          )

    Table('congratulations', metadata,
          Column('id', Integer, primary_key=True, autoincrement=True),
          Column('message', String(1000), nullable=False),  # Исправлено
          Column('is_active', Boolean),
          Column('format_type', String(20)),
          Column('created_at', DateTime),
          Column('updated_at', DateTime),
          )

    Table('images', metadata,
          Column('id', Integer, primary_key=True, autoincrement=True),
          Column('url', String(500), nullable=False),
          Column('description', String(500)),
          Column('created_at', DateTime),
          Column('updated_at', DateTime),
          )

    Table('stopwords', metadata,
          Column('id', Integer, primary_key=True, autoincrement=True),
          Column('word', String(50), unique=True, nullable=False),
          Column('language', String(10)),
          Column('category', String(10)),
          Column('created_at', DateTime),
          Column('updated_at', DateTime),
          )

    Table('users', metadata,
          Column('id', Integer, primary_key=True, autoincrement=True),
          Column('username', String(50), nullable=False),  # Исправлено
          Column('first_name', String(50), nullable=False),
          Column('last_name', String(50)),
          Column('tg_id', Integer, unique=True, nullable=False),
          Column('position', String(100), nullable=False),
          Column('department', String(100), nullable=False),
          Column('tg_username', String(50), unique=True, nullable=False),
          Column('birth_date', Date, nullable=False),
          Column('role', String(10), nullable=False),
          Column('email', String(100)),
          Column('phone', String(20)),
          Column('password_hash', String(255)),
          Column('created_at', DateTime),
          Column('updated_at', DateTime),
          Column('is_subscribed', Boolean, default=False, nullable=False),
          Column('is_active', Boolean, default=True, nullable=False),
          )

    Table('reminders', metadata,
          Column('id', Integer, primary_key=True, autoincrement=True),
          Column('reminder_date', String(50), nullable=False),
          Column('message', String(500), nullable=False),
          Column('user_id', Integer, ForeignKey('users.id')),
          Column('created_at', DateTime),
          Column('updated_at', DateTime),
          )

    Table('subscriptions', metadata,
          Column('id', Integer, primary_key=True, autoincrement=True),
          Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
          Column('is_active', Boolean),
          Column('days_before', Integer, nullable=False),
          Column('created_at', DateTime),
          Column('updated_at', DateTime),
          )

    Table('vacancies', metadata,
          Column('id', Integer, primary_key=True, autoincrement=True),
          Column('position', String(100), nullable=False),
          Column('description', String(1000), nullable=False),
          Column('company_id', Integer, ForeignKey('companies.id')),
          Column('created_at', DateTime),
          Column('updated_at', DateTime),
          )

    Table('registration_tokens', metadata,
          Column('id', Integer, autoincrement=True, primary_key=True),
          Column('token', String(100), nullable=False),
          Column('expires_at', DateTime, nullable=False),
          Column('used', Boolean, default=False),
          Column('created_by', Integer, ForeignKey('users.id')),
          Column('target_user_email', String(100)),
          Column('tg_id', BigInteger),
          Column('created_at', DateTime),
          Column('updated_at', DateTime),
          )


def validate_enum(value, allowed_values):  # noqa: ANN001, ANN201
    """Валидация ENUM-значений."""
    if value not in allowed_values:
        raise ValueError(f"Invalid value '{value}'. Allowed: {allowed_values}")
    return value


def load_data(session) -> None:  # noqa: ANN001
    """Основная функция загрузки данных."""
    if not JSON_PATH.exists():
        raise FileNotFoundError(f"JSON file {JSON_PATH} not found")

    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    current_time = datetime.now()

    try:
        print("Loading companies...")
        session.execute(
            metadata.tables['companies'].insert(),
            [{
                **item,
                'created_at': current_time,
                'updated_at': current_time,
            } for item in data['companies']],
        )

        print("Loading users...")
        session.execute(
            metadata.tables['users'].insert(),
            [{
                **item,
                'birth_date': datetime.strptime(item['birth_date'], '%Y-%m-%d').date(),  # noqa: E501
                'role': validate_enum(item['role'], ['user', 'admin']),
                'created_at': current_time,
                'updated_at': current_time,
            } for item in data['users']],
        )

        print("Loading congratulations...")
        session.execute(
            metadata.tables['congratulations'].insert(),
            [{
                **item,
                'format_type': validate_enum(item['format_type'], ['markdown', 'html']),  # noqa: E501
                'created_at': current_time,
                'updated_at': current_time,
            } for item in data['congratulations']],
        )

        print("Loading images...")
        session.execute(
            metadata.tables['images'].insert(),
            [{
                **item,
                'created_at': current_time,
                'updated_at': current_time,
            } for item in data['images']],
        )

        print("Loading stopwords...")
        session.execute(
            metadata.tables['stopwords'].insert(),
            [{
                **item,
                'language': validate_enum(item['language'], ['ru', 'en']),
                'category': validate_enum(item['category'], ['key', 'stop']),
                'created_at': current_time,
                'updated_at': current_time,
            } for item in data['stopwords']],
        )

        print("Loading vacancies...")
        session.execute(
            metadata.tables['vacancies'].insert(),
            [{
                **item,
                'created_at': current_time,
                'updated_at': current_time,
            } for item in data['vacancies']],
        )

        print("Loading registration_tokens...")
        session.execute(
            metadata.tables['registration_tokens'].insert(),
            [{
                **item,
                'expires_at': datetime.strptime(item['expires_at'], '%Y-%m-%d').date(),  # noqa: E501
                'created_at': current_time,
                'updated_at': current_time,
            } for item in data['registration_tokens']],
        )

        session.commit()
        print("\n✅ Все данные успешно загружены!")

    except Exception as e:
        session.rollback()
        print(f"\n❌ Ошибка: {str(e)}")
        raise


if __name__ == "__main__":
    if DB_PATH.exists():
        DB_PATH.unlink()
        print("♻️ Существующая база данных удалена")

    define_tables()
    metadata.create_all(engine)
    print("🆕 Создана новая структура базы данных")

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        load_data(session)
    finally:
        session.close()
