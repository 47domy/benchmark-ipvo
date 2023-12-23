from pymongo import MongoClient
import random

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db["myCollection"]

collection.create_index([('location', '2dsphere')])

print("Created a 2dsphere index on the 'location' field!")