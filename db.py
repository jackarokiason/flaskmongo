from flask import Flask
from flask_pymongo import pymongo
from app import app
CONNECTION_STRING = "ownURI"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('flask_mongodb_atlas')
user_collection = pymongo.collection.Collection(db, 'user_collection')
