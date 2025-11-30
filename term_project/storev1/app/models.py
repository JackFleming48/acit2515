from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship
from sqlalchemy import String, DECIMAL, Integer, VARCHAR, DATETIME, ForeignKey
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Category(Base):
    __tablename__ = "categories"

    id = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = mapped_column(String, nullable=False)
    products = relationship("Product", back_populates="category")

    def __str__(self):
        return f"{self.id} | {self.name}"

class Product(Base):
    __tablename__ = "product"

    id = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = mapped_column(String, nullable=False)
    price = mapped_column(DECIMAL(10, 2))
    inventory = mapped_column(Integer, default=0, nullable=False)
    category_id = mapped_column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Price: {self.price} | Stock Left:{self.inventory} | Category: {self.category}"
    
class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String, nullable=False)
    phone = mapped_column(Integer, nullable=False)
    password = mapped_column(VARCHAR(255), nullable=False)
    create_date = mapped_column(DATETIME, default=datetime.now, nullable=False)

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | PASSWORD | Ph.: {self.phone} | Create Date: {self.create_date}"

