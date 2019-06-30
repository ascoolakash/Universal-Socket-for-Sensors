#import Tkinter
from Tkinter import *
import tkMessageBox
import time
import RPi.GPIO as GPIO
import qwe
#import usonic
#top = Tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")
   qwe.abc()
def helloCallBack1():
   import usonic
   data=usonic.reading(0)
   #import test01.py
   #data=test01.graph()
   tkMessageBox.showinfo( "ultrasoni",data)
   #GPIO.setwarnings(False)	
   # use the values of the GPIO pins, and not the actual pin number
   # so if you connect to GPIO 25 which is on pin number 22, the 
   # reference in this code is 25, which is the number of the GPIO 
   # port and not the number of the physical pin
   #GPIO.setmode(GPIO.BCM)
   #GPIO.setup(14,GPIO.OUT)
   #GPIO.output(14, GPIO.HIGH)
   #GPIO.output(14, GPIO.LOW)
		
root=Tk()	
root.title("ultrasonic")
B = Button(root, text ="Temperature Sensor", command = helloCallBack)
C = Button(root, text ="Ultrasonic Sensor", command = helloCallBack1)
quitButton = Button(root, text="Quit", command=exit)


B.pack()
C.pack()
quitButton.pack(side=LEFT)
#top.mainloop()

#app=App(root)
root.mainloop()
