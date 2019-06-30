#import Tkinter
from Tkinter import *
import tkMessageBox
import time
import RPi.GPIO as GPIO
import qwe
import usonicgraph
import ldrgraph
import lm35graph
#import ds18b20graph
import thermistergraph
import pirgraph
import accelerometergraph

#top = Tkinter.Tk()

def helloCallBack():
   data=lm35graph.lm35graph_temp()
   tkMessageBox.showinfo( "LM35", data)
def helloCallBack1():
   data1=usonicgraph.usonicgraph()
   tkMessageBox.showinfo( "ultrasonic",data1)
def helloCallBack2():
   data2=thermistergraph.thermistergraph()
   tkMessageBox.showinfo( "thermister",data2)
def helloCallBack3():
   data3=ds18b20graph.ds18b20graph_c()
   tkMessageBox.showinfo( "DS18B20",data3)
def helloCallBack4():
   data4=pirgraph.pirgraph()
   tkMessageBox.showinfo( "pir",data4)
def helloCallBack5():
   data5=accelerometergraph.accxgraph_volts()
   tkMessageBox.showinfo( "accelerometer",data5)
def helloCallBack6():
   data6=ldrgraph.ldrgraph_volts()
   tkMessageBox.showinfo( "ldr",data6)
		
root=Tk()	
root.title("Menu")
B = Button(root, text ="                            Temperature Sensor(LM35)                                  ", command = helloCallBack)
C = Button(root, text ="                            Ultrasonic Sensor                                   ", command = helloCallBack1)
D = Button(root, text ="                            Thermister                                          ", command = helloCallBack2)
E = Button(root, text ="                            Temperature Sensor(DS18B20)                                  ", command = helloCallBack3)
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
