import random
from tkinter import *
import threading
from tkinter import messagebox as msgbox
import pygame

window= Tk()

list_1=["周嘉铖","钱珑超","徐展","尤桉哲","钱涛","黄舒怡","胡志辉","吴昭耀","陈萌萌","郑巧悦","陈艳","梁明皓","蒋俊超","徐颖","倪宏涛","潘梦倩","俞靖庐","王中阳","毛贞强","张嫒","朱速航",
                "陈涛","陆远超","叶振雄","奚申杰","叶梦婷","徐丽丽","潘艳"]

file=r'G:\CloudMusic\小旭音乐 - 欢乐斗地主背景音乐.mp3'
pygame.mixer.init()
track = pygame.mixer.music.load(file)

class run():
    def __init__(self):
        self.window=window
        self.msgbox=msgbox
        self.window.geometry("800x400+280+80")
        self.window.title("抽人系统")
        self.button_start=Button(self.window,text="开始",width=6,command=self.start)
        self.button_stop=Button(self.window,text="停止",width=6,command=self.stop)
        self.label_str=StringVar()
        self.label_str.set("0.0")
        self.label_winner = Label(self.window, font=("华文行楷", 20), width=20, height=30,fg="black",textvariable=self.label_str)
        self.label_winner.pack()
        self.button_start.place(relx=0.2,rely=0.7)
        self.button_stop.place(relx=0.7,rely=0.7)
        self.ready=0
        self.window.mainloop()


    def draw(self):
        print("滚动显示都抽到了哪些人")
        global list_1
        while self.ready:
            index_num = random.randint(1, 1000) % len(list_1)
            #print(index_num)
            people = list_1[index_num]
            self.label_str.set(people)
        print("抽中的人是" + people)
        self.msgbox.showinfo("结果", "抽到的人是" + people )


    def start(self):
        print("开始抽奖")
        self.ready=1
        self.thread=threading.Thread(target=self.draw,args=())
        self.thread.setDaemon(True)
        self.thread.start()
        #多线程运行
        pygame.mixer.music.play()



    def stop(self):
        print("结束抽奖")
        global winner
        self.ready=0
        pygame.mixer.music.stop()


if __name__ == '__main__':
    Lottery=run()
