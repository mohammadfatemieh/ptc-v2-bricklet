#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your PTC Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_ptc_v2 import BrickletPTCV2

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    ptc = BrickletPTCV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current temperature
    temperature = ptc.get_temperature()
    print("Temperature: " + str(temperature/100.0) + " °C")

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
