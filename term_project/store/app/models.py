from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, DECIMAL, Integer, VARCHAR, DATETIME


class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "product"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    price = mapped_column(DECIMAL(10, 2))
    inventory = mapped_column(Integer, default=0)
    category = mapped_column(String)

    def __str__(self):
        return f"{self.id} | {self.name} | (${self.price} - Stock Left:{self.inventory}) | {self.category}"
    
class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    email = mapped_column(VARCHAR)
    password = mapped_column(VARCHAR)
    create_date = mapped_column(DATETIME)

    def __str__(self):
        return f"{self.id} | {self.name} | PASSWORD , {self.email} | {self.create_date}"
