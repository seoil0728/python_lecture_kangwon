import turtle

print('201413271 김석우')

radius = int(input('그리고자 하는 원의 반지름을 입력해주세요 : '))

turtle.color('blue')
turtle.penup()
turtle.goto(-100, -25)
turtle.pendown()
turtle.circle(radius)
turtle.mainloop()
