import tkinter.messagebox
from tkinter import *
import pymysql
# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "tingshi")
cursor = db.cursor()
class Reg (Frame):
    def __init__(self,master):
        frame = Frame(master)
        frame.grid()

        self.button= Button(frame,text = "个人信息查询",width=20,height=5,command = self.chaxun)
        self.button.grid(row = 0)
        self.button2 = Button(frame,text = "出库申请",width=20,height=5,command=self.apply)
        self.button2.grid(row = 0,column = 1)
        self.button3 = Button(frame,text = "节哀",width=20,height=5)
        self.button3.grid(row = 1,column = 0,sticky =W)
        self.button4 = Button(frame,text = "顺变",width=20,height=5)
        self.button4.grid(row = 1,column = 1,sticky = W)
        self.button6 = Button(frame,text = "安慰系统",width=20,height=5,command=self.cor)
        self.button6.grid(row = 2,column = 0,sticky = W)
        self.button5 = Button(frame,text = "退出系统",command = frame.quit,width=20,height=5)
        self.button5.grid(row = 2,column = 2,sticky =W)
    def chaxun(self):
        tc =Tk()
        tc.grid()
        self.lab1 = Label(tc, text="请输入用户ID")
        self.lab1.grid(row = 0,column = 0,sticky = W)
        self.ent1 = Entry(tc)
        self.ent1.grid(row = 0,column = 1,sticky = W)
        self.lab2 = Label(tc, text="请输入您的名字")
        self.lab2.grid(row = 1,column = 0,sticky = W)
        self.ent2 = Entry(tc)
        self.ent2.grid(row = 1,column = 1,sticky = W)
        self.button = Button(tc,text="go",command=self.chaxun2)
        self.button.grid(row=3,sticky=W)
        # self.button2 = Button(tc,text="quit",command=tc.quit)
        # self.button2.grid(row=3,sticky=E)
    def chaxun2(self):
        a = self.ent1.get()
        b = self.ent2.get()
        sql='select name,cor_name from p where user_id=%s and name="%s"'% (a,b)
        try:
            print(sql)
            cursor.execute(sql)
            result=cursor.fetchall()
            print(sql,result)
            for i in result:
                name=i[0]
                cor_name=i[1]
            tkinter.messagebox.showinfo('查询成功','你好%s的家属%s，请节哀顺变'%(cor_name,name))
            print(result)
        except:
            tkinter.messagebox.showwarning('警告','请不要乱查询')
    def apply(self):
        tc=Tk()
        tc.grid()
        self.lab1 = Label(tc, text="尸体姓名:")
        self.lab1.grid(row=0, column=0, sticky=W)
        self.ent1 = Entry(tc)
        self.ent1.grid(row=0, column=1, sticky=W)
        self.lab2 = Label(tc, text="尸体ID:")
        self.lab2.grid(row=1, column=0)
        self.ent2 = Entry(tc)
        self.ent2.grid(row=1, column=1, sticky=W)
        self.lab3 = Label(tc, text="申请人姓名:")
        self.lab3.grid(row=2, column=0)
        self.ent3 = Entry(tc)
        self.ent3.grid(row=2, column=1, sticky=W)
        self.button=Button(tc,text='确定',command=self.apply2)
        self.button.grid(row=3,column=0)
        self.button = Button(tc, text='退出',command = tc.quit)
        self.button.grid(row=3, column=3)
    def apply2(self):
        s1 = self.ent1.get()#cor_name
        s2 = self.ent2.get()#id
        s3=self.ent3.get()#name
        sql='select name from cor where id=%s'%(s2)
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            print(bool(s1 in result),result)
            if s1 in result:
                # print('sbnb')
                sql2='select name,cor_name from p'
                cursor.execute(sql2)
                result2 = cursor.fetchall()
                print(result2,bool(s3==result2[0][0]))

                if (s3==result2[0][0]):

                    sql3="select max(id) from apply"
                    cursor.execute(sql3)
                    result3=cursor.fetchall()
                    i=result3[0][0]
                    print(type(s2),type(i),i,result3)
                    sql4='insert into apply(id,cor_id,cor_name,name,type) values' + ' (%d,%d,"%s","%s","家属申请")' % (i+1,int(s2),s1,s3)
                    sql5='select cor_id from apply'
                    cursor.execute(sql5)
                    result4=cursor.fetchall()
                    x=0
                    while x<len(result4):
                        if int(s2) in result4[x]:
                            print('yicunzai')
                            tkinter.messagebox.showwarning('警告', '该尸体已被申请')
                            break
                        x+=1
                        print(result2[0][1])
                        print(s3)
                        print(bool(s3==result2[0][1]))

                        if (s1==result2[0][1]):
                            try:
                            # 执行sql语句

                                cursor.execute(sql4)

                                # 提交到数据库执行
                                db.commit()
                                break
                            except Exception:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                        else:
                            tkinter.messagebox.showwarning('警告', '不是你家人也敢出库？')
                            break
                elif(s3==result2[1][0]):
                    sql3 = "select max(id) from apply"
                    cursor.execute(sql3)
                    result3 = cursor.fetchall()
                    i = result3[0][0]
                    print(type(s2), type(i), i, result3)
                    sql4 = 'insert into apply(id,cor_id,cor_name,name,type) values' + ' (%d,%d,"%s","%s","家属申请")' % (
                    i + 1, int(s2), s1, s3)
                    sql5 = 'select cor_id from apply'
                    cursor.execute(sql5)
                    result4 = cursor.fetchall()
                    x = 0
                    while x < len(result4):
                        if int(s2) in result4[x]:
                            print('yicunzai')
                            tkinter.messagebox.showwarning('警告', '该尸体已被申请')
                            break
                        x += 1
                        print(result2)
                        print(s2)
                        print(bool(s3 == result2))

                        if (s1 == result2[1][1]):
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                # 提交到数据库执行
                                db.commit()
                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                        else:
                            tkinter.messagebox.showwarning('警告', '不是你家人也敢出库？')
                else:
                    tkinter.messagebox.showwarning('警告', '你不是家属你是谁')
            else:
                tkinter.messagebox.showwarning('警告', '尸体信息不匹配')
                # print(result[0])
        except:
            tkinter.messagebox.showwarning('警告', '尸体id信息错误')
    def cor(self):
        tc=Tk()
        tc.title('道路千万条，开心第一条')
        tc.frma=Frame(tc,width=500,height=500,bg='yellow')
        tc.frmb=Frame(tc,width=500,height=500,bg='red')
        tc.frma.grid(row=0,column=0)
        tc.frmb.grid(row=1, column=0)
        sql = 'select cor_name,name company from p'
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            j = 0
            print(result)

        except:
            tkinter.messagebox.showwarning('警告', '请不要乱查询')
        # self.te=Label(frma,width=50,height=5)
        # self.te.grid(frma,row=10,column=10)
        # btnSend = Button(tc.frma, text='发 送', width=8)  # 在frmLB容器中添加
        # btnSend.grid(row=2, column=0)
        # btnCancel = Button(tc.frma, text='取消', width=8)
        # btnCancel.grid(row=2, column=1, sticky=E)


        while j < len(result):
            self.j = Text(tc.frma, width=50, height=5)
            self.j.grid(column=0)
            self.j.insert(INSERT, '尸体名:%s，家属:%s' % (result[j][0], result[j][1]))
            j += 1
        self.lab=Label(tc.frmb,text='你看他们家也死了人，生活还要继续，加油啊',width=50,height=10,font=("黑体",8))
        self.lab.grid()
        tc.frma.grid_propagate(0)
        tc.frmb.grid_propagate(0)
def my():
    root = Tk()
    root.title("家属系统")
    app = Reg(root)
    root.mainloop()
# my()