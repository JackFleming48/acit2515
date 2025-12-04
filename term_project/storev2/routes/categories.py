from flask import render_template, Blueprint
from models.categories import Category
from models.product import Product
from db import db

categories_bp = Blueprint("categories", __name__)

@categories_bp.route("/")
def categories_display():
    
    stmt = db.select(Category)

    categories = db.session.execute(stmt).scalars().all()
    print(categories)

    return render_template("categories.html",
                           categories=categories)

@categories_bp.route("/<string:name>")
def category_name(name):
    stmt = db.select(Product).where(Product.category.has(Category.name == name))
    products = db.session.execute(stmt).scalars().all()

    return render_template("category.html",
                           products=products)