
def readFile(path):
    with open(path,"r") as f:
        return f.read()


def read_data():
    s = readFile("score.txt")
    d = s.split("\n")
    d.sort()
    student = []
    for i in range(len(d)):          # 재조합해서 [학번 [과목 점수]] 형태로 만듬
        std = d[i].split(", ")
        std[0] = int(std[0])
        std[2] = int(std[2])
        student += [std[0],[std[1],std[2]]]

    rea = len(student)
    rei = 0
    count = 0
    while (rei < rea):          # 중복된 학번을 제거하는 작업
        if (count == 0):
            rei += 2
        elif(count == 1):
            student.pop(rei)
            rea -= 1
            rei += 1
        else:
            student.pop(rei)
            rea -= 1
            rei += 1
        count += 1
        if(count == 3):
            count = 0
    res = []
    fi = 0
    while(fi < len(student)):        # 최종적으로 리스트들을 모아주어 리턴
        res.append(student[fi:fi+4])
        fi+=4


    return res

# 학번을 입력할 시 각 과목별 점수와 평균, 최대,최소점수를 출력한다.
def sortByID(std):
    sortID = int(input("Input your Student ID : "))
    for i in range(len(std)):
        if(std[i][0] == sortID):
            avg = (std[i][1][1] + std[i][2][1] + std[i][3][1])/3
            max = returnMax(std[i])  # 최대, 최솟값 구하는 함수를 따로 만들어 계산
            min = returnMin(std[i])
            print(std[i][1][0] + " : " + str(std[i][1][1]))
            print(std[i][2][0] + " : " + str(std[i][2][1]))
            print(std[i][3][0] + " : " + str(std[i][3][1]))
            print("Average : " + str(round(avg, 2)) + ", Max : " + str(max) + ", Min : " + str(min))

# 과목과 점수를 입력하여 해당 과목의 점수 이상인 학번을 출력
def showPassStudent(std):
    subj = input("Input the subject : ")
    minScore = int(input("Min Score : "))
    strs = ""
    if(subj == "English"):
        rea = 1
    elif(subj == "Math"):
        rea = 2
    elif(subj == "Science"):
        rea = 3
    else:
        rea = 0
    if(rea == 0):           # 과목 이름이 정확하지 않을 경우 에러 메세지 프린트
        print(subj + " is not allowed subject")
    else:                   # rea = 과목 이름에 맞게 부여한 번호.
        for i in range(len(std)):
            if(std[i][rea][1] >= minScore):
                strs += str(std[i][0]) + ", "
        strs = strs[:len(strs)-2]   # 맨 마지막 붙는 ", " 를 제거한다.
        print("Student ID who gets over " + str(minScore) + " in " + std[0][rea][0] + " : " + strs)

# 히스토그램 출력 함수
def showHistogram(std):
    subj = input("Input the subject : ")
    if (subj == "English"):             # 기본 구조는 showPassStudent 함수와 동일
        rea = 1
    elif (subj == "Math"):
        rea = 2
    elif (subj == "Science"):
        rea = 3
    else:
        rea = 0
    if (rea == 0):
        print(subj + " is not allowed subject")
    else:
        print("histogram for " + subj)
        print()
        n = 0   # 90점 이상 카운트
        m = 0   # 80이상 90미만 카운트
        v = 0   # 80미만 카운트
        for i in range(len(std)):
            if(std[i][rea][1] >= 90):
                n += 1
            elif(std[i][rea][1] >= 80):
                m += 1
            else:
                v += 1
        for i in range(8,0,-1):     # 해당 항목 전체에서 최대치가 8개여서 임의로 8부터 시작 1씩 감소
            if(n >= i):             # 현재 줄 번호가 카운트보다 큰 경우 별 출력
                print("    *    ", end="")
            else:                   # 그렇지 않다면 빈 공간 출력
                print("         ", end="")
            if (m >= i):
                print("    *    ", end="")
            else:
                print("         ", end="")
            if (v >= i):
                print("    *    ", end="")
            else:
                print("         ", end="")
            print()
        print("---------------------------------")
        print("  90-100   80-90    70-80  ")


# 점수 최댓값을 구하는 함수
def returnMax(stdsli):
    max = stdsli[1][1]
    if (max < stdsli[2][1]):
        max = stdsli[2][1]
    if (max < stdsli[3][1]):
        max = stdsli[3][1]
    return max

# 점수 최솟값을 구하는 함수
def returnMin(stdsli):
    min = stdsli[1][1]
    if (min > stdsli[2][1]):
        min = stdsli[2][1]
    if (min > stdsli[3][1]):
        min = stdsli[3][1]
    return min

stds = read_data()
sortByID(stds)
showPassStudent(stds)
showHistogram(stds)
'''
    for i in range(len(res)):
        print(res[i])
[2,4],[8,10],[14,16]
i = 0 skip
i += 2
pop
i += 1
pop
i += 1 skip
i += 2
pop
i += 1
pop
i += 1 skip

'''