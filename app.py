from tkinter import *
import math
from turtle import bgcolor
import numpy as np
import re

regex = r'^[-+]?[0-9]+[\.]?[0-9]*([0-9]+)?$'

def clear():
    t1.delete('0','end')
    t2.delete('0','end')
    t3.delete('0','end')
    lblo['text']=''
    lb = [lb13,lb14,lb15,lb16,lb17,lb18,lb19,lb20,lb21,lb22,lb23,lb24]
    for i in lb:
        i['text']=''

def calc(x):
    carat=float(t1.get())
    ratio=float(t2.get())
    depth_per=float(t3.get())
    global arr,arr1,result
    arr = np.linspace(58,69,num=12)
    if x == 'EM':
        arr1 = np.linspace(0,0,num=12)
        result=round(math.pow((carat * math.pow(ratio,2) * 100)/(depth_per * 0.0102),(1/3)),2)
        for i in range(0,len(arr)):
            y =round(math.pow((carat * math.pow(ratio,2) * 100)/(arr[i] * 0.0102),(1/3)),2)
            arr1[i] = y
        
    elif x == 'HT':
        arr1 = np.linspace(0,0,num=12)
        result=round(math.pow((carat * 100 ) / (ratio * depth_per * 0.00632),(1/3)),2)
        for i in range(0,len(arr)):
            y = round(math.pow((carat * 100 ) / (ratio * arr[i] * 0.00632),(1/3)),2)
            arr1[i] = y

    elif x == 'RN':
        arr1 = np.linspace(0,0,num=12)
        result=round(math.pow((carat * math.pow(ratio,2) * 100) / (depth_per * 0.00925),1/3),2)
        for i in range(0,len(arr)):
            y = round(math.pow((carat * math.pow(ratio,2) * 100) / (arr[i] * 0.00925),1/3),2)
            arr1[i] = y

    elif x == 'CM/CML':
        arr1 = np.linspace(0,0,num=12)
        result=round(math.pow((carat * math.pow(ratio,2) * 100) / (depth_per * 0.0087),1/3),2)
        for i in range(0,len(arr)):
            y = round(math.pow((carat * math.pow(ratio,2) * 100) / (arr[i] * 0.0087),1/3),2)
            arr1[i] = y

    elif x == 'PS':
        arr1 = np.linspace(0,0,num=12)
        result=round(math.pow((carat * math.pow(ratio,2) * 100) / (depth_per * 0.0066),1/3),2)
        for i in range(0,len(arr)):
            y = round(math.pow((carat * math.pow(ratio,2) * 100) / (arr[i] * 0.0066),1/3),2)
            arr1[i] = y

    elif x == 'PC':
        arr1 = np.linspace(0,0,num=12)
        result=round(math.pow((carat * math.pow(ratio,2) * 100) / (depth_per * 0.0099),1/3),2)
        for i in range(0,len(arr)):
            y = round(math.pow((carat * math.pow(ratio,2) * 100) / (arr[i] * 0.0099),1/3),2)
            arr1[i] = y

    elif x == 'OV':
        arr1 = np.linspace(0,0,num=12)
        result=round(math.pow((carat * math.pow(ratio,2) * 100) / (depth_per * 0.0082),1/3),2)
        for i in range(0,len(arr)):
            y = round(math.pow((carat * math.pow(ratio,2) * 100) / (arr[i] * 0.0082),1/3),2)
            arr1[i] = y
    
    return (result,arr1)

def display_output():
    res = calc(x)
    lblo['text']=str(res[0]) + ' mm'
    lb = [lb13,lb14,lb15,lb16,lb17,lb18,lb19,lb20,lb21,lb22,lb23,lb24]
    c = 183
    p=0
    for i in lb:
        i['text']=res[1][p]
        i.place(x=c,y=430)
        c = c + 40
        p = p + 1

def only_floats(char):
    if char == "":
        return True
    if char:
        try:
            float(char)
            return True
        except ValueError:
            return False
    else:
        return False


mywin=Tk()
# p1 = PhotoImage(file = '3.png')
# mywin.iconphoto(False,p1)

lbl=Label(mywin, text='Minimum Length Calculator',fg = '#D4AF37',bg = '#000000',font=("Times New Roman",18,'bold','underline'))
lbl.place(x=200, y=30)

