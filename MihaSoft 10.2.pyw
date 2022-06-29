# Copyright (C) 2022 Vlasko M.M. <https://mihasoft.glitch.me> All rights reserved.

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
import random
import time
import requests
import winsound


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
        self.id = self.button.after(15, self.showtip)

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


def YourAgeOnline():
    def yao_to_home():
        yao_Destroing()
        home()

    def yao_Destroing():
        yao_title.destroy()
        yao_label_8.destroy()
        yao_label_7.destroy()
        yao_label_6.destroy()
        yao_label_5.destroy()
        yao_label_4.destroy()
        yao_label_3.destroy()
        yao_label_2.destroy()
        yao_label_1.destroy()
        yao_day_input.destroy()
        yao_month_input.destroy()
        yao_year_input.destroy()
        yao_now_day_input.destroy()
        yao_now_month_input.destroy()
        yao_now_year_input.destroy()
        yao_sysdate_button.destroy()
        yao_save_button.destroy()
        yao_birthday_button.destroy()
        yao_delete_button.destroy()
        yao_clean_button.destroy()
        yao_result_button.destroy()
        yao_choice_radbut_1.destroy()
        yao_choice_radbut_2.destroy()
        yao_off.destroy()

    def function():
        global yao_days
        if not yao_day_input.get().isdigit() or not yao_month_input.get().isdigit() or not yao_year_input.get().isdigit() or not yao_now_day_input.get().isdigit() or not yao_now_month_input.get().isdigit() or not yao_now_year_input.get().isdigit():
            messagebox.showerror('Ошибка!', 'Введены некорректные значения!')
        else:
            yao_days = 0

            yao_day_1 = int(yao_day_input.get())
            yao_month_1 = int(yao_month_input.get())
            yao_year_1 = int(yao_year_input.get())
            yao_day_2 = int(yao_now_day_input.get())
            yao_month_2 = int(yao_now_month_input.get())
            yao_year_2 = int(yao_now_year_input.get())
            if ((yao_day_1 >= 1) and (yao_day_1 <= 31)) and ((yao_month_1 >= 1) and (yao_month_1 <= 12)) and (
                    yao_year_1 > 0) and ((yao_day_2 >= 1) and (yao_day_2 <= 31)) and (
                    (yao_month_2 >= 1) and (yao_month_2 <= 12)) and (yao_year_2 > 0) and (yao_year_2 >= yao_year_1):
                z = yao_month_2 - 1
                yao_years = yao_year_2 - yao_year_1 - 1
                h = 12 - yao_month_1
                if yao_month_1 != 2:
                    if yao_month_1 % 2 == 0:
                        k = 30 - yao_day_1
                        yao_days = k + yao_day_2
                        if yao_days >= 30:
                            h += 1
                            yao_days = yao_days - 30
                    else:
                        k = 31 - yao_day_1
                        yao_days = k + yao_day_2
                        if yao_days >= 31:
                            h += 1
                            yao_days = yao_days - 31
                else:
                    if yao_year_1 % 4 == 0:
                        k = 29 - yao_day_1
                        yao_days = k + yao_day_2
                        if yao_days >= 19:
                            h += 1
                            yao_days = yao_days - 29
                        else:
                            k = 28 - yao_day_1
                            yao_days = k + yao_day_2
                        if yao_days >= 28:
                            h += 1
                            yao_days = yao_days - 28
                yao_months = h + z
                if yao_months >= 12:
                    yao_years += 1
                    yao_months = yao_months - 12
                if z % 2 == 0:
                    yao_days += 1
                l = yao_choice_def.get()
                if l == 1:
                    if yao_years == 0:
                        yao_label_8.configure(text=(yao_years, 'год', yao_months, 'месяцев', yao_days - 1, 'дней.'))
                    elif yao_years == 1:
                        yao_label_8.configure(text=(yao_years, 'год', yao_months, 'месяцев', yao_days - 1, 'дней.'))
                    elif (yao_years == 2) or (yao_years == 3) or (yao_years == 4):
                        yao_label_8.configure(text=(yao_years, 'года', yao_months, 'месяцев', yao_days - 1, 'дней.'))
                    else:
                        yao_label_8.configure(text=(yao_years, 'лет', yao_months, 'месяцев', yao_days - 1, 'дней.'))
                if l == 2:
                    yao_label_8.configure(
                        text=(((365.29 * yao_years) + (yao_months * 30.25) + (yao_days - 2) // 1, 'дней.')))
            else:
                messagebox.showerror('Ошибка!', 'Проверьте правильность ввода!')

    def yao_Now_Date():
        yao_now = datetime.datetime.now()
        yao_now_day_input.insert(0, str(yao_now.day))
        yao_now_month_input.insert(0, str(yao_now.month))
        yao_now_year_input.insert(0, str(yao_now.year))

    def yao_Save():
        def yao_Save_OK():
            if not os.path.exists('C:/MihaSoft Files/YAO Files'):
                os.mkdir('C:/MihaSoft Files/YAO Files')
            text_file = open("C:/MihaSoft Files/YAO Files/" + str(yao_save_name_input.get()), "w")
            text_file.write(str(yao_day_input.get()) + '.' + str(yao_month_input.get()) + '.' + str(
                yao_year_input.get()) + '.*******')
            text_file.close()
            yao_save_window.destroy()

        def yao_Save_Abort():
            yao_save_window.destroy()

        yao_save_window = Toplevel()
        yao_save_window.geometry('250x100+70+70')
        yao_save_window.maxsize(250, 100)
        yao_save_window.title('Сохранение')

        yao_save_label = Label(yao_save_window, text='Введите имя...')
        yao_save_label.place(x=5, y=5)

        yao_save_name_input = Entry(yao_save_window, width=20)
        yao_save_name_input.place(x=5, y=30)

        yao_save_button = Button(yao_save_window, text='Сохранить', width=10, height=1, bg="#8ceb8a", fg="black",
                                 command=yao_Save_OK)
        yao_save_button.place(x=140, y=29)

        yao_save_abort_button = Button(yao_save_window, text='Отмена', width=10, height=1, bg="#999999", fg="black",
                                       command=yao_Save_Abort)
        yao_save_abort_button.place(x=140, y=64)

    def yao_Open():
        def yao_Open_OK():
            if yao_files_list != []:
                yao_open_file = open("C:/MihaSoft Files/YAO Files/" + str(yao_open_combobox.get()), "r")
                yao_file = yao_open_file.read()
                yao_open_file.close()

                yao_data_from_file = list(str(yao_file))
                yao_day = ''
                yao_month = ''
                yao_year = ''

                if yao_data_from_file[0] != '.' and yao_data_from_file[1] != '.':
                    yao_day = yao_data_from_file[0] + yao_data_from_file[1]

                elif yao_data_from_file[0] != '.' and yao_data_from_file[1] == '.':
                    yao_day = yao_data_from_file[0]

                if yao_data_from_file[1] == '.':
                    if yao_data_from_file[3] == '.':
                        yao_month = yao_data_from_file[2]
                    elif yao_data_from_file[4] == '.':
                        yao_month = yao_data_from_file[2] + yao_data_from_file[3]

                elif yao_data_from_file[2] == '.':
                    if yao_data_from_file[4] == '.':
                        yao_month = yao_data_from_file[3]
                    elif yao_data_from_file[5] == '.':
                        yao_month = yao_data_from_file[3] + yao_data_from_file[4]

                if yao_data_from_file[3] == '.':
                    if yao_data_from_file[8] == '.':
                        yao_year = yao_data_from_file[4] + yao_data_from_file[5] + yao_data_from_file[6] + \
                                   yao_data_from_file[7]
                    elif yao_data_from_file[7] == '.':
                        yao_year = yao_data_from_file[4] + yao_data_from_file[5] + yao_data_from_file[6]
                    elif yao_data_from_file[6] == '.':
                        yao_year = yao_data_from_file[4] + yao_data_from_file[5]
                    elif yao_data_from_file[5] == '.':
                        yao_year = yao_data_from_file[4]

                elif yao_data_from_file[4] == '.':
                    if yao_data_from_file[9] == '.':
                        yao_year = yao_data_from_file[5] + yao_data_from_file[6] + yao_data_from_file[7] + \
                                   yao_data_from_file[8]
                    elif yao_data_from_file[8] == '.':
                        yao_year = yao_data_from_file[5] + yao_data_from_file[6] + yao_data_from_file[7]
                    elif yao_data_from_file[7] == '.':
                        yao_year = yao_data_from_file[5] + yao_data_from_file[6]
                    elif yao_data_from_file[6] == '.':
                        yao_year = yao_data_from_file[5]

                elif yao_data_from_file[5] == '.':
                    if yao_data_from_file[10] == '.':
                        yao_year = yao_data_from_file[6] + yao_data_from_file[7] + yao_data_from_file[8] + \
                                   yao_data_from_file[9]
                    elif yao_data_from_file[9] == '.':
                        yao_year = yao_data_from_file[6] + yao_data_from_file[7] + yao_data_from_file[8]
                    elif yao_data_from_file[8] == '.':
                        yao_year = yao_data_from_file[6] + yao_data_from_file[7]
                    elif yao_data_from_file[7] == '.':
                        yao_year = yao_data_from_file[6]

                yao_day_input.insert(0, yao_day)
                yao_month_input.insert(0, yao_month)
                yao_year_input.insert(0, yao_year)
                yao_open_window.destroy()

        def yao_Open_Abort():
            yao_open_window.destroy()

        yao_open_window = Toplevel()
        yao_open_window.geometry('300x150+70+70')
        yao_open_window.resizable(0, 0)
        yao_open_window.title('Подставить...')

        yao_open_label = Label(yao_open_window, text='Выберите имя...')
        yao_open_label.place(x=5, y=5)

        yao_files_list = os.listdir('C:/MihaSoft Files/YAO Files')

        yao_open_combobox = ttk.Combobox(yao_open_window, values=yao_files_list, font=('Arial Bold', 16),
                                         state='readonly')
        yao_open_combobox.place(x=10, y=50)

        yao_open_button = Button(yao_open_window, text='Подставить', font=("Arial Bold", 10), bg='#7bd491', width=14,
                                 command=yao_Open_OK)
        yao_open_button.place(x=10, y=100)

        yao_open_abort_button = Button(yao_open_window, text='Отмена', font=('Arial Bold', 10), bg='#999999', width=14,
                                       command=yao_Open_Abort)
        yao_open_abort_button.place(x=150, y=100)

    def yao_Delete():
        def yao_Delete_OK():
            if yao_files_list != []:
                os.remove('C:/MihaSoft Files/YAO Files/' + str(yao_del_combobox.get()))
                yao_delete_window.destroy()

        def yao_Delete_Abort():
            yao_delete_window.destroy()

        yao_delete_window = Toplevel()
        yao_delete_window.geometry('300x150+70+70')
        yao_delete_window.resizable(0, 0)
        yao_delete_window.title('Удаление записи')

        yao_del_label = Label(yao_delete_window, text='Выберите запись для удаления...')
        yao_del_label.place(x=5, y=5)

        yao_files_list = os.listdir('C:/MihaSoft Files/YAO Files')

        yao_del_combobox = ttk.Combobox(yao_delete_window, values=yao_files_list, font=("Arial Bold", 16),
                                        state="readonly")
        yao_del_combobox.place(x=10, y=50)

        yao_del_ok_button = Button(yao_delete_window, text="Удалить", font=("Arial Bold", 10), fg="black", bg='#eb8a8a',
                                   width=14, command=yao_Delete_OK)
        yao_del_ok_button.place(x=10, y=100)

        yao_del_abort_button = Button(yao_delete_window, text="Отмена", font=("Arial Bold", 10), fg="black",
                                      bg='#999999', width=14, command=yao_Delete_Abort)
        yao_del_abort_button.place(x=150, y=100)

    def yao_Clean():
        yao_day_input.delete(0, 'end')
        yao_now_day_input.delete(0, 'end')
        yao_month_input.delete(0, 'end')
        yao_now_month_input.delete(0, 'end')
        yao_year_input.delete(0, 'end')
        yao_now_year_input.delete(0, 'end')

    window.title("YourAgeOnline 3.0")
    window.geometry('650x250+50+50')

    yao_title = Label(window, text="YourAgeOnline 3.0", font=("Arial Bold", 16), fg="red")
    yao_title.place(x=40, y=20)

    yao_label_1 = Label(window, text="Дата рождения:", font=("Times New Roman", 12))
    yao_label_1.place(x=40, y=60)

    yao_day_input = Entry(window, width=4)
    yao_day_input.place(x=40, y=100)
    ToolTip(yao_day_input, 'День')

    yao_label_2 = Label(window, text=".", font=("Times New Roman", 12))
    yao_label_2.place(x=73, y=103)

    yao_month_input = Entry(window, width=4)
    yao_month_input.place(x=90, y=100)
    ToolTip(yao_month_input, 'Месяц')

    yao_label_3 = Label(window, text=".", font=("Times New Roman", 12))
    yao_label_3.place(x=124, y=100)

    yao_year_input = Entry(window, width=9)
    yao_year_input.place(x=140, y=100)
    ToolTip(yao_year_input, 'Год')

    yao_sysdate_button = Button(window, text="Подставить т. д.", width=13, height=1, bg="#eef5b3", fg="black",
                                command=yao_Now_Date)
    yao_sysdate_button.place(x=250, y=20)
    ToolTip(yao_sysdate_button, 'Подставить системную дату...')

    yao_save_button = Button(window, text="Сохранить зап.", width=13, height=1, bg="#8ceb8a", fg="black",
                             command=yao_Save)
    yao_save_button.place(x=490, y=120)
    ToolTip(yao_save_button, 'Сохранить данные о дате рождения...')

    yao_birthday_button = Button(window, text="Подставить д. р.", width=13, height=1, bg="#b3f5ec", fg="black",
                                 command=yao_Open)
    yao_birthday_button.place(x=370, y=20)
    ToolTip(yao_birthday_button, 'Подставить сохранённую дату рождения...')

    yao_delete_button = Button(window, text="Удалить зап.", width=13, height=1, bg="#eb8a8a", fg="black",
                               command=yao_Delete)
    yao_delete_button.place(x=490, y=70)
    ToolTip(yao_delete_button, 'Удалить запись о дате рождения...')

    yao_clean_button = Button(window, text="Очистить", width=13, height=1, bg="#ebd38a", fg="black", command=yao_Clean)
    yao_clean_button.place(x=490, y=20)
    ToolTip(yao_clean_button, 'Очистить поля ввода...')

    yao_label_4 = Label(window, text="Текущая дата:", font=("Times New Roman", 12))
    yao_label_4.place(x=300, y=60)

    yao_now_day_input = Entry(window, width=4)
    yao_now_day_input.place(x=300, y=100)
    ToolTip(yao_now_day_input, 'День')

    yao_label_5 = Label(window, text=".", font=("Times New Roman", 12))
    yao_label_5.place(x=333, y=100)

    yao_now_month_input = Entry(window, width=4)
    yao_now_month_input.place(x=350, y=100)
    ToolTip(yao_now_month_input, 'Месяц')

    yao_label_6 = Label(window, text=".", font=("Times New Roman", 12))
    yao_label_6.place(x=384, y=100)

    yao_now_year_input = Entry(window, width=9)
    yao_now_year_input.place(x=400, y=100)
    ToolTip(yao_now_year_input, 'Год')

    yao_choice_def = IntVar()

    yao_choice_radbut_1 = Radiobutton(window, text="Вывести возраст в годах, месяцах и днях", variable=yao_choice_def,
                                      value=1)
    yao_choice_radbut_1.place(x=40, y=150)

    yao_choice_radbut_2 = Radiobutton(window, text="Вывести возраст в днях", variable=yao_choice_def, value=2)
    yao_choice_radbut_2.place(x=300, y=150)

    yao_result_button = Button(window, text="РАССЧИТАТЬ", width=19, height=2, bg="black", fg="white", command=function)
    yao_result_button.place(x=40, y=190)

    yao_label_7 = Label(window, text="Ваш возраст: ", font=("Times New Roman", 16))
    yao_label_7.place(x=220, y=190)

    yao_label_8 = Label(window, text="", font=("Times New Roman", 16))
    yao_label_8.place(x=350, y=190)

    yao_off = Button(window, text="⌂", font=("Arial Bold", 15), width=2, height=1, bg="black", fg="white",
                     command=yao_to_home)
    yao_off.place(x=0, y=0)
    ToolTip(yao_off, 'На главную...')


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
        if not eba.get().isdigit() or (not huya.get().isdigit() and huya.get() != ''):
            messagebox.showerror('Ошибка!', 'Введены некорректные значения!')
        else:
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
                    lbl5.configure(text=('У вас выходит пятёрка!\n Не получайте плохих оценок!'))
        print(b, j)

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
        btn5.destroy()
        off.destroy()
        text.destroy()

    def returni4():
        rasherec4()
        home()

    def f1():
        def x():
            win2 = Toplevel()
            win2.title("run...")
            win2.geometry('200x100+50+50')
            win2.resizable(0, 0)
            asd = Label(win2, text="5 + 5 = 10")
            asd.place(x=10, y=30)
            win2.mainloop()

        def g():
            win1.destroy()

        win1 = Toplevel()
        win1.title("Справка")
        win1.geometry('1200x500+50+50')
        win1.resizable(0, 0)

        tox = Text(win1, width=145, height=25, font=('Times New Roman', 12))
        tox.place(x=5, y=5)

        text_insert = '''
          The Simplest Mihail’s Language
            _____________
          1 строка - объявление языка: <!DOCTYPE sml>
            _____________
          2 строка - объявление типа: using input; (вводить числа с клавиатуры) или using const; (конкретные числа)  
            _____________
          3 строка - если using input;: method=x;, где x это с (сложение), в (вычитание), у (умножение), д (деление), ц (целочисленное деление), д (деление с остатком)  
                     если using const;: const1=x;, где x - первое значение  
            _____________  
          4 строка - если using input;: окончание программы: end;  
                     если using const;: const2=y, где y - второе значение
            _____________  
          5 строка - если using const;: method=x;, где x это с (сложение), в (вычитание), у (умножение), д (деление), ц (целочисленное деление), д (деление с остатком)  
            _____________  
          6 строка - если using const;: окончание программы: end;

          ПРИМЕР:  
            <!DOCTYPE sml>
            using const;
            const1=5;
            const2=5;
            method=с;
            end;  
        '''
        tox.insert(1.0, text_insert)
        tox.configure(state='disabled')

        bt = Button(win1, text="ВЫПОЛНИТЬ", bg="white", fg="black", command=x)
        bt.place(x=133, y=450)

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
                                    win3.title("run...")
                                    win3.geometry('200x100+50+50')
                                    win3.maxsize(200, 100)

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
                            win3.title("run...")
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

        def ccc():
            text_file = open('C:/MihaSoft Files/SML Files/' + str(ent.get()) + '.miha', "w")
            text_file.write(text.get(1.0, END))
            text_file.close()
            win4.destroy()

        win4 = Toplevel()
        win4.title("Сохранение")
        win4.geometry('350x100+80+80')
        win4.resizable(0, 0)

        lbl0 = Label(win4, text="Введите назавание программы...")
        lbl0.place(x=5, y=5)

        ent = Entry(win4, width=30)
        ent.place(x=10, y=40)

        btni = Button(win4, text="Сохранить", bg='#c0ebd6', command=ccc, width=10)
        btni.place(x=225, y=10)

        btnl = Button(win4, text="Отмена", bg='#b8b8b8', command=cccc, width=10)
        btnl.place(x=225, y=50)

    def f4():
        def her():
            text_file = open('C:/MihaSoft Files/SML Files/' + str(zul1.get()), "r")
            content = text_file.read()
            text.insert(END, content)
            text_file.close()
            win4.destroy()

        def huer():
            win4.destroy()

        win4 = Toplevel()
        win4.title("Открыть")
        win4.geometry('350x120+80+80')
        win4.resizable(0, 0)

        lbl0 = Label(win4, text="Выберите файл...")
        lbl0.place(x=5, y=5)

        sa = os.listdir('C:/MihaSoft Files/SML Files')

        zul1 = ttk.Combobox(win4, values=sa, font=("Arial Bold", 16), width=20, state="readonly")
        zul1.place(x=10, y=40)

        btni = Button(win4, text="Открыть", bg='#c0ebd6', command=her, width=10)
        btni.place(x=225, y=80)

        btnl = Button(win4, text="Отмена", bg='#b8b8b8', command=huer, width=10)
        btnl.place(x=135, y=80)

    def f5():
        def hera():
            os.remove('C:/MihaSoft Files/SML Files/' + str(zal1.get()))
            win5.destroy()

        def er():
            win5.destroy()

        win5 = Toplevel()
        win5.title("Удалить")
        win5.geometry('350x120+80+80')
        win5.resizable(0, 0)

        lbl0 = Label(win5, text="Выберите файл...")
        lbl0.place(x=5, y=5)

        sa = os.listdir('C:/MihaSoft Files/SML Files')

        zal1 = ttk.Combobox(win5, values=sa, font=("Arial Bold", 16), width=20, state="readonly")
        zal1.place(x=10, y=40)

        btni = Button(win5, text="Удалить", bg='#eb9898', command=hera, width=10)
        btni.place(x=225, y=80)

        btnl = Button(win5, text="Отмена", bg='#b8b8b8', command=er, width=10)
        btnl.place(x=135, y=80)

    if os.path.exists('C:/MihaSoft Files/SML Files') == False:
        os.mkdir('C:/MihaSoft Files/SML Files')

    window.title("The Simplest Mihail’s Language - IDE & Compiler")
    window.geometry('810x325+50+50')

    lab1 = Label(window, text="The Simplest Mihail’s Language - IDE & Compiler", font=("Arial Bold", 26), fg="red")
    lab1.place(x=35, y=15)

    btn1 = Button(window, text="Справка", bg="red", fg="white", command=f1)
    btn1.place(x=15, y=70)

    text = Text(window, width=75, height=12)
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

    btn5 = Button(window, text="УДАЛИТЬ", bg="#eb9898", fg="black", width=15, command=f5)
    btn5.place(x=480, y=70)
    ToolTip(btn5, 'Удалить сохранённый код...')

    lol = Label(window, text="", fg="red")
    lol.place(x=670, y=110)

    lol1 = Label(window, text="", fg="red")
    lol1.place(x=670, y=140)

    lol2 = Label(window, text="", fg="red")
    lol2.place(x=670, y=170)

    lol3 = Label(window, text="", fg="red")
    lol3.place(x=670, y=200)

    lol4 = Label(window, text="", fg="red")
    lol4.place(x=670, y=230)

    lol5 = Label(window, text="", fg="red")
    lol5.place(x=670, y=260)

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

        if not zk.get().isdigit() or not zt.get().isdigit() or not txt.get().isdigit():
            messagebox.showerror('Ошибка!', 'Введены некорректные значения!')
        else:
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
        btn5.destroy()
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
            her = 1

        def CloseParam():
            wind1.destroy()

        wind1 = Toplevel()
        wind1.title("Параметры")
        wind1.geometry('300x110+80+80')
        wind1.resizable(0, 0)

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

        cz_close_button = Button(wind1, text="Отмена", bg='#b8b8b8', width=10, command=CloseParam)
        cz_close_button.place(x=80, y=70)

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

            def o2():
                wind2.destroy()

            wind2 = Toplevel()
            wind2.title("Новая игра")
            wind2.geometry('200x100+80+80')
            wind2.resizable(0, 0)

            lel = Label(wind2, text="Начать новую игру?")
            lel.place(x=5, y=5)

            btnu = Button(wind2, text="ДА", bg='#c0ebd6', width=10, command=o1)
            btnu.place(x=10, y=45)

            btny = Button(wind2, text="НЕТ", bg='#ebc0d0', width=10, command=o2)
            btny.place(x=110, y=45)

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

                now = datetime.datetime.now()
                o = str(now.strftime("%d-%m-%Y %H.%M"))
                text_file = open('C:/MihaSoft Files/CZ Files/Log_' + o + '.miha', "w")
                text_file.write(zx)
                text_file.close()

            def ol():
                ggg()
                wind4.destroy()

            def al():
                wind4.destroy()

            wind4 = Toplevel()
            wind4.title("Сохранение")
            wind4.geometry('265x100+80+80')
            wind4.resizable(0, 0)

            lelx = Label(wind4, text="Сохранить отчёт об игре?")
            lelx.place(x=5, y=5)

            btna = Button(wind4, text="ДА", bg='#c0ebd6', width=10, command=ol)
            btna.place(x=25, y=45)

            btnb = Button(wind4, text="НЕТ", bg='#ebc0d0', width=10, command=al)
            btnb.place(x=125, y=45)

    def onclu():
        def i():
            wind6.destroy()

        def ii():
            def ia():
                wind5.destroy()

            xx = str(zul1.get())
            wind6.destroy()

            wind5 = Toplevel()
            wind5.title("Отчёт")
            wind5.geometry('200x100+80+80')
            wind5.maxsize(300, 150)

            lin = Label(wind5, text="")
            lin.place(x=5, y=5)

            b = Button(wind5, text='OK', command=ia)
            b.place(x=15, y=35)

            f = open("C:/MihaSoft Files/CZ Files/" + xx, "r")
            con = f.readline()
            con = str(con)
            lin.configure(text=con)
            f.close()

        wind6 = Toplevel()
        wind6.title("Открыть отчёт")
        wind6.geometry('385x140+80+80')
        wind6.resizable(0, 0)

        j = os.listdir('C:/MihaSoft Files/CZ Files')

        lix = Label(wind6, text='Выберите запись...')
        lix.place(x=5, y=5)

        zul1 = ttk.Combobox(wind6, values=j, font=("Arial Bold", 16), width=27, state="readonly")
        zul1.place(x=10, y=40)

        but = Button(wind6, text='Открыть', bg='#c0ebd6', width=10, command=ii)
        but.place(x=280, y=90)

        but1 = Button(wind6, text='Отмена', bg='#b8b8b8', width=10, command=i)
        but1.place(x=170, y=90)

    def oncli():
        def iiz():
            os.remove('C:/MihaSoft Files/CZ Files/' + str(zul1.get()))
            wind6.destroy()

        def iz():
            wind6.destroy()

        wind6 = Toplevel()
        wind6.title("Удалить отчёт")
        wind6.geometry('385x140+80+80')
        wind6.resizable(0, 0)

        j = os.listdir('C:/MihaSoft Files/CZ Files')

        lix = Label(wind6, text='Выберите запись...')
        lix.place(x=5, y=5)

        zul1 = ttk.Combobox(wind6, values=j, font=("Arial Bold", 16), width=27, state="readonly")
        zul1.place(x=10, y=40)

        but = Button(wind6, text='Удалить', bg='#eb9898', width=10, command=iiz)
        but.place(x=280, y=90)

        but1 = Button(wind6, text='Отмена', bg='#b8b8b8', width=10, command=iz)
        but1.place(x=170, y=90)

    if os.path.exists('C:/MihaSoft Files/CZ Files') == False:
        os.mkdir('C:/MihaSoft Files/CZ Files')

    window.geometry('790x600+50+50')
    window.title("CrossZero 2.1")
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

    btn3 = Button(window, text="Сохранить\n отчёт", font=("Times New Roman", 14), fg="blue", bg='#e0cf92',
                  command=oncla)
    btn3.place(x=20, y=240)
    ToolTip(btn3, 'Сохранить отчёт о последней игре...')

    btn4 = Button(window, text="Открыть\n отчёт", font=("Times New Roman", 14), fg="blue", bg='#87e6ad',
                  command=onclu)
    btn4.place(x=20, y=350)
    ToolTip(btn4, 'Открыть отчёт в новом окне...')

    btn5 = Button(window, text="Удалить\n отчёт", font=("Times New Roman", 14), fg="blue", bg='#eb9898',
                  command=oncli)
    btn5.place(x=20, y=460)
    ToolTip(btn5, 'Удалить существующий отчёт...')

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
            win2.resizable(0, 0)
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

        def CloseSave():
            win1.destroy()

        win1 = Toplevel()
        win1.geometry('450x400+70+70')
        win1.resizable(0, 0)
        win1.title("Создание новой заметки")

        but1 = Button(win1, text="Сохранить", font=("Arial Bold", 12), fg="black", bg='#b2e6ae', width=13,
                      command=click)
        but1.place(x=15, y=5)

        txt = Text(win1, width=50, height=15)
        txt.place(x=15, y=50)

        mn_close_button = Button(win1, text='Отмена', font=("Arial Bold", 12), bg='#b8b8b8', width=13,
                                 command=CloseSave)
        mn_close_button.place(x=290, y=5)

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
            zol.destroy()
            btt.destroy()
            a = os.listdir('C:/MihaSoft Files/MihNote Files')
            if a != []:
                def dele():
                    c = str(zol.get())
                    zol.destroy()
                    btt.destroy()
                    os.remove('C:/MihaSoft Files/MihNote Files/' + c)
                    win3.destroy()
                    win3.update()

                def CloseDel():
                    win3.destroy()

                win3 = Toplevel()
                win3.geometry('300x100+90+90')
                win3.resizable(0, 0)
                win3.title("Удаление")

                l2 = Label(win3, text="Удалить файл?")
                l2.place(x=5, y=5)

                bt = Button(win3, text="ОК", font=("Arial Bold", 10), bg='#c97979', width=13, command=dele)
                bt.place(x=170, y=60)

                mn_close_button = Button(win3, text='Отмена', font=("Arial Bold", 10), bg='#b8b8b8', width=13,
                                         command=CloseDel)
                mn_close_button.place(x=170, y=15)

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

                def CloseEdit():
                    win4.destroy()

                d = os.listdir('C:/MihaSoft Files/MihNote Files')
                if d != []:
                    m = str(zol2.get())
                    zol2.destroy()
                    btt2.destroy()

                    win4 = Toplevel()
                    win4.geometry('450x400+70+70')
                    win4.resizable(0, 0)
                    win4.title("Редактирование")

                    but0 = Button(win4, text="Сохранить", font=("Arial Bold", 12), bg='#b2e6ae', width=13,
                                  command=com)
                    but0.place(x=15, y=5)

                    txt1 = Text(win4, width=50, height=15)
                    txt1.place(x=15, y=50)

                    fa = open("C:/MihaSoft Files/MihNote Files/" + m, "r")
                    content = fa.read()
                    txt1.insert(END, content)
                    fa.close()

                    mn_close_button = Button(win4, text='Отмена', font=("Arial Bold", 12), bg='#b8b8b8', width=13,
                                             command=CloseEdit)
                    mn_close_button.place(x=290, y=5)

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

        def CloseSave():
            wind1.destroy()

        global x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, german, flagx, dd
        all()
        a = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11]
        if flagx == False:
            wind1 = Toplevel()
            wind1.geometry('300x100+70+70')
            wind1.resizable(0, 0)
            wind1.title('Сохранение')

            lcl = Label(wind1, text='Сохранить изменения?')
            lcl.place(x=5, y=5)

            but4 = Button(wind1, text='ОК', width=10, bg='#93e6a8', command=goo)
            but4.place(x=200, y=43)

            wm_close_button = Button(wind1, text='Отмена', bg='#b8b8b8', width=10, command=CloseSave)
            wm_close_button.place(x=100, y=43)
        else:
            wind1 = Toplevel()
            wind1.geometry('300x100+70+70')
            wind1.resizable(0, 0)
            wind1.title('Сохранение')

            lcl = Label(wind1, text='Введите название файла...')
            lcl.place(x=5, y=5)

            ect = Entry(wind1, width=25)
            ect.place(x=10, y=45)

            but4 = Button(wind1, text='Сохранить', width=10, bg='#93e6a8', command=go)
            but4.place(x=200, y=53)

            wm_close_button = Button(wind1, text='Отмена', bg='#b8b8b8', width=10, command=CloseSave)
            wm_close_button.place(x=200, y=13)

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

        def CloseEdit():
            wind2.destroy()

        xx = os.listdir('C:/MihaSoft Files/WM Files')
        wind2 = Toplevel()
        wind2.geometry('300x100+70+70')
        wind2.resizable(0, 0)
        wind2.title('Открыть')

        lcl = Label(wind2, text='Выберите файл...')
        lcl.place(x=5, y=5)

        ect = ttk.Combobox(wind2, values=xx, state='readonly')
        ect.place(x=10, y=45)

        but4 = Button(wind2, text='Редактировать', width=13, bg='#93e6a8', command=gg)
        but4.place(x=180, y=53)

        wm_close_button = Button(wind2, text='Отмена', bg='#b8b8b8', width=13, command=CloseEdit)
        wm_close_button.place(x=180, y=13)

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

        def CloseOp():
            wind2.destroy()

        xx = os.listdir('C:/MihaSoft Files/WM Files')
        wind2 = Toplevel()
        wind2.geometry('300x100+70+70')
        wind2.resizable(0, 0)
        wind2.title('Открыть')

        lcl = Label(wind2, text='Выберите файл...')
        lcl.place(x=5, y=5)

        ect = ttk.Combobox(wind2, values=xx, state='readonly')
        ect.place(x=10, y=45)

        but4 = Button(wind2, text='Открыть', width=10, bg='#93e6a8', command=gg)
        but4.place(x=200, y=53)

        wm_close_button = Button(wind2, text='Отмена', bg='#b8b8b8', width=10, command=CloseOp)
        wm_close_button.place(x=200, y=13)

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
        wind3.resizable(0, 0)
        wind3.title('Удалить')

        def CloseDel():
            wind3.destroy()

        lcl = Label(wind3, text='Выберите файл...')
        lcl.place(x=5, y=5)

        ect = ttk.Combobox(wind3, values=xx, state='readonly')
        ect.place(x=10, y=45)

        buts = Button(wind3, text='Удалить', width=10, bg='#e69b93', command=gga)
        buts.place(x=200, y=53)

        wm_close_button = Button(wind3, text='Отмена', bg='#b8b8b8', width=10, command=CloseDel)
        wm_close_button.place(x=200, y=13)

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


def fallout8():
    def returnil():
        lbl1.destroy()
        but.destroy()
        off.destroy()
        home()

    def beg():
        z = open('C:/MihaSoft Files/FlagHW.miha', 'w')
        z.write('.')
        z.close()
        but.configure(text='ОСТАНОВИТЬ ПРОГРАММУ', command=stop, bg='#eb9898')
        ToolTip(but, "Запретить показ уведомлений о праздничных датах при запуске MihaSoft...")

    def stop():
        os.remove('C:/MihaSoft Files/FlagHW.miha')
        but.configure(text='ЗАПУСТИТЬ ПРОГРАММУ', command=beg, bg='#98ebc0')
        ToolTip(but, "Разрешить показ уведомлений о праздничных датах при запуске MihaSoft...")

    window.geometry('400x200+50+50')
    window.title('HolidayWarnings 1.0')

    lbl1 = Label(window, text='HolidayWarnings 1.0', font=('Times New Roman', 20), fg='red')
    lbl1.place(x=50, y=5)

    but = Button(window, text='', font=("Arial Bold", 15), width=25, height=2, bg='#98ebc0')
    but.place(x=40, y=80)

    if os.path.exists('C:/MihaSoft Files/FlagHW.miha') == False:
        but.configure(text='ЗАПУСТИТЬ ПРОГРАММУ', command=beg, bg='#98ebc0')
        ToolTip(but, "Разрешить показ уведомлений о праздничных датах при запуске MihaSoft...")

    else:
        but.configure(text='ОСТАНОВИТЬ ПРОГРАММУ', command=stop, bg='#eb9898')
        ToolTip(but, "Запретить показ уведомлений о праздничных датах при запуске MihaSoft...")

    off = Button(window, text="⌂", font=("Arial Bold", 15), width=2, height=1, bg="black", fg="white", command=returnil)
    off.place(x=0, y=0)
    ToolTip(off, "На главную...")


def fallout9():
    def returnia():
        rashereca()
        home()

    def rashereca():
        lbl.destroy()
        lbl1.destroy()
        lbl2.destroy()
        lbl3.destroy()
        ent.destroy()
        ent1.destroy()
        txt.destroy()
        but.destroy()
        but1.destroy()
        but2.destroy()
        off.destroy()

    if os.path.exists('C:/MihaSoft Files/YW Files') == False:
        os.mkdir('C:/MihaSoft Files/YW Files')

    def create():
        if not ent1.get().isdigit() or not ent1.get().isdigit() or (
                (ent1.get().isdigit() and ent1.get().isdigit()) and int(ent.get()) < 1 or int(ent.get()) > 31 or int(
            ent1.get()) < 1 or int(ent1.get()) > 12):
            messagebox.showerror('Ошибка!', 'Введены некорректные данные!')

        else:
            a = str(ent.get())
            b = str(ent1.get())
            c = str(txt.get("1.0", END))
            la = [a, b, c]
            np.save('C:/MihaSoft Files/YW Files/' + a + '.' + b, la)
            ent.delete(0, 'end')
            ent1.delete(0, 'end')
            txt.delete(1.0, END)

    def look():
        def gga():
            ka = np.load('C:/MihaSoft Files/YW Files/' + str(ect.get()))
            wind = Toplevel()
            wind.attributes('-topmost', 'true')
            wind.geometry('480x400+80+80')
            wind.title(ect.get())

            lbl = Label(wind, text=ka[2], font=('Times New Roman', 20), fg='red')
            lbl.place(x=5, y=255)

            r1 = Label(wind, text="Ⓜ", font=("Arial Bold", 150), fg="green")
            r1.place(x=120, y=5)

            wind3.destroy()

        def CloseLook():
            wind3.destroy()

        xx = os.listdir('C:/MihaSoft Files/YW Files')

        wind3 = Toplevel()
        wind3.geometry('300x100+70+70')
        wind3.resizable(0, 0)
        wind3.title('Предварительный просмотр')

        lcl = Label(wind3, text='Выберите запись...')
        lcl.place(x=5, y=5)

        ect = ttk.Combobox(wind3, values=xx, state='readonly')
        ect.place(x=10, y=45)

        buts = Button(wind3, text='Открыть', width=10, bg='#aae09f', command=gga)
        buts.place(x=200, y=23)

        yw_close_button = Button(wind3, text='Отмена', width=10, bg='#b8b8b8', command=CloseLook)
        yw_close_button.place(x=200, y=60)

    def delet():
        def gg():
            os.remove('C:/MihaSoft Files/YW Files/' + str(ect.get()))
            wind3.destroy()

        def CloseDel():
            wind3.destroy()

        xx = os.listdir('C:/MihaSoft Files/YW Files')

        wind3 = Toplevel()
        wind3.geometry('300x100+70+70')
        wind3.resizable(0, 0)
        wind3.title('Удаление')

        lcl = Label(wind3, text='Выберите запись...')
        lcl.place(x=5, y=5)

        ect = ttk.Combobox(wind3, values=xx, state='readonly')
        ect.place(x=10, y=45)

        buts = Button(wind3, text='Удалить', width=10, bg='#e69b93', command=gg)
        buts.place(x=200, y=23)

        yw_close_button = Button(wind3, text='Отмена', width=10, bg='#b8b8b8', command=CloseDel)
        yw_close_button.place(x=200, y=60)

    window.geometry('400x400+50+50')
    window.title('YourWarnings 1.0')

    lbl = Label(window, text='YourWarnings 1.0', font=('Times New Roman', 20), fg='red')
    lbl.place(x=50, y=5)

    lbl1 = Label(window, text='Введите дату:')
    lbl1.place(x=20, y=70)

    ent = Entry(window, width=20)
    ent.place(x=20, y=100)

    lbl2 = Label(window, text='Введите месяц:')
    lbl2.place(x=20, y=140)

    ent1 = Entry(window, width=20)
    ent1.place(x=20, y=170)

    lbl3 = Label(window, text='Введите текст сообщения:')
    lbl3.place(x=20, y=210)

    txt = Text(window, width=30, height=5)
    txt.place(x=20, y=240)

    but = Button(window, text='Добавить', bg="#aae09f", width=20, command=create)
    but.place(x=20, y=350)
    ToolTip(but, 'Добавить новое уведомление...')

    but1 = Button(window, text='Просмотреть', bg="#e0d09f", width=15, command=look)
    but1.place(x=200, y=70)
    ToolTip(but1, 'Предварительный просмотр уведомления...')

    but2 = Button(window, text='Удалить', bg="#e09f9f", width=15, command=delet)
    but2.place(x=200, y=120)
    ToolTip(but2, 'Удалить файл уведомления...')

    off = Button(window, text="⌂", font=("Arial Bold", 15), width=2, height=1, bg="black", fg="white",
                 command=returnia)
    off.place(x=0, y=0)
    ToolTip(off, "На главную...")


def YourWarnings():
    if os.path.exists('C:/MihaSoft Files/YW Files') == False:
        os.mkdir('C:/MihaSoft Files/YW Files')
    xx = os.listdir('C:/MihaSoft Files/YW Files')
    now = datetime.datetime.now()
    ny = str(now.day) + '.' + str(now.month) + '.npy'
    for i in range(len(xx)):
        if xx[i] == ny:
            ka = np.load('C:/MihaSoft Files/YW Files/' + xx[i])
            wind = Toplevel()
            wind.attributes('-topmost', 'true')
            wind.geometry('480x400+320+80')
            wind.title(xx[i])

            lbl = Label(wind, text=ka[2], font=('Times New Roman', 20), fg='red')
            lbl.place(x=5, y=255)

            r1 = Label(wind, text="Ⓜ", font=("Arial Bold", 150), fg="green")
            r1.place(x=120, y=5)


def HolidayWarnings():
    def okno(text):
        now = datetime.datetime.now()

        wind = Toplevel()
        wind.attributes('-topmost', 'true')
        wind.geometry('480x400+80+80')
        wind.title(now)

        lbl = Label(wind, text='ПОЗДРАВЛЯЕМ!!!', font=('Times New Roman', 20), fg='red')
        lbl.place(x=115, y=255)

        lbl1 = Label(wind, text=text, font=('Times New Roman', 20), fg='red')
        lbl1.place(x=35, y=295)

        r1 = Label(wind, text="Ⓜ", font=("Arial Bold", 150), fg="red")
        r1.place(x=120, y=5)

    if os.path.exists('C:/MihaSoft Files/FlagHW.miha') == True:
        now = datetime.datetime.now()

        if now.day == 1 and now.month == 1:
            okno('Сегодня наступил новый\n    ' + str(now.year) + ' год!')

        if now.day == 7 and now.month == 1:
            okno('Сегодня отмечается\n      Рождество Христово! ')

        if now.day == 12 and now.month == 1:
            okno('Сегодня отмечается День\n Работника прокуратуры РФ!')

        if now.day == 13 and now.month == 1:
            okno('Сегодня День Российской\n печати!')

        if now.day == 14 and now.month == 1:
            okno('Сегодня День\n Трубопроводных войск!')

        if now.day == 21 and now.month == 1:
            okno('Сегодня День\n Инженерных войск!')

        if now.day == 25 and now.month == 1:
            okno('Сегодня День\n Российского студенчества!')

        if now.day == 27 and now.month == 1:
            okno('Сегодня День Снятия\n блокады Ленинграда!')

        if now.day == 2 and now.month == 2:
            okno('Сегодня День победы\n в Сталинградской битве!')

        if now.day == 8 and now.month == 2:
            okno('Сегодня День\n Российской науки!')

        if now.day == 9 and now.month == 2:
            okno('Сегодня День Работника\n гражданской авиации!')

        if now.day == 10 and now.month == 2:
            okno('Сегодня День\n Дипломатического работника!')

        if now.day == 15 and now.month == 2:
            okno('Сегодня День Памяти\n воинов-интернационалистов!')

        if now.day == 17 and now.month == 2:
            okno('Сегодня День Российских\n студенческих отрядов!')

        if now.day == 23 and now.month == 2:
            okno('Сегодня День\n Защитника Отечества!')

        if now.day == 24 and now.month == 2:
            okno('Сегодня день, когда\n Земля остановилась...')

        if now.day == 27 and now.month == 2:
            okno('Сегодня День Сил\n специальных операций!')

        if now.day == 1 and now.month == 3:
            okno('Сегодня Всемирный\n день Гражданской обороны!')

        if now.day == 8 and now.month == 3:
            okno('Сегодня Международный\n Женский день!')

        if now.day == 11 and now.month == 3:
            okno('Сегодня День\n Работников наркоконтроля!')

        if now.day == 12 and now.month == 3:
            okno('Сегодня День работников\n уголовно-исполнительной системы!')

        if now.day == 18 and now.month == 3:
            okno('Сегодня День\n Воссоединения Крыма и России!')

        if now.day == 19 and now.month == 3:
            okno('Сегодня День \nМоряка-подводника!')

        if now.day == 23 and now.month == 3:
            okno('Сегодня День Гидрометеоролога!')

        if now.day == 25 and now.month == 3:
            okno('Сегодня День\n Работника культуры России!')

        if now.day == 27 and now.month == 3:
            okno('Сегодня День Войск\n национальной гвардии РФ!')

        if now.day == 29 and now.month == 3:
            okno('Сегодня День Специалиста\n юридической службы!')

        if now.day == 1 and now.month == 4:
            okno('Сегодня День Смеха!')

        if now.day == 2 and now.month == 4:
            okno('Сегодня День Единения народов!')

        if now.day == 8 and now.month == 4:
            okno('Сегодня День\n Сотрудников военкоматов!')

        if now.day == 12 and now.month == 4:
            okno('Сегодня День Космонавтики!')

        if now.day == 15 and now.month == 4:
            okno('Сегодня День специалиста по\n радиоэлектронной борьбе!')

        if now.day == 18 and now.month == 4:
            okno('Сегодня День Победы\n на Чудском озере!')

        if now.day == 19 and now.month == 4:
            okno('Сегодня День\n Российской полиграфии!')

        if now.day == 21 and now.month == 4:
            okno('Сегодня День\n Местного самоуправления!')

        if now.day == 26 and now.month == 4:
            okno('Сегодня День Нотариата!')

        if now.day == 27 and now.month == 4:
            okno('Сегодня День\n Российского парламентаризма!')

        if now.day == 28 and now.month == 4:
            okno('Сегодня Международный\n день Охраны Труда!')

        if now.day == 30 and now.month == 4:
            okno('Сегодня День Пожарной охраны!')

        if now.day == 1 and now.month == 5:
            okno('Сегодня Праздник\n Весны и Труда!')

        if now.day == 7 and now.month == 5:
            okno('Сегодня День Радио!')

        if now.day == 9 and now.month == 5:
            okno('Сегодня День Победы!')

        if now.day == 21 and now.month == 5:
            okno('Сегодня День Полярника!')

        if now.day == 24 and now.month == 5:
            okno('Сегодня День Славянской\n письменности и культуры!')

        if now.day == 25 and now.month == 5:
            okno('Сегодня День Филолога!')

        if now.day == 26 and now.month == 5:
            okno('Сегодня День\n Российского предпринимательства!')

        if now.day == 27 and now.month == 5:
            okno('Сегодня Общероссийский\n день библиотек!')

        if now.day == 28 and now.month == 5:
            okno('Сегодня День Пограничника!')

        if now.day == 29 and now.month == 5:
            okno('Сегодня День\n Военного автомобилиста!')

        if now.day == 31 and now.month == 5:
            okno('Сегодня День\n Российской адвакатуры!')

        if now.day == 1 and now.month == 6:
            okno('Сегодня Международный День\n защиты детей!')

        if now.day == 2 and now.month == 6:
            okno('Сегодня День Спутникового\n мониторинга и навигации!')

        if now.day == 5 and now.month == 6:
            okno('Сегодня День Эколога!')

        if now.day == 6 and now.month == 6:
            okno('Сегодня День Русского языка!')

        if now.day == 8 and now.month == 6:
            okno('Сегодня День\n Социального работника!')

        if now.day == 12 and now.month == 6:
            okno('Сегодня День России!')

        if now.day == 14 and now.month == 6:
            okno('Сегодня День Работников\n миграционной службы!')

        if now.day == 18 and now.month == 6:
            okno('Сегодня День Службы\n военных сообщений!')

        if now.day == 25 and now.month == 6:
            okno('Сегодня День Работника\n статистики!')

        if now.day == 27 and now.month == 6:
            okno('Сегодня День Молодёжи!')

        if now.day == 29 and now.month == 6:
            okno('Сегодня День Партизан\n и подпольщиков!')

        if now.day == 30 and now.month == 6:
            okno('Сегодня День Экономиста!')

        if now.day == 3 and now.month == 7:
            okno('Сегодня День ГИБДД!')

        if now.day == 7 and now.month == 7:
            okno('Сегодня День Победы\n в Чесменском сражении!')

        if now.day == 8 and now.month == 7:
            okno('Сегодня День Семьи, любви и\n верности!')

        if now.day == 10 and now.month == 7:
            okno('Сегодня День Победы\n в Полтавской битве!')

        if now.day == 17 and now.month == 7:
            okno('Сегодня День Этнографа')

        if now.day == 25 and now.month == 7:
            okno('Сегодня День Следователя!')

        if now.day == 28 and now.month == 7:
            okno('Сегодня День Крещения Руси!')

        if now.day == 1 and now.month == 8:
            okno('Сегодня День Тыла ВС РФ!')

        if now.day == 2 and now.month == 8:
            okno('Сегодня День ВДВ!')

        if now.day == 6 and now.month == 8:
            okno('Сегодня День\n Железнодорожных войск!')

        if now.day == 9 and now.month == 8:
            okno('Сегодня День Победы\n в Гангутском сражении!')

        if now.day == 12 and now.month == 8:
            okno('Сегодня День\n Воеенно-воздушных сил!')

        if now.day == 15 and now.month == 8:
            okno('Сегодня День Археолога!')

        if now.day == 18 and now.month == 8:
            okno('Сегодня День Географа!')

        if now.day == 22 and now.month == 8:
            okno('Сегодня День\n Государственного флага РФ!')

        if now.day == 23 and now.month == 8:
            okno('Сегодня День \nПобеды в Курской битве!')

        if now.day == 27 and now.month == 8:
            okno('Сегодня День Кино!')

        if now.day == 31 and now.month == 8:
            okno('Сегодня День\n Ветеринарного Работника!')

        if now.day == 1 and now.month == 9:
            okno('Сегодня День Знаний!')

        if now.day == 2 and now.month == 9:
            okno('Сегодня День \nРоссийской гвардии!')

        if now.day == 3 and now.month == 9:
            okno('Сегодня День\n Окончания Второй Мировой войны!')

        if now.day == 4 and now.month == 9:
            okno('Сегодня День Специалиста\n по ядерному обеспечению!')

        if now.day == 8 and now.month == 9:
            okno('Сегодня День\n Бородинского сражения!')

        if now.day == 9 and now.month == 9:
            okno('Сегодня День Тестировщика!')

        if now.day == 11 and now.month == 9:
            okno('Сегодня День\n Победы у мыса Тендра!')

        if now.day == 13 and now.month == 9:
            okno('Сегодня День Программиста!')

        if now.day == 19 and now.month == 9:
            okno('Сегодня День Оружейника!')

        if now.day == 21 and now.month == 9:
            okno('Сегодня День\n Победы в Куликовской битве!')

        if now.day == 24 and now.month == 9:
            okno('Сегодня День\n Системного аналитика!')

        if now.day == 27 and now.month == 9:
            okno('Сегодня Всемирный\n день Туризма!')

        if now.day == 28 and now.month == 9:
            okno('Сегодня День Работника\n атомной промышленности!')

        if now.day == 30 and now.month == 9:
            okno('Сегодня День Переводчика!')

        if now.day == 1 and now.month == 10:
            okno('Сегодня День Сухопутных войск!')

        if now.day == 4 and now.month == 10:
            okno('Сегодня День Космических войск!')

        if now.day == 5 and now.month == 10:
            okno('Сегодня День Учителя!')

        if now.day == 9 and now.month == 10:
            okno('День Победы в Битве за Кавказ!')

        if now.day == 19 and now.month == 10:
            okno('Сегодня Всероссийский\n день Лицеиста!')

        if now.day == 20 and now.month == 10:
            okno('Сегодня День\n Военного связиста!')

        if now.day == 22 and now.month == 10:
            okno('Сегодня День \nФинансово-экономической службы!')

        if now.day == 23 and now.month == 10:
            okno('Сегодня День Работников рекламы!')

        if now.day == 25 and now.month == 10:
            okno('Сегодня День Таможенника РФ!')

        if now.day == 29 and now.month == 10:
            okno('Сегодня День\n Вневедомственной охраны!')

        if now.day == 30 and now.month == 10:
            okno('Сегодня День Инженера-механика!')

        if now.day == 31 and now.month == 10:
            okno('Сегодня День\n Работника СИЗО и тюрем!')

        if now.day == 1 and now.month == 11:
            okno('Сегодня День\n Судебного пристава РФ!')

        if now.day == 4 and now.month == 11:
            okno('Сегодня День Народного Единства!')

        if now.day == 5 and now.month == 11:
            okno('Сегодня День Военного разведчика!')

        if now.day == 7 and now.month == 11:
            okno('Сегодня Годовщина\n Великой Октябрьской революции!')

        if now.day == 9 and now.month == 11:
            okno('Сегодня День Специального\n отряда быстрого реагирования!')

        if now.day == 10 and now.month == 11:
            okno('Сегодня День Сотрудника ОВД РФ!')

        if now.day == 11 and now.month == 11:
            okno('Сегодня День Экономиста!')

        if now.day == 13 and now.month == 11:
            okno('Сегодня День войск РХБЗ!')

        if now.day == 14 and now.month == 11:
            okno('Сегодня День Социолога!')

        if now.day == 19 and now.month == 11:
            okno('Сегодня Международный Мужской день')

        if now.day == 20 and now.month == 11:
            okno('Сегодня День Работника транспорта!')

        if now.day == 21 and now.month == 11:
            okno('Сегодня День Работника\n налоговых органов РФ!')

        if now.day == 27 and now.month == 11:
            okno('Сегодня День Морской пехоты!')

        if now.day == 30 and now.month == 11:
            okno('Сегодня Международный\n день Защиты информации!')

        if now.day == 1 and now.month == 12:
            okno('Сегодня День Победы \nв Синопском сражении!')

        if now.day == 3 and now.month == 12:
            okno('Сегодня День Неизвестного солдата!')

        if now.day == 5 and now.month == 12:
            okno('Сегодня День Волонтёра!')

        if now.day == 9 and now.month == 12:
            okno('Сегодня День Героев Отечества!')

        if now.day == 12 and now.month == 12:
            okno('Сегодня День Конституции РФ!')

        if now.day == 17 and now.month == 12:
            okno('Сегодня День Ракетных\n войск стратегического назначения!')

        if now.day == 18 and now.month == 12:
            okno('Сегодня День Работников ЗАГС!')

        if now.day == 19 and now.month == 12:
            okno('Сегодня День Работников\n военной контрразведки РФ!')

        if now.day == 20 and now.month == 12:
            okno('Сегодня День Работников\n органов безопасности РФ!')

        if now.day == 22 and now.month == 12:
            okno('Сегодня День Энергетика!')

        if now.day == 24 and now.month == 12:
            okno('Сегодня День Взятия\n турецкой крепости Измаил!')

        if now.day == 27 and now.month == 12:
            okno('Сегодня День Спасателя РФ!')

        if now.day == 31 and now.month == 12:
            okno('Сегодня Последний день ' + str(now.year) + ' года!')


def fallout10():
    global k, kk, flag, speed_push, speed_snar, z
    z = 130

    def returniq():
        window2.destroy()
        window.state('normal')

    flag = True
    k = 0
    kk = 0
    speed_push = 2
    speed_snar = 1

    def zalp():
        global flag, k, kk, speed_snar, xz
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            winsound.Beep(300, 70)
        xz = 100

        def odin():
            global xz
            snaryad.place(x=xz)
            xz += 5

        kk += 1
        lbl5.configure(text=kk)

        for i in range(100, 185):
            window2.after(speed_snar, odin())
            window2.update()

        flag = True
        snaryad.place(x=100)
        a = random.randint(130, 530)
        cel.place(x=530, y=a)

        if (snaryad.winfo_y() - cel.winfo_y()) <= 10 and (snaryad.winfo_y() - cel.winfo_y()) >= -10:
            k += 1
            lbl3.configure(text=k)
            if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
                winsound.Beep(500, 500)
            lbl1.configure(text="Shmalyalka 1.2")

    def vverh_abs():
        global z, flag
        flag = True

        def odin():
            if pushka.winfo_y() > 130:
                global z
                pushka.place(x=30, y=z)
                snaryad.place(x=100, y=z)
                z -= 1

        while pushka.winfo_y() != 130 and flag == True:
            window2.after(speed_push, odin())
            window2.update()

        while flag == True:
            vniz_abs()

    def vniz_abs():
        global z, flag
        flag = True

        def odin():
            if pushka.winfo_y() < 530:
                global z
                pushka.place(x=30, y=z)
                snaryad.place(x=100, y=z)
                z += 1

        while pushka.winfo_y() != 530 and flag == True:
            window2.after(speed_push, odin())
            window2.update()

        while flag == True:
            vverh_abs()

    def stop():
        global flag, k, kk

        def yes():
            global flag, k, kk, z
            flag = False
            z = 130
            a = random.randint(130, 530)
            pushka.place(x=30, y=130)
            snaryad.place(x=100, y=130)
            cel.place(x=530, y=a)
            cel.configure(bg='black')
            was.destroy()
            k = 0
            lbl3.configure(text='0')
            kk = 0
            lbl5.configure(text='0')

        def no():
            was.destroy()

        was = Toplevel()
        was.geometry('250x100+100+100')
        was.resizable(0, 0)
        was.title('Заново')

        lkl = Label(was, text='Заново? Ваш процент попаданий:')
        lkl.place(x=5, y=5)

        if kk == 0:
            s = '0%'
        else:
            s = str(int((k / kk) * 100)) + '%'
        lkl1 = Label(was, text=s)
        lkl1.place(x=200, y=5)

        butn1 = Button(was, text='ДА', bg='#c0ebd6', width=10, command=yes)
        butn1.place(x=10, y=40)

        butn2 = Button(was, text='НЕТ', bg='#ebc0d0', width=10, command=no)
        butn2.place(x=100, y=40)

    def params():
        global speed_push, speed_snar

        def yes():
            global speed_push, speed_snar
            if not ent1.get().isdigit() and not ent.get().isdigit():
                messagebox.showinfo('Ошибка', 'Введите корректные значения!')
            else:
                if not ent.get().isdigit():
                    speed_snar = int(ent1.get())
                elif not ent1.get().isdigit():
                    speed_push = int(ent.get())
                else:
                    speed_push = int(ent.get())
                    speed_snar = int(ent1.get())
                win.destroy()

        def no():
            win.destroy()

        win = Toplevel()
        win.geometry('250x200+100+100')
        win.resizable(0, 0)
        win.title('Параметры')

        loh = Label(win, text='Скорость пушки (мс/y):')
        loh.place(x=5, y=5)

        ent = Entry(win, width=20)
        ent.place(x=10, y=50)

        lah = Label(win, text='Скорость снаяряда (мс/x):')
        lah.place(x=5, y=90)

        ent1 = Entry(win, width=20)
        ent1.place(x=10, y=135)

        btt = Button(win, text='ОК', bg='#c0ebd6', width=8, command=yes)
        btt.place(x=160, y=10)

        btt1 = Button(win, text='Отмена', bg='#ebc0d0', width=8, command=no)
        btt1.place(x=160, y=50)

        ToolTip(win, 'Количество миллисекунд, проходящих между перемещением объекта на единицу x/y.')

    window2 = Toplevel()
    window2.geometry('600x640+50+50')
    window2.title('Shmalyalka 1.2')

    lbl1 = Label(window2, text="Shmalyalka 1.2", font=("Arial Bold", 16), fg="red")
    lbl1.place(x=40, y=20)

    but = Button(window2, text='⇧', font=('Arial Black', 20), bg='#90d69f', command=vverh_abs)
    but.place(x=240, y=20)

    but1 = Button(window2, text='⇩', font=('Arial Black', 20), bg='#90d69f', command=vniz_abs)
    but1.place(x=310, y=20)

    pushka = Label(window2, text='', width=10, bg='#ff0000')
    pushka.place(x=30, y=130)

    snaryad = Label(window2, text='', width=2, bg='#11ff00')
    snaryad.place(x=100, y=130)

    cel = Label(window2, text='', width=2, bg='black')
    a = random.randint(130, 530)
    cel.place(x=530, y=a)

    zalp = Button(window2, text='ЗАЛП', bg="yellow", width=10, font=('Times New Roman', 16), command=zalp)
    zalp.place(x=400, y=20)

    lbl2 = Label(window2, text='Попаданий:')
    lbl2.place(x=30, y=70)

    lbl3 = Label(window2, text='0')
    lbl3.place(x=100, y=70)

    lbl4 = Label(window2, text='Выстрелов:')
    lbl4.place(x=30, y=90)

    lbl5 = Label(window2, text='0')
    lbl5.place(x=100, y=90)

    but2 = Button(window2, text='ЗАНОВО', bg="#d47f7f", width=10, font=('Times New Roman', 16), command=stop)
    but2.place(x=400, y=70)

    but3 = Button(window2, text='Параметры', bg="#9be0df", width=10, font=('Times New Roman', 12), command=params)
    but3.place(x=450, y=570)

    off = Button(window2, text="⌂", font=("Arial Bold", 15), width=2, height=1, bg="black", fg="white",
                 command=returniq)
    off.place(x=0, y=0)
    ToolTip(off, "На главную...")


def fallout11():
    global choose_flag, save_flag

    def returnim():
        window3.destroy()
        window.state('normal')

    global sd
    sd = 'white'

    def recol(pix):
        global sd
        pix.configure(bg=sd)

    def r1():
        recol(a1)

    def r2():
        recol(a2)

    def r3():
        recol(a3)

    def r4():
        recol(a4)

    def r5():
        recol(a5)

    def r6():
        recol(a6)

    def r7():
        recol(a7)

    def r8():
        recol(a8)

    def r9():
        recol(a9)

    def r10():
        recol(a10)

    def r11():
        recol(a11)

    def r12():
        recol(a12)

    def r13():
        recol(a13)

    def r14():
        recol(a14)

    def r15():
        recol(a15)

    def r16():
        recol(a16)

    def r17():
        recol(a17)

    def r18():
        recol(a18)

    def r19():
        recol(a19)

    def r20():
        recol(a20)

    def r21():
        recol(a21)

    def r22():
        recol(a22)

    def r23():
        recol(a23)

    def r24():
        recol(a24)

    def r25():
        recol(a25)

    def r26():
        recol(a26)

    def r27():
        recol(a27)

    def r28():
        recol(a28)

    def r29():
        recol(a29)

    def r30():
        recol(a30)

    def s1():
        recol(b1)

    def s2():
        recol(b2)

    def s3():
        recol(b3)

    def s4():
        recol(b4)

    def s5():
        recol(b5)

    def s6():
        recol(b6)

    def s7():
        recol(b7)

    def s8():
        recol(b8)

    def s9():
        recol(b9)

    def s10():
        recol(b10)

    def s11():
        recol(b11)

    def s12():
        recol(b12)

    def s13():
        recol(b13)

    def s14():
        recol(b14)

    def s15():
        recol(b15)

    def s16():
        recol(b16)

    def s17():
        recol(b17)

    def s18():
        recol(b18)

    def s19():
        recol(b19)

    def s20():
        recol(b20)

    def s21():
        recol(b21)

    def s22():
        recol(b22)

    def s23():
        recol(b23)

    def s24():
        recol(b24)

    def s25():
        recol(b25)

    def s26():
        recol(b26)

    def s27():
        recol(b27)

    def s28():
        recol(b28)

    def s29():
        recol(b29)

    def s30():
        recol(b30)

    def t1():
        recol(c1)

    def t2():
        recol(c2)

    def t3():
        recol(c3)

    def t4():
        recol(c4)

    def t5():
        recol(c5)

    def t6():
        recol(c6)

    def t7():
        recol(c7)

    def t8():
        recol(c8)

    def t9():
        recol(c9)

    def t10():
        recol(c10)

    def t11():
        recol(c11)

    def t12():
        recol(c12)

    def t13():
        recol(c13)

    def t14():
        recol(c14)

    def t15():
        recol(c15)

    def t16():
        recol(c16)

    def t17():
        recol(c17)

    def t18():
        recol(c18)

    def t19():
        recol(c19)

    def t20():
        recol(c20)

    def t21():
        recol(c21)

    def t22():
        recol(c22)

    def t23():
        recol(c23)

    def t24():
        recol(c24)

    def t25():
        recol(c25)

    def t26():
        recol(c26)

    def t27():
        recol(c27)

    def t28():
        recol(c28)

    def t29():
        recol(c29)

    def t30():
        recol(c30)

    def u1():
        recol(d1)

    def u2():
        recol(d2)

    def u3():
        recol(d3)

    def u4():
        recol(d4)

    def u5():
        recol(d5)

    def u6():
        recol(d6)

    def u7():
        recol(d7)

    def u8():
        recol(d8)

    def u9():
        recol(d9)

    def u10():
        recol(d10)

    def u11():
        recol(d11)

    def u12():
        recol(d12)

    def u13():
        recol(d13)

    def u14():
        recol(d14)

    def u15():
        recol(d15)

    def u16():
        recol(d16)

    def u17():
        recol(d17)

    def u18():
        recol(d18)

    def u19():
        recol(d19)

    def u20():
        recol(d20)

    def u21():
        recol(d21)

    def u22():
        recol(d22)

    def u23():
        recol(d23)

    def u24():
        recol(d24)

    def u25():
        recol(d25)

    def u26():
        recol(d26)

    def u27():
        recol(d27)

    def u28():
        recol(d28)

    def u29():
        recol(d29)

    def u30():
        recol(d30)

    def v1():
        recol(e1)

    def v2():
        recol(e2)

    def v3():
        recol(e3)

    def v4():
        recol(e4)

    def v5():
        recol(e5)

    def v6():
        recol(e6)

    def v7():
        recol(e7)

    def v8():
        recol(e8)

    def v9():
        recol(e9)

    def v10():
        recol(e10)

    def v11():
        recol(e11)

    def v12():
        recol(e12)

    def v13():
        recol(e13)

    def v14():
        recol(e14)

    def v15():
        recol(e15)

    def v16():
        recol(e16)

    def v17():
        recol(e17)

    def v18():
        recol(e18)

    def v19():
        recol(e19)

    def v20():
        recol(e20)

    def v21():
        recol(e21)

    def v22():
        recol(e22)

    def v23():
        recol(e23)

    def v24():
        recol(e24)

    def v25():
        recol(e25)

    def v26():
        recol(e26)

    def v27():
        recol(e27)

    def v28():
        recol(e28)

    def v29():
        recol(e29)

    def v30():
        recol(e30)

    def w1():
        recol(f1)

    def w2():
        recol(f2)

    def w3():
        recol(f3)

    def w4():
        recol(f4)

    def w5():
        recol(f5)

    def w6():
        recol(f6)

    def w7():
        recol(f7)

    def w8():
        recol(f8)

    def w9():
        recol(f9)

    def w10():
        recol(f10)

    def w11():
        recol(f11)

    def w12():
        recol(f12)

    def w13():
        recol(f13)

    def w14():
        recol(f14)

    def w15():
        recol(f15)

    def w16():
        recol(f16)

    def w17():
        recol(f17)

    def w18():
        recol(f18)

    def w19():
        recol(f19)

    def w20():
        recol(f20)

    def w21():
        recol(f21)

    def w22():
        recol(f22)

    def w23():
        recol(f23)

    def w24():
        recol(f24)

    def w25():
        recol(f25)

    def w26():
        recol(f26)

    def w27():
        recol(f27)

    def w28():
        recol(f28)

    def w29():
        recol(f29)

    def w30():
        recol(f30)

    def x1():
        recol(g1)

    def x2():
        recol(g2)

    def x3():
        recol(g3)

    def x4():
        recol(g4)

    def x5():
        recol(g5)

    def x6():
        recol(g6)

    def x7():
        recol(g7)

    def x8():
        recol(g8)

    def x9():
        recol(g9)

    def x10():
        recol(g10)

    def x11():
        recol(g11)

    def x12():
        recol(g12)

    def x13():
        recol(g13)

    def x14():
        recol(g14)

    def x15():
        recol(g15)

    def x16():
        recol(g16)

    def x17():
        recol(g17)

    def x18():
        recol(g18)

    def x19():
        recol(g19)

    def x20():
        recol(g20)

    def x21():
        recol(g21)

    def x22():
        recol(g22)

    def x23():
        recol(g23)

    def x24():
        recol(g24)

    def x25():
        recol(g25)

    def x26():
        recol(g26)

    def x27():
        recol(g27)

    def x28():
        recol(g28)

    def x29():
        recol(g29)

    def x30():
        recol(g30)

    def y1():
        recol(h1)

    def y2():
        recol(h2)

    def y3():
        recol(h3)

    def y4():
        recol(h4)

    def y5():
        recol(h5)

    def y6():
        recol(h6)

    def y7():
        recol(h7)

    def y8():
        recol(h8)

    def y9():
        recol(h9)

    def y10():
        recol(h10)

    def y11():
        recol(h11)

    def y12():
        recol(h12)

    def y13():
        recol(h13)

    def y14():
        recol(h14)

    def y15():
        recol(h15)

    def y16():
        recol(h16)

    def y17():
        recol(h17)

    def y18():
        recol(h18)

    def y19():
        recol(h19)

    def y20():
        recol(h20)

    def y21():
        recol(h21)

    def y22():
        recol(h22)

    def y23():
        recol(h23)

    def y24():
        recol(h24)

    def y25():
        recol(h25)

    def y26():
        recol(h26)

    def y27():
        recol(h27)

    def y28():
        recol(h28)

    def y29():
        recol(h29)

    def y30():
        recol(h30)

    choose_flag = True

    def colorch():
        global sd, choose_flag
        b = colorchooser.askcolor()
        sd = b[1]
        rec.configure(bg=sd)
        choose_flag = True

    def Lastik():
        global sd, choose_flag, now_color
        if choose_flag:
            now_color = rec['background']
            sd = 'white'
            rec.configure(bg='white')
            choose_flag = False
        else:
            sd = now_color
            rec.configure(bg=now_color)
            choose_flag = True

    def save():

        global save_flag, file_name

        def go():
            c = []
            for i in range(len(a)):
                c.append(a[i]['background'])
            gf = str(ect.get())
            np.save('C:/MihaSoft Files/P Files/' + gf, c)
            wind1.destroy()

        def go_1():

            c = []
            for i in range(len(a)):
                c.append(a[i]['background'])
            np.save(file_name, c)
            wind1.destroy()

        def CloseSave():
            wind1.destroy()

        if save_flag:
            wind1 = Toplevel()
            wind1.geometry('300x100+70+70')
            wind1.resizable(0, 0)
            wind1.title('Сохранение')

            lcl = Label(wind1, text='Введите название файла...')
            lcl.place(x=5, y=5)

            ect = Entry(wind1, width=25)
            ect.place(x=10, y=45)

            but4 = Button(wind1, text='Сохранить', width=10, bg='#93e6a8', command=go)
            but4.place(x=200, y=23)

            p_close_button = Button(wind1, text='Отмена', width=10, bg='#b8b8b8', command=CloseSave)
            p_close_button.place(x=200, y=60)

        else:
            wind1 = Toplevel()
            wind1.geometry('300x100+70+70')
            wind1.resizable(0, 0)
            wind1.title('Сохранение изменений')

            lcl = Label(wind1, text='Сохранить изменения в файле\n' + file_name + '?')
            lcl.place(x=5, y=5)

            but4 = Button(wind1, text='Сохранить', width=10, bg='#93e6a8', command=go_1)
            but4.place(x=100, y=60)

            p_close_button = Button(wind1, text='Отмена', width=10, bg='#b8b8b8', command=CloseSave)
            p_close_button.place(x=200, y=60)

    def opn():
        def gg():
            global file_name, save_flag
            ak = str(ect.get())
            ka = np.load('C:/MihaSoft Files/P Files/' + ak)
            file_name = 'C:/MihaSoft Files/P Files/' + ak
            for i in range(len(a)):
                a[i].configure(bg=ka[i])
            wind2.destroy()
            save_flag = False

        def CloseOpn():
            wind2.destroy()

        xx = os.listdir('C:/MihaSoft Files/P Files')
        wind2 = Toplevel()
        wind2.geometry('300x100+70+70')
        wind2.resizable(0, 0)
        wind2.title('Открыть')

        lcl = Label(wind2, text='Выберите файл...')
        lcl.place(x=5, y=5)

        ect = ttk.Combobox(wind2, values=xx, state='readonly')
        ect.place(x=10, y=45)

        but4 = Button(wind2, text='Открыть', width=10, bg='#93e6a8', command=gg)
        but4.place(x=200, y=23)

        p_close_button = Button(wind2, text='Отмена', width=10, bg='#b8b8b8', command=CloseOpn)
        p_close_button.place(x=200, y=60)

    def Clean():
        for i in range(len(a)):
            a[i].configure(bg='white')

    def New():
        global save_flag, file_name
        save_flag = True
        file_name = None
        Clean()

    a = []
    save_flag = True
    file_name = None

    if not os.path.exists('C:/MihaSoft Files/P Files'):
        os.mkdir('C:/MihaSoft Files/P Files')

    window3 = Toplevel()
    window3.geometry('550x300+50+50')
    window3.title('Paint 1.1')

    lbl1 = Label(window3, text="Paint 1.1", font=("Arial Bold", 16), fg="red")
    lbl1.place(x=50, y=10)

    new_button = Button(window3, text='Новый рисунок', bg='#b8b8b8', command=New)
    new_button.place(x=180, y=10)

    clean_button = Button(window3, text='Очистить', bg='#b8b8b8', command=Clean)
    clean_button.place(x=285, y=10)

    lastik = Button(window3, text='Ластик', bg='#b8b8b8', command=Lastik)
    lastik.place(x=355, y=10)
    ToolTip(lastik, 'Нажмите повтороно для возвращения к последнему цвету...')

    rec = Button(window3, text='Выбрать цвет', bg='white', command=colorch)
    rec.place(x=415, y=10)

    a1 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r1)
    a1.place(x=50, y=50)
    a.append(a1)

    a2 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r2)
    a2.place(x=65, y=50)
    a.append(a2)

    a3 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r3)
    a3.place(x=80, y=50)
    a.append(a3)

    a4 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r4)
    a4.place(x=95, y=50)
    a.append(a4)

    a5 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r5)
    a5.place(x=110, y=50)
    a.append(a5)

    a6 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r6)
    a6.place(x=125, y=50)
    a.append(a6)

    a7 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r7)
    a7.place(x=140, y=50)
    a.append(a7)

    a8 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r8)
    a8.place(x=155, y=50)
    a.append(a8)

    a9 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r9)
    a9.place(x=170, y=50)
    a.append(a9)

    a10 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r10)
    a10.place(x=185, y=50)
    a.append(a10)

    a11 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r11)
    a11.place(x=200, y=50)
    a.append(a11)

    a12 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r12)
    a12.place(x=215, y=50)
    a.append(a12)

    a13 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r13)
    a13.place(x=230, y=50)
    a.append(a13)

    a14 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r14)
    a14.place(x=245, y=50)
    a.append(a14)

    a15 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r15)
    a15.place(x=260, y=50)
    a.append(a15)

    a16 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r16)
    a16.place(x=275, y=50)
    a.append(a16)

    a17 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r17)
    a17.place(x=290, y=50)
    a.append(a17)

    a18 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r18)
    a18.place(x=305, y=50)
    a.append(a18)

    a19 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r19)
    a19.place(x=320, y=50)
    a.append(a19)

    a20 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r20)
    a20.place(x=335, y=50)
    a.append(a20)

    a21 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r21)
    a21.place(x=350, y=50)
    a.append(a21)

    a22 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r22)
    a22.place(x=365, y=50)
    a.append(a22)

    a23 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r23)
    a23.place(x=380, y=50)
    a.append(a23)

    a24 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r24)
    a24.place(x=395, y=50)
    a.append(a24)

    a25 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r25)
    a25.place(x=410, y=50)
    a.append(a25)

    a26 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r26)
    a26.place(x=425, y=50)
    a.append(a26)

    a27 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r27)
    a27.place(x=440, y=50)
    a.append(a27)

    a28 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r28)
    a28.place(x=455, y=50)
    a.append(a28)

    a29 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r29)
    a29.place(x=470, y=50)
    a.append(a29)

    a30 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r30)
    a30.place(x=485, y=50)
    a.append(a30)

    b1 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s1)
    b1.place(x=50, y=68)
    a.append(b1)

    b2 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s2)
    b2.place(x=65, y=68)
    a.append(b2)

    b3 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s3)
    b3.place(x=80, y=68)
    a.append(b3)

    b4 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s4)
    b4.place(x=95, y=68)
    a.append(b4)

    b5 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s5)
    b5.place(x=110, y=68)
    a.append(b5)

    b6 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s6)
    b6.place(x=125, y=68)
    a.append(b6)

    b7 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s7)
    b7.place(x=140, y=68)
    a.append(b7)

    b8 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s8)
    b8.place(x=155, y=68)
    a.append(b8)

    b9 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s9)
    b9.place(x=170, y=68)
    a.append(b9)

    b10 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s10)
    b10.place(x=185, y=68)
    a.append(b10)

    b11 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s11)
    b11.place(x=200, y=68)
    a.append(b11)

    b12 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s12)
    b12.place(x=215, y=68)
    a.append(b12)

    b13 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s13)
    b13.place(x=230, y=68)
    a.append(b13)

    b14 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s14)
    b14.place(x=245, y=68)
    a.append(b14)

    b15 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s15)
    b15.place(x=260, y=68)
    a.append(b15)

    b16 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s16)
    b16.place(x=275, y=68)
    a.append(b16)

    b17 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s17)
    b17.place(x=290, y=68)
    a.append(b17)

    b18 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s18)
    b18.place(x=305, y=68)
    a.append(b18)

    b19 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s19)
    b19.place(x=320, y=68)
    a.append(b19)

    b20 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s20)
    b20.place(x=335, y=68)
    a.append(b20)

    b21 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s21)
    b21.place(x=350, y=68)
    a.append(b21)

    b22 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s22)
    b22.place(x=365, y=68)
    a.append(b22)

    b23 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s23)
    b23.place(x=380, y=68)
    a.append(b23)

    b24 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s24)
    b24.place(x=395, y=68)
    a.append(b24)

    b25 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s25)
    b25.place(x=410, y=68)
    a.append(b25)

    b26 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s26)
    b26.place(x=425, y=68)
    a.append(b26)

    b27 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s27)
    b27.place(x=440, y=68)
    a.append(b27)

    b28 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s28)
    b28.place(x=455, y=68)
    a.append(b28)

    b29 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s29)
    b29.place(x=470, y=68)
    a.append(b29)

    b30 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s30)
    b30.place(x=485, y=68)
    a.append(b30)

    c1 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t1)
    c1.place(x=50, y=86)
    a.append(c1)

    c2 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t2)
    c2.place(x=65, y=86)
    a.append(c2)

    c3 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t3)
    c3.place(x=80, y=86)
    a.append(c3)

    c4 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t4)
    c4.place(x=95, y=86)
    a.append(c4)

    c5 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t5)
    c5.place(x=110, y=86)
    a.append(c5)

    c6 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t6)
    c6.place(x=125, y=86)
    a.append(c6)

    c7 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t7)
    c7.place(x=140, y=86)
    a.append(c7)

    c8 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t8)
    c8.place(x=155, y=86)
    a.append(c8)

    c9 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t9)
    c9.place(x=170, y=86)
    a.append(c9)

    c10 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t10)
    c10.place(x=185, y=86)
    a.append(c10)

    c11 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t11)
    c11.place(x=200, y=86)
    a.append(c11)

    c12 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t12)
    c12.place(x=215, y=86)
    a.append(c12)

    c13 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t13)
    c13.place(x=230, y=86)
    a.append(c13)

    c14 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t14)
    c14.place(x=245, y=86)
    a.append(c14)

    c15 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t15)
    c15.place(x=260, y=86)
    a.append(c15)

    c16 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t16)
    c16.place(x=275, y=86)
    a.append(c16)

    c17 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t17)
    c17.place(x=290, y=86)
    a.append(c17)

    c18 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t18)
    c18.place(x=305, y=86)
    a.append(c18)

    c19 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t19)
    c19.place(x=320, y=86)
    a.append(c19)

    c20 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t20)
    c20.place(x=335, y=86)
    a.append(c20)

    c21 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t21)
    c21.place(x=350, y=86)
    a.append(c21)

    c22 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t22)
    c22.place(x=365, y=86)
    a.append(c22)

    c23 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t23)
    c23.place(x=380, y=86)
    a.append(c23)

    c24 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t24)
    c24.place(x=395, y=86)
    a.append(c24)

    c25 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t25)
    c25.place(x=410, y=86)
    a.append(c25)

    c26 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t26)
    c26.place(x=425, y=86)
    a.append(c26)

    c27 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t27)
    c27.place(x=440, y=86)
    a.append(c27)

    c28 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t28)
    c28.place(x=455, y=86)
    a.append(c28)

    c29 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t29)
    c29.place(x=470, y=86)
    a.append(c29)

    c30 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t30)
    c30.place(x=485, y=86)
    a.append(c30)

    d1 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u1)
    d1.place(x=50, y=104)
    a.append(d1)

    d2 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u2)
    d2.place(x=65, y=104)
    a.append(d2)

    d3 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u3)
    d3.place(x=80, y=104)
    a.append(d3)

    d4 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u4)
    d4.place(x=95, y=104)
    a.append(d4)

    d5 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u5)
    d5.place(x=110, y=104)
    a.append(d5)

    d6 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u6)
    d6.place(x=125, y=104)
    a.append(d6)

    d7 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u7)
    d7.place(x=140, y=104)
    a.append(d7)

    d8 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u8)
    d8.place(x=155, y=104)
    a.append(d8)

    d9 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u9)
    d9.place(x=170, y=104)
    a.append(d9)

    d10 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u10)
    d10.place(x=185, y=104)
    a.append(d10)

    d11 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u11)
    d11.place(x=200, y=104)
    a.append(d11)

    d12 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u12)
    d12.place(x=215, y=104)
    a.append(d12)

    d13 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u13)
    d13.place(x=230, y=104)
    a.append(d13)

    d14 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u14)
    d14.place(x=245, y=104)
    a.append(d14)

    d15 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u15)
    d15.place(x=260, y=104)
    a.append(d15)

    d16 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u16)
    d16.place(x=275, y=104)
    a.append(d16)

    d17 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u17)
    d17.place(x=290, y=104)
    a.append(d17)

    d18 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u18)
    d18.place(x=305, y=104)
    a.append(d18)

    d19 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u19)
    d19.place(x=320, y=104)
    a.append(d19)

    d20 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u20)
    d20.place(x=335, y=104)
    a.append(d20)

    d21 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u21)
    d21.place(x=350, y=104)
    a.append(d21)

    d22 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u22)
    d22.place(x=365, y=104)
    a.append(d22)

    d23 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u23)
    d23.place(x=380, y=104)
    a.append(d23)

    d24 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u24)
    d24.place(x=395, y=104)
    a.append(d24)

    d25 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u25)
    d25.place(x=410, y=104)
    a.append(d25)

    d26 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u26)
    d26.place(x=425, y=104)
    a.append(d26)

    d27 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u27)
    d27.place(x=440, y=104)
    a.append(d27)

    d28 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u28)
    d28.place(x=455, y=104)
    a.append(d28)

    d29 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u29)
    d29.place(x=470, y=104)
    a.append(d29)

    d30 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u30)
    d30.place(x=485, y=104)
    a.append(d30)

    e1 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v1)
    e1.place(x=50, y=122)
    a.append(e1)

    e2 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v2)
    e2.place(x=65, y=122)
    a.append(e2)

    e3 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v3)
    e3.place(x=80, y=122)
    a.append(e3)

    e4 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v4)
    e4.place(x=95, y=122)
    a.append(e4)

    e5 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v5)
    e5.place(x=110, y=122)
    a.append(e5)

    e6 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v6)
    e6.place(x=125, y=122)
    a.append(e6)

    e7 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v7)
    e7.place(x=140, y=122)
    a.append(e7)

    e8 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v8)
    e8.place(x=155, y=122)
    a.append(e8)

    e9 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v9)
    e9.place(x=170, y=122)
    a.append(e9)

    e10 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v10)
    e10.place(x=185, y=122)
    a.append(e10)

    e11 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v11)
    e11.place(x=200, y=122)
    a.append(e11)

    e12 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v12)
    e12.place(x=215, y=122)
    a.append(e12)

    e13 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v13)
    e13.place(x=230, y=122)
    a.append(e13)

    e14 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v14)
    e14.place(x=245, y=122)
    a.append(e14)

    e15 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v15)
    e15.place(x=260, y=122)
    a.append(e15)

    e16 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v16)
    e16.place(x=275, y=122)
    a.append(e16)

    e17 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v17)
    e17.place(x=290, y=122)
    a.append(e17)

    e18 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v18)
    e18.place(x=305, y=122)
    a.append(e18)

    e19 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v19)
    e19.place(x=320, y=122)
    a.append(e19)

    e20 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v20)
    e20.place(x=335, y=122)
    a.append(e20)

    e21 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v21)
    e21.place(x=350, y=122)
    a.append(e21)

    e22 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v22)
    e22.place(x=365, y=122)
    a.append(e22)

    e23 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v23)
    e23.place(x=380, y=122)
    a.append(e23)

    e24 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v24)
    e24.place(x=395, y=122)
    a.append(e24)

    e25 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v25)
    e25.place(x=410, y=122)
    a.append(e25)

    e26 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v26)
    e26.place(x=425, y=122)
    a.append(e26)

    e27 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v27)
    e27.place(x=440, y=122)
    a.append(e27)

    e28 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v28)
    e28.place(x=455, y=122)
    a.append(e28)

    e29 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v29)
    e29.place(x=470, y=122)
    a.append(e29)

    e30 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v30)
    e30.place(x=485, y=122)
    a.append(e30)

    f1 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w1)
    f1.place(x=50, y=140)
    a.append(f1)

    f2 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w2)
    f2.place(x=65, y=140)
    a.append(f2)

    f3 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w3)
    f3.place(x=80, y=140)
    a.append(f3)

    f4 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w4)
    f4.place(x=95, y=140)
    a.append(f4)

    f5 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w5)
    f5.place(x=110, y=140)
    a.append(f5)

    f6 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w6)
    f6.place(x=125, y=140)
    a.append(f6)

    f7 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w7)
    f7.place(x=140, y=140)
    a.append(f7)

    f8 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w8)
    f8.place(x=155, y=140)
    a.append(f8)

    f9 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w9)
    f9.place(x=170, y=140)
    a.append(f9)

    f10 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w10)
    f10.place(x=185, y=140)
    a.append(f10)

    f11 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w11)
    f11.place(x=200, y=140)
    a.append(f11)

    f12 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w12)
    f12.place(x=215, y=140)
    a.append(f12)

    f13 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w13)
    f13.place(x=230, y=140)
    a.append(f13)

    f14 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w14)
    f14.place(x=245, y=140)
    a.append(f14)

    f15 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w15)
    f15.place(x=260, y=140)
    a.append(f15)

    f16 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w16)
    f16.place(x=275, y=140)
    a.append(f16)

    f17 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w17)
    f17.place(x=290, y=140)
    a.append(f17)

    f18 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w18)
    f18.place(x=305, y=140)
    a.append(f18)

    f19 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w19)
    f19.place(x=320, y=140)
    a.append(f19)

    f20 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w20)
    f20.place(x=335, y=140)
    a.append(f20)

    f21 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w21)
    f21.place(x=350, y=140)
    a.append(f21)

    f22 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w22)
    f22.place(x=365, y=140)
    a.append(f22)

    f23 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w23)
    f23.place(x=380, y=140)
    a.append(f23)

    f24 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w24)
    f24.place(x=395, y=140)
    a.append(f24)

    f25 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w25)
    f25.place(x=410, y=140)
    a.append(f25)

    f26 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w26)
    f26.place(x=425, y=140)
    a.append(f26)

    f27 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w27)
    f27.place(x=440, y=140)
    a.append(f27)

    f28 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w28)
    f28.place(x=455, y=140)
    a.append(f28)

    f29 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w29)
    f29.place(x=470, y=140)
    a.append(f29)

    f30 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w30)
    f30.place(x=485, y=140)
    a.append(f30)

    g1 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x1)
    g1.place(x=50, y=158)
    a.append(g1)

    g2 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x2)
    g2.place(x=65, y=158)
    a.append(g2)

    g3 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x3)
    g3.place(x=80, y=158)
    a.append(g3)

    g4 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x4)
    g4.place(x=95, y=158)
    a.append(g4)

    g5 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x5)
    g5.place(x=110, y=158)
    a.append(g5)

    g6 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x6)
    g6.place(x=125, y=158)
    a.append(g6)

    g7 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x7)
    g7.place(x=140, y=158)
    a.append(g7)

    g8 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x8)
    g8.place(x=155, y=158)
    a.append(g8)

    g9 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x9)
    g9.place(x=170, y=158)
    a.append(g9)

    g10 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x10)
    g10.place(x=185, y=158)
    a.append(g10)

    g11 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x11)
    g11.place(x=200, y=158)
    a.append(g11)

    g12 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x12)
    g12.place(x=215, y=158)
    a.append(g12)

    g13 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x13)
    g13.place(x=230, y=158)
    a.append(g13)

    g14 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x14)
    g14.place(x=245, y=158)
    a.append(g14)

    g15 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x15)
    g15.place(x=260, y=158)
    a.append(g15)

    g16 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x16)
    g16.place(x=275, y=158)
    a.append(g16)

    g17 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x17)
    g17.place(x=290, y=158)
    a.append(g17)

    g18 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x18)
    g18.place(x=305, y=158)
    a.append(g18)

    g19 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x19)
    g19.place(x=320, y=158)
    a.append(g19)

    g20 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x20)
    g20.place(x=335, y=158)
    a.append(g20)

    g21 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x21)
    g21.place(x=350, y=158)
    a.append(g21)

    g22 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x22)
    g22.place(x=365, y=158)
    a.append(g22)

    g23 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x23)
    g23.place(x=380, y=158)
    a.append(g23)

    g24 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x24)
    g24.place(x=395, y=158)
    a.append(g24)

    g25 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x25)
    g25.place(x=410, y=158)
    a.append(g25)

    g26 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x26)
    g26.place(x=425, y=158)
    a.append(g26)

    g27 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x27)
    g27.place(x=440, y=158)
    a.append(g27)

    g28 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x28)
    g28.place(x=455, y=158)
    a.append(g28)

    g29 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x29)
    g29.place(x=470, y=158)
    a.append(g29)

    g30 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x30)
    g30.place(x=485, y=158)
    a.append(g30)

    h1 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y1)
    h1.place(x=50, y=176)
    a.append(h1)

    h2 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y2)
    h2.place(x=65, y=176)
    a.append(h2)

    h3 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y3)
    h3.place(x=80, y=176)
    a.append(h3)

    h4 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y4)
    h4.place(x=95, y=176)
    a.append(h4)

    h5 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y5)
    h5.place(x=110, y=176)
    a.append(h5)

    h6 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y6)
    h6.place(x=125, y=176)
    a.append(h6)

    h7 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y7)
    h7.place(x=140, y=176)
    a.append(h7)

    h8 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y8)
    h8.place(x=155, y=176)
    a.append(h8)

    h9 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y9)
    h9.place(x=170, y=176)
    a.append(h9)

    h10 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y10)
    h10.place(x=185, y=176)
    a.append(h10)

    h11 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y11)
    h11.place(x=200, y=176)
    a.append(h11)

    h12 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y12)
    h12.place(x=215, y=176)
    a.append(h12)

    h13 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y13)
    h13.place(x=230, y=176)
    a.append(h13)

    h14 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y14)
    h14.place(x=245, y=176)
    a.append(h14)

    h15 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y15)
    h15.place(x=260, y=176)
    a.append(h15)

    h16 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y16)
    h16.place(x=275, y=176)
    a.append(h16)

    h17 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y17)
    h17.place(x=290, y=176)
    a.append(h17)

    h18 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y18)
    h18.place(x=305, y=176)
    a.append(h18)

    h19 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y19)
    h19.place(x=320, y=176)
    a.append(h19)

    h20 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y20)
    h20.place(x=335, y=176)
    a.append(h20)

    h21 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y21)
    h21.place(x=350, y=176)
    a.append(h21)

    h22 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y22)
    h22.place(x=365, y=176)
    a.append(h22)

    h23 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y23)
    h23.place(x=380, y=176)
    a.append(h23)

    h24 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y24)
    h24.place(x=395, y=176)
    a.append(h24)

    h25 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y25)
    h25.place(x=410, y=176)
    a.append(h25)

    h26 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y26)
    h26.place(x=425, y=176)
    a.append(h26)

    h27 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y27)
    h27.place(x=440, y=176)
    a.append(h27)

    h28 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y28)
    h28.place(x=455, y=176)
    a.append(h28)

    h29 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y29)
    h29.place(x=470, y=176)
    a.append(h29)

    h30 = Button(window3, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y30)
    h30.place(x=485, y=176)
    a.append(h30)

    but = Button(window3, text='Сохранить', bg="#9be0b4", width=10, font=('Times New Roman', 16), command=save)
    but.place(x=50, y=220)

    but1 = Button(window3, text='Открыть', bg="#e0dc9b", width=10, font=('Times New Roman', 16), command=opn)
    but1.place(x=370, y=220)

    off = Button(window3, text="⌂", font=("Arial Bold", 15), width=2, height=1, bg="black", fg="white",
                 command=returnim)
    off.place(x=0, y=0)
    ToolTip(off, "На главную...")


