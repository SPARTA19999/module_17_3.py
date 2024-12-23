from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Объект Base, который используется для описания моделей
Base = declarative_base()

# Пример строки подключения, измените на свою БД
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # или ваша база данных

# Создаем движок для базы данных
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Создаем SessionLocal, который будем использовать для работы с БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
