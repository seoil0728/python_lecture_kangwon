from tkinter import *
from tkinter import messagebox


def myfunc():
    messagebox.showinfo('강아지 버튼', '강아지가 귀엽죠?')


def myfunc2():
    if chk.get() == 0:
        messagebox.showinfo('', '체크박스 해제')
    else:
        messagebox.showinfo('', '체크박스 체크')


def radio():
    if var.get() == 1:
        label4.configure(text='파이썬')
    elif var.get() == 2:
        label4.configure(text='C++')
    else:
        label4.configure(text='Java')


# 윈도우 생성
window = Tk()
window.title('윈도우 창 연습')
window.geometry('400x800')
window.resizable(width=FALSE, height=TRUE)

# 라벨 (텍스트)
label1 = Label(window, text='SWEDU~~ Python을')
label2 = Label(window, text='열심히', font=('궁서체', 30), fg='blue')
label3 = Label(window, text='공부 중입니다.', bg='magenta', width=20, height=5, anchor=SE)

# 버튼
button0 = Button(window, text='메세지 박스', command=myfunc)
button1 = Button(window, text='파이썬 종료', fg='red', command=quit)

# 체크박스
chk = IntVar()
cb1 = Checkbutton(window, text='체크박스', variable=chk, command=myfunc2)

# 라디오버튼튼
var = IntVar()
rb1 = Radiobutton(window, text='파이썬', variable=var, value=1, command=radio)
rb2 = Radiobutton(window, text='C++', variable=var, value=2, command=radio)
rb3 = Radiobutton(window, text='Java', variable=var, value=3, command=radio)

label4 = Label(window, text='선택한 언어 : ', fg='red')

# 리스트를 활용한 패킹
btn_list = []

for i in range(3):
    btn_list.append(Button(window, text='버튼_리스트'))

label1.pack()
label2.pack()
label3.pack()

button0.pack()
button1.pack()

cb1.pack()

rb1.pack()
rb2.pack()
rb3.pack()
label4.pack()

for i in btn_list:
    i.pack(side=TOP, fill=X, padx=30, pady=10)

window.mainloop()