def Saper():
    def Return():
        Destroing()
        home()

    def Destroing():
        s_title.destroy()
        restart_button.destroy()
        info_label.destroy()
        off.destroy()
        s_box_a1.destroy()
        s_box_a2.destroy()
        s_box_a3.destroy()
        s_box_a4.destroy()
        s_box_a5.destroy()
        s_box_b1.destroy()
        s_box_b2.destroy()
        s_box_b3.destroy()
        s_box_b4.destroy()
        s_box_b5.destroy()
        s_box_c1.destroy()
        s_box_c2.destroy()
        s_box_c3.destroy()
        s_box_c4.destroy()
        s_box_c5.destroy()
        s_box_d1.destroy()
        s_box_d2.destroy()
        s_box_d3.destroy()
        s_box_d4.destroy()
        s_box_d5.destroy()
        s_box_e1.destroy()
        s_box_e2.destroy()
        s_box_e3.destroy()
        s_box_e4.destroy()
        s_box_e5.destroy()
        stat_button.destroy()

    def NewGame():
        global s_flag_a1, s_flag_a2, s_flag_a3, s_flag_a4, s_flag_a5, s_flag_b1, s_flag_b2, s_flag_b3, s_flag_b4, s_flag_b5, s_flag_c1, s_flag_c2, s_flag_c3, s_flag_c4, s_flag_c5, s_flag_d1, s_flag_d2, s_flag_d3, s_flag_d4, s_flag_d5, s_flag_e1, s_flag_e2, s_flag_e3, s_flag_e4, s_flag_e5, s_bomb_list, s_box_list, s_global_flag
        s_box_list = [s_box_a1, s_box_a2, s_box_a3, s_box_a4, s_box_a5, s_box_b1, s_box_b2, s_box_b3, s_box_b4,
                      s_box_b5, s_box_c1, s_box_c2, s_box_c3, s_box_c4, s_box_c5, s_box_d1, s_box_d2, s_box_d3,
                      s_box_d4, s_box_d5, s_box_e1, s_box_e2, s_box_e3, s_box_e4, s_box_e5]
        s_flags_list = [False, False, False, False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False, False, False]
        s_numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        s_bomb_list = []
        for i in range(1, 6):
            s_bomb_loc = random.choice(s_numbers_list)
            s_numbers_list.remove(s_bomb_loc)
            s_flags_list[s_bomb_loc] = True
            s_bomb_list.append(s_box_list[s_bomb_loc])
        for i in range(len(s_bomb_list)):
            s_box_list.remove(s_bomb_list[i])
        s_global_flag = True
        s_flag_a1, s_flag_a2, s_flag_a3, s_flag_a4, s_flag_a5, s_flag_b1, s_flag_b2, s_flag_b3, s_flag_b4, s_flag_b5, s_flag_c1, s_flag_c2, s_flag_c3, s_flag_c4, s_flag_c5, s_flag_d1, s_flag_d2, s_flag_d3, s_flag_d4, s_flag_d5, s_flag_e1, s_flag_e2, s_flag_e3, s_flag_e4, s_flag_e5 = \
            s_flags_list[0], s_flags_list[1], s_flags_list[2], s_flags_list[3], s_flags_list[4], s_flags_list[5], \
            s_flags_list[6], s_flags_list[7], s_flags_list[8], s_flags_list[9], s_flags_list[10], s_flags_list[11], \
            s_flags_list[12], s_flags_list[13], s_flags_list[14], s_flags_list[15], s_flags_list[16], s_flags_list[17], \
            s_flags_list[18], s_flags_list[19], s_flags_list[20], s_flags_list[21], s_flags_list[22], s_flags_list[23], \
            s_flags_list[24]

    def GameOver():
        global s_bomb_list, s_box_list, s_global_flag
        if s_global_flag:
            for i in range(len(s_bomb_list)):
                s_bomb_list[i].configure(bg='red')
            for i in range(len(s_box_list)):
                s_box_list[i].configure(bg='white')
            info_label.configure(text='Вы проиграли!', fg='red')
            s_global_flag = False
            stat_list = np.load('C:/MihaSoft Files/SaperStat.npy')
            numb_of_games = stat_list[0] + 1
            new_stat_list = [numb_of_games, stat_list[1]]
            np.save('C:/MihaSoft Files/SaperStat', new_stat_list)
            if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
                winsound.Beep(1000, 500)

    def CheckWin():
        global s_box_list, s_bomb_list, s_global_flag
        k = 0
        for i in range(len(s_box_list)):
            if s_box_list[i]['background'] != 'white':
                k += 1
        if k == 0:
            for i in range(len(s_box_list)):
                s_box_list[i].configure(bg='white')
            for i in range(len(s_bomb_list)):
                s_bomb_list[i].configure(bg='green')
            s_global_flag = False
            info_label.configure(text='Вы выиграли!', fg='green')
            stat_list = np.load('C:/MihaSoft Files/SaperStat.npy')
            numb_of_games = stat_list[0] + 1
            numb_of_wins = stat_list[1] + 1
            new_stat_list = [numb_of_games, numb_of_wins]
            np.save('C:/MihaSoft Files/SaperStat', new_stat_list)
            if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
                winsound.Beep(500, 400)
                window.after(30, winsound.Beep(500, 400))
                window.after(30, winsound.Beep(500, 400))

    def RestartGame():
        NewGame()
        info_label.configure(text='')
        s_box_list_2 = [s_box_a1, s_box_a2, s_box_a3, s_box_a4, s_box_a5, s_box_b1, s_box_b2, s_box_b3, s_box_b4,
                        s_box_b5,
                        s_box_c1, s_box_c2, s_box_c3, s_box_c4, s_box_c5, s_box_d1, s_box_d2, s_box_d3, s_box_d4,
                        s_box_d5,
                        s_box_e1, s_box_e2, s_box_e3, s_box_e4, s_box_e5]
        for i in range(len(s_box_list_2)):
            s_box_list_2[i].configure(bg='#7a9cd6', text='')

    def type_1(box, this_flag, flag_1, flag_2, flag_3):
        global s_flag_a1, s_flag_a2, s_flag_a3, s_flag_a4, s_flag_a5, s_flag_b1, s_flag_b2, s_flag_b3, s_flag_b4, s_flag_b5, s_flag_c1, s_flag_c2, s_flag_c3, s_flag_c4, s_flag_c5, s_flag_d1, s_flag_d2, s_flag_d3, s_flag_d4, s_flag_d5, s_flag_e1, s_flag_e2, s_flag_e3, s_flag_e4, s_flag_e5, s_global_flag
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            winsound.Beep(300, 50)
        if s_global_flag:
            if not this_flag:
                k = 0
                listok = [flag_1, flag_2, flag_3]
                for i in range(len(listok)):
                    if listok[i]:
                        k += 1
                box.configure(text=k, bg='white')
                CheckWin()
            else:
                GameOver()

    def on_a1():
        type_1(s_box_a1, s_flag_a1, s_flag_a2, s_flag_b2, s_flag_b1)

    def on_a5():
        type_1(s_box_a5, s_flag_a5, s_flag_a4, s_flag_b4, s_flag_b5)

    def on_e1():
        type_1(s_box_e1, s_flag_e1, s_flag_d1, s_flag_d2, s_flag_e2)

    def on_e5():
        type_1(s_box_e5, s_flag_e5, s_flag_e4, s_flag_d4, s_flag_d5)

    def type_2(box, this_flag, flag_1, flag_2, flag_3, flag_4, flag_5):
        global s_flag_a1, s_flag_a2, s_flag_a3, s_flag_a4, s_flag_a5, s_flag_b1, s_flag_b2, s_flag_b3, s_flag_b4, s_flag_b5, s_flag_c1, s_flag_c2, s_flag_c3, s_flag_c4, s_flag_c5, s_flag_d1, s_flag_d2, s_flag_d3, s_flag_d4, s_flag_d5, s_flag_e1, s_flag_e2, s_flag_e3, s_flag_e4, s_flag_e5, s_global_flag
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            winsound.Beep(300, 50)
        if s_global_flag:
            if not this_flag:
                k = 0
                listok = [flag_1, flag_2, flag_3, flag_4, flag_5]
                for i in range(len(listok)):
                    if listok[i]:
                        k += 1
                box.configure(text=k, bg='white')
                CheckWin()
            else:
                GameOver()

    def on_a2():
        type_2(s_box_a2, s_flag_a2, s_flag_a1, s_flag_b1, s_flag_b2, s_flag_b3, s_flag_a3)

    def on_a3():
        type_2(s_box_a3, s_flag_a3, s_flag_a2, s_flag_b2, s_flag_b3, s_flag_b4, s_flag_a4)

    def on_a4():
        type_2(s_box_a4, s_flag_a4, s_flag_a3, s_flag_b3, s_flag_b4, s_flag_b5, s_flag_a5)

    def on_b1():
        type_2(s_box_b1, s_flag_b1, s_flag_a1, s_flag_a2, s_flag_b2, s_flag_c2, s_flag_c1)

    def on_c1():
        type_2(s_box_c1, s_flag_c1, s_flag_b1, s_flag_b2, s_flag_c2, s_flag_d2, s_flag_d1)

    def on_d1():
        type_2(s_box_d1, s_flag_d1, s_flag_c1, s_flag_c2, s_flag_d2, s_flag_e2, s_flag_e1)

    def on_e2():
        type_2(s_box_e2, s_flag_e2, s_flag_e1, s_flag_d1, s_flag_d2, s_flag_d3, s_flag_e3)

    def on_e3():
        type_2(s_box_e3, s_flag_e3, s_flag_e2, s_flag_d2, s_flag_d3, s_flag_d4, s_flag_e4)

    def on_e4():
        type_2(s_box_e4, s_flag_e4, s_flag_e3, s_flag_d3, s_flag_d4, s_flag_d5, s_flag_e5)

    def on_b5():
        type_2(s_box_b5, s_flag_b5, s_flag_a5, s_flag_a4, s_flag_b4, s_flag_c4, s_flag_c5)

    def on_c5():
        type_2(s_box_c5, s_flag_c5, s_flag_b5, s_flag_b4, s_flag_c4, s_flag_d4, s_flag_d5)

    def on_d5():
        type_2(s_box_d5, s_flag_d5, s_flag_c5, s_flag_c4, s_flag_d4, s_flag_e4, s_flag_e5)

    def type_3(box, this_flag, flag_1, flag_2, flag_3, flag_4, flag_5, flag_6, flag_7, flag_8):
        global s_flag_a1, s_flag_a2, s_flag_a3, s_flag_a4, s_flag_a5, s_flag_b1, s_flag_b2, s_flag_b3, s_flag_b4, s_flag_b5, s_flag_c1, s_flag_c2, s_flag_c3, s_flag_c4, s_flag_c5, s_flag_d1, s_flag_d2, s_flag_d3, s_flag_d4, s_flag_d5, s_flag_e1, s_flag_e2, s_flag_e3, s_flag_e4, s_flag_e5, s_global_flag
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            winsound.Beep(300, 50)
        if s_global_flag:
            if not this_flag:
                k = 0
                listok = [flag_1, flag_2, flag_3, flag_4, flag_5, flag_6, flag_7, flag_8]
                for i in range(len(listok)):
                    if listok[i]:
                        k += 1
                box.configure(text=k, bg='white')
                CheckWin()

            else:
                GameOver()

    def on_b2():
        type_3(s_box_b2, s_flag_b2, s_flag_a1, s_flag_a2, s_flag_a3, s_flag_b3, s_flag_c3, s_flag_c2, s_flag_c1,
               s_flag_b1)

    def on_b3():
        type_3(s_box_b3, s_flag_b3, s_flag_a2, s_flag_a3, s_flag_a4, s_flag_b4, s_flag_c4, s_flag_c3, s_flag_c2,
               s_flag_b2)

    def on_b4():
        type_3(s_box_b4, s_flag_b4, s_flag_a3, s_flag_a4, s_flag_a5, s_flag_b5, s_flag_c5, s_flag_c4, s_flag_c3,
               s_flag_b3)

    def on_c2():
        type_3(s_box_c2, s_flag_c2, s_flag_b1, s_flag_b2, s_flag_b3, s_flag_c3, s_flag_d3, s_flag_d2, s_flag_d1,
               s_flag_c1)

    def on_c3():
        type_3(s_box_c3, s_flag_c3, s_flag_b2, s_flag_b3, s_flag_b4, s_flag_c4, s_flag_d4, s_flag_d3, s_flag_d2,
               s_flag_c2)

    def on_c4():
        type_3(s_box_c4, s_flag_c4, s_flag_b3, s_flag_b4, s_flag_b5, s_flag_c5, s_flag_d5, s_flag_d4, s_flag_d3,
               s_flag_c3)

    def on_d2():
        type_3(s_box_d2, s_flag_d2, s_flag_c1, s_flag_c2, s_flag_c3, s_flag_d3, s_flag_e3, s_flag_e2, s_flag_e1,
               s_flag_d1)

    def on_d3():
        type_3(s_box_d3, s_flag_d3, s_flag_c2, s_flag_c3, s_flag_c4, s_flag_d4, s_flag_e4, s_flag_e3, s_flag_e2,
               s_flag_d2)

    def on_d4():
        type_3(s_box_d4, s_flag_d4, s_flag_c3, s_flag_c4, s_flag_c5, s_flag_d5, s_flag_e5, s_flag_e4, s_flag_e3,
               s_flag_d3)

    def Statistics():
        def CleanStat():
            s_stat_start_list = [0, 0]
            np.save('C:/MihaSoft Files/SaperStat', s_stat_start_list)
            stat_window.destroy()

        def Close():
            stat_window.destroy()

        stat_window = Toplevel()
        stat_window.geometry('200x220+70+70')
        stat_window.resizable(0, 0)
        stat_window.title('Статистика')

        first_label = Label(stat_window, text='Побед:')
        first_label.place(x=5, y=5)

        second_label = Label(stat_window, text='Всего игр:')
        second_label.place(x=5, y=50)

        third_label = Label(stat_window, text='Процент выигрышей:')
        third_label.place(x=5, y=95)

        s_stat_list = np.load('C:/MihaSoft Files/SaperStat.npy')

        if s_stat_list[0] == 0:
            percent = '0%'

        else:
            percent = str(int((s_stat_list[1] / s_stat_list[0]) * 100)) + '%'

        wins = Label(stat_window, text=s_stat_list[1])
        wins.place(x=150, y=5)

        games = Label(stat_window, text=s_stat_list[0])
        games.place(x=150, y=50)

        percents = Label(stat_window, text=percent)
        percents.place(x=150, y=95)

        clean_button = Button(stat_window, text='Очистить статистику', bg='#db9c9c', command=CleanStat)
        clean_button.place(x=30, y=135)

        close_button = Button(stat_window, text='ОК', bg='#b6e0e0', width=16, command=Close)
        close_button.place(x=32, y=170)

    if not os.path.exists('C:/MihaSoft Files/SaperStat.npy'):
        s_stat_start_list = [0, 0]
        np.save('C:/MihaSoft Files/SaperStat', s_stat_start_list)

    window.geometry('430x450+50+50')
    window.title('Saper 1.0')

    s_title = Label(window, text="Saper 1.0", font=("Arial Bold", 16), fg="red")
    s_title.place(x=50, y=10)

    s_box_a1 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_a1)
    s_box_a1.place(x=80, y=100)

    s_box_a2 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_a2)
    s_box_a2.place(x=132, y=100)

    s_box_a3 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_a3)
    s_box_a3.place(x=184, y=100)

    s_box_a4 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_a4)
    s_box_a4.place(x=236, y=100)

    s_box_a5 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_a5)
    s_box_a5.place(x=288, y=100)

    s_box_b1 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_b1)
    s_box_b1.place(x=80, y=156)

    s_box_b2 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_b2)
    s_box_b2.place(x=132, y=156)

    s_box_b3 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_b3)
    s_box_b3.place(x=184, y=156)

    s_box_b4 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_b4)
    s_box_b4.place(x=236, y=156)

    s_box_b5 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_b5)
    s_box_b5.place(x=288, y=156)

    s_box_c1 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_c1)
    s_box_c1.place(x=80, y=212)

    s_box_c2 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_c2)
    s_box_c2.place(x=132, y=212)

    s_box_c3 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_c3)
    s_box_c3.place(x=184, y=212)

    s_box_c4 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_c4)
    s_box_c4.place(x=236, y=212)

    s_box_c5 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_c5)
    s_box_c5.place(x=288, y=212)

    s_box_d1 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_d1)
    s_box_d1.place(x=80, y=268)

    s_box_d2 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_d2)
    s_box_d2.place(x=132, y=268)

    s_box_d3 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_d3)
    s_box_d3.place(x=184, y=268)

    s_box_d4 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_d4)
    s_box_d4.place(x=236, y=268)

    s_box_d5 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_d5)
    s_box_d5.place(x=288, y=268)

    s_box_e1 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_e1)
    s_box_e1.place(x=80, y=324)

    s_box_e2 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_e2)
    s_box_e2.place(x=132, y=324)

    s_box_e3 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_e3)
    s_box_e3.place(x=184, y=324)

    s_box_e4 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_e4)
    s_box_e4.place(x=236, y=324)

    s_box_e5 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_e5)
    s_box_e5.place(x=288, y=324)

    restart_button = Button(window, text='Новая игра', width=10, bg='#93e6a8', font=("Arial Bold", 12),
                            command=RestartGame)
    restart_button.place(x=300, y=10)

    info_label = Label(window, text='', font=("Arial Bold", 16))
    info_label.place(x=138, y=400)

    stat_button = Button(window, text='Статистика', width=10, bg='#d9c786', font=("Arial Bold", 12), command=Statistics)
    stat_button.place(x=180, y=10)
    NewGame()

    off = Button(window, text="⌂", font=("Arial Bold", 15), width=2, height=1, bg="black", fg="white",
                 command=Return)
    off.place(x=0, y=0)
    ToolTip(off, "На главную...")


