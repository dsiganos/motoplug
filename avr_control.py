#!/usr/bin/python
import time
import serial

#Turns on and of the avr -io-m16 board
#Works with the factory firmware
#
#
def open_serial(serdev, baudrt):
    defserdev ='/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller-if00-port0'
    if serdev == None:
        serdev = defserdev
    ser = serial.Serial(
        port=serdev,
        baudrate=baudrt,
        timeout=2,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
)
    ser.xonxoff = False
    ser.rtscts = False
    ser.dsrdtr = False 
    return ser

def open_all(ser):
    ser.write("o")
    print("Turned all relays on")

def close_all(ser):
    ser.write("c")
    print("Turned all relays off")

def toggle_relay(ser, relaynumber):
    if relaynumber > 4 or relaynumber < 0:
        raise Exception('Relay Number is not between 1 and 4')
    ser.write("%s" % relaynumber)
    print("toggle relay %s" % relaynumber)

if __name__ == "__main__":
    ser = open_serial(None, 9600)
    open_all(ser)
    time.sleep(2)
    close_all(ser)
    time.sleep(2)
    toggle_relay(ser, 1)
    time.sleep(2)
    toggle_relay(ser, 2)
    time.sleep(2)
    toggle_relay(ser, 3)
    time.sleep(2)
    toggle_relay(ser, 4)
    time.sleep(2)
    close_all(ser)
