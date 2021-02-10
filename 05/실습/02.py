def input_count():
  count = 0
  cnt_P = 0
  cnt_N = 0
  cnt_Z = 0
  while(count < 10):
    number=int(input("Enter Number :"))
    if(number>0):
      cnt_P += 1
    elif(number<0):
      cnt_N += 1
    else:
      cnt_Z += 1
    count += 1
  return cnt_P, cnt_N, cnt_Z

x,y,z = input_count()
print("Number of Positive Integers :", x)
print("Number of Negative Integers :", y)
print("Number of Zero :", z)
