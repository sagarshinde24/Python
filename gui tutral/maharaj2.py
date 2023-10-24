import time
import tkinter as tk

from PIL import Image, ImageTk, ImageSequence


class App:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tk.Canvas(parent, width=350, height=250)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(rb'raje1.gif'))]
        self.image = self.canvas.create_image(160,120, image=self.sequence[0])
        self.animate(1)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(20, lambda: self.animate((counter+1) % len(self.sequence)))





def printString(item, string):
    if item:
        for char in string:
            idx = c.index(item, tk.END)
            c.insert(item, idx, char)
            c.update()
            time.sleep(.05)


root = tk.Tk()
root.title('SAGAR SHINDE!')
text = "\t\t\t|||राजमुद्रा||| \n \n \t\tप्रतिपच्चंद्रलेखेव। वर्धिष्णुर्विश्ववंदिता। \n \t\tशाहसूनो: शिवस्यैषा मुद्रा भद्राय राजते।।"
c = tk.Canvas(root ,bg='orange')

c_txt = c.create_text(100,100)
c.pack( expand=True)
c.update()
printString(c_txt, text)
app = App(c)

root.mainloop()