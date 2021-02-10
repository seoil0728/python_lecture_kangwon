import copy
row = 3
col = 4
a = [[0]*col]*row
b = copy.deepcopy(a)

print("a =", a)
print("b =", b)
print("----------------")

a[0][0] = "a"
b[0][0] = "b"
print("a =", a)
print("b =", b)