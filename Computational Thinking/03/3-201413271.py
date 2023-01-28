print('201413271 김석우')

a = int(input('첫 번째 수를 입력하세요. : '))
b = int(input('두 번째 수를 입력하세요. : '))
c = int(input('세 번째 수를 입력하세요. : '))


print('{}은(는) {}, {}의 공배수인가? {}'.format(c, a, b, (c % a == 0) and (c % b == 0)))

