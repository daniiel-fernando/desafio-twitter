import os
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://dio:dio@localhost:27017/")
client = MongoClient(MONGO_URI)

db = client.dio_live
trends_collection = db.trends
