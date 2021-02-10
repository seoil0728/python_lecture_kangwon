def sumOfEvensFromMtoN(m,n):
  sum=0
  for i in range(m,n+1):
    if(i%2==0):
      sum=sum+i
  return sum

print(sumOfEvensFromMtoN(1,5))