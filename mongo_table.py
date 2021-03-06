import os
from pymongo import MongoClient

MONGO_URL = '{server}{host_or_user}:{port_or_password}{suffix}'


class MongoTable:
    _db = None

    def __init__(self):
        table_name = self.__class__.__name__
        if not self._db:
            password = os.environ.get('MONGO_PASSWORD')
            if password:
                conn = MongoClient(MONGO_URL.format(
                    server='mongodb+srv://',
                    host_or_user='julio',
                    port_or_password=password,
                    suffix='@cluster0.at3xql1.mongodb.net/test'
                ))
            else:
                conn = MongoClient('mongodb://localhost:27017/')
            self._db = conn['fome_DQ']
        self._collection = self._db.get_collection(table_name)

    def save(self):
        record  = self.__data()
        key = list(record.keys())[0]
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
        return list(self._collection.find(filter=self.__data()))

    def delete(self):
        filter = self.__data()
        if filter:
            self._collection.delete_one(filter)
