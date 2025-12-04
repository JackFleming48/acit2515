from utils.csv_todb_format import read_csv
from utils.loaders.loadCategory import LoadCategories
from utils.loaders.loadUsers import LoadUsers
from utils.loaders.loadProduct import LoadProducts

categories = LoadCategories("products.csv", read_csv)
categories.load()
users = LoadUsers("customers.csv", read_csv)
users.load()
products = LoadProducts("products.csv", read_csv)
products.load()
