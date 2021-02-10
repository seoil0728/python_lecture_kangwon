def isMultipleOf3or7(x):
  return ((x%3)==0) or ((x%7)==0)

def getMultiplesOf3or7(n):
  i=2
  j=0
  while(j<10):
    i += 1
    if(isMultipleOf3or7(i)):
      print(i,end=" ")
      j += 1

def getMultiplesOf3or7_(n):
  val=1
  for i in range(n):
    while(not isMultipleOf3or7(val)):
      val += 1
    print(val, end=" ")
    val += 1

getMultiplesOf3or7(10)
print()
getMultiplesOf3or7_(10)