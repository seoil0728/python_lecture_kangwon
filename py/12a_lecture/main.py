s = "Python : 91"
s2 = "Python : 1"

'''
s = {1, 2, 3}
t = {1, 2, 4}
u = {1, 3, 5}
s.update(u)
t |= u
print(s, t, u)
'''





'''
a = [2, 3, 5, 3, 2]
s = set(a)
print("type(a):", type(a))
print("a:", a, end="\n\n")
print("type(s):", type(s))
print("s:", s, end="\n\n")
for i in range(7):
    if (i in s):
        print(i, end=" ")
'''


'''
s1 = set([1,3,2,2,5])
print(s1)

a = ["python", "programming"]
s2 = set(a)
print(s2)

s = set("Good")
print(s)

s3 = { }
print(s3)
'''


'''
s1 = set([1,2,3])
s2 = set([3,2,1])
print(s1 == s2)

a = [2, 3, 5, 3, 2]
print("a:", a)
print("len(a):", len(a))
print()

print("set(a):", set(a))
print("len(set(a)):", len(set(a)))

'''


'''
s = {1, 2, 3, 2, 1}
print(len(s))

s1 = {2,3,5}
s2 = s1.copy()
s2.add(7)
print(s1)
print(s2)

s1.clear()
print(s1, len(s1))

s1 = {2,3,5}
print(0 in s1)
print(3 in s1)
print(0 not in s)

s1.add(7)
print(s, 7 in s)
print()
s.remove(3)
print(s)
print(s)
'''


'''
s = {2, 3, 5}
print(s, 3 in s)
s.discard(3)
print(s, 3 in s)
s.discard(3)
print(s, 3 in s)
print()


'''

'''
print({1,2} <= {1}, {1,2}.issubset({1}))
print({1,2} <= {1,2}, {1,2}.issubset({1,2}))
print({1,2} <= {1,2,3}, {1,2}.issubset({1,2,3}))
print()
print({1,2} >= {1}, {1,2}.issuperset({1}))
print({1,2} >= {1,2}, {1,2}.issuperset({1,2}))
print({1,2} >= {1,2,3}, {1,2}.issuperset({1,2,3}))
print()

print({1,2} | {1}, {1,2}.union({1}))
print({1,2} | {1,3}, {1,2}.union({1,3}))
s1 = {1,2}
s2 = s1 | {1,3}
print(s1, s2)
print()

print({1,2} & {1}, {1,2}.intersection({1}))
print({1,2} & {1,3}, {1,2}.intersection({1,3}))
s1 = {1,2}
s2 = s1 & {1,3}
print(s1, s2)
print()

print({1,2} - {1}, {1,2}.difference({1}))
print({1,2} - {1,3}, {1,2}.difference({1,3}))
s1 = {1,2}
s2 = s1 - {1,3}
print(s1, s2)
'''