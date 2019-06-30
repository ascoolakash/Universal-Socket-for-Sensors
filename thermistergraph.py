import time
#impot numpy as np
import RPi.GPIO as GPIO
import thermister
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


def thermistergraph():
	xar = []
	yar = []
	for i in range(50):
		    x=thermister.thermister_temp()
	    	    xar.append(float(i))
       	    	    yar.append(float(x))
	    	    draw(xar,yar)
	pylab.show()