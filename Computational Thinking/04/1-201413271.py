print('201413271 김석우')

year = int(input('년도 입력 : '))

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print('{}년은 윤년입니다.'.format(year))
else:
    print('{}년은 윤년이 아닙니다.'.format(year))

if year % 4 == 0 and year <= 2020:
    print('{}년은 올림픽이 열리는 해 입니다.'.format(year))
if year % 4 == 2 and year <= 2018:
    print('{}년은 월드컵이 열리는 해 입니다.'.format(year))
