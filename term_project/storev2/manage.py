import sys
from db import db
from app import create_app

from models.users import User
from models.categories import Category
from models.product import Product

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


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print("you must run main.py with args either 'create' or 'drop'")
