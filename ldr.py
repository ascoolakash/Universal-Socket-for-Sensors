#!/usr/bin/python
 
import spidev
import time
import os
 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  if channel>7 or channel<0:
	return -1
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts
 
def ldr_levels():
	# Define sensor channels
	light_channel = 0
	# Define delay between readings
	delay = 5
 
	while True:
 
 		 # Read the light sensor data
  		light_level = ReadChannel(light_channel)
  		light_volts = ConvertVolts(light_level,2)
 		 # Wait before repeating loop
  		return light_level
		time.sleep(delay)
		

def ldr_volts():
	# Define sensor channels
	light_channel = 0
	# Define delay between readings
	delay = 5
 
	while True:
 
 		 # Read the light sensor data
  		light_level = ReadChannel(light_channel)
  		light_volts = ConvertVolts(light_level,2)
 		 # Wait before repeating loop
  		return light_volts
		time.sleep(delay)
		