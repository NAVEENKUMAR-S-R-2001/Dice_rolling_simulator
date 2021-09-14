import random
from tkinter import *

def roll(event=0):
    number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']

    label1.config(bg='red',text=f'{random.choice(number)}  {random.choice(number)}')
    label1.pack()
win=Tk()
win.title('DICE SIMULATOR')
win.geometry('700x450')
win.configure(bg='green')
label1=Label(win,font=('times',200))
button=Button(win,text='CLICK HERE TO ROLL THE DICE ',bg='black',fg='white',command=roll,relief='solid')
button.pack()


label2=Label(win,text='OR PRESS THE ENTER KEY',bg='black',fg='white',font=('times',20)).pack()
win.bind('<Return>',roll)
win.mainloop()
