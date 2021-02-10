import copy
a = [3, -2, -3, 5, -5, 7, 11, -11]
b = copy.copy(a)

b.sort(key=abs)
print(a)
print("A = ", a.sort(key=abs))
