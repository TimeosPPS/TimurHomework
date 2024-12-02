from sqlalchemy import (
    create_engine,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker
)

DB = "sqlite:///app.db"

engine = create_engine(DB, echo=True)

Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    ...

def create_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)