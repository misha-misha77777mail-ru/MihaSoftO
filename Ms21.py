# ------------------------------------------------------------------------------------ #
#            M     M   M   M                  MMMMMMM          MMMM     M              #
#            M M M M       M         M        M         MMMM   M        M              #
#            M  M  M   M   MMMM   MMMM        MMMMMMM   M  M   MMMM   MMMMM            #
#            M     M   M   M  M   M  M              M   M  M   M        M              #
#            M     M   M   M  M   MMMMMM      MMMMMMM   MMMM   M        MMM            #
#                                                                                      #
#    Copyright (C) 2022 Vlasko M.M. <https://mihasoft.glitch.me> All rights reserved.  #
# ------------------------------------------------------------------------------------ #

# - 1 ------------- ИМПОРТЫ ---------------------

import datetime
import os
import tkinter.font as tkFont
from random import randint, choice
from shutil import rmtree
from time import sleep, strftime
from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from tkinter.ttk import Radiobutton
from turtle import *
import requests
from autopy.bitmap import capture_screen
from numpy import save, load
from winsound import Beep

# - 2 ------------- ОБЩИЕ ФУНКЦИИ ---------------


def center_window(root, x_width, height):
    """ 
    Функция для размещения окон в центре экрана 
    """

    x_window_height = height
    x_window_width = x_width

    # Получение ширины и высоты экрана монитора
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Расчёт координаты верхнего левого угла окна
    x_coordinate = int((screen_width / 2) - (x_window_width / 2))
    y_coordinate = int((screen_height / 2) - (x_window_height / 2))

    root.geometry('{}x{}+{}+{}'.format(x_window_width, x_window_height, x_coordinate, y_coordinate))


class ToolTipBase:
    """ 
    Пртотип всплывающих при наведении 
    курсора на объект подсказок 
    """

    def __init__(self, button, text):
        self.button = button
        self.text = text
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        self._id1 = self.button.bind('<Enter>', self.enter)        # Событие при наведении курсора
        self._id2 = self.button.bind('<Leave>', self.leave)        # Событие при отводе курсора от объекта
        self._id3 = self.button.bind('<ButtonPress>', self.leave)  # Событие при нажатии на объект (кнопку)

    def enter(self, event=None):
        """
        Появление подсказки 
        """

        self.schedule()

    def leave(self, event=None):
        """ 
        Исчезновение подсказки 
        """

        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.button.after(15, self.showtip)

    def unschedule(self):
        ad = self.id
        self.id = None
        if ad:
            self.button.after_cancel(ad)

    def showtip(self):
        if self.tipwindow:
            return
        xx = self.button.winfo_rootx() + 20
        yy = self.button.winfo_rooty() + self.button.winfo_height() + 1
        self.tipwindow = tw = Toplevel(self.button)
        tw.wm_overrideredirect(True)
        tw.wm_geometry('+%d+%d' % (xx, yy))
        self.showcontents()

    def showcontents(self):
        label = Label(self.tipwindow, text=str(self.text), justify=LEFT,
                      background='#ffffe0', relief=SOLID, borderwidth=1)
        label.pack()

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


class ToolTipok(ToolTipBase):
    """
    Объект подсказки 
    """
    def __init__(self, button, text):
        ToolTipBase.__init__(self, button, text)

    def showcontents(self):
        ToolTipBase.showcontents(self)


def ToolTip(button, text):
    """
    Функция, благодаря которой всплывающие подсказки появляются только
    при включении соответствующих настроек
    """

    if os.path.exists('C:/MihaSoft Files/TintFlagFile.miha'):
        ToolTipok(button, text)


class SMLGlobals:
    """
    Глобальные переменные для приложения
    The Simplest Mihail's language (SML) - IDE and Compiler
    """

    def __init__(self):
        self.run_result = None
        self.flag = None
        self.flag_1 = None


class CrossZeroGlobals:
    """ 
    Глобальные переменные для приложения CrossZero
    """

    def __init__(self):
        self.flag_1 = 3
        self.flag_2 = 3
        self.flag_3 = 3
        self.flag_4 = 3
        self.flag_5 = 3
        self.flag_6 = 3
        self.flag_7 = 3
        self.flag_8 = 3
        self.flag_9 = 3
        self.number_of_moves = 0
        self.winner = ''
        self.player_1 = ''
        self.player_2 = ''
        self.naming_condition = 0
        self.condition = 3
        self.number_of_moves_str = None
        self.name_of_winner_str = None
        self.save_string = None
        self.game_condition = True
        self.game_res_condition = None


class MihNoteGlobals:
    """
    Глобальные переменные для приложения MihNote 
    """

    def __init__(self):
        self.open_combobox = None
        self.open_ok_button = None
        self.edit_combobox = None
        self.edit_ok_button = None
        self.delete_combobox = None
        self.delete_ask_button = None


class PaintGlobals:
    """ 
    Глобальные переменные для приложения Paint 
    """

    def __init__(self):
        self.choose_flag = True
        self.save_flag = True
        self.chosen_color = 'white'
        self.now_color = None
        self.file_name = None


class SaperGlobals:
    """ 
    Глобальные переменные для приложения Saper 
    """

    def __init__(self):
        self.flag_a1 = None
        self.flag_a2 = None
        self.flag_a3 = None
        self.flag_a4 = None
        self.flag_a5 = None
        self.flag_b1 = None
        self.flag_b2 = None
        self.flag_b3 = None
        self.flag_b4 = None
        self.flag_b5 = None
        self.flag_c1 = None
        self.flag_c2 = None
        self.flag_c3 = None
        self.flag_c4 = None
        self.flag_c5 = None
        self.flag_d1 = None
        self.flag_d2 = None
        self.flag_d3 = None
        self.flag_d4 = None
        self.flag_d5 = None
        self.flag_e1 = None
        self.flag_e2 = None
        self.flag_e3 = None
        self.flag_e4 = None
        self.flag_e5 = None
        self.bomb_list = None
        self.box_list = None
        self.global_flag = None


class ShmalyalkaGlobals:
    """ 
    Глобальные переменные для приложения Shmalyalka 
    """

    def __init__(self):
        self.number_of_hits = 0
        self.number_of_shots = 0
        self.flag = True
        self.speed_push = 2
        self.speed_snar = 1
        self.y_pushka = 130
        self.x_snaryad = None


class WindowManagerGlobals:
    """ 
    Глобальные переменные для приложения WindowManager 
    """

    def __init__(self):
        self.width = None
        self.height = None
        self.x_cord = None
        self.y_cord = None
        self.cust_title = None
        self.text = None
        self.font = None
        self.fsize = None
        self.color = ''
        self.text_x = None
        self.text_y = None
        self.open_path = None
        self.flag = True


class TurtlePaintGlobal:
    """ 
    Глобальная переменная для приложения TurtlePaint 
    """

    def __init__(self):
        self.colors = None


class LoadingLineGlobals:
    """ 
    Глобальные переменные для функции
    анимации загрузки программы 
    """

    def __init__(self):
        self.line_height = 1
        self.logo_size = 1


class PoupGlobals:
    """ 
    Глобальные переменные для функции
    выпадающего меню 
    """

    def __init__(self):
        self.x = None
        self.y = None

# - 3 ------------ ОСНОВНЫЕ ПРИЛОЖЕНИЯ --------------


