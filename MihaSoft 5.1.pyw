## 2022 © Copyright by M. M. Vlasko ##
import tkinter as tk


class ToolTipBase:

    def __init__(self, button):
        self.button = button
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        self._id1 = self.button.bind("<Enter>", self.enter)
        self._id2 = self.button.bind("<Leave>", self.leave)
        self._id3 = self.button.bind("<ButtonPress>", self.leave)

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.button.after(1500, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.button.after_cancel(id)

    def showtip(self):
        if self.tipwindow:
            return
        x = self.button.winfo_rootx() + 20
        y = self.button.winfo_rooty() + self.button.winfo_height() + 1
        self.tipwindow = tw = Toplevel(self.button)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        self.showcontents()

    def showcontents(self, text="Your text here"):
        # Override this in derived class
        label = Label(self.tipwindow, text=text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1)
        label.pack()

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


class ToolTip(ToolTipBase):

    def __init__(self, button, text):
        ToolTipBase.__init__(self, button)
        self.text = text

    def showcontents(self):
        ToolTipBase.showcontents(self, self.text)




def fallout1():
    def returni2():
        rasherec3()
        home()

    def rasherec3():
        lbl0.destroy()
        lbl1.destroy()
        lbl2.destroy()
        lbl3.destroy()
        lbl4.destroy()
        lbl5.destroy()
        lbl6.destroy()
        lbl7.destroy()
        lbl8.destroy()
        txt1.destroy()
        txt2.destroy()
        txt3.destroy()
        txt4.destroy()
        txt5.destroy()
        txt6.destroy()
        but.destroy()
        but1.destroy()
        but3.destroy()
        but4.destroy()
        but5.destroy()
        btn.destroy()
        rad1.destroy()
        rad2.destroy()
        off.destroy()

    def function():
        global m
        m = 0

        a = int(txt1.get())
        b = int(txt2.get())
        c = int(txt3.get())
        d = int(txt4.get())
        e = int(txt5.get())
        f = int(txt6.get())
        if ((a >= 1) and (a <= 31)) and ((b >= 1) and (b <= 12)) and (c > 0) and ((d >= 1) and (d <= 31)) and (
                (e >= 1) and (e <= 12)) and (f > 0) and (f >= c):
            z = e - 1
            g = f - c - 1
            h = 12 - b
            if b != 2:
                if b % 2 == 0:
                    k = 30 - a
                    m = k + d
                    if m >= 30:
                        h += 1
                        m = m - 30
                else:
                    k = 31 - a
                    m = k + d
                    if m >= 31:
                        h += 1
                        m = m - 31
            else:
                if c % 4 == 0:
                    k = 29 - a
                    m = k + d
                    if m >= 19:
                        h += 1
                        m = m - 29
                    else:
                        k = 28 - a
                        m = k + d
                    if m >= 28:
                        h += 1
                        m = m - 28
            x = h + z
            if x >= 12:
                g += 1
                x = x - 12
            if z % 2 == 0:
                m += 1
            l = var.get()
            if l == 1:
                if g == 0:
                    lbl8.configure(text=(g, 'год', x, 'месяцев', m - 1, 'дней.'))
                elif g == 1:
                    lbl8.configure(text=(g, 'год', x, 'месяцев', m - 1, 'дней.'))
                elif (g == 2) or (g == 3) or (g == 4):
                    lbl8.configure(text=(g, 'года', x, 'месяцев', m - 1, 'дней.'))
                else:
                    lbl8.configure(text=(g, 'лет', x, 'месяцев', m - 1, 'дней.'))
            if l == 2:
                lbl8.configure(text=(((365.29 * g) + (x * 30.25) + (m - 2) // 1, 'дней.')))
        else:
            messagebox.showerror('Ошибка!', 'Проверьте правильность ввода!')

    def functionx():
        now = datetime.datetime.now()
        txt4.insert(0, str(now.day))
        txt5.insert(0, str(now.month))
        txt6.insert(0, str(now.year))

    def functiony():
        def sav():
            if os.path.exists('C:/MihaSoft Files/YAO Files') == False:
                os.mkdir('C:/MihaSoft Files/YAO Files')
            a = str(tex.get())
            text_file = open("C:/MihaSoft Files/YAO Files/" + a, "w")
            b = str(txt1.get())
            c = str(txt2.get())
            d = str(txt3.get())
            text_file.write(b + '.' + c + '.' + d + '.' + '*' + '*' + '*' + '*' + '*' + '*' + '*')
            text_file.close()
            wind.destroy()

        def otm():
            wind.destroy()

        wind = Toplevel()
        wind.geometry('250x100+70+70')
        wind.maxsize(250, 100)
        wind.title('Сохранение')

        lol = Label(wind, text='Введите имя...')
        lol.place(x=5, y=5)

        tex = Entry(wind, width=20)
        tex.place(x=5, y=30)

        but2 = Button(wind, text='Сохранить', width=10, height=1, bg="#8ceb8a", fg="black", command=sav)
        but2.place(x=140, y=29)

        but2x = Button(wind, text='Отмена', width=10, height=1, bg="#999999", fg="black", command=otm)
        but2x.place(x=140, y=64)

    def functionz():
        def openz():
            a = os.listdir('C:/MihaSoft Files/YAO Files')
            if a != []:
                b = str(zol1.get())
                fa = open("C:/MihaSoft Files/YAO Files/" + b, "r")
                con = fa.read()
                fa.close()
                print(con)
                x = list(str(con))
                s1 = ''
                s2 = ''
                s3 = ''
                if x[0] != '.' and x[1] != '.':
                    s1 = x[0] + x[1]

                elif x[0] != '.' and x[1] == '.':
                    s1 = x[0]

                if x[1] == '.':
                    if x[3] == '.':
                        s2 = x[2]
                    elif x[4] == '.':
                        s2 = x[2] + x[3]

                elif x[2] == '.':
                    if x[4] == '.':
                        s2 = x[3]
                    elif x[5] == '.':
                        s2 = x[3] + x[4]

                if x[3] == '.':
                    if x[8] == '.':
                        s3 = x[4] + x[5] + x[6] + x[7]
                    elif x[7] == '.':
                        s3 = x[4] + x[5] + x[6]
                    elif x[6] == '.':
                        s3 = x[4] + x[5]
                    elif x[5] == '.':
                        s3 = x[4]

                elif x[4] == '.':
                    if x[9] == '.':
                        s3 = x[5] + x[6] + x[7] + x[8]
                    elif x[8] == '.':
                        s3 = x[5] + x[6] + x[7]
                    elif x[7] == '.':
                        s3 = x[5] + x[6]
                    elif x[6] == '.':
                        s3 = x[5]

                elif x[5] == '.':
                    if x[10] == '.':
                        s3 = x[6] + x[7] + x[8] + x[9]
                    elif x[9] == '.':
                        s3 = x[6] + x[7] + x[8]
                    elif x[8] == '.':
                        s3 = x[6] + x[7]
                    elif x[7] == '.':
                        s3 = x[6]

                txt1.insert(0, s1)
                txt2.insert(0, s2)
                txt3.insert(0, s3)
                wind1.destroy()

        def otm():
            wind1.destroy()

        wind1 = Toplevel()
        wind1.geometry('300x150+70+70')
        wind1.maxsize(300, 150)
        wind1.title('Подставить...')

        lol = Label(wind1, text='Выберите имя...')
        lol.place(x=5, y=5)

        a = os.listdir('C:/MihaSoft Files/YAO Files')

        zol1 = ttk.Combobox(wind1, values=a, font=("Arial Bold", 16), state="readonly")
        zol1.place(x=10, y=50)

        btt1 = Button(wind1, text="Подставить", font=("Arial Bold", 10), fg="black", bg='#7bd491', width=14,
                      command=openz)
        btt1.place(x=10, y=100)

        btt1x = Button(wind1, text="Отмена", font=("Arial Bold", 10), fg="black", bg='#999999', width=14, command=otm)
        btt1x.place(x=150, y=100)

    def functionw():
        def delz():
            a = os.listdir('C:/MihaSoft Files/YAO Files')
            if a != []:
                c = str(zol1.get())
                os.remove('C:/MihaSoft Files/YAO Files/' + c)
                wind2.destroy()

        def otm():
            wind2.destroy()

        wind2 = Toplevel()
        wind2.geometry('300x150+70+70')
        wind2.maxsize(300, 150)
        wind2.title('Удаление записи')

        lix = Label(wind2, text='Выберите запись для удаления...')
        lix.place(x=5, y=5)

        a = os.listdir('C:/MihaSoft Files/YAO Files')

        zol1 = ttk.Combobox(wind2, values=a, font=("Arial Bold", 16), state="readonly")
        zol1.place(x=10, y=50)

        btt1 = Button(wind2, text="Удалить", font=("Arial Bold", 10), fg="black", bg='#eb8a8a', width=14, command=delz)
        btt1.place(x=10, y=100)

        btt1x = Button(wind2, text="Отмена", font=("Arial Bold", 10), fg="black", bg='#999999', width=14, command=otm)
        btt1x.place(x=150, y=100)

    def functionu():
        txt1.delete(0, 'end')
        txt2.delete(0, 'end')
        txt3.delete(0, 'end')
        txt4.delete(0, 'end')
        txt5.delete(0, 'end')
        txt6.delete(0, 'end')

    window.title("YourAgeOnline 3.0")
    window.geometry('650x250+50+50')

    lbl1 = Label(window, text="YourAgeOnline 3.0", font=("Arial Bold", 16), fg="red")
    lbl1.place(x=40, y=20)

    lbl2 = Label(window, text="Дата рождения:", font=("Times New Roman", 12))
    lbl2.place(x=40, y=60)

    txt1 = Entry(window, width=4)
    txt1.place(x=40, y=100)
    ToolTip(txt1, 'День')

    lbl3 = Label(window, text=".", font=("Times New Roman", 12))
    lbl3.place(x=73, y=103)

    txt2 = Entry(window, width=4)
    txt2.place(x=90, y=100)
    ToolTip(txt2, 'Месяц')

    lbl4 = Label(window, text=".", font=("Times New Roman", 12))
    lbl4.place(x=124, y=100)

    txt3 = Entry(window, width=9)
    txt3.place(x=140, y=100)
    ToolTip(txt3, 'Год')

    but = Button(window, text="Подставить т. д.", width=13, height=1, bg="#eef5b3", fg="black", command=functionx)
    but.place(x=250, y=20)
    ToolTip(but, 'Подставить системную дату...')

    but1 = Button(window, text="Сохранить зап.", width=13, height=1, bg="#8ceb8a", fg="black", command=functiony)
    but1.place(x=490, y=120)
    ToolTip(but1, 'Сохранить данные о дате рождения...')

    but3 = Button(window, text="Подставить д. р.", width=13, height=1, bg="#b3f5ec", fg="black", command=functionz)
    but3.place(x=370, y=20)
    ToolTip(but3, 'Подставить сохранённую дату рождения...')

    but4 = Button(window, text="Удалить зап.", width=13, height=1, bg="#eb8a8a", fg="black", command=functionw)
    but4.place(x=490, y=70)
    ToolTip(but4, 'Удалить запись о дате рождения...')

    but5 = Button(window, text="Очичтить", width=13, height=1, bg="#ebd38a", fg="black", command=functionu)
    but5.place(x=490, y=20)
    ToolTip(but5, 'Очистить поля ввода...')

    lbl5 = Label(window, text="Текущая дата:", font=("Times New Roman", 12))
    lbl5.place(x=300, y=60)

    txt4 = Entry(window, width=4)
    txt4.place(x=300, y=100)
    ToolTip(txt4, 'День')

    lbl6 = Label(window, text=".", font=("Times New Roman", 12))
    lbl6.place(x=333, y=100)

    txt5 = Entry(window, width=4)
    txt5.place(x=350, y=100)
    ToolTip(txt5, 'Месяц')

    lbl7 = Label(window, text=".", font=("Times New Roman", 12))
    lbl7.place(x=384, y=100)

    txt6 = Entry(window, width=9)
    txt6.place(x=400, y=100)
    ToolTip(txt6, 'Год')

    var = IntVar()
    rad1 = Radiobutton(window, text="Вывести возраст в годах, месяцах и днях", variable=var, value=1)
    rad1.place(x=40, y=150)

    rad2 = Radiobutton(window, text="Вывести возраст в днях", variable=var, value=2)
    rad2.place(x=300, y=150)

    btn = Button(window, text="РАССЧИТАТЬ", width=19, height=2, bg="black", fg="white", command=function)
    btn.place(x=40, y=190)

    lbl0 = Label(window, text="Ваш возраст: ", font=("Times New Roman", 16))
    lbl0.place(x=220, y=190)

    lbl8 = Label(window, text="", font=("Times New Roman", 16))
    lbl8.place(x=350, y=190)

    off = Button(window, text="⌂", font=("Arial Bold", 15), width=2, height=1, bg="black", fg="white", command=returni2)
    off.place(x=0, y=0)
    ToolTip(off, 'На главную...')


def fallout2():
    def rasherec2():
        lbl1.destroy()
        lbl2.destroy()
        lbl3.destroy()
        lbl4.destroy()
        lbl4x.destroy()
        lbl5.destroy()
        lbl6z.destroy()
        lbl6x.destroy()
        lbl6y.destroy()
        off.destroy()
        eba.destroy()
        huya.destroy()
        btn.destroy()

    def returni1():
        rasherec2()
        home()

    def function():
        flag = 1
        j = 0
        bx = eba.get()
        b = list(map(int, str(bx)))
        for i in range(len(b)):
            if (b[i] != 2) and (b[i] != 3) and (b[i] != 4) and (b[i] != 5):
                b[i] = 0
        while 0 in b:
            b.remove(0)
        cx = huya.get()
        c = list(map(int, str(cx)))
        if c == [0]:
            flag = 0
        for i in range(len(c)):
            if (c[i] != 2) and (c[i] != 3) and (c[i] != 4) and (c[i] != 5) and (c[i] != 0):
                c[i] = 0
        while 0 in c:
            c.remove(0)
        if flag == 0:
            q = sum(b) / len(b)
            lbl4.configure(text=q)
            if (q >= 3.6) and (q <= 4.6):
                lbl5.configure(text=('Можете расслабиться!!!'))
                while sum(b) / len(b) < 4.6:
                    b.append(5)
                    j += 1
                if j == 1:
                    lbl6x.configure(text=('У вас выходит четвёрка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличную оценку до пятёрки в триместре.')
                if (j == 2) or (j == 3) or (j == 4):
                    lbl6x.configure(text=('У вас выходит четвёрка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличные оценки до пятёрки в триместре.')
                if j >= 5:
                    lbl6x.configure(text=('У вас выходит четвёрка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличных оценок до пятёрки в триместре.')
            if (q >= 2.6) and (q < 3.6):
                lbl5.configure(text=('Внимание!!!'))
                while sum(b) / len(b) < 3.6:
                    b.append(5)
                    j += 1
                if j == 1:
                    lbl6x.configure(text=('У вас выходит тройка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличную оценку до четвёрки в триместре.')
                if (j == 2) or (j == 3) or (j == 4):
                    lbl6x.configure(text=('У вас выходит тройка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличные оценки до четвёрки в триместре.')
                if j >= 5:
                    lbl6x.configure(text=('У вас выходит тройка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличных оценок до четвёрки в триместре.')
            if (q >= 2) and (q < 2.6):
                lbl5.configure(text=('Вам пи**ец!!!!'))
                while sum(b) / len(b) < 2.6:
                    b.append(5)
                    j += 1
                if j == 1:
                    lbl6x.configure(text=('У вас выходит ДВОЙКА. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличную оценку до тройки в триместре.')
                if (j == 2) or (j == 3) or (j == 4):
                    lbl6x.configure(text=('У вас выходит ДВОЙКА. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличные оценки до тройки в триместре.')
                if j >= 5:
                    lbl6x.configure(text=('У вас выходит ДВОЙКА. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличных оценок до тройки в триместре.')
            if (q >= 4.6) and (q <= 5):
                lbl6x.configure(text='')
                lbl6y.configure(text='')
                lbl6z.configure(text='')
                lbl5.configure(text=('У вас выходит пятёрка! Не получайте плохих оценок.'))
        if flag != 0:
            z = (sum(c) * 2 + sum(b)) / (len(b) + len(c) * 2)
            lbl4.configure(text=z)
            if (z >= 3.6) and (z <= 4.6):
                lbl5.configure(text=('Можете расслабиться!!!'))
                while (sum(c) * 2 + sum(b)) / (len(b) + len(c) * 2) < 4.6:
                    b.append(5)
                    j += 1
                if j == 1:
                    lbl6x.configure(text=('У вас выходит четвёрка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличную оценку до пятёрки в триместре.')
                if (j == 2) or (j == 3) or (j == 4):
                    lbl6x.configure(text=('У вас выходит четвёрка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличные оценки до пятёрки в триместре.')
                if j >= 5:
                    lbl6x.configure(text=('У вас выходит четвёрка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличных оценок до пятёрки в триместре.')
            if (z >= 2.6) and (z < 3.6):
                lbl5.configure(text=('Внимание!!!'))
                while (sum(c) * 2 + sum(b)) / (len(b) + len(c) * 2) < 3.6:
                    b.append(5)
                j += 1
                if j == 1:
                    lbl6x.configure(text=('У вас выходит тройка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличную оценку до четвёрки в триместре.')
                if (j == 2) or (j == 3) or (j == 4):
                    lbl6x.configure(text=('У вас выходит тройка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличные оценки до четвёрки в триместре.')
                if j >= 5:
                    lbl6x.configure(text=('У вас выходит тройка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличных оценок до четвёрки в триместре.')
            if (z >= 2) and (z < 2.6):
                lbl5.configure(text=('Вам пи**ец!!!!'))
                while (sum(c) * 2 + sum(b)) / (len(b) + len(c) * 2) < 2.6:
                    b.append(5)
                    j += 1
                if j == 1:
                    lbl6x.configure(text=('У вас выходит ДВОЙКА. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличную оценку до тройки в триместре.')
                if (j == 2) or (j == 3) or (j == 4):
                    lbl6x.configure(text=('У вас выходит ДВОЙКА. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличные оценки до тройки в триместре.')
                if j >= 5:
                    lbl6x.configure(text=('У вас выходит ДВОЙКА. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличных оценок до тройки в триместре.')
            if (z >= 4.6) and (z <= 5):
                lbl6x.configure(text='')
                lbl6y.configure(text='')
                lbl6z.configure(text='')
                lbl5.configure(text=('У вас выходит пятёрка! Не получайте плохих оценок!'))

    window.title("MiddleScoreOnline 5.1")
    window.geometry('790x325+50+50')

    lbl1 = Label(window, text="MiddleScoreOnline 5.1", font=("Arial Bold", 16), fg="red")
    lbl1.place(x=40, y=20)

    lbl2 = Label(window, text="Введите оценки без индекса:", font=("Times New Roman", 12))
    lbl2.place(x=40, y=60)
    eba = Entry(window, width=40)
    eba.place(x=40, y=100)

    lbl3 = Label(window, text="Введите оценки с индексом «2»:", font=("Times New Roman", 12))
    lbl3.place(x=40, y=140)
    huya = Entry(window, width=40)
    huya.place(x=40, y=180)
    ToolTip(huya, '5₂')

    btn = Button(window, text="РАССЧИТАТЬ", width=19, height=2, bg="black", fg="white", command=function)
    btn.place(x=40, y=220)

    lbl4x = Label(window, text="Ваш средний балл: ", font=("Times New Roman", 16))
    lbl4x.place(x=290, y=20)

    lbl4 = Label(window, text="", font=("Times New Roman", 16))
    lbl4.place(x=310, y=60)

    lbl5 = Label(window, text="", font=("Times New Roman", 16))
    lbl5.place(x=310, y=100)

    lbl6x = Label(window, text="", font=("Times New Roman", 14))
    lbl6x.place(x=310, y=140)

    lbl6y = Label(window, text="", font=("Times New Roman", 14))
    lbl6y.place(x=310, y=170)

    lbl6z = Label(window, text="", font=("Times New Roman", 14))
    lbl6z.place(x=333, y=170)

    off = Button(window, text="⌂", font=("Arial Bold", 15), width=2, height=1, bg="black", fg="white", command=returni1)
    off.place(x=0, y=0)
    ToolTip(off, 'На главную...')


def fallout3():
    def rasherec4():
        lol.destroy()
        lol1.destroy()
        lol2.destroy()
        lol3.destroy()
        lol4.destroy()
        lol5.destroy()
        lab1.destroy()
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        btn4.destroy()
        off.destroy()
        text.destroy()

    def returni4():
        rasherec4()
        home()

    def f1():
        def x():
            win2 = Toplevel()
            win2.title("Program1")
            win2.geometry('200x100+50+50')
            win2.maxsize(200, 100)
            asd = Label(win2, text="5 + 5 = 10")
            asd.place(x=10, y=30)
            win2.mainloop()

        def g():
            win1.destroy()

        win1 = Toplevel()
        win1.title("Справка")
        win1.geometry('1100x500+50+50')
        win1.maxsize(1100, 500)

        tox = Text(win1, width=135, height=25, font=('Times New Roman', 12))
        tox.place(x=5, y=5)

        tox.insert(1.0, '  The Simplest Mihail’s Language\n')
        tox.insert(2.0, '  _____________\n')
        tox.insert(3.0, '  1 строка - объявление языка: <!DOCTYPE sml>\n')
        tox.insert(4.0, '  _____________\n')
        tox.insert(5.0,
                   '  2 строка - объявление типа: using input; (вводить числа с клавиатуры) или using const; (конкретные числа)\n')
        tox.insert(6.0, '  _____________\n')
        tox.insert(7.0,
                   '  3 строка - если using input;: method=x;, где x это с (сложение), в (вычитание), у (умножение), д (деление), ц (целочисленное деление), д (деление с остатком)\n')
        tox.insert(8.0, '                    если using const;: const1=x;, где x - первое значение\n')
        tox.insert(9.0, '  _____________\n')
        tox.insert(10.0, '  4 строка - если using input;: окончание программы: end;\n')
        tox.insert(11.0, '                  если using const;: const2=y, где y - второе значение\n')
        tox.insert(13.0, '  _____________\n')
        tox.insert(13.0,
                   '  5 строка - если using const;: method=x;, где x это с (сложение), в (вычитание), у (умножение), д (деление), ц (целочисленное деление), д (деление с остатком)\n')
        tox.insert(14.0, '  _____________\n')
        tox.insert(15.0, '  6 строка - если using const;: окончание программы: end;\n')
        tox.insert(16.0, '  _____________\n')
        tox.insert(17.0, '  ПРИМЕР:\n')
        tox.insert(18.0, '  <!DOCTYPE sml>\n')
        tox.insert(19.0, '  using const;\n')
        tox.insert(20.0, '  const1=5;\n')
        tox.insert(21.0, '  const2=5;\n')
        tox.insert(22.0, '  method=с;\n')
        tox.insert(23.0, '  end;')
        tox.configure(state='disabled')

        bt = Button(win1, text="ВЫПОЛНИТЬ", bg="white", fg="black", command=x)
        bt.place(x=13, y=450)

        bt = Button(win1, text="ЗАКРЫТЬ", bg='#e6bebe', fg="black", command=g)
        bt.place(x=1000, y=450)

    def f2():
        lol.configure(text="")
        lol1.configure(text="")
        lol2.configure(text="")
        lol3.configure(text="")
        lol4.configure(text="")
        lol5.configure(text="")

        def ex():
            oy = int(asd1.get())
            ox = int(asd3.get())

            if flag1 == "+":
                ooo = oy + ox
            elif flag1 == "-":
                ooo = oy - ox
            elif flag1 == "*":
                ooo = oy * ox
            elif flag1 == "/":
                ooo = oy / ox
            elif flag1 == "//":
                ooo = oy // ox
            elif flag1 == "%":
                ooo = oy % ox

            asd5.configure(text=ooo)

        if text.get("1.0", "1.14") != "<!DOCTYPE sml>":
            lol.configure(text="Ошибка: линия 1")
        else:
            if (text.get("2.0", "2.12") != "using const;") and (text.get("2.0", "2.12") != "using input;"):
                lol1.configure(text="Ошибка: линия 2")
            else:
                if text.get("2.0", "2.12") == "using const;":
                    if text.get("3.0", "3.7") != "const1=":
                        lol2.configure(text="Ошибка: линия 3")
                    else:
                        if text.get("4.0", "4.7") != "const2=":
                            lol3.configure(text="Ошибка: линия 4")
                        else:
                            ff = int(text.get("3.7"))
                            ff1 = int(text.get("4.7"))
                            if text.get("5.0", "5.7") != "method=":
                                lol4.configure(text="Ошибка: линия 5")
                            else:
                                if text.get("5.7") == "с":
                                    flag = "+"
                                elif text.get("5.7") == "в":
                                    flag = "-"
                                elif text.get("5.7") == "у":
                                    flag = "*"
                                elif text.get("5.7") == "д":
                                    flag = "/"
                                elif text.get("5.7") == "ц":
                                    flag = "//"
                                elif text.get("5.7") == "о":
                                    flag = "%"
                                if text.get("6.0", "6.4") != "end;":
                                    lol5.configure(text="Ошибка: линия 6")
                                else:
                                    win3 = Toplevel()
                                    win3.title("Program1")
                                    win3.geometry('200x100+50+50')
                                    asd1 = Label(win3, text="")
                                    asd1.place(x=10, y=30)
                                    asd1.configure(text=ff)
                                    asd2 = Label(win3, text="")
                                    asd2.place(x=30, y=30)
                                    asd2.configure(text=flag)
                                    asd3 = Label(win3, text="")
                                    asd3.place(x=50, y=30)
                                    asd3.configure(text=ff1)
                                    asd4 = Label(win3, text="=")
                                    asd4.place(x=70, y=30)
                                    asd5 = Label(win3, text="")
                                    asd5.place(x=90, y=30)
                                    if flag == "+":
                                        ooo = ff + ff1
                                    elif flag == "-":
                                        ooo = ff - ff1
                                    elif flag == "*":
                                        ooo = ff * ff1
                                    elif flag == "/":
                                        ooo = ff / ff1
                                    elif flag == "//":
                                        ooo = ff // ff1
                                    elif flag == "%":
                                        ooo = ff % ff1
                                    asd5.configure(text=ooo)
                                    win3.mainloop()

                elif text.get("2.0", "2.12") == "using input;":
                    if text.get("3.0", "3.7") != "method=":
                        lol2.configure(text="Ошибка: линия 3")
                    else:
                        if text.get("4.0", "4.4") != "end;":
                            lol3.configure(text="Ошибка: линия 4")
                        else:
                            if text.get("3.7") == "с":
                                flag1 = "+"
                            elif text.get("3.7") == "в":
                                flag1 = "-"
                            elif text.get("3.7") == "у":
                                flag1 = "*"
                            elif text.get("3.7") == "д":
                                flag1 = "/"
                            elif text.get("3.7") == "ц":
                                flag1 = "//"
                            elif text.get("3.7") == "о":
                                flag1 = "%"
                            win3 = Toplevel()
                            win3.title("Program1")
                            win3.geometry('200x100+50+50')
                            win3.maxsize(200, 100)
                            asd1 = Entry(win3, width=5)
                            asd1.place(x=10, y=30)
                            asd2 = Label(win3, text=flag1)
                            asd2.place(x=30, y=30)
                            asd3 = Entry(win3, width=5)
                            asd3.place(x=50, y=30)
                            asd4 = Label(win3, text="=")
                            asd4.place(x=70, y=30)
                            asd5 = Label(win3, text="")
                            asd5.place(x=90, y=30)
                            btnx = Button(win3, text="ВЫПОЛНИТЬ", command=ex)
                            btnx.place(x=10, y=60)

    def f3():
        def cccc():
            win4.destroy()
            win4.update()

        def ccc():
            text_file = open("program1.miha", "w")
            text_file.write(text.get(1.0, END))
            text_file.close()
            os.replace("program1.miha", "C:\MihaSoft Files\program1.miha")
            win4.destroy()
            win4.update()

        win4 = Toplevel()
        win4.title("Сохранение")
        win4.geometry('350x100+80+80')
        win4.maxsize(350, 100)

        lbl0 = Label(win4, text="Сохранить файл program1.miha на локальном диске C:?")
        lbl0.place(x=5, y=5)

        btni = Button(win4, text="ДА", command=ccc, width=7)
        btni.place(x=105, y=40)

        btnl = Button(win4, text="НЕТ", command=cccc, width=7)
        btnl.place(x=180, y=40)

    def f4():
        text_file = open("C:/MihaSoft Files/program1.miha", "r")
        content = text_file.read()
        text.insert(END, content)
        text_file.close()

    window.title("The Simplest Mihail’s Language - IDE & Compiler")
    window.geometry('810x325+50+50')

    lab1 = Label(window, text="The Simplest Mihail’s Language - IDE & Compiler", font=("Arial Bold", 26), fg="red")
    lab1.place(x=35, y=15)

    btn1 = Button(window, text="Справка", bg="red", fg="white", command=f1)
    btn1.place(x=15, y=70)

    text = Text(window, width=60, height=12)
    text.place(x=15, y=110)
    ToolTip(text, 'Ваш код...')

    btn2 = Button(window, text="ВЫПОЛНИТЬ", bg="green", fg="white", width=15, command=f2)
    btn2.place(x=90, y=70)
    ToolTip(btn2, 'Запустить программу...')

    btn3 = Button(window, text="СОХРАНИТЬ", bg="yellow", fg="black", width=15, command=f3)
    btn3.place(x=220, y=70)
    ToolTip(btn3, 'Сохранить введённый код...')

    btn4 = Button(window, text="ОТКРЫТЬ", bg="grey", fg="black", width=15, command=f4)
    btn4.place(x=350, y=70)
    ToolTip(btn4, 'Подставить сохранённый код...')

    lol = Label(window, text="", fg="red")
    lol.place(x=570, y=110)

    lol1 = Label(window, text="", fg="red")
    lol1.place(x=570, y=120)

    lol2 = Label(window, text="", fg="red")
    lol2.place(x=570, y=130)

    lol3 = Label(window, text="", fg="red")
    lol3.place(x=570, y=140)

    lol4 = Label(window, text="", fg="red")
    lol4.place(x=570, y=150)

    lol5 = Label(window, text="", fg="red")
    lol5.place(x=570, y=160)

    off = Button(window, text="⌂", font=("Arial Bold", 15), width=2, height=1, bg="black", fg="white", command=returni4)
    off.place(x=0, y=0)
    ToolTip(off, 'На главную...')


def fallout4():
    def rasherecx():
        lbl.destroy()
        lbl1.destroy()
        lbl2.destroy()
        lbl3.destroy()
        txt.destroy()
        text.destroy()
        off.destroy()
        but1.destroy()
        but.destroy()
        zk.destroy()
        zt.destroy()

    def returnix():
        rasherecx()
        home()

    def h():
        def lol(to, fromx):
            num = int(txt.get())
            n = int(num, fromx) if isinstance(num, str) else num
            al = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            res = ""
            while n > 0:
                n, m = divmod(n, to)
                res += al[m]
            text.insert(1.0, res[::-1])

        s = int(zk.get())
        b = int(zt.get())
        if b > 45 or s > 45:
            messagebox.showinfo('Ошибка!',
                                'Максимальная для латинского алфавита размерность системы счисления равна 45!')
        else:
            lol(b, a)

    def z():
        text.delete(1.0, END)

    window.geometry('620x430+50+50')
    window.title("TrunsNumSystem 2.0")

    lbl = Label(window, text="TrunsNumSystem 2.0", font=("Arial Bold", 15), fg="red")
    lbl.place(x=40, y=20)

    lbl1 = Label(window, text="Введите значение:")
    lbl1.place(x=20, y=300)

    lbl2 = Label(window, text="ИЗ")
    lbl2.place(x=20, y=80)

    lbl3 = Label(window, text="В")
    lbl3.place(x=20, y=190)

    txt = Entry(window, width=24, font=("Arial Bold", 15))
    txt.place(x=20, y=320)
    ToolTip(txt, 'Только цифры!')

    but = Button(window, text="Перевести", bg="white", fg="black", width=15, command=h)
    but.place(x=340, y=100)

    but1 = Button(window, text="Очистить", bg="red", fg="white", width=15, command=z)
    but1.place(x=470, y=100)
    ToolTip(but1, 'Очистить поле вывода...')

    a = []
    for i in range(2, 46):
        a.append(i)

    zk = ttk.Combobox(window, values=a, font=("Arial Bold", 16))
    zk.place(x=20, y=100)

    zt = ttk.Combobox(window, values=a, font=("Arial Bold", 16))
    zt.place(x=20, y=210)

    text = Text(window, width=30, height=13)
    text.place(x=340, y=130)

    off = Button(window, text="⌂", font=("Arial Bold", 15), width=2, height=1, bg="black", fg="white", command=returnix)
    off.place(x=0, y=0)
    ToolTip(off, 'На главную...')


def fallout5():
    global k, plr_res, plr1, plr2, her, flag1, flag2, flag3, flag4, flag5, flag6, flag7, flag8, flag9, a, s1, s2, zx, q

    def returniz():
        rasherecz()
        home()

    def rasherecz():
        lbl1.destroy()
        lbl2.destroy()
        lbl3.destroy()
        lbl4.destroy()
        lblm.destroy()
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        btn4.destroy()
        cl1.destroy()
        cl2.destroy()
        cl3.destroy()
        cl4.destroy()
        cl5.destroy()
        cl6.destroy()
        cl7.destroy()
        cl8.destroy()
        cl9.destroy()
        off.destroy()

    def param():
        def oncl():
            global plr1, plr2, her
            plr1 = str(ent1.get())
            plr2 = str(ent2.get())
            wind1.destroy()
            wind1.update()
            her = 1

        wind1 = Toplevel()
        wind1.title("Параметры")
        wind1.geometry('300x110+80+80')
        wind1.maxsize(300, 110)

        lblx = Label(wind1, text="Имя первого игрока:")
        lblx.place(x=5, y=5)

        ent1 = Entry(wind1, width=17)
        ent1.place(x=130, y=5)

        lbly = Label(wind1, text="Имя второго игрока:")
        lbly.place(x=5, y=40)

        ent2 = Entry(wind1, width=17)
        ent2.place(x=130, y=40)

        btn2 = Button(wind1, text="ОК", bg='#c0ebd6', width=10, command=oncl)
        btn2.place(x=180, y=70)

    q = True
    a = 3
    her = 0
    flag1 = 3
    flag2 = 3
    flag3 = 3
    flag4 = 3
    flag5 = 3
    flag6 = 3
    flag7 = 3
    flag8 = 3
    flag9 = 3

    def clear():
        global k, flag1, flag2, flag3, flag4, flag5, flag6, flag7, flag8, flag9, q, z
        k = 0
        q = True
        z = False
        lblm.configure(text="1")
        lbl4.configure(text="  ход")
        cl1.configure(text="")
        cl2.configure(text="")
        cl3.configure(text="")
        cl4.configure(text="")
        cl5.configure(text="")
        cl6.configure(text="")
        cl7.configure(text="")
        cl8.configure(text="")
        cl9.configure(text="")
        lbl2.configure(text="")
        lbl3.configure(text="")
        flag1 = 3
        flag2 = 3
        flag3 = 3
        flag4 = 3
        flag5 = 3
        flag6 = 3
        flag7 = 3
        flag8 = 3
        flag9 = 3

    def iniz():

        def zin():
            global flag1, flag2, flag3, flag4, flag5, flag6, flag7, flag8, flag9
            flag1, flag2, flag3, flag4, flag5, flag6, flag7, flag8, flag9 = 0, 0, 0, 0, 0, 0, 0, 0, 0

        def okno():
            def o1():
                clear()
                wind2.destroy()
                wind2.update()

            def o2():
                wind2.destroy()
                wind2.update()

            wind2 = Toplevel()
            wind2.title("Новая игра")
            wind2.geometry('300x110+80+80')
            wind2.maxsize(300, 110)

            lel = Label(wind2, text="Начать новую игру?")
            lel.place(x=95, y=5)

            btnu = Button(wind2, text="ДА", bg='#c0ebd6', width=10, command=o1)
            btnu.place(x=50, y=45)

            btny = Button(wind2, text="НЕТ", bg='#ebc0d0', width=10, command=o2)
            btny.place(x=170, y=45)

        lblm.configure(text=k + 2)
        global plr1, plr2, plr_res, a, q, z
        if ((flag1 == 1 and flag2 == 1 and flag3 == 1) or (flag4 == 1 and flag5 == 1 and flag6 == 1) or (
                flag7 == 1 and flag8 == 1 and flag9 == 1) or (flag1 == 1 and flag4 == 1 and flag7 == 1) or (
                flag2 == 1 and flag5 == 1 and flag8 == 1) or (flag3 == 1 and flag6 == 1 and flag9 == 1) or (
                flag1 == 1 and flag5 == 1 and flag9 == 1) or (flag3 == 1 and flag5 == 1 and flag7 == 1)):
            zin()
            q = False
            z = False
            lbl2.configure(text="Победил")
            a = 1
            if her == 0:
                lbl3.configure(text="Игрок 1")
            else:
                lbl3.configure(text=plr1)
            lblm.configure(text=k + 1)
            lbl4.configure(text="  ходов")
            okno()
            plr_res = plr1
        elif ((flag1 == 0 and flag2 == 0 and flag3 == 0) or (flag4 == 0 and flag5 == 0 and flag6 == 0) or (
                flag7 == 0 and flag8 == 0 and flag9 == 0) or (flag1 == 0 and flag4 == 0 and flag7 == 0) or (
                      flag2 == 0 and flag5 == 0 and flag8 == 0) or (flag3 == 0 and flag6 == 0 and flag9 == 0) or (
                      flag1 == 0 and flag5 == 0 and flag9 == 0) or (flag3 == 0 and flag5 == 0 and flag7 == 0)):
            zin()
            q = False
            z = False
            lbl2.configure(text="Победил")
            a = 2
            if her == 0:
                lbl3.configure(text="Игрок 2")
            else:
                lbl3.configure(text=plr2)
            lblm.configure(text=k + 1)
            lbl4.configure(text="  ходов")
            okno()
            plr_res = plr2
        elif (
                flag1 != 3 and flag2 != 3 and flag3 != 3 and flag4 != 3 and flag5 != 3 and flag6 != 3 and flag7 != 3 and flag8 != 3 and flag9 != 3):
            zin()
            a = 4
            q = False
            z = True
            lbl2.configure(text="НИЧЬЯ!")
            okno()

    def x1():
        global k, flag1
        if flag1 != 1 and flag1 != 0:
            if k % 2 == 0:
                cl1.configure(text="X")
                flag1 = 1
            else:
                cl1.configure(text="O")
                flag1 = 0
            iniz()
            k += 1

    def x2():
        global k, flag2
        if flag2 != 1 and flag2 != 0:
            if k % 2 == 0:
                cl2.configure(text="X")
                flag2 = 1
            else:
                cl2.configure(text="O")
                flag2 = 0
            iniz()
            k += 1

    def x3():
        global k, flag3
        if flag3 != 1 and flag3 != 0:
            if k % 2 == 0:
                cl3.configure(text="X")
                flag3 = 1
            else:
                cl3.configure(text="O")
                flag3 = 0
            iniz()
            k += 1

    def x4():
        global k, flag4
        if flag4 != 1 and flag4 != 0:
            if k % 2 == 0:
                cl4.configure(text="X")
                flag4 = 1
            else:
                cl4.configure(text="O")
                flag4 = 0
            iniz()
            k += 1

    def x5():
        global k, flag5
        if flag5 != 1 and flag5 != 0:
            if k % 2 == 0:
                cl5.configure(text="X")
                flag5 = 1
            else:
                cl5.configure(text="O")
                flag5 = 0
            iniz()
            k += 1

    def x6():
        global k, flag6
        if flag6 != 1 and flag6 != 0:
            if k % 2 == 0:
                cl6.configure(text="X")
                flag6 = 1
            else:
                cl6.configure(text="O")
                flag6 = 0
            iniz()
            k += 1

    def x7():
        global k, flag7
        if flag7 != 1 and flag7 != 0:
            if k % 2 == 0:
                cl7.configure(text="X")
                flag7 = 1
            else:
                cl7.configure(text="O")
                flag7 = 0
            iniz()
            k += 1

    def x8():
        global k, flag8
        if flag8 != 1 and flag8 != 0:
            if k % 2 == 0:
                cl8.configure(text="X")
                flag8 = 1
            else:
                cl8.configure(text="O")
                flag8 = 0
            iniz()
            k += 1

    def x9():
        global k, flag9
        if flag9 != 1 and flag9 != 0:
            if k % 2 == 0:
                cl9.configure(text="X")
                flag9 = 1
            else:
                cl9.configure(text="O")
                flag9 = 0
            iniz()
            k += 1

    def oncla():
        global s2, z
        if q == True:
            messagebox.showwarning('Ошибка!', 'Вы не завершили игру!')
        else:
            def ggg():
                if a == 1 or a == 2 or a == 4:
                    if a == 1 and her == 0:
                        s2 = "Игрок 1"
                    elif a == 2 and her == 0:
                        s2 = "Игрок 2"
                    else:
                        s2 = str(plr_res)
                else:
                    messagebox.showinfo('Ошибка!', 'Нет завершённых игр!')
                s1 = str(k)
                if z == True:
                    zx = 'Ничья ' + " за " + s1 + " ходов. "
                else:
                    zx = "Победил " + s2 + " за " + s1 + " ходов. "
                text_file = open("CrossZeroLog.miha", "w")
                text_file.write(zx)
                text_file.close()
                os.replace("CrossZeroLog.miha", "C:\MihaSoft Files\CrossZeroLog.miha")

            def ol():
                ggg()
                wind4.destroy()
                wind4.update()

            def al():
                wind4.destroy()
                wind4.update()

            wind4 = Toplevel()
            wind4.title("Сохранение")
            wind4.geometry('385x110+80+80')
            wind4.maxsize(385, 110)

            lelx = Label(wind4, text="Сохранить отчёт об игре?")
            lelx.place(x=5, y=5)

            btna = Button(wind4, text="ДА", bg='#c0ebd6', width=10, command=ol)
            btna.place(x=85, y=45)

            btnb = Button(wind4, text="НЕТ", bg='#ebc0d0', width=10, command=al)
            btnb.place(x=205, y=45)

    def onclu():
        def i():
            wind5.destroy()

        wind5 = Toplevel()
        wind5.title("Отчёт")
        wind5.geometry('200x100+80+80')
        wind5.maxsize(300, 150)

        lin = Label(wind5, text="")
        lin.place(x=5, y=5)

        b = Button(wind5, text='OK', command=i)
        b.place(x=15, y=35)

        f = open("C:/MihaSoft Files/CrossZeroLog.miha", "r")
        con = f.readline()
        con = str(con)
        lin.configure(text=con)
        f.close()

    window.geometry('790x600+50+50')
    window.title("CrossZero 2.0")
    plr1 = ""
    plr2 = ""
    plr_res = ""
    k = 0
    lbl1 = Label(window, text="КРЕСТИКИ - НОЛИКИ", font=("Times New Roman", 26), fg="red")
    lbl1.place(x=215, y=10)

    cl1 = Button(window, text="", font=("Times New Roman", 26), fg="red", bg='#b1d4e6', width=7, height=3, command=x1)
    cl1.place(x=170, y=80)

    cl2 = Button(window, text="", font=("Times New Roman", 26), fg="red", bg='#b1d4e6', width=7, height=3, command=x2)
    cl2.place(x=320, y=80)

    cl3 = Button(window, text="", font=("Times New Roman", 26), fg="red", bg='#b1d4e6', width=7, height=3, command=x3)
    cl3.place(x=470, y=80)

    cl4 = Button(window, text="", font=("Times New Roman", 26), fg="red", bg='#b1d4e6', width=7, height=3, command=x4)
    cl4.place(x=170, y=235)

    cl5 = Button(window, text="", font=("Times New Roman", 26), fg="red", bg='#b1d4e6', width=7, height=3, command=x5)
    cl5.place(x=320, y=235)

    cl6 = Button(window, text="", font=("Times New Roman", 26), fg="red", bg='#b1d4e6', width=7, height=3, command=x6)
    cl6.place(x=470, y=235)

    cl7 = Button(window, text="", font=("Times New Roman", 26), fg="red", bg='#b1d4e6', width=7, height=3, command=x7)
    cl7.place(x=170, y=390)

    cl8 = Button(window, text="", font=("Times New Roman", 26), fg="red", bg='#b1d4e6', width=7, height=3, command=x8)
    cl8.place(x=320, y=390)

    cl9 = Button(window, text="", font=("Times New Roman", 26), fg="red", bg='#b1d4e6', width=7, height=3, command=x9)
    cl9.place(x=470, y=390)

    btn1 = Button(window, text="Параметры", font=("Times New Roman", 14), fg="blue", bg='#ddc0eb', command=param)
    btn1.place(x=20, y=80)
    ToolTip(btn1, 'Присвоить игрокам произвольные имена...')

    btn2 = Button(window, text="Новая игра", font=("Times New Roman", 14), fg="blue", bg='#c0ebcb', command=clear)
    btn2.place(x=20, y=160)
    ToolTip(btn2, 'Обновить поле и начать новую игру...')

    btn3 = Button(window, text="Сохранить\n отчёт", font=("Times New Roman", 14), fg="blue", bg='#e0cf92', command=oncla)
    btn3.place(x=20, y=240)
    ToolTip(btn3, 'Сохранить отчёт о последней игре...')

    btn4 = Button(window, text="Открыть\n отчёт", font=("Times New Roman", 14), fg="blue", bg='#87e6ad',
                  command=onclu)
    btn4.place(x=20, y=350)
    ToolTip(btn4, 'Открыть отчёт в новом окне...')

    lbl2 = Label(window, text="", font=("Times New Roman", 20), fg="blue")
    lbl2.place(x=630, y=140)

    lbl3 = Label(window, text="", font=("Times New Roman", 20), fg="blue")
    lbl3.place(x=630, y=200)

    lblm = Label(window, text="1", font=("Times New Roman", 20), fg="blue")
    lblm.place(x=630, y=80)

    lbl4 = Label(window, text="ХОД", font=("Times New Roman", 20), fg="blue")
    lbl4.place(x=670, y=80)

    off = Button(window, text="⌂", font=("Arial Bold", 15), width=2, height=1, bg="black", fg="white", command=returniz)
    off.place(x=0, y=0)
    ToolTip(off, 'На главную...')


def fallout6():
    global zol1, zol, zol2, btt, btt1, btt2

    def returnin():
        window1.destroy()
        window.state('normal')

    def create():
        def click():
            def save():
                a = str(ol.get())
                text_file = open("C:/MihaSoft Files/MihNote Files/" + a + ".miha", "w")
                text_file.write(txt.get(1.0, END))
                text_file.close()
                win2.destroy()
                win2.update()
                win1.destroy()
                win1.update()

            win2 = Toplevel()
            win2.geometry('300x100+90+90')
            win2.maxsize(300, 100)
            win2.title("Сохранение")

            ll1 = Label(win2, text="Введите название файла:")
            ll1.place(x=5, y=5)

            ol = Entry(win2, width=20)
            ol.place(x=10, y=35)

            ll2 = Label(win2, text=".miha")
            ll2.place(x=125, y=35)

            bt = Button(win2, text="Сохранить", font=("Arial Bold", 10), fg="black", bg='#b2e6ae', width=13,
                        command=save)
            bt.place(x=170, y=60)

        win1 = Toplevel()
        win1.geometry('450x400+70+70')
        win1.maxsize(450, 400)
        win1.title("Создание новой заметки")

        but1 = Button(win1, text="Сохранить", font=("Arial Bold", 12), fg="black", bg='#b2e6ae', width=13,
                      command=click)
        but1.place(x=15, y=5)

        txt = Text(win1, width=50, height=15)
        txt.place(x=15, y=50)

    def openx():
        lin.configure(text="")

        def openz():
            a = os.listdir('C:/MihaSoft Files/MihNote Files')
            if a != []:
                b = str(zol1.get())
                zol1.destroy()
                btt1.destroy()
                fa = open("C:/MihaSoft Files/MihNote Files/" + b, "r")
                con = fa.read()
                con = str(con)
                lin.configure(text=con)
                fa.close()

        a = os.listdir('C:/MihaSoft Files/MihNote Files')

        zol1 = ttk.Combobox(window1, values=a, font=("Arial Bold", 16), state="readonly")
        zol1.place(x=20, y=100)

        btt1 = Button(window1, text="Открыть", font=("Arial Bold", 10), fg="black", bg='#7bd491', width=14,
                      command=openz)
        btt1.place(x=300, y=100)

    def delet():
        lin.configure(text="")

        def openo():
            a = os.listdir('C:/MihaSoft Files/MihNote Files')
            if a != []:
                def dele():
                    c = str(zol.get())
                    zol.destroy()
                    btt.destroy()
                    os.remove('C:/MihaSoft Files/MihNote Files/' + c)
                    win3.destroy()
                    win3.update()

                win3 = Toplevel()
                win3.geometry('300x100+90+90')
                win3.maxsize(300, 100)
                win3.title("Удаление")

                l2 = Label(win3, text="Удалить файл?")
                l2.place(x=5, y=5)

                bt = Button(win3, text="ОК", font=("Arial Bold", 10), fg="black", bg='#c97979', width=13, command=dele)
                bt.place(x=170, y=60)

        a = os.listdir('C:/MihaSoft Files/MihNote Files')

        zol = ttk.Combobox(window1, values=a, font=("Arial Bold", 16), state="readonly")
        zol.place(x=20, y=100)

        btt = Button(window1, text="Удалить", font=("Arial Bold", 10), fg="black", bg='#c97979', width=14,
                     command=openo)
        btt.place(x=300, y=100)

    def edit():
        lin.configure(text="")

        def openv():
            a = os.listdir('C:/MihaSoft Files/MihNote Files')
            if a != []:
                def com():
                    fa = open("C:/MihaSoft Files/MihNote Files/" + m, "w")
                    fa.write(txt1.get(1.0, END))
                    fa.close()
                    win4.destroy()
                    win4.update()

                d = os.listdir('C:/MihaSoft Files/MihNote Files')
                if d != []:
                    m = str(zol2.get())
                    zol2.destroy()
                    btt2.destroy()
                    win4 = Toplevel()
                    win4.geometry('450x400+70+70')
                    win4.maxsize(450, 400)
                    win4.title("Редактирование")
                    but0 = Button(win4, text="Сохранить", font=("Arial Bold", 12), fg="black", bg='#b2e6ae', width=13,
                                  command=com)
                    but0.place(x=15, y=5)
                    txt1 = Text(win4, width=50, height=15)
                    txt1.place(x=15, y=50)
                    fa = open("C:/MihaSoft Files/MihNote Files/" + m, "r")
                    content = fa.read()
                    txt1.insert(END, content)
                    fa.close()

        a = os.listdir('C:/MihaSoft Files/MihNote Files')

        zol2 = ttk.Combobox(window1, values=a, font=("Arial Bold", 16), state="readonly")
        zol2.place(x=20, y=100)

        btt2 = Button(window1, text="Редактировать", font=("Arial Bold", 10), fg="black", bg='#79a7c9', width=14,
                      command=openv)
        btt2.place(x=300, y=100)

    if os.path.exists('C:/MihaSoft Files/MihNote Files') == False:
        os.mkdir('C:/MihaSoft Files/MihNote Files')

    window1 = Toplevel()
    window1.geometry('800x700+50+50')
    window1.title("MihNote 1.0")

    lbl = Label(window1, text="MihNote 1.0", font=("Arial Bold", 16), fg="red")
    lbl.place(x=80, y=10)

    btn1 = Button(window1, text="Открыть", font=("Arial Bold", 12), fg="black", bg='#e6aeae', width=13, command=openx)
    btn1.place(x=210, y=10)
    ToolTip(btn1, "Открыть файл...")

    btn2 = Button(window1, text="Редактировать", font=("Arial Bold", 12), fg="black", bg='#aeb4e6', width=13,
                  command=edit)
    btn2.place(x=350, y=10)
    ToolTip(btn2, "Редактировать существующий файл...")

    btn3 = Button(window1, text="Создать", font=("Arial Bold", 12), fg="black", bg='#aee6c9', width=13, command=create)
    btn3.place(x=490, y=10)
    ToolTip(btn3, "Создать новый файл...")

    btn4 = Button(window1, text="Удалить", font=("Arial Bold", 12), fg="black", bg='#e6e2ae', width=13, command=delet)
    btn4.place(x=630, y=10)
    ToolTip(btn4, "Удалить файл...")

    lbl2 = Label(window1,
                 text="__________________________________________________________________________________________________________________________________________________________")
    lbl2.place(x=10, y=60)

    lin = Label(window1, text="", font=("Arial Bold", 16))
    lin.place(x=50, y=90)

    btt2 = Button(window1, text="", font=("Arial Bold", 10), fg="black", bg='#c97979', width=14)

    off = Button(window1, text="⌂", font=("Arial Bold", 15), width=2, height=1, bg="black", fg="white",
                 command=returnin)

    off.place(x=0, y=0)
    ToolTip(off, "На главную...")


def fallout7():
    global flagx, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, dd

    def returnib():
        rasherecb()
        home()

    def rasherecb():
        lbl.destroy()
        lbl1.destroy()
        lbl2.destroy()
        lbl3.destroy()
        lbl4.destroy()
        lbl5.destroy()
        lbl6.destroy()
        lbl8.destroy()
        lbl9.destroy()
        lbl10.destroy()
        lbl11.destroy()
        lbl12.destroy()
        lbl13.destroy()
        lbl14.destroy()
        ent.destroy()
        ent1.destroy()
        ent2.destroy()
        ent3.destroy()
        ent4.destroy()
        ent5.destroy()
        ent6.destroy()
        zt1.destroy()
        zt2.destroy()
        txt.destroy()
        liz.destroy()
        liz1.destroy()
        lol.destroy()
        but1.destroy()
        but2.destroy()
        but3.destroy()
        but4.destroy()
        but5.destroy()
        but6.destroy()
        but7.destroy()
        off.destroy()

    def all():
        global x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, dd
        x1 = str(ent.get())
        x2 = str(ent1.get())
        x3 = str(ent2.get())
        x4 = str(ent3.get())
        x5 = str(ent4.get())
        x6 = str(txt.get("1.0", END))
        x7 = str(zt1.get())
        x8 = str(zt2.get())
        x9 = dd
        x10 = str(ent5.get())
        x11 = str(ent6.get())

    def x():
        global dd
        b = colorchooser.askcolor()
        dd = b[1]
        lol.configure(bg=dd)

    def done():
        global flag, flagx
        all()
        xa = x1 + 'x' + x2 + '+' + x3 + '+' + x4
        if not x1.isdigit() or not x2.isdigit() or not x3.isdigit() or not x4.isdigit() or x5 == '' or x6 == '' or x7 == '' or not x8.isdigit() or x9 == '' or not x10.isdigit() or not x11.isdigit():
            messagebox.showerror('Ошибка!', 'Проверьте корректность введённых данных!')
        else:
            flag = False
            wind = Toplevel()
            wind.geometry(xa)
            wind.title(x5)

            zil = Label(wind, text=x6, font=(x7, x8), fg=x9)
            zil.place(x=x10, y=x11)

    def save():
        def goo():
            global flagx
            os.remove(german)
            np.save(german, a)
            flagx = True
            wind1.destroy()

        def go():
            gf = str(ect.get())
            np.save('C:/MihaSoft Files/WM Files/' + gf, a)
            wind1.destroy()

        global x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, german, flagx, dd
        all()
        a = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11]
        if flagx == False:
            wind1 = Toplevel()
            wind1.geometry('300x100+70+70')
            wind1.maxsize(300, 100)
            wind1.title('Сохранение')

            lcl = Label(wind1, text='Сохранить изменения?')
            lcl.place(x=5, y=5)

            but4 = Button(wind1, text='ОК', width=10, bg='#93e6a8', command=goo)
            but4.place(x=200, y=43)
        else:
            wind1 = Toplevel()
            wind1.geometry('300x100+70+70')
            wind1.maxsize(300, 100)
            wind1.title('Сохранение')

            lcl = Label(wind1, text='Введите название файла...')
            lcl.place(x=5, y=5)

            ect = Entry(wind1, width=25)
            ect.place(x=10, y=45)

            but4 = Button(wind1, text='Сохранить', width=10, bg='#93e6a8', command=go)
            but4.place(x=200, y=43)

    def edit():
        def gg():
            global dd, flagx, german
            ak = str(ect.get())
            ka = np.load('C:/MihaSoft Files/WM Files/' + ak)
            german = 'C:/MihaSoft Files/WM Files/' + ak

            ent.insert(0, ka[0])
            ent1.insert(0, ka[1])
            ent2.insert(0, ka[2])
            ent3.insert(0, ka[3])
            ent4.insert(0, ka[4])
            txt.insert(1.0, ka[5])
            liz.configure(text=ka[6])
            liz1.configure(text=ka[7])
            lol.configure(bg=ka[8])
            ent5.insert(0, ka[9])
            ent6.insert(0, ka[10])
            flagx = False
            wind2.destroy()

        xx = os.listdir('C:/MihaSoft Files/WM Files')
        wind2 = Toplevel()
        wind2.geometry('300x100+70+70')
        wind2.maxsize(300, 100)
        wind2.title('Открыть')

        lcl = Label(wind2, text='Выберите файл...')
        lcl.place(x=5, y=5)

        ect = ttk.Combobox(wind2, values=xx, state='readonly')
        ect.place(x=10, y=45)

        but4 = Button(wind2, text='Редактировать', width=13, bg='#93e6a8', command=gg)
        but4.place(x=180, y=43)

    def op():
        def gg():
            global x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, flagx, dd

            ak = str(ect.get())
            ka = np.load('C:/MihaSoft Files/WM Files/' + ak)

            x1 = ka[0]
            x2 = ka[1]
            x3 = ka[2]
            x4 = ka[3]
            x5 = ka[4]
            x6 = ka[5]
            x7 = ka[6]
            x8 = ka[7]
            dd = ka[8]
            x9 = dd
            x10 = ka[9]
            x11 = ka[10]
            xa = x1 + 'x' + x2 + '+' + x3 + '+' + x4
            if not x1.isdigit() or not x2.isdigit() or not x3.isdigit() or not x4.isdigit() or x5 == '' or x6 == '' or x7 == '' or not x8.isdigit() or x9 == '' or not x10.isdigit() or not x11.isdigit():
                messagebox.showerror('Ошибка!', 'Проверьте корректность введённых данных!')
            else:
                wind = Toplevel()
                wind.geometry(xa)
                wind.title(x5)
                zil = Label(wind, text=x6, font=(x7, x8), fg=x9)
                zil.place(x=x10, y=x11)
            wind2.destroy()

        xx = os.listdir('C:/MihaSoft Files/WM Files')
        wind2 = Toplevel()
        wind2.geometry('300x100+70+70')
        wind2.maxsize(300, 100)
        wind2.title('Открыть')

        lcl = Label(wind2, text='Выберите файл...')
        lcl.place(x=5, y=5)

        ect = ttk.Combobox(wind2, values=xx, state='readonly')
        ect.place(x=10, y=45)

        but4 = Button(wind2, text='Открыть', width=10, bg='#93e6a8', command=gg)
        but4.place(x=200, y=43)

    def opa():
        global flagx

        liz.configure(text='')
        liz1.configure(text='')

        ent.delete(0, 'end')
        ent1.delete(0, 'end')
        ent2.delete(0, 'end')
        ent3.delete(0, 'end')
        ent4.delete(0, 'end')
        ent5.delete(0, 'end')
        ent6.delete(0, 'end')
        txt.delete(1.0, tkinter.END)
        lol.configure(bg='white')
        flagx = True

    def opi():
        def gga():
            ak = str(ect.get())
            os.remove('C:/MihaSoft Files/WM Files/' + ak)
            wind3.destroy()

        xx = os.listdir('C:/MihaSoft Files/WM Files')
        wind3 = Toplevel()
        wind3.geometry('300x100+70+70')
        wind3.maxsize(300, 100)
        wind3.title('Удалить')

        lcl = Label(wind3, text='Выберите файл...')
        lcl.place(x=5, y=5)

        ect = ttk.Combobox(wind3, values=xx, state='readonly')
        ect.place(x=10, y=45)

        buts = Button(wind3, text='Удалить', width=10, bg='#e69b93', command=gga)
        buts.place(x=200, y=43)

    flagx = True
    dd = ''

    if os.path.exists('C:/MihaSoft Files/WM Files') == False:
        os.mkdir('C:/MihaSoft Files/WM Files')

    window.geometry('600x500+50+50')
    window.title('WindowManager 1.1')

    lbl = Label(window, text='WindowManager 1.1', font=('Times New Roman', 20), fg='red')
    lbl.place(x=50, y=5)

    lbl1 = Label(window, text='Размеры окна:', font=('Times New Roman', 12))
    lbl1.place(x=20, y=60)

    ent = Entry(window, width=12)
    ent.place(x=30, y=100)
    ToolTip(ent, 'Ширина')

    lbl2 = Label(window, text='X')
    lbl2.place(x=110, y=100)

    ent1 = Entry(window, width=12)
    ent1.place(x=125, y=100)
    ToolTip(ent1, 'Высота')

    lbl3 = Label(window, text='Расстояние от границ экрана:', font=('Times New Roman', 12))
    lbl3.place(x=20, y=130)

    lbl4 = Label(window, text='X =')
    lbl4.place(x=20, y=170)

    ent2 = Entry(window, width=10)
    ent2.place(x=50, y=170)
    ToolTip(ent2, 'От левой границы')

    lbl5 = Label(window, text='Y =')
    lbl5.place(x=20, y=200)

    ent3 = Entry(window, width=10)
    ent3.place(x=50, y=200)
    ToolTip(ent3, 'От верхней границы')

    lbl6 = Label(window, text='Заголовок:', font=('Times New Roman', 12))
    lbl6.place(x=20, y=230)

    ent4 = Entry(window, width=28)
    ent4.place(x=30, y=260)

    a = list(tkFont.families())
    lbl8 = Label(window, text='Введите текст:', font=('Times New Roman', 12))
    lbl8.place(x=300, y=80)

    txt = Text(window, width=30, height=3)
    txt.place(x=300, y=110)

    lbl9 = Label(window, text='Шрифт текста:', font=('Times New Roman', 12))
    lbl9.place(x=300, y=170)

    zt1 = ttk.Combobox(window, values=a, state='readonly')
    zt1.place(x=300, y=200)

    lbl10 = Label(window, text='Размер шрифта:', font=('Times New Roman', 12))
    lbl10.place(x=300, y=230)

    zt2 = ttk.Combobox(window, values=[8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72])
    zt2.place(x=300, y=260)

    liz = Label(window, text='')
    liz.place(x=460, y=200)

    liz1 = Label(window, text='')
    liz1.place(x=460, y=260)

    lbl11 = Label(window, text='Цвет текста:', font=('Times New Roman', 12))
    lbl11.place(x=300, y=290)

    but1 = Button(window, text='Выбрать', bg="yellow", width=15, command=x)
    but1.place(x=300, y=320)

    lol = Label(window, text='', width=30, height=10)
    lol.place(x=30, y=320)

    lbl12 = Label(window, text='Расположение текста в окне:', font=('Times New Roman', 12))
    lbl12.place(x=300, y=350)

    lbl13 = Label(window, text='X =')
    lbl13.place(x=300, y=380)

    ent5 = Entry(window, width=10)
    ent5.place(x=330, y=380)
    ToolTip(ent5, 'От левой границы')

    lbl14 = Label(window, text='Y =')
    lbl14.place(x=300, y=410)

    ent6 = Entry(window, width=10)
    ent6.place(x=330, y=410)
    ToolTip(ent6, 'От верхней границы')

    but2 = Button(window, text='СОЗДАТЬ', bg="green", fg="white", width=20, font=('Times New Roman', 16), command=done)
    but2.place(x=300, y=440)
    ToolTip(but2, "Созать окно по текущим параметрам...")

    but3 = Button(window, text='Сохранить', bg="#f2ac6b", width=15, command=save)
    but3.place(x=450, y=10)
    ToolTip(but3, "Сохранить текущие параметры...")

    but4 = Button(window, text='Открыть', bg="#f2dc6b", width=15, command=op)
    but4.place(x=300, y=10)
    ToolTip(but4, "Создать окно с сохранёнными параметрами...")

    but5 = Button(window, text='Обновить', bg="#93bbe6", width=15, command=opa)
    but5.place(x=450, y=45)
    ToolTip(but5, "Стереть текущие параметры...")

    but6 = Button(window, text='Удалить', bg="#e69b93", width=15, command=opi)
    but6.place(x=300, y=45)
    ToolTip(but6, "Удалить файл...")

    but7 = Button(window, text='Редактирвать', bg="#90d4cb", width=15, command=edit)
    but7.place(x=150, y=45)
    ToolTip(but7, "Подставить параметры окна для редактирования...")

    off = Button(window, text="⌂", font=("Arial Bold", 15), width=2, height=1, bg="black", fg="white", command=returnib)
    off.place(x=0, y=0)
    ToolTip(off, "На главную...")


def home():
    def germes1():
        rasherec1()
        fallout1()

    def germes2():
        rasherec1()
        fallout2()

    def germes3():
        rasherec1()
        fallout3()

    def germes4():
        rasherec1()
        fallout4()

    def germes5():
        rasherec1()
        fallout5()

    def germes6():
        window.wm_state('iconic')
        fallout6()

    def germes7():
        rasherec1()
        fallout7()

    def rasherec1():
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        r5.destroy()
        r6.destroy()
        r7.destroy()
        x.destroy()
        r8.destroy()

    window.title("MihaSoft 5.1")
    window.geometry('790x870+50+50')

    r1 = Label(window, text="Ⓜ", font=("Arial Bold", 350), fg="red")
    r1.place(x=150, y=5)

    x = Label(window, width=90, height=22, bg='#e0b6b6')
    x.place(x=70, y=500)

    r2 = Button(window, text="YourAgeOnline", font=("Arial Bold", 15), width=25, height=2, bg="#0039A6", fg="white",
                command=germes1)
    r2.place(x=90, y=680)

    r3 = Button(window, text="MiddleScoreOnline", font=("Arial Bold", 15), width=25, height=2, bg="#FF0000",
                fg="white", command=germes2)
    r3.place(x=400, y=680)

    r4 = Button(window, text="The SML - IDE & Compiler", font=("Arial Bold", 15), width=25, height=2, bg="#D52B1E",
                fg="white", command=germes3)
    r4.place(x=90, y=760)

    r5 = Button(window, text="TrunsNumSystem", font=("Arial Bold", 15), width=25, height=2, bg='#FFDF00',
                fg="black", command=germes4)
    r5.place(x=400, y=760)

    r6 = Button(window, text="CrossZero", font=("Arial Bold", 15), width=25, height=2, bg='#FFFFFF',
                fg="black", command=germes5)
    r6.place(x=90, y=600)

    r7 = Button(window, text="MihNote", font=("Arial Bold", 15), width=25, height=2, bg='#FFFFFF',
                fg="black", command=germes6)
    r7.place(x=400, y=600)

    r8 = Button(window, text="WindowManager", font=("Arial Bold", 15), width=25, height=2, bg='#93e6a1',
                fg="black", command=germes7)
    r8.place(x=245, y=510)


import os
from tkinter import ttk
from tkinter import messagebox
import datetime
from tkinter import *
from tkinter import colorchooser
import tkinter.font as tkFont
import numpy as np
import tkinter
from tkinter.ttk import Radiobutton


window = Tk()


def ola():
    window.quit()

def ala():
    os.mkdir('C:/MihaSoft Files')
    lbli.destroy()
    btn1.destroy()
    btn2.destroy()
    home()


if os.path.exists('C:/MihaSoft Files') == False:
    window.geometry('470x100+50+50')
    window.title('Добро пожаловать!')
    lbli = Label(window,
                 text='Вас приветствют разработчики MihaSoft! Для корректного продолжения работы\n программы необходимо разрешение на создание системных папок на диске C:')
    lbli.place(x=5, y=5)
    btn1 = Button(window, text='РАЗРЕШИТЬ', font=('Times New Roman', 10), width=13, command=ala)
    btn1.place(x=230, y=50)
    ToolTip(btn1, 'На диске C: будет создана папка MihaSoft Files, в которой будут размещаться новые папки и файлы, создаваемые в процессе работы программы')
    btn2 = Button(window, text='ОТМЕНА', font=('Times New Roman', 10), width=13, command=ola)
    btn2.place(x=350, y=50)

else:
    home()


window.mainloop()
