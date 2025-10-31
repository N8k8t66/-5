from tkinter import *
import random

size_btn = 150
window = Tk()

list_btn = []
btn_click = []
btn_comp = []

window.geometry(f'{size_btn * 3}x{size_btn * 3 + 100}')
window.title('Крестики-нолики')

class Btn():
    global size_btn, list_btn, btn_click, btn_comp

    def __init__(self, x0, y0, index_btn):
        self.index_btn = index_btn
        self.x0 = x0
        self.y0 = y0

        self.btn = Button(font=('Arial', 100, 'bold'))
        self.btn.place(x=x0, y=y0, width=size_btn, height=size_btn)
        self.start_btn = Button(text='Start', height = 2, width=8, command=self.click_start)
        self.start_btn.place(rely=0.9, relx=0.8)
        self.lbl = Label(text='Для начала игры нажмите старт', height=2, width=30)
        self.lbl.place(relx=0.1, rely=0.9)
        self.wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [1, 4, 7], [0, 3, 6], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    def unbind1(self, event):
        self.btn.unbind('<Button-1>')

    def bind1(self, event):
        self.btn.bind('<Button-1>', self.click)

    def cfg_green(self):
        self.btn.config(bg='green')

    def cfg_white(self):
        self.btn.config(bg='white')

    def check_win(self, lst1):
        self.win = False
        btn_choice = sorted(lst1)
        k = 0
        for i in range(8):
            for j in range(3):
                if self.wins[i][j] in btn_choice:
                    k += 1
            if k == 3:
                self.win = True
                break
            else:
                k = 0
        if self.win:
            for q in list_btn:
                q.unbind1('<Button-1>')
            for w in range(3):
                list_btn[self.wins[i][w]].cfg_green()

    def cfg_o(self, str1):
        self.btn.config(text=str1)

    def game(self):
        while (len(btn_comp) + len(btn_click)) < 9:
            x = random.randint(0, 8)
            if x not in btn_click and x not in btn_comp:
                btn_comp.append(x)
                list_btn[x].cfg_o('0')
                list_btn[x].unbind1('<Button-1>')
                break
        self.check_win(btn_comp)

    def click_start(self):
        global btn_click, btn_comp
        btn_click = []
        btn_comp = []
        for b in list_btn:
            b.btn.config(text='')
            b.btn.bind('<Button-1>', b.click)
            b.cfg_white()
        self.game()

    def click(self, event):
        self.btn.config(text="X")
        btn_click.append(self.index_btn)
        self.check_win(btn_comp)
        self.check_win(btn_click)
        self.btn.unbind('<Button-1>')
        self.game()


def draw():
    index = 0
    x = 0
    y = 0
    for i in range(3):
        for j in range(3):
            list_btn.append(Btn(x, y, index))
            index += 1
            x += size_btn
        x = 0
        y += size_btn

draw()
window.mainloop()
