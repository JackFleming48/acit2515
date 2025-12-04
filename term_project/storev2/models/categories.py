from db import db

class Category(db.Model):
    __tablename__ = "categories"

    id = db.mapped_column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.mapped_column(db.String, nullable=False)
    products = db.relationship("Product", back_populates="category")

    def __str__(self):
        return f"{self.id} | {self.name}"