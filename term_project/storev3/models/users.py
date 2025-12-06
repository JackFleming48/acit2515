from db import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "customers"

    id = db.mapped_column(db.Integer, primary_key=True, autoincrement=True)
    name = db.mapped_column(db.String, nullable=False)
    phone = db.mapped_column(db.Integer, nullable=False)
    password = db.mapped_column(db.VARCHAR(255), nullable=False)
    orders = db.relationship("Order", back_populates="customer")
    create_date = db.mapped_column(db.DateTime, default=datetime.now, nullable=False)

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | PASSWORD | Ph.: {self.phone} | Create Date: {self.create_date}"