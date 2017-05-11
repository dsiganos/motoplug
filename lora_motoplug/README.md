# Motoplug

This project is based on an RM186 Laird lora module.
It connects to a 12V battery (car or motorcycle) and reports the battery's
voltage once every hour. The data are received by the TTN (the things network)
and then we use a python script over MQTT protocol to receive the data.
There is a voltage divider constructed by 2 resistors. The first one is actually
three resistors in series at 13.52 kOhm, and the second one is 1 kOhm.
There is a button on the RM186 dev board and a led. We can turn the led on and off
from the python script.
Each time we send a command from the python script this command will go in a queue
and will get sent to the mote the next time the mote transmits something.
So, for example, if we want to turn the led on, we need to press "on" on the python
script and then press the button to send data from the RM186. After the data have
been received from the TTN, our command will be sent from TTN to the mote and will get
executed.

# How to run the project.
* Power up the Rm186.
* Power up the lora gateway.
* Connect WB50 to the internet either by connecting an Ethernet cable or by setting up the wifi connection.
* Power up the WB50.
* Log in the WB50.
   * Find out the address of the serial port by issuing: ls /dev/serial/by-id
   * Start minicom: minicom -D  serial port address
   * Username is root, password is summit
   * Go to /temp/lora and run ./lora_pkt_fwd
* Start Uwterminal which watches the RM186.
   * ./UwTerminalX COM=/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A502GU7M-if00-port0 ACCEPT BAUD=115200 STOP=1 DATA=8 PAR=0 FLOW=1 ENDCHR=0 LOCALECHO=1 LOG+
   * ( Need to be in the folder where the uwterminal file is located)
   * Right click and choose load and run.
   * Select the program to run. (lora_motoplug.uwc)
* Start the python script. Run: python ttn_client.py 



# motoplug

## How to start the UwTerminalX with all the settings from command line

./UwTerminalX COM=/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A502GU7M-if00-port0 ACCEPT BAUD=115200 STOP=1 DATA=8 PAR=0 FLOW=1 ENDCHR=0 LOCALECHO=1 LOG+



## Open an account to the things network (TTN)
https://account.thethingsnetwork.org/users/login

## Install UwTerminalX
Go to https://github.com/LairdCP/UwTerminalX/releases

To install it in Linux:
Download the release you want.
tar xf UwTerminalX.tar ~/    // This is to unzip the release to the home folder.

And then to run the UwTerminalX:
./UwTerminalX

## Connect and Power up the devices.
The Laird gateway powers up with 5 volts DC. It needs a lot of power so the power
supply should be more than 500 mA.
Power up the gateway first. Then power up the WB50. This is very important.
There is a chance that the gateway will burn if we don't follow this sequence.

The Laird Lora client (RM 186 test bench) takes its power from a micro USB cable
which is also used to get access to the device through a terminal.

The WB50 needs to connect to the host computer through a usb-to-serial cable.
We use minicom to get access to it.

Pins in Laird's gateway:
Starting from the side that has the pins(the ones that seem as they can be inserted somewhere):
Vcc, Spi_Csn0, Spi_Clk, Spi_Miso, Spi_Mosi, Led2, Gnd.
Ground pin is connected both to the power supply and the WB50 board.
These are the pins where the cables are going. At the time of this writing we
do not have any documentation from Laird so not sure what the pins are.
They end up at the SPI group and the Led2 one ends up at the GPIO group at the WB50 test bench.

The Laird gateway is connected through an spi bus to the WB50 test bench.
When we power up the WB50 we need to go to /opt/lora and run the packet_forwarder program.
(lora_pkt_fwd)

## Activate the gateway at TTN.
Connect to the WB50. Go to /opt/lora. Open local_conf.json file and see what the
"gateway_ID" is. In our case it is: "c0ee40FFFE293402"
We will later need to change the following values: "server_address"
                                                     "serv_port_up"
                                                     "serv_port_down"

On TTN from our console we select register new gateway.
Activation method is bridge.
The gateway EUI is the gateway id we saw earlier on the local_conf.json file.
For frequency plan we choose Europe and 868Mhz.
We set a location and press the register button on the right bottom of the page.

## Configure the gateway.
We need to change the following values:             "server_address"
                                                     "serv_port_up"
                                                     "serv_port_down"
For TTN these values must be:"server_address": "router.eu.thethings.network",
"serv_port_up": 1700,"serv_port_down": 1700.

After setting these values we need to reboot the wb50.
Once it has rebooted we need to start the lora packet forwader. (lora_pkt_fwd)


## Activate the lora client at TTN.
On TTN from the console select applications.
We need to create an application, so we select add application.
We give an arbitrary application id and a description and continue.
Then we select the application we just created and select devices and then register device.
We give an arbitrary device id and then we either give an arbitrary device EUI or
we ask the system to generate one for us.
All the above we will need to store on our client.


## Configure the lora client.
We start the client and the commands to give are: 
at+cfgex 1010 "AppEui"
at+cfgex 1011 "DevEui"
at+cfgex 1012 "AppKey"

We reboot the client and then we run one of the sample applications.
The one called lora.connect.sb will try and send some dummy data at intervals.

## This is where to get sample applications for the RM186 dev kit:
https://github.com/LairdCP/RM1xx-Applications


## How to upload and run a program in the Lora RM186 Dev Kit.
Just press right click on the UwTerminalX and select 'compile and run' on the
emerging menu.


## How to figure out which compiler you need:
AT I 0 : gives the modules name: RM186_PE
AT I 13 : gives the hash signature: CD09 4F27


## How to start the UwTerminalX with all the settings from command line

./UwTerminalX COM=/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A502GU7M-if00-port0 ACCEPT BAUD=115200 STOP=1 DATA=8 PAR=0 FLOW=1 ENDCHR=0 LOCALECHO=1 LOG+

