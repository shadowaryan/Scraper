import os
from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient
from Scraper import funcs

load_dotenv()

for func in funcs:
    
    cluster = MongoClient(os.getenv("URL"))
    db = cluster['Scrapper']
    collectionName = str(func).split(' ')[1]
    # print(collectionName)
    collection = db[collectionName]
    collection.insert_many(func())