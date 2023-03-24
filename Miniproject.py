from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมบันทึกประวัติการใช้ยา')
GUI.geometry('700x500')

L1 = Label(GUI,text='โปรแกรมบันทึกประวัติการใช้ยาของผู้ป่วย',font=('TH Sarabun New',30,'bold'),fg='green')
L1.place(x=50,y=40)
#########################
def Button1():
    text = 'นายเอ อายุ 46 ปี เป็นโรคเบาหวาน เคยพบแพทย์มากกว่า 3 ครั้ง และมีประวัติในการใช้ยาคือ ยาป้องกันโรคเบาหวาน'
    messagebox.showinfo('คนที่ 1',text)

FB1 = Frame(GUI)
FB1.place(x=30,y=100)
B1 = ttk.Button(FB1,text='คนที่ 1',command=Button1)
B1.pack(ipadx=40,ipady=40)
#########################
def Button2():
    text = 'นายบี อายุ 38 ปี เป็นโรคหัวใจ เคยพบแพทย์มากกว่า 4 ครั้ง และมีประวัติในการใช้ยาคือ ยาลิ่มเลือด'
    messagebox.showinfo('คนที่ 2',text)

FB2 = Frame(GUI)
FB2.place(x=40,y=100)
B2 = ttk.Button(FB1,text='คนที่ 2',command=Button2)
B2.pack(ipadx=40,ipady=40)
#########################
def Button3():
    text = 'นายซี อายุุ 53 ปี เป็นโรคไต เคยพบแพทย์มากกว่า 7 ครั้ง และมีประวัติการใช้ยาคือ ยาล้างไต'
    messagebox.showinfo('คนที่ 3',text)

FB3 = Frame(GUI)
FB3.place(x=50,y=100)
B3 = ttk.Button(FB1,text='คนที่ 3',command=Button3)
B3.pack(ipadx=40,ipady=40)

GUI.mainloop()
