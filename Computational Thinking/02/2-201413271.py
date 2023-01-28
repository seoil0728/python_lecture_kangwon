import calendar

print('201413271 김석우')

year = int(input('태어난 연도를 입력해주세요. : '))
month = int(input('태어난 월을 입력해주세요. : '))

print(year, '년', month, '월의 달력은 다음과 같습니다.')
calendar.prmonth(year, month)
