import pymongo
# with pymongo.MongoClient('172.28.171.13') as client:
client = pymongo.MongoClient(host='172.28.171.13', port=27017)
db=client.JDLT
coll=db.jdlt_midea
# coll.remove()
# client.database_names()
for each in coll.find():
    print(each)
print(db.collection_names())
print(coll.find_one())