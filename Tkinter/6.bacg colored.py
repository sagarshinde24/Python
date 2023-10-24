from tkinter import Tk,Label

root = Tk()

label = Label(root,text = 'Welcome to my world SAGAR SHINDE')

label.config(font=('callibri',24,'italic bold underline'))

label.pack()

label.configure(foreground = 'red',background = 'yellow')#,text = 'updated text !!!!')

root.mainloop()

