from app.csv_todb_format import read_csv
from app.loaders.loadCategory import LoadCategories
from app.loaders.loadUsers import LoadUsers
from app.loaders.loadProduct import LoadProducts

categories = LoadCategories("products.csv", read_csv)
categories.load()
users = LoadUsers("customers.csv", read_csv)
users.load()
products = LoadProducts("products.csv", read_csv)
products.load()
