import sys
from tkinter import Tk,LabelFrame,PhotoImage
root = Tk()

img = PhotoImage( file=sys.argv[1])
IMG = LabelFrame(root,image=img)

IMG.pack()

root.mainloop()
