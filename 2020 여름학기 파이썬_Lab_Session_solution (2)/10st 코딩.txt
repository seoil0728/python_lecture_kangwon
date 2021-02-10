from tkinter import *
import math
import time

def rgbString(rgb):
    return "#%02x%02x%02x" % (rgb[0], rgb[1], rgb[2])

def interpolate(t, c1, c2):
    return int((1-t)*c1[0]+t*c2[0]), int((1-t)*c1[1]+t*c2[1]), int((1-t)*c1[2]+t*c2[2])

def drawSun(canvas, width, height, i):
    c = (width-600, height)
    r = min(400, 200) / 4
    hour = i

    angle = math.pi / 2 - 2 * math.pi * hour / 24
    x = c[0] + 600 *  math.cos(angle+math.pi/2)
    y = c[1] - 750 * math.sin(angle+math.pi/2)
    yellowRGB =  (255,255,0) #노랑
    redRGB = (255,0,0)  #빨강
    mixedRGB = interpolate(0.06*i, yellowRGB, redRGB)
    mixed = rgbString(mixedRGB)

    canvas.create_oval(x - r - 15, y - r - 15, x + r + 15, y + r + 15,
                       fill=mixed, tags='sun')

def draw_star(canvas, width, height, t):
    time = t
    x = 200
    y = 150
    if t%2==0:
        point = [110+x*t,10+y,50+x*t,198+y, \
                 200+x*t,78+y,20+x*t,78+y,170+x*t,198+y]
    else:
        point = [110 + x * t, 10, 50 + x * t, 198, \
                 200 + x * t, 78, 20 + x * t, 78, 170 + x * t, 198]
    canvas.create_polygon(point, fill='yellow')




def what_time_is_it(canvas, width, height):
    print("AM6 ~ PM6 -> sun, PM7 ~ AM6 -> star")
    #6
    time = input("Enter your time: ")
    if time == '0':
        return 0
    else:
        clock = 0
        clock += int(time[2:])
        #print(clock)
        if time[0:2] == 'AM':
            if clock >= 6 and clock <= 12:
                clock -=6
                drawSun(canvas, width, height, clock)
            else:
                canvas.destroy()
                return 1
                #draw_star(canvas, width, height, t=6)
        elif time[0:2] == 'PM':
            if clock >=1 and clock <=6:
                clock += 6
                print(clock)
                drawSun(canvas, width, height, clock)
            else:
                canvas.destroy()
                return 1
                #draw_star(canvas, width, height, t=6)


def draw(canvas, width, height):
    # (좌표,위치), 꼭지점, 왼아래, 오아래 == 삼각형
    #(좌표,위치), 왼위, 왼 아래, 오 아래, 오 위 == 사각형

    #지붕
    canvas.create_polygon(600,700, 400,900, 800,900, fill="brown")
    #집
    canvas.create_polygon(450,900, 450,1200, 750,1200, 750,900, fill="orange")
    #대문
    canvas.create_polygon(550,1050, 550,1200, 650,1200, 650,1050, fill="blue")
    #창문
    canvas.create_polygon(500,950, 500,1000, 580,1000, 580,950, fill="skyblue")
    canvas.create_polygon(620, 950, 620, 1000, 680, 1000, 680, 950, fill="skyblue")
    #문손잡이
    canvas.create_polygon(550,1100, 550,1130, 570,1130, 570,1100, fill="red")


def runCanvas(canvas_width, canvas_height):
    master = Tk()
    master.resizable(width=False, height=False)

    canvas = Canvas(master, width=canvas_width, height=canvas_height, background='white')
    canvas.pack()
    draw(canvas, canvas_width, canvas_height)
    #time.sleep(3)
    point = what_time_is_it(canvas, canvas_width,canvas_height)
    if  point == 0:
        for i in range(14):
            if i <= 12:
                canvas.delete('sun')
                drawSun(canvas, canvas_width,canvas_height, i)
                master.update()

                time.sleep(0.5)
            '''
            elif i == 13:
                canvas.destroy()

        canvas = Canvas(master, width=canvas_width, height=canvas_height, background='black')
        canvas.pack()
        draw(canvas, canvas_width, canvas_height)
        for t in range(6):
            draw_star(canvas, canvas_width, canvas_height, t)
        '''
    elif point ==1:
        canvas = Canvas(master, width=canvas_width, height=canvas_height, background='black')
        canvas.pack()
        draw(canvas, canvas_width, canvas_height)
        for t in range(6):
            draw_star(canvas, canvas_width, canvas_height, t)

    master.mainloop()

runCanvas(1200,1200)
