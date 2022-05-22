import sys
import time
import random
import pymongo
class DBINFORM:
    def __init__(self):
        self.myclient= pymongo.MongoClient("mongodb+srv://glkingf:<password>@cluster0.mnlfs.mongodb.net/?retryWrites=true&w=majority")
        self.my_db=self.myclient["my_project"]
        self.my_coll=self.my_db["eb-bill"]
    def func_name():
       return sys._getframe(1).f_code.co_name
    def insert_data(self,data):
       self.my_coll.insert_one(data)
       print("{} Successfully".format(DBINFORM.func_name()))
    def read_data(self,):
       result=self.my_coll.find()
       for i in result:
           print("Name:{}",format(i))
       print("{} Successfully".format(DBINFORM.func_name()))
    def update_data(self,uname,values):
       self.my_coll.update_one(uname,values)
       print("{} Successfully".format(DBINFORM.func_name()))
    def delete_data(self,data):
        self.my_coll.delete_one(data)
        print("{} Successfully".format(DBINFORM.func_name()))
dbobj=DBINFORM()
data={"uname": "Arun",
  "upassword": "123",
  "oldunit": 10,
  "newunit": 20,
  "__v": 656}
def mainfunction():
    action=int(input("1.insert/n 2.read./n3.update. /n4.delete"))
    global data
    if(action==1):
        print("insert_data")
        dbobj.insert_data(data)
    elif(action==2):
        print("read_data")
        dbobj.read_data()
    elif(action==3):
        print("update_data")
        uname=input("Enter a element to update")
        uname={ "uname":uname}
        values=input("input name")
        values={"$set":{"uname":values}}
        dbobj.update_data(uname,values)
    else:
        print("delete_data")
        uname=input("Enter a element to Delete")
        data={ "uname":uname}
mainfunction()
        dbobj.delete_data(data)
