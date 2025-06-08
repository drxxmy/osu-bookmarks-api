from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL_DATABASE = "sqlite:///database.db"

connect_args = {"check_same_thread": False}
engine = create_engine(URL_DATABASE, connect_args=connect_args, echo=True)

Base = declarative_base()

# Import schemes here to register them with Base
import database.schemes

# Create tables
Base.metadata.create_all(engine)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
