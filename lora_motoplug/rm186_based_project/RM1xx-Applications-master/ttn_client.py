# Simple Python client to show node activity from ttn MQTT brooker with credentials
 
import paho.mqtt.client as mqtt
import base64
import json

#Call back functions 

# gives connection message
def on_connect(client,userdata,rc):
    print("Connected with result code:"+str(rc))
    # subscribe for all devices of user
    client.subscribe('+/devices/+/up')

# gives message from device
def on_message(client,userdata,msg):
    msg_dict = json.loads(msg.payload)
    print"Topic",msg.topic + "\nMessage:" + str(msg.payload)
    print 'app_id ' + str(msg_dict['app_id'])
    print "dev_id " + str(msg_dict['dev_id'])
    print "hardware_serial " + str(msg_dict['hardware_serial'])
    print "port " +str(msg_dict['port'])
    print "counter " +str(msg_dict['counter'])
    print "payload " + repr(base64.b64decode(msg_dict['payload_raw']))

#def on_log(client,userdata,level,buf):
#    print("message:" + str(buf))
#    print("userdata:" + str(userdata))

mqttc= mqtt.Client()
mqttc.on_connect=on_connect
mqttc.on_message=on_message

mqttc.username_pw_set("george_gkekis_packet_storm_app","ttn-account-v2.FtYIbM6FDiDP1ju9uH2kKZYJYvwYBNF93c4yD9vXKOg")
mqttc.connect("eu.thethings.network",1883,10)

# and listen to server
run = True
while run:
    mqttc.loop()

