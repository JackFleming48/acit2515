from db import db
from datetime import datetime


class Order(db.Model):
    __tablename__ = "orders"

    id = db.mapped_column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    created = db.mapped_column(db.DateTime, default=datetime.now, nullable=False)
    completed = db.mapped_column(db.DateTime, default=None, nullable=True)
    amount = db.mapped_column(db.DECIMAL(6,2), defualt=None, nullable=True)
    items = db.relationship('ProductOrder', back_populates='order')

class ProductOrder(db.Model):
    __tablename__ = "product_order"

    product_id = db.mapped_column(db.ForeignKey("product.id"), primary_key=True)
    order_id = db.mapped_column(db.ForeignKey("order.id"), primary_key=True)
    quantity = db.mapped_column(db.Integer, nullable=False)
    product = db.relationship('Product')
    order = db.relationship('Order', back_populates='items')
