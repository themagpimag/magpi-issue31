#!/usr/bin/python

import smbus
import bmp180

bus = smbus.SMBus(1)
sensor = bmp180.Bmp180(bus)
print sensor.pressure_and_temperature

