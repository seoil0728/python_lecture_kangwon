print('201413271 김석우')

while True:
    plain = input('질문 입력 >> ')

    if plain.find('안녕') >= 0:
        print('안녕하세요. 만나서 반가워요.')
    elif plain.find('파이썬') >= 0:
        print('파이썬 프로그램으로 작성되었습니다.')
    elif plain.find('이름') >= 0:
        print('이름은 김석우 입니다.')
    elif plain.find('취미') >= 0:
        print('취미는 기타도 치고 큐브도 하고 이것저것 다양합니다.')
    elif plain.find('학년') >= 0:
        print('현재 대학교 4학년입니다.')
    elif plain.find('날씨') >= 0:
        print('맑거나 구름이 있거나 비가 오거나 안개가 끼거나 눈이 옵니다.')
    elif plain.find('게임') >= 0:
        print('스타크래프트나 롤, 배그 외에도 다양하게 즐깁니다.')
    elif plain.find('전공') >= 0:
        print('전공은 컴퓨터공학입니다.')
    elif plain.find('취업') >= 0:
        print('취업준비는 열심히...')
    elif plain.find('음식') >= 0:
        print('먹는 건 거의 다 좋아해요.')
    else:
        print('질문을 이해하지 못했습니다.')
