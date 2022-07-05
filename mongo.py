import pymongo
from pymongo import MongoClient
from Scrapper import Naval, BluntedBuddha

cluster = MongoClient('mongodb+srv://Shadow:WD0NglN7E8IdUBEO@cluster0.mpvcmn9.mongodb.net/?retryWrites=true&w=majority')
db = cluster['Scrapper']
collection = db['Naval']
print(Naval)
collection.insert_many(Naval)