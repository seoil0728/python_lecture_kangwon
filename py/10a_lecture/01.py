from tkinter import *

def draw(canvas, width, height):
    x1, x2 = width/4, width/2
    y1, y2 = height/4, height/2
    canvas.create_rectangle(x2-x1, y2-y1, x2+x1, y2+y1, fill="red")


def runCanvas(canvas_width, canvas_height):
    master = Tk()
    master.resizable(width=False, height=False)
    canvas = Canvas(master, width=canvas_width, height=canvas_height)
    canvas.pack()
    draw(canvas, canvas_width, canvas_height)
    master.mainloop()

runCanvas(400,200)