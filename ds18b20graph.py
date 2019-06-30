import time
#impot numpy as np
import RPi.GPIO as GPIO
import ds18b20
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


def ds18b20graph_c():
	xar = []
	yar = []
	for i in range(50):
		    x=ds18b20.ds18b20_temp_c()
	    	    xar.append(float(i))
       	    	    yar.append(float(x))
	    	    draw(xar,yar)
	pylab.show()

def ds18b20graph_f():
	xar = []
	yar = []
	for i in range(50):
		    x=ds18b20.ds18b20_temp_f()
	    	    xar.append(float(i))
       	    	    yar.append(float(x))
	    	    draw(xar,yar)
	pylab.show()