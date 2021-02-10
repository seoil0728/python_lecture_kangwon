from tkinter import *
import math

def drawClock(canvas, width, height):
    c = (width / 2, height / 2)
    r = min(width, height) / 3
    canvas.create_oval(c[0] - r - 15, c[1] - r - 15, c[0] + r + 15, c[1] + r + 15, fill="yellow")
    canvas.create_polygon(50, 30, 150, 50, 250, 30, 150, 10, fill="green")

    for hour in range(12):
        angle = math.pi / 2 - 2 * math.pi * hour / 12
        x = c[0] + r * math.cos(angle)
        y = c[1] - r * math.sin(angle)
        label = str(hour if (hour > 0) else 12)
        canvas.create_text(x, y, text=label, font="Calibri 14 bold")

    angle = math.pi / 2 - 2 * math.pi * 4 / 12
    x = c[0] + r * math.cos(angle)
    y = c[1] - r * math.sin(angle)
    canvas.create_line(c,x-17,y-12, width=3)
    angle = math.pi / 2 - 2 * math.pi * 0 / 12
    x = c[0] + r * math.cos(angle)
    y = c[1] - r * math.sin(angle)
    canvas.create_line(c,x,y)



def rgbString(rgbValue):
    return "#%02x%02x%02x" % (rgbValue[0], rgbValue[1], rgbValue[2])

def interpolate(t, c1, c2):
    return int((1-t)*c1[0]+t*c2[0]), int((1-t)*c1[1]+t*c2[1]), int((1-t)*c1[2]+t*c2[2])

def runCanvas(canvas_width, canvas_height):
    # create a window
    master = Tk()
    # window cannot be resized
    master.resizable(width=False, height=False)
    # create a canvas widget
    canvas = Canvas(master, width=canvas_width, height=canvas_height)
    # pack the canvas widget
    canvas.pack()
    # run the application, wait for an event to occur and process the event as long as the window is not closed.
    drawClock(canvas, canvas_width, canvas_height)
    master.mainloop()

runCanvas(400,200)