def Clock():
    def timing():
        current_time = time.strftime("%H:%M:%S")
        clock.config(text=current_time)
        clock.after(200, timing)

    root = Toplevel()
    root.resizable(0, 0)
    root.attributes('-topmost', 'true')
    root.title('Часы')
    clock = Label(root, font=("times", 60, "bold"))
    clock.pack()
    timing()


def home():
    def germes1():
        rasherec1()
        YourAgeOnline()

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

    def germes8():
        rasherec1()
        fallout8()

    def germes9():
        rasherec1()
        fallout9()

    def germes10():
        window.wm_state('iconic')
        fallout10()

    def germes11():
        window.wm_state('iconic')
        fallout11()

    def germes12():
        rasherec1()
        Saper()

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
        r9.destroy()
        r10.destroy()
        r11.destroy()
        r12.destroy()
        r13.destroy()
        clock_click.destroy()
        settings_click.destroy()
        message_click.destroy()

    window.title("MihaSoft 10.2")
    window.geometry('790x870+50+50')

    r1 = Label(window, text="Ⓜ", font=("Arial Bold", 365), fg="red")
    r1.place(x=150, y=5)

    x = Label(window, width=90, height=22, bg='#e0b6b6')
    x.place(x=70, y=520)

    r2 = Button(window, text="YourAgeOnline", font=("Arial Bold", 13), width=25, height=2, bg="#0039A6", fg="white",
                command=germes1)
    r2.place(x=90, y=720)
    rep(r2)

    r3 = Button(window, text="MiddleScoreOnline", font=("Arial Bold", 13), width=25, height=2, bg="#FF0000",
                fg="white", command=germes2)
    r3.place(x=450, y=720)
    rep(r3)

    r4 = Button(window, text="The SML - IDE & Compiler", font=("Arial Bold", 13), width=25, height=2, bg="#D52B1E",
                fg="white", command=germes3)
    r4.place(x=90, y=780)
    rep(r4)

    r5 = Button(window, text="TrunsNumSystem", font=("Arial Bold", 13), width=25, height=2, bg='#FFDF00',
                fg="black", command=germes4)
    r5.place(x=450, y=780)
    rep(r5)

    r6 = Button(window, text="CrossZero", font=("Arial Bold", 13), width=25, height=2, bg='#FFFFFF',
                fg="black", command=germes5)
    r6.place(x=90, y=660)
    rep(r6)

    r7 = Button(window, text="MihNote", font=("Arial Bold", 13), width=25, height=2, bg='#FFFFFF',
                fg="black", command=germes6)
    r7.place(x=450, y=660)
    rep(r7)

    r8 = Button(window, text="WindowManager", font=("Arial Bold", 13), width=25, height=2, bg='#93e6a1',
                fg="black", command=germes7)
    r8.place(x=90, y=600)
    rep(r8)

    r9 = Button(window, text="HolidayWarnings", font=("Arial Bold", 13), width=25, height=2, bg='#93e6a1',
                fg="black", command=germes8)
    r9.place(x=450, y=600)
    rep(r9)

    r10 = Button(window, text="YourWarnings", font=("Arial Bold", 13), width=25, height=2, bg='#9ae3de',
                 fg="black", command=germes9)
    r10.place(x=90, y=540)
    rep(r10)

    r11 = Button(window, text="Shmalyalka", font=("Arial Bold", 13), width=25, height=2, bg='#9ae3de',
                 fg="black", command=germes10)
    r11.place(x=450, y=540)
    rep(r11)

    r12 = Button(window, text="Paint", font=("Arial Bold", 13), width=10, height=2, bg='#a9e866',
                 fg="black", command=germes11)
    r12.place(x=337, y=660)
    rep(r12)

    r13 = Button(window, text="Saper", font=("Arial Bold", 13), width=10, height=2, bg='#d67ab4',
                 fg="black", command=germes12)
    r13.place(x=337, y=600)
    rep(r13)

    clock_click = Button(window, text="Часы", font=("Arial Bold", 10), width=5, height=1, bg='#b8b8b8',
                         fg="black", command=Clock)
    clock_click.place(x=10, y=10)
    rep(clock_click)

    settings_click = Button(window, text="Настройки", font=("Arial Bold", 10), width=8, height=1, bg='#b8b8b8',
                            fg="black", command=Settings)
    settings_click.place(x=70, y=10)
    rep(settings_click)

    message_click = Button(window, text="Сообщение от автора", font=("Arial Bold", 10), width=18, height=1,
                           bg='#b8b8b8',
                           fg="black", command=AuthorList)
    message_click.place(x=155, y=10)
    rep(message_click)


