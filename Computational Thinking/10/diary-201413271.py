import datetime

print('201413271 김석우')

print('종료는 \' /종료 \'를 입력하세요.')
with open('diary.txt', 'a', encoding='UTF-8') as f:
    while True:
        text = input('내용을 입력하세요. : ')
        date_now = '[' + str(datetime.datetime.now()) + ']'
        if text == '/종료':
            break
        else:
            print(date_now, text)
            f.write(date_now + ' ' + text + '\n')
        print()
