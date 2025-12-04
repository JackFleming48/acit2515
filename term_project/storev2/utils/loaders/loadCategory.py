from utils.loaders.loadBase import Loader
from db import db
from models.categories import Category
from sqlalchemy import select

class LoadCategories(Loader):
    def __init__(self, file_name, read_csv):
        super().__init__(file_name, read_csv)
        self._session = db.session

    def load(self):
        data = self._get_data()
        self._insert_session_data(data)
        self._session.commit()
        self._session.close()

    # get data using read csv and return formatted data
    def _get_data(self):
        return self._read_csv(self._file_name)
    
    # insert items categories into the session
    # making sure to not insert duplicates into the session
    def _insert_session_data(self, data):

        for item in (list(data.values()))[1:]:
            item = item["category"]

            possible_category = self._session.execute(select(Category).where(Category.name == item)).scalar()

            if not possible_category:
                # add item to session as category
                category_obj = Category(name=f"{item}")
                self._session.add(category_obj)
            else:
                category_obj = possible_category

        