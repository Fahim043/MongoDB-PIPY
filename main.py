import pymongo
client = pymongo.MongoClient("localhost", 27017)
dataBase = client["UnoPro"]

collection = dataBase['Products']

d= {'companyName':'AiByters',
    'product':'Affordable AI',
    'courseOffered':'ML Crash course'}

rec=collection.insert_one(d)

all_record=collection.find()

for idx, record in enumerate(all_record):
    print(f"{idx}:{record}")