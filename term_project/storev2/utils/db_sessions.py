from utils.csv_todb_format import read_csv
from utils.loaders.loadCategory import LoadCategories
from utils.loaders.loadUsers import LoadUsers
from utils.loaders.loadProduct import LoadProducts

def load_categories():
    categories = LoadCategories("products.csv", read_csv)
    categories.load()

def load_users():
    users = LoadUsers("customers.csv", read_csv)
    users.load()
    
def load_products():
    products = LoadProducts("products.csv", read_csv)
    products.load()
