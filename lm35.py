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
  volts = (data * 5.0) / float(1023)
  volts = round(volts,places)
  return volts
 
# Function to calculate temperature from
# TMP36 data, rounded to specified
# number of decimal places.
def ConvertTemp(data,places):
 
  # ADC Value
  # (approx)  Temp  Volts
  #    0      -50    0.00
  #   78      -25    0.25
  #  155        0    0.50
  #  233       25    0.75
  #  310       50    1.00
  #  465      100    1.50
  #  775      200    2.50
  # 1023      280    3.30
 
  temp = ((data * 500)/float(1023))-25
  temp = round(temp,places)
  return temp

def lm35_level(): 
	# Define sensor channels
	temp_channel  = 1
 
	# Define delay between readings
	delay = 5
 
	while True:
 	
  		# Read the temperature sensor data
  		temp_level = ReadChannel(temp_channel)
  		temp_volts = ConvertVolts(temp_level,2)
  		temp       = ConvertTemp(temp_level,2)
  		# Wait before repeating loop
  		return temp_level
		time.sleep(delay)

		

def lm35_volts(): 
	# Define sensor channels
	temp_channel  = 1
 
	# Define delay between readings
	delay = 5
 
	while True:
 	
  		# Read the temperature sensor data
  		temp_level = ReadChannel(temp_channel)
  		temp_volts = ConvertVolts(temp_level,2)
  		temp       = ConvertTemp(temp_level,2)
  		# Wait before repeating loop
  		return temp_volts
		time.sleep(delay)

def lm35_temp(): 
	# Define sensor channels
	temp_channel  = 1
 
	# Define delay between readings
	delay = 5
 
	while True:
 	
  		# Read the temperature sensor data
  		temp_level = ReadChannel(temp_channel)
  		temp_volts = ConvertVolts(temp_level,2)
  		temp       = ConvertTemp(temp_level,2)
  		# Wait before repeating loop
  		return temp
		time.sleep(delay)

