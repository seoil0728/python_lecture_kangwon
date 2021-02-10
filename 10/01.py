from tkinter import *
import math

def draw(canvas, width, height):
    brown = (180,100,42)
    color1 = rgbString(brown)

    canvas.create_polygon(width/2, height/2, width/4, height/2+150, width/4*3, height/2+150, fill="purple")
    canvas.create_rectangle(width/2-150,height/2+150,width/2+150,height, fill="gray")
    canvas.create_rectangle(width/2-100,height/2+200,width/2-50, height/2+250, fill="blue")
    canvas.create_rectangle(width/2+100,height/2+200,width/2+50, height/2+250, fill="blue")
    canvas.create_rectangle(width/2-30,height/2+280,width/2+30,height, fill=color1)


def drawSun(canvas,width,height,i):
    yellowRGB = (255, 255, 0)
    redRGB = 255, 0, 0
    mixedRGB = interpolate(i/12, yellowRGB, redRGB)
    colors = rgbString(mixedRGB)
    canvas.create_oval(width,height,width+75,height+75,fill=colors,tags="sun")

def WTII():
    times = int(input("Enter your time : "))
    return times

def rgbString(rgbValue):
    return "#%02x%02x%02x" % (rgbValue[0], rgbValue[1], rgbValue[2])

def interpolate(t, c1, c2):
    return int((1-t)*c1[0]+t*c2[0]), int((1-t)*c1[1]+t*c2[1]), int((1-t)*c1[2]+t*c2[2])

def runCanvas(canvas_width, canvas_height):
    # create a window
    master = Tk()
    # window cannot be resized
    master.resizable(width=False, height=False)
    a = WTII()
    # create a canvas widget
    if(a==0):
        canvas = Canvas(master, width=canvas_width, height=canvas_height, bg="white")
        canvas.pack()
        draw(canvas, canvas_width, canvas_height)
        for i in range(24):
            if (i >= 6 and i <= 18):
                x, y = calculateByTime(canvas_width, canvas_height, i - 6)
                drawSun(canvas, x, y, i-6)
    else:
        if(a>=6 and a<=18):
            canvas = Canvas(master, width=canvas_width, height=canvas_height, bg="white")
        else:
            canvas = Canvas(master, width=canvas_width, height=canvas_height, bg="black")
    # pack the canvas widget
        canvas.pack()
    # run the application, wait for an event to occur and process the event as long as the window is not closed.
        draw(canvas, canvas_width, canvas_height)
        if(a>=6 and a<=18):
            x,y = calculateByTime(canvas_width, canvas_height,a-6)
            drawSun(canvas,x,y,a-6)
    master.mainloop()

def calculateByTime(width, height,i):
    c = (width / 2, height)
    r = min(width, height)/3 + 150
    angle = math.pi / 1 - 1 * math.pi * i / 12
    x = c[0]-50 + r * math.cos(angle) *6/7
    y = c[1] - r * math.sin(angle) - 100
    return x,y

'''
    for hour in range(12):
        angle = math.pi / 2 - 2 * math.pi * hour / 12
        x = c[0] + r * math.cos(angle)
        y = c[1] - r * math.sin(angle)
        label = str(hour if (hour > 0) else 12)
        canvas.create_text(x, y, text=label, font="Calibri 14 bold")
        
        
        if(i>=6 and i<=18):
                canvas = Canvas(master, width=canvas_width, height=canvas_height, bg="white")
            else:
                canvas = Canvas(master, width=canvas_width, height=canvas_height, bg="black")
            canvas.pack()
            draw(canvas, canvas_width, canvas_height)
'''


runCanvas(800,800)