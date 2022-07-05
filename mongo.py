import os
from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient
from Scraper import Naval

cluster = MongoClient('mongodb+srv://Shadow:WD0NglN7E8IdUBEO@cluster0.mpvcmn9.mongodb.net/?retryWrites=true&w=majority')
db = cluster['Scrapper']
collection = db['Naval']
print(Naval())
collection.insert_many(Naval())