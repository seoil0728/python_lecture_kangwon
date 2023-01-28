import turtle

print('201413271 김석우')

turtle.pensize(5)
turtle.speed(0)

turtle.color('blue')
turtle.penup()
turtle.goto(-100, -25)
turtle.pendown()
turtle.circle(45)

turtle.color('yellow')
turtle.penup()
turtle.goto(-50, -75)
turtle.pendown()
turtle.circle(45)

turtle.color('black')
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(45)

turtle.color('green')
turtle.penup()
turtle.goto(50, -75)
turtle.pendown()
turtle.circle(45)

turtle.color('red')
turtle.penup()
turtle.goto(100, -25)
turtle.pendown()
turtle.circle(45)

turtle.mainloop()
