import matplotlib.pyplot as plt
import csv

f = open('교통사고통계.csv', 'r')
data = csv.reader(f)

# 제목 행 건너뛰기
next(data)

# 데이터 저장
x = []
y = []
z = []
for row in data:
    x.append(row[0])
    y.append(int(row[1]))
    z.append(int(row[2]))

f.close()

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize=(12, 5), facecolor='#C5C2FF')
plt.plot(x, y, label='accident', color='red')
plt.plot(x, z, label='death', color='blue')
plt.legend()
plt.grid()
plt.xlabel('Year')
plt.ylabel('Number of accidents')
plt.title('연도별 교통사고 통계 (201413271 김석우)')
plt.show()
