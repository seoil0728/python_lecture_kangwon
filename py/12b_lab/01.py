def readFile(path):
    with open(path,"r") as f:
        return f.read()

def Chk_same_score():
    strs = readFile("P_score.txt")
    d = strs.split("\n")
    i=0
    ca = []

    while i < len(d):
        ca.append(d[i])
        i += 1
        ca.append(d[i:i+100])
        i += 100

    # 최대 동점자 수 찾기

    i = 1
    while(i < len(ca)-2):
        cs = set(ca[i])
        max = 0
        strs = ""
        for ia in cs:
            count = ca[i].count(ia)
            if max < count:
                max = count
                strs = ia[8:]
        print(ca[i-1] + "의 최대 동점자는 " + str(max) + "명 입니다. 점수 : " + strs)
        i += 2


    # 점수 분포표 만들기


    mi = 1
    while mi < len(ca)-2:
        cali = []
        for i in ca[mi]:
            cali.append(int(i[8:]))
        css = set(cali)
        li = list(css)
        li.sort()
        li.reverse()
        print(ca[mi-1] + "차")
        for i in li:
            print(str(i) + " : " + str(cali.count(i)))
        mi += 2



Chk_same_score()


'''
cali = []
    for i in ca[1]:
        cali.append(int(i[8:]))
    css = set(cali)
    li = list(css)
    li.sort()
    li.reverse()
    print(li)
    print(ca[1 - 1] + "차")
    for i in li:
        print(str(i) + " : " + str(cali.count(i)))

'''