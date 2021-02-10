def printRightAngledTri(n):
  for i in range(n):
    for j in range(i+1):
      print("*", end="")
    print()

printRightAngledTri(4)