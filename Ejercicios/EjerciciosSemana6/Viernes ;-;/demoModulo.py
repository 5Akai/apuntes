from pymongo import MongoClient, collection
from flask import request
from bson.json_util import dumps, loads

server = "localhost"

port = 27017

db = "northwind"

def Get_Customers_List() -> str:
    try:
        return list(Get_Customers_List("customers").find{}, {"_id": 0})
    except Exception as e:
        return{"Error": e}

def Get_Customer(id) -> str:
    try:
        return __Get_Collection("customers").find_one{"CustomerID": id}, {"_id": 0}))
    except Exception as e:
        return{"Error": e}
    
def __Get_Collection(collection, server=server, port=port, )