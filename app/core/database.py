from sqlalchemy import create_engine, text, Engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import DeclarativeMeta
from typing import Generator, Iterable

from app.core.settings import settings

server: str
port: int
db_name: str
user: str
pwd: str

try:
    server = settings.POSTGRES_SERVER
    port = settings.POSTGRES_PORT
    db_name = settings.POSTGRES_DB
    user = settings.POSTGRES_USER
    pwd = settings.POSTGRES_PASSWORD
    print(server, port, db_name, user, pwd)

except Exception as e:
    print(e)

database_url = f"postgresql+psycopg2://{user}:{pwd}@{server}:{port}/{db_name}"

class DatabaseSessionManager:
    def __init__(self):
        self.engine: Engine | None = None
        self.session_maker = None
        self.session: Session = None

    def init_db(self):
        self.engine = create_engine(
            database_url, pool_size=100, max_overflow=0, pool_pre_ping=False
        )
        if not database_exists(self.engine.url): 
            print("Creating database")
            create_database(self.engine.url)
        
        def test_engine():
            print("Testing DB connection")
            with self.engine.connect() as conn:
                result = conn.execute(text("SELECT 'test complete'"))
                print(result.all())

        test_engine()

        self.session = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    def get_db(self):
        session = sessionmanager.session()
        try:
            yield session
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()

# Initialize the DatabaseSessionManager
sessionmanager = DatabaseSessionManager()
sessionmanager.init_db()



