from azure.iot.device import IoTHubDeviceClient, Message
import Adafruit_DHT
import time

from azure.iot.device import IoTHubDeviceClient, Message

sensor = Adafruit_DHT.DHT11

gpio = 17


CONNECTION_STRING = "HostName=rsraspberrypihub.azure-devices.net;DeviceId=RaspberryPi;SharedAccessKey=f7lqEV4S+/gU0CULjHTPkdclJJWuhS86rz7KmE9wY5c="


MSG_TXT = '{{"temperature": {temperature}}}'


def iothub_client_init():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )

        while True:
            HUMIDITY, TEMPERATURE = Adafruit_DHT.read_retry(sensor, gpio)
            if HUMIDITY is not None and TEMPERATURE is not None:
             temperature = '{0:0.1f}*C'.format(TEMPERATURE)
             #humidity = 'Humidity={1:0.1f}%'.format(HUMIDITY)
             msg_txt_formatted = MSG_TXT.format(temperature=temperature)
             message = Message(msg_txt_formatted)

             print("Sending message: {}".format(message))
             client.send_message(message)

         

            # Send the message.
             print( "Sending message: {}".format(message) )
             client.send_message(message)
             print ( "Message successfully sent" )
             time.sleep(1)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()
