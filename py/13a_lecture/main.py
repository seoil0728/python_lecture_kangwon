a = "Founded"
b = [1,1]

d1 = dict()
d1[a] = b
print(d1)

'''
d1 = { 1:"Albert", 2:"Cathy" }
d2 = { 2:"John", 3:"Simon" }
d1.update(d2)
print("d1 =", d1)
print("d2 =", d2)
'''



'''
carDic = { "brand": "Food", "model": "Mustang", "year": 1964}

print(carDic)
print(carDic["model"])
print(carDic["year"])

scores = [("math",100),("physics",99),("history",70)]
d = dict(scores)
print(d)

'''


'''
employee = dict()
key = "Albert"
info = 20200001, "male"
employee[key] = info

key = "Cathy"
info = 20200002, "female"
employee[key] = info

print(employee)
print("Albert's id :", employee["Albert"][0])
print("Cathy's gender :", employee["Cathy"][1])
'''


'''
d = dict()
d["Albert"] = 3
d["Albert"] = 2
d["Albert"] = 1
print(d)

d = dict()
a = [1]
d[a] = 42   # Error
'''


'''
d = {"Albert": 100, "Cathy":90, "Brown":80}
print("d :", d)
print()
print("keys in d :", d.keys())
print()
print("keys : ", end="")
for i in d.keys():
    print(i, end=" ")
print("\n")
print("items : ", end="")
for i in d.items():
    print(i, end=" ")
print("\n")
print("values : ", end="")
for i in d.values():
    print(i, end=" ")
'''


'''
d = {"Albert": 100, "Cathy":90, "Brown":80}
print("keys in d :", d.keys())
print("\n * keys in list")
keys_list1 = [*d]
print(keys_list1)
keys_list2 = list(d)
print(keys_list2)
keys_list3 = list(d.keys())
print(keys_list3)

print("\n * keys in tuple")
keys_tuple1 = tuple(d)
print(keys_tuple1)
keys_tuple2 = tuple(d.keys())
print(keys_tuple1)
'''


'''
d = {"Albert": 100, "Cathy":90, "Brown":80}
print("d :", d)
print("keys in d :", d.keys())
for val in d.keys():
    print("d[%s]: %d " % (val, d[val]))
print()
for val in d.items():
    print("d[%s]: %d " % (val[0], val[1]))
'''


'''
d = { 1: [1,2,3,4,5], 2:"abcd"}
print(len(d))

d1 = { 1:"Albert" }
d2 = d1.copy()
d1[2] = "Cathy"
print(d1)
print(d2)

d.clear()
print(d, len(d))
'''


'''
d = { 1:"Albert", 2:"Cathy" }
print(d.get(1))
print(d.get(1) == d[1])
print(d.get(0))
print(d)
'''


'''
d = { 1:"Albert", 2:"Cathy" }
print(1 in d)
del d[1]
print(1 in d)
print("d[2]:", d[2])
print("d[1]:", d[1])
'''