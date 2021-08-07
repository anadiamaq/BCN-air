from pymongo import MongoClient
from config import mongo_url
from utils.json_response import str_to_json

client = MongoClient(mongo_url)


def mongo_read(db, coll, query={}, project=None, client=client):
    collection = client.get_database(db)[coll]
    return collection.find(query, project)
