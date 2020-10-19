import random as rd
import tkinter as tk
from tkinter import messagebox


S = True
def start():
    while 1:
        if S == True:
            import random
            p = {1: '周嘉铖', 2: '钱珑超', 3: '徐展', 4: '尤桉哲', 5: '钱涛', 6: '黄舒怡', 7: '胡志辉', 8: '吴昭耀',
             9: '陈萌萌', 10: '郑巧悦', 11: '陈艳', 12: '梁明皓', 13: '蒋俊超', 14: '徐颖', 15: '倪宏涛', 16: '潘梦倩',
             17: '俞靖庐', 18: '王中阳', 19: '毛贞强', 20: '张嫒', 21: '朱速航', 22: '陈涛', 23: '陆远超', 24: '叶振雄',
             25: '奚申杰', 26: '叶梦婷', 27: '徐丽丽', 28: '潘艳'}
            n = int(text.get())
            a = random.sample(p.keys(), n)
            for i in a:
                A = print('抽到的同学为：第{0}号{1}'.format(str(i), p[i]))
                global label2
                label2 = tk.Label(window,text=A).grid(row=10,column=10,ipadx=10,ipady=10)
        else:
            p = {1: '周嘉铖', 2: '钱珑超', 3: '徐展', 4: '尤桉哲', 5: '钱涛', 6: '黄舒怡', 7: '胡志辉', 8: '吴昭耀',
                 9: '陈萌萌', 10: '郑巧悦', 11: '陈艳', 12: '梁明皓', 13: '蒋俊超', 14: '徐颖', 15: '倪宏涛', 16: '潘梦倩',
                 17: '俞靖庐', 18: '王中阳', 19: '毛贞强', 20: '张嫒', 21: '朱速航', 22: '陈涛', 23: '陆远超', 24: '叶振雄',
                 25: '奚申杰', 26: '叶梦婷', 27: '徐丽丽', 28: '潘艳'}
            n = int(text.get())
            a = random.sample(p.keys(), n)
            for i in a:
                A = print('抽到的同学为：第{0}号{1}'.format(str(i), p[i]))
                messagebox.askokcancel('恭喜', A)


def stop():
    global S
    S = False
    start()




window = tk.Tk() #创建窗口window
window.title('抽人')
window.geometry('400x400') #设置窗口的长和宽
window.resizable(width=True,height=True) #窗口变为可调



# 设置和接受输入的内容
text = tk.StringVar() #StringVar为跟踪变量的值的变化，以保证值的变更随时可以显示在界面上
text.set('')
en = tk.Entry(window) #创建文本框
en['textvariable'] = text #textvariable 可变文字
en.grid(row=4,column=2,ipadx=10,ipady=10,pady=10)

label1 = tk.Label(window,text='要选几抽个人:').grid(row=2,column=2,ipadx=10,ipady=10)



button1 = tk.Button(window,text='停止',command=stop).grid(row=4,column=5,ipadx=3,ipady=3,padx=10,pady=5)#padx,pady为x轴或者y轴所留白部分
button2 = tk.Button(window,text='开始',command=start).grid(row=4,column=1,ipadx=3,ipady=3,padx=10,pady=5)
window.mainloop()


# import random as rd
# import tkinter as tk
# from tkinter import messagebox
# import threading
#
#
#
# def pok():
#     global Sure
#     Sure = False
#     while 1:
#         if Sure:
#             p = {1: '周嘉铖', 2: '钱珑超', 3: '徐展', 4: '尤桉哲', 5: '钱涛', 6: '黄舒怡', 7: '胡志辉', 8: '吴昭耀',
#                  9: '陈萌萌', 10: '郑巧悦', 11: '陈艳', 12: '梁明皓', 13: '蒋俊超', 14: '徐颖', 15: '倪宏涛', 16: '潘梦倩',
#                  17: '俞靖庐', 18: '王中阳', 19: '毛贞强', 20: '张嫒', 21: '朱速航', 22: '陈涛', 23: '陆远超', 24: '叶振雄',
#                  25: '奚申杰', 26: '叶梦婷', 27: '徐丽丽', 28: '潘艳'}
#             a = rd.sample(p.keys(), 1)
#             for i in a:
#                 A = print('抽到的同学为：第{0}号{1}'.format(str(i), p[i]))
#                 global label2
#                 label2 = tk.Label(window, text=A).grid(row=10, column=10, ipadx=10, ipady=10)
#
#
# def start():
#     global Sure
#     Sure = True
#     global n
#
#
#
# def stop():
#     global Sure
#     Sure = False
#     messagebox.askokcancel('恭喜', text=A)
#
#
#
# window = tk.Tk() #创建窗口window
# window.title('抽人')
# window.geometry('400x400') #设置窗口的长和宽
# window.resizable(width=True,height=True) #窗口变为可调
#
# # 设置和接受输入的内容
# text = tk.StringVar() #StringVar为跟踪变量的值的变化，以保证值的变更随时可以显示在界面上
# text.set('')
# en = tk.Entry(window) #创建文本框
# en['textvariable'] = text #textvariable 可变文字
# en.grid(row=4,column=2,ipadx=10,ipady=10)
#
#
# task=threading.Thread(target=pok)
# task.start()
#
#
# button1 = tk.Button(window,text='停止',command=stop).grid(row=4,column=5,ipadx=3,ipady=3,padx=10,pady=5)#padx,pady为x轴或者y轴所留白部分
# button2 = tk.Button(window,text='开始',command=start).grid(row=4,column=1,ipadx=3,ipady=3,padx=10,pady=5)
# window.mainloop()

#
# import tkinter as tk,random,threading,time
#
# def pok():
#     global s
#     s = False
#     while 1:
#         if s == True:
#             p = {1: '周嘉铖', 2: '钱珑超', 3: '徐展', 4: '尤桉哲', 5: '钱涛', 6: '黄舒怡', 7: '胡志辉', 8: '吴昭耀',
#                  9: '陈萌萌', 10: '郑巧悦', 11: '陈艳', 12: '梁明皓', 13: '蒋俊超', 14: '徐颖', 15: '倪宏涛', 16: '潘梦倩',
#                  17: '俞靖庐', 18: '王中阳', 19: '毛贞强', 20: '张嫒', 21: '朱速航', 22: '陈涛', 23: '陆远超', 24: '叶振雄',
#                  25: '奚申杰', 26: '叶梦婷', 27: '徐丽丽', 28: '潘艳'}
#             Name = p[random.randint(1,28)]
#             label1['text']= Name
#             label_winner = Label(self.root, font=("华文行楷", 20), width=45, height=10, fg="red",textvariable=self.label_str)
#
# def start():
#     global s
#     s = True
# def stop():
#     global s
#     s = False
#
# window = tk.Tk()
# window.title('抽人')
# window.geometry('300x300')
# window.resizable(width=True,height=True)
#
#
# button1 = tk.Button(window,text='停止',command=stop).grid(row=4,column=5,ipadx=3,ipady=3,padx=150,pady=5)
# button2 = tk.Button(window,text='开始',command=start).grid(row=4,column=1,ipadx=3,ipady=3,padx=10,pady=5)
# label1 = tk.Label(window, text='').grid(row=5, column=2, ipadx=10, ipady=10).pack()
#
# task=threading.Thread(target=pok)
# task.start()
#
# window.mainloop()