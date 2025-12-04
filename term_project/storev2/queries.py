from utils.database import Session
from utils.models import Category, Product, User
from sqlalchemy import select

session = Session()

def get_p_out_of_stock(session):
    stmt = select(Product).where(Product.inventory == 0)
    res = session.execute(stmt)
    for p in res.scalars():
        print(p)

def get_name_contains(session):
    stmt = select(User).where(User.name.contains("ma"))
    res = session.execute(stmt)
    for p in res.scalars():
        print(p)

def get_dairy_products(session):
    stmt = select(Product).where(Product.category_id == 4)
    res = session.execute(stmt)
    for p in res.scalars():
        print(p)

    stmt = select(Category).where(Category.name == "dairy")
    res = session.execute(stmt).scalar_one_or_none()
    for p in res.products:
        print(p)

def get_dairy_out_of_stock(session):
    stmt = select(Product).where(Product.inventory == 0 and Product.category_id == 4)
    res = session.execute(stmt)
    for p in res.scalars():
        print(p)

# get_p_out_of_stock(session)
# get_name_contains(session)
# get_dairy_products(session)
# get_dairy_out_of_stock(session)