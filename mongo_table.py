from pymongo import MongoClient

MONGO_URL = '{server}{host_or_user}:{port_or_password}{suffix}'


class MongoTable:
    _db = None

    def __init__(self):
        table_name = self.__class__.__name__
        if not self._db:
            conn = MongoClient('mongodb://localhost:27017/')
            self._db = conn['fome_DQ']
        self._collection = self.db.get_collection(table_name)

    def save(self):
        record  = self.__data()
        key = record.keys()[0]
        self._collection.update_one(
            {key: record[key]},
            {'$set': record},
            upsert=True
        )

    def __data(self) -> dict:
        return {
            k: v for k, v in self.__dict__.items()
            if not k.startswith('_') and v
        }

    def find(self) -> list:
        return self._collection.find(filter=self.__data())

    def delete(self):
        filter = self.__data()
        if filter:
            self._collection.delete_one(filter)
