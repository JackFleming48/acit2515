from db import db
from .product import Product
from datetime import datetime


class Order(db.Model):
    __tablename__ = "orders"

    id = db.mapped_column(db.Integer, primary_key=True)
    created = db.mapped_column(db.DateTime, default=datetime.now)
    completed = db.mapped_column(db.DateTime, nullable=True)
    customer_id = db.mapped_column(db.Integer, db.ForeignKey("customers.id"))
    customer = db.relationship("User", back_populates="orders")
    items = db.relationship("ProductOrder", back_populates="order")
    amount = db.mapped_column(db.DECIMAL(6, 2), nullable=True, default=None)


    def estimate(self):
        total = 0
        for po in self.items:
            one = po.product.price * po.quantity
            total = total + one
        return total
    
    def complete(self):
        for po in self.items:
            if po.quantity > po.product.inventory:
                raise ValueError(f"Not enough stock for {po.product.name} needed for {po.product.inventory}")
            
        for po in self.items:
            po.product.inventory -= po.quantity

    
        self.completed = datetime.now()
        self.amount = self.estimate()



class ProductOrder(db.Model):
    __tablename__ = "product_order"

    product_id = db.mapped_column(db.ForeignKey("product.id"), primary_key=True)
    order_id = db.mapped_column(db.ForeignKey("orders.id"), primary_key=True)
    quantity = db.mapped_column(db.Integer, nullable=False)
    product = db.relationship('Product')
    order = db.relationship('Order', back_populates='items')
