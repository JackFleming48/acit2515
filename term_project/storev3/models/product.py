from db import db

class Product(db.Model):
    __tablename__ = "product"

    id = db.mapped_column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.mapped_column(db.String, nullable=False)
    price = db.mapped_column(db.DECIMAL(10, 2))
    inventory = db.mapped_column(db.Integer, default=0, nullable=False)
    category_id = db.mapped_column(db.Integer, db.ForeignKey("categories.id"))
    category = db.relationship("Category", back_populates="products")

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Price: {self.price} | Stock Left:{self.inventory} | Category: {self.category}"