# importing module
from pymongo import MongoClient
from bson.binary import Binary
import os
import gridfs
from PIL import Image
from pylab import imshow, show, get_cmap
from numpy import random
import pylab as plt
import numpy as np
print("Step1")
if os.path.exists("testfile.001"):
    os.remove("testfile.001")
    print("The file has been deleted successfully")
else:
    print("The file does not exist!")

print("Step2")
newfile = open("testfile.001", "a")
#newfile.write (os.urandom(500000000))    # generate 500MB random content file
newfile.write(str(os.urandom(5000000)))
newfile.close()
x = newfile.name

# Connect with the portnumber and host
try:
    client = MongoClient("mongodb://localhost:27017/",username='root',password='rwIJNavOkO')
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

db = client['test_database_5']
coll = db['mycoll']
fs = gridfs.GridFS(db)
with open(x, 'rb') as f:
    contents = f.read()

fs.put(contents, filename="testfile.001")

list_of_db = client.list_database_names()
print(list_of_db)

print(db.command("collstats", "events"))
print(db.command("dbstats"))

"""for i in fs.find():
    print(i)"""


#os.remove(x)


"""# Access database
mydatabase = client['test_database']

# Access collection of the database
mycollection = mydatabase['myTable']

# dictionary to be added in the database
record = {
    'title': 'MongoDB and Python',
    'description': 'MongoDB is no SQL database',
    'tags': ['mongodb', 'database', 'NoSQL'],
    'viewers': 104
}

# inserting the data in the database
rec = mydatabase.myTable.insert_one(record)

for i in mydatabase.myTable.find({'title': 'MongoDB and Python'}):
    print(i)

try:
    conn = MongoClient("mongodb://localhost:27017/",username='root',password='rwIJNavOkO')
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

# database name: mydatabase
db = conn.test_database

# Created or Switched to collection names: myTable
collection = db.myTable

# To find() all the entries inside collection name 'myTable'
cursor = collection.find()
for record in cursor:
    print(record)"""


#print(x.inserted_id)