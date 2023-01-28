print('201413271 김석우')

a = int(input('첫 번째 수를 입력하세요. : '))
b = int(input('두 번째 수를 입력하세요. : '))

lcm = 0

while True:
    lcm += 1
    if lcm % a == 0 and lcm % b == 0:
        break

print(lcm)
