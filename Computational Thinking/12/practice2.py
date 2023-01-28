from tkinter import *
from tkinter import messagebox


def click_left(event):
    messagebox.showinfo('윈도우', '마우스 왼쪽 클릭')


def click_right(event):
    messagebox.showinfo('윈도우', '마우스 오른쪽 클릭')


def label_click_left(event):
    messagebox.showinfo('라벨', '마우스 왼쪽 클릭')


def label_click_right(event):
    messagebox.showinfo('라벨', '마우스 오른쪽 클릭')


def click_mouse(event):
    txt = ''
    if event.num == 1:
        txt += '마우스 왼쪽 버튼 클릭, 좌표 (x,y): '
    elif event.num == 3:
        txt += '마우스 오른쪽 버튼 클릭, 좌표 (x,y): '

    txt += str(event.x) + ',' + str(event.y)
    label2.configure(text=txt)


def key_event(event):
    messagebox.showinfo('키보드 이벤트', '눌린 키 : ' + chr(event.keycode))

# 윈도우 생성
window = Tk()
window.title('윈도우 창 연습')
window.geometry('400x400')
window.resizable(width=FALSE, height=TRUE)

# 마우스 이벤트
# window.bind('<Button-1>', click_left)
# window.bind('<Button-3>', click_right)


# 라벨 등에도 적용 가능
label1 = Label(window, text='라벨1')

label1.bind('<Button-1>', label_click_left)
label1.bind('<Button-3>', label_click_right)


# 마우스 클릭 좌표 표시
label2 = Label(window, text='좌표 인식')
window.bind('<Button>', click_mouse)

label1.pack()
label2.pack(expand=1, anchor=CENTER)


# 키보드 이벤트
window.bind("<Key>", key_event)


window.mainloop()
