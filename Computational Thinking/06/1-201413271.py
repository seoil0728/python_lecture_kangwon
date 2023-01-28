print('201413271 김석우')

menus = {'김치찌개': 6500, '부대찌개': 8000, '순대국': 7000, '제육볶음': 9000}

print('주문 가능한 메뉴 : {}'.format(list(menus.keys())))
total = 0

while True:
    sel = input('메뉴 입력(주문 완료는 0, 메뉴 취소는 1) : ')
    if sel == '김치찌개':
        print('김치찌개 = 6,500원')
        total += menus.get(sel)
    elif sel == '부대찌개':
        print('부대찌개 = 8,000원')
        total += menus.get(sel)
    elif sel == '순대국':
        print('순대국 = 7,000원')
        total += menus.get(sel)
    elif sel == '제육볶음':
        print('제육볶음 = 9,000원')
        total += menus.get(sel)
    elif sel == '0':
        break
    elif sel == '1':
        print('주문이 취소되었습니다. 다시 주문해주세요')
        total = 0
    else:
        print('없는 메뉴입니다.')

print('주문이 완료되었습니다.')
print('주문 금액은 {:,}원 입니다.'.format(total))
