from utils.loaders.loadBase import Loader
from utils.database import Session
from utils.models import Product, Category
from sqlalchemy import select

class LoadProducts(Loader):
    def __init__(self, file_name, read_csv):
        super().__init__(file_name, read_csv)
        self._session = Session()

    def load(self):
        data = self._get_data()
        self._insert_session_data(data)
        self._session.commit()
        self._session.close()
    
    def _get_data(self):
        return self._read_csv(self._file_name)
    
    def _insert_session_data(self, data):
        
        for nom, info in (list(data.items()))[1:]:
            possible_product = self._session.execute(select(Product).where(Product.name == nom)).scalar()

            category_obj = self._session.execute(select(Category).where(Category.name == info["category"])).scalar()

            if not possible_product:
                product_obj = Product(name=nom, price=info["price"], inventory=info["inventory"], category_id=category_obj.id)
                self._session.add(product_obj)
            else:
                product_obj = possible_product