import sys
import random
from db import db
from app import create_app
from sqlalchemy import select, func
from datetime import datetime as dt
from datetime import timedelta
from flask import Flask

from models.users import User
from models.categories import Category
from models.product import Product
from models.order import Order, ProductOrder
from models.users import User

from utils import db_sessions

app = create_app()

def main():

    with app.app_context():

        print("DB URI =", app.config["SQLALCHEMY_DATABASE_URI"])
        print("Engine =", db.get_engine())
        print("Tables =", db.Model.metadata.tables)

        command = sys.argv[1].lower()

        if command == "create":
            try:
                db.create_all()
            except Exception as e:
                print(f"An error has occurred: {e}")
        elif command == "drop":
            try:
                db.drop_all()
            except Exception as e:
                print(f"An error has occurred: {e}")
        elif command == "seed":
            db_sessions.load_categories()
            db_sessions.load_products()
            db_sessions.load_users()
        elif command == "rand":
            rand_orders()

def rand_orders():
    num_orders = 5

    for x in range(num_orders):

        customer = db.session.execute(select(User).order_by(func.random())).scalars().first()

        order = Order(customer=customer)

        num_products = random.randint(3, 6)
        products = db.session.execute(select(Product).order_by(func.random()).limit(num_products)).scalars().all()

        for product in products:
            quantity = random.randint(1, 10)
            line = ProductOrder(product=product, quantity=quantity, order=order)
            db.session.add(line)

        db.session.add(order)

    db.session.commit()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print("you must run main.py with args either 'create' or 'drop' or 'seed' or 'drop'")
