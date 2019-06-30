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

root=Tk()	
root.title("Menu")
#top = Tkinter.Tk()
def lm35_temp():
	a=lm35graph.lm35graph_temp()
   	tkMessageBox.showinfo( "LM35", a)
def lm35_level():
	b=lm35graph.lm35graph_level()
   	tkMessageBox.showinfo( "LM35", b)
def lm35_volts():
	c=lm35graph.lm35graph_volts()
   	tkMessageBox.showinfo( "LM35", c)
def ldr_level():
	level=ldrgraph.ldrgraph_level()
   	tkMessageBox.showinfo( "LDR", level)
def ldr_volts():
	volt=ldrgraph.ldrgraph_volts()
   	tkMessageBox.showinfo( "LDR", volt)
def helloCallBack():
	l1 = Button(root, text ="                           lm35 level                                  ", command = lm35_level)
	l2= Button(root, text ="                            lm35 volts                                    ", command =lm35_volts)
   	l3= Button(root, text ="                            lm35 temperature                                   ", command =lm35_temp)
	l1.pack()
	l2.pack()
	l3.pack()   
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
   x = Button(root, text ="                           x-axis                                  ", command = x_axis)
   y= Button(root, text ="                            y-axis                                    ", command =y_axis)
   z = Button(root, text ="                           z-axis                                  ", command = z_axis)
   x.pack()
   y.pack()
   z.pack()   			

def x_axis():
	x1 = Button(root, text ="                           x level                                  ", command = x_level)
	x2= Button(root, text ="                            x volts                                    ", command =x_volts)
	x1.pack()
	x2.pack()
def x_level():
   xyz=accelerometergraph.accxgraph_level()
   tkMessageBox.showinfo( "accelerometer",xyz)
   
def x_volts():
   xyz1=accelerometergraph.accxgraph_volts()
   tkMessageBox.showinfo( "accelerometer",xyz1)
def y_axis():
	y1 = Button(root, text ="                           y level                                  ", command = y_level)
	y2= Button(root, text ="                            y volts                                    ", command =y_volts)
	y1.pack()
	y2.pack()
def y_level():
   xyz2=accelerometergraph.accygraph_level()
   tkMessageBox.showinfo( "accelerometer",xyz2)
   
def y_volts():
   xyz3=accelerometergraph.accygraph_volts()
   tkMessageBox.showinfo( "accelerometer",xyz3)
def z_axis():
	z1 = Button(root, text ="                           x level                                  ", command = z_level)
	z2= Button(root, text ="                            x volts                                    ", command =z_volts)
	z1.pack()
	z2.pack()
def z_level():
   xyz4=accelerometergraph.acczgraph_level()
   tkMessageBox.showinfo( "accelerometer",xyz4)
   
def z_volts():
   xyz5=accelerometergraph.acczgraph_volts()
   tkMessageBox.showinfo( "accelerometer",xyz5)
	
def helloCallBack6():
   	a1 = Button(root, text ="                           ldr level                                  ", command = ldr_level)
	a2= Button(root, text ="                            ldr volts                                    ", command =ldr_volts)
	a1.pack()
	a2.pack()


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
