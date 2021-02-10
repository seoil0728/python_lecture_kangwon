def readFile(path):
    with open(path,"r") as f:
        return f.read()

def concordance(a):
    at = a.replace(",", "").replace(". ", "").replace("!", "").replace(".", "")
    t = at.split("\n")


    ts = []
    for i in t:
        ts.append(i.split(" "))

    di = dict()
    count = 0
    ln = 1
    while True:
        for i in ts:
            for j in i:
                if j in di:
                    di.get(j).append(ln)
                else:
                    cli = []
                    di[j] = cli
                    cli.append(ln)
            ln += 1
        count += 1
        if count < len(ts):
            break


    for i in di.items():
        print(i)
    print()

def sortConcordance(a):
    at = a.replace(",", "").replace(". ", "").replace("!", "").replace(".", "")
    t = at.split("\n")

    ts = []
    for i in t:
        ts.append(i.split(" "))

    di = dict()
    count = 0
    ln = 1
    while True:
        for i in ts:
            for j in i:
                if j in di:
                    di.get(j).append(ln)
                else:
                    cli = []
                    di[j] = cli
                    cli.append(ln)
            ln += 1
        count += 1
        if count < len(ts):
            break
    dis = sorted(di.items())
    for key, value in dis:
        print(key, " : ", value)

s = readFile("aboutKNU2.txt")

def concordance2(a):
    at = a.replace(",", "").replace(". ", "").replace("!", "").replace(".", "")
    t = at.split("\n")

    ts = []
    for i in t:
        ts.append(i.split(" "))

    di = dict()
    count = 0
    ln = 1
    while True:
        for i in ts:
            for j in i:
                if j in di:
                    if ln not in di.get(j):
                        di.get(j).append(ln)
                else:
                    cli = []
                    di[j] = cli
                    cli.append(ln)
            ln += 1
        count += 1
        if count < len(ts):
            break
    dis = sorted(di.items())
    for key, value in dis:
        print(key, " : ", value)


concordance(s)
print()
print("알파벳 순 정렬")
sortConcordance(s)
print()
print("중복 제거")
concordance2(s)