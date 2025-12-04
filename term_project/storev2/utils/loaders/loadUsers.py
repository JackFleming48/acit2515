from utils.loaders.loadBase import Loader
from utils.database import Session
from utils.models import User
from sqlalchemy import select

class LoadUsers(Loader):
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
        
        for nom, info in list(data.items())[1:]:
             
            possible_user = self._session.execute(select(User).where(User.phone == info["phone"])).scalar()

            if not possible_user:
                user_obj = User(name=nom, phone=info["phone"], password=info["password"])
                self._session.add(user_obj)
            else:
                user_obj = possible_user