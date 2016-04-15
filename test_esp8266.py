#!/usr/bin/python
import time
import serial
import avr_control
import esp

#Tests esp 8266 reliability. powers up the module
# checks that it repsonds, that it can connect to
# a server and send and receive data
#
#avr board is used to power on and off the module
#
iterations = 5
results =[]
avr_ser = avr_control.open_serial(None, 9600)
i=1
while i <= iterations:
    print 'this is iteration %s' % i
    #turn esp on
    avr_control.open_all(avr_ser)
    time.sleep(1) # this is for the module to boot
    #test
    results.append(esp.test())
    time.sleep(1)
    #turn esp off
    avr_control.close_all(avr_ser)
    time.sleep(1)
    print 'results are: %s' % results
    i = i + 1
avr_ser.close()
print 'total tries are %s' % len(results)
passes = results.count('success')
fails = results.count('failure') 
print 'total passes are %s' % passes
print 'total fails are %s' % fails

