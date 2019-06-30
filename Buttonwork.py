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
def helloCallBack2():
   import usonic
   data=usonic.reading(0)
   #import test01.py
   #data=test01.graph()
   tkMessageBox.showinfo( "ultrasoni",data)
def helloCallBack3():
   import usonic
   data=usonic.reading(0)
   #import test01.py
   #data=test01.graph()
   tkMessageBox.showinfo( "ultrasoni",data)
def helloCallBack4():
   import usonic
   data=usonic.reading(0)
   #import test01.py
   #data=test01.graph()
   tkMessageBox.showinfo( "ultrasoni",data)
def helloCallBack5():
   import usonic
   data=usonic.reading(0)
   #import test01.py
   #data=test01.graph()
   tkMessageBox.showinfo( "ultrasoni",data)
def helloCallBack6():
   import usonic
   data=usonic.reading(0)
   #import test01.py
   #data=test01.graph()
   tkMessageBox.showinfo( "ultrasoni",data)
		
root=Tk()	
root.title("ultrasonic")
B = Button(root, text ="                            Temperature Sensor                                  ", command = helloCallBack)
C = Button(root, text ="                            Ultrasonic Sensor                                   ", command = helloCallBack1)
D = Button(root, text ="                            Thermister                                          ", command = helloCallBack2)
E = Button(root, text ="                            Temperature Sensor                                  ", command = helloCallBack3)
F = Button(root, text ="                            PIR Sensor                                          ", command = helloCallBack4)
G = Button(root, text ="                            Acclerometer                                        ", command = helloCallBack5)
H = Button(root, text ="                            Light Dependent Resitor                             ", command = helloCallBack6)
quitButton = Button(root, text="Quit", command=exit)


B.pack()
C.pack()
D.pack()
E.pack()
F.pack()
G.pack()
H.pack()
quitButton.pack(side=LEFT)
#top.mainloop()

#app=App(root)
root.mainloop()
