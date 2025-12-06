from flask import Flask, render_template, redirect, url_for, Blueprint
from models.order import Order
from models.categories import Category
from db import db

order_bp = Blueprint("order", __name__)

@order_bp.route("/")
def order_display():

    stmt = db.select(Order)

    orders = db.session.execute(stmt).scalars().all()

    return render_template("orders.html",
                           orders=orders)

@order_bp.route("/<int:id>")
def order_id(id):
    stmt = db.select(Order).where(Order.id == id)
    order = db.session.execute(stmt).scalars().first()

    if order is None:
        return "Order Not Found", 404
    
    return render_template("order.html", order=order)

@order_bp.route("/<int:id>/complete", methods=["POST"])
def complete_order(id):
    order = db.session.get(Order, id)

    if order is None:
        return "Order Not Found", 404
    
    try:
        order.complete()
        db.session.commit()
        return redirect(url_for("orders.order_id", id=id))
    
    except ValueError as e:
        return f"Error: {e}", 404