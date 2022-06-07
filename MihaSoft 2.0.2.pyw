## 2022 © Copyright by M. M. Vlasko ##

def fallout1():
    from tkinter.ttk import Radiobutton
    from tkinter import messagebox
    l = 2

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
        btn.destroy()
        rad1.destroy()
        rad2.destroy()
        off.destroy()

    def function():
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
                    lbl8.configure(text=(g, 'лет', x, 'месяцев', m, 'дней.'))
            if l == 2:
                lbl8.configure(text=(((365.29 * g) + (x * 30.25) + m) // 1, 'дней.'))
        else:
            messagebox.showerror('Ошибка!', 'Проверьте правильность ввода!')

    window.title("YourAgeOnline 2.0")
    window.geometry('650x650+600+200')

    lbl1 = Label(window, text="YourAgeOnline 2.0", font=("Arial Bold", 16), fg="red")
    lbl1.place(x=40, y=20)

    lbl2 = Label(window, text="Введите дату вашего рождения:", font=("Times New Roman", 12))
    lbl2.place(x=40, y=60)
    txt1 = Entry(window, width=20)
    txt1.place(x=40, y=100)

    lbl3 = Label(window, text="Введите месяц вашего рождения:", font=("Times New Roman", 12))
    lbl3.place(x=40, y=140)
    txt2 = Entry(window, width=20)
    txt2.place(x=40, y=180)

    lbl4 = Label(window, text="Введите год вашего рождения:", font=("Times New Roman", 12))
    lbl4.place(x=40, y=220)
    txt3 = Entry(window, width=20)
    txt3.place(x=40, y=260)

    lbl5 = Label(window, text="Введите текущую дату:", font=("Times New Roman", 12))
    lbl5.place(x=40, y=300)
    txt4 = Entry(window, width=20)
    txt4.place(x=40, y=340)

    lbl6 = Label(window, text="Введите текущий месяц:", font=("Times New Roman", 12))
    lbl6.place(x=40, y=380)
    txt5 = Entry(window, width=20)
    txt5.place(x=40, y=420)

    lbl7 = Label(window, text="Введите текущий год:", font=("Times New Roman", 12))
    lbl7.place(x=40, y=460)
    txt6 = Entry(window, width=20)
    txt6.place(x=40, y=500)

    var = IntVar()
    rad1 = Radiobutton(window, text="Вывести возраст в годах, месяцах и днях", variable=var, value=1)
    rad1.place(x=40, y=540)
    rad2 = Radiobutton(window, text="Вывести возраст в днях", variable=var, value=2)
    rad2.place(x=300, y=540)

    btn = Button(window, text="РАССЧИТАТЬ", width=19, height=2, bg="black", fg="white", command=function)
    btn.place(x=40, y=580)

    lbl0 = Label(window, text="Ваш возраст: ", font=("Times New Roman", 16))
    lbl0.place(x=220, y=580)
    lbl8 = Label(window, text="", font=("Times New Roman", 16))
    lbl8.place(x=350, y=580)

    off = Button(window, text="⌂", font=("Arial Bold", 15), width=2, height=1, bg="black", fg="white", command=returni2)
    off.place(x=0, y=0)


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
        print(b)
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
                lbl5.configure(text=('У вас выходит пятёрка! Не получайте плохих оценок!'))

    window.title("MiddleScoreOnline 5.0")
    window.geometry('790x325+600+300')

    lbl1 = Label(window, text="MiddleScoreOnline 5.0", font=("Arial Bold", 16), fg="red")
    lbl1.place(x=40, y=20)

    lbl2 = Label(window, text="Введите оценки без индекса:", font=("Times New Roman", 12))
    lbl2.place(x=40, y=60)
    eba = Entry(window, width=40)
    eba.place(x=40, y=100)

    lbl3 = Label(window, text="Введите оценки с индексом «2»:", font=("Times New Roman", 12))
    lbl3.place(x=40, y=140)
    huya = Entry(window, width=40)
    huya.place(x=40, y=180)

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
            win2.geometry('200x100')
            asd = Label(win2, text="5 + 5 = 10")
            asd.place(x=0, y=0)
            win2.mainloop()

        win1 = Toplevel()
        win1.title("Справка")
        win1.geometry('900x500')

        ll = Label(win1, text="The Simplest Mihail’s Language")
        ll.place(x=5, y=5)

        ll1 = Label(win1, text="1 строка - объявление языка: <!DOCTYPE sml>")
        ll1.place(x=5, y=30)

        ll2 = Label(win1,
                    text="2 строка - объявление типа: using input; (вводить числа с клавиатуры) или using const; (конкретные числа)")
        ll2.place(x=5, y=55)

        ll3 = Label(win1,
                    text="3 строка - если using input;: method=x;, где x это с (сложение), в (вычитание), у (умножение), д (деление), ц (целочисленное деление), д (деление с остатком) ")
        ll3.place(x=5, y=80)

        ll4 = Label(win1, text="если using const;: const1=x;, где x - первое значение")
        ll4.place(x=5, y=105)

        ll5 = Label(win1, text="4 строка - если using input;: окончание программы: end;")
        ll5.place(x=5, y=130)

        ll6 = Label(win1, text="если using const;: const2=y, где y - второе значение")
        ll6.place(x=5, y=155)

        ll7 = Label(win1,
                    text="5 строка - если using const;: method=x;, где x это с (сложение), в (вычитание), у (умножение), д (деление), ц (целочисленное деление), д (деление с остатком) ")
        ll7.place(x=5, y=180)

        ll8 = Label(win1, text="6 строка - если using const;: окончание программы: end;")
        ll8.place(x=5, y=205)

        ll9 = Label(win1, text="ПРИМЕР:")
        ll9.place(x=5, y=260)

        ll10 = Label(win1, text="<!DOCTYPE sml>")
        ll10.place(x=5, y=285)

        ll11 = Label(win1, text="using const;")
        ll11.place(x=5, y=310)

        ll12 = Label(win1, text="const1=5;")
        ll12.place(x=5, y=335)

        ll13 = Label(win1, text="const2=5;")
        ll13.place(x=5, y=360)

        ll14 = Label(win1, text="method=с;")
        ll14.place(x=5, y=385)

        ll15 = Label(win1, text="end;")
        ll15.place(x=5, y=410)

        bt = Button(win1, text="ВЫПОЛНИТЬ", bg="blue", fg="white", command=x)
        bt.place(x=5, y=445)

        win1.mainloop()

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
                                    win3.geometry('200x100+650+350')
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
                            win3.geometry('200x100+650+350')
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
                            win3.mainloop()

    def f3():
        def cccc():
            win4.destroy()
            win4.update()

        def ccc():
            text_file = open("program1.sml", "w")
            text_file.write(text.get(1.0, END))
            text_file.close()
            os.replace("program1.sml", "C:\program1.sml")
            win4.destroy()
            win4.update()

        win4 = Toplevel()
        win4.title("Сохранение")
        win4.geometry('350x100+650+350')

        lbl0 = Label(win4, text="Сохранить файл program1.sml на локальном диске C:?")
        lbl0.place(x=5, y=5)

        btni = Button(win4, text="ДА", command=ccc, width=7)
        btni.place(x=105, y=40)

        btnl = Button(win4, text="НЕТ", command=cccc, width=7)
        btnl.place(x=180, y=40)

    def f4():
        text_file = open("C:/program1.txt", "r")
        content = text_file.read()
        text.insert(END, content)
        text_file.close()

    window.title("The Simplest Mihail’s Language - IDE & Compiler")
    window.geometry('810x325+600+300')

    lab1 = Label(window, text="The Simplest Mihail’s Language - IDE & Compiler", font=("Arial Bold", 26), fg="red")
    lab1.place(x=35, y=15)

    btn1 = Button(window, text="Справка", bg="red", fg="white", command=f1)
    btn1.place(x=15, y=70)

    text = Text(window, width=60, height=12)
    text.place(x=15, y=110)

    btn2 = Button(window, text="ВЫПОЛНИТЬ", bg="green", fg="white", width=15, command=f2)
    btn2.place(x=90, y=70)

    btn3 = Button(window, text="СОХРАНИТЬ", bg="yellow", fg="black", width=15, command=f3)
    btn3.place(x=220, y=70)

    btn4 = Button(window, text="ОТКРЫТЬ", bg="grey", fg="black", width=15, command=f4)
    btn4.place(x=350, y=70)

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

    window.mainloop()


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

    def rasherec1():
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()

    window.title("MihaSoft Begin")
    window.geometry('790x790+580+140')

    r1 = Label(window, text="Ⓜ", font=("Arial Bold", 350), fg="red")
    r1.place(x=150, y=80)

    r2 = Button(window, text="YourAgeOnline 2.0", font=("Arial Bold", 15), width=23, height=2, bg="blue", fg="white",
                command=germes1)
    r2.place(x=90, y=640)

    r3 = Button(window, text="MiddleScoreOnline 5.0", font=("Arial Bold", 15), width=23, height=2, bg="orange",
                fg="white", command=germes2)
    r3.place(x=400, y=640)

    r4 = Button(window, text="The SML - IDE & Compiler 1.0", font=("Arial Bold", 15), width=25, height=2, bg="green",
                fg="white", command=germes3)
    r4.place(x=240, y=720)


from tkinter import *
import os
from tkinter import Toplevel

window = Tk()
home()
window.mainloop()