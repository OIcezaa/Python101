from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อโปรแกรม
GUI.geometry('500x400') #นี่คือขนาดโปรแกรม

L1 = Label(GUI,text='โปรแกรมบันทึกจำนวนครู บุคลากร และนักเรียน',font=('TH Sarabun New',30),fg='black')
L1.place(x=30,y=20)
#######################
def Button1():
    text = '14 คน'
    messagebox.showinfo('คุณครูที่สอนห้อง 2/9',text)
    
FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=200)
B1 = ttk.Button(FB1,text='คุณครูที่สอนในห้องมีกี่คน',command=Button1)
B1.pack(ipadx=20,ipady=20)
#######################
def Button2():
    text = '40 คน'
    messagebox.showinfo('เพื่อนในห้องเรียน 2/9',text)
    
FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=200,y=200)
B2 = ttk.Button(FB1,text='มีเพื่อนอยู่เท่าไร',command=Button2)
B2.pack(ipadx=20,ipady=20)

#######################
def Button3():
    text = '3,500 คน'
    messagebox.showinfo('เพื่อนทั้งโรงเรียน',text)
    
FB3 = Frame(GUI) #คล้ายกระดาน
FB3.place(x=300,y=200)
B3 = ttk.Button(FB1,text='มีเพื่อนทั้งโรงเรียนอยู่เท่าไร',command=Button3)
B3.pack(ipadx=20,ipady=20)

GUI.mainloop()
