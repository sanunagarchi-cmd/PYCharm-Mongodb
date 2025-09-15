import pymongo


mydata=pymongo.MongoClient("mongodb://localhost:27017/")

mydb= mydata["mydatabase"]
y=mydb["Student"]

mylist=[{"Rollno":105,"Name":'Raju',"Marks":40},
        {"Rollno":106,"Name":'Aman',"Marks":50},
        {"Rollno":107,"Name":'Reena',"Marks":48},
        {"Rollno":108,"Name":'Sonu',"Marks":68},
        {"Rollno":109,"Name":'Monu',"Marks":70},
        {"Rollno":110,"Name":'Saniya',"Marks":45}]

x=y.insert_many(mylist)

print(x.inserted_ids)
