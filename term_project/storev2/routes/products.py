from flask import Flask, render_template, redirect, url_for, Blueprint
from models.product import Product
from models.categories import Category
from db import db

products_bp = Blueprint("products", __name__)

@products_bp.route("/")
def products_display():

    stmt = db.select(Product)

    products = db.session.execute(stmt).scalars().all()
    # print(products)

    return render_template("products.html",
                           products=products)