import sqlite3
import matplotlib.pyplot as plt
import csv

# con = sqlite3.connect('naverDB')
# cur = con.cursor()
#
# cur.execute('CREATE TABLE userTable (id char(4), userName char(15), email char(15), birthYear int)')
# cur.execute("INSERT INTO userTable VALUES('john', 'John Bann', 'john@naver.com', 1990)")
# cur.execute("INSERT INTO userTable VALUES('kim', 'Kim Chi', 'kim@naver.com', 1992)")
# cur.execute("INSERT INTO userTable VALUES('lee', 'Lee Nal', 'lee@naver.com', 1988)")
# cur.execute("INSERT INTO userTable VALUES('park', 'Park Sa', 'park@naver.com', 1993)")
# cur.execute("INSERT INTO userTable VALUES('soma', 'Sang Hyeon', 'soma@naver.com', 1995)")
#
# con.commit()
# con.close()

# x = ['choi', 'han', 'jung', 'kim', 'lee']
# y = [93, 67, 90, 78, 80]
#
# plt.scatter(x, y)
# plt.show()
#

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
plt.figure(figsize=(12, 5), facecolor='lightyellow')
plt.plot(x, y, label='accident', color='red')
plt.plot(x, z, label='death', color='blue')
plt.legend()
plt.grid()
plt.xlabel('Year')
plt.ylabel('Number of accidents')
plt.title('연도별 교통사고 통계 (201413271 김석우)')
plt.show()
