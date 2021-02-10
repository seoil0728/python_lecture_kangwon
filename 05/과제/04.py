def isPrime(n):
  if(n<2):
    return False
  for factor in range(2,n):
    if(n%factor == 0):
      return False
  return True

def getNthPrime(n):
  val=0
  i=2
  while(True):
    if(isPrime(i)):
      val+=1
    if(val==n):
      break
    i += 1
  return i

for n in range(20):
  if isPrime(n):
    print(n, end=" ")
print()

print(getNthPrime(7))