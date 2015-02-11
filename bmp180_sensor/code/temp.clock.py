#!/usr/bin/python

# Needs bmp180 code from https://github.com/keiichishima/RPiSensors
from Tkinter import *
import time
import smbus
import bmp180

root = Tk()
time1 = ''

bus = smbus.SMBus(1)
sensor = bmp180.Bmp180(bus)
sensor.os_mode = 3

clockDisplay = Label(root, font = ('fixed', 24, 'bold'))
clockD.grid(row = 2, column = 5, columnspan = 2, padx = 5, pady = (2,2))

tempDisplay = Label(root, font=('fixed', 20), )
tempDisplay.grid(row = 1, column = 5, padx = 5, pady = (5,2))

pressDisplay = Label(root, font=('fixed', 20), )
pressDisplay.grid(row = 3, column = 5, padx = 5, pady = (2,5))

def tick():
    global time1
    press, temp = sensor.pressure_and_temperature
    tempVal = "%2.1f%sC" % (temp, unichr(176))
    pressVal = "%4.2f hPa" % (press)
    pressDisplay.config(text=pressVal)
    tempDisplay.config(text=tempVal)
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clockDisplay.config(text=time2)
    clockDisplay.after(200, tick)

tick()
root.mainloop()
