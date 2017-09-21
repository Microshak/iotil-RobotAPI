import random
import sys
import iothub_service_client
from iothub_service_client import IoTHubMessaging, IoTHubMessage, IoTHubError
#from iothub_service_client_args import get_iothub_opt, OptionError

from RobotFlask import iothub_service_client_args   


OPEN_CONTEXT = 0
FEEDBACK_CONTEXT = 1
MESSAGE_COUNT = 10

    # String containing Hostname, SharedAccessKeyName & SharedAccessKey in the format:
    # "HostName=<host_name>;SharedAccessKeyName=<SharedAccessKeyName>;SharedAccessKey=<SharedAccessKey>"
CONNECTION_STRING = "HostName=RobotForman.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=eJPYT9KWIMkC+8BYcqulBtVl/QxC0YNf7i7sxqiBFTg="
DEVICE_ID = "PythonTest"

class ioTHub(object):




   

    def sendC2DMsg(msg):
        try:
            iothub_messaging = IoTHubMessaging(CONNECTION_STRING)
            iothub_messaging.set_feedback_message_callback(feedback_received_callback, FEEDBACK_CONTEXT)

            iothub_messaging.open(open_complete_callback, OPEN_CONTEXT)

            message = IoTHubMessage(bytearray(msg, 'utf8'))

         
            iothub_messaging.send_async(DEVICE_ID, message, send_complete_callback, 1)
            
            iothub_messaging.close()
          
        except IoTHubError as iothub_error:
            print ( "Unexpected error {0}" % iothub_error )
            return
        except KeyboardInterrupt:
            print ( "IoTHubMessaging sample stopped" )
        return ''

    def usage():
        print ( "Usage: iothub_messaging_sample.py -c <connectionstring>" )
        print ( "    connectionstring: <HostName=<host_name>;SharedAccessKeyName=<SharedAccessKeyName>;SharedAccessKey=<SharedAccessKey>>" )
        print ( "    deviceid        : <Existing device ID to to send a message to>" )


    if __name__ == '__main__':
        print ( "" )
        print ( "Python {0}".format(sys.version) )
        print ( "IoT Hub Service Client for Python" )
        print ( "" )

        try:
            (CONNECTION_STRING, DEVICE_ID) =  get_iothub_opt(sys.argv[1:], CONNECTION_STRING, DEVICE_ID)
        except OptionError as option_error:
            print ( option_error )
            usage()
            sys.exit(1)

        print ( "Starting the IoT Hub Service Client Messaging Python sample..." )
        print ( "    Connection string = {0}".format(CONNECTION_STRING) )
        print ( "    Device ID         = {0}".format(DEVICE_ID) )

def open_complete_callback(context):
    print ( 'open_complete_callback called with context: {0}'.format(context) )


def send_complete_callback(context, messaging_result):
    context = 0
    print ( 'send_complete_callback called with context : {0}'.format(context) )
    print ( 'messagingResult : {0}'.format(messaging_result) )


def feedback_received_callback(context, batch_user_id, batch_lock_token, feedback_records):
    print ( 'feedback_received_callback called with context: {0}'.format(context) )
    print ( 'Batch userId                 : {0}'.format(batch_user_id) )
    print ( 'Batch lockToken              : {0}'.format(batch_lock_token) )

    if feedback_records:
        number_of_feedback_records = len(feedback_records)
        print ( 'Number of feedback records   : {0}'.format(number_of_feedback_records) )

        for feedback_index in range(0, number_of_feedback_records):
            print ( 'Feedback record {0}'.format(feedback_index) )
            print ( '    statusCode               : {0}'.format(feedback_records[feedback_index]["statusCode"]) )
            print ( '    description              : {0}'.format(feedback_records[feedback_index]["description"]) )
            print ( '    deviceId                 : {0}'.format(feedback_records[feedback_index]["deviceId"]) )
            print ( '    generationId             : {0}'.format(feedback_records[feedback_index]["generationId"]) )
            print ( '    correlationId            : {0}'.format(feedback_records[feedback_index]["correlationId"]) )
            print ( '    enqueuedTimeUtc          : {0}'.format(feedback_records[feedback_index]["enqueuedTimeUtc"]) )
            print ( '    originalMessageId        : {0}'.format(feedback_records[feedback_index]["originalMessageId"]) )
