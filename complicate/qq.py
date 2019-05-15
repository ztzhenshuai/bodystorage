import pymysql
import tkinter.messagebox
import doc
import p
import police
import os
from tkinter import *
db = pymysql.connect("localhost", "root", "123456", "tingshi")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)
root = Tk()
root.title("welcome")
class Reg (Frame):
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.lab1 = Label(frame,text = "User:")
        self.lab1.grid(row = 0,column = 0,sticky = W)
        self.ent1 = Entry(frame)
        self.ent1.grid(row = 0,column = 1,sticky = W)
        self.lab2 = Label(frame,text = "Password:")
        self.lab2.grid(row = 1,column = 0)
        self.ent2 = Entry(frame,show = "*")
        self.ent2.grid(row = 1,column = 1,sticky = W)
        self.button = Button(frame,text = "Submit",command = self.Submit)
        self.button.grid(row = 2,column = 0,sticky =W)
        self.button3 = Button(frame,text = "Hello")
        self.button3.grid(row = 2,column = 2,sticky = W)
        self.button2 = Button(frame,text = "Quit",command = frame.quit)
        self.button2.grid(row = 2,column = 3,sticky =W)
    def Submit(self):
        s1 = self.ent1.get()
        s2 = self.ent2.get()

        sql = "SELECT password,auth FROM user where id=%s" % (s1)
        # 执行SQL语句
        # print(sql)
        try:
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            # # 关闭数据库连接
            # db.close()
            if s2 in results[0]:
                if 1 in results[0]:
                    x = tkinter.messagebox.askyesno('欢迎你', '以医生身份进入？')
                    root.destroy()
                    #是/否，返回值true/false
                    if x:
                        doc.my()

                if 2 in results[0]:
                    x=tkinter.messagebox.askyesno('欢迎你', '以家属身份进入？')
                    root.destroy()
                    if x:
                        p.my()
                        # root.destroy()
                    # else:
                    #     root.destroy()
                if 3 in results[0]:
                    x=tkinter.messagebox.askyesno('欢迎你', '以警察身份进入？')
                    root.destroy()
                    if x:
                        police.my()

            else:
                tkinter.messagebox.showinfo('密码错误 ', '请重新输入')


        except:
            tkinter.messagebox.showinfo('用户不存在', '请不要乱输')
            self.ent1.delete(0, len(s1) )
            self.ent2.delete(0, len(s2) )

app = Reg(root)
root.mainloop()
