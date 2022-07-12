import tkinter as tk
from random import randint, choice
import random
import math




def randomColor():
    de = ("%02x"%randint(0,255))
    re = ("%02x"%randint(0,255))
    we = ("%02x"%randint(0,255))
    ge = "#"
    return ge+de+re+we

colors = ["mintcream","orangered","gold","coral","red", "orange", "yellow", "green", "blue","violet","midnightblue"]
canvas_height = 900
canvas_width = 900
canvas_colour = randomColor()
line_width = 1
randomh = randint(1,900)
randomw = randint(1,900)
randomh2 = randint(1,900)
randomw2 = randint(1,900)

def jagged(self):
     ja = [randint(1,900), randint(1,900), randint(1,900), randint(1,900),
     randint(1,900), randint(1,900), randint(1,900), randint(1,900),
     randint(1,900), randint(1,900), randint(1,900), randint(1,900)]
     canvas.create_polygon(ja, outline = randomColor(), fill = randomColor(), width=2)

def circle(self):
     ci = [randint(1,900), randint(1,900), randint(1,900), randint(1,900)]
     canvas.create_oval(ci, outline = randomColor(), fill = randomColor(), width=2)

def rectangle(self):
     req = [randint(1,900), randint(1,900), randint(1,900), randint(1,900)]
     canvas.create_rectangle(req, outline = randomColor(), fill = randomColor(), width=2)

def pie(self):
     pie = [randint(1,900), randint(1,900), randint(1,900), randint(1,900)]
     canvas.create_arc(pie, start=0, extent=randint(1,180), outline = randomColor(), fill = randomColor(), width=2)

def pac_man(self):
     pac = [randint(1,900), randint(1,900), randint(1,900), randint(1,900)]
     canvas.create_arc(pac, start=180, extent=randint(181,360), outline = randomColor(), fill = randomColor(), width=2)

def point(self):
     pt = [randint(1,900), randint(1,900)]
     canvas.create_polygon(pt, outline = randomColor(), fill = randomColor(), width=2)



window= tk.Tk()
window.title("Art Abstractor")
canvas= tk.Canvas(bg=canvas_colour,height=canvas_height,width=canvas_width, highlightthickness=0)
canvas.pack()
###Click in window to start
window.bind("<Button-1>", pac_man)
window.mainloop()
