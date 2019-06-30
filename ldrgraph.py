import time
#impot numpy as np
import RPi.GPIO as GPIO
import ldr
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


def ldrgraph_level():
	xar = []
	yar = []
	for i in range(50):
		    x=ldr.ldr_level()
	    	    xar.append(float(i))
       	    	    yar.append(float(x))
	    	    draw(xar,yar)
	pylab.show()

def ldrgraph_volts():
	xar = []
	yar = []
	for i in range(50):
		    x=ldr.ldr_volts()
	    	    xar.append(float(i))
       	    	    yar.append(float(x))
	    	    draw(xar,yar)
	pylab.show()