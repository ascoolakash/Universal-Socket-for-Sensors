from Tkinter import *

root = Tk()

toolbar = Frame(root)

# All the buttons in my program
b = Button(toolbar, text="Home", width=9)
b.pack(side=LEFT, padx=2, pady=2)

b = Button(toolbar, text="About-us", width=9)
b.pack(side=LEFT, padx=2, pady=2)

b = Button(toolbar, text="Contact-us", width=9)
b.pack(side=LEFT, padx=2, pady=2)

b = Button(toolbar, text="Travelling", width=9)
b.pack(side=LEFT, padx=2, pady=2)


toolbar.pack(side=TOP, fill=X)

# All the labels in my program
o = Label(root,text="Frank Anne",font =("Italic",18,"bold"))
o.pack()

toolbar1 = Frame(root)

o=Label(root,)
o.pack()


o=Label(root,text ="Age:                     27")
o.pack()

o=Label(root,text ="Address:                 71 strawberry lane, JU8 8TY")
o.pack()

toolbar1.pack(side=BOTTOM, fill=X)

mainloop()
