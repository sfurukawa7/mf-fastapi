from sqlalchemy import create_engine
from config import MIGRATE_DB_URL
from database import Base

engine = create_engine(MIGRATE_DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    reset_database()
