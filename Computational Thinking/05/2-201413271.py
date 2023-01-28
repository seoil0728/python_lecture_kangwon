import random

print('201413271 김석우')

number = random.randrange(100)
print('1부터 100까지 수를 맞추는 게임 입니다.')
while True:
    a = int(input('수를 입력하세요. : '))
    if number > a:
        print('Up!')
    elif number < a:
        print('Down!')
    else:
        print('정답입니다.')
        break
