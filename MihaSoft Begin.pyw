def fallout1():
    from tkinter.ttk import Radiobutton
    from tkinter import messagebox
    l=2
    
    def returni2():
        rasherec3()
        home()
        
    def rasherec3():
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
        a=int(txt1.get())
        b=int(txt2.get())
        c=int(txt3.get())
        d=int(txt4.get())
        e=int(txt5.get())
        f=int(txt6.get())
        if ((a>=1) and (a<=31)) and ((b>=1) and (b<=12)) and (c>0) and ((d>=1) and (d<=31)) and ((e>=1) and (e<=12)) and (f>0) and (f>=c):
            z=e-1
            g=f-c-1
            h=12-b
            if b!=2:
                if b%2==0:
                    k=30-a
                    m=k+d
                    if m>=30:
                        h+=1
                        m=m-30
                else:
                    k=31-a
                    m=k+d
                    if m>=31:
                        h+=1
                        m=m-31
            else:
                if c%4==0:
                    k=29-a
                    m=k+d
                    if m>=19:
                        h+=1
                        m=m-29
                    else:
                        k=28-a
                        m=k+d
                    if m>=28:
                        h+=1
                        m=m-28
            x=h+z
            if x>=12:
                g+=1 
                x=x-12
            if z%2==0:
                m+=1
            l = var.get()
            if l==1:
                if g==0:
                    lbl8.configure(text=(g, 'год', x, 'месяцев', m-1, 'дней.'))
                elif g==1:
                    lbl8.configure(text=(g, 'год', x, 'месяцев', m-1, 'дней.' ))
                elif (g==2) or (g==3) or (g==4):
                    lbl8.configure(text=(g, 'года', x, 'месяцев', m-1, 'дней.' ))
                else:
                    lbl8.configure(text=(g, 'лет', x, 'месяцев', m, 'дней.' ))
            if l==2:
                lbl8.configure(text=(((365.29*g)+(x*30.25)+m)//1, 'дней.'))
        else:
            messagebox.showerror('Ошибка!', 'Проверьте правильность ввода!')

    window.title("YourAgeOnline 2.0")  
    window.geometry('650x650+600+200')  

    lbl1 = Label(window, text="YourAgeOnline 2.0", font=("Arial Bold", 16), fg = "red")  
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
        flag=1
        j=0
        bx=eba.get()
        b=list(map(int, str(bx)))
        for i in range (len(b)):
            if (b[i]!=2) and (b[i]!=3) and (b[i]!=4) and (b[i]!=5):
               b[i]=0
        while 0 in b:
            b.remove(0)
        print(b)
        cx=huya.get()
        c=list(map(int, str(cx)))
        if c==[0]:
            flag=0
        for i in range (len(c)):
            if (c[i]!=2) and (c[i]!=3) and (c[i]!=4) and (c[i]!=5) and (c[i]!=0):
                c[i]=0
        while 0 in c:
            c.remove(0)
        if flag==0:
            q=sum(b)/len(b)
            lbl4.configure(text=q)
            if (q>=3.6) and (q<=4.6):
                lbl5.configure(text=('Можете расслабиться!!!'))
                while sum(b)/len(b)<4.6:
                    b.append(5)
                    j+=1
                if j==1:
                    lbl6x.configure(text=('У вас выходит четвёрка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличную оценку до пятёрки в триместре.')
                if (j==2) or (j==3) or (j==4):
                    lbl6x.configure(text=('У вас выходит четвёрка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличные оценки до пятёрки в триместре.')
                if j>=5:
                    lbl6x.configure(text=('У вас выходит четвёрка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличных оценок до пятёрки в триместре.')
            if (q>=2.6) and (q<3.6):
                lbl5.configure(text=('Внимание!!!'))
                while sum(b)/len(b)<3.6:
                    b.append(5)
                    j+=1
                if j==1:
                    lbl6x.configure(text=('У вас выходит тройка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличную оценку до четвёрки в триместре.')
                if (j==2) or (j==3) or (j==4):
                    lbl6x.configure(text=('У вас выходит тройка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличные оценки до четвёрки в триместре.')
                if j>=5:
                    lbl6x.configure(text=('У вас выходит тройка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличных оценок до четвёрки в триместре.')
            if (q>=2) and (q<2.6):
                lbl5.configure(text=('Вам пи**ец!!!!'))
                while sum(b)/len(b)<2.6:
                    b.append(5)
                    j+=1
                if j==1:
                    lbl6x.configure(text=('У вас выходит ДВОЙКА. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличную оценку до тройки в триместре.')
                if (j==2) or (j==3) or (j==4):
                    lbl6x.configure(text=('У вас выходит ДВОЙКА. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличные оценки до тройки в триместре.')
                if j>=5:
                    lbl6x.configure(text=('У вас выходит ДВОЙКА. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличных оценок до тройки в триместре.')   
            if (q>=4.6) and (q<=5):
                lbl5.configure(text=('У вас выходит пятёрка! Не получайте плохих оценок.'))
        if flag!=0:
            z=(sum(c)*2+sum(b))/(len(b)+len(c)*2)
            lbl4.configure(text=z)
            if (z>=3.6) and (z<=4.6):
                lbl5.configure(text=('Можете расслабиться!!!'))
                while (sum(c)*2+sum(b))/(len(b)+len(c)*2)<4.6:
                    b.append(5)
                    j+=1
                if j==1:
                    lbl6x.configure(text=('У вас выходит четвёрка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличную оценку до пятёрки в триместре.')
                if (j==2) or (j==3) or (j==4):
                    lbl6x.configure(text=('У вас выходит четвёрка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличные оценки до пятёрки в триместре.')
                if j>=5:
                    lbl6x.configure(text=('У вас выходит четвёрка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличных оценок до пятёрки в триместре.')
            if (z>=2.6) and (z<3.6):
                lbl5.configure(text=('Внимание!!!'))
                while (sum(c)*2+sum(b))/(len(b)+len(c)*2)<3.6:
                    b.append(5)
                j+=1
                if j==1:
                    lbl6x.configure(text=('У вас выходит тройка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличную оценку до четвёрки в триместре.')
                if (j==2) or (j==3) or (j==4):
                    lbl6x.configure(text=('У вас выходит тройка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличные оценки до четвёрки в триместре.')
                if j>=5:
                    lbl6x.configure(text=('У вас выходит тройка. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличных оценок до четвёрки в триместре.')
            if (z>=2) and (z<2.6):
                lbl5.configure(text=('Вам пи**ец!!!!'))
                while (sum(c)*2+sum(b))/(len(b)+len(c)*2)<2.6:
                    b.append(5)
                    j+=1
                if j==1:
                    lbl6x.configure(text=('У вас выходит ДВОЙКА. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличную оценку до тройки в триместре.')
                if (j==2) or (j==3) or (j==4):
                    lbl6x.configure(text=('У вас выходит ДВОЙКА. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличные оценки до тройки в триместре.')
                if j>=5:
                    lbl6x.configure(text=('У вас выходит ДВОЙКА. Вам нужно получить ещё'))
                    lbl6y.configure(text=j)
                    lbl6z.configure(text='отличных оценок до тройки в триместре.')        
            if (z>=4.6) and (z<=5):
                lbl5.configure(text=('У вас выходит пятёрка! Не получайте плохих оценок!'))
            
    window.title("MiddleScoreOnline 5.0")  
    window.geometry('790x325+600+300')

    lbl1 = Label(window, text="MiddleScoreOnline 5.0", font=("Arial Bold", 16), fg = "red")  
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


def home():
    def germes1():
        rasherec1()
        fallout1()
        
    def germes2():
        rasherec1()
        fallout2()
            
    def rasherec1():
        r1.destroy()
        r2.destroy()
        r3.destroy()
        
    window.title("MihaSoft Begin")  
    window.geometry('790x790+580+140')
    r1=Label(window, text="Ⓜ", font=("Arial Bold", 350), fg = "red")
    r1.place(x=150, y=80)
    r2 = Button(window, text="YourAgeOnline 2.0", font=("Arial Bold", 15), width=23, height=2, bg="blue", fg="white", command=germes1)
    r2.place(x=90, y=640)
    r3 = Button(window, text="MiddleScoreOnline 5.0", font=("Arial Bold", 15), width=23, height=2, bg="orange", fg="white", command=germes2)
    r3.place(x=400, y=640)


from tkinter import * 
window = Tk()
home()
window.mainloop()