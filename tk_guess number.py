import random as rd
import tkinter as tk
from tkinter import messagebox #不加这条，下面使用messagebox的时候不知道为啥，会报错

num = rd.randint(1,1024)
def guess_number():
    try:
        guess_num = int(text.get())
        if guess_num < num:
            print(messagebox.askokcancel('提示','太小了'))
        elif guess_num > num:
            print(messagebox.askokcancel('提示','太大了'))
        else:
            print(messagebox.askokcancel('提示','猜对啦'))
    except:
        print(messagebox.askokcancel('提示','请输入1-1024的数字'))
def again():
    global num #将num变为全局变量
    set_num = random.randint(1,1024)
    print(num)


window = tk.Tk()
window.title('猜数字1-1024') #创建窗口window
window.geometry('400x400') #设置窗口的长和宽
window.resizable(width=True,height=True) #窗口变为可调
label1 = tk.Label(window,text='输入一个数:',bg='blue').grid(row=2,column=2,ipadx=10,ipady=10)

text = tk.StringVar() #设置和接受输入的内容
text.set('')
en = tk.Entry(window)
en['textvariable'] = text
en.grid(row=4,column=2,ipadx=10,ipady=10) #text variable 可变文字
button1 = tk.Button(window,text='确定',command=guess_number).grid(row=4,column=5,ipadx=3,ipady=3,padx=5,pady=5)#padx,pady为x轴或者y轴所留白部分
button2 = tk.Button(window,text='再玩一次',command=again).grid(row=4,column=1,ipadx=3,ipady=3,padx=5,pady=5)
window.mainloop()


