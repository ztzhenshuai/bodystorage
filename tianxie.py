import tkinter as tk
import pymysql
import tkinter.messagebox
import time
db = pymysql.connect("localhost", "root", "123456", "tingshi")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
now = time.strftime("%Y-%m-%d %H:%M:%S")


def initialGUI():
    TITLE = "choose"
    WIDTH = 1000
    HEIGHT = 500
    window = tk.Tk()
    window.title(TITLE)
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    window.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, ws / 2, hs / 2))
    window.grid()

    bt1=tk.Button(window,text='入库单',command=lambda :click(1))
    bt1.grid(row=0,column=0)
    bt2 = tk.Button(window,text='出库单',command=lambda :click(0))
    bt2.grid(row=1,column=1)
    bt3 = tk.Button(window,text='移库单',command=lambda :click(0))
    bt3.grid(row=2,column=2)
    def click(q):
        if q==0:
            tk.messagebox.showwarning('警告', '请前往库存查询中填写该单据')
        else:
            tc=tk.Tk()
            lab1=tk.Label(tc,text='尸体姓名')
            lab1.grid(row=0,column=0)
            lab2 = tk.Label(tc, text='医生编号' )
            lab2.grid(row=1, column=0)
            lab3 = tk.Label(tc, text='医生姓名')
            lab3.grid(row=2, column=0)
            lab4 = tk.Label(tc, text='货位编号')
            lab4.grid(row=3, column=0)
            lab5 = tk.Label(tc, text='家属姓名' )
            lab5.grid(row=4, column=0)
            lab6 = tk.Label(tc, text='入库公司' )
            lab6.grid(row=5, column=0)
            ent1 =tk.Entry(tc)
            ent1.grid(row=0, column=1)
            ent2 = tk.Entry(tc)
            ent2.grid(row=1, column=1)
            ent3 = tk.Entry(tc)
            ent3.grid(row=2, column=1)
            ent4 = tk.Entry(tc)
            ent4.grid(row=3, column=1)
            ent5 = tk.Entry(tc)
            ent5.grid(row=4, column=1)
            ent6 = tk.Entry(tc)
            ent6.grid(row=5, column=1)
            def ruku(a):
                c_name=ent1.get()#c_name
                d_id = ent2.get()#d_id
                d_name= ent3.get()#d_name
                l_id = ent4.get()
                p_name = ent5.get()
                company=ent6.get()
                sql1='select max(id) from tingshi.in'
                sql2='select max(id) from cor'
                cursor.execute(sql1)
                result = cursor.fetchall()
                i=result[0][0]
                cursor.execute(sql2)
                result = cursor.fetchall()
                j=result[0][0]
                print(type(i),type(j),i,j)
                sql='insert into tingshi.in values '+'(%d,%d,"%s",%d,"%s","%s",%d)'%(int(i+1),int(j+1),c_name,int(d_id),d_name,now,int(l_id))
                sql1='insert into tingshi.cor values '+'(%d,"%s",%d,"%s")'%(int(j+1),c_name,int(l_id),company)
                sql2='update loc set cor_id=%d where id=%d'%(int(j+1),int(l_id))
                print(sql)
                try:
                    cursor.execute(sql1)
                    db.commit()


                except:
                    # 发生错误时回滚
                    print("sql1 wrong")
                    db.rollback()
                try:
                    cursor.execute(sql)
                    db.commit()


                except:
                    # 发生错误时回滚
                    print("sql wrong")
                    db.rollback()
                try:
                    cursor.execute(sql2)
                except:
                    print('sql2 wrong')
                if a==1:
                    sql1='select max(id) from tingshi.user'
                    cursor.execute(sql1)
                    result = cursor.fetchall()
                    i = result[0][0]
                    sql2 = 'select max(id) from tingshi.p'
                    cursor.execute(sql2)
                    result = cursor.fetchall()
                    k = result[0][0]
                    sql1 = 'insert into tingshi.user values ' + '(%d,"%s",%d)' % (
                    int(i + 1), '000000', 2)
                    sql = 'insert into tingshi.p values ' + '(%d,"%s","%s",%d,%d)' % (
                        int(k + 1), p_name, c_name, int(j+1),  int(i+1))
                    try:
                        cursor.execute(sql1)
                        db.commit()


                    except:
                        # 发生错误时回滚
                        print("sql1 wrong")
                        db.rollback()
                    try:
                        cursor.execute(sql)
                        db.commit()


                    except:
                        # 发生错误时回滚
                        print("sql wrong")
                        db.rollback()
            bt1=tk.Button(tc,text='无家属入库',command=lambda:ruku(0))
            bt1.grid(row=6,column=0)
            bt2=tk.Button(tc,text='有家属入库',command=lambda:ruku(1))
            bt2.grid(row=6,column=1)

    window.mainloop()
# initialGUI()
