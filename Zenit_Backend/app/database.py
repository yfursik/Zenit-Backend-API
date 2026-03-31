from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Указываем, где будет лежать файл базы данных
# sqlite:///./zenit.db означает "файл zenit.db в текущей папке"
SQLALCHEMY_DATABASE_URL = "sqlite:///./zenit.db"

# 2. Создаем "Движок" (он управляет файлом)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Создаем "Фабрику сессий"
# Каждый раз, когда мы работаем с базой, мы открываем новую "Сессию"
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Базовый класс для всех будущих таблиц
Base = declarative_base()