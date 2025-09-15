import pymongo

mydata=pymongo.MongoClient("mongodb://localhost:27017/")

mydb= mydata["mydatabase"]
y=mydb["Student"]

for x in y.find():
    print(x)



