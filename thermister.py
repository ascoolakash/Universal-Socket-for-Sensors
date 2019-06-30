#!/usr/bin/python
# -*- coding: utf-8 -*-
# A simple script to log data from the MCP3208
# Based off mcp3208.py

import spidev
import time
import math
from time import strftime
import string

spi = spidev.SpiDev()
spi.open(0, 0)
 
def ReadChannel(channel):
  if channel>7 or channel<0:
	return -1
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

#thermistor reading function
def thermister_temp():
    thermister_channel=2
    value = ReadChannel(thermister_channel) #read the adc
    volts = (value * 3.3) / 1024 #calculate the voltage
    ohms = ((1/volts)*3300)-1000 #calculate the ohms of the thermististor

    lnohm = math.log1p(ohms) #take ln(ohms)

    #a, b, & c values from http://www.thermistor.com/calculators.php
    #using curve R (-6.2%/C @ 25C) Mil Ratio X
    a =  0.002197222470870
    b =  0.000161097632222
    c =  0.000000125008328

    #Steinhart Hart Equation
    # T = 1/(a + b[ln(ohm)] + c[ln(ohm)]^3)

    t1 = (b*lnohm) # b[ln(ohm)]

    c2 = c*lnohm # c[ln(ohm)]

    t2 = math.pow(c2,3) # c[ln(ohm)]^3

    temp = 1/(a + t1 + t2) #calcualte temperature

    tempc = (temp - 273.15 - 4)/8 + 8 #K to C
    # the -4 is error correction for bad python math

    #print out info
#    print ("%4d/1023 => %5.3f V => %4.1f Ω => %4.1f °K => %4.1f °C from adc %d" % (value, volts, ohms, temp, tempc, adc))
    return tempc
