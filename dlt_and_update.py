from tkinter import *
import pymongo
root=Tk()
l1=Label(text="Rollno")
l2=Label(text="Update")
t1=Entry()
t2=Entry()
t3=Entry()
def delete():
    mydata=pymongo.MongoClient("mongodb://localhost:27017/")

    mydb= mydata["mydatabase"]
    mytb=mydb["Student"]

    myquery={"Rollno":int(t1.get())}

    x=mytb.delete_one(myquery)
    print(x)

def update():
    mydata = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = mydata["mydatabase"]
    mytb = mydb["Student"]
    myquery={"Rollno":int(t2.get())}
    newvalues={"$set":{"Marks":t3.get()}}

    x=mytb.update_one(myquery, newvalues)
    print(x.modified_count, "Documents updated.")

b1=Button(text="Delete",command=delete)
b2=Button(text="Update",command=update)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
t1.grid(row=0,column=1)
t2.grid(row=1,column=1)
t3.grid(row=2,column=1)
b1.grid(row=3,column=0)
b2.grid(row=3,column=3)
mainloop()
