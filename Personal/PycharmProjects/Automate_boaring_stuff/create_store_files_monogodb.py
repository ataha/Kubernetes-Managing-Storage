#!python
#pip install --user pymongo
#pip install --user gridfs
#pip install --user os
from pymongo import MongoClient
import os
import gridfs


database = 'test_database'                  #The name of the Database

# Connect with the portnumber and host
try:
    client = MongoClient("mongodb://localhost:27017/", username='root', password='rwIJNavOkO')   #specify the host,port,username and password of mongodb
    print("Connected successfully to Mongodb!")
except:
    print("Could not connect to MongoDB")

client.drop_database(database)


for numFile in range(10):                      #How many files to be uploaded

    if os.path.exists("testfile.001"):
        os.remove("testfile.001")
    else:
        print("The file does not exist!")


    newfile = open("testfile.001", "a")
    #newfile.write (os.urandom(500000000))      # generate 500MB random content file
    newfile.write(str(os.urandom(399000)))
    newfile.close()
    x = newfile.name


    db = client[database]
    fs = gridfs.GridFS(db)
    with open(x, 'rb') as f:
        contents = f.read()

    fs.put(contents, filename="testfile.001")
    file_stats = os.stat(x)

    print(f'New File uploaded with Size {int(file_stats.st_size / (1024 * 1024))} MegaBytes ')


print(f"{numFile + 1} files are uploaded successfully")

dic = db.command("dbstats")
print(f'Total dataSize uploaded into DB { database }: { int(dic["dataSize"] / (1024 * 1024)) } MegaBytes')

