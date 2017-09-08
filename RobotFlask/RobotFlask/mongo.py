
from flask import Blueprint

from datetime import datetime
from flask import render_template
from RobotFlask import app

from bson.json_util import dumps
import pymongo

from pymongo import MongoClient

from bson.son import SON

from bson.code import Code

from flask import Response
from flask import request
from bson.objectid import ObjectId

db = Blueprint('db', __name__)
uri =app.config["mongouri"]
mongoclient = MongoClient(uri)
dba = mongoclient.SawyerDB
collection = dba.Command    

@db.route('/commands/<string:name>', methods=['GET'])
def get_command(name):
    data = collection.find({"Name": name}).sort("Order", pymongo.ASCENDING)

    resp = Response(response=dumps(data),
                    status=200,
                    mimetype="application/json")
        

    return resp

def generateData(dat):
       updateDic = {
            "Cartisian.position.x":dat['Cartisian[position][x]'],
            "Cartisian.position.y":dat['Cartisian[position][y]'],
            "Cartisian.position.z":dat['Cartisian[position][z]'],
            "Cartisian.orientation.x":dat['Cartisian[orientation][x]'],
            "Cartisian.orientation.y":dat['Cartisian[orientation][y]'],
            "Cartisian.orientation.z":dat['Cartisian[orientation][z]'],
            "Cartisian.orientation.w":dat['Cartisian[orientation][w]'],
            "FriendlyName":dat["FriendlyName"],
            "Order":dat["Order"],
            "Speed":dat["Speed"]
        }
       return updateDic
 
@db.route('/command/Move', methods=['POST'])
def save_command():
    
    dat = request.form
   
    updateDic = generateData(dat)
    

@db.route('/command/Save', methods=['POST'])
def save_command():
    
    dat = request.form
   
    updateDic = generateData(dat)
  
    
    collection.update(
        {"_id":  ObjectId(dat["_id"])},
        {
        "$set": updateDic
        }, upsert=True
    )
    resp = Response(response=dumps(dat),
                    status=200,
                    mimetype="application/json")

    return resp

'''
    
    data = collection.find()
    output = set()
  
    for x in data:
        output.add(x["Name"])
   
    resp = Response(response=dumps(output),
                    status=200,
                    mimetype="application/json")
     return resp   
'''  

#Microsoft Mongo does not support aggragation.. :(
@db.route('/command/All', methods=['GET'])
def all_commands():
    data = collection.find()
    output = set()
  
    for x in data:
        output.add(x["Name"])
   
    resp = Response(response=dumps(output),
                    status=200,
                    mimetype="application/json")
        

    return resp
