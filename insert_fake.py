from pymongo import MongoClient
import random


client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db["myCollection"]

#string = '{location: { type: "Point", coordinates: [ -73.97, 40.77 ] }}'

broj = int(input("Broj dokumenata koje zelite unijeti u MongoDB: \n"))

for _ in range(broj):
    data = {
        "number": random.randint(0,100),
        "location": {
            "type": "Point",
            "coordinates": [random.randint(-180,180), random.randint(-90, 90)]
        }
    }
    collection.insert_one(data)

print("Uneseno ", broj, " dokumenata u MongoDB.")
