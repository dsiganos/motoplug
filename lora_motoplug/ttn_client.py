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
    print "\n\n\n"
    print 'App_id: ' + str(msg_dict['app_id'])
    print "Dev_id: " + str(msg_dict['dev_id'])
    print "Hardware_Serial: " + str(msg_dict['hardware_serial'])
    print "Port: " +str(msg_dict['port'])
    print "Frame Counter: " +str(msg_dict['counter'])
    print "Payload: " + repr(base64.b64decode(msg_dict['payload_raw']))
    print "Time: " + str(msg_dict['metadata']['time'])
    print "Frequency: " + str(msg_dict['metadata']['frequency'])
    print "Modulation: " + str(msg_dict['metadata']['modulation'])
    print "Data Rate: " + str(msg_dict['metadata']['data_rate'])
    print "Coding_rate: " + str(msg_dict['metadata']['coding_rate'])
    print "Gateway Id: " + str(msg_dict['metadata']['gateways'][0]['gtw_id'])
    print "Gateway Timestamp: " + str(msg_dict['metadata']['gateways'][0]['timestamp'])
    print "Gateway Time: " + str(msg_dict['metadata']['gateways'][0]['time'])
    print "Gateway Channel: " + str(msg_dict['metadata']['gateways'][0]['channel'])
    print "Gateway RSSI: " + str(msg_dict['metadata']['gateways'][0]['rssi'])
    print "Gateway SNR: " + str(msg_dict['metadata']['gateways'][0]['snr'])
    print "\n\n\n"

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

