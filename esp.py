#!/usr/bin/python
import time
import serial
import avr_control

#Set of commands to control esp 8266
#Connects to the pstorm server
#and gets back some data
#
#


def ser_check_reply(ser1, s1, s2):

    c=  ser1.read(10000)
    print("Line is: " + c)
    if (s1 in c) or (s2 in c):
        return 'success'
    else:
        return 'failure'

def test():
    result = []
    ser1 = avr_control.open_serial('/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_siganos1-if00-port0', 115200)

    #check status
    ser1.write("AT\r\n")
    result.append(ser_check_reply(ser1, '\r\nOK\r\n', 'None'))

    #join access point 
    #ser1.write("AT+CWJAP=\"dimitris-public\",\"easypassword456\"\r\n")
    #time.sleep(2)
    #result.append(ser_check_reply(ser1, '\r\nOK\r\n', 'None'))

    #open a tcp connection on port 6004
    ser1.write("AT+CIPSTART=\"TCP\",\"www.pstorm.co.uk\",6004\r\n")
    time.sleep(1)
    result.append(ser_check_reply(ser1, '\r\nOK\r\n', 'CONNECT\r\n'))
    time.sleep(1)

    #send 7 bytes of data
    ser1.write("AT+CIPSEND=7\r\n")
    result.append(ser_check_reply(ser1, '>', 'None'))

    #data to be sent
    ser1.write("HELLO\r\n")
    time.sleep(1)
    result.append(ser_check_reply(ser1, '+IPD,17:7', 'None'))

    #close tcp connection. not needed when talking to pstorm server.
    #ser1.write("AT+CIPCLOSE\r\n")
    #result.append(ser_check_reply(ser1, 'SEND OK\r\n', '\r\nOK\r\n'))
    if result.count('failure') >= 1: return 'failure'
    return 'success'

if __name__ == "__main__":
    test()

