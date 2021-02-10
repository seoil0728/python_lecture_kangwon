def FtoC(x):
  return (x-32) / 1.8

def CtoF(x):
  return x*1.8 + 32

def Reverse(f,t):
  print(t," -> ", eval(f)(t))

fc = input("변환하고 싶은 온도계를 골라주세요. CtoF,FtoC : ")
tm = int(input("온도를 입력해주세요 : "))
Reverse(fc,tm)