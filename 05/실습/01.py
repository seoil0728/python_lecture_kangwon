def print_divisor(x):
  count=0
  for i in range(1,x+1):
    if(x%i==0):
      print(i)
      count += 1
  print("d_cnt = ", count)

print("input your number to print divisor!!")
number = int(input("input your number : "))
print_divisor(number)