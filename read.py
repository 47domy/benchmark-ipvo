from pymongo import MongoClient
import time
import random


client = MongoClient('mongodb://mongodb:27017/')
db = client['mydatabase']
collection = db['myCollection']

min_lng = random.randint(-40, 0)
max_lng = random.randint(0, 70)
min_lat = random.randint(-40, 0)
max_lat = random.randint(0, 70)

query = {
    "location.coordinates.0": {'$gte': min_lng, '$lte': max_lng},
    "location.coordinates.1": {'$gte': min_lat, '$lte': max_lat}
}

t1 = time.time()
docs = collection.find(query)
num = 0
for doc in docs:
    num += 1
    print(doc)

t2 = time.time()

d = t2 - t1

print("Number of documents found: ", num)
print("Time for reads:", d)