import time
#impot numpy as np
import RPi.GPIO as GPIO
import accelerometer
import pylab
import sys
import datetime
import gc



def graph():

	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	usonic.initialize()
def draw(xdata,ydata):
		pylab.figure(1)
		pylab.plot(xdata,ydata)


def accxgraph_level():
	xar = []
	yar = []
	for i in range(50):
		    x=accelerometer.acc_x_level()
	    	    xar.append(float(i))
       	    	    yar.append(float(x))
	    	    draw(xar,yar)
	pylab.show()

def accxgraph_volts():
	xar = []
	yar = []
	for i in range(50):
		    x=accelerometer.acc_x_volts()
	    	    xar.append(float(i))
       	    	    yar.append(float(x))
	    	    draw(xar,yar)
	pylab.show()
def accygraph_level():
	xar = []
	yar = []
	for i in range(50):
		    x=accelerometer.acc_y_level()
	    	    xar.append(float(i))
       	    	    yar.append(float(x))
	    	    draw(xar,yar)
	pylab.show()

def accygraph_volts():
	xar = []
	yar = []
	for i in range(50):
		    x=accelerometer.acc_y_volts()
	    	    xar.append(float(i))
       	    	    yar.append(float(x))
	    	    draw(xar,yar)
	pylab.show()
def acczgraph_level():
	xar = []
	yar = []
	for i in range(50):
		    x=accelerometer.acc_z_level()
	    	    xar.append(float(i))
       	    	    yar.append(float(x))
	    	    draw(xar,yar)
	pylab.show()

def acczgraph_volts():
	xar = []
	yar = []
	for i in range(50):
		    x=accelerometer.acc_z_volts()
	    	    xar.append(float(i))
       	    	    yar.append(float(x))
	    	    draw(xar,yar)
	pylab.show()