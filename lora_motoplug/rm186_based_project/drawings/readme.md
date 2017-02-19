Motoplug_design_v1.jpg is the design of the project as it will be when finished.
The protection module has not been determinded where exactly it will sit, that's
the reason why you can see to different places on the drawing.

Motoplug_design_v0_2.jpg is the design of the project as it currently is.
The project is based on the RM186 Dev Kit. We have used the SPI expander to connect
a led and have used button number 2 to issue commands to send data.
As it is the project sends data that reads from the ADC pin every hour. The data
are received by TTN and then our python script which is connected to TTN, takes
them. From the python script we can send two commands. (The commands will be sent
right after the RM186 sends data. That is if an hour has passed or if we have
pressed button number 2 on the Dev Kit.) These commands are on or off and they
turn on and off respectively the led that is connected on the RM 186. (led 1)

Motoplug_design.jpg is the first complete and working project. Basically we just
connected a voltage divider on the RM186 Dev Kit and send the data read from the
ADC pin to TTN over Lora.

Detailed.jpg is a close up look on all the connections of the RM186. Will be very
useful when the breakout board arrives to be able to connect the RM186 and create
a standalone project, that is with no need of the RM186 Dev Kit.
