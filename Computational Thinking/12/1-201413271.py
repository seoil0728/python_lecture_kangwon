from tkinter import *
from tkinter import messagebox


def weight_unit_converter(e):
    unit_table = {
        1: (1000, 'g'),
        2: (35.274, 'oz'),
        3: (15432, 'gr'),
        4: (2.204, 'lb')
    }

    v = var.get()

    try:
        weight = float(m.get())
    except:
        result.config(text='실수형의 숫자만 입력하세요.')
    else:
        rate, units = unit_table.get(v)
        result.config(text='{} {}'.format(weight*rate, units))


print('201413271 김석우')


# 윈도우, 타이틀 생성 및 사이즈 설정
window = Tk()
window.title('무게 단위 변환기')
window.geometry('300x220')
window.resizable(width=FALSE, height=FALSE)

# 변환 단위 선택 라벨
label1 = Label(window, text='변환하려는 단위를 선택하세요.')
label1.pack()

# 라디오 버튼의 변수 준비
var = IntVar()
# 처음 라디오 버튼이 1에 눌릴 수 있도록 설정
var.set(1)

# 라디오 버튼 생성
rb1 = Radiobutton(window, text='gram', variable=var, value=1, command=weight_unit_converter)
rb2 = Radiobutton(window, text='ounce', variable=var, value=2, command=weight_unit_converter)
rb3 = Radiobutton(window, text='grain', variable=var, value=3, command=weight_unit_converter)
rb4 = Radiobutton(window, text='pound', variable=var, value=4, command=weight_unit_converter)

rb1.pack()
rb2.pack()
rb3.pack()
rb4.pack()

# 변환할 무게 입력 안내 라벨
label2 = Label(window, text='변환하려는 무게를 킬로그램(kg) 단위로 입력하세요.')
label2.pack()

# 입력 박스
m = Entry(window)
m.pack()

# 입력 박스에서 엔터를 입력하여 변환
m.bind('<Return>', weight_unit_converter)

# 결과 표시 라벨
result = Label(window, text='', fg='red')
result.pack()

# 종료 버튼
quit_button = Button(window, text='변환기 종료', fg='red', command=quit)
quit_button.pack()

# 윈도우 메인 루프
window.mainloop()
