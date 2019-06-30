#from PIL import Image
import Image
from Tkinter import *
path = './smile.gif'
#root=Tk()
#b=Button(root,justify = LEFT)
#photo=PhotoImage(file="smile.gif")
#b.config(image=photo,width="10",height="10")
#b.pack(side=LEFT)
#root.mainloop()

root = Tk()
img = PhotoImage(Image.open(path))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()