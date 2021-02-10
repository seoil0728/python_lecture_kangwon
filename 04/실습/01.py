def compare(a,b,c):
  mxm = a
  if (mxm < b):
    mxm = b
  if (mxm < c):
    mxm = c
  return mxm

x=int(input("Enter a: "))
y=int(input("Enter b: "))
z=int(input("Enter c: "))

print(x,y,z,"중 가장 큰 값은", compare(x,y,z),"입니다.")