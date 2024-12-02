from . import Base
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import mapped_column, Mapped, declarative_base
Base = declarative_base()
class Pizza(Base):
    __tablename__ = 'pizzas'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[int] = mapped_column(Integer)
    image_url: Mapped[str] = mapped_column(Text)

def __repr__(self):
    return super().__repr__()