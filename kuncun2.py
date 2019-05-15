import tkinter as tk
import pymysql
import tkinter.messagebox
import time




import tkinter as tk
import pymysql
import tkinter.messagebox
db = pymysql.connect("localhost", "root", "123456", "tingshi")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
now = time.strftime("%Y-%m-%d %H:%M:%S")

# class TestBenchMaker:

        #
        # TITLE = "Test"
        # WIDTH = 500
        # HEIGHT = 500
        # parseDic = {}

    # Initial GUI
def initialGUI():
    TITLE = "库存详情"
    WIDTH = 1000
    HEIGHT = 500
    parseDic = {}

    # Change tag
    def changeTag(tag):
        frame3.pack_forget()
        frame4.pack_forget()
        frame5.pack_forget()
        frame6.pack_forget()
        frame7.pack_forget()
        if tag == 0:
            frame3.pack(fill=tk.X)
        elif tag == 1:
            frame4.pack(fill=tk.X)
        elif tag == 2:
            frame5.pack(fill=tk.X)
        elif tag == 3:
            frame6.pack(fill=tk.X)
        elif tag == 4:
            frame7.pack(fill=tk.X)


    window = tk.Tk()
    window.title(TITLE)

    # Place GUI on the center of screen
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - (WIDTH / 2)
    y = (hs / 2) - (HEIGHT / 2)
    window.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, ws/2, hs/2))




        # Tag: 0 --> input; 1 --> output; 2 --> other
    frame2 = tk.Frame(window)
    frame2.pack(fill=tk.Y, pady=10)
    tag = tk.IntVar()
    tagWidth = 23
    tk.Radiobutton(frame2, text="第一页", command=lambda: changeTag(0), width=tagWidth, variable=tag, value=0, bd=1, indicatoron=0).grid(column=0, row=1)
    tk.Radiobutton(frame2, text="第二页", command=lambda: changeTag(1), variable=tag, width=tagWidth, value=1, bd=1, indicatoron=0).grid(column=1, row=1)
    tk.Radiobutton(frame2, text="第三页", command=lambda: changeTag(2), variable=tag, width=tagWidth, value=2, bd=1, indicatoron=0).grid(column=2, row=1)
    tk.Radiobutton(frame2, text="第四页", command=lambda: changeTag(3), variable=tag, width=tagWidth, value=3, bd=1,indicatoron=0).grid(column=3, row=1)
    tk.Radiobutton(frame2, text="第五页", command=lambda: changeTag(4), variable=tag, width=tagWidth, value=4, bd=1,indicatoron=0).grid(column=4, row=1)


    frame5 = tk.Frame(window, height=350, bg="yellow")

    def fenye1():
        sql = 'select id,name,company,location_id from cor'
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            # j = 0
            print(result)

        except:
            tk.messagebox.showwarning('警告', '请不要乱查询')
        # self.te=Label(frma,width=50,height=5)
        # self.te.grid(frma,row=10,column=10)
        # btnSend = Button(tc.frma, text='发 送', width=8)  # 在frmLB容器中添加
        # btnSend.grid(row=2, column=0)
        # btnCancel = Button(tc.frma, text='取消', width=8)
        # btnCancel.grid(row=2, column=1, sticky=E)
        lb3 = tk.Listbox(frame5, selectmode='BROWSE', height=len(result))
        lb3.pack(side='left', fill='both')
        lb1 = tk.Listbox(frame5, selectmode='extended', height=len(result))
        lb1.pack(side='left', fill='both')
        lb2 = tk.Listbox(frame5, selectmode='extended', height=len(result))
        lb2.pack(side='left', fill='both')
        lb4 = tk.Listbox(frame5, selectmode='extended', height=len(result))
        lb4.pack(side='left', fill='both')
        lb4.insert(0, '货位编号')
        lb3.insert(0, '尸体编号')
        lb1.insert(0, '尸体姓名')
        lb2.insert(0, '存放单位')
        j = 49
        def show_msg(*args):

            indexs = lb3.curselection()
            id = int(indexs[0])
            s_id=lb3.get(id)
            s_name=lb1.get(indexs[0])
            s_id2=lb4.get(id)
            s_company=lb2.get(id)
            # print(s_id,s_name,s_id2,s_company)
            tc=tk.Tk()
            tc.title('单据填写')
            lab1 = tk.Label(tc, text="尸体id")
            lab1.grid(row=0, column=0,)
            lab2 = tk.Label(tc, text="尸体名称")
            lab2.grid(row=1, column=0)
            lab3 = tk.Label(tc, text="操作人姓名")
            lab3.grid(row=2, column=0)
            lab4 = tk.Label(tc, text="老货位编号")
            lab4.grid(row=3, column=0)
            lab5= tk.Label(tc, text="新货位编号")
            lab5.grid(row=4, column=0)
            tt1= tk.Text(tc,width=10,height=1)
            tt1.grid(row=0, column=1)
            tt1.insert(tk.INSERT,s_id)
            tt2 = tk.Text(tc, width=10, height=1)
            tt2.grid(row=1, column=1)
            tt2.insert(tk.INSERT, s_name)
            tt3 = tk.Text(tc, width=10, height=1)
            tt3.grid(row=2, column=1)
            tt3.insert(tk.INSERT,'请在此输入')
            tt4 = tk.Text(tc, width=10, height=1)
            tt4.grid(row=3, column=1)
            tt4.insert(tk.INSERT, s_id2)
            tt5 = tk.Text(tc, width=10, height=1)
            tt5.grid(row=4, column=1)
            tt5.insert(tk.INSERT, '请在此输入')


            def out(z):
                p_name = tt3.get(1.0, 1.5)
                oloc_id=tt4.get(1.0,1.5)
                nloc_id=tt5.get(1.0,1.5)
                sql = 'select name from cor where id=%s' % (s_id)
                # try:
                cursor.execute(sql)
                result = cursor.fetchone()
                if s_name in result:
                    # print('sbnb')
                    sql2 = 'select name from doc'
                    cursor.execute(sql2)
                    result2 = cursor.fetchall()


                    if p_name in result2[0]:
                        if z==1:
                            sql3 = "select max(id) from a_out"
                        else:
                            sql3='select max(id) from m_out'
                        try:
                            print(1)
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)
                        if z==1:
                            sql5 = 'select cor_id from a_out'
                        else:
                            sql5 = 'select cor_id from m_out'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        # print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被出库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            if z==1:
                                sql6='select id from apply where cor_id=%s'%(s_id)
                            else:
                                sql6='select id from move where cor_id=%s'%(s_id)
                            try:
                                cursor.execute(sql6)
                                result=cursor.fetchall()
                                print(result)
                                x=result[0][0]
                                print(x)
                            except:
                                tkinter.messagebox.showwarning('警告', '该尸体未被出申请或移库')
                                return
                            if z==1:
                                sql4 = 'insert into a_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, x, now, int(s_id), p_name)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                                print(sql4)
                            else:
                                sql4 = 'insert into m_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, int(s_id), x, p_name, now)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                            print(x)
                            print(sql5)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            cursor.execute(sql7)
                            # 提交到数据库执行
                            db.commit()
                    elif p_name in result2[1]:
                        if z==1:
                            sql3 = "select max(id) from a_out"
                        else:
                            sql3='select max(id) from m_out'
                        try:
                            print(1)
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)
                        if z==1:
                            sql5 = 'select cor_id from a_out'
                        else:
                            sql5 = 'select cor_id from m_out'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        # print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被出库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            if z==1:
                                sql6='select id from apply where cor_id=%s'%(s_id)
                            else:
                                sql6='select id from move where cor_id=%s'%(s_id)
                            try:
                                cursor.execute(sql6)
                                result=cursor.fetchall()
                                print(result)
                                x=result[0][0]
                                print(x)
                            except:
                                tkinter.messagebox.showwarning('警告', '该尸体未被出申请或移库')
                                return
                            if z==1:
                                sql4 = 'insert into a_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, x, now, int(s_id), p_name)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                                print(sql4)
                            else:
                                sql4 = 'insert into m_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, int(s_id), x, p_name, now)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                            print(x)
                            print(sql5)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            cursor.execute(sql7)
                            # 提交到数据库执行
                            db.commit()
                    elif p_name in result2[2]:
                        if z==1:
                            sql3 = "select max(id) from a_out"
                        else:
                            sql3='select max(id) from m_out'
                        try:
                            print(1)
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)
                        if z==1:
                            sql5 = 'select cor_id from a_out'
                        else:
                            sql5 = 'select cor_id from m_out'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        # print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被出库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            if z==1:
                                sql6='select id from apply where cor_id=%s'%(s_id)
                            else:
                                sql6='select id from move where cor_id=%s'%(s_id)
                            try:
                                cursor.execute(sql6)
                                result=cursor.fetchall()
                                print(result)
                                x=result[0][0]
                                print(x)
                            except:
                                tkinter.messagebox.showwarning('警告', '该尸体未被出申请或移库')
                                return
                            if z==1:
                                sql4 = 'insert into a_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, x, now, int(s_id), p_name)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                                print(sql4)
                            else:
                                sql4 = 'insert into m_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, int(s_id), x, p_name, now)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                            print(x)
                            print(sql5)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            cursor.execute(sql7)
                            # 提交到数据库执行
                            db.commit()
                    elif p_name in result2[3]:
                        if z==1:
                            sql3 = "select max(id) from a_out"
                        else:
                            sql3='select max(id) from m_out'
                        try:
                            print(1)
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)
                        if z==1:
                            sql5 = 'select cor_id from a_out'
                        else:
                            sql5 = 'select cor_id from m_out'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        # print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被出库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            if z==1:
                                sql6='select id from apply where cor_id=%s'%(s_id)
                            else:
                                sql6='select id from move where cor_id=%s'%(s_id)
                            try:
                                cursor.execute(sql6)
                                result=cursor.fetchall()
                                print(result)
                                x=result[0][0]
                                print(x)
                            except:
                                tkinter.messagebox.showwarning('警告', '该尸体未被出申请或移库')
                                return
                            if z==1:
                                sql4 = 'insert into a_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, x, now, int(s_id), p_name)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                                print(sql4)
                            else:
                                sql4 = 'insert into m_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, int(s_id), x, p_name, now)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                            print(x)
                            print(sql5)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            cursor.execute(sql7)
                            # 提交到数据库执行
                            db.commit()




            def move():
                p_name = tt3.get(1.0, 1.5)
                oloc_id=tt4.get(1.0,1.5)
                nloc_id=tt5.get(1.0,1.5)
                sql = 'select name from cor where id=%s' % (s_id)
                # try:
                cursor.execute(sql)
                result = cursor.fetchone()
                if s_name in result:
                    # print('sbnb')
                    sql2 = 'select name from doc'
                    cursor.execute(sql2)
                    result2 = cursor.fetchall()
                    print(result2)
                    if p_name in result2[0]:
                        sql3 = "select max(id) from move"
                        try:
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)

                        sql5 = 'select cor_id from move'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被移库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            sql6='select id from tingshi.in where cor_id=%s'%(s_id)
                            cursor.execute(sql6)
                            result=cursor.fetchall()
                            x=result[0][0]
                            print(x)
                            sql4 = 'insert into move values' + ' (%d,%d,"%s","%s","%s","%s")' % (
                                i + 1, int(s_id), int(oloc_id), int(nloc_id), x, now)
                            sql5='update cor set location_id=%s where id=%s'%(int(nloc_id),s_id)
                            print(sql5)
                            sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                            sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                            print(sql4)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql6)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            # cursor.execute(sql7)
                            # 提交到数据库执行
                            # db.commit()
                    elif p_name in result2[1]:
                                sql3 = "select max(id) from move"
                                try:
                                    cursor.execute(sql3)
                                    result3 = cursor.fetchall()
                                    i = result3[0][0]
                                    if (i == None):
                                        i = 0
                                except:
                                    i = 0
                                print(type(s_id), type(tt4), type(tt5))
                                # print(type(s2), type(i), i, result3)

                                sql5 = 'select cor_id from move'
                                cursor.execute(sql5)
                                result4 = cursor.fetchall()
                                print(result4)
                                x = 0
                                while x <= len(result4):
                                    if (x == len(result4)):
                                        x += 1
                                    elif int(s_id) in result4[x]:
                                        print('yicunzai')
                                        tkinter.messagebox.showwarning('警告', '该尸体已被移库，请勿重复操作')
                                        break
                                    x += 1
                                    print(result4)

                                    # print(sql4)
                                    sql6 = 'select id from tingshi.in where cor_id=%s' % (s_id)
                                    cursor.execute(sql6)
                                    result = cursor.fetchall()
                                    x = result[0][0]
                                    print(x)
                                    sql4 = 'insert into move values' + ' (%d,%d,"%s","%s","%s","%s")' % (
                                        i + 1, int(s_id), int(oloc_id), int(nloc_id), x, now)
                                    sql5 = 'update cor set location_id=%s where id=%s' % (int(nloc_id), s_id)
                                    print(sql5)
                                    sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                    sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                                    print(sql4)
                                    try:
                                        # 执行sql语句
                                        cursor.execute(sql4)
                                        db.commit()
                                        cursor.execute(sql5)
                                        db.commit()
                                        cursor.execute(sql6)
                                        # 提交到数据库执行
                                        db.commit()

                                    except:
                                        # 发生错误时回滚
                                        print("sql wrong")
                                        db.rollback()
                                    # cursor.execute(sql5)
                                    # db.commit()
                                    cursor.execute(sql7)
                                    # 提交到数据库执行
                                    db.commit()
                    elif p_name in result2[2]:
                                sql3 = "select max(id) from move"
                                try:
                                    cursor.execute(sql3)
                                    result3 = cursor.fetchall()
                                    i = result3[0][0]
                                    if (i == None):
                                        i = 0
                                except:
                                    i = 0
                                print(type(s_id), type(tt4), type(tt5))
                                # print(type(s2), type(i), i, result3)

                                sql5 = 'select cor_id from move'
                                cursor.execute(sql5)
                                result4 = cursor.fetchall()
                                print(result4)
                                x = 0
                                while x <= len(result4):
                                    if (x == len(result4)):
                                        x += 1
                                    elif int(s_id) in result4[x]:
                                        print('yicunzai')
                                        tkinter.messagebox.showwarning('警告', '该尸体已被移库，请勿重复操作')
                                        break
                                    x += 1
                                    print(result4)

                                    # print(sql4)
                                    sql6 = 'select id from tingshi.in where cor_id=%s' % (s_id)
                                    cursor.execute(sql6)
                                    result = cursor.fetchall()
                                    x = result[0][0]
                                    print(x)
                                    sql4 = 'insert into move values' + ' (%d,%d,"%s","%s","%s","%s")' % (
                                        i + 1, int(s_id), int(oloc_id), int(nloc_id), x, now)
                                    sql5 = 'update cor set location_id=%s where id=%s' % (int(nloc_id), s_id)
                                    print(sql5)
                                    sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                    sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                                    print(sql4)
                                    try:
                                        # 执行sql语句
                                        cursor.execute(sql4)
                                        db.commit()
                                        cursor.execute(sql5)
                                        db.commit()
                                        cursor.execute(sql6)
                                        # 提交到数据库执行
                                        db.commit()

                                    except:
                                        # 发生错误时回滚
                                        print("sql wrong")
                                        db.rollback()
                                    # cursor.execute(sql5)
                                    # db.commit()
                                    cursor.execute(sql7)
                                    # 提交到数据库执行
                                    db.commit()
                    elif p_name in result2[3]:
                                sql3 = "select max(id) from move"
                                try:
                                    cursor.execute(sql3)
                                    result3 = cursor.fetchall()
                                    i = result3[0][0]
                                    if (i == None):
                                        i = 0
                                except:
                                    i = 0
                                print(type(s_id), type(tt4), type(tt5))
                                # print(type(s2), type(i), i, result3)

                                sql5 = 'select cor_id from move'
                                cursor.execute(sql5)
                                result4 = cursor.fetchall()
                                print(result4)
                                x = 0
                                while x <= len(result4):
                                    if (x == len(result4)):
                                        x += 1
                                    elif int(s_id) in result4[x]:
                                        print('yicunzai')
                                        tkinter.messagebox.showwarning('警告', '该尸体已被移库，请勿重复操作')
                                        break
                                    x += 1
                                    print(result4)

                                    # print(sql4)
                                    sql6 = 'select id from tingshi.in where cor_id=%s' % (s_id)
                                    cursor.execute(sql6)
                                    result = cursor.fetchall()
                                    x = result[0][0]
                                    print(x)
                                    sql4 = 'insert into move values' + ' (%d,%d,"%s","%s","%s","%s")' % (
                                        i + 1, int(s_id), int(oloc_id), int(nloc_id), x, now)
                                    sql5 = 'update cor set location_id=%s where id=%s' % (int(nloc_id), s_id)
                                    print(sql5)
                                    sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                    sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                                    print(sql4)
                                    try:
                                        # 执行sql语句
                                        cursor.execute(sql4)
                                        db.commit()
                                        cursor.execute(sql5)
                                        db.commit()
                                        cursor.execute(sql6)
                                        # 提交到数据库执行
                                        db.commit()

                                    except:
                                        # 发生错误时回滚
                                        print("sql wrong")
                                        db.rollback()
                                    # cursor.execute(sql5)
                                    # db.commit()
                                    cursor.execute(sql7)
                                    # 提交到数据库执行
                                    db.commit()
                    else:
                        tkinter.messagebox.showwarning('警告', '你不是医生你是谁')
                else:
                    tkinter.messagebox.showwarning('警告', '该尸体不存在或已出库')
            if len(indexs) == 0:
                return
            bt = tk.Button(tc, text='移库', command=move)
            bt.grid(row=5, column=0)
            bt = tk.Button(tc, text='申请出库', command=lambda :out(1))
            bt.grid(row=5, column=1)
            bt = tk.Button(tc, text='强制出库', command=lambda:out(2))
            bt.grid(row=5, column=2)
            bt = tk.Button(tc, text='返回', command=tc.destroy)
            bt.grid(row=5, column=3)
        while j < 48:
            lb3.insert(result[j][0], result[j][0])
            lb1.insert(result[j][0], result[j][1])
            lb2.insert(result[j][0], result[j][2])
            lb4.insert(result[j][0], result[j][3])
            j += 1
        lb3.bind("<<ListboxSelect>>", show_msg)
        while j < 72:
            lb3.insert(result[j][0], result[j][0])
            lb1.insert(result[j][0], result[j][1])
            lb2.insert(result[j][0], result[j][2])
            lb4.insert(result[j][0], result[j][3])
            # a_j.pack()
            # # self.j.grid(column=0)
            # a_j.insert( '尸体名:%s，家属:%s' % (result[j][0], result[j][1]),chars=100)
            j += 1
    fenye1()#three
    frame6 = tk.Frame(window, height=350, bg="yellow")
    def fenye2():
        sql = 'select id,name,company,location_id from cor'
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            # j = 0
            print(result)

        except:
            tk.messagebox.showwarning('警告', '请不要乱查询')
        # self.te=Label(frma,width=50,height=5)
        # self.te.grid(frma,row=10,column=10)
        # btnSend = Button(tc.frma, text='发 送', width=8)  # 在frmLB容器中添加
        # btnSend.grid(row=2, column=0)
        # btnCancel = Button(tc.frma, text='取消', width=8)
        # btnCancel.grid(row=2, column=1, sticky=E)
        lb3 = tk.Listbox(frame6, selectmode='BROWSE', height=len(result))
        lb3.pack(side='left', fill='both')
        lb1 = tk.Listbox(frame6, selectmode='extended', height=len(result))
        lb1.pack(side='left', fill='both')
        lb2 = tk.Listbox(frame6, selectmode='extended', height=len(result))
        lb2.pack(side='left', fill='both')
        lb4 = tk.Listbox(frame6, selectmode='extended', height=len(result))
        lb4.pack(side='left', fill='both')
        lb4.insert(0, '货位编号')
        lb3.insert(0, '尸体编号')
        lb1.insert(0, '尸体姓名')
        lb2.insert(0, '存放单位')
        j = 73
        def show_msg(*args):

            indexs = lb3.curselection()
            id = int(indexs[0])
            s_id=lb3.get(id)
            s_name=lb1.get(indexs[0])
            s_id2=lb4.get(id)
            s_company=lb2.get(id)
            # print(s_id,s_name,s_id2,s_company)
            tc=tk.Tk()
            tc.title('单据填写')
            lab1 = tk.Label(tc, text="尸体id")
            lab1.grid(row=0, column=0,)
            lab2 = tk.Label(tc, text="尸体名称")
            lab2.grid(row=1, column=0)
            lab3 = tk.Label(tc, text="操作人姓名")
            lab3.grid(row=2, column=0)
            lab4 = tk.Label(tc, text="老货位编号")
            lab4.grid(row=3, column=0)
            lab5= tk.Label(tc, text="新货位编号")
            lab5.grid(row=4, column=0)
            tt1= tk.Text(tc,width=10,height=1)
            tt1.grid(row=0, column=1)
            tt1.insert(tk.INSERT,s_id)
            tt2 = tk.Text(tc, width=10, height=1)
            tt2.grid(row=1, column=1)
            tt2.insert(tk.INSERT, s_name)
            tt3 = tk.Text(tc, width=10, height=1)
            tt3.grid(row=2, column=1)
            tt3.insert(tk.INSERT,'请在此输入')
            tt4 = tk.Text(tc, width=10, height=1)
            tt4.grid(row=3, column=1)
            tt4.insert(tk.INSERT, s_id2)
            tt5 = tk.Text(tc, width=10, height=1)
            tt5.grid(row=4, column=1)
            tt5.insert(tk.INSERT, '请在此输入')


            def out(z):
                p_name = tt3.get(1.0, 1.5)
                oloc_id=tt4.get(1.0,1.5)
                nloc_id=tt5.get(1.0,1.5)
                sql = 'select name from cor where id=%s' % (s_id)
                # try:
                cursor.execute(sql)
                result = cursor.fetchone()
                if s_name in result:
                    # print('sbnb')
                    sql2 = 'select name from doc'
                    cursor.execute(sql2)
                    result2 = cursor.fetchall()


                    if p_name in result2[0]:
                        if z==1:
                            sql3 = "select max(id) from a_out"
                        else:
                            sql3='select max(id) from m_out'
                        try:
                            print(1)
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)
                        if z==1:
                            sql5 = 'select cor_id from a_out'
                        else:
                            sql5 = 'select cor_id from m_out'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        # print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被出库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            if z==1:
                                sql6='select id from apply where cor_id=%s'%(s_id)
                            else:
                                sql6='select id from move where cor_id=%s'%(s_id)
                            try:
                                cursor.execute(sql6)
                                result=cursor.fetchall()
                                print(result)
                                x=result[0][0]
                                print(x)
                            except:
                                tkinter.messagebox.showwarning('警告', '该尸体未被出申请或移库')
                                return
                            if z==1:
                                sql4 = 'insert into a_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, x, now, int(s_id), p_name)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                                print(sql4)
                            else:
                                sql4 = 'insert into m_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, int(s_id), x, p_name, now)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                            print(x)
                            print(sql5)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            cursor.execute(sql7)
                            # 提交到数据库执行
                            db.commit()
                    elif p_name in result2[1]:
                        if z==1:
                            sql3 = "select max(id) from a_out"
                        else:
                            sql3='select max(id) from m_out'
                        try:
                            print(1)
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)
                        if z==1:
                            sql5 = 'select cor_id from a_out'
                        else:
                            sql5 = 'select cor_id from m_out'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        # print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被出库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            if z==1:
                                sql6='select id from apply where cor_id=%s'%(s_id)
                            else:
                                sql6='select id from move where cor_id=%s'%(s_id)
                            try:
                                cursor.execute(sql6)
                                result=cursor.fetchall()
                                print(result)
                                x=result[0][0]
                                print(x)
                            except:
                                tkinter.messagebox.showwarning('警告', '该尸体未被出申请或移库')
                                return
                            if z==1:
                                sql4 = 'insert into a_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, x, now, int(s_id), p_name)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                                print(sql4)
                            else:
                                sql4 = 'insert into m_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, int(s_id), x, p_name, now)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                            print(x)
                            print(sql5)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            cursor.execute(sql7)
                            # 提交到数据库执行
                            db.commit()
                    elif p_name in result2[2]:
                        if z==1:
                            sql3 = "select max(id) from a_out"
                        else:
                            sql3='select max(id) from m_out'
                        try:
                            print(1)
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)
                        if z==1:
                            sql5 = 'select cor_id from a_out'
                        else:
                            sql5 = 'select cor_id from m_out'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        # print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被出库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            if z==1:
                                sql6='select id from apply where cor_id=%s'%(s_id)
                            else:
                                sql6='select id from move where cor_id=%s'%(s_id)
                            try:
                                cursor.execute(sql6)
                                result=cursor.fetchall()
                                print(result)
                                x=result[0][0]
                                print(x)
                            except:
                                tkinter.messagebox.showwarning('警告', '该尸体未被出申请或移库')
                                return
                            if z==1:
                                sql4 = 'insert into a_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, x, now, int(s_id), p_name)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                                print(sql4)
                            else:
                                sql4 = 'insert into m_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, int(s_id), x, p_name, now)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                            print(x)
                            print(sql5)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            cursor.execute(sql7)
                            # 提交到数据库执行
                            db.commit()
                    elif p_name in result2[3]:
                        if z==1:
                            sql3 = "select max(id) from a_out"
                        else:
                            sql3='select max(id) from m_out'
                        try:
                            print(1)
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)
                        if z==1:
                            sql5 = 'select cor_id from a_out'
                        else:
                            sql5 = 'select cor_id from m_out'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        # print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被出库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            if z==1:
                                sql6='select id from apply where cor_id=%s'%(s_id)
                            else:
                                sql6='select id from move where cor_id=%s'%(s_id)
                            try:
                                cursor.execute(sql6)
                                result=cursor.fetchall()
                                print(result)
                                x=result[0][0]
                                print(x)
                            except:
                                tkinter.messagebox.showwarning('警告', '该尸体未被出申请或移库')
                                return
                            if z==1:
                                sql4 = 'insert into a_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, x, now, int(s_id), p_name)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                                print(sql4)
                            else:
                                sql4 = 'insert into m_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, int(s_id), x, p_name, now)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                            print(x)
                            print(sql5)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            cursor.execute(sql7)
                            # 提交到数据库执行
                            db.commit()




            def move():
                p_name = tt3.get(1.0, 1.5)
                oloc_id=tt4.get(1.0,1.5)
                nloc_id=tt5.get(1.0,1.5)
                sql = 'select name from cor where id=%s' % (s_id)
                # try:
                cursor.execute(sql)
                result = cursor.fetchone()
                if s_name in result:
                    # print('sbnb')
                    sql2 = 'select name from doc'
                    cursor.execute(sql2)
                    result2 = cursor.fetchall()
                    print(result2)
                    if p_name in result2[0]:
                        sql3 = "select max(id) from move"
                        try:
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)

                        sql5 = 'select cor_id from move'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被移库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            sql6='select id from tingshi.in where cor_id=%s'%(s_id)
                            cursor.execute(sql6)
                            result=cursor.fetchall()
                            x=result[0][0]
                            print(x)
                            sql4 = 'insert into move values' + ' (%d,%d,"%s","%s","%s","%s")' % (
                                i + 1, int(s_id), int(oloc_id), int(nloc_id), x, now)
                            sql5='update cor set location_id=%s where id=%s'%(int(nloc_id),s_id)
                            print(sql5)
                            sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                            sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                            print(sql4)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql6)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            # cursor.execute(sql7)
                            # 提交到数据库执行
                            # db.commit()
                    elif p_name in result2[1]:
                                sql3 = "select max(id) from move"
                                try:
                                    cursor.execute(sql3)
                                    result3 = cursor.fetchall()
                                    i = result3[0][0]
                                    if (i == None):
                                        i = 0
                                except:
                                    i = 0
                                print(type(s_id), type(tt4), type(tt5))
                                # print(type(s2), type(i), i, result3)

                                sql5 = 'select cor_id from move'
                                cursor.execute(sql5)
                                result4 = cursor.fetchall()
                                print(result4)
                                x = 0
                                while x <= len(result4):
                                    if (x == len(result4)):
                                        x += 1
                                    elif int(s_id) in result4[x]:
                                        print('yicunzai')
                                        tkinter.messagebox.showwarning('警告', '该尸体已被移库，请勿重复操作')
                                        break
                                    x += 1
                                    print(result4)

                                    # print(sql4)
                                    sql6 = 'select id from tingshi.in where cor_id=%s' % (s_id)
                                    cursor.execute(sql6)
                                    result = cursor.fetchall()
                                    x = result[0][0]
                                    print(x)
                                    sql4 = 'insert into move values' + ' (%d,%d,"%s","%s","%s","%s")' % (
                                        i + 1, int(s_id), int(oloc_id), int(nloc_id), x, now)
                                    sql5 = 'update cor set location_id=%s where id=%s' % (int(nloc_id), s_id)
                                    print(sql5)
                                    sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                    sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                                    print(sql4)
                                    try:
                                        # 执行sql语句
                                        cursor.execute(sql4)
                                        db.commit()
                                        cursor.execute(sql5)
                                        db.commit()
                                        cursor.execute(sql6)
                                        # 提交到数据库执行
                                        db.commit()

                                    except:
                                        # 发生错误时回滚
                                        print("sql wrong")
                                        db.rollback()
                                    # cursor.execute(sql5)
                                    # db.commit()
                                    cursor.execute(sql7)
                                    # 提交到数据库执行
                                    db.commit()
                    elif p_name in result2[2]:
                                sql3 = "select max(id) from move"
                                try:
                                    cursor.execute(sql3)
                                    result3 = cursor.fetchall()
                                    i = result3[0][0]
                                    if (i == None):
                                        i = 0
                                except:
                                    i = 0
                                print(type(s_id), type(tt4), type(tt5))
                                # print(type(s2), type(i), i, result3)

                                sql5 = 'select cor_id from move'
                                cursor.execute(sql5)
                                result4 = cursor.fetchall()
                                print(result4)
                                x = 0
                                while x <= len(result4):
                                    if (x == len(result4)):
                                        x += 1
                                    elif int(s_id) in result4[x]:
                                        print('yicunzai')
                                        tkinter.messagebox.showwarning('警告', '该尸体已被移库，请勿重复操作')
                                        break
                                    x += 1
                                    print(result4)

                                    # print(sql4)
                                    sql6 = 'select id from tingshi.in where cor_id=%s' % (s_id)
                                    cursor.execute(sql6)
                                    result = cursor.fetchall()
                                    x = result[0][0]
                                    print(x)
                                    sql4 = 'insert into move values' + ' (%d,%d,"%s","%s","%s","%s")' % (
                                        i + 1, int(s_id), int(oloc_id), int(nloc_id), x, now)
                                    sql5 = 'update cor set location_id=%s where id=%s' % (int(nloc_id), s_id)
                                    print(sql5)
                                    sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                    sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                                    print(sql4)
                                    try:
                                        # 执行sql语句
                                        cursor.execute(sql4)
                                        db.commit()
                                        cursor.execute(sql5)
                                        db.commit()
                                        cursor.execute(sql6)
                                        # 提交到数据库执行
                                        db.commit()

                                    except:
                                        # 发生错误时回滚
                                        print("sql wrong")
                                        db.rollback()
                                    # cursor.execute(sql5)
                                    # db.commit()
                                    cursor.execute(sql7)
                                    # 提交到数据库执行
                                    db.commit()
                    elif p_name in result2[3]:
                                sql3 = "select max(id) from move"
                                try:
                                    cursor.execute(sql3)
                                    result3 = cursor.fetchall()
                                    i = result3[0][0]
                                    if (i == None):
                                        i = 0
                                except:
                                    i = 0
                                print(type(s_id), type(tt4), type(tt5))
                                # print(type(s2), type(i), i, result3)

                                sql5 = 'select cor_id from move'
                                cursor.execute(sql5)
                                result4 = cursor.fetchall()
                                print(result4)
                                x = 0
                                while x <= len(result4):
                                    if (x == len(result4)):
                                        x += 1
                                    elif int(s_id) in result4[x]:
                                        print('yicunzai')
                                        tkinter.messagebox.showwarning('警告', '该尸体已被移库，请勿重复操作')
                                        break
                                    x += 1
                                    print(result4)

                                    # print(sql4)
                                    sql6 = 'select id from tingshi.in where cor_id=%s' % (s_id)
                                    cursor.execute(sql6)
                                    result = cursor.fetchall()
                                    x = result[0][0]
                                    print(x)
                                    sql4 = 'insert into move values' + ' (%d,%d,"%s","%s","%s","%s")' % (
                                        i + 1, int(s_id), int(oloc_id), int(nloc_id), x, now)
                                    sql5 = 'update cor set location_id=%s where id=%s' % (int(nloc_id), s_id)
                                    print(sql5)
                                    sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                    sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                                    print(sql4)
                                    try:
                                        # 执行sql语句
                                        cursor.execute(sql4)
                                        db.commit()
                                        cursor.execute(sql5)
                                        db.commit()
                                        cursor.execute(sql6)
                                        # 提交到数据库执行
                                        db.commit()

                                    except:
                                        # 发生错误时回滚
                                        print("sql wrong")
                                        db.rollback()
                                    # cursor.execute(sql5)
                                    # db.commit()
                                    cursor.execute(sql7)
                                    # 提交到数据库执行
                                    db.commit()
                    else:
                        tkinter.messagebox.showwarning('警告', '你不是医生你是谁')
                else:
                    tkinter.messagebox.showwarning('警告', '该尸体不存在或已出库')
            if len(indexs) == 0:
                return
            bt = tk.Button(tc, text='移库', command=move)
            bt.grid(row=5, column=0)
            bt = tk.Button(tc, text='申请出库', command=lambda :out(1))
            bt.grid(row=5, column=1)
            bt = tk.Button(tc, text='强制出库', command=lambda:out(2))
            bt.grid(row=5, column=2)
            bt = tk.Button(tc, text='返回', command=tc.destroy)
            bt.grid(row=5, column=3)
        while j < 48:
            lb3.insert(result[j][0], result[j][0])
            lb1.insert(result[j][0], result[j][1])
            lb2.insert(result[j][0], result[j][2])
            lb4.insert(result[j][0], result[j][3])
            j += 1
        lb3.bind("<<ListboxSelect>>", show_msg)
        while j < 96:
            lb3.insert(result[j][0], result[j][0])
            lb1.insert(result[j][0], result[j][1])
            lb2.insert(result[j][0], result[j][2])
            lb4.insert(result[j][0], result[j][3])
            # a_j.pack()
            # # self.j.grid(column=0)
            # a_j.insert( '尸体名:%s，家属:%s' % (result[j][0], result[j][1]),chars=100)
            j += 1
    fenye2()#four
    frame7 = tk.Frame(window, height=350, bg="yellow")
    def fenye3():
        sql = 'select id,name,company,location_id from cor order by location_id'
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            # j = 0
            print(result)

        except:
            tk.messagebox.showwarning('警告', '请不要乱查询')
        lb3 = tk.Listbox(frame7, selectmode='BROWSE', height=len(result))
        lb3.pack(side='left', fill='both')
        lb1 = tk.Listbox(frame7, selectmode='extended', height=len(result))
        lb1.pack(side='left', fill='both')
        lb2 = tk.Listbox(frame7, selectmode='extended', height=len(result))
        lb2.pack(side='left', fill='both')
        lb4 = tk.Listbox(frame7, selectmode='extended', height=len(result))
        lb4.pack(side='left', fill='both')
        lb4.insert(0, '货位编号')
        lb3.insert(0, '尸体编号')
        lb1.insert(0, '尸体姓名')
        lb2.insert(0, '存放单位')
        j = 97
        def show_msg(*args):

            indexs = lb3.curselection()
            id = int(indexs[0])
            s_id=lb3.get(id)
            s_name=lb1.get(indexs[0])
            s_id2=lb4.get(id)
            s_company=lb2.get(id)
            # print(s_id,s_name,s_id2,s_company)
            tc=tk.Tk()
            tc.title('单据填写')
            lab1 = tk.Label(tc, text="尸体id")
            lab1.grid(row=0, column=0,)
            lab2 = tk.Label(tc, text="尸体名称")
            lab2.grid(row=1, column=0)
            lab3 = tk.Label(tc, text="操作人姓名")
            lab3.grid(row=2, column=0)
            lab4 = tk.Label(tc, text="老货位编号")
            lab4.grid(row=3, column=0)
            lab5= tk.Label(tc, text="新货位编号")
            lab5.grid(row=4, column=0)
            tt1= tk.Text(tc,width=10,height=1)
            tt1.grid(row=0, column=1)
            tt1.insert(tk.INSERT,s_id)
            tt2 = tk.Text(tc, width=10, height=1)
            tt2.grid(row=1, column=1)
            tt2.insert(tk.INSERT, s_name)
            tt3 = tk.Text(tc, width=10, height=1)
            tt3.grid(row=2, column=1)
            tt3.insert(tk.INSERT,'请在此输入')
            tt4 = tk.Text(tc, width=10, height=1)
            tt4.grid(row=3, column=1)
            tt4.insert(tk.INSERT, s_id2)
            tt5 = tk.Text(tc, width=10, height=1)
            tt5.grid(row=4, column=1)
            tt5.insert(tk.INSERT, '请在此输入')


            def out(z):
                p_name = tt3.get(1.0, 1.5)
                oloc_id=tt4.get(1.0,1.5)
                nloc_id=tt5.get(1.0,1.5)
                sql = 'select name from cor where id=%s' % (s_id)
                # try:
                cursor.execute(sql)
                result = cursor.fetchone()
                if s_name in result:
                    # print('sbnb')
                    sql2 = 'select name from doc'
                    cursor.execute(sql2)
                    result2 = cursor.fetchall()


                    if p_name in result2[0]:
                        if z==1:
                            sql3 = "select max(id) from a_out"
                        else:
                            sql3='select max(id) from m_out'
                        try:
                            print(1)
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)
                        if z==1:
                            sql5 = 'select cor_id from a_out'
                        else:
                            sql5 = 'select cor_id from m_out'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        # print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被出库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            if z==1:
                                sql6='select id from apply where cor_id=%s'%(s_id)
                            else:
                                sql6='select id from move where cor_id=%s'%(s_id)
                            try:
                                cursor.execute(sql6)
                                result=cursor.fetchall()
                                print(result)
                                x=result[0][0]
                                print(x)
                            except:
                                tkinter.messagebox.showwarning('警告', '该尸体未被出申请或移库')
                                return
                            if z==1:
                                sql4 = 'insert into a_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, x, now, int(s_id), p_name)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                                print(sql4)
                            else:
                                sql4 = 'insert into m_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, int(s_id), x, p_name, now)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                            print(x)
                            print(sql5)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            cursor.execute(sql7)
                            # 提交到数据库执行
                            db.commit()
                    elif p_name in result2[1]:
                        if z==1:
                            sql3 = "select max(id) from a_out"
                        else:
                            sql3='select max(id) from m_out'
                        try:
                            print(1)
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)
                        if z==1:
                            sql5 = 'select cor_id from a_out'
                        else:
                            sql5 = 'select cor_id from m_out'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        # print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被出库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            if z==1:
                                sql6='select id from apply where cor_id=%s'%(s_id)
                            else:
                                sql6='select id from move where cor_id=%s'%(s_id)
                            try:
                                cursor.execute(sql6)
                                result=cursor.fetchall()
                                print(result)
                                x=result[0][0]
                                print(x)
                            except:
                                tkinter.messagebox.showwarning('警告', '该尸体未被出申请或移库')
                                return
                            if z==1:
                                sql4 = 'insert into a_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, x, now, int(s_id), p_name)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                                print(sql4)
                            else:
                                sql4 = 'insert into m_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, int(s_id), x, p_name, now)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                            print(x)
                            print(sql5)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            cursor.execute(sql7)
                            # 提交到数据库执行
                            db.commit()
                    elif p_name in result2[2]:
                        if z==1:
                            sql3 = "select max(id) from a_out"
                        else:
                            sql3='select max(id) from m_out'
                        try:
                            print(1)
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)
                        if z==1:
                            sql5 = 'select cor_id from a_out'
                        else:
                            sql5 = 'select cor_id from m_out'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        # print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被出库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            if z==1:
                                sql6='select id from apply where cor_id=%s'%(s_id)
                            else:
                                sql6='select id from move where cor_id=%s'%(s_id)
                            try:
                                cursor.execute(sql6)
                                result=cursor.fetchall()
                                print(result)
                                x=result[0][0]
                                print(x)
                            except:
                                tkinter.messagebox.showwarning('警告', '该尸体未被出申请或移库')
                                return
                            if z==1:
                                sql4 = 'insert into a_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, x, now, int(s_id), p_name)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                                print(sql4)
                            else:
                                sql4 = 'insert into m_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, int(s_id), x, p_name, now)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                            print(x)
                            print(sql5)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            cursor.execute(sql7)
                            # 提交到数据库执行
                            db.commit()
                    elif p_name in result2[3]:
                        if z==1:
                            sql3 = "select max(id) from a_out"
                        else:
                            sql3='select max(id) from m_out'
                        try:
                            print(1)
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)
                        if z==1:
                            sql5 = 'select cor_id from a_out'
                        else:
                            sql5 = 'select cor_id from m_out'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        # print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被出库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            if z==1:
                                sql6='select id from apply where cor_id=%s'%(s_id)
                            else:
                                sql6='select id from move where cor_id=%s'%(s_id)
                            try:
                                cursor.execute(sql6)
                                result=cursor.fetchall()
                                print(result)
                                x=result[0][0]
                                print(x)
                            except:
                                tkinter.messagebox.showwarning('警告', '该尸体未被出申请或移库')
                                return
                            if z==1:
                                sql4 = 'insert into a_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, x, now, int(s_id), p_name)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                                print(sql4)
                            else:
                                sql4 = 'insert into m_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, int(s_id), x, p_name, now)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                            print(x)
                            print(sql5)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            cursor.execute(sql7)
                            # 提交到数据库执行
                            db.commit()




            def move():
                p_name = tt3.get(1.0, 1.5)
                oloc_id=tt4.get(1.0,1.5)
                nloc_id=tt5.get(1.0,1.5)
                sql = 'select name from cor where id=%s' % (s_id)
                # try:
                cursor.execute(sql)
                result = cursor.fetchone()
                if s_name in result:
                    # print('sbnb')
                    sql2 = 'select name from doc'
                    cursor.execute(sql2)
                    result2 = cursor.fetchall()
                    print(result2)
                    if p_name in result2[0]:
                        sql3 = "select max(id) from move"
                        try:
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)

                        sql5 = 'select cor_id from move'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被移库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            sql6='select id from tingshi.in where cor_id=%s'%(s_id)
                            cursor.execute(sql6)
                            result=cursor.fetchall()
                            x=result[0][0]
                            print(x)
                            sql4 = 'insert into move values' + ' (%d,%d,"%s","%s","%s","%s")' % (
                                i + 1, int(s_id), int(oloc_id), int(nloc_id), x, now)
                            sql5='update cor set location_id=%s where id=%s'%(int(nloc_id),s_id)
                            print(sql5)
                            sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                            sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                            print(sql4)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql6)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            # cursor.execute(sql7)
                            # 提交到数据库执行
                            # db.commit()
                    elif p_name in result2[1]:
                                sql3 = "select max(id) from move"
                                try:
                                    cursor.execute(sql3)
                                    result3 = cursor.fetchall()
                                    i = result3[0][0]
                                    if (i == None):
                                        i = 0
                                except:
                                    i = 0
                                print(type(s_id), type(tt4), type(tt5))
                                # print(type(s2), type(i), i, result3)

                                sql5 = 'select cor_id from move'
                                cursor.execute(sql5)
                                result4 = cursor.fetchall()
                                print(result4)
                                x = 0
                                while x <= len(result4):
                                    if (x == len(result4)):
                                        x += 1
                                    elif int(s_id) in result4[x]:
                                        print('yicunzai')
                                        tkinter.messagebox.showwarning('警告', '该尸体已被移库，请勿重复操作')
                                        break
                                    x += 1
                                    print(result4)

                                    # print(sql4)
                                    sql6 = 'select id from tingshi.in where cor_id=%s' % (s_id)
                                    cursor.execute(sql6)
                                    result = cursor.fetchall()
                                    x = result[0][0]
                                    print(x)
                                    sql4 = 'insert into move values' + ' (%d,%d,"%s","%s","%s","%s")' % (
                                        i + 1, int(s_id), int(oloc_id), int(nloc_id), x, now)
                                    sql5 = 'update cor set location_id=%s where id=%s' % (int(nloc_id), s_id)
                                    print(sql5)
                                    sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                    sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                                    print(sql4)
                                    try:
                                        # 执行sql语句
                                        cursor.execute(sql4)
                                        db.commit()
                                        cursor.execute(sql5)
                                        db.commit()
                                        cursor.execute(sql6)
                                        # 提交到数据库执行
                                        db.commit()

                                    except:
                                        # 发生错误时回滚
                                        print("sql wrong")
                                        db.rollback()
                                    # cursor.execute(sql5)
                                    # db.commit()
                                    cursor.execute(sql7)
                                    # 提交到数据库执行
                                    db.commit()
                    elif p_name in result2[2]:
                                sql3 = "select max(id) from move"
                                try:
                                    cursor.execute(sql3)
                                    result3 = cursor.fetchall()
                                    i = result3[0][0]
                                    if (i == None):
                                        i = 0
                                except:
                                    i = 0
                                print(type(s_id), type(tt4), type(tt5))
                                # print(type(s2), type(i), i, result3)

                                sql5 = 'select cor_id from move'
                                cursor.execute(sql5)
                                result4 = cursor.fetchall()
                                print(result4)
                                x = 0
                                while x <= len(result4):
                                    if (x == len(result4)):
                                        x += 1
                                    elif int(s_id) in result4[x]:
                                        print('yicunzai')
                                        tkinter.messagebox.showwarning('警告', '该尸体已被移库，请勿重复操作')
                                        break
                                    x += 1
                                    print(result4)

                                    # print(sql4)
                                    sql6 = 'select id from tingshi.in where cor_id=%s' % (s_id)
                                    cursor.execute(sql6)
                                    result = cursor.fetchall()
                                    x = result[0][0]
                                    print(x)
                                    sql4 = 'insert into move values' + ' (%d,%d,"%s","%s","%s","%s")' % (
                                        i + 1, int(s_id), int(oloc_id), int(nloc_id), x, now)
                                    sql5 = 'update cor set location_id=%s where id=%s' % (int(nloc_id), s_id)
                                    print(sql5)
                                    sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                    sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                                    print(sql4)
                                    try:
                                        # 执行sql语句
                                        cursor.execute(sql4)
                                        db.commit()
                                        cursor.execute(sql5)
                                        db.commit()
                                        cursor.execute(sql6)
                                        # 提交到数据库执行
                                        db.commit()

                                    except:
                                        # 发生错误时回滚
                                        print("sql wrong")
                                        db.rollback()
                                    # cursor.execute(sql5)
                                    # db.commit()
                                    cursor.execute(sql7)
                                    # 提交到数据库执行
                                    db.commit()
                    elif p_name in result2[3]:
                                sql3 = "select max(id) from move"
                                try:
                                    cursor.execute(sql3)
                                    result3 = cursor.fetchall()
                                    i = result3[0][0]
                                    if (i == None):
                                        i = 0
                                except:
                                    i = 0
                                print(type(s_id), type(tt4), type(tt5))
                                # print(type(s2), type(i), i, result3)

                                sql5 = 'select cor_id from move'
                                cursor.execute(sql5)
                                result4 = cursor.fetchall()
                                print(result4)
                                x = 0
                                while x <= len(result4):
                                    if (x == len(result4)):
                                        x += 1
                                    elif int(s_id) in result4[x]:
                                        print('yicunzai')
                                        tkinter.messagebox.showwarning('警告', '该尸体已被移库，请勿重复操作')
                                        break
                                    x += 1
                                    print(result4)

                                    # print(sql4)
                                    sql6 = 'select id from tingshi.in where cor_id=%s' % (s_id)
                                    cursor.execute(sql6)
                                    result = cursor.fetchall()
                                    x = result[0][0]
                                    print(x)
                                    sql4 = 'insert into move values' + ' (%d,%d,"%s","%s","%s","%s")' % (
                                        i + 1, int(s_id), int(oloc_id), int(nloc_id), x, now)
                                    sql5 = 'update cor set location_id=%s where id=%s' % (int(nloc_id), s_id)
                                    print(sql5)
                                    sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                    sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                                    print(sql4)
                                    try:
                                        # 执行sql语句
                                        cursor.execute(sql4)
                                        db.commit()
                                        cursor.execute(sql5)
                                        db.commit()
                                        cursor.execute(sql6)
                                        # 提交到数据库执行
                                        db.commit()

                                    except:
                                        # 发生错误时回滚
                                        print("sql wrong")
                                        db.rollback()
                                    # cursor.execute(sql5)
                                    # db.commit()
                                    cursor.execute(sql7)
                                    # 提交到数据库执行
                                    db.commit()
                    else:
                        tkinter.messagebox.showwarning('警告', '你不是医生你是谁')
                else:
                    tkinter.messagebox.showwarning('警告', '该尸体不存在或已出库')
            if len(indexs) == 0:
                return
            bt = tk.Button(tc, text='移库', command=move)
            bt.grid(row=5, column=0)
            bt = tk.Button(tc, text='申请出库', command=lambda :out(1))
            bt.grid(row=5, column=1)
            bt = tk.Button(tc, text='强制出库', command=lambda:out(2))
            bt.grid(row=5, column=2)
            bt = tk.Button(tc, text='返回', command=tc.destroy)
            bt.grid(row=5, column=3)

        lb3.bind("<<ListboxSelect>>", show_msg)
        while j < len(result):
            lb3.insert(result[j][0], result[j][0])
            lb1.insert(result[j][0], result[j][1])
            lb2.insert(result[j][0], result[j][2])
            lb4.insert(result[j][0], result[j][3])
            j += 1

    fenye3()#five

    frame3 = tk.Frame(window, height=350, bg="yellow")
    frame3.pack(side=tk.TOP, fill=tk.X)
    def fenye4():

        sql = 'select id,name,company,location_id from cor'
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            # j = 0
            print(result)

        except:
            tk.messagebox.showwarning('警告', '请不要乱查询')
        # self.te=Label(frma,width=50,height=5)
        # self.te.grid(frma,row=10,column=10)
        # btnSend = Button(tc.frma, text='发 送', width=8)  # 在frmLB容器中添加
        # btnSend.grid(row=2, column=0)
        # btnCancel = Button(tc.frma, text='取消', width=8)
        # btnCancel.grid(row=2, column=1, sticky=E)
        lb3 = tk.Listbox(frame3, selectmode='BROWSE',height=len(result))
        lb3.pack(side='left', fill='both')
        lb1 = tk.Listbox(frame3, selectmode='extended',height=len(result))
        lb1.pack(side='left', fill='both')
        lb2 = tk.Listbox(frame3, selectmode='extended', height=len(result))
        lb2.pack(side='left', fill='both')
        lb4 = tk.Listbox(frame3, selectmode='extended', height=len(result))
        lb4.pack(side='left', fill='both')
        lb4.insert(0, '货位编号')
        lb3.insert(0, '尸体编号')
        lb1.insert(0, '尸体姓名')
        lb2.insert(0, '存放单位')
        j = 0

        def show_msg(*args):

            indexs = lb3.curselection()
            id = int(indexs[0])
            s_id=lb3.get(id)
            s_name=lb1.get(indexs[0])
            s_id2=lb4.get(id)
            s_company=lb2.get(id)
            # print(s_id,s_name,s_id2,s_company)
            tc=tk.Tk()
            tc.title('单据填写')
            lab1 = tk.Label(tc, text="尸体id")
            lab1.grid(row=0, column=0,)
            lab2 = tk.Label(tc, text="尸体名称")
            lab2.grid(row=1, column=0)
            lab3 = tk.Label(tc, text="操作人姓名")
            lab3.grid(row=2, column=0)
            lab4 = tk.Label(tc, text="老货位编号")
            lab4.grid(row=3, column=0)
            lab5= tk.Label(tc, text="新货位编号")
            lab5.grid(row=4, column=0)
            tt1= tk.Text(tc,width=10,height=1)
            tt1.grid(row=0, column=1)
            tt1.insert(tk.INSERT,s_id)
            tt2 = tk.Text(tc, width=10, height=1)
            tt2.grid(row=1, column=1)
            tt2.insert(tk.INSERT, s_name)
            tt3 = tk.Text(tc, width=10, height=1)
            tt3.grid(row=2, column=1)
            tt3.insert(tk.INSERT,'请在此输入')
            tt4 = tk.Text(tc, width=10, height=1)
            tt4.grid(row=3, column=1)
            tt4.insert(tk.INSERT, s_id2)
            tt5 = tk.Text(tc, width=10, height=1)
            tt5.grid(row=4, column=1)
            tt5.insert(tk.INSERT, '请在此输入')


            def out(z):
                p_name = tt3.get(1.0, 1.5)
                oloc_id=tt4.get(1.0,1.5)
                nloc_id=tt5.get(1.0,1.5)
                sql = 'select name from cor where id=%s' % (s_id)
                # try:
                cursor.execute(sql)
                result = cursor.fetchone()
                if s_name in result:
                    # print('sbnb')
                    sql2 = 'select name from doc'
                    cursor.execute(sql2)
                    result2 = cursor.fetchall()


                    if p_name in result2[0]:
                        if z==1:
                            sql3 = "select max(id) from a_out"
                        else:
                            sql3='select max(id) from m_out'
                        try:
                            print(1)
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)
                        if z==1:
                            sql5 = 'select cor_id from a_out'
                        else:
                            sql5 = 'select cor_id from m_out'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        # print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被出库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            if z==1:
                                sql6='select id from apply where cor_id=%s'%(s_id)
                            else:
                                sql6='select id from move where cor_id=%s'%(s_id)
                            try:
                                cursor.execute(sql6)
                                result=cursor.fetchall()
                                print(result)
                                x=result[0][0]
                                print(x)
                            except:
                                tkinter.messagebox.showwarning('警告', '该尸体未被出申请或移库')
                                return
                            if z==1:
                                sql4 = 'insert into a_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, x, now, int(s_id), p_name)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                                print(sql4)
                            else:
                                sql4 = 'insert into m_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, int(s_id), x, p_name, now)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                            print(x)
                            print(sql5)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            cursor.execute(sql7)
                            # 提交到数据库执行
                            db.commit()
                    elif p_name in result2[1]:
                        if z==1:
                            sql3 = "select max(id) from a_out"
                        else:
                            sql3='select max(id) from m_out'
                        try:
                            print(1)
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)
                        if z==1:
                            sql5 = 'select cor_id from a_out'
                        else:
                            sql5 = 'select cor_id from m_out'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        # print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被出库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            if z==1:
                                sql6='select id from apply where cor_id=%s'%(s_id)
                            else:
                                sql6='select id from move where cor_id=%s'%(s_id)
                            try:
                                cursor.execute(sql6)
                                result=cursor.fetchall()
                                print(result)
                                x=result[0][0]
                                print(x)
                            except:
                                tkinter.messagebox.showwarning('警告', '该尸体未被出申请或移库')
                                return
                            if z==1:
                                sql4 = 'insert into a_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, x, now, int(s_id), p_name)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                                print(sql4)
                            else:
                                sql4 = 'insert into m_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, int(s_id), x, p_name, now)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                            print(x)
                            print(sql5)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            cursor.execute(sql7)
                            # 提交到数据库执行
                            db.commit()
                    elif p_name in result2[2]:
                        if z==1:
                            sql3 = "select max(id) from a_out"
                        else:
                            sql3='select max(id) from m_out'
                        try:
                            print(1)
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)
                        if z==1:
                            sql5 = 'select cor_id from a_out'
                        else:
                            sql5 = 'select cor_id from m_out'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        # print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被出库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            if z==1:
                                sql6='select id from apply where cor_id=%s'%(s_id)
                            else:
                                sql6='select id from move where cor_id=%s'%(s_id)
                            try:
                                cursor.execute(sql6)
                                result=cursor.fetchall()
                                print(result)
                                x=result[0][0]
                                print(x)
                            except:
                                tkinter.messagebox.showwarning('警告', '该尸体未被出申请或移库')
                                return
                            if z==1:
                                sql4 = 'insert into a_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, x, now, int(s_id), p_name)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                                print(sql4)
                            else:
                                sql4 = 'insert into m_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, int(s_id), x, p_name, now)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                            print(x)
                            print(sql5)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            cursor.execute(sql7)
                            # 提交到数据库执行
                            db.commit()
                    elif p_name in result2[3]:
                        if z==1:
                            sql3 = "select max(id) from a_out"
                        else:
                            sql3='select max(id) from m_out'
                        try:
                            print(1)
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)
                        if z==1:
                            sql5 = 'select cor_id from a_out'
                        else:
                            sql5 = 'select cor_id from m_out'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        # print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被出库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            if z==1:
                                sql6='select id from apply where cor_id=%s'%(s_id)
                            else:
                                sql6='select id from move where cor_id=%s'%(s_id)
                            try:
                                cursor.execute(sql6)
                                result=cursor.fetchall()
                                print(result)
                                x=result[0][0]
                                print(x)
                            except:
                                tkinter.messagebox.showwarning('警告', '该尸体未被出申请或移库')
                                return
                            if z==1:
                                sql4 = 'insert into a_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, x, now, int(s_id), p_name)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                                print(sql4)
                            else:
                                sql4 = 'insert into m_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, int(s_id), x, p_name, now)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                            print(x)
                            print(sql5)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            cursor.execute(sql7)
                            # 提交到数据库执行
                            db.commit()




            def move():
                p_name = tt3.get(1.0, 1.5)
                oloc_id=tt4.get(1.0,1.5)
                nloc_id=tt5.get(1.0,1.5)
                sql = 'select name from cor where id=%s' % (s_id)
                # try:
                cursor.execute(sql)
                result = cursor.fetchone()
                if s_name in result:
                    # print('sbnb')
                    sql2 = 'select name from doc'
                    cursor.execute(sql2)
                    result2 = cursor.fetchall()
                    print(result2)
                    if p_name in result2[0]:
                        sql3 = "select max(id) from move"
                        try:
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)

                        sql5 = 'select cor_id from move'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被移库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            sql6='select id from tingshi.in where cor_id=%s'%(s_id)
                            cursor.execute(sql6)
                            result=cursor.fetchall()
                            x=result[0][0]
                            print(x)
                            sql4 = 'insert into move values' + ' (%d,%d,"%s","%s","%s","%s")' % (
                                i + 1, int(s_id), int(oloc_id), int(nloc_id), x, now)
                            sql5='update cor set location_id=%s where id=%s'%(int(nloc_id),s_id)
                            print(sql5)
                            sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                            sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                            print(sql4)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql6)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            # cursor.execute(sql7)
                            # 提交到数据库执行
                            # db.commit()
                    elif p_name in result2[1]:
                                sql3 = "select max(id) from move"
                                try:
                                    cursor.execute(sql3)
                                    result3 = cursor.fetchall()
                                    i = result3[0][0]
                                    if (i == None):
                                        i = 0
                                except:
                                    i = 0
                                print(type(s_id), type(tt4), type(tt5))
                                # print(type(s2), type(i), i, result3)

                                sql5 = 'select cor_id from move'
                                cursor.execute(sql5)
                                result4 = cursor.fetchall()
                                print(result4)
                                x = 0
                                while x <= len(result4):
                                    if (x == len(result4)):
                                        x += 1
                                    elif int(s_id) in result4[x]:
                                        print('yicunzai')
                                        tkinter.messagebox.showwarning('警告', '该尸体已被移库，请勿重复操作')
                                        break
                                    x += 1
                                    print(result4)

                                    # print(sql4)
                                    sql6 = 'select id from tingshi.in where cor_id=%s' % (s_id)
                                    cursor.execute(sql6)
                                    result = cursor.fetchall()
                                    x = result[0][0]
                                    print(x)
                                    sql4 = 'insert into move values' + ' (%d,%d,"%s","%s","%s","%s")' % (
                                        i + 1, int(s_id), int(oloc_id), int(nloc_id), x, now)
                                    sql5 = 'update cor set location_id=%s where id=%s' % (int(nloc_id), s_id)
                                    print(sql5)
                                    sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                    sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                                    print(sql4)
                                    try:
                                        # 执行sql语句
                                        cursor.execute(sql4)
                                        db.commit()
                                        cursor.execute(sql5)
                                        db.commit()
                                        cursor.execute(sql6)
                                        # 提交到数据库执行
                                        db.commit()

                                    except:
                                        # 发生错误时回滚
                                        print("sql wrong")
                                        db.rollback()
                                    # cursor.execute(sql5)
                                    # db.commit()
                                    cursor.execute(sql7)
                                    # 提交到数据库执行
                                    db.commit()
                    elif p_name in result2[2]:
                                sql3 = "select max(id) from move"
                                try:
                                    cursor.execute(sql3)
                                    result3 = cursor.fetchall()
                                    i = result3[0][0]
                                    if (i == None):
                                        i = 0
                                except:
                                    i = 0
                                print(type(s_id), type(tt4), type(tt5))
                                # print(type(s2), type(i), i, result3)

                                sql5 = 'select cor_id from move'
                                cursor.execute(sql5)
                                result4 = cursor.fetchall()
                                print(result4)
                                x = 0
                                while x <= len(result4):
                                    if (x == len(result4)):
                                        x += 1
                                    elif int(s_id) in result4[x]:
                                        print('yicunzai')
                                        tkinter.messagebox.showwarning('警告', '该尸体已被移库，请勿重复操作')
                                        break
                                    x += 1
                                    print(result4)

                                    # print(sql4)
                                    sql6 = 'select id from tingshi.in where cor_id=%s' % (s_id)
                                    cursor.execute(sql6)
                                    result = cursor.fetchall()
                                    x = result[0][0]
                                    print(x)
                                    sql4 = 'insert into move values' + ' (%d,%d,"%s","%s","%s","%s")' % (
                                        i + 1, int(s_id), int(oloc_id), int(nloc_id), x, now)
                                    sql5 = 'update cor set location_id=%s where id=%s' % (int(nloc_id), s_id)
                                    print(sql5)
                                    sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                    sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                                    print(sql4)
                                    try:
                                        # 执行sql语句
                                        cursor.execute(sql4)
                                        db.commit()
                                        cursor.execute(sql5)
                                        db.commit()
                                        cursor.execute(sql6)
                                        # 提交到数据库执行
                                        db.commit()

                                    except:
                                        # 发生错误时回滚
                                        print("sql wrong")
                                        db.rollback()
                                    # cursor.execute(sql5)
                                    # db.commit()
                                    cursor.execute(sql7)
                                    # 提交到数据库执行
                                    db.commit()
                    elif p_name in result2[3]:
                                sql3 = "select max(id) from move"
                                try:
                                    cursor.execute(sql3)
                                    result3 = cursor.fetchall()
                                    i = result3[0][0]
                                    if (i == None):
                                        i = 0
                                except:
                                    i = 0
                                print(type(s_id), type(tt4), type(tt5))
                                # print(type(s2), type(i), i, result3)

                                sql5 = 'select cor_id from move'
                                cursor.execute(sql5)
                                result4 = cursor.fetchall()
                                print(result4)
                                x = 0
                                while x <= len(result4):
                                    if (x == len(result4)):
                                        x += 1
                                    elif int(s_id) in result4[x]:
                                        print('yicunzai')
                                        tkinter.messagebox.showwarning('警告', '该尸体已被移库，请勿重复操作')
                                        break
                                    x += 1
                                    print(result4)

                                    # print(sql4)
                                    sql6 = 'select id from tingshi.in where cor_id=%s' % (s_id)
                                    cursor.execute(sql6)
                                    result = cursor.fetchall()
                                    x = result[0][0]
                                    print(x)
                                    sql4 = 'insert into move values' + ' (%d,%d,"%s","%s","%s","%s")' % (
                                        i + 1, int(s_id), int(oloc_id), int(nloc_id), x, now)
                                    sql5 = 'update cor set location_id=%s where id=%s' % (int(nloc_id), s_id)
                                    print(sql5)
                                    sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                    sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                                    print(sql4)
                                    try:
                                        # 执行sql语句
                                        cursor.execute(sql4)
                                        db.commit()
                                        cursor.execute(sql5)
                                        db.commit()
                                        cursor.execute(sql6)
                                        # 提交到数据库执行
                                        db.commit()

                                    except:
                                        # 发生错误时回滚
                                        print("sql wrong")
                                        db.rollback()
                                    # cursor.execute(sql5)
                                    # db.commit()
                                    cursor.execute(sql7)
                                    # 提交到数据库执行
                                    db.commit()
                    else:
                        tkinter.messagebox.showwarning('警告', '你不是医生你是谁')
                else:
                    tkinter.messagebox.showwarning('警告', '该尸体不存在或已出库')
            if len(indexs) == 0:
                return
            bt = tk.Button(tc, text='移库', command=move)
            bt.grid(row=5, column=0)
            bt = tk.Button(tc, text='申请出库', command=lambda :out(1))
            bt.grid(row=5, column=1)
            bt = tk.Button(tc, text='强制出库', command=lambda:out(2))
            bt.grid(row=5, column=2)
            bt = tk.Button(tc, text='返回', command=tc.destroy)
            bt.grid(row=5, column=3)


        while j < 24:

            lb3.insert(result[j][0],result[j][0])
            lb1.insert(result[j][0],result[j][1])
            lb2.insert(result[j][0], result[j][2])
            lb4.insert(result[j][0],result[j][3])
            # a_j.pack()
            # # self.j.grid(column=0)
            # a_j.insert( '尸体名:%s，家属:%s' % (result[j][0], result[j][1]),chars=100)
            j += 1
        lb3.bind("<<ListboxSelect>>", show_msg)
    fenye4()#第一页


    frame4 = tk.Frame(window, height=350, bg="yellow")
    frame4.pack(side=tk.TOP, fill=tk.X)
    def fenye5():

        sql = 'select id,name,company,location_id from cor'
        try:
            cursor.execute(sql)
            result = cursor.fetchall()



        except:
            tk.messagebox.showwarning('警告', '请不要乱查询')
        # self.te=Label(frma,width=50,height=5)
        # self.te.grid(frma,row=10,column=10)
        # btnSend = Button(tc.frma, text='发 送', width=8)  # 在frmLB容器中添加
        # btnSend.grid(row=2, column=0)
        # btnCancel = Button(tc.frma, text='取消', width=8)
        # btnCancel.grid(row=2, column=1, sticky=E)
        lb3 = tk.Listbox(frame4, selectmode='BROWSE', height=len(result))
        lb3.pack(side='left', fill='both')
        lb1 = tk.Listbox(frame4, selectmode='extended', height=len(result))
        lb1.pack(side='left', fill='both')
        lb2 = tk.Listbox(frame4, selectmode='extended', height=len(result))
        lb2.pack(side='left', fill='both')
        lb4 = tk.Listbox(frame4, selectmode='extended', height=len(result))
        lb4.pack(side='left', fill='both')
        lb4.insert(0, '货位编号')
        lb3.insert(0, '尸体编号')
        lb1.insert(0, '尸体姓名')
        lb2.insert(0, '存放单位')
        j = 25
        def show_msg(*args):

            indexs = lb3.curselection()
            id = int(indexs[0])
            s_id=lb3.get(id)
            s_name=lb1.get(indexs[0])
            s_id2=lb4.get(id)
            s_company=lb2.get(id)
            # print(s_id,s_name,s_id2,s_company)
            tc=tk.Tk()
            tc.title('单据填写')
            lab1 = tk.Label(tc, text="尸体id")
            lab1.grid(row=0, column=0,)
            lab2 = tk.Label(tc, text="尸体名称")
            lab2.grid(row=1, column=0)
            lab3 = tk.Label(tc, text="操作人姓名")
            lab3.grid(row=2, column=0)
            lab4 = tk.Label(tc, text="老货位编号")
            lab4.grid(row=3, column=0)
            lab5= tk.Label(tc, text="新货位编号")
            lab5.grid(row=4, column=0)
            tt1= tk.Text(tc,width=10,height=1)
            tt1.grid(row=0, column=1)
            tt1.insert(tk.INSERT,s_id)
            tt2 = tk.Text(tc, width=10, height=1)
            tt2.grid(row=1, column=1)
            tt2.insert(tk.INSERT, s_name)
            tt3 = tk.Text(tc, width=10, height=1)
            tt3.grid(row=2, column=1)
            tt3.insert(tk.INSERT,'请在此输入')
            tt4 = tk.Text(tc, width=10, height=1)
            tt4.grid(row=3, column=1)
            tt4.insert(tk.INSERT, s_id2)
            tt5 = tk.Text(tc, width=10, height=1)
            tt5.grid(row=4, column=1)
            tt5.insert(tk.INSERT, '请在此输入')


            def out(z):
                p_name = tt3.get(1.0, 1.5)
                oloc_id=tt4.get(1.0,1.5)
                nloc_id=tt5.get(1.0,1.5)
                sql = 'select name from cor where id=%s' % (s_id)
                # try:
                cursor.execute(sql)
                result = cursor.fetchone()
                if s_name in result:
                    # print('sbnb')
                    sql2 = 'select name from doc'
                    cursor.execute(sql2)
                    result2 = cursor.fetchall()


                    if p_name in result2[0]:
                        if z==1:
                            sql3 = "select max(id) from a_out"
                        else:
                            sql3='select max(id) from m_out'
                        try:
                            print(1)
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)
                        if z==1:
                            sql5 = 'select cor_id from a_out'
                        else:
                            sql5 = 'select cor_id from m_out'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        # print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被出库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            if z==1:
                                sql6='select id from apply where cor_id=%s'%(s_id)
                            else:
                                sql6='select id from move where cor_id=%s'%(s_id)
                            try:
                                cursor.execute(sql6)
                                result=cursor.fetchall()
                                print(result)
                                x=result[0][0]
                                print(x)
                            except:
                                tkinter.messagebox.showwarning('警告', '该尸体未被出申请或移库')
                                return
                            if z==1:
                                sql4 = 'insert into a_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, x, now, int(s_id), p_name)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                                print(sql4)
                            else:
                                sql4 = 'insert into m_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, int(s_id), x, p_name, now)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                            print(x)
                            print(sql5)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            cursor.execute(sql7)
                            # 提交到数据库执行
                            db.commit()
                    elif p_name in result2[1]:
                        if z==1:
                            sql3 = "select max(id) from a_out"
                        else:
                            sql3='select max(id) from m_out'
                        try:
                            print(1)
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)
                        if z==1:
                            sql5 = 'select cor_id from a_out'
                        else:
                            sql5 = 'select cor_id from m_out'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        # print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被出库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            if z==1:
                                sql6='select id from apply where cor_id=%s'%(s_id)
                            else:
                                sql6='select id from move where cor_id=%s'%(s_id)
                            try:
                                cursor.execute(sql6)
                                result=cursor.fetchall()
                                print(result)
                                x=result[0][0]
                                print(x)
                            except:
                                tkinter.messagebox.showwarning('警告', '该尸体未被出申请或移库')
                                return
                            if z==1:
                                sql4 = 'insert into a_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, x, now, int(s_id), p_name)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                                print(sql4)
                            else:
                                sql4 = 'insert into m_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, int(s_id), x, p_name, now)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                            print(x)
                            print(sql5)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            cursor.execute(sql7)
                            # 提交到数据库执行
                            db.commit()
                    elif p_name in result2[2]:
                        if z==1:
                            sql3 = "select max(id) from a_out"
                        else:
                            sql3='select max(id) from m_out'
                        try:
                            print(1)
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)
                        if z==1:
                            sql5 = 'select cor_id from a_out'
                        else:
                            sql5 = 'select cor_id from m_out'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        # print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被出库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            if z==1:
                                sql6='select id from apply where cor_id=%s'%(s_id)
                            else:
                                sql6='select id from move where cor_id=%s'%(s_id)
                            try:
                                cursor.execute(sql6)
                                result=cursor.fetchall()
                                print(result)
                                x=result[0][0]
                                print(x)
                            except:
                                tkinter.messagebox.showwarning('警告', '该尸体未被出申请或移库')
                                return
                            if z==1:
                                sql4 = 'insert into a_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, x, now, int(s_id), p_name)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                                print(sql4)
                            else:
                                sql4 = 'insert into m_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, int(s_id), x, p_name, now)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                            print(x)
                            print(sql5)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            cursor.execute(sql7)
                            # 提交到数据库执行
                            db.commit()
                    elif p_name in result2[3]:
                        if z==1:
                            sql3 = "select max(id) from a_out"
                        else:
                            sql3='select max(id) from m_out'
                        try:
                            print(1)
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)
                        if z==1:
                            sql5 = 'select cor_id from a_out'
                        else:
                            sql5 = 'select cor_id from m_out'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        # print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被出库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            if z==1:
                                sql6='select id from apply where cor_id=%s'%(s_id)
                            else:
                                sql6='select id from move where cor_id=%s'%(s_id)
                            try:
                                cursor.execute(sql6)
                                result=cursor.fetchall()
                                print(result)
                                x=result[0][0]
                                print(x)
                            except:
                                tkinter.messagebox.showwarning('警告', '该尸体未被出申请或移库')
                                return
                            if z==1:
                                sql4 = 'insert into a_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, x, now, int(s_id), p_name)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                                print(sql4)
                            else:
                                sql4 = 'insert into m_out values' + ' (%d,%d,"%s","%s","%s")' % (
                                    i + 1, int(s_id), x, p_name, now)
                                sql5 = 'update cor set location_id=NULL where id=%s' % (int(s_id))
                                print(sql5)
                                # sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                            print(x)
                            print(sql5)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            cursor.execute(sql7)
                            # 提交到数据库执行
                            db.commit()




            def move():
                p_name = tt3.get(1.0, 1.5)
                oloc_id=tt4.get(1.0,1.5)
                nloc_id=tt5.get(1.0,1.5)
                sql = 'select name from cor where id=%s' % (s_id)
                # try:
                cursor.execute(sql)
                result = cursor.fetchone()
                if s_name in result:
                    # print('sbnb')
                    sql2 = 'select name from doc'
                    cursor.execute(sql2)
                    result2 = cursor.fetchall()
                    print(result2)
                    if p_name in result2[0]:
                        sql3 = "select max(id) from move"
                        try:
                            cursor.execute(sql3)
                            result3 = cursor.fetchall()
                            i = result3[0][0]
                            if(i==None):
                                i=0
                        except:
                            i=0
                        print(type(s_id),type(tt4),type(tt5))
                        # print(type(s2), type(i), i, result3)

                        sql5 = 'select cor_id from move'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        print(result4)
                        x = 0
                        while x <= len(result4):
                            if (x==len(result4)):
                                x+=1
                            elif int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被移库，请勿重复操作')
                                break
                            x += 1
                            print(result4)

                            # print(sql4)
                            sql6='select id from tingshi.in where cor_id=%s'%(s_id)
                            cursor.execute(sql6)
                            result=cursor.fetchall()
                            x=result[0][0]
                            print(x)
                            sql4 = 'insert into move values' + ' (%d,%d,"%s","%s","%s","%s")' % (
                                i + 1, int(s_id), int(oloc_id), int(nloc_id), x, now)
                            sql5='update cor set location_id=%s where id=%s'%(int(nloc_id),s_id)
                            print(sql5)
                            sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                            sql7='update loc set cor_id=NULL where id=%s'%(int(oloc_id))
                            print(sql4)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                cursor.execute(sql5)
                                cursor.execute(sql6)
                                cursor.execute(sql7)
                                # 提交到数据库执行
                                db.commit()

                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                            # cursor.execute(sql5)
                            # db.commit()
                            # cursor.execute(sql7)
                            # 提交到数据库执行
                            # db.commit()
                    elif p_name in result2[1]:
                                sql3 = "select max(id) from move"
                                try:
                                    cursor.execute(sql3)
                                    result3 = cursor.fetchall()
                                    i = result3[0][0]
                                    if (i == None):
                                        i = 0
                                except:
                                    i = 0
                                print(type(s_id), type(tt4), type(tt5))
                                # print(type(s2), type(i), i, result3)

                                sql5 = 'select cor_id from move'
                                cursor.execute(sql5)
                                result4 = cursor.fetchall()
                                print(result4)
                                x = 0
                                while x <= len(result4):
                                    if (x == len(result4)):
                                        x += 1
                                    elif int(s_id) in result4[x]:
                                        print('yicunzai')
                                        tkinter.messagebox.showwarning('警告', '该尸体已被移库，请勿重复操作')
                                        break
                                    x += 1
                                    print(result4)

                                    # print(sql4)
                                    sql6 = 'select id from tingshi.in where cor_id=%s' % (s_id)
                                    cursor.execute(sql6)
                                    result = cursor.fetchall()
                                    x = result[0][0]
                                    print(x)
                                    sql4 = 'insert into move values' + ' (%d,%d,"%s","%s","%s","%s")' % (
                                        i + 1, int(s_id), int(oloc_id), int(nloc_id), x, now)
                                    sql5 = 'update cor set location_id=%s where id=%s' % (int(nloc_id), s_id)
                                    print(sql5)
                                    sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                    sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                                    print(sql4)
                                    try:
                                        # 执行sql语句
                                        cursor.execute(sql4)
                                        db.commit()
                                        cursor.execute(sql5)
                                        db.commit()
                                        cursor.execute(sql6)
                                        # 提交到数据库执行
                                        db.commit()

                                    except:
                                        # 发生错误时回滚
                                        print("sql wrong")
                                        db.rollback()
                                    # cursor.execute(sql5)
                                    # db.commit()
                                    cursor.execute(sql7)
                                    # 提交到数据库执行
                                    db.commit()
                    elif p_name in result2[2]:
                                sql3 = "select max(id) from move"
                                try:
                                    cursor.execute(sql3)
                                    result3 = cursor.fetchall()
                                    i = result3[0][0]
                                    if (i == None):
                                        i = 0
                                except:
                                    i = 0
                                print(type(s_id), type(tt4), type(tt5))
                                # print(type(s2), type(i), i, result3)

                                sql5 = 'select cor_id from move'
                                cursor.execute(sql5)
                                result4 = cursor.fetchall()
                                print(result4)
                                x = 0
                                while x <= len(result4):
                                    if (x == len(result4)):
                                        x += 1
                                    elif int(s_id) in result4[x]:
                                        print('yicunzai')
                                        tkinter.messagebox.showwarning('警告', '该尸体已被移库，请勿重复操作')
                                        break
                                    x += 1
                                    print(result4)

                                    # print(sql4)
                                    sql6 = 'select id from tingshi.in where cor_id=%s' % (s_id)
                                    cursor.execute(sql6)
                                    result = cursor.fetchall()
                                    x = result[0][0]
                                    print(x)
                                    sql4 = 'insert into move values' + ' (%d,%d,"%s","%s","%s","%s")' % (
                                        i + 1, int(s_id), int(oloc_id), int(nloc_id), x, now)
                                    sql5 = 'update cor set location_id=%s where id=%s' % (int(nloc_id), s_id)
                                    print(sql5)
                                    sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                    sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                                    print(sql4)
                                    try:
                                        # 执行sql语句
                                        cursor.execute(sql4)
                                        db.commit()
                                        cursor.execute(sql5)
                                        db.commit()
                                        cursor.execute(sql6)
                                        # 提交到数据库执行
                                        db.commit()

                                    except:
                                        # 发生错误时回滚
                                        print("sql wrong")
                                        db.rollback()
                                    # cursor.execute(sql5)
                                    # db.commit()
                                    cursor.execute(sql7)
                                    # 提交到数据库执行
                                    db.commit()
                    elif p_name in result2[3]:
                                sql3 = "select max(id) from move"
                                try:
                                    cursor.execute(sql3)
                                    result3 = cursor.fetchall()
                                    i = result3[0][0]
                                    if (i == None):
                                        i = 0
                                except:
                                    i = 0
                                print(type(s_id), type(tt4), type(tt5))
                                # print(type(s2), type(i), i, result3)

                                sql5 = 'select cor_id from move'
                                cursor.execute(sql5)
                                result4 = cursor.fetchall()
                                print(result4)
                                x = 0
                                while x <= len(result4):
                                    if (x == len(result4)):
                                        x += 1
                                    elif int(s_id) in result4[x]:
                                        print('yicunzai')
                                        tkinter.messagebox.showwarning('警告', '该尸体已被移库，请勿重复操作')
                                        break
                                    x += 1
                                    print(result4)

                                    # print(sql4)
                                    sql6 = 'select id from tingshi.in where cor_id=%s' % (s_id)
                                    cursor.execute(sql6)
                                    result = cursor.fetchall()
                                    x = result[0][0]
                                    print(x)
                                    sql4 = 'insert into move values' + ' (%d,%d,"%s","%s","%s","%s")' % (
                                        i + 1, int(s_id), int(oloc_id), int(nloc_id), x, now)
                                    sql5 = 'update cor set location_id=%s where id=%s' % (int(nloc_id), s_id)
                                    print(sql5)
                                    sql6 = 'update loc set cor_id=%s where id=%s' % (s_id, int(nloc_id))
                                    sql7 = 'update loc set cor_id=NULL where id=%s' % (int(oloc_id))
                                    print(sql4)
                                    try:
                                        # 执行sql语句
                                        cursor.execute(sql4)
                                        db.commit()
                                        cursor.execute(sql5)
                                        db.commit()
                                        cursor.execute(sql6)
                                        # 提交到数据库执行
                                        db.commit()

                                    except:
                                        # 发生错误时回滚
                                        print("sql wrong")
                                        db.rollback()
                                    # cursor.execute(sql5)
                                    # db.commit()
                                    cursor.execute(sql7)
                                    # 提交到数据库执行
                                    db.commit()
                    else:
                        tkinter.messagebox.showwarning('警告', '你不是医生你是谁')
                else:
                    tkinter.messagebox.showwarning('警告', '该尸体不存在或已出库')
            if len(indexs) == 0:
                return
            bt = tk.Button(tc, text='移库', command=move)
            bt.grid(row=5, column=0)
            bt = tk.Button(tc, text='申请出库', command=lambda :out(1))
            bt.grid(row=5, column=1)
            bt = tk.Button(tc, text='强制出库', command=lambda:out(2))
            bt.grid(row=5, column=2)
            bt = tk.Button(tc, text='返回', command=tc.destroy)
            bt.grid(row=5, column=3)
        while j < 48:
            lb3.insert(result[j][0], result[j][0])
            lb1.insert(result[j][0], result[j][1])
            lb2.insert(result[j][0], result[j][2])
            lb4.insert(result[j][0], result[j][3])
            j += 1
        lb3.bind("<<ListboxSelect>>", show_msg)
    fenye5()#第二页

    # window.attributes("-topmost", True)
    window.mainloop()
# if __name__ == "__main__":
#     tbm = TestBenchMaker()

# initialGUI()