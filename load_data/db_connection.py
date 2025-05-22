import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

load_dotenv()
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME')
MONGO_COLLECTION = os.getenv('MONGO_COLLECTION')
MONGO_URI = os.getenv('MONGO_URI')


class MongoDBConnection:
    _instance = None

    def __new__(cls, uri=MONGO_URI, db_name=MONGO_DB_NAME):
        if not cls._instance:
            cls._instance = super(MongoDBConnection, cls).__new__(cls)
            try:
                cls._instance.client = MongoClient(uri)
                cls._instance.client.admin.command('ping')
                cls._instance.db = cls._instance.client[db_name]
                print("Conectado ao MongoDB (Singleton)!")
            except ConnectionFailure as e:
                print(f"Não conectou ao MongoDB: {e}")
                cls._instance = None
        return cls._instance

    def get_collection(self, collection_name=MONGO_COLLECTION):
        if self.db is not None:
            return self.db[collection_name]
        return None

    def close(self):
        if self.client is not None:
            self.client.close()
            print("Conexão com MongoDB encerrada.")
            MongoDBConnection._instance = None
