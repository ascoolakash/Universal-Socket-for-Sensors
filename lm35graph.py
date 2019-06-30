import time
#impot numpy as np
import RPi.GPIO as GPIO
import lm35
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


def lm35graph_level():
	xar = []
	yar = []
	for i in range(50):
		    x=lm35.lm35_level()
	    	    xar.append(float(i))
       	    	    yar.append(float(x))
	    	    draw(xar,yar)
	pylab.show()

def lm35graph_volts():
	xar = []
	yar = []
	for i in range(50):
		    x=lm35.lm35_volts()
	    	    xar.append(float(i))
       	    	    yar.append(float(x))
	    	    draw(xar,yar)
	pylab.show()

def lm35graph_temp():
	xar = []
	yar = []
	for i in range(50):
		    x=lm35.lm35_temp()
	    	    xar.append(float(i))
       	    	    yar.append(float(x))
	    	    draw(xar,yar)
	pylab.show()
