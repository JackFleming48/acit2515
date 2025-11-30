import sys
from app.database import engine, Session
from app.models import Base

def main():
    if sys.argv[1] == "create":
        try:
            Base.metadata.create_all(engine)
        except Exception as e:
            print(f"An error has occurred: {e}")
    elif sys.argv[1] == "drop":
        try:
            Base.metadata.drop_all(engine)
        except Exception as e:
            print(f"An error has occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print("you must run main.py with args either 'create' or 'drop'")
