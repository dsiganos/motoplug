#!/usr/bin/python
import threading
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import base64
import json
import sys

#Call back functions 

# gives connection message
def on_connect(client,userdata,rc):
    print("Connected with result code:"+str(rc))
    # subscribe for all devices of user
    client.subscribe('+/devices/+/up')

# gives message from device
def on_message(client,userdata,msg):
    msg_dict = json.loads(msg.payload)
#    print"Topic",msg.topic + "\nMessage:" + str(msg.payload)
    print "\n\n\n"
    print "Last voltage received:" + repr(base64.b64decode(msg_dict['payload_raw']))
#    print 'App_id: ' + str(msg_dict['app_id'])
#    print "Dev_id: " + str(msg_dict['dev_id'])
#    print "Hardware_Serial: " + str(msg_dict['hardware_serial'])
#    print "Port: " +str(msg_dict['port'])
#    print "Frame Counter: " +str(msg_dict['counter'])
#    print "Payload: " + repr(base64.b64decode(msg_dict['payload_raw']))
#    print "Time: " + str(msg_dict['metadata']['time'])
    print "Date:" + str(msg_dict['metadata']['time'][0:10])
    print "Time:" + str(msg_dict['metadata']['time'][11:19])
#    print "Frequency: " + str(msg_dict['metadata']['frequency'])
#    print "Modulation: " + str(msg_dict['metadata']['modulation'])
#    print "Data Rate: " + str(msg_dict['metadata']['data_rate'])
#    print "Coding_rate: " + str(msg_dict['metadata']['coding_rate'])
#    print "Gateway Id: " + str(msg_dict['metadata']['gateways'][0]['gtw_id'])
#    print "Gateway Timestamp: " + str(msg_dict['metadata']['gateways'][0]['timestamp'])
#    print "Gateway Time: " + str(msg_dict['metadata']['gateways'][0]['time'])
#    print "Gateway Channel: " + str(msg_dict['metadata']['gateways'][0]['channel'])
#    print "Gateway RSSI: " + str(msg_dict['metadata']['gateways'][0]['rssi'])
#    print "Gateway SNR: " + str(msg_dict['metadata']['gateways'][0]['snr'])
    print "\n\n\n"

#def on_log(client,userdata,level,buf):
#    print("message:" + str(buf))
#    print("userdata:" + str(userdata))

def print_menu():
    print 'Press \"on\" to send an on command'
    print 'Press \"off\" to send an off command'
    print 'Press q to quit'

def publish_command(topic, command):
    print 'sending \"%s command\" in the queue' %command
    result, mid = mqttc.publish(topic, command)
    print "This is the result of the publish effort:%s %s" % (str(result),mid)

def check_button():
    while True:
        print_menu()
        text = raw_input()
        if text == "on":
            publish_command(topic, on_command)
        elif text == "off":
            publish_command(topic, off_command)
        elif text == "q":
            mqttc.loop_stop()
            sys.exit()
        else:
            pass

topic = 'george_gkekis_packet_storm_app/devices/01/down'
on_command = '{"payload_raw": "T04="}'
off_command = '{"payload_raw": "T0ZG"}'

mqttc= mqtt.Client()
mqttc.on_connect=on_connect
mqttc.on_message=on_message
#mqttc.on_log=on_log

mqttc.username_pw_set("george_gkekis_packet_storm_app","ttn-account-v2.FtYIbM6FDiDP1ju9uH2kKZYJYvwYBNF93c4yD9vXKOg")
mqttc.connect("eu.thethings.network",1883,10)

# and listen to server
mqttc.loop_start()
check_button()
