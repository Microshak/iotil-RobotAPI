
from flask import Blueprint

from datetime import datetime
from flask import render_template
from RobotFlask import app

from bson.json_util import dumps
import pymongo

from pymongo import MongoClient

from bson.son import SON

from bson.code import Code

db = Blueprint('db', __name__)
uri =app.config["mongouri"]
mongoclient = MongoClient(uri)
dba = mongoclient.SawyerDB
collection = dba.Command    

@db.route('/commands/<string:name>', methods=['GET'])
def get_command(name):
    data = collection.find({"Name": name}).sort("Order", pymongo.ASCENDING)
    return dumps(data)


#Microsoft Mongo does not support aggragation.. :(
@db.route('/command/All', methods=['GET'])
def all_commands():
    data = collection.find()
    output = set()
  
    for x in data:
        output.add(x["Name"])
        
    return dumps(output)
'''
@db.route('/commands/Update<int:id>/<:value>', methods=['GET'])
def update():
    db.ProductData.update_one({
  '_id': p['_id']
    },{
  '$set': {
    'd.a': existing + 1
     }
    }, upsert=False)
 '''