def rep(a):
    bg = a['background']
    fg = a['foreground']

    def on_enter(e):
        a['background'] = '#6e6e6e'
        a['foreground'] = 'white'

    def on_leave(e):
        a['background'] = bg
        a['foreground'] = fg

    a.bind("<Enter>", on_enter)
    a.bind("<Leave>", on_leave)


def Start():
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
        ToolTip(btn1,
                'На диске C: будет создана папка MihaSoft Files, в которой будут размещаться новые папки и файлы, создаваемые в процессе работы программы')
        btn2 = Button(window, text='ОТМЕНА', font=('Times New Roman', 10), width=13, command=ola)
        btn2.place(x=350, y=50)

    else:
        if os.path.exists('C:/MihaSoft Files/AnimationFlagFile.miha'):
            LoadingLine()
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Music()
        home()
        HolidayWarnings()
        YourWarnings()


def LoadingLine():
    global line_height, logo_size
    line_height = 1
    logo_size = 1

    def LoadingLineCicle():
        global line_height, logo_size
        line_1.configure(height=line_height)
        line_2.configure(height=line_height)
        line_height += 1
        r1.configure(font=("Arial Bold", logo_size))
        logo_size += 13

    def Destroing():
        line_1.destroy()
        line_2.destroy()

    line_1 = Label(window, height=1, width=8, bg='red')
    line_1.place(x=20, y=20)
    line_2 = Label(window, height=1, width=8, bg='red')
    line_2.place(x=705, y=20)

    window.title("MihaSoft 10.2")
    window.geometry('790x870+50+50')

    r1 = Label(window, text="Ⓜ", font=("Arial Bold", 1), fg="red")
    r1.place(x=150, y=5)

    for i in range(1, 30):
        window.after(20, LoadingLineCicle())
        window.update()

    line_1.configure(bg='green')
    line_2.configure(bg='green')
    window.update()
    window.after(800, Destroing())
    r1.destroy()


