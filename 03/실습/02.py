def myAdd(a,b):
  return a+b

def mySubtract(a,b):
  return a-b

def myMultiply(a,b):
  return a*b

def myDivide(a,b):
  return a/b

def myCalculate(func, a, b):
  return func(a,b)

print(myCalculate(myAdd, 1, 3))
print(myCalculate(mySubtract, 6, 2))
print(myCalculate(myMultiply, 2, 2))
print(myCalculate(myDivide, 8, 2))
