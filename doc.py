import tkinter.messagebox
from tkinter import *
import pymysql
import kuncun2
import danju
import tianxie


# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "tingshi")
cursor = db.cursor()
class Reg (Frame):
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.button= Button(frame,text = "医生信息查询",width=20,height=5,command = self.chaxun)
        self.button.grid(row = 0)
        self.button2 = Button(frame,text = "查看申请",width=20,height=5,command=self.apply)
        self.button2.grid(row = 0,column = 1)
        self.button3 = Button(frame,text = "单据查询",width=20,height=5,command=danju.initialGUI)
        self.button3.grid(row = 1,column = 0,sticky =W)
        self.button4 = Button(frame,text = "单据填写",width=20,height=5,command=tianxie.initialGUI)
        self.button4.grid(row = 1,column = 1,sticky = W)
        self.button6 = Button(frame,text = "库存查询",width=20,height=5,command=kuncun2.initialGUI)
        self.button6.grid(row = 2,column = 0,sticky = W)
        self.button5 = Button(frame,text = "退出系统",command = frame.quit,width=20,height=5)
        self.button5.grid(row = 2,column = 2,sticky =W)
    def chaxun(self):
        tc =Tk()
        tc.grid()
        self.lab1 = Label(tc,text = "请输入用户ID")
        self.lab1.grid(row = 0,column = 0,sticky = W)
        self.ent1 = Entry(tc)
        self.ent1.grid(row = 0,column = 1,sticky = W)
        self.button = Button(tc,text="go",command=self.chaxun2)
        self.button.grid(row=3,sticky=W)
        # self.button2 = Button(tc,text="quit",command=tc.quit)
        # self.button2.grid(row=3,sticky=E)
    def chaxun2(self):
        a = self.ent1.get()
        sql='select * from doc where user_id=%s'%(a)
        try:
            cursor.execute(sql)
            result=cursor.fetchall()
            for i in result:
                id=i[0]
                company=i[2]
                name=i[1]
            tkinter.messagebox.showinfo('查询成功','你好编号为%s的%s的%s医生'%(id,company,name))
            print(result[0][3])
        except:
            tkinter.messagebox.showwarning('警告','请不要乱查询')
    def apply(self):
        sql = 'select cor_id,cor_name,name,apply.type from apply'
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            j=0

        except:
            tkinter.messagebox.showwarning('警告', '请不要乱查询')
        tc = Tk()
        tc.grid()
        lb3 = Listbox(tc, selectmode='BROWSE', height=30)
        lb3.grid(row=0,column=1,sticky=W)
        lb1 = Listbox(tc, selectmode='extended', height=30)
        lb1.grid(row=0,column=2,sticky=W)
        lb2 = Listbox(tc, selectmode='extended', height=30)
        lb2.grid(row=0,column=3,sticky=W)
        lb4 = Listbox(tc, selectmode='extended', height=30)
        lb4.grid(row=0,column=4,sticky=W)
        lb4.insert(0, '尸体编号')
        lb3.insert(0, '尸体姓名')
        lb1.insert(0, '申请人姓名')
        lb2.insert(0, '申请类型')
        def show_msg(*args):
            indexs = lb3.curselection()
            id = int(indexs[0])
            s_name = lb3.get(id)
            name = lb1.get(indexs[0])
            s_id = lb4.get(id)
            type = lb2.get(id)
            tc=Tk()
            tc.title('申请详情')
            lab1 = Label(tc, text="尸体id")
            lab1.grid(row=0, column=0, )
            lab2 = Label(tc, text="尸体名称")
            lab2.grid(row=1, column=0)
            lab3 = Label(tc, text="申请人姓名")
            lab3.grid(row=2, column=0)
            lab4 = Label(tc, text="申请类型")
            lab4.grid(row=3, column=0)
            tt1 = Text(tc, width=10, height=1)
            tt1.grid(row=0, column=1)
            tt1.insert(INSERT, s_id)
            tt2 = Text(tc, width=10, height=1)
            tt2.grid(row=1, column=1)
            tt2.insert(INSERT, s_name)
            tt3 = Text(tc, width=10, height=1)
            tt3.grid(row=2, column=1)
            tt3.insert(INSERT,name)
            tt4 = Text(tc, width=10, height=1)
            tt4.grid(row=3, column=1)
            tt4.insert(INSERT, type)
            def qq(z):
                if z==1:
                    tkinter.messagebox.showwarning('恭喜你', '操作成功，请填写出库单')
                else:
                    tkinter.messagebox.showwarning('为什么要拒绝呢？', '做人留一线，日后好相见')
            bt = Button(tc, text='批准',command=lambda:qq(1))

            bt.grid(row=4, column=0)
            bt1 = Button(tc, text='拒绝', command=lambda:qq(2))
            bt1.grid(row=4, column=1)
        while j < len(result):
            lb4.insert(result[j][0], result[j][0])
            lb3.insert(result[j][0], result[j][1])
            lb1.insert(result[j][0], result[j][2])
            lb2.insert(result[j][0], result[j][3])
            j += 1
        lb3.bind("<<ListboxSelect>>", show_msg)
            # self.button5 = Button(text="next page", width=20, height=5)
            # self.button5.grid(row = 0,column = 1,sticky = E)
        # self.lab1.grid(row=0, column=0, sticky=W)
        # self.ent1 = Entry(tc)
        # self.ent1.grid(row=0, column=1, sticky=W)
        # self.button = Button(tc, text="go", command=self.chaxun2)
        # self.button.grid(row=3, sticky=W)

        # frame = Frame()
        # frame.pack()
        # self.lab2 = Label(frame,text = "Password:")
        # self.lab2.grid(row = 1,column = 0)
        # self.ent2 = Entry(frame, show="*")
        # self.ent2.grid(row=1, column=1, sticky=W)
    # def Submit(self):
    #     s1 = self.ent1.get()
    #     s2 = self.ent2.get()
    #     if s1 == 'freedom' and s2 == '123':
    #         tkinter.messagebox.showinfo('hhh', 'sss')
    #     else:
    #         tkinter.messagebox.showinfo('hhhss', 'ssqqqss')
    #     self.ent1.delete(0,len(s1))
    #     self.ent2.delete(0,len(s2))


def my():
    root = Tk()
    root.title("医生系统")
    app = Reg(root)
    root.mainloop()


if __name__ == "__main__":
    my()