def Settings():
    def click_an_but():
        if not os.path.exists('C:/MihaSoft Files/AnimationFlagFile.miha'):
            f = open('C:/MihaSoft Files/AnimationFlagFile.miha', 'w')
            f.close()
            animation_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')
        else:
            os.remove('C:/MihaSoft Files/AnimationFlagFile.miha')
            animation_button.configure(text='ВКЛЮЧИТЬ', bg='green')

    def click_so_but():
        if not os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            f = open('C:/MihaSoft Files/SoundFlagFile.miha', 'w')
            f.close()
            sound_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')
        else:
            os.remove('C:/MihaSoft Files/SoundFlagFile.miha')
            sound_button.configure(text='ВКЛЮЧИТЬ', bg='green')

    def set_exit():
        set_window.destroy()

    set_window = Toplevel()
    set_window.geometry('400x200+70+70')
    set_window.resizable(0, 0)
    set_window.title('Настройки')

    first_label = Label(set_window, text='Анимация запуска программы:')
    first_label.place(x=10, y=10)

    animation_button = Button(set_window, font=("Arial Bold", 11), width=13, fg='white', command=click_an_but)
    animation_button.place(x=220, y=10)

    if not os.path.exists('C:/MihaSoft Files/AnimationFlagFile.miha'):
        animation_button.configure(text='ВКЛЮЧИТЬ', bg='green')
    else:
        animation_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')

    second_label = Label(set_window, text='Звук:')
    second_label.place(x=10, y=90)

    sound_button = Button(set_window, font=("Arial Bold", 11), width=13, fg='white', command=click_so_but)
    sound_button.place(x=220, y=90)

    if not os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
        sound_button.configure(text='ВКЛЮЧИТЬ', bg='green')
    else:
        sound_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')

    exit_button = Button(set_window, text='OK', bg='#b8b8b8', font=("Arial Bold", 11), width=13, command=set_exit)
    exit_button.place(x=220, y=140)


def Music():
    winsound.Beep(300, 900)
    for i in range(1, 4):
        window.after(50, winsound.Beep(300, 100))


def AuthorList():
    def mess_exit():
        mess_window.destroy()

    mess_window = Toplevel()
    mess_window.geometry('435x280+70+70')
    mess_window.title('Сообщение от автора')
    mess_window.resizable(0, 0)

    mess_ground = Text(mess_window, width=52, height=13)
    mess_ground.place(x=5, y=5)

    try:
        response = requests.get('https://mihasoft.glitch.me/api.txt')
        mess_ground.insert(1.0, response.text)
        mess_ground.configure(state='disabled')

    except:
        mess_ground.configure(fg='red')
        mess_ground.insert(1.0, 'НЕТ ДОСТУПА К СЕТИ!')

    exit_button = Button(mess_window, text='OK', bg='#b8b8b8', font=("Arial Bold", 11), width=13, command=mess_exit)
    exit_button.place(x=270, y=230)


window = Tk()
Start()
window.mainloop()
