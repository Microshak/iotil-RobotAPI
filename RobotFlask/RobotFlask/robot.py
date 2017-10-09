
from flask import Blueprint

from datetime import datetime
from flask import render_template
from RobotFlask import app
from bson.json_util import dumps

from flask import Response
from flask import request

import random
import sys
import iothub_service_client
from iothub_service_client import IoTHubMessaging, IoTHubMessage, IoTHubError
import json
from RobotFlask import common
from RobotFlask import ioTHub

import time



robot = Blueprint('robot', __name__)
hubstring =app.config["iothub"]
MESSAGING_CONTEXT = 34
CONNECTION_STRING = hubstring
DEVICE_ID = 'PythonTest'
connectionString = 'HostName=RobotForman.azure-devices.net;DeviceId=PythonTest;SharedAccessKey=oh9Fj0mAMWJZpNNyeJ+bSecVH3cBQwbzjDnoVmeSV5g='


 
@robot.route('/robot/Move', methods=['POST'])
def go_command():
    
    dat = request.form
    messagetxtfake =  "{\"service client sent a message\": \"to\"}"
   
    updateDic =common.common.generateData(dat)
    msg = json.dumps(updateDic)
    ioTHub.ioTHub.sendC2DMsg(msg)
    #ioTHub.ioTHub.iothub_messaging_sample_run()

    resp = Response(status=200, mimetype="application/json")
    return resp
