import abc

class Loader(abc.ABC):
    """This is the ABC for loading CSV files for insertion to the database.
    Enforces abstractmethods for each type of loader to follow.
    """

    @abc.abstractmethod
    def __init__(self, file_name, read_csv):
        self._file_name = file_name
        self._read_csv = read_csv
        

    @abc.abstractmethod
    def _get_data(self):
        pass

    @abc.abstractmethod
    def _insert_session_data(self):
        pass