from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)


def mongo_read(db, coll, query={}, project=None, client=client):
    collection = client.get_database(db)[coll]
    return collection.find(query, project)
