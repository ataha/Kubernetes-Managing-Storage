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

imarray = np.random.rand(20000,20000,3) * 255
im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
#image = image.resize((4*z, 3*z), Image.ANTIALIAS)

"""plt.imshow(Z, cmap=get_cmap("Spectral"), interpolation='nearest')
plt.show()"""



newfile = open("testfile.001", "a")
#newfile.write (os.urandom(500000000))    # generate 500MB random content file
newfile.write(str(os.urandom(50)))
newfile.close()


"""def main():
    coll = db.sample
    with open('/Users/ahmedhagag/Personal/PycharmProjects/Automate_boaring_stuff/testfile.001', "rb") as f:
        encoded = Binary(f.read())

    coll.insert({"filename": '/Users/ahmedhagag/Personal/PycharmProjects/Automate_boaring_stuff/testfile.001', "file": encoded, "description": "test"})

"""
# Connect with the portnumber and host
try:
    client = MongoClient("mongodb://localhost:27017/",username='root',password='rwIJNavOkO')
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

db = client['test_database_2']
fs = gridfs.GridFS(db)
with open('/Users/ahmedhagag/Personal/PycharmProjects/Automate_boaring_stuff/result_image.png', 'rb') as f:
    contents = f.read()

fs.put(contents, filename="result_image.png")

list_of_db = client.list_database_names()
print(list_of_db)

print(db.command("collstats", "events"))
print(db.command("dbstats"))

"""for i in fs.find():
    print(i)"""


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