def YourAgeOnline():
    """
    Приложение для расчёта времени, прошедшего между двумя датами.
    Подробнее - https://mihasoft.glitch.me/yao.html
    """

    def yao_to_home():
        """
         Функция возвращения на главную страницу MihaSoft
        (Уничтожение (destroy()) всех виджетов и запуск функции главной страницы)
        """

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
        home()
        center_window(window, 790, 870)

    def yao_begin():
        """ 
        Функция расчёта возраста при нажатии 
        соответствующей кнопки 
        """

        # Проверка корректности введённых пользователем данных.
        # Функция isdigit() проверяет, является ли введённое значение числом.

        if (not yao_day_input.get().isdigit()) or (not yao_month_input.get().isdigit()) or (
                not yao_year_input.get().isdigit()) or (not yao_now_day_input.get().isdigit()) or (
                not yao_now_month_input.get().isdigit()) or (not yao_now_year_input.get().isdigit()):
            messagebox.showerror('Ошибка!', 'Введены некорректные значения!')

        else:
            yao_days = 0
            yao_day_1 = int(yao_day_input.get())
            yao_month_1 = int(yao_month_input.get())
            yao_year_1 = int(yao_year_input.get())
            yao_day_2 = int(yao_now_day_input.get())
            yao_month_2 = int(yao_now_month_input.get())
            yao_year_2 = int(yao_now_year_input.get())

            # Проверка соответствия введённых чисел размерам месяца, года
            # и того факта, что текущяя дата больше, чем исходная.

            if ((yao_day_1 >= 1) and (yao_day_1 <= 31)) and ((yao_month_1 >= 1) and (yao_month_1 <= 12)) and (
                    yao_year_1 > 0) and ((yao_day_2 >= 1) and (yao_day_2 <= 31)) and (
                    (yao_month_2 >= 1) and (yao_month_2 <= 12)) and (yao_year_2 > 0) and (yao_year_2 >= yao_year_1):
                z = yao_month_2 - 1
                yao_years = yao_year_2 - yao_year_1 - 1
                h = 12 - yao_month_1

                # Обработка потенциальной високосности года:

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

                # Обработка выбранной пользователем формы вывода данных
                # и подбор нужных окончаний слов в зависимости от числа.

                yao_l = yao_choice_def.get()
                if yao_l == 1:
                    if yao_years == 0:
                        yao_label_8.configure(
                            text=(str(yao_years) + ' год ' + str(yao_months) + ' месяцев ' + str(
                                yao_days - 1) + ' дней.'))
                    elif yao_years == 1:
                        yao_label_8.configure(text=(str(yao_years) + ' год ' + str(yao_months) + ' месяцев ' + str(
                            yao_days - 1) + ' дней.'))
                    elif (yao_years == 2) or (yao_years == 3) or (yao_years == 4):
                        yao_label_8.configure(
                            text=(str(yao_years) + ' года ' + str(yao_months) + ' месяцев ' + str(
                                yao_days - 1) + ' дней.'))
                    else:
                        yao_label_8.configure(text=(str(yao_years) + ' лет ' + str(yao_months) + ' месяцев ' + str(
                            yao_days - 1) + ' дней.'))
                if yao_l == 2:
                    yao_label_8.configure(
                        text=(str((365.29 * yao_years) + (yao_months * 30.25) + (yao_days - 2) // 1) + ' дней.'))
            else:
                messagebox.showerror('Ошибка!', 'Проверьте правильность ввода!')

    def yao_Now_Date():
        """
        Функция получения текущего системного времени
        и его подстановки в соответствующие поля ввода
        """
        yao_now = datetime.datetime.now()
        yao_now_day_input.insert(0, str(yao_now.day))
        yao_now_month_input.insert(0, str(yao_now.month))
        yao_now_year_input.insert(0, str(yao_now.year))

    def yao_Save():
        """
        Функция сохранения в файл данных об исходной
        дате, введённой пользователем
        """
        def yao_Save_OK():
            """ 
            Сохранение файла с введённым 
            названием и закрытие окна сохранения
            """
            text_file = open('C:/MihaSoft Files/YAO Files/' + str(yao_save_name_input.get()), 'w')
            text_file.write(str(yao_day_input.get()) + '/' + str(yao_month_input.get()) + '*' + str(
                yao_year_input.get()) + '.')
            text_file.close()
            yao_save_window.destroy()

        def yao_Save_Abort():
            """ 
            Закрытие окна без сохранения 
            """
            yao_save_window.destroy()

        yao_save_window = Toplevel()
        center_window(yao_save_window, 250, 100)
        yao_save_window.resizable(False, False)  # Неизменяемый размер окна
        yao_save_window.title('Сохранение')

        yao_save_label = Label(yao_save_window, text='Введите имя...')
        yao_save_label.place(x=5, y=5)
        
        # Поле ввода имени файла
        yao_save_name_input = Entry(yao_save_window, width=20)
        yao_save_name_input.place(x=5, y=30)

        yao_saving_button = Button(yao_save_window, text='Сохранить', width=10, height=1, bg="#8ceb8a",
                                   command=yao_Save_OK)
        yao_saving_button.place(x=140, y=29)

        yao_save_abort_button = Button(yao_save_window, text='Отмена', width=10, height=1, bg='#999999',
                                       command=yao_Save_Abort)
        yao_save_abort_button.place(x=140, y=64)

    def yao_Open():
        """ 
        Функция подстановки ранее сохранённой исходной
        даты в соответствующие поля ввода
        """
        def yao_Open_OK():
            """ 
            Открытие выбранного файла и вывод данных 
            """
            if yao_files_list:
                yao_open_file = open('C:/MihaSoft Files/YAO Files/' + str(yao_open_combobox.get()), 'r')
                yao_file = yao_open_file.read()
                yao_open_file.close()

                yao_data_from_file = list(str(yao_file))

                yao_day = yao_month = yao_year = ''
                
                # Структура сохраняемых файлов: 11/11*1111.
                # Следующие циклы for считывают цифры между соответствующими
                # знаками и записывают их в соответствующие переменные.
                
                for i in range(0, yao_data_from_file.index('/')):
                    yao_day += str(yao_data_from_file[i])

                for i in range(yao_data_from_file.index('/') + 1, yao_data_from_file.index('*')):
                    yao_month += str(yao_data_from_file[i])

                for i in range(yao_data_from_file.index('*') + 1, yao_data_from_file.index('.')):
                    yao_year += str(yao_data_from_file[i])

                yao_day_input.insert(0, yao_day)
                yao_month_input.insert(0, yao_month)
                yao_year_input.insert(0, yao_year)
                yao_open_window.destroy()

        def yao_Open_Abort():
            """ 
            Закрытие окна без вывода данных 
            """
            yao_open_window.destroy()

        yao_open_window = Toplevel()
        center_window(yao_open_window, 300, 150)
        yao_open_window.resizable(False, False)
        yao_open_window.title('Подставить...')

        yao_open_label = Label(yao_open_window, text='Выберите имя...')
        yao_open_label.place(x=5, y=5)
        
        # Выпадающий список имеющихся файлов
        yao_open_combobox = ttk.Combobox(yao_open_window, values=os.listdir('C:/MihaSoft Files/YAO Files'),
                                         font=('Arial Bold', 16),
                                         state='readonly')
        yao_open_combobox.place(x=10, y=50)

        yao_open_button = Button(yao_open_window, text='Подставить', font=('Arial Bold', 10), bg='#7bd491', width=14,
                                 command=yao_Open_OK)
        yao_open_button.place(x=10, y=100)

        yao_open_abort_button = Button(yao_open_window, text='Отмена', font=('Arial Bold', 10), bg='#999999', width=14,
                                       command=yao_Open_Abort)
        yao_open_abort_button.place(x=150, y=100)

    def yao_Delete():
        """ 
        Функция удаления ранее записанных файлов 
        """
        
        def yao_Delete_OK():
            """ 
            Удаление выбранного файла и закрытие окна 
            """
            
            if yao_files_list:  # Проверяет, выбран ли хоть какой-то файл
                os.remove('C:/MihaSoft Files/YAO Files/' + str(yao_del_combobox.get()))
                yao_delete_window.destroy()

        def yao_Delete_Abort():
            """ 
            Закрытие окна без удаления 
            """
            yao_delete_window.destroy()

        yao_delete_window = Toplevel()
        yao_delete_window.geometry('300x150+70+70')
        center_window(yao_delete_window, 300, 150)
        yao_delete_window.resizable(False, False)
        yao_delete_window.title('Удаление записи')

        yao_del_label = Label(yao_delete_window, text='Выберите запись для удаления...')
        yao_del_label.place(x=5, y=5)

        # Выпадающий список имеющихся файлов
        yao_del_combobox = ttk.Combobox(yao_delete_window, values=os.listdir('C:/MihaSoft Files/YAO Files'),
                                        font=('Arial Bold', 16),
                                        state='readonly')
        yao_del_combobox.place(x=10, y=50)

        yao_del_ok_button = Button(yao_delete_window, text='Удалить', font=('Arial Bold', 10), bg='#eb8a8a',
                                   width=14, command=yao_Delete_OK)
        yao_del_ok_button.place(x=10, y=100)

        yao_del_abort_button = Button(yao_delete_window, text='Отмена', font=('Arial Bold', 10),
                                      bg='#999999', width=14, command=yao_Delete_Abort)
        yao_del_abort_button.place(x=150, y=100)

    def yao_Clean():
        """ 
        Функция очистки всех полей ввода 
        """
        yao_day_input.delete(0, 'end')
        yao_now_day_input.delete(0, 'end')
        yao_month_input.delete(0, 'end')
        yao_now_month_input.delete(0, 'end')
        yao_year_input.delete(0, 'end')
        yao_now_year_input.delete(0, 'end')
    
    # Создание папки файлов приложения в случае отсутствия таковой:
    if not os.path.exists('C:/MihaSoft Files/YAO Files'):
        os.mkdir('C:/MihaSoft Files/YAO Files')
    
    center_window(window, 650, 250)
    window.title('YourAgeOnline 3.0')

    yao_title = Label(window, text='YourAgeOnline 3.0', font=('Arial Bold', 16), fg='red')
    yao_title.place(x=40, y=20)

    yao_label_1 = Label(window, text='Дата рождения:', font=('Times New Roman', 12))
    yao_label_1.place(x=40, y=60)

    # Поле ввода исходного дня
    yao_day_input = Entry(window, width=4)
    yao_day_input.place(x=40, y=100)
    ToolTip(yao_day_input, 'День')

    yao_label_2 = Label(window, text='.', font=('Times New Roman', 12))
    yao_label_2.place(x=73, y=103)

    # Поле ввода исходного месяца
    yao_month_input = Entry(window, width=4)
    yao_month_input.place(x=90, y=100)
    ToolTip(yao_month_input, 'Месяц')

    yao_label_3 = Label(window, text='.', font=('Times New Roman', 12))
    yao_label_3.place(x=124, y=100)

    # Поле ввода исходного года
    yao_year_input = Entry(window, width=9)
    yao_year_input.place(x=140, y=100)
    ToolTip(yao_year_input, 'Год')

    yao_sysdate_button = Button(window, text='Подставить т. д.', width=13, height=1, bg='#eef5b3',
                                command=yao_Now_Date)
    yao_sysdate_button.place(x=250, y=20)
    ToolTip(yao_sysdate_button, 'Подставить системную дату...')

    yao_save_button = Button(window, text='Сохранить зап.', width=13, height=1, bg='#8ceb8a',
                             command=yao_Save)
    yao_save_button.place(x=490, y=120)
    ToolTip(yao_save_button, 'Сохранить данные о дате рождения...')

    yao_birthday_button = Button(window, text='Подставить д. р.', width=13, height=1, bg='#b3f5ec',
                                 command=yao_Open)
    yao_birthday_button.place(x=370, y=20)
    ToolTip(yao_birthday_button, 'Подставить сохранённую дату рождения...')

    yao_delete_button = Button(window, text='Удалить зап.', width=13, height=1, bg='#eb8a8a', fg='black',
                               command=yao_Delete)
    yao_delete_button.place(x=490, y=70)
    ToolTip(yao_delete_button, 'Удалить запись о дате рождения...')

    yao_clean_button = Button(window, text='Очистить', width=13, height=1, bg='#ebd38a', command=yao_Clean)
    yao_clean_button.place(x=490, y=20)
    ToolTip(yao_clean_button, 'Очистить поля ввода...')

    yao_label_4 = Label(window, text='Текущая дата:', font=('Times New Roman', 12))
    yao_label_4.place(x=300, y=60)
   
    # Поле ввода текущего дня
    yao_now_day_input = Entry(window, width=4)
    yao_now_day_input.place(x=300, y=100)
    ToolTip(yao_now_day_input, 'День')

    yao_label_5 = Label(window, text='.', font=('Times New Roman', 12))
    yao_label_5.place(x=333, y=100)

    # Поле ввода текущего месяца
    yao_now_month_input = Entry(window, width=4)
    yao_now_month_input.place(x=350, y=100)
    ToolTip(yao_now_month_input, 'Месяц')

    yao_label_6 = Label(window, text='.', font=('Times New Roman', 12))
    yao_label_6.place(x=384, y=100)

    # Поле ввода текущего года
    yao_now_year_input = Entry(window, width=9)
    yao_now_year_input.place(x=400, y=100)
    ToolTip(yao_now_year_input, 'Год')
   
    # Получение выбранного способа вывода данных
    yao_choice_def = IntVar()
    
    # Кнопки выбора одного из двух способов вывода данных:
    yao_choice_radbut_1 = Radiobutton(window, text='Вывести возраст в годах, месяцах и днях', variable=yao_choice_def,
                                      value=1)
    yao_choice_radbut_1.place(x=40, y=150)

    yao_choice_radbut_2 = Radiobutton(window, text='Вывести возраст в днях', variable=yao_choice_def, value=2)
    yao_choice_radbut_2.place(x=300, y=150)

    yao_result_button = Button(window, text='РАССЧИТАТЬ', width=19, height=2, bg='black', fg='white', command=yao_begin)
    yao_result_button.place(x=40, y=190)

    yao_label_7 = Label(window, text='Ваш возраст: ', font=('Times New Roman', 16))
    yao_label_7.place(x=220, y=190)

    yao_label_8 = Label(window, font=('Times New Roman', 16))
    yao_label_8.place(x=350, y=190)

    yao_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                     command=yao_to_home)
    yao_off.place(x=0, y=5)
    ToolTip(yao_off, 'На главную...')


def MiddleScoreOnline():
    """
    Приложения для подсчёта среднего балла набора оценок.
    Подробнее - https://mihasoft.glitch.me/mso.html
    """
    def mso_to_home():
        """
        Возвращение на главную страницу MihaSoft
        """
        mso_title.destroy()
        mso_label_1.destroy()
        mso_label_2.destroy()
        mso_label_3.destroy()
        mso_label_4.destroy()
        mso_label_5.destroy()
        mso_label_6.destroy()
        mso_label_7.destroy()
        mso_label_8.destroy()
        mso_off.destroy()
        mso_input_1.destroy()
        mso_input_2.destroy()
        mso_result_button.destroy()
        home()
        center_window(window, 790, 870)     

    def mso_Done():
        """
        Функция расчёта среднего балла
        """
        
        # Проверка корректности введённых оценок
        if not mso_input_1.get().isdigit() or (not mso_input_2.get().isdigit() and mso_input_2.get() != ''):
            messagebox.showerror('Ошибка!', 'Введены некорректные значения!')
        else:
            mso_flag = 1
            mso_j = 0
            mso_score_list_1 = list(map(int, str(mso_input_1.get())))
            # Удаление чисел, не являющихся оценками
            for i in range(len(mso_score_list_1)):
                if (mso_score_list_1[i] != 2) and (mso_score_list_1[i] != 3) and (mso_score_list_1[i] != 4) and (
                        mso_score_list_1[i] != 5):
                    mso_score_list_1[i] = 0
            while 0 in mso_score_list_1:
                mso_score_list_1.remove(0)
            mso_score_list_2 = list(map(int, str(mso_input_2.get())))
            if mso_score_list_2 == [0]:
                mso_flag = 0
            for i in range(len(mso_score_list_2)):
                if (mso_score_list_2[i] != 2) and (mso_score_list_2[i] != 3) and (mso_score_list_2[i] != 4) and (
                        mso_score_list_2[i] != 5) and (mso_score_list_2[i] != 0):
                    mso_score_list_2[i] = 0
            while 0 in mso_score_list_2:
                mso_score_list_2.remove(0)
            if mso_flag == 0:
                mso_q = sum(mso_score_list_1) / len(mso_score_list_1)
                mso_label_4.configure(text=mso_q)
                if (mso_q >= 3.6) and (mso_q <= 4.6):
                    mso_label_5.configure(text='Можете расслабиться!!!')
                    # Расчёт необходимого числа лополнительных пятёрок
                    while sum(mso_score_list_1) / len(mso_score_list_1) < 4.6:
                        mso_score_list_1.append(5)
                        mso_j += 1
                    if mso_j == 1:
                        mso_label_6.configure(text='У вас выходит четвёрка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличную оценку до пятёрки в триместре.')
                    if (mso_j == 2) or (mso_j == 3) or (mso_j == 4):
                        mso_label_6.configure(text='У вас выходит четвёрка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличные оценки до пятёрки в триместре.')
                    if mso_j >= 5:
                        mso_label_6.configure(text='У вас выходит четвёрка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличных оценок до пятёрки в триместре.')
                if (mso_q >= 2.6) and (mso_q < 3.6):
                    mso_label_5.configure(text='Внимание!!!')
                    while sum(mso_score_list_1) / len(mso_score_list_1) < 3.6:
                        mso_score_list_1.append(5)
                        mso_j += 1
                    if mso_j == 1:
                        mso_label_6.configure(text='У вас выходит тройка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличную оценку до четвёрки в триместре.')
                    if (mso_j == 2) or (mso_j == 3) or (mso_j == 4):
                        mso_label_6.configure(text='У вас выходит тройка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличные оценки до четвёрки в триместре.')
                    if mso_j >= 5:
                        mso_label_6.configure(text='У вас выходит тройка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличных оценок до четвёрки в триместре.')
                if (mso_q >= 2) and (mso_q < 2.6):
                    mso_label_5.configure(text='Вам трындец!!!!')
                    while sum(mso_score_list_1) / len(mso_score_list_1) < 2.6:
                        mso_score_list_1.append(5)
                        mso_j += 1
                    if mso_j == 1:
                        mso_label_6.configure(text='У вас выходит ДВОЙКА. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличную оценку до тройки в триместре.')
                    if (mso_j == 2) or (mso_j == 3) or (mso_j == 4):
                        mso_label_6.configure(text='У вас выходит ДВОЙКА. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличные оценки до тройки в триместре.')
                    if mso_j >= 5:
                        mso_label_6.configure(text='У вас выходит ДВОЙКА. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличных оценок до тройки в триместре.')
                if (mso_q >= 4.6) and (mso_q <= 5):
                    mso_label_6.configure(text='')
                    mso_label_7.configure(text='')
                    mso_label_8.configure(text='')
                    mso_label_5.configure(text='У вас выходит пятёрка! Не получайте плохих оценок.')
            if mso_flag != 0:
                mso_z = (sum(mso_score_list_2) * 2 + sum(mso_score_list_1)) / (
                        len(mso_score_list_1) + len(mso_score_list_2) * 2)
                mso_label_4.configure(text=mso_z)
                if (mso_z >= 3.6) and (mso_z <= 4.6):
                    mso_label_5.configure(text='Можете расслабиться!!!')
                    while (sum(mso_score_list_2) * 2 + sum(mso_score_list_1)) / (
                            len(mso_score_list_1) + len(mso_score_list_2) * 2) < 4.6:
                        mso_score_list_1.append(5)
                        mso_j += 1
                    if mso_j == 1:
                        mso_label_6.configure(text='У вас выходит четвёрка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличную оценку до пятёрки в триместре.')
                    if (mso_j == 2) or (mso_j == 3) or (mso_j == 4):
                        mso_label_6.configure(text='У вас выходит четвёрка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличные оценки до пятёрки в триместре.')
                    if mso_j >= 5:
                        mso_label_6.configure(text='У вас выходит четвёрка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличных оценок до пятёрки в триместре.')
                if (mso_z >= 2.6) and (mso_z < 3.6):
                    mso_label_5.configure(text='Внимание!!!')
                    while (sum(mso_score_list_2) * 2 + sum(mso_score_list_1)) / (
                            len(mso_score_list_1) + len(mso_score_list_2) * 2) < 3.6:
                        mso_score_list_1.append(5)
                        mso_j += 1
                    if mso_j == 1:
                        mso_label_6.configure(text='У вас выходит тройка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличную оценку до четвёрки в триместре.')
                    if (mso_j == 2) or (mso_j == 3) or (mso_j == 4):
                        mso_label_6.configure(text='У вас выходит тройка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличные оценки до четвёрки в триместре.')
                    if mso_j >= 5:
                        mso_label_6.configure(text='У вас выходит тройка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличных оценок до четвёрки в триместре.')
                if (mso_z >= 2) and (mso_z < 2.6):
                    mso_label_5.configure(text='Вам трындец!!!!')
                    while (sum(mso_score_list_2) * 2 + sum(mso_score_list_1)) / (
                            len(mso_score_list_1) + len(mso_score_list_2) * 2) < 2.6:
                        mso_score_list_1.append(5)
                        mso_j += 1
                    if mso_j == 1:
                        mso_label_6.configure(text='У вас выходит ДВОЙКА. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличную оценку до тройки в триместре.')
                    if (mso_j == 2) or (mso_j == 3) or (mso_j == 4):
                        mso_label_6.configure(text='У вас выходит ДВОЙКА. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличные оценки до тройки в триместре.')
                    if mso_j >= 5:
                        mso_label_6.configure(text='У вас выходит ДВОЙКА. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличных оценок до тройки в триместре.')
                if (mso_z >= 4.6) and (mso_z <= 5):
                    mso_label_6.configure(text='')
                    mso_label_7.configure(text='')
                    mso_label_8.configure(text='')
                    mso_label_5.configure(text='У вас выходит пятёрка!\n Не получайте плохих оценок!')

    center_window(window, 790, 325)
    window.title('MiddleScoreOnline 5.1')

    mso_title = Label(window, text='MiddleScoreOnline 5.1', font=('Arial Bold', 16), fg='red')
    mso_title.place(x=40, y=20)

    mso_label_1 = Label(window, text='Введите оценки без индекса:', font=('Times New Roman', 12))
    mso_label_1.place(x=40, y=60)

    # Поле ввода оценок без индекса
    mso_input_1 = Entry(window, width=40)
    mso_input_1.place(x=40, y=100)

    mso_label_2 = Label(window, text='Введите оценки с индексом «2»:', font=('Times New Roman', 12))
    mso_label_2.place(x=40, y=140)

    # Поле ввода оценок с индексом
    mso_input_2 = Entry(window, width=40)
    mso_input_2.place(x=40, y=180)
    ToolTip(mso_input_2, '5₂')

    mso_result_button = Button(window, text='РАССЧИТАТЬ', width=19, height=2, bg='black', fg='white', command=mso_Done)
    mso_result_button.place(x=40, y=220)

    mso_label_3 = Label(window, text='Ваш средний балл: ', font=('Times New Roman', 16))
    mso_label_3.place(x=290, y=20)
    
    # Области вывода данных
    mso_label_4 = Label(window, font=('Times New Roman', 16))
    mso_label_4.place(x=310, y=60)

    mso_label_5 = Label(window, font=('Times New Roman', 16))
    mso_label_5.place(x=310, y=100)

    mso_label_6 = Label(window, font=('Times New Roman', 14))
    mso_label_6.place(x=310, y=140)

    mso_label_7 = Label(window, font=('Times New Roman', 14))
    mso_label_7.place(x=310, y=170)

    mso_label_8 = Label(window, font=('Times New Roman', 14))
    mso_label_8.place(x=333, y=170)

    mso_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                     command=mso_to_home)
    mso_off.place(x=0, y=5)
    ToolTip(mso_off, 'На главную...')


def SML():
    """
    Интерпритатор простейшего самодельного
    языка программирования
    Подробнее - https://mihasoft.glitch.me
    """
    sml = SMLGlobals()

    def sml_to_home():
        """ 
        Возвращение на главную страницу MihaSoft 
        """
        sml_error_1.destroy()
        sml_error_2.destroy()
        sml_error_3.destroy()
        sml_error_4.destroy()
        sml_error_5.destroy()
        sml_error_6.destroy()
        sml_title.destroy()
        sml_begin_button.destroy()
        sml_open_button.destroy()
        sml_save_button.destroy()
        sml_delete_button.destroy()
        sml_help_button.destroy()
        sml_off.destroy()
        sml_code_input.destroy()
        home()
        center_window(window, 790, 870)

    def sml_Help():
        """
        Функция вывода справочной информации
        """
        def sml_Help_Example():
            """
            Пример работы SML-программы
            """
            sml_example_window = Toplevel()
            sml_example_window.title('run...')
            center_window(sml_example_window, 200, 100)
            sml_example_window.resizable(False, False)
            sml_example_label = Label(sml_example_window, text='5 + 5 = 10')
            sml_example_label.place(x=10, y=30)

        def sml_Help_Exit():
            """ 
            Закрытие окна справки 
            """
            sml_help_window.destroy()

        sml_help_window = Toplevel()
        sml_help_window.title('Справка')
        center_window(sml_help_window, 1200, 540)
        sml_help_window.resizable(False, False)

        sml_help_field = Text(sml_help_window, width=145, height=28, font=('Times New Roman', 12))
        sml_help_field.place(x=5, y=5)

        sml_help_text = '''
          The Simplest Mihail’s Language
            _____________
          1 строка - объявление языка: <!DOCTYPE sml>
            _____________
          2 строка - объявление типа: using input; (вводить числа с клавиатуры) или using const; (конкретные числа)  
            _____________
          3 строка - если using input;: method=x;, где x это с (сложение), в (вычитание), у (умножение), д (деление), 
          ц (целочисленное деление), д (деление с остатком)  
                     если using const;: const1=x;, где x - первое значение  
            _____________  
          4 строка - если using input;: окончание программы: end;  
                     если using const;: const2=y, где y - второе значение
            _____________  
          5 строка - если using const;: method=x;, где x это с (сложение), в (вычитание), у (умножение), д (деление), 
          ц (целочисленное деление), д (деление с остатком)  
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
        sml_help_field.insert(1.0, sml_help_text)
        sml_help_field.configure(state='disabled')

        sml_show_example_button = Button(sml_help_window, text='ВЫПОЛНИТЬ', bg='white', command=sml_Help_Example)
        sml_show_example_button.place(x=133, y=450)

        sml_exit_help_button = Button(sml_help_window, text='ЗАКРЫТЬ', bg='#e6bebe', command=sml_Help_Exit)
        sml_exit_help_button.place(x=1000, y=450)

    def sml_Begin():
        """ 
        Функция выпобнения SML-программы 
        """
        
        # Очистка сообщений об ошибках
        sml_error_1.configure(text='')
        sml_error_2.configure(text='')
        sml_error_3.configure(text='')
        sml_error_4.configure(text='')
        sml_error_5.configure(text='')
        sml_error_6.configure(text='')

        def ex():
            """
            Функция выполнения программы при
            использовании метода input
            """
            # Получения введённых значений
            sml_args_1 = int(sml_run_input_1.get())
            sml_args_2 = int(sml_run_input_2.get())

            # Выполнение выбранной пользователем операции
            if sml.flag_1 == '+':
                sml.run_result = sml_args_1 + sml_args_2
            elif sml.flag_1 == '-':
                sml.run_result = sml_args_1 - sml_args_2
            elif sml.flag_1 == '*':
                sml.run_result = sml_args_1 * sml_args_2
            elif sml.flag_1 == '/':
                sml.run_result = sml_args_1 / sml_args_2
            elif sml.flag_1 == '//':
                sml.run_result = sml_args_1 // sml_args_2
            elif sml.flag_1 == '%':
                sml.run_result = sml_args_1 % sml_args_2

            sml_run_result_label.configure(text=sml.run_result)

        # Построчный разбор строчек введённого кода
        # и вывод потенциальных сообщений об ошибках
        if sml_code_input.get("1.0", "1.14") != "<!DOCTYPE sml>":
            sml_error_1.configure(text='Ошибка: линия 1')
        else:
            # 1 вариант работы программы: арифметичесвие операции
            # с конкретными числами
            if (sml_code_input.get('2.0', '2.12') != 'using const;') and (
                    sml_code_input.get('2.0', '2.12') != 'using input;'):
                sml_error_2.configure(text='Ошибка: линия 2')
            else:
                if sml_code_input.get('2.0', '2.12') == 'using const;':
                    if sml_code_input.get('3.0', '3.7') != 'const1=':
                        sml_error_3.configure(text='Ошибка: линия 3')
                    else:
                        if sml_code_input.get('4.0', '4.7') != 'const2=':
                            sml_error_4.configure(text='Ошибка: линия 4')
                        else:
                            sml_arg_1 = int(sml_code_input.get("3.7"))
                            sml_arg_2 = int(sml_code_input.get("4.7"))
                            if sml_code_input.get('5.0', '5.7') != 'method=':
                                sml_error_5.configure(text='Ошибка: линия 5')
                            else:
                                if sml_code_input.get('5.7') == 'с':
                                    sml.flag = '+'
                                elif sml_code_input.get('5.7') == 'в':
                                    sml.flag = '-'
                                elif sml_code_input.get('5.7') == 'у':
                                    sml.flag = '*'
                                elif sml_code_input.get('5.7') == "д":
                                    sml.flag = '/'
                                elif sml_code_input.get('5.7') == 'ц':
                                    sml.flag = '//'
                                elif sml_code_input.get('5.7') == 'о':
                                    sml.flag = '%'
                                if sml_code_input.get('6.0', '6.4') != 'end;':
                                    sml_error_6.configure(text='Ошибка: линия 6')
                                else:
                                    sml_run_window = Toplevel()
                                    sml_run_window.title('run...')
                                    center_window(sml_run_window, 200, 100)
                                    sml_run_window.resizable(False, False)

                                    sml_run_arg_1 = Label(sml_run_window, text=sml_arg_1)
                                    sml_run_arg_1.place(x=10, y=30)

                                    sml_run_arg_2 = Label(sml_run_window, text=sml.flag)
                                    sml_run_arg_2.place(x=30, y=30)

                                    sml_run_arg_3 = Label(sml_run_window, text=sml_arg_2)
                                    sml_run_arg_3.place(x=50, y=30)

                                    sml_label = Label(sml_run_window, text='=')
                                    sml_label.place(x=70, y=30)

                                    sml_run_result_label = Label(sml_run_window)
                                    sml_run_result_label.place(x=90, y=30)

                                    if sml.flag == '+':
                                        sml.run_result = sml_arg_1 + sml_arg_2
                                    elif sml.flag == '-':
                                        sml.run_result = sml_arg_1 - sml_arg_2
                                    elif sml.flag == '*':
                                        sml.run_result = sml_arg_1 * sml_arg_2
                                    elif sml.flag == '/':
                                        sml.run_result = sml_arg_1 / sml_arg_2
                                    elif sml.flag == '//':
                                        sml.run_result = sml_arg_1 // sml_arg_2
                                    elif sml.flag == '%':
                                        sml.run_result = sml_arg_1 % sml_arg_2

                                    sml_run_result_label.configure(text=sml.run_result)

                # 2 вариант: арифметические операции с произвольными числами
                elif sml_code_input.get('2.0', '2.12') == 'using input;':
                    if sml_code_input.get('3.0', '3.7') != 'method=':
                        sml_error_3.configure(text='Ошибка: линия 3')
                    else:
                        if sml_code_input.get('4.0', '4.4') != 'end;':
                            sml_error_4.configure(text='Ошибка: линия 4')
                        else:
                            if sml_code_input.get('3.7') == 'с':
                                sml.flag_1 = '+'
                            elif sml_code_input.get('3.7') == 'в':
                                sml.flag_1 = '-'
                            elif sml_code_input.get('3.7') == 'у':
                                sml.flag_1 = '*'
                            elif sml_code_input.get('3.7') == 'д':
                                sml.flag_1 = '/'
                            elif sml_code_input.get('3.7') == 'ц':
                                sml.flag_1 = '//'
                            elif sml_code_input.get('3.7') == 'о':
                                sml.flag_1 = '%'
                            sml_run_window = Toplevel()
                            sml_run_window.title('run...')
                            center_window(sml_run_window, 200, 100)
                            sml_run_window.resizable(False, False)

                            sml_run_input_1 = Entry(sml_run_window, width=5)
                            sml_run_input_1.place(x=10, y=30)

                            sml_run_arg = Label(sml_run_window, text=sml.flag_1)
                            sml_run_arg.place(x=30, y=30)

                            sml_run_input_2 = Entry(sml_run_window, width=5)
                            sml_run_input_2.place(x=50, y=30)

                            sml_run_label = Label(sml_run_window, text='=')
                            sml_run_label.place(x=70, y=30)

                            sml_run_result_label = Label(sml_run_window)
                            sml_run_result_label.place(x=90, y=30)

                            sml_run_button = Button(sml_run_window, text='ВЫПОЛНИТЬ', command=ex)
                            sml_run_button.place(x=10, y=60)

    def sml_Save():
        """
        Функция сохранения исходного кода программ 
        в файл
        """
        def sml_Save_OK():
            """
            Считывание введённого имени файла 
            и его сохранение
            """
            sml_text_file = open('C:/MihaSoft Files/SML Files/' + str(sml_save_input.get()) + '.miha', "w")
            sml_text_file.write(sml_code_input.get(1.0, END))
            sml_text_file.close()
            sml_save_window.destroy()

        def sml_Save_Abort():
            """ 
            Отмена сохранения 
            """
            sml_save_window.destroy()

        sml_save_window = Toplevel()
        sml_save_window.title('Сохранение')
        center_window(sml_save_window, 350, 100)
        sml_save_window.resizable(False, False)

        sml_save_label = Label(sml_save_window, text='Введите название программы...')
        sml_save_label.place(x=5, y=5)

        # Поле ввода названия программы
        sml_save_input = Entry(sml_save_window, width=30)
        sml_save_input.place(x=10, y=40)

        sml_save_ok_button = Button(sml_save_window, text='Сохранить', bg='#c0ebd6', command=sml_Save_OK, width=10)
        sml_save_ok_button.place(x=225, y=10)

        sml_save_abort_button = Button(sml_save_window, text='Отмена', bg='#b8b8b8', command=sml_Save_Abort, width=10)
        sml_save_abort_button.place(x=225, y=50)

    def sml_Open():
        """ 
        Функция подстановки сохранённого кода
        в поле ввода
        """
        def sml_Open_OK():
            """ 
            Открытие файла и подстановка кода 
            """
            sml_text_file = open('C:/MihaSoft Files/SML Files/' + str(sml_open_combobox.get()), "r")
            sml_code_input.insert(END, sml_text_file.read())
            sml_text_file.close()
            sml_open_window.destroy()

        def sml_Open_Abort():
            """
            Отмена подстановки 
            """
            sml_open_window.destroy()

        sml_open_window = Toplevel()
        sml_open_window.title('Открыть')
        center_window(sml_open_window, 350, 120)
        sml_open_window.resizable(False, False)

        sml_open_label = Label(sml_open_window, text='Выберите файл...')
        sml_open_label.place(x=5, y=5)

        # Список существующих файлов
        sml_open_combobox = ttk.Combobox(sml_open_window, values=os.listdir('C:/MihaSoft Files/SML Files'),
                                         font=('Arial Bold', 16), width=20, state='readonly')
        sml_open_combobox.place(x=10, y=40)

        sml_open_ok_button = Button(sml_open_window, text='Открыть', bg='#c0ebd6', command=sml_Open_OK, width=10)
        sml_open_ok_button.place(x=225, y=80)

        sml_open_abort_button = Button(sml_open_window, text='Отмена', bg='#b8b8b8', command=sml_Open_Abort, width=10)
        sml_open_abort_button.place(x=135, y=80)

    def sml_Delete():
        """ 
        Функция удаления ранее сохранённого кода
        """
        def sml_Delete_OK():
            """
            Удаление выбранного файла
            """
            os.remove('C:/MihaSoft Files/SML Files/' + str(sml_delete_combobox.get()))
            sml_delete_window.destroy()

        def sml_Delete_Abort():
            """
            Отмена удаления
            """
            sml_delete_window.destroy()

        sml_delete_window = Toplevel()
        sml_delete_window.title('Удалить')
        center_window(sml_delete_window, 350, 120)
        sml_delete_window.resizable(False, False)

        sml_delete_label = Label(sml_delete_window, text='Выберите файл...')
        sml_delete_label.place(x=5, y=5)

        # Список существующих файлов
        sml_delete_combobox = ttk.Combobox(sml_delete_window, values=os.listdir('C:/MihaSoft Files/SML Files'),
                                           font=('Arial Bold', 16), width=20, state='readonly')
        sml_delete_combobox.place(x=10, y=40)

        sml_delete_ok_button = Button(sml_delete_window, text='Удалить', bg='#eb9898', command=sml_Delete_OK, width=10)
        sml_delete_ok_button.place(x=225, y=80)

        sml_delete_abort_button = Button(sml_delete_window, text='Отмена', bg='#b8b8b8', command=sml_Delete_Abort,
                                         width=10)
        sml_delete_abort_button.place(x=135, y=80)

    # Создание папки для файлов SML в случае отсутствия таковой
    if not os.path.exists('C:/MihaSoft Files/SML Files'):
        os.mkdir('C:/MihaSoft Files/SML Files')

    center_window(window, 810, 325)
    window.title('The Simplest Mihail’s Language - IDE & Compiler')

    sml_title = Label(window, text='The Simplest Mihail’s Language - IDE & Compiler', font=('Arial Bold', 26), fg='red')
    sml_title.place(x=35, y=15)

    sml_help_button = Button(window, text='Справка', bg='red', fg="white", command=sml_Help)
    sml_help_button.place(x=15, y=70)

    # Поле ввода исходного кода
    sml_code_input = Text(window, width=75, height=12)
    sml_code_input.place(x=15, y=110)
    ToolTip(sml_code_input, 'Ваш код...')

    sml_begin_button = Button(window, text='ВЫПОЛНИТЬ', bg='green', fg='white', width=15, command=sml_Begin)
    sml_begin_button.place(x=90, y=70)
    ToolTip(sml_begin_button, 'Запустить программу...')

    sml_save_button = Button(window, text='СОХРАНИТЬ', bg='yellow', width=15, command=sml_Save)
    sml_save_button.place(x=220, y=70)
    ToolTip(sml_save_button, 'Сохранить введённый код...')

    sml_open_button = Button(window, text='ОТКРЫТЬ', bg='grey', width=15, command=sml_Open)
    sml_open_button.place(x=350, y=70)
    ToolTip(sml_open_button, 'Подставить сохранённый код...')

    sml_delete_button = Button(window, text='УДАЛИТЬ', bg='#eb9898', width=15, command=sml_Delete)
    sml_delete_button.place(x=480, y=70)
    ToolTip(sml_delete_button, 'Удалить сохранённый код...')

    # Область вывода сообщений об ошибках на соответствующих строках
    sml_error_1 = Label(window, fg='red')
    sml_error_1.place(x=670, y=110)

    sml_error_2 = Label(window, fg='red')
    sml_error_2.place(x=670, y=140)

    sml_error_3 = Label(window, fg='red')
    sml_error_3.place(x=670, y=170)

    sml_error_4 = Label(window, fg='red')
    sml_error_4.place(x=670, y=200)

    sml_error_5 = Label(window, fg='red')
    sml_error_5.place(x=670, y=230)

    sml_error_6 = Label(window, fg='red')
    sml_error_6.place(x=670, y=260)

    sml_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                     command=sml_to_home)
    sml_off.place(x=0, y=5)
    ToolTip(sml_off, 'На главную...')


def TrunsNumSystem():
    """
    Приложение для перевода чисел из одной
    системы счисления в другую
    Подробнее - https://mihasoft.glitch.me/tns.html
    """
    def tns_to_home():
        """ 
        Возвращение на главную страницу MihaSoft
        """
        tns_title.destroy()
        tns_label_1.destroy()
        tns_label_2.destroy()
        tns_label_3.destroy()
        tns_input.destroy()
        tns_output.destroy()
        tns_off.destroy()
        tns_re_button.destroy()
        tns_clean_button.destroy()
        tns_from_combobox.destroy()
        tns_to_combobox.destroy()
        home()
        center_window(window, 790, 870)
        
    def tns_Begin():
        """ 
        Перевод числа
        """
        def lol(to, _from):
            """
            Функция непосредственного перевода
            """
            tns_begin_num = int(tns_input.get())
            tns_begin_n = int(tns_begin_num, _from) if isinstance(tns_begin_num, str) else tns_begin_num
            tns_begin_voc = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Список символов для перевода
            tns_begin_res = ''
            while tns_begin_n > 0:
                tns_begin_n, tns_begin_m = divmod(tns_begin_n, to)
                tns_begin_res += tns_begin_voc[tns_begin_m]
            tns_output.insert(1.0, tns_begin_res[::-1])  # Разворот числа

        # Проверка корректности введённых чисел
        if tns_from_combobox.get().isdigit() and tns_to_combobox.get().isdigit() and tns_input.get().isdigit():
            lol(int(tns_to_combobox.get()), int(tns_from_combobox.get()))
        else:
            messagebox.showerror('Ошибка!', 'Введены некорректные значения!')

    def tns_Clean():
        """
        Функция очистки поля вывода
        результата перевода
        """
        tns_output.delete(1.0, END)

    center_window(window, 620, 430)
    window.title('TrunsNumSystem 2.0')

    tns_title = Label(window, text='TrunsNumSystem 2.0', font=('Arial Bold', 15), fg='red')
    tns_title.place(x=40, y=20)

    tns_label_1 = Label(window, text='Введите значение:')
    tns_label_1.place(x=20, y=300)

    tns_label_2 = Label(window, text='ИЗ')
    tns_label_2.place(x=20, y=80)

    tns_label_3 = Label(window, text='В')
    tns_label_3.place(x=20, y=190)

    tns_input = Entry(window, width=24, font=('Arial Bold', 15))
    tns_input.place(x=20, y=320)
    ToolTip(tns_input, 'Только цифры!')

    tns_re_button = Button(window, text='Перевести', bg='white', fg='black', width=15, command=tns_Begin)
    tns_re_button.place(x=340, y=100)

    tns_clean_button = Button(window, text='Очистить', bg='red', fg='white', width=15, command=tns_Clean)
    tns_clean_button.place(x=470, y=100)
    ToolTip(tns_clean_button, 'Очистить поле вывода...')

    # Генерация списка допустимых исходных систем счисления
    tns_list = []
    for i in range(2, 46):
        tns_list.append(str(i))

    tns_from_combobox = ttk.Combobox(window, values=tns_list, font=('Arial Bold', 16), state='readonly')
    tns_from_combobox.place(x=20, y=100)

    # Генерация списка допустимых выходных систем счисления
    tns_list.clear()
    for i in range(2, 42):
        tns_list.append(str(i))

    tns_to_combobox = ttk.Combobox(window, values=tns_list, font=('Arial Bold', 16), state='readonly')
    tns_to_combobox.place(x=20, y=210)

    # Поле вывода результата
    tns_output = Text(window, width=30, height=13)
    tns_output.place(x=340, y=130)

    tns_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                     command=tns_to_home)
    tns_off.place(x=0, y=5)
    ToolTip(tns_off, 'На главную...')


def CrossZero():
    """
    Игра "Крестики-нолики"
    """
    # Создание объекта с глобальными переменными
    cz = CrossZeroGlobals()

    def cz_to_home():
        cz_title.destroy()
        cz_name_of_winner_label.destroy()
        cz_numb_of_moves_label.destroy()
        cz_info_label.destroy()
        cz_game_condition_label.destroy()
        cz_save_button.destroy()
        cz_open_button.destroy()
        cz_delete_button.destroy()
        cz_new_game_button.destroy()
        cz_parametrs_button.destroy()
        cz_box_1.destroy()
        cz_box_2.destroy()
        cz_box_3.destroy()
        cz_box_4.destroy()
        cz_box_5.destroy()
        cz_box_6.destroy()
        cz_box_7.destroy()
        cz_box_8.destroy()
        cz_box_9.destroy()
        cz_off.destroy()
        home()
        center_window(window, 790, 870)

    def cz_parametrs():
        """
        Функция определения имён игроков
        """
        def cz_save_parametrs():
            """
            Функция сохранения выбранных параметров
            """
            cz.player_1 = str(cz_parametrs_input_1.get())
            cz.player_2 = str(cz_parametrs_input_2.get())
            cz.naming_condition = 1
            cz_parametrs_window.destroy()

        def cz_close_parametrs():
            """
            Закрытие окна без сохранения параметров
            """
            cz_parametrs_window.destroy()

        cz_parametrs_window = Toplevel()
        cz_parametrs_window.title('Параметры')
        center_window(cz_parametrs_window, 300, 110)
        cz_parametrs_window.resizable(False, False)

        cz_parametrs_label_1 = Label(cz_parametrs_window, text='Имя первого игрока:')
        cz_parametrs_label_1.place(x=5, y=5)

        # Поле ввода имени первого игрока (крестик)
        cz_parametrs_input_1 = Entry(cz_parametrs_window, width=17)
        cz_parametrs_input_1.place(x=130, y=5)

        cz_parametrs_label_2 = Label(cz_parametrs_window, text='Имя второго игрока:')
        cz_parametrs_label_2.place(x=5, y=40)

        # Поле ввода имени второго игрока (нолик)
        cz_parametrs_input_2 = Entry(cz_parametrs_window, width=17)
        cz_parametrs_input_2.place(x=130, y=40)

        cz_parametrs_save_button = Button(cz_parametrs_window, text='ОК', bg='#c0ebd6', width=10,
                                          command=cz_save_parametrs)
        cz_parametrs_save_button.place(x=180, y=70)

        cz_close_button = Button(cz_parametrs_window, text='Отмена', bg='#b8b8b8', width=10, command=cz_close_parametrs)
        cz_close_button.place(x=80, y=70)

    def cz_new_game():
        """
        Функция сброса параметров текущей игры
        и начало новой
        """
        # Счётчик количества ходов
        cz.number_of_moves = 0
        
        # Переменная, отмечающая ход игры или её завершение
        cz.game_condition = True
        
        # Переменная, отмечающая наличие ничьи или победы одного из игроков
        cz.game_res_condition = False
        cz_numb_of_moves_label.configure(text='1')
        cz_info_label.configure(text='  ход')
        cz_box_1.configure(text='')
        cz_box_2.configure(text='')
        cz_box_3.configure(text='')
        cz_box_4.configure(text='')
        cz_box_5.configure(text='')
        cz_box_6.configure(text='')
        cz_box_7.configure(text='')
        cz_box_8.configure(text='')
        cz_box_9.configure(text='')
        cz_game_condition_label.configure(text='')
        cz_name_of_winner_label.configure(text='')
        
        # Переменные, регулирующие состояние каждой клетки игрового поля
        cz.flag_1 = 3
        cz.flag_2 = 3
        cz.flag_3 = 3
        cz.flag_4 = 3
        cz.flag_5 = 3
        cz.flag_6 = 3
        cz.flag_7 = 3
        cz.flag_8 = 3
        cz.flag_9 = 3

    def cz_check_gameover():
        """
        Функция, проверяющая при каждом нажатии на клетку поля
        наличие ситуации, знаменующей завершение игры
        """

        def cz_cg_to_zero():
            cz.flag_1 = cz.flag_2 = cz.flag_3 = cz.flag_4 = cz.flag_5 = cz.flag_6 = cz.flag_7 = cz.flag_8 = \
                cz.flag_9 = 0

        def cz_req_new_game():
            def cz_rng_yes():
                cz_new_game()
                cz_rng_window.destroy()

            def cz_rng_no():
                cz_rng_window.destroy()

            cz_rng_window = Toplevel()
            cz_rng_window.title('Новая игра')
            center_window(cz_rng_window, 200, 100)
            cz_rng_window.resizable(False, False)

            cz_rng_label = Label(cz_rng_window, text='Начать новую игру?')
            cz_rng_label.place(x=5, y=5)

            cz_rng_yes_button = Button(cz_rng_window, text='ДА', bg='#c0ebd6', width=10, command=cz_rng_yes)
            cz_rng_yes_button.place(x=10, y=45)

            cz_rng_no_button = Button(cz_rng_window, text='НЕТ', bg='#ebc0d0', width=10, command=cz_rng_no)
            cz_rng_no_button.place(x=110, y=45)

        cz_numb_of_moves_label.configure(text=cz.number_of_moves + 2)

        # cz.flag = 1 : крестик; cz.flag = 0 : нолик
        if ((cz.flag_1 == 1 and cz.flag_2 == 1 and cz.flag_3 == 1) or (
                cz.flag_4 == 1 and cz.flag_5 == 1 and cz.flag_6 == 1) or (
                cz.flag_7 == 1 and cz.flag_8 == 1 and cz.flag_9 == 1) or (
                cz.flag_1 == 1 and cz.flag_4 == 1 and cz.flag_7 == 1) or (
                cz.flag_2 == 1 and cz.flag_5 == 1 and cz.flag_8 == 1) or (
                cz.flag_3 == 1 and cz.flag_6 == 1 and cz.flag_9 == 1) or (
                cz.flag_1 == 1 and cz.flag_5 == 1 and cz.flag_9 == 1) or (
                cz.flag_3 == 1 and cz.flag_5 == 1 and cz.flag_7 == 1)):
            cz_cg_to_zero()
            cz.game_condition = False
            cz.game_res_condition = False
            cz_game_condition_label.configure(text='Победил')
            cz.condition = 1
            if cz.naming_condition == 0:
                cz_name_of_winner_label.configure(text='Игрок 1')
            else:
                cz_name_of_winner_label.configure(text=cz.player_1)
            cz_numb_of_moves_label.configure(text=cz.number_of_moves + 1)
            cz_info_label.configure(text='  ходов')
            cz_req_new_game()
            cz.winner = cz.player_1
        elif ((cz.flag_1 == 0 and cz.flag_2 == 0 and cz.flag_3 == 0) or (
                cz.flag_4 == 0 and cz.flag_5 == 0 and cz.flag_6 == 0) or (
                      cz.flag_7 == 0 and cz.flag_8 == 0 and cz.flag_9 == 0) or (
                      cz.flag_1 == 0 and cz.flag_4 == 0 and cz.flag_7 == 0) or (
                      cz.flag_2 == 0 and cz.flag_5 == 0 and cz.flag_8 == 0) or (
                      cz.flag_3 == 0 and cz.flag_6 == 0 and cz.flag_9 == 0) or (
                      cz.flag_1 == 0 and cz.flag_5 == 0 and cz.flag_9 == 0) or (
                      cz.flag_3 == 0 and cz.flag_5 == 0 and cz.flag_7 == 0)):
            cz_cg_to_zero()
            cz.game_condition = False
            cz.game_res_condition = False
            cz_game_condition_label.configure(text='Победил')
            cz.condition = 2
            if cz.naming_condition == 0:
                cz_name_of_winner_label.configure(text='Игрок 2')
            else:
                cz_name_of_winner_label.configure(text=cz.player_2)
            cz_numb_of_moves_label.configure(text=cz.number_of_moves + 1)
            cz_info_label.configure(text='  ходов')
            cz_req_new_game()
            cz.winner = cz.player_2
        # cz.flag = 3 : клетка не была нажата
        elif (cz.flag_1 != 3) and (cz.flag_2 != 3) and (cz.flag_3 != 3) and (cz.flag_4 != 3) and (
                cz.flag_5 != 3) and (cz.flag_6 != 3) and (cz.flag_7 != 3) and (cz.flag_8 != 3) and (
                cz.flag_9 != 3):
            cz_cg_to_zero()
            cz.condition = 4
            cz.game_condition = False
            cz.game_res_condition = True
            cz_game_condition_label.configure(text='НИЧЬЯ!')
            cz_req_new_game()

    # Функции нажатия для каждой клетки
    def cz_on_click_1():
        if cz.flag_1 != 1 and cz.flag_1 != 0:
            if cz.number_of_moves % 2 == 0:
                cz_box_1.configure(text='╳')
                cz.flag_1 = 1
            else:
                cz_box_1.configure(text='◯')
                cz.flag_1 = 0
            cz_check_gameover()
            cz.number_of_moves += 1

    def cz_on_click_2():
        if cz.flag_2 != 1 and cz.flag_2 != 0:
            if cz.number_of_moves % 2 == 0:
                cz_box_2.configure(text='╳')
                cz.flag_2 = 1
            else:
                cz_box_2.configure(text='◯')
                cz.flag_2 = 0
            cz_check_gameover()
            cz.number_of_moves += 1

    def cz_on_click_3():
        if cz.flag_3 != 1 and cz.flag_3 != 0:
            if cz.number_of_moves % 2 == 0:
                cz_box_3.configure(text='╳')
                cz.flag_3 = 1
            else:
                cz_box_3.configure(text='◯')
                cz.flag_3 = 0
            cz_check_gameover()
            cz.number_of_moves += 1

    def cz_on_click_4():
        if cz.flag_4 != 1 and cz.flag_4 != 0:
            if cz.number_of_moves % 2 == 0:
                cz_box_4.configure(text='╳')
                cz.flag_4 = 1
            else:
                cz_box_4.configure(text='◯')
                cz.flag_4 = 0
            cz_check_gameover()
            cz.number_of_moves += 1

    def cz_on_click_5():
        if cz.flag_5 != 1 and cz.flag_5 != 0:
            if cz.number_of_moves % 2 == 0:
                cz_box_5.configure(text='╳')
                cz.flag_5 = 1
            else:
                cz_box_5.configure(text='◯')
                cz.flag_5 = 0
            cz_check_gameover()
            cz.number_of_moves += 1

    def cz_on_click_6():
        if cz.flag_6 != 1 and cz.flag_6 != 0:
            if cz.number_of_moves % 2 == 0:
                cz_box_6.configure(text='╳')
                cz.flag_6 = 1
            else:
                cz_box_6.configure(text='◯')
                cz.flag_6 = 0
            cz_check_gameover()
            cz.number_of_moves += 1

    def cz_on_click_7():
        if cz.flag_7 != 1 and cz.flag_7 != 0:
            if cz.number_of_moves % 2 == 0:
                cz_box_7.configure(text='╳')
                cz.flag_7 = 1
            else:
                cz_box_7.configure(text='◯')
                cz.flag_7 = 0
            cz_check_gameover()
            cz.number_of_moves += 1

    def cz_on_click_8():
        if cz.flag_8 != 1 and cz.flag_8 != 0:
            if cz.number_of_moves % 2 == 0:
                cz_box_8.configure(text='╳')
                cz.flag_8 = 1
            else:
                cz_box_8.configure(text='◯')
                cz.flag_8 = 0
            cz_check_gameover()
            cz.number_of_moves += 1

    def cz_on_click_9():
        if cz.flag_9 != 1 and cz.flag_9 != 0:
            if cz.number_of_moves % 2 == 0:
                cz_box_9.configure(text='╳')
                cz.flag_9 = 1
            else:
                cz_box_9.configure(text='◯')
                cz.flag_9 = 0
            cz_check_gameover()
            cz.number_of_moves += 1

    def cz_save_report():
        """
        Функция сохранения отчёта об игре
        """
        # Проверка наличия завершённой игры для сохранения отчёта
        if cz.game_condition:
            messagebox.showwarning('Ошибка!', 'Вы не завершили игру!')

        else:
            def cz_save_report_ok():
                """
                Создание строки отчёта и запись её в файл
                """
                if cz.condition == 1 or cz.condition == 2 or cz.condition == 4:
                    if cz.condition == 1 and cz.naming_condition == 0:
                        cz.name_of_winner_str = 'Игрок 1'
                    elif cz.condition == 2 and cz.naming_condition == 0:
                        cz.name_of_winner_str = 'Игрок 2'
                    else:
                        cz.name_of_winner_str = str(cz.winner)
                else:
                    messagebox.showinfo('Ошибка!', 'Нет завершённых игр!')

                cz_number_of_moves_str = str(cz.number_of_moves)

                if cz.game_res_condition:
                    cz_save_string = 'Ничья ' + ' за ' + cz_number_of_moves_str + ' ходов. '
                else:
                    cz_save_string = 'Победил ' + cz.name_of_winner_str + ' за ' + cz_number_of_moves_str + ' ходов. '

                cz_now = datetime.datetime.now()
                cz_text_file = open(
                    'C:/MihaSoft Files/CZ Files/Log_' + str(cz_now.strftime('%d-%m-%Y %H.%M')) + '.miha', 'w')
                cz_text_file.write(cz_save_string)
                cz_text_file.close()
                cz_save_window.destroy()

            def cz_save_report_abort():
                """
                Отмена сохранения отчёта
                """
                cz_save_window.destroy()

            cz_save_window = Toplevel()
            cz_save_window.title('Сохранение')
            center_window(cz_save_window, 265, 100)
            cz_save_window.resizable(False, False)

            cz_save_label = Label(cz_save_window, text='Сохранить отчёт об игре?')
            cz_save_label.place(x=5, y=5)

            cz_save_ok_button = Button(cz_save_window, text='ДА', bg='#c0ebd6', width=10, command=cz_save_report_ok)
            cz_save_ok_button.place(x=25, y=45)

            cz_save_abort_button = Button(cz_save_window, text='НЕТ', bg='#ebc0d0', width=10,
                                          command=cz_save_report_abort)
            cz_save_abort_button.place(x=125, y=45)

    def cz_open_report():
        """
        Функция вывода ранее сохранённого отчёта
        """

        def cz_open_ok():
            """
            Открытие выбранного отчёта в отдельном окне
            """
            def cz_close_report():
                """
                Функция закрытия окна с отчётом
                """
                cz_report_window.destroy()

            cz_report_name = str(cz_open_combobox.get())
            cz_open_window.destroy()

            cz_report_window = Toplevel()
            cz_report_window.title("Отчёт")
            center_window(cz_report_window, 200, 100)
            cz_report_window.resizable(False, False)

            # Область вывода строки отчёта
            cz_report = Label(cz_report_window, text="")
            cz_report.place(x=5, y=5)

            cz_report_close_button = Button(cz_report_window, text='OK', command=cz_close_report)
            cz_report_close_button.place(x=15, y=35)

            # Открытие файла с отчётом и вывод сттоки на экран
            cz_report_file = open("C:/MihaSoft Files/CZ Files/" + cz_report_name, "r")
            cz_report.configure(text=str(cz_report_file.readline()))
            cz_report_file.close()

        def cz_open_abort():
            """
            Закрытие окна выбора отчёта
            """
            cz_open_window.destroy()

        cz_open_window = Toplevel()
        cz_open_window.title('Открыть отчёт')
        center_window(cz_open_window, 385, 140)
        cz_open_window.resizable(False, False)

        cz_open_label = Label(cz_open_window, text='Выберите запись...')
        cz_open_label.place(x=5, y=5)

        # Список существующих отчётов
        cz_open_combobox = ttk.Combobox(cz_open_window, values=os.listdir('C:/MihaSoft Files/CZ Files'),
                                        font=("Arial Bold", 16), width=27, state="readonly")
        cz_open_combobox.place(x=10, y=40)

        cz_open_ok_button = Button(cz_open_window, text='Открыть', bg='#c0ebd6', width=10, command=cz_open_ok)
        cz_open_ok_button.place(x=280, y=90)

        cz_open_abort_button = Button(cz_open_window, text='Отмена', bg='#b8b8b8', width=10, command=cz_open_abort)
        cz_open_abort_button.place(x=170, y=90)

    def cz_delete_report():
        """
        Функция удаления отчётов об играх
        """
        def cz_delete_ok():
            """
            Удаление выбранного отчёта
            """
            os.remove('C:/MihaSoft Files/CZ Files/' + str(cz_delete_combobox.get()))
            cz_delete_window.destroy()

        def cz_delete_abort():
            """
            Отмена удаления
            """
            cz_delete_window.destroy()

        cz_delete_window = Toplevel()
        cz_delete_window.title('Удалить отчёт')
        center_window(cz_delete_window, 385, 140)
        cz_delete_window.resizable(False, False)

        cz_delete_label = Label(cz_delete_window, text='Выберите запись...')
        cz_delete_label.place(x=5, y=5)
        
        # Список существующих отчётов
        cz_delete_combobox = ttk.Combobox(cz_delete_window, values=os.listdir('C:/MihaSoft Files/CZ Files'),
                                          font=('Arial Bold', 16), width=27, state='readonly')
        cz_delete_combobox.place(x=10, y=40)

        cz_delete_ok_button = Button(cz_delete_window, text='Удалить', bg='#eb9898', width=10, command=cz_delete_ok)
        cz_delete_ok_button.place(x=280, y=90)

        cz_delete_abort_button = Button(cz_delete_window, text='Отмена', bg='#b8b8b8', width=10,
                                        command=cz_delete_abort)
        cz_delete_abort_button.place(x=170, y=90)

    # Создание папки для отчётов в случае отсутствия таковой
    if not os.path.exists('C:/MihaSoft Files/CZ Files'):
        os.mkdir('C:/MihaSoft Files/CZ Files')

    center_window(window, 790, 600)
    window.title('CrossZero 2.1')

    cz_title = Label(window, text='КРЕСТИКИ - НОЛИКИ', font=('Times New Roman', 26), fg='red')
    cz_title.place(x=215, y=10)

    # Клетки
    cz_box_1 = Button(window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=7, height=3,
                      command=cz_on_click_1)
    cz_box_1.place(x=170, y=80)

    cz_box_2 = Button(window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=7, height=3,
                      command=cz_on_click_2)
    cz_box_2.place(x=320, y=80)

    cz_box_3 = Button(window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=7, height=3,
                      command=cz_on_click_3)
    cz_box_3.place(x=470, y=80)

    cz_box_4 = Button(window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=7, height=3,
                      command=cz_on_click_4)
    cz_box_4.place(x=170, y=235)

    cz_box_5 = Button(window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=7, height=3,
                      command=cz_on_click_5)
    cz_box_5.place(x=320, y=235)

    cz_box_6 = Button(window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=7, height=3,
                      command=cz_on_click_6)
    cz_box_6.place(x=470, y=235)

    cz_box_7 = Button(window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=7, height=3,
                      command=cz_on_click_7)
    cz_box_7.place(x=170, y=390)

    cz_box_8 = Button(window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=7, height=3,
                      command=cz_on_click_8)
    cz_box_8.place(x=320, y=390)

    cz_box_9 = Button(window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=7, height=3,
                      command=cz_on_click_9)
    cz_box_9.place(x=470, y=390)

    cz_parametrs_button = Button(window, text='Параметры', font=('Times New Roman', 14), fg='blue', bg='#ddc0eb',
                                 command=cz_parametrs)
    cz_parametrs_button.place(x=20, y=80)
    ToolTip(cz_parametrs_button, 'Присвоить игрокам произвольные имена...')

    cz_new_game_button = Button(window, text='Новая игра', font=('Times New Roman', 14), fg='blue', bg='#c0ebcb',
                                command=cz_new_game)
    cz_new_game_button.place(x=20, y=160)
    ToolTip(cz_new_game_button, 'Обновить поле и начать новую игру...')

    cz_save_button = Button(window, text='Сохранить\n отчёт', font=('Times New Roman', 14), fg='blue', bg='#e0cf92',
                            command=cz_save_report)
    cz_save_button.place(x=20, y=240)
    ToolTip(cz_save_button, 'Сохранить отчёт о последней игре...')

    cz_open_button = Button(window, text='Открыть\n отчёт', font=('Times New Roman', 14), fg='blue', bg='#87e6ad',
                            command=cz_open_report)
    cz_open_button.place(x=20, y=350)
    ToolTip(cz_open_button, 'Открыть отчёт в новом окне...')

    cz_delete_button = Button(window, text='Удалить\n отчёт', font=('Times New Roman', 14), fg='blue', bg='#eb9898',
                              command=cz_delete_report)
    cz_delete_button.place(x=20, y=460)
    ToolTip(cz_delete_button, 'Удалить существующий отчёт...')

    # Строки вывода информации о результате игры
    cz_game_condition_label = Label(window, font=('Times New Roman', 20), fg='blue')
    cz_game_condition_label.place(x=630, y=140)

    cz_name_of_winner_label = Label(window, font=('Times New Roman', 20), fg='blue')
    cz_name_of_winner_label.place(x=630, y=200)

    cz_numb_of_moves_label = Label(window, text='1', font=('Times New Roman', 20), fg='blue')
    cz_numb_of_moves_label.place(x=630, y=80)

    cz_info_label = Label(window, text='ХОД', font=('Times New Roman', 20), fg='blue')
    cz_info_label.place(x=670, y=80)

    cz_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=cz_to_home)
    cz_off.place(x=0, y=5)
    ToolTip(cz_off, 'На главную...')


def MihNote():
    """
    Блокнот
    """
    # Создание объекта с глобальными переменными
    mn = MihNoteGlobals()

    def mn_to_home():
        """
        Возвращение на главную страницу MihaSoft
        """
        mn_title.destroy()
        mn_line.destroy()
        mn_new_note_button.destroy()
        mn_delete_button.destroy()
        mn_open_button.destroy()
        mn_edit_button.destroy()
        mn_note_ground.destroy()
        mn_off.destroy()

        # Удаление виджетов, появляющихся в процессе работы приложения
        # если они не были удалены до этого
        try:
            mn.open_combobox.destroy()
            mn.open_ok_button.destroy()
        except AttributeError:
            pass

        try:
            mn.delete_combobox.destroy()
            mn.delete_ask_button.destroy()
        except AttributeError:
            pass

        try:
            mn.edit_combobox.destroy()
            mn.edit_ok_button.destroy()
        except AttributeError:
            pass

        home()
        center_window(window, 790, 870)

    def mn_new_note():
        """
        Функция создания новой заметки
        """
        def mn_save_note():
            """
            Функция сохранения созданной заметки
            """
            def mn_save_note_ok():
                """
                Подтверждение сохранения
                """
                mn_text_file = open('C:/MihaSoft Files/MihNote Files/' + str(mn_save_input.get()) + '.miha', 'w')
                mn_text_file.write(mn_new_note_ground.get(1.0, END))
                mn_text_file.close()
                mn_save_window.destroy()
                mn_new_note_window.destroy()

            def mn_save_note_abort():
                """
                Отмена сохранения
                """
                mn_save_window.destroy()

            mn_save_window = Toplevel()
            center_window(mn_save_window, 300, 100)
            mn_save_window.resizable(False, False)
            mn_save_window.title('Сохранение')

            mn_save_label = Label(mn_save_window, text='Введите название файла:')
            mn_save_label.place(x=5, y=5)

            # Поле ввода названия заметки
            mn_save_input = Entry(mn_save_window, width=20)
            mn_save_input.place(x=10, y=35)

            mn_save_label_1 = Label(mn_save_window, text='.miha')
            mn_save_label_1.place(x=125, y=35)

            mn_save_ok_button = Button(mn_save_window, text='Сохранить', font=('Arial Bold', 10), bg='#b2e6ae',
                                       width=13,
                                       command=mn_save_note_ok)
            mn_save_ok_button.place(x=170, y=60)

            mn_save_abort_button = Button(mn_save_window, text='Отмена', font=('Arial Bold', 10), bg='#b8b8b8',
                                          width=13,
                                          command=mn_save_note_abort)
            mn_save_abort_button.place(x=170, y=20)

        def mn_close_nn_window():
            """
            Отмена создания новой заметки
            """
            mn_new_note_window.destroy()

        mn_new_note_window = Toplevel()
        center_window(mn_new_note_window, 450, 400)
        mn_new_note_window.resizable(False, False)
        mn_new_note_window.title('Создание новой заметки')

        mn_nn_save_button = Button(mn_new_note_window, text='Сохранить', font=('Arial Bold', 12), bg='#b2e6ae',
                                   width=13,
                                   command=mn_save_note)
        mn_nn_save_button.place(x=15, y=5)

        # Поле ввода текста новой заметки
        mn_new_note_ground = Text(mn_new_note_window, width=50, height=15)
        mn_new_note_ground.place(x=15, y=50)

        mn_nn_close_button = Button(mn_new_note_window, text='Отмена', font=('Arial Bold', 12), bg='#b8b8b8', width=13,
                                    command=mn_close_nn_window)
        mn_nn_close_button.place(x=290, y=5)

    def mn_open_note():
        """
        Функция открытия сохранённой заметки
        """
        # Очистка поля вывода заметки
        mn_note_ground.configure(text='')

        def open_note_ok():
            """
            Подтверждение открытия
            """
            # Проверка наличия существующих заметок
            if os.listdir('C:/MihaSoft Files/MihNote Files'):
                mn_file_name = str(mn.open_combobox.get())
                # Удаление виджетов открытия
                mn.open_combobox.destroy()
                mn.open_ok_button.destroy()
                mn_open_text_file = open('C:/MihaSoft Files/MihNote Files/' + mn_file_name, 'r')
                mn_note_ground.configure(text=str(mn_open_text_file.read()))
                mn_open_text_file.close()

        # Список существующих заметок
        mn.open_combobox = ttk.Combobox(window, values=os.listdir('C:/MihaSoft Files/MihNote Files'),
                                        font=('Arial Bold', 16), state='readonly')
        mn.open_combobox.place(x=20, y=60)

        mn.open_ok_button = Button(window, text='Открыть', font=('Arial Bold', 10), bg='#7bd491', width=14,
                                   command=open_note_ok)
        mn.open_ok_button.place(x=300, y=60)

    def mn_delete_note():
        """
        Функция удаления существующей заметки
        """
        # Очистка поля вывода заметки
        mn_note_ground.configure(text="")

        def mn_delete_ask():
            """
            Вывод окна с запросом
            о подтверждении удаления
            """
            # Проверка наличия существующих заметок
            if os.listdir('C:/MihaSoft Files/MihNote Files'):
                def mn_delete_ok():
                    mn_delete_file_name = str(mn.delete_combobox.get())
                    # Удаление виджетов удаления
                    mn.delete_combobox.destroy()
                    mn.delete_ask_button.destroy()
                    os.remove('C:/MihaSoft Files/MihNote Files/' + mn_delete_file_name)
                    mn_delete_window.destroy()

                def CloseDel():
                    """
                    Отмена удаления
                    """
                    mn_delete_window.destroy()

                mn_delete_window = Toplevel()
                center_window(mn_delete_window, 300, 100)
                mn_delete_window.resizable(False, False)
                mn_delete_window.title("Удаление")

                mn_delete_label = Label(mn_delete_window, text="Удалить файл?")
                mn_delete_label.place(x=5, y=5)

                mn_delete_ok_button = Button(mn_delete_window, text="ОК", font=("Arial Bold", 10), fg="black",
                                             bg='#c97979', width=13, command=mn_delete_ok)
                mn_delete_ok_button.place(x=170, y=60)

                mn_close_button = Button(mn_delete_window, text='Отмена', font=('Arial Bold', 10), bg='#b8b8b8',
                                         width=13,
                                         command=CloseDel)
                mn_close_button.place(x=170, y=15)

        # Список существующих заметок
        mn.delete_combobox = ttk.Combobox(window, values=os.listdir('C:/MihaSoft Files/MihNote Files'),
                                          font=('Arial Bold', 16), state='readonly')
        mn.delete_combobox.place(x=20, y=60)

        mn.delete_ask_button = Button(window, text='Удалить', font=('Arial Bold', 10), fg="black", bg='#c97979',
                                      width=14,
                                      command=mn_delete_ask)
        mn.delete_ask_button.place(x=300, y=60)

    def mn_edit_note():
        """
        Функция редактирования существующей заметки
        """
        mn_note_ground.configure(text='')

        def mn_edit_ok():
            """
            Функция сохранения внесённых изменений
            """
            # Проверка наличия существующих заметок
            if os.listdir('C:/MihaSoft Files/MihNote Files'):
                def save_changes():
                    """
                    Полтверждение сохранения изменений
                    """
                    mn_edit_file = open('C:/MihaSoft Files/MihNote Files/' + mn_edit_file_name, 'w')
                    mn_edit_file.write(mn_edit_ground.get(1.0, END))
                    mn_edit_file.close()
                    mn_edit_window.destroy()

                def mn_edit_abort():
                    """
                    Отмена сохранения изменений
                    """
                    mn_edit_window.destroy()

                mn_edit_file_name = str(mn.edit_combobox.get())
                mn.edit_combobox.destroy()
                mn.edit_ok_button.destroy()

                mn_edit_window = Toplevel()
                center_window(mn_edit_window, 450, 400)
                mn_edit_window.resizable(False, False)
                mn_edit_window.title('Редактирование')

                mn_sch_button = Button(mn_edit_window, text='Сохранить', font=('Arial Bold', 12), bg='#b2e6ae',
                                       width=13,
                                       command=save_changes)
                mn_sch_button.place(x=15, y=5)

                # Поле вывода текста для редактирования
                mn_edit_ground = Text(mn_edit_window, width=50, height=15)
                mn_edit_ground.place(x=15, y=50)

                # Открытие выбранного файла и вывод текста заметки в поле редактирования
                mn_edit_open_file = open('C:/MihaSoft Files/MihNote Files/' + mn_edit_file_name, 'r')
                mn_edit_ground.insert(END, mn_edit_open_file.read())
                mn_edit_open_file.close()

                mn_close_button = Button(mn_edit_window, text='Отмена', font=('Arial Bold', 12), bg='#b8b8b8', width=13,
                                         command=mn_edit_abort)
                mn_close_button.place(x=290, y=5)

        # Список существующих заметок
        mn.edit_combobox = ttk.Combobox(window, values=os.listdir('C:/MihaSoft Files/MihNote Files'),
                                        font=('Arial Bold', 16), state='readonly')
        mn.edit_combobox.place(x=20, y=60)

        mn.edit_ok_button = Button(window, text='Редактировать', font=('Arial Bold', 10), bg='#79a7c9', width=14,
                                   command=mn_edit_ok)
        mn.edit_ok_button.place(x=300, y=60)

    # Создание папки для заметок в случае отсутствия таковой
    if not os.path.exists('C:/MihaSoft Files/MihNote Files'):
        os.mkdir('C:/MihaSoft Files/MihNote Files')

    center_window(window, 800, 700)
    window.title('MihNote 1.1')

    mn_title = Label(window, text='MihNote 1.1', font=('Arial Bold', 16), fg='red')
    mn_title.place(x=80, y=10)

    mn_open_button = Button(window, text='Открыть', font=('Arial Bold', 12), bg='#e6aeae', width=13,
                            command=mn_open_note)
    mn_open_button.place(x=210, y=10)
    ToolTip(mn_open_button, 'Открыть файл...')

    mn_edit_button = Button(window, text='Редактировать', font=('Arial Bold', 12), bg='#aeb4e6', width=13,
                            command=mn_edit_note)
    mn_edit_button.place(x=350, y=10)
    ToolTip(mn_edit_button, 'Редактировать существующий файл...')

    mn_new_note_button = Button(window, text='Создать', font=('Arial Bold', 12), bg='#aee6c9', width=13,
                                command=mn_new_note)
    mn_new_note_button.place(x=490, y=10)
    ToolTip(mn_new_note_button, 'Создать новый файл...')

    mn_delete_button = Button(window, text='Удалить', font=('Arial Bold', 12), bg='#e6e2ae', width=13,
                              command=mn_delete_note)
    mn_delete_button.place(x=630, y=10)
    ToolTip(mn_delete_button, 'Удалить файл...')

    # Линия, отграждающая кнопок от области вывода заметок
    mn_line = Label(window,
                    text='_' * 154)
    mn_line.place(x=10, y=90)

    # Область вывода заметок
    mn_note_ground = Label(window, font=('Arial Bold', 16))
    mn_note_ground.place(x=50, y=120)

    mn_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg="white",
                    command=mn_to_home)

    mn_off.place(x=0, y=5)
    ToolTip(mn_off, 'На главную...')


def WindowManager():
    """
    Приложения для создания и сохранение окон 
    с надписями
    """
    # Создание объекта с глобальными переменными
    wm = WindowManagerGlobals()

    def wm_to_home():
        """
        Возвращение на главную страницу MihaSoft
        """
        wm_title.destroy()
        wm_label_1.destroy()
        wm_label_2.destroy()
        wm_label_3.destroy()
        wm_label_4.destroy()
        wm_label_5.destroy()
        wm_label_6.destroy()
        wm_label_8.destroy()
        wm_label_9.destroy()
        wm_label_10.destroy()
        wm_label_11.destroy()
        wm_label_12.destroy()
        wm_label_13.destroy()
        wm_label_14.destroy()
        wm_width_input.destroy()
        wm_height_input.destroy()
        wm_x_cord_input.destroy()
        wm_y_cord_input.destroy()
        wm_cust_title_input.destroy()
        wm_text_x_input.destroy()
        wm_text_y_input.destroy()
        wm_font_combobox.destroy()
        wm_fsize_combobox.destroy()
        wm_text_ground.destroy()
        wm_font_demo.destroy()
        wm_fsize_demo.destroy()
        wm_demo_ground.destroy()
        wm_choose_button.destroy()
        wm_create_button.destroy()
        wm_save_button.destroy()
        wm_open_button.destroy()
        wm_clean_button.destroy()
        wm_delete_button.destroy()
        wm_edit_button.destroy()
        wm_off.destroy()
        home()
        center_window(window, 790, 870)

    def wm_read_data():
        """
        Функция считывания введённых параметров
        окна и запись их в переменные
        """
        wm.width = str(wm_width_input.get())
        wm.height = str(wm_height_input.get())
        wm.x_cord = str(wm_x_cord_input.get())
        wm.y_cord = str(wm_y_cord_input.get())
        wm.cust_title = str(wm_cust_title_input.get())
        wm.text = str(wm_text_ground.get('1.0', END))
        wm.font = str(wm_font_combobox.get())
        wm.fsize = str(wm_fsize_combobox.get())
        wm.text_x = str(wm_text_x_input.get())
        wm.text_y = str(wm_text_y_input.get())

    def wm_choose_color():
        """
        Функция выбора цвета надписи
        """
        wm_colorchooser = colorchooser.askcolor()
        wm.color = str(wm_colorchooser[1])
        wm_demo_ground.configure(bg=str(wm.color))

    def wm_open_custom_window():
        """
        Функция открытия окна
        с введёнными параметрами
        """
        wm_read_data()
        
        # Проверка правильности заполнения полей с папраметрами
        if (not wm.width.isdigit()) or (not wm.height.isdigit()) or (not wm.x_cord.isdigit()) or (
                not wm.y_cord.isdigit()) or (wm.cust_title == '') or (
                wm.text == '') or (wm.font == '') or (not wm.fsize.isdigit()) or (wm.color == '') or (
                not wm.text_x.isdigit()) or (
                not wm.text_y.isdigit()):
            messagebox.showerror('Ошибка!', 'Проверьте корректность введённых данных!')
        else:
            # Вывод окна на экран
            wm_custom_window = Toplevel()
            wm_custom_window.geometry(wm.width + 'x' + wm.height + '+' + wm.x_cord + '+' + wm.y_cord)
            wm_custom_window.title(wm.cust_title)

            wm_custom_label = Label(wm_custom_window, text=wm.text, font=(wm.font, wm.fsize), fg=wm.color)
            wm_custom_label.place(x=wm.text_x, y=wm.text_y)

    def wm_save():
        """
        Функция сохранения параметров
        окна в файл
        """
        def wm_save_changes():
            """
            Функция сохранения изменений в 
            открытом для редактирования файла
            """
            save(wm.open_path,
                 [wm.width, wm.height, wm.x_cord, wm.y_cord, wm.cust_title, wm.text, wm.font, wm.fsize, wm.color,
                  wm.text_x, wm.text_y])
            wm.flag = True
            wm_save_window.destroy()

        def wm_save_file():
            """
            Функция сохранения нового файла
            """
            save('C:/MihaSoft Files/WM Files/' + str(wm_save_input.get()),
                 [wm.width, wm.height, wm.x_cord, wm.y_cord, wm.cust_title, wm.text, wm.font, wm.fsize, wm.color,
                  wm.text_x, wm.text_y])
            wm_save_window.destroy()

        def wm_save_abort():
            """
            Отмена сохранения
            """
            wm_save_window.destroy()

        wm_read_data()

        # Проверка значения переменной, отвечающей за состояния
        # приложения (создание нового файла или редактирование существующего)
        # и вызов соответствующего окна.
        if not wm.flag:
            wm_save_window = Toplevel()
            center_window(wm_save_window, 300, 100)
            wm_save_window.resizable(False, False)
            wm_save_window.title('Сохранение')

            wm_save_label = Label(wm_save_window, text='Сохранить изменения?')
            wm_save_label.place(x=5, y=5)

            wm_save_ok_button = Button(wm_save_window, text='ОК', width=10, bg='#93e6a8', command=wm_save_changes)
            wm_save_ok_button.place(x=200, y=43)

            wm_close_button = Button(wm_save_window, text='Отмена', bg='#b8b8b8', width=10, command=wm_save_abort)
            wm_close_button.place(x=100, y=43)

        else:
            wm_save_window = Toplevel()
            center_window(wm_save_window, 300, 100)
            wm_save_window.resizable(False, False)
            wm_save_window.title('Сохранение')

            wm_save_label = Label(wm_save_window, text='Введите название файла...')
            wm_save_label.place(x=5, y=5)

            # Поле ввода названия нового файла
            wm_save_input = Entry(wm_save_window, width=25)
            wm_save_input.place(x=10, y=45)

            wm_save_ok_button = Button(wm_save_window, text='Сохранить', width=10, bg='#93e6a8', command=wm_save_file)
            wm_save_ok_button.place(x=200, y=53)

            wm_save_close_button = Button(wm_save_window, text='Отмена', bg='#b8b8b8', width=10, command=wm_save_abort)
            wm_save_close_button.place(x=200, y=13)

    def wm_edit():
        """
        Функция редактирования существующего файла
        (подстановка параметров из существующего файла
        в соответствующие поля
        """
        def wm_edit_ok():
            """
            Функция вывода параметров в соответствующие поля
            из выбранного файла
            """
            wm_edit_path = str(wm_edit_combobox.get())
            wm_data_list = load('C:/MihaSoft Files/WM Files/' + wm_edit_path)
            wm.open_path = 'C:/MihaSoft Files/WM Files/' + wm_edit_path

            wm_width_input.insert(0, wm_data_list[0])
            wm_height_input.insert(0, wm_data_list[1])
            wm_x_cord_input.insert(0, wm_data_list[2])
            wm_y_cord_input.insert(0, wm_data_list[3])
            wm_cust_title_input.insert(0, wm_data_list[4])
            wm_text_ground.insert(1.0, wm_data_list[5])
            wm_font_demo.configure(text=wm_data_list[6])
            wm_fsize_demo.configure(text=wm_data_list[7])
            wm_demo_ground.configure(bg=wm_data_list[8])
            wm_text_x_input.insert(0, wm_data_list[9])
            wm_text_y_input.insert(0, wm_data_list[10])
            wm.flag = False
            wm_edit_window.destroy()

        def wm_edit_abort():
            """
            Отмена редактирования
            """
            wm_edit_window.destroy()

        wm_edit_window = Toplevel()
        center_window(wm_edit_window, 300, 100)
        wm_edit_window.resizable(False, False)
        wm_edit_window.title('Открыть')

        wm_edit_label = Label(wm_edit_window, text='Выберите файл...')
        wm_edit_label.place(x=5, y=5)

        # Список существующих файлов
        wm_edit_combobox = ttk.Combobox(wm_edit_window, values=os.listdir('C:/MihaSoft Files/WM Files'),
                                        state='readonly')
        wm_edit_combobox.place(x=10, y=45)

        wm_edit_ok_button = Button(wm_edit_window, text='Редактировать', width=13, bg='#93e6a8', command=wm_edit_ok)
        wm_edit_ok_button.place(x=180, y=53)

        wm_edit_close_button = Button(wm_edit_window, text='Отмена', bg='#b8b8b8', width=13, command=wm_edit_abort)
        wm_edit_close_button.place(x=180, y=13)

    def wm_open():
        """
        Функция открытия окна по сохранённым
        ранее параметрам
        """
        def wm_open_ok():
            """
            Открытие выбранного файла
            """
            wm_op_path = str(wm_open_combobox.get())
            wm_open_data_list = load('C:/MihaSoft Files/WM Files/' + wm_op_path)

            wm.width = wm_open_data_list[0]
            wm.height = wm_open_data_list[1]
            wm.x_cord = wm_open_data_list[2]
            wm.y_cord = wm_open_data_list[3]
            wm.cust_title = wm_open_data_list[4]
            wm.text = wm_open_data_list[5]
            wm.font = wm_open_data_list[6]
            wm.fsize = wm_open_data_list[7]
            wm.color = wm_open_data_list[8]
            wm.text_x = wm_open_data_list[9]
            wm.text_y = wm_open_data_list[10]
            
            # Проверка корректности сохранённых параметров
            if (not wm.width.isdigit()) or (not wm.height.isdigit()) or (not wm.x_cord.isdigit()) or (
                    not wm.y_cord.isdigit()) or (wm.cust_title == '') or (
                    wm.text == '') or (wm.font == '') or (not wm.fsize.isdigit()) or (wm.color == '') or (
                    not wm.text_x.isdigit()) or (
                    not wm.text_y.isdigit()):
                messagebox.showerror('Ошибка!', 'Проверьте корректность введённых данных!')
            else:
                wm_open_cust_window = Toplevel()
                wm_open_cust_window.geometry(wm.width + 'x' + wm.height + '+' + wm.x_cord + '+' + wm.y_cord)
                wm_open_cust_window.title(wm.cust_title)
                wm_open_cust_label = Label(wm_open_cust_window, text=wm.text, font=(wm.font, wm.fsize), fg=wm.color)
                wm_open_cust_label.place(x=wm.text_x, y=wm.text_y)
            wm_open_window.destroy()

        def wm_open_abort():
            """
            Отмена открытия
            """
            wm_open_window.destroy()

        wm_open_window = Toplevel()
        center_window(wm_open_window, 300, 100)
        wm_open_window.resizable(False, False)
        wm_open_window.title('Открыть')

        wm_open_label = Label(wm_open_window, text='Выберите файл...')
        wm_open_label.place(x=5, y=5)

        # Список существующих файлов
        wm_open_combobox = ttk.Combobox(wm_open_window, values=os.listdir('C:/MihaSoft Files/WM Files'),
                                        state='readonly')
        wm_open_combobox.place(x=10, y=45)

        wm_open_ok_button = Button(wm_open_window, text='Открыть', width=10, bg='#93e6a8', command=wm_open_ok)
        wm_open_ok_button.place(x=200, y=53)

        wm_open_close_button = Button(wm_open_window, text='Отмена', bg='#b8b8b8', width=10, command=wm_open_abort)
        wm_open_close_button.place(x=200, y=13)

    def wm_clean():
        """
        Функция очистки полей 
        ввода параметров
        """
        wm_font_demo.configure(text='')
        wm_fsize_demo.configure(text='')

        wm_width_input.delete(0, 'end')
        wm_height_input.delete(0, 'end')
        wm_x_cord_input.delete(0, 'end')
        wm_y_cord_input.delete(0, 'end')
        wm_cust_title_input.delete(0, 'end')
        wm_text_x_input.delete(0, 'end')
        wm_text_y_input.delete(0, 'end')
        wm_text_ground.delete(1.0, END)
        wm_demo_ground.configure(bg='white')
        wm.flag = True

    def wm_delete():
        """
        Функция удаления ранее сохранённых файлов
        """
        def wm_delete_ok():
            """
            Удаление выбранного файла
            """
            wm_delete_path = str(wm_delete_combobox.get())
            os.remove('C:/MihaSoft Files/WM Files/' + wm_delete_path)
            wm_delete_window.destroy()

        def wm_delete_abort():
            """
            Отмена удаления
            """
            wm_delete_window.destroy()

        wm_delete_window = Toplevel()
        center_window(wm_delete_window, 300, 100)
        wm_delete_window.resizable(False, False)
        wm_delete_window.title('Удалить')

        wm_delete_label = Label(wm_delete_window, text='Выберите файл...')
        wm_delete_label.place(x=5, y=5)

        # Список существующих файлов
        wm_delete_combobox = ttk.Combobox(wm_delete_window, values=os.listdir('C:/MihaSoft Files/WM Files'),
                                          state='readonly')
        wm_delete_combobox.place(x=10, y=45)

        wm_delete_ok_button = Button(wm_delete_window, text='Удалить', width=10, bg='#e69b93', command=wm_delete_ok)
        wm_delete_ok_button.place(x=200, y=53)

        wm_delete_close_button = Button(wm_delete_window, text='Отмена', bg='#b8b8b8', width=10,
                                        command=wm_delete_abort)
        wm_delete_close_button.place(x=200, y=13)

    # Создание папки с файлами в случае отсутствия таковой
    if not os.path.exists('C:/MihaSoft Files/WM Files'):
        os.mkdir('C:/MihaSoft Files/WM Files')

    center_window(window, 600, 500)
    window.title('WindowManager 1.1')

    wm_title = Label(window, text='WindowManager 1.1', font=('Times New Roman', 20), fg='red')
    wm_title.place(x=50, y=5)

    wm_label_1 = Label(window, text='Размеры окна:', font=('Times New Roman', 12))
    wm_label_1.place(x=20, y=60)

    # Поле ввода ширины окна
    wm_width_input = Entry(window, width=12)
    wm_width_input.place(x=30, y=100)
    ToolTip(wm_width_input, 'Ширина')

    wm_label_2 = Label(window, text='X')
    wm_label_2.place(x=110, y=100)

    # Поле ввода высоты окна
    wm_height_input = Entry(window, width=12)
    wm_height_input.place(x=125, y=100)
    ToolTip(wm_height_input, 'Высота')

    wm_label_3 = Label(window, text='Расстояние от границ экрана:', font=('Times New Roman', 12))
    wm_label_3.place(x=20, y=130)

    wm_label_4 = Label(window, text='X =')
    wm_label_4.place(x=20, y=170)

    # Поле ввода расстояния от верхнего левого угла окна до левой границы экрана
    wm_x_cord_input = Entry(window, width=10)
    wm_x_cord_input.place(x=50, y=170)
    ToolTip(wm_x_cord_input, 'От левой границы')

    wm_label_5 = Label(window, text='Y =')
    wm_label_5.place(x=20, y=200)

    # Поле ввода расстояния от левого верхнего угла окна до верхней границы экрана
    wm_y_cord_input = Entry(window, width=10)
    wm_y_cord_input.place(x=50, y=200)
    ToolTip(wm_y_cord_input, 'От верхней границы')

    wm_label_6 = Label(window, text='Заголовок:', font=('Times New Roman', 12))
    wm_label_6.place(x=20, y=230)

    # Поле ввода заголовка окна
    wm_cust_title_input = Entry(window, width=28)
    wm_cust_title_input.place(x=30, y=260)

    wm_label_8 = Label(window, text='Введите текст:', font=('Times New Roman', 12))
    wm_label_8.place(x=300, y=80)

    # Поле ввода текста надписи, выводимой в окне
    wm_text_ground = Text(window, width=30, height=3)
    wm_text_ground.place(x=300, y=110)

    wm_label_9 = Label(window, text='Шрифт текста:', font=('Times New Roman', 12))
    wm_label_9.place(x=300, y=170)

    wm_font_combobox = ttk.Combobox(window, values=list(tkFont.families()), state='readonly')
    wm_font_combobox.place(x=300, y=200)

    wm_label_10 = Label(window, text='Размер шрифта:', font=('Times New Roman', 12))
    wm_label_10.place(x=300, y=230)
    
    # Поле ввода размера шрифта надписи
    wm_fsize_combobox = ttk.Combobox(window, values=[8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72])
    wm_fsize_combobox.place(x=300, y=260)

    wm_font_demo = Label(window)
    wm_font_demo.place(x=460, y=200)

    wm_fsize_demo = Label(window)
    wm_fsize_demo.place(x=460, y=260)

    wm_label_11 = Label(window, text='Цвет текста:', font=('Times New Roman', 12))
    wm_label_11.place(x=300, y=290)

    wm_choose_button = Button(window, text='Выбрать', bg='yellow', width=15, command=wm_choose_color)
    wm_choose_button.place(x=300, y=320)

    # Поле демонстрации выбранного цвета надписи
    wm_demo_ground = Label(window, text='', width=30, height=10)
    wm_demo_ground.place(x=30, y=320)

    wm_label_12 = Label(window, text='Расположение текста в окне:', font=('Times New Roman', 12))
    wm_label_12.place(x=300, y=350)

    wm_label_13 = Label(window, text='X =')
    wm_label_13.place(x=300, y=380)

    # Расстояние от надписи до левой границы окна
    wm_text_x_input = Entry(window, width=10)
    wm_text_x_input.place(x=330, y=380)
    ToolTip(wm_text_x_input, 'От левой границы')

    wm_label_14 = Label(window, text='Y =')
    wm_label_14.place(x=300, y=410)

    # Расстояние от надписи до верхней границы
    wm_text_y_input = Entry(window, width=10)
    wm_text_y_input.place(x=330, y=410)
    ToolTip(wm_text_y_input, 'От верхней границы')

    # Кнопка открытия окна по введённым параметрам
    wm_create_button = Button(window, text='СОЗДАТЬ', bg='green', fg='white', width=20, font=('Times New Roman', 16),
                              command=wm_open_custom_window)
    wm_create_button.place(x=300, y=440)
    ToolTip(wm_create_button, 'Создать окно по текущим параметрам...')

    wm_save_button = Button(window, text='Сохранить', bg='#f2ac6b', width=15, command=wm_save)
    wm_save_button.place(x=450, y=10)
    ToolTip(wm_save_button, 'Сохранить текущие параметры...')

    wm_open_button = Button(window, text='Открыть', bg='#f2dc6b', width=15, command=wm_open)
    wm_open_button.place(x=300, y=10)
    ToolTip(wm_open_button, 'Создать окно с сохранёнными параметрами...')

    wm_clean_button = Button(window, text='Обновить', bg='#93bbe6', width=15, command=wm_clean)
    wm_clean_button.place(x=450, y=45)
    ToolTip(wm_clean_button, 'Стереть текущие параметры...')

    wm_delete_button = Button(window, text='Удалить', bg='#e69b93', width=15, command=wm_delete)
    wm_delete_button.place(x=300, y=45)
    ToolTip(wm_delete_button, 'Удалить файл...')

    wm_edit_button = Button(window, text='Редактировать', bg='#90d4cb', width=15, command=wm_edit)
    wm_edit_button.place(x=150, y=45)
    ToolTip(wm_edit_button, 'Подставить параметры окна для редактирования...')

    wm_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=wm_to_home)
    wm_off.place(x=0, y=5)
    ToolTip(wm_off, 'На главную...')


def HolidayWarnings():
    """
    Приложение для включения-выключения
    функции вывода уведомлений о праздниках и памятных датах
    """
    def hw_to_home():
        """
        Возвращение на главную страницу MihaSoft
        """
        hw_title.destroy()
        hw_button.destroy()
        hw_off.destroy()
        home()
        center_window(window, 790, 870)

    def hw_start():
        """
        Функция включения показа уведомлений
        """
        hw_holiday_flag = open('C:/MihaSoft Files/FlagHW.miha', 'w')
        hw_holiday_flag.close()
        hw_button.configure(text='ОСТАНОВИТЬ ПРОГРАММУ', command=hw_stop, bg='#eb9898')
        ToolTip(hw_button, 'Запретить показ уведомлений о праздничных датах при запуске MihaSoft...')

    def hw_stop():
        """
        Функция отключения показа уведомлений
        """
        os.remove('C:/MihaSoft Files/FlagHW.miha')
        hw_button.configure(text='ЗАПУСТИТЬ ПРОГРАММУ', command=hw_start, bg='#98ebc0')
        ToolTip(hw_button, 'Разрешить показ уведомлений о праздничных датах при запуске MihaSoft...')

    window.geometry('400x200+50+50')
    center_window(window, 400, 200)
    window.title('HolidayWarnings 1.0')

    hw_title = Label(window, text='HolidayWarnings 1.0', font=('Times New Roman', 20), fg='red')
    hw_title.place(x=50, y=5)

    hw_button = Button(window, font=('Arial Bold', 15), width=25, height=2, bg='#98ebc0')
    hw_button.place(x=40, y=80)

    # Проверка наличия или отсутствия регулирующего файла
    # и соответствующее оформление управляющей кнопки.
    if not os.path.exists('C:/MihaSoft Files/FlagHW.miha'):
        hw_button.configure(text='ЗАПУСТИТЬ ПРОГРАММУ', command=hw_start, bg='#98ebc0')
        ToolTip(hw_button, 'Разрешить показ уведомлений о праздничных датах при запуске MihaSoft...')

    else:
        hw_button.configure(text='ОСТАНОВИТЬ ПРОГРАММУ', command=hw_stop, bg='#eb9898')
        ToolTip(hw_button, 'Запретить показ уведомлений о праздничных датах при запуске MihaSoft...')

    hw_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=hw_to_home)
    hw_off.place(x=0, y=5)
    ToolTip(hw_off, 'На главную...')


def YourWarnings():
    """
    Приложение для создания 
    фоновых уведомлений на конкретную дату
    """
    def yw_to_home():
        """
        Возвращение на главную страницу MihaSoft
        """
        yw_title.destroy()
        yw_label_1.destroy()
        yw_label_2.destroy()
        yw_label_3.destroy()
        yw_day_input.destroy()
        yw_month_input.destroy()
        yw_message_input.destroy()
        yw_create_button.destroy()
        yw_preview_button.destroy()
        yw_delete_button.destroy()
        yw_off.destroy()
        home()
        center_window(window, 790, 870)

    def yw_create():
        """
        Функция сохранения нового уведомления
        """
        # Проверка корректности введённых параметров
        if yw_month_input.get().isdigit() and yw_day_input.get().isdigit() and (
                (not yw_day_input.get().isdigit() or not yw_month_input.get().isdigit()) or 1 <= int(
                yw_day_input.get())) and int(yw_day_input.get()) <= 31 and int(
                yw_month_input.get()) >= 1:

            if int(yw_month_input.get()) <= 12:
                save('C:/MihaSoft Files/YW Files/' + str(yw_day_input.get()) + '.' + str(yw_month_input.get()),
                     [str(yw_day_input.get()), str(yw_month_input.get()), str(yw_message_input.get('1.0', END))])
                yw_day_input.delete(0, 'end')
                yw_month_input.delete(0, 'end')
                yw_message_input.delete(1.0, END)

            else:
                messagebox.showerror('Ошибка!', 'Введены некорректные данные!')
        else:
            messagebox.showerror('Ошибка!', 'Введены некорректные данные!')

    def yw_preview():
        """
        Функция предварительного просмотра сохранённого уведомдения
        """
        def yw_open_preview():
            """
            Открытие окна с уведомлением
            """
            yw_message = load('C:/MihaSoft Files/YW Files/' + str(yw_preview_combobox.get()))
            yw_preview_window = Toplevel()
            yw_preview_window.attributes('-topmost', 'true')
            center_window(yw_preview_window, 480, 400)
            yw_preview_window.title(yw_preview_combobox.get())

            yw_preview_message = Label(yw_preview_window, text=yw_message[2], font=('Times New Roman', 20), fg='red')
            yw_preview_message.place(x=5, y=255)

            yw_preview_logo = Label(yw_preview_window, text='Ⓜ', font=('Arial Bold', 150), fg='green')
            yw_preview_logo.place(x=120, y=5)

            yw_preview_ask_window.destroy()

        def yw_abort_preview():
            """
            Отмена предварительного просмотра
            """
            yw_preview_ask_window.destroy()

        yw_preview_ask_window = Toplevel()
        center_window(yw_preview_ask_window, 300, 100)
        yw_preview_ask_window.resizable(False, False)
        yw_preview_ask_window.title('Предварительный просмотр')

        yw_preview_label = Label(yw_preview_ask_window, text='Выберите запись...')
        yw_preview_label.place(x=5, y=5)

        # Список сохранённых уведомлений
        yw_preview_combobox = ttk.Combobox(yw_preview_ask_window, values=os.listdir('C:/MihaSoft Files/YW Files'),
                                           state='readonly')
        yw_preview_combobox.place(x=10, y=45)

        yw_preview_ok_button = Button(yw_preview_ask_window, text='Открыть', width=10, bg='#aae09f',
                                      command=yw_open_preview)
        yw_preview_ok_button.place(x=200, y=23)

        yw_preview_close_button = Button(yw_preview_ask_window, text='Отмена', width=10, bg='#b8b8b8',
                                         command=yw_abort_preview)
        yw_preview_close_button.place(x=200, y=60)

    def yw_delete():
        """
        Функция удаления сохранённого уведомления
        """
        def yw_delete_ok():
            """
            Удаление выбранного уведомления
            """
            os.remove('C:/MihaSoft Files/YW Files/' + str(yw_delete_combobox.get()))
            yw_delete_window.destroy()

        def yw_delete_abort():
            """
            Отмена удаления
            """
            yw_delete_window.destroy()

        yw_delete_window = Toplevel()
        center_window(yw_delete_window, 300, 100)
        yw_delete_window.resizable(False, False)
        yw_delete_window.title('Удаление')

        yw_delete_label = Label(yw_delete_window, text='Выберите запись...')
        yw_delete_label.place(x=5, y=5)

        # Список существующих уведомлений
        yw_delete_combobox = ttk.Combobox(yw_delete_window, values=os.listdir('C:/MihaSoft Files/YW Files'),
                                          state='readonly')
        yw_delete_combobox.place(x=10, y=45)

        yw_delete_ok_button = Button(yw_delete_window, text='Удалить', width=10, bg='#e69b93', command=yw_delete_ok)
        yw_delete_ok_button.place(x=200, y=23)

        yw_delete_close_button = Button(yw_delete_window, text='Отмена', width=10, bg='#b8b8b8',
                                        command=yw_delete_abort)
        yw_delete_close_button.place(x=200, y=60)

        # Создание папки с уведомлениями в случае отсутствия таковой
    if not os.path.exists('C:/MihaSoft Files/YW Files'):
        os.mkdir('C:/MihaSoft Files/YW Files')

    center_window(window, 400, 400)
    window.title('YourWarnings 1.0')

    yw_title = Label(window, text='YourWarnings 1.0', font=('Times New Roman', 20), fg='red')
    yw_title.place(x=50, y=5)

    yw_label_1 = Label(window, text='Введите дату:')
    yw_label_1.place(x=20, y=70)

    # Поле ввода даты вывода уведомления
    yw_day_input = Entry(window, width=20)
    yw_day_input.place(x=20, y=100)

    yw_label_2 = Label(window, text='Введите месяц:')
    yw_label_2.place(x=20, y=140)

    # Поле ввода месяца вывода уведомления
    yw_month_input = Entry(window, width=20)
    yw_month_input.place(x=20, y=170)

    yw_label_3 = Label(window, text='Введите текст сообщения:')
    yw_label_3.place(x=20, y=210)

    # Поле ввода текста уведомления
    yw_message_input = Text(window, width=30, height=5)
    yw_message_input.place(x=20, y=240)

    yw_create_button = Button(window, text='Добавить', bg='#aae09f', width=20, command=yw_create)
    yw_create_button.place(x=20, y=350)
    ToolTip(yw_create_button, 'Добавить новое уведомление...')

    yw_preview_button = Button(window, text='Просмотреть', bg='#e0d09f', width=15, command=yw_preview)
    yw_preview_button.place(x=200, y=70)
    ToolTip(yw_preview_button, 'Предварительный просмотр уведомления...')

    yw_delete_button = Button(window, text='Удалить', bg='#e09f9f', width=15, command=yw_delete)
    yw_delete_button.place(x=200, y=120)
    ToolTip(yw_delete_button, 'Удалить файл уведомления...')

    yw_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=yw_to_home)
    yw_off.place(x=0, y=5)
    ToolTip(yw_off, 'На главную...')


def Shmalyalka():
    """
    Авторский шутер
    """
    # Создание объекта с глобальными переменными
    sh = ShmalyalkaGlobals()

    def sh_to_home():
        """
        Возвращение на главную страницу MihaSoft
        """
        sh_title.destroy()
        sh_label_1.destroy()
        sh_label_2.destroy()
        pushka.destroy()
        snaryad.destroy()
        cel.destroy()
        sh_up_button.destroy()
        sh_down_button.destroy()
        sh_shoot_button.destroy()
        sh_parametrs_button.destroy()
        sh_stop_button.destroy()
        sh_number_of_shots_label.destroy()
        sh_number_of_hits_label.destroy()
        sh_off.destroy()
        home()
        center_window(window, 790, 870)

    def sh_to_shoot():
        """
        Функция произведения выстрела из пушки
        """
        # Озвучка выстрела в случае наличия соответствующей настройки
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 70)
         
        sh.x_snaryad = 100

        def odin():
            """
            Шаг итерации перемещения снаряда
            """
            snaryad.place(x=sh.x_snaryad)
            sh.x_snaryad += 5

        # Добавление нового выстрела к статистике
        sh.number_of_shots += 1
        sh_number_of_shots_label.configure(text=sh.number_of_shots)

        # Движение снаряда до уровня цели
        for i in range(100, 185):
            window.after(sh.speed_snar, odin())
            window.update()

        # Возвращение снаряда на исходное место
        sh.flag = True
        snaryad.place(x=100)
        
        # Перемещение цели на новую случайную позицию
        cel.place(x=530, y=randint(130, 530))

        # Проверка попадания снаряда в цель
        if 10 >= (snaryad.winfo_y() - cel.winfo_y()) >= -10:
            # Добавление нового попадания к статистике
            sh.number_of_hits += 1
            sh_number_of_hits_label.configure(text=sh.number_of_hits)
            # Озвучка попадания в случае наличия соответствующей настройки
            if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
                Beep(500, 500)

    def sh_up():
        """
        Функция движения пушки вверх
        """
        sh.flag = True

        def sh_up_one():
            """
            Шаг итерации движения пушки
            """
            # Проверка невыхода пушки за границы игрового поля
            if pushka.winfo_y() > 130:
                pushka.place(x=30, y=sh.y_pushka)
                snaryad.place(x=100, y=sh.y_pushka)
                sh.y_pushka -= 1

        # Движение пушки до границы игрового поля
        while pushka.winfo_y() != 130 and sh.flag:
            window.after(sh.speed_push, sh_up_one())
            window.update()

        # Движение пушки вниз после 
        # достижения границы игрового поля
        while sh.flag:
            sh_down()

    def sh_down():
        """
        Функция движения пушки вниз
        """
        sh.flag = True

        def sh_down_one():
            """
            Шаг итерации движения пушки
            """
            if pushka.winfo_y() < 530:
                pushka.place(x=30, y=sh.y_pushka)
                snaryad.place(x=100, y=sh.y_pushka)
                sh.y_pushka += 1

        # Движение пушки до границы игрового поля
        while pushka.winfo_y() != 530 and sh.flag:
            window.after(sh.speed_push, sh_down_one())
            window.update()

        # Движениепушки вверх после
        # после достижения границы игрового поля
        while sh.flag:
            sh_up()

    def sh_stop():
        """
        Остановка движения пушки
        и запрос о запуске новой игры
        """
        def sh_stop_ok():
            """
            Запуск новой игры
            """
            sh.flag = False
            sh.y_pushka = 130
            pushka.place(x=30, y=130)
            snaryad.place(x=100, y=130)
            cel.place(x=530, y=randint(130, 530))
            cel.configure(bg='black')
            sh_stop_window.destroy()
            sh.number_of_hits = 0
            sh_number_of_hits_label.configure(text='0')
            sh.number_of_shots = 0
            sh_number_of_shots_label.configure(text='0')

        def sh_abort_stop():
            """
            Отмена запуска новой игры
            """
            sh_stop_window.destroy()

        sh_stop_window = Toplevel()
        center_window(sh_stop_window, 250, 100)
        sh_stop_window.resizable(False, False)
        sh_stop_window.title('Заново')

        sh_stop_label = Label(sh_stop_window, text='Заново? Ваш процент попаданий:')
        sh_stop_label.place(x=5, y=5)

        # Вывод процентного соотнешения выстрелов и попаданий
        if sh.number_of_shots == 0:
            sh_percents = '0%'
        else:
            sh_percents = str(int((sh.number_of_hits / sh.number_of_shots) * 100)) + '%'

        sh_percents_label = Label(sh_stop_window, text=sh_percents)
        sh_percents_label.place(x=200, y=5)

        sh_stop_ok_button = Button(sh_stop_window, text='ДА', bg='#c0ebd6', width=10, command=sh_stop_ok)
        sh_stop_ok_button.place(x=10, y=40)

        sh_stop_abort_button = Button(sh_stop_window, text='НЕТ', bg='#ebc0d0', width=10, command=sh_abort_stop)
        sh_stop_abort_button.place(x=100, y=40)

    def sh_parametrs():
        """
        Функция изменения скорости 
        движения пушки и снаряда
        """
        def sh_save_changes():
            """
            Функция сохранения изменений параметров
            """
            # Проверка корректности введённых параметров
            if not sh_parametrs_input_1.get().isdigit() and not sh_parametrs_input_2.get().isdigit():
                messagebox.showinfo('Ошибка', 'Введите корректные значения!')
            else:
                if not sh_parametrs_input_1.get().isdigit():
                    sh.speed_snar = int(sh_parametrs_input_2.get())
                elif not sh_parametrs_input_2.get().isdigit():
                    sh.speed_push = int(sh_parametrs_input_1.get())
                else:
                    sh.speed_push = int(sh_parametrs_input_1.get())
                    sh.speed_snar = int(sh_parametrs_input_2.get())
                sh_parametrs_window.destroy()

        def sh_exit_parametrs():
            """
            Отмена изменения параметров
            """
            sh_parametrs_window.destroy()

        sh_parametrs_window = Toplevel()
        center_window(sh_parametrs_window, 250, 200)
        sh_parametrs_window.resizable(False, False)
        sh_parametrs_window.title('Параметры')

        sh_parametrs_label_1 = Label(sh_parametrs_window, text='Скорость пушки (мс/y):')
        sh_parametrs_label_1.place(x=5, y=5)

        # Поле ввода скорости движения пушки
        sh_parametrs_input_1 = Entry(sh_parametrs_window, width=20)
        sh_parametrs_input_1.place(x=10, y=50)

        sh_parametrs_label_2 = Label(sh_parametrs_window, text='Скорость снаряда (мс/x):')
        sh_parametrs_label_2.place(x=5, y=90)

        # Поле ввода скорости движения снаряда
        sh_parametrs_input_2 = Entry(sh_parametrs_window, width=20)
        sh_parametrs_input_2.place(x=10, y=135)

        sh_parametrs_ok_button = Button(sh_parametrs_window, text='ОК', bg='#c0ebd6', width=8, command=sh_save_changes)
        sh_parametrs_ok_button.place(x=160, y=10)

        sh_parametrs_abort_button = Button(sh_parametrs_window, text='Отмена', bg='#ebc0d0', width=8,
                                           command=sh_exit_parametrs)
        sh_parametrs_abort_button.place(x=160, y=50)
        ToolTip(sh_parametrs_window, 'Количество миллисекунд, проходящих между перемещением объекта на единицу x/y.')

    center_window(window, 600, 640)
    window.title('Shmalyalka 1.2')

    sh_title = Label(window, text='Shmalyalka 1.2', font=('Arial Bold', 16), fg='red')
    sh_title.place(x=40, y=20)

    sh_up_button = Button(window, text='⇧', font=('Arial Black', 20), bg='#90d69f', command=sh_up)
    sh_up_button.place(x=240, y=20)

    sh_down_button = Button(window, text='⇩', font=('Arial Black', 20), bg='#90d69f', command=sh_down)
    sh_down_button.place(x=310, y=20)

    pushka = Label(window, width=10, bg='#ff0000')
    pushka.place(x=30, y=130)

    snaryad = Label(window, width=2, bg='#11ff00')
    snaryad.place(x=100, y=130)

    cel = Label(window, width=2, bg='black')
    cel.place(x=530, y=randint(130, 530))

    sh_shoot_button = Button(window, text='ЗАЛП', bg='yellow', width=10, font=('Times New Roman', 16),
                             command=sh_to_shoot)
    sh_shoot_button.place(x=400, y=20)

    sh_label_1 = Label(window, text='Попаданий:')
    sh_label_1.place(x=30, y=70)

    sh_number_of_hits_label = Label(window, text='0')
    sh_number_of_hits_label.place(x=100, y=70)

    sh_label_2 = Label(window, text='Выстрелов:')
    sh_label_2.place(x=30, y=90)

    sh_number_of_shots_label = Label(window, text='0')
    sh_number_of_shots_label.place(x=100, y=90)

    sh_stop_button = Button(window, text='ЗАНОВО', bg='#d47f7f', width=10, font=('Times New Roman', 16),
                            command=sh_stop)
    sh_stop_button.place(x=400, y=70)

    sh_parametrs_button = Button(window, text='Параметры', bg='#9be0df', width=10, font=('Times New Roman', 12),
                                 command=sh_parametrs)
    sh_parametrs_button.place(x=450, y=570)

    sh_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=sh_to_home)
    sh_off.place(x=0, y=5)
    ToolTip(sh_off, 'На главную...')


def Paint():
    """
    Пиксельный графический редактор
    """
    # Создание объекта с глобальными переменными
    p = PaintGlobals()

    def p_to_home():
        """
        Возвращение на главную страницу MihaSoft
        """
        window3.destroy()
        window.state('normal')

    def recol(pix):
        """
        Общая функция изменеия цвета пикселя
        """
        pix.configure(bg=p.chosen_color)

    # Функции изменения цвета для каждого пикселя
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

    def p_choose_color():
        """
        Функция выбора цвета редактирования
        """
        p_colorchoose_window = colorchooser.askcolor()
        p.chosen_color = p_colorchoose_window[1]
        p_choose_button.configure(bg=str(p.chosen_color))
        p.choose_flag = True

    def eraser():
        """
        Функция включения-выключения режима ластика
        """
        # Включение ластика
        if p.choose_flag:
            p.now_color = p_choose_button['background']
            p.chosen_color = 'white'
            p_choose_button.configure(bg='white')
            p.choose_flag = False
            
        # Возвращение к последнему использовавшемуся цвету
        else:
            p.chosen_color = p.now_color
            p_choose_button.configure(bg=p.now_color)
            p.choose_flag = True

    def p_save():
        """
        Функция сохранения рисунка в файл
        """
        def p_save_file():
            """
            Сохранение нового файла
            """
            p_colors_list = []
            for i in range(len(a)):
                p_colors_list.append(a[i]['background'])
            save('C:/MihaSoft Files/P Files/' + str(p_save_input.get()), p_colors_list)
            p_save_window.destroy()

        def p_save_changes():
            """
            Функция сохранения изменений в существующем файле
            """
            p_colors_list = []
            for i in range(len(a)):
                p_colors_list.append(a[i]['background'])
            save(p.file_name, p_colors_list)
            p_save_window.destroy()

        def p_abort_save():
            """
            Отмена сохранения
            """
            p_save_window.destroy()

        # Проверка значения переменной, отвечающей за состояния
        # приложения (создание нового файла или редактирование существующего)
        # и вызов соответствующего окна.
        if p.save_flag:
            p_save_window = Toplevel()
            center_window(p_save_window, 300, 100)
            p_save_window.resizable(False, False)
            p_save_window.title('Сохранение')

            p_save_label = Label(p_save_window, text='Введите название файла...')
            p_save_label.place(x=5, y=5)

            p_save_input = Entry(p_save_window, width=25)
            p_save_input.place(x=10, y=45)

            p_save_ok_button = Button(p_save_window, text='Сохранить', width=10, bg='#93e6a8', command=p_save_file)
            p_save_ok_button.place(x=200, y=23)

            p_close_button = Button(p_save_window, text='Отмена', width=10, bg='#b8b8b8', command=p_abort_save)
            p_close_button.place(x=200, y=60)

        else:
            p_save_window = Toplevel()
            center_window(p_save_window, 300, 100)
            p_save_window.resizable(False, False)
            p_save_window.title('Сохранение изменений')

            p_save_label = Label(p_save_window, text='Сохранить изменения в файле\n' + p.file_name + '?')
            p_save_label.place(x=5, y=5)

            p_save_ok_button = Button(p_save_window, text='Сохранить', width=10, bg='#93e6a8', command=p_save_changes)
            p_save_ok_button.place(x=100, y=60)

            p_close_button = Button(p_save_window, text='Отмена', width=10, bg='#b8b8b8', command=p_abort_save)
            p_close_button.place(x=200, y=60)

    def p_open():
        """
        Функция открытия сохранённого рисунка
        """
        def p_open_ok():
            """
            Считывание данных и вывод рисунка на экран
            """
            p_open_colors_list = load('C:/MihaSoft Files/P Files/' + str(p_open_combobox.get()))
            p.file_name = 'C:/MihaSoft Files/P Files/' + str(p_open_combobox.get())
            for i in range(len(a)):
                a[i].configure(bg=p_open_colors_list[i])
            p_open_window.destroy()
            p.save_flag = False

        def p_abort_open():
            """
            Отмена открытия
            """
            p_open_window.destroy()

        p_open_window = Toplevel()
        center_window(p_open_window, 300, 100)
        p_open_window.resizable(False, False)
        p_open_window.title('Открыть')

        p_open_label = Label(p_open_window, text='Выберите файл...')
        p_open_label.place(x=5, y=5)

        # Список существующих файлов
        p_open_combobox = ttk.Combobox(p_open_window, values=os.listdir('C:/MihaSoft Files/P Files'), state='readonly')
        p_open_combobox.place(x=10, y=45)

        p_open_ok_button = Button(p_open_window, text='Открыть', width=10, bg='#93e6a8', command=p_open_ok)
        p_open_ok_button.place(x=200, y=23)

        p_open_abort_button = Button(p_open_window, text='Отмена', width=10, bg='#b8b8b8', command=p_abort_open)
        p_open_abort_button.place(x=200, y=60)

    def p_delete():
        """
        Функция удаления сохранённых файлов
        """
        def p_delete_ok():
            """
            Удаление выбранного файла
            """
            os.remove('C:/MihaSoft Files/P Files/' + str(p_delete_combobox.get()))
            p_delete_window.destroy()

        def p_delete_abort():
            """
            Отмена удаления
            """
            p_delete_window.destroy()

        p_delete_window = Toplevel()
        center_window(p_delete_window, 300, 100)
        p_delete_window.resizable(False, False)
        p_delete_window.title('Удаление')

        p_delete_label = Label(p_delete_window, text='Выберите файл...')
        p_delete_label.place(x=5, y=5)

        # Список существующих файлов
        p_delete_combobox = ttk.Combobox(p_delete_window, values=os.listdir('C:/MihaSoft Files/P Files'),
                                         state='readonly')
        p_delete_combobox.place(x=10, y=45)

        p_delete_ok_button = Button(p_delete_window, text='Удалить', width=10, bg='#e69b93', command=p_delete_ok)
        p_delete_ok_button.place(x=200, y=23)

        p_delete_close_button = Button(p_delete_window, text='Отмена', width=10, bg='#b8b8b8', command=p_delete_abort)
        p_delete_close_button.place(x=200, y=60)

    def p_clean():
        """
        Функция очистки поля для рисования
        """
        for i in range(len(a)):
            a[i].configure(bg='white')

    def p_new_pict():
        """
        Функция очистки поля для рисования
        и выхода из режима редактирования
        """
        p.save_flag = True
        p.file_name = None
        p_clean()

    # Массив для последующего добавления объектов всех
    # пикселей для последующих операций с ними
    a = []

    # Создание папки с файлами в случае отсутствия таковой
    if not os.path.exists('C:/MihaSoft Files/P Files'):
        os.mkdir('C:/MihaSoft Files/P Files')

    window3 = Toplevel()
    center_window(window3, 550, 300)
    window3.title('Paint 1.1')

    p_title = Label(window3, text='Paint 1.1', font=('Arial Bold', 16), fg='red')
    p_title.place(x=50, y=10)

    p_new_picture_button = Button(window3, text='Новый рисунок', bg='#b8b8b8', command=p_new_pict)
    p_new_picture_button.place(x=180, y=10)

    p_clean_button = Button(window3, text='Очистить', bg='#b8b8b8', command=p_clean)
    p_clean_button.place(x=285, y=10)

    p_eraser_button = Button(window3, text='Ластик', bg='#b8b8b8', command=eraser)
    p_eraser_button.place(x=355, y=10)
    ToolTip(p_eraser_button, 'Нажмите повторно для возвращения к последнему цвету...')

    p_choose_button = Button(window3, text='Выбрать цвет', bg='white', command=p_choose_color)
    p_choose_button.place(x=415, y=10)

    # Пиксели
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

    p_save_button = Button(window3, text='Сохранить', bg='#9be0b4', width=10, font=('Times New Roman', 16),
                           command=p_save)
    p_save_button.place(x=50, y=220)

    p_delete_button = Button(window3, text='Удалить', bg='#e69b93', width=10, font=('Times New Roman', 16),
                             command=p_delete)
    p_delete_button.place(x=210, y=220)

    p_open_button = Button(window3, text='Открыть', bg='#e0dc9b', width=10, font=('Times New Roman', 16),
                           command=p_open)
    p_open_button.place(x=370, y=220)

    p_off = Button(window3, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                   command=p_to_home)
    p_off.place(x=0, y=5)
    ToolTip(p_off, 'На главную...')


def Saper():
    s = SaperGlobals()

    def Return():
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
        home()
        center_window(window, 790, 870)

    def NewGame():
        s.box_list = [s_box_a1, s_box_a2, s_box_a3, s_box_a4, s_box_a5, s_box_b1, s_box_b2, s_box_b3, s_box_b4,
                      s_box_b5, s_box_c1, s_box_c2, s_box_c3, s_box_c4, s_box_c5, s_box_d1, s_box_d2, s_box_d3,
                      s_box_d4, s_box_d5, s_box_e1, s_box_e2, s_box_e3, s_box_e4, s_box_e5]
        s_flags_list = [False, False, False, False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False, False, False]
        s_numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        s.bomb_list = []
        for i in range(1, 6):
            s_bomb_loc = choice(s_numbers_list)
            s_numbers_list.remove(s_bomb_loc)
            s_flags_list[s_bomb_loc] = True
            s.bomb_list.append(s.box_list[s_bomb_loc])
        for i in range(len(s.bomb_list)):
            s.box_list.remove(s.bomb_list[i])
        s.global_flag = True
        s.flag_a1, s.flag_a2, s.flag_a3, s.flag_a4, s.flag_a5, s.flag_b1, s.flag_b2, s.flag_b3, s.flag_b4, s.flag_b5, \
            s.flag_c1, s.flag_c2, s.flag_c3, s.flag_c4, s.flag_c5, s.flag_d1, s.flag_d2, s.flag_d3, s.flag_d4, \
            s.flag_d5, s.flag_e1, s.flag_e2, s.flag_e3, s.flag_e4, s.flag_e5 = \
            s_flags_list[0], s_flags_list[1], s_flags_list[2], s_flags_list[3], s_flags_list[4], s_flags_list[5], \
            s_flags_list[6], s_flags_list[7], s_flags_list[8], s_flags_list[9], s_flags_list[10], s_flags_list[11], \
            s_flags_list[12], s_flags_list[13], s_flags_list[14], s_flags_list[15], s_flags_list[16], s_flags_list[17],\
            s_flags_list[18], s_flags_list[19], s_flags_list[20], s_flags_list[21], s_flags_list[22], s_flags_list[23],\
            s_flags_list[24]

    def GameOver():
        if s.global_flag:
            for i in range(len(s.bomb_list)):
                s.bomb_list[i].configure(bg='red')
            for i in range(len(s.box_list)):
                s.box_list[i].configure(bg='white')
            info_label.configure(text='Вы проиграли!', fg='red')
            s.global_flag = False
            stat_list = load('C:/MihaSoft Files/SaperStat.npy')
            numb_of_games = stat_list[0] + 1
            new_stat_list = [numb_of_games, stat_list[1]]
            save('C:/MihaSoft Files/SaperStat', new_stat_list)
            if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
                Beep(1000, 500)

    def CheckWin():
        k = 0
        for i in range(len(s.box_list)):
            if s.box_list[i]['background'] != 'white':
                k += 1
        if k == 0:
            for i in range(len(s.box_list)):
                s.box_list[i].configure(bg='white')
            for i in range(len(s.bomb_list)):
                s.bomb_list[i].configure(bg='green')
            s.global_flag = False
            info_label.configure(text='Вы выиграли!', fg='green')
            stat_list = load('C:/MihaSoft Files/SaperStat.npy')
            numb_of_games = stat_list[0] + 1
            numb_of_wins = stat_list[1] + 1
            new_stat_list = [numb_of_games, numb_of_wins]
            save('C:/MihaSoft Files/SaperStat', new_stat_list)
            if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
                Beep(500, 400)
                window.after(30, Beep(500, 400))
                window.after(30, Beep(500, 400))

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
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag:
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
        type_1(s_box_a1, s.flag_a1, s.flag_a2, s.flag_b2, s.flag_b1)

    def on_a5():
        type_1(s_box_a5, s.flag_a5, s.flag_a4, s.flag_b4, s.flag_b5)

    def on_e1():
        type_1(s_box_e1, s.flag_e1, s.flag_d1, s.flag_d2, s.flag_e2)

    def on_e5():
        type_1(s_box_e5, s.flag_e5, s.flag_e4, s.flag_d4, s.flag_d5)

    def type_2(box, this_flag, flag_1, flag_2, flag_3, flag_4, flag_5):
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag:
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
        type_2(s_box_a2, s.flag_a2, s.flag_a1, s.flag_b1, s.flag_b2, s.flag_b3, s.flag_a3)

    def on_a3():
        type_2(s_box_a3, s.flag_a3, s.flag_a2, s.flag_b2, s.flag_b3, s.flag_b4, s.flag_a4)

    def on_a4():
        type_2(s_box_a4, s.flag_a4, s.flag_a3, s.flag_b3, s.flag_b4, s.flag_b5, s.flag_a5)

    def on_b1():
        type_2(s_box_b1, s.flag_b1, s.flag_a1, s.flag_a2, s.flag_b2, s.flag_c2, s.flag_c1)

    def on_c1():
        type_2(s_box_c1, s.flag_c1, s.flag_b1, s.flag_b2, s.flag_c2, s.flag_d2, s.flag_d1)

    def on_d1():
        type_2(s_box_d1, s.flag_d1, s.flag_c1, s.flag_c2, s.flag_d2, s.flag_e2, s.flag_e1)

    def on_e2():
        type_2(s_box_e2, s.flag_e2, s.flag_e1, s.flag_d1, s.flag_d2, s.flag_d3, s.flag_e3)

    def on_e3():
        type_2(s_box_e3, s.flag_e3, s.flag_e2, s.flag_d2, s.flag_d3, s.flag_d4, s.flag_e4)

    def on_e4():
        type_2(s_box_e4, s.flag_e4, s.flag_e3, s.flag_d3, s.flag_d4, s.flag_d5, s.flag_e5)

    def on_b5():
        type_2(s_box_b5, s.flag_b5, s.flag_a5, s.flag_a4, s.flag_b4, s.flag_c4, s.flag_c5)

    def on_c5():
        type_2(s_box_c5, s.flag_c5, s.flag_b5, s.flag_b4, s.flag_c4, s.flag_d4, s.flag_d5)

    def on_d5():
        type_2(s_box_d5, s.flag_d5, s.flag_c5, s.flag_c4, s.flag_d4, s.flag_e4, s.flag_e5)

    def type_3(box, this_flag, flag_1, flag_2, flag_3, flag_4, flag_5, flag_6, flag_7, flag_8):

        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag:
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
        type_3(s_box_b2, s.flag_b2, s.flag_a1, s.flag_a2, s.flag_a3, s.flag_b3, s.flag_c3, s.flag_c2, s.flag_c1,
               s.flag_b1)

    def on_b3():
        type_3(s_box_b3, s.flag_b3, s.flag_a2, s.flag_a3, s.flag_a4, s.flag_b4, s.flag_c4, s.flag_c3, s.flag_c2,
               s.flag_b2)

    def on_b4():
        type_3(s_box_b4, s.flag_b4, s.flag_a3, s.flag_a4, s.flag_a5, s.flag_b5, s.flag_c5, s.flag_c4, s.flag_c3,
               s.flag_b3)

    def on_c2():
        type_3(s_box_c2, s.flag_c2, s.flag_b1, s.flag_b2, s.flag_b3, s.flag_c3, s.flag_d3, s.flag_d2, s.flag_d1,
               s.flag_c1)

    def on_c3():
        type_3(s_box_c3, s.flag_c3, s.flag_b2, s.flag_b3, s.flag_b4, s.flag_c4, s.flag_d4, s.flag_d3, s.flag_d2,
               s.flag_c2)

    def on_c4():
        type_3(s_box_c4, s.flag_c4, s.flag_b3, s.flag_b4, s.flag_b5, s.flag_c5, s.flag_d5, s.flag_d4, s.flag_d3,
               s.flag_c3)

    def on_d2():
        type_3(s_box_d2, s.flag_d2, s.flag_c1, s.flag_c2, s.flag_c3, s.flag_d3, s.flag_e3, s.flag_e2, s.flag_e1,
               s.flag_d1)

    def on_d3():
        type_3(s_box_d3, s.flag_d3, s.flag_c2, s.flag_c3, s.flag_c4, s.flag_d4, s.flag_e4, s.flag_e3, s.flag_e2,
               s.flag_d2)

    def on_d4():
        type_3(s_box_d4, s.flag_d4, s.flag_c3, s.flag_c4, s.flag_c5, s.flag_d5, s.flag_e5, s.flag_e4, s.flag_e3,
               s.flag_d3)

    def Statistics():
        def CleanStat():
            s_stats_start_list = [0, 0]
            save('C:/MihaSoft Files/SaperStat', s_stats_start_list)
            stat_window.destroy()

        def Close():
            stat_window.destroy()

        stat_window = Toplevel()
        center_window(stat_window, 200, 220)
        stat_window.resizable(False, False)
        stat_window.title('Статистика')

        first_label = Label(stat_window, text='Побед:')
        first_label.place(x=5, y=5)

        second_label = Label(stat_window, text='Всего игр:')
        second_label.place(x=5, y=50)

        third_label = Label(stat_window, text='Процент выигрышей:')
        third_label.place(x=5, y=95)

        s_stat_list = load('C:/MihaSoft Files/SaperStat.npy')

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
        save('C:/MihaSoft Files/SaperStat', s_stat_start_list)

    center_window(window, 430, 450)
    window.title('Saper 1.0')

    s_title = Label(window, text='Saper 1.0', font=('Arial Bold', 16), fg='red')
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

    restart_button = Button(window, text='Новая игра', width=10, bg='#93e6a8', font=('Arial Bold', 12),
                            command=RestartGame)
    restart_button.place(x=300, y=10)

    info_label = Label(window, font=('Arial Bold', 16))
    info_label.place(x=138, y=400)

    stat_button = Button(window, text='Статистика', width=10, bg='#d9c786', font=('Arial Bold', 12), command=Statistics)
    stat_button.place(x=180, y=10)
    NewGame()

    off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                 command=Return)
    off.place(x=0, y=5)
    ToolTip(off, 'На главную...')


def TurtlePaint():
    def paint_save():
        paint_window.setup(width=1.0, height=1.0)
        window.state('iconic')
        sleep(0.3)
        paint_image = capture_screen()
        sleep(0.3)
        window.state('normal')
        paint_window.setup(800, 600)
        paint_file = asksaveasfile(title='Сохранить файл', defaultextension='.png',
                                   filetypes=(('PNG file', '*.png'), ('All Files', '*.*')))
        if paint_file is not None:
            paint_image.save(paint_file.name)

    def paint_destroy():
        try:
            paint_window.bye()
        finally:
            paint_help_label.destroy()
            paint_off.destroy()
            paint_save_button.destroy()
            home()
            center_window(window, 790, 870)

    window.geometry('460x220+0+0')
    window.title('TurtlePaint')

    paint_help_text = '''
    Для начала рисования и переключения между режимами 
    рисования и перемещения пера нажмите правую кнопку мыши.
    Для передвижения пера или начертания линии в 
    зависимости от выбранного правой кнопкой режима 
    нажимайте левую кнопку мыши.
    Для выбора цвета нажимайте среднюю кнопку мыши (колёсико).
    Для закрашивания начертанной фигуры используйте 
    нажатие правой кнопки мыши при включённом режиме рисования.
    '''
    paint_help_label = Label(window, text=paint_help_text)
    paint_help_label.place(x=30, y=10)

    paint_save_button = Button(window, text='СОХРАНИТЬ РИСУНОК', bg='#93e6a8', font=('Arial Bold', 12),
                               command=paint_save)
    paint_save_button.place(x=220, y=170)

    paint_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                       command=paint_destroy)
    paint_off.place(x=0, y=5)
    ToolTip(paint_off, 'На главную...')

    TurtleScreen._RUNNING = True
    tp = TurtlePaintGlobal()

    def paint_switchupdown(xx=0.0, yy=0.0):
        if pen()['pendown']:
            end_fill()
            up()
        else:
            down()
            begin_fill()

    def paint_changecolor(xx=0.0, yy=0.0):
        tp.colors = tp.colors[1:] + tp.colors[:1]

    def paint_main():
        shape('circle')
        resizemode('user')
        shapesize(.5)
        width(3)
        tp.colors = ['red', 'green', 'blue', 'yellow', 'grey', 'black']
        color(tp.colors[0])
        paint_switchupdown()
        onscreenclick(goto, 1)
        onscreenclick(paint_changecolor, 2)
        onscreenclick(paint_switchupdown, 3)

    paint_window = Screen()
    paint_window.title('TurtlePaint')
    paint_window.setup(800, 600)

    paint_main()


def Clock():
    def timing():
        current_time = strftime('%H:%M:%S')
        clock.config(text=current_time)
        clock.after(200, timing)

    root = Toplevel()
    root.resizable(False, False)
    root.attributes('-topmost', 'true')
    root.title('Часы')
    clock = Label(root, font=('times', 60, 'bold'))
    clock.pack()
    timing()


def LoadingLine():
    lola = LoadingLineGlobals()

    lola.line_height = 1
    lola.logo_size = 1

    def LoadingLineCycle():
        line_1.configure(height=lola.line_height)
        line_2.configure(height=lola.line_height)
        lola.line_height += 1
        r1.configure(font=('Arial Bold', lola.logo_size))
        lola.logo_size += 13

    def Destroying():
        line_1.destroy()
        line_2.destroy()

    line_1 = Label(window, height=1, width=8, bg='red')
    line_1.place(x=20, y=20)
    line_2 = Label(window, height=1, width=8, bg='red')
    line_2.place(x=705, y=20)

    window.title('MihaSoft 11.1')
    center_window(window, 790, 870)

    r1 = Label(window, text='Ⓜ', font=('Arial Bold', 1), fg='red')
    r1.place(x=150, y=5)

    for i in range(1, 30):
        window.after(20, LoadingLineCycle())
        window.update()

    line_1.configure(bg='green')
    line_2.configure(bg='green')
    window.update()
    window.after(800, Destroying())
    r1.destroy()


def YourWarningsDo():
    if not os.path.exists('C:/MihaSoft Files/YW Files'):
        os.mkdir('C:/MihaSoft Files/YW Files')
    now = datetime.datetime.now()

    for i in range(len(os.listdir('C:/MihaSoft Files/YW Files'))):
        if os.listdir('C:/MihaSoft Files/YW Files')[i] == (str(now.day) + '.' + str(now.month) + '.npy'):
            yw_data = load('C:/MihaSoft Files/YW Files/' + os.listdir('C:/MihaSoft Files/YW Files')[i])

            yw_window = Toplevel()
            yw_window.attributes('-topmost', 'true')
            center_window(yw_window, 480, 400)
            yw_window.title(os.listdir('C:/MihaSoft Files/YW Files')[i])

            yw_message = Label(yw_window, text=yw_data[2], font=('Times New Roman', 20), fg='red')
            yw_message.place(x=5, y=255)

            yw_logo = Label(yw_window, text='Ⓜ', font=('Arial Bold', 150), fg='green')
            yw_logo.place(x=120, y=5)


def HolidayWarningsDo():
    now = datetime.datetime.now()

    def okno(text):
        hw_window = Toplevel()
        hw_window.attributes('-topmost', 'true')
        center_window(hw_window, 480, 400)
        hw_window.title(str(now))

        hw_do_label = Label(hw_window, text='ПОЗДРАВЛЯЕМ!!!', font=('Times New Roman', 20), fg='red')
        hw_do_label.place(x=115, y=255)

        hw_do_message = Label(hw_window, text=text, font=('Times New Roman', 20), fg='red')
        hw_do_message.place(x=35, y=295)

        hw_do_logo = Label(hw_window, text='Ⓜ', font=("Arial Bold", 150), fg='red')
        hw_do_logo.place(x=120, y=5)

    if os.path.exists('C:/MihaSoft Files/FlagHW.miha'):

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
            okno('Сегодня День\n Российской адвокатуры!')

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
            okno('Сегодня День\n Военно-воздушных сил!')

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

    def click_ti_but():
        if not os.path.exists('C:/MihaSoft Files/TintFlagFile.miha'):
            f = open('C:/MihaSoft Files/TintFlagFile.miha', 'w')
            f.close()
            third_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')
        else:
            os.remove('C:/MihaSoft Files/TintFlagFile.miha')
            third_button.configure(text='ВКЛЮЧИТЬ', bg='green')

    def set_exit():
        set_window.destroy()

    set_window = Toplevel()
    center_window(set_window, 400, 300)
    set_window.resizable(False, False)
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

    sound_button = Button(set_window, font=('Arial Bold', 11), width=13, fg='white', command=click_so_but)
    sound_button.place(x=220, y=90)

    if not os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
        sound_button.configure(text='ВКЛЮЧИТЬ', bg='green')
    else:
        sound_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')

    third_label = Label(set_window, text='Всплывающие подсказки\n к кнопкам:')
    third_label.place(x=10, y=165)

    third_button = Button(set_window, font=('Arial Bold', 11), width=13, fg='white', command=click_ti_but)
    third_button.place(x=220, y=170)

    if not os.path.exists('C:/MihaSoft Files/TintFlagFile.miha'):
        third_button.configure(text='ВКЛЮЧИТЬ', bg='green')
    else:
        third_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')

    exit_button = Button(set_window, text='OK', bg='#b8b8b8', font=('Arial Bold', 11), width=13, command=set_exit)
    exit_button.place(x=220, y=220)


def Music():
    Beep(300, 900)
    for i in range(1, 4):
        window.after(50, Beep(300, 100))


def AuthorList():
    def mess_exit():
        mess_window.destroy()

    mess_window = Toplevel()
    center_window(mess_window, 435, 280)
    mess_window.title('Сообщение от автора')
    mess_window.resizable(False, False)

    mess_ground = Text(mess_window, width=52, height=13)
    mess_ground.place(x=5, y=5)

    try:
        response = requests.get('https://mihasoft.glitch.me/api.txt')
        mess_ground.insert(1.0, response.text)
        mess_ground.configure(state='disabled')

    except ConnectionError:
        mess_ground.configure(fg='red')
        mess_ground.insert(1.0, 'НЕТ ДОСТУПА К СЕТИ!')

    exit_button = Button(mess_window, text='OK', bg='#b8b8b8', font=('Arial Bold', 11), width=13, command=mess_exit)
    exit_button.place(x=270, y=230)


def valute():
    def valute_exit():
        valute_window.destroy()

    valute_window = Toplevel()
    center_window(valute_window, 330, 280)
    valute_window.resizable(False, False)
    valute_window.title('Курсы валют')

    try:
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        valute_json = response.json()

        date_string = ''
        for i in range(0, 10):
            date_string += valute_json['Date'][i]
        date_string += ' '
        for i in range(11, 16):
            date_string += valute_json['Date'][i]
        valute_window.title('Курсы валют - ' + date_string)

        val_label_1 = Label(valute_window, text='Доллар США:', font=('Times New Roman', 14))
        val_label_1.place(x=10, y=10)

        val_label_1_2 = Label(valute_window, text=valute_json['Valute']['USD']['Value'], font=('Times New Roman', 14))
        val_label_1_2.place(x=180, y=10)

        val_label_2 = Label(valute_window, text='Евро:', font=('Times New Roman', 14))
        val_label_2.place(x=10, y=50)

        val_label_2_2 = Label(valute_window, text=valute_json['Valute']['EUR']['Value'], font=('Times New Roman', 14))
        val_label_2_2.place(x=180, y=50)

        val_label_3 = Label(valute_window, text='Фунт стерлингов:', font=('Times New Roman', 14))
        val_label_3.place(x=10, y=90)

        val_label_3_2 = Label(valute_window, text=valute_json['Valute']['GBP']['Value'], font=('Times New Roman', 14))
        val_label_3_2.place(x=180, y=90)

        val_label_3 = Label(valute_window, text='Белорусский рубль:', font=('Times New Roman', 14))
        val_label_3.place(x=10, y=130)

        val_label_3_2 = Label(valute_window, text=valute_json['Valute']['BYN']['Value'], font=('Times New Roman', 14))
        val_label_3_2.place(x=180, y=130)

    except ConnectionError:
        err_label = Label(valute_window, text='НЕТ ДОСТУПА К СЕТИ!', font=('Times New Roman', 14), fg='red')
        err_label.place(x=10, y=10)

    valute_exit_button = Button(valute_window, text='ОК', width=16, font=('Times New Roman', 14), bg='#b8b8b8',
                                command=valute_exit)
    valute_exit_button.place(x=140, y=180)


def CleanTemp():
    def ct_clean():
        delete_size = 0
        number_of_del_files = 0
        no_del_files = ''
        user_name = os.environ.get('USERNAME')
        ct_report_ground.configure(state=NORMAL)
        ct_report_ground.insert('1.0', 'Идёт процесс удаления...\n\n')
        for i in os.listdir('C:/Users/' + user_name + '/AppData/Local/Temp'):
            try:
                d_size = os.path.getsize('C:/Users/' + user_name + '/AppData/Local/Temp/' + i)
                if os.path.isdir('C:/Users/' + user_name + '/AppData/Local/Temp/' + i):
                    rmtree('C:/Users/' + user_name + '/AppData/Local/Temp/' + i)
                else:
                    os.remove('C:/Users/' + user_name + '/AppData/Local/Temp/' + i)
                number_of_del_files += 1
                delete_size += d_size
            except PermissionError:
                no_del_files += (i + '\n')

        delete_size = round(delete_size / (1024 * 1024), 5)

        ct_report_ground.insert('2.0', 'Всего удалено ' + str(number_of_del_files) + ' объектов размером\n')
        ct_report_ground.insert('3.0', str(delete_size) + ' мегабайт\n')
        ct_report_ground.insert('4.0', 'Не удалось удалить следующие файлы:\n' + no_del_files)
        ct_report_ground.configure(state=DISABLED)

    def ct_ok():
        ct_window.destroy()

    ct_window = Toplevel()
    center_window(ct_window, 415, 460)
    ct_window.resizable(False, False)
    ct_window.title('Очистить папку Temp')

    ct_clean_button = Button(ct_window, text='Очистить', bg='green', fg='white', width=20, font=('Times New Roman', 16),
                             command=ct_clean)
    ct_clean_button.place(x=80, y=10)

    ct_report_ground = Text(ct_window, width=50, height=20, state=DISABLED)
    ct_report_ground.place(x=5, y=60)

    ct_ok_button = Button(ct_window, text='ОK', bg='#b8b8b8', width=20, font=('Times New Roman', 16), command=ct_ok)
    ct_ok_button.place(x=80, y=400)


def blackout(button):
    bg = button['background']
    fg = button['foreground']

    def on_enter(e):
        button['background'] = '#6e6e6e'
        button['foreground'] = 'white'

    def on_leave(e):
        button['background'] = bg
        button['foreground'] = fg

    button.bind('<Enter>', on_enter)
    button.bind('<Leave>', on_leave)


def home():
    def home_to_yao():
        home_destroying()
        YourAgeOnline()

    def home_to_mso():
        home_destroying()
        MiddleScoreOnline()

    def home_to_sml():
        home_destroying()
        SML()

    def home_to_tns():
        home_destroying()
        TrunsNumSystem()

    def home_to_cz():
        home_destroying()
        CrossZero()

    def home_to_mn():
        home_destroying()
        MihNote()

    def home_to_wm():
        home_destroying()
        WindowManager()

    def home_to_hw():
        home_destroying()
        HolidayWarnings()

    def home_to_yw():
        home_destroying()
        YourWarnings()

    def home_to_sh():
        home_destroying()
        Shmalyalka()

    def home_to_p():
        window.wm_state('iconic')
        Paint()

    def home_to_s():
        home_destroying()
        Saper()

    def home_to_tp():
        home_destroying()
        TurtlePaint()

    def home_destroying():
        MIHA_SOFT_LOGOTYPE.destroy()
        ms_ground.destroy()
        ms_yao_button.destroy()
        ms_mso_button.destroy()
        ms_sml_button.destroy()
        ms_tns_button.destroy()
        ms_cz_button.destroy()
        ms_mn_button.destroy()
        ms_wm_button.destroy()
        ms_hw_button.destroy()
        ms_yw_button.destroy()
        ms_sh_button.destroy()
        ms_p_button.destroy()
        ms_s_button.destroy()
        ms_tp_button.destroy()

    def main_exit():
        window.quit()

    def popup(event):
        p = PoupGlobals()
        p.x = event.x
        p.y = event.y
        r_menu.post(event.x_root, event.y_root)

    window.title('MihaSoft 11.1')
    center_window(window, 790, 870)

    menu = Menu(window)
    window.config(menu=menu)
    menu.add_command(label='Настройки', command=Settings)
    menu_2 = Menu(menu, tearoff=0)
    menu_2.add_command(label='Часы', command=Clock)
    menu_2.add_command(label='Сообщение от автора', command=AuthorList)
    menu_2.add_command(label='Курсы валют', command=valute)
    menu_2.add_command(label='Очистить папку Temp', command=CleanTemp)
    menu.add_cascade(label='Дополнительно', menu=menu_2)

    r_menu = Menu(tearoff=0)
    r_menu.add_command(label='Выход', command=main_exit)
    window.bind('<Button-3>', popup)

    MIHA_SOFT_LOGOTYPE = Label(window, text='Ⓜ', font=('Arial Bold', 365), fg='red')
    MIHA_SOFT_LOGOTYPE.place(x=150, y=5)

    ms_ground = Label(window, width=90, height=21, bg='#e0b6b6')
    ms_ground.place(x=70, y=520)

    ms_yao_button = Button(window, text='YourAgeOnline', font=('Arial Bold', 13), width=25, height=2, bg='#0039A6',
                           fg='white',
                           command=home_to_yao)
    ms_yao_button.place(x=90, y=720)
    blackout(ms_yao_button)

    ms_mso_button = Button(window, text='MiddleScoreOnline', font=('Arial Bold', 13), width=25, height=2, bg='#FF0000',
                           fg='white', command=home_to_mso)
    ms_mso_button.place(x=450, y=720)
    blackout(ms_mso_button)

    ms_sml_button = Button(window, text='The SML - IDE & Compiler', font=('Arial Bold', 13), width=25, height=2,
                           bg='#D52B1E',
                           fg='white', command=home_to_sml)
    ms_sml_button.place(x=90, y=780)
    blackout(ms_sml_button)

    ms_tns_button = Button(window, text='TrunsNumSystem', font=('Arial Bold', 13), width=25, height=2, bg='#FFDF00',
                           command=home_to_tns)
    ms_tns_button.place(x=450, y=780)
    blackout(ms_tns_button)

    ms_cz_button = Button(window, text='CrossZero', font=('Arial Bold', 13), width=25, height=2, bg='#FFFFFF',
                          command=home_to_cz)
    ms_cz_button.place(x=90, y=660)
    blackout(ms_cz_button)

    ms_mn_button = Button(window, text='MihNote', font=('Arial Bold', 13), width=25, height=2, bg='#FFFFFF',
                          command=home_to_mn)
    ms_mn_button.place(x=450, y=660)
    blackout(ms_mn_button)

    ms_wm_button = Button(window, text='WindowManager', font=('Arial Bold', 13), width=25, height=2, bg='#93e6a1',
                          command=home_to_wm)
    ms_wm_button.place(x=90, y=600)
    blackout(ms_wm_button)

    ms_hw_button = Button(window, text='HolidayWarnings', font=('Arial Bold', 13), width=25, height=2, bg='#93e6a1',
                          command=home_to_hw)
    ms_hw_button.place(x=450, y=600)
    blackout(ms_hw_button)

    ms_yw_button = Button(window, text='YourWarnings', font=('Arial Bold', 13), width=25, height=2, bg='#9ae3de',
                          command=home_to_yw)
    ms_yw_button.place(x=90, y=540)
    blackout(ms_yw_button)

    ms_sh_button = Button(window, text='Shmalyalka', font=('Arial Bold', 13), width=25, height=2, bg='#9ae3de',
                          command=home_to_sh)
    ms_sh_button.place(x=450, y=540)
    blackout(ms_sh_button)

    ms_p_button = Button(window, text='Paint', font=('Arial Bold', 13), width=10, height=2, bg='#a9e866',
                         command=home_to_p)
    ms_p_button.place(x=337, y=660)
    blackout(ms_p_button)

    ms_s_button = Button(window, text='Saper', font=('Arial Bold', 13), width=10, height=2, bg='#d67ab4',
                         command=home_to_s)
    ms_s_button.place(x=337, y=600)
    blackout(ms_s_button)

    ms_tp_button = Button(window, text='TurtlePaint', font=('Arial Bold', 13), width=10, height=2, bg='#9ae3de',
                          command=home_to_tp)
    ms_tp_button.place(x=337, y=720)
    blackout(ms_tp_button)


def Start():
    text_1 = '''
    Вас приветствуют разработчики MihaSoft! Для корректного продолжения работы
    программы необходимо разрешение на создание системных папок на диске C:
    '''

    text_2 = '''
    На диске C: будет создана папка MihaSoft Files, в которой будут 
    размещаться новые папки и файлы, создаваемые в процессе работы программы
    '''

    def sss_exit():
        window.quit()

    def sss_welcome():
        os.mkdir('C:/MihaSoft Files')
        well_label.destroy()
        well_button.destroy()
        bye_button.destroy()
        home()

    if not os.path.exists('C:/MihaSoft Files'):
        center_window(window, 500, 100)
        window.title('Добро пожаловать!')

        well_label = Label(window, text=text_1)
        well_label.place(x=5, y=5)

        well_button = Button(window, text='РАЗРЕШИТЬ', font=('Times New Roman', 10), width=13, command=sss_welcome)
        well_button.place(x=230, y=60)
        ToolTip(well_button, text_2)

        bye_button = Button(window, text='ОТМЕНА', font=('Times New Roman', 10), width=13, command=sss_exit)
        bye_button.place(x=350, y=60)

    else:
        if os.path.exists('C:/MihaSoft Files/AnimationFlagFile.miha'):
            LoadingLine()
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Music()

        home()
        HolidayWarningsDo()
        YourWarningsDo()


if __name__ == '__main__':
    window = Tk()
    Start()
    window.mainloop()