lbl1=Label(mywin, text='Carat',font=("Times New Roman",16,'bold'),fg = '#D4AF37',bg = '#000000')
lbl1.place(x=200, y=100)

lbl2=Label(mywin, text='Ratio',font=("Times New Roman",16,'bold'),fg = '#D4AF37',bg = '#000000')
lbl2.place(x=200, y=150)

lbl3=Label(mywin, text='Maximum Depth %',font=("Times New Roman",16,'bold'),fg = '#D4AF37',bg = '#000000')
lbl3.place(x=80, y=200)

lbl4=Label(mywin, text='Minimum Length',font=("Times New Roman",16,'bold'),fg = '#D4AF37',bg = '#000000')
lbl4.place(x=80, y=330)

lbl5=Label(mywin, text='Depth %',font=("Times New Roman",14,'bold'),fg = '#D4AF37',bg = '#000000')
lbl5.place(x=22, y=380)

lbl6=Label(mywin, text='Minimum Length',font=("Times New Roman",14,'bold'),fg = '#D4AF37',bg = '#000000')
lbl6.place(x=22, y=430)

validation = mywin.register(only_floats)

t1=Entry(bd=4,font=("Times New Roman",14),fg = '#D4AF37',bg = '#000000',insertbackground="#D4AF37",validate='key',validatecommand=(validation, '%P'))
t1.place(x=300, y=100)

t2=Entry(bd=4,font=("Times New Roman",14),fg = '#D4AF37',bg = '#000000',insertbackground="#D4AF37",validate='key',validatecommand=(validation, '%P'))
t2.place(x=300, y=150)

t3=Entry(bd=4,font=("Times New Roman",14),fg = '#D4AF37',bg = '#000000',insertbackground="#D4AF37",validate='key',validatecommand=(validation, '%P'))
t3.place(x=300, y=200)

menu= StringVar()
menu.set("Select the Shape")

global x
#Create a dropdown Menu
drop= OptionMenu(mywin, menu,"EM", "HT","RN","CM/CML","PS","PC","OV",command=calc)
drop.config(font=("Times New Roman",14,'bold'),fg = '#D4AF37',bg = '#000000',width=13)
x = menu.get()
drop.place(x=140,y=260)

# Calculate button
btn1 = Button(mywin, text='Calculate',font=("Times New Roman",14,'bold'),fg = '#D4AF37',bg = '#000000',command=display_output)
btn1.place(x=327,y=260)

# Clear button
btn2 = Button(mywin, text='Clear',font=("Times New Roman",14,'bold'),fg = '#D4AF37',bg = '#000000',command=clear)
btn2.place(x=435,y=260)

# fixed range of depth %
arr = np.linspace(58,69,num=12)
lb1 = Label(mywin,text=arr[0],font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb2 = Label(mywin,text=arr[1],font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb3 = Label(mywin,text=arr[2],font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb4 = Label(mywin,text=arr[3],font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb5 = Label(mywin,text=arr[4],font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb6 = Label(mywin,text=arr[5],font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb7 = Label(mywin,text=arr[6],font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb8 = Label(mywin,text=arr[7],font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb9 = Label(mywin,text=arr[8],font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb10 = Label(mywin,text=arr[9],font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb11 = Label(mywin,text=arr[10],font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb12 = Label(mywin,text=arr[11],font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb = [lb1,lb2,lb3,lb4,lb5,lb6,lb7,lb8,lb9,lb10,lb11,lb12]
a = 183
for i in lb:
    i.place(x=a,y=380)
    a = a + 40

lblo = Label(mywin, text='',font=("Times New Roman",17,'bold'),fg = '#D4AF37',bg = '#000000')
lblo.place(x=320, y=330)
lb13 = Label(mywin,text='',font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb14 = Label(mywin,text='',font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb15 = Label(mywin,text='',font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb16 = Label(mywin,text='',font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb17 = Label(mywin,text='',font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb18 = Label(mywin,text='',font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb19 = Label(mywin,text='',font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb20 = Label(mywin,text='',font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb21 = Label(mywin,text='',font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb22 = Label(mywin,text='',font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb23 = Label(mywin,text='',font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')
lb24 = Label(mywin,text='',font=("Times New Roman",12),fg = '#D4AF37',bg = '#000000')

mywin.title('Minimum Length Calculator')
mywin['bg']='black'
mywin.geometry("700x500+400+300")
mywin.maxsize(700,500)
mywin.mainloop()