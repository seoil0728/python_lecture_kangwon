import math

a = int(input("a값을 입력해주세요 : "))
b = int(input("b값을 입력해주세요 : "))
c = int(input("c값을 입력해주세요 : "))

x1 = (-b + math.sqrt(pow(b,2) - 4*a*c)) / 2*a
x2 = (-b - math.sqrt(pow(b,2) - 4*a*c)) / 2*a

print("x1=",x1,"x2=",x2)