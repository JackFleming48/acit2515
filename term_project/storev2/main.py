import sys
from utils.database import engine, Session
from db import db
from app import create_app

app = create_app()

def main():
    if sys.argv[1] == "create":
        try:
            db.metadata.create_all(engine)
        except Exception as e:
            print(f"An error has occurred: {e}")
    elif sys.argv[1] == "drop":
        try:
            db.metadata.drop_all(engine)
        except Exception as e:
            print(f"An error has occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print("you must run main.py with args either 'create' or 'drop'")
