import tkinter as tk
import pymysql
import tkinter.messagebox
db = pymysql.connect("localhost", "root", "123456", "tingshi")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# class TestBenchMaker:

        #
        # TITLE = "Test"
        # WIDTH = 500
        # HEIGHT = 500
        # parseDic = {}

    # Initial GUI
def initialGUI():
    TITLE = "单据详情"
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

        # Change type
        # def changeType(tag):
        #     clockSet.pack_forget()
        #     resetSet.pack_forget()
        #     customSet.pack_forget()
        #     if tag == 0:
        #         clockSet.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES, pady=5, padx=10)
        #     elif tag == 1:
        #         resetSet.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES, pady=5, padx=10)
        #     elif tag == 2:
        #         customSet.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES, pady=5, padx=10)


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
    tk.Radiobutton(frame2, text="入库单", command=lambda: changeTag(0), width=tagWidth, variable=tag, value=0, bd=1, indicatoron=0).grid(column=0, row=1)
    tk.Radiobutton(frame2, text="移库单", command=lambda: changeTag(1), variable=tag, width=tagWidth, value=1, bd=1, indicatoron=0).grid(column=1, row=1)
    tk.Radiobutton(frame2, text="申请式出库单", command=lambda: changeTag(2), variable=tag, width=tagWidth, value=2, bd=1, indicatoron=0).grid(column=2, row=1)
    tk.Radiobutton(frame2, text="移库式出库单", command=lambda: changeTag(3), variable=tag, width=tagWidth, value=3, bd=1,indicatoron=0).grid(column=3, row=1)
    tk.Radiobutton(frame2, text="第五页", command=lambda: changeTag(4), variable=tag, width=tagWidth, value=4, bd=1,indicatoron=0).grid(column=4, row=1)


    frame5 = tk.Frame(window, height=350, bg="yellow")

    def fenye1():
        sql = 'select * from a_out'
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            # j = 0
            print(result)

        except:
            tk.messagebox.showwarning('警告', '请不要乱查询')
        lb3 = tk.Listbox(frame5, selectmode='BROWSE', height=len(result)+1)
        lb3.pack(side='left', fill='both')
        lb1 = tk.Listbox(frame5, selectmode='extended', height=len(result)+1)
        lb1.pack(side='left', fill='both')
        lb2 = tk.Listbox(frame5, selectmode='extended', height=len(result)+1)
        lb2.pack(side='left', fill='both')
        lb4 = tk.Listbox(frame5, selectmode='extended', height=len(result)+1)
        lb4.pack(side='left', fill='both')
        lb5 = tk.Listbox(frame5, selectmode='extended', height=len(result) + 1)
        lb5.pack(side='left', fill='both')
        lb5.insert(0, '操作人姓名')
        lb4.insert(0, '单据编号')
        lb3.insert(0, '申请单编号')
        lb1.insert(0, '时间')
        lb2.insert(0, '尸体编号')
        j = 0
        while j < len(result):
            lb3.insert(result[j][0], result[j][1])
            lb1.insert(result[j][0], result[j][2])
            lb2.insert(result[j][0], result[j][3])
            lb4.insert(result[j][0], result[j][0])
            lb5.insert(result[j][0], result[j][4])

            j += 1
    fenye1()#申请式出库单
    frame6 = tk.Frame(window, height=350, bg="yellow")
    def fenye2():
        sql = 'select * from m_out'
        try:
            cursor.execute(sql)
            result = cursor.fetchall()


        except:
            tk.messagebox.showwarning('警告', '请不要乱查询')

        lb3 = tk.Listbox(frame6, selectmode='BROWSE', height=len(result) + 1)
        lb3.pack(side='left', fill='both')
        lb1 = tk.Listbox(frame6, selectmode='extended', height=len(result) + 1)
        lb1.pack(side='left', fill='both')
        lb2 = tk.Listbox(frame6, selectmode='extended', height=len(result) + 1)
        lb2.pack(side='left', fill='both')
        lb4 = tk.Listbox(frame6, selectmode='extended', height=len(result) + 1)
        lb4.pack(side='left', fill='both')
        lb5 = tk.Listbox(frame6, selectmode='extended', height=len(result) + 1)
        lb5.pack(side='left', fill='both')
        lb5.insert(0, '操作人姓名')
        lb4.insert(0, '单据编号')
        lb3.insert(0, '移库单编号')
        lb1.insert(0, '时间')
        lb2.insert(0, '尸体编号')
        j = 0
        while j < len(result):
            lb3.insert(result[j][0], result[j][2])
            lb1.insert(result[j][0], result[j][4])
            lb2.insert(result[j][0], result[j][1])
            lb4.insert(result[j][0], result[j][0])
            lb5.insert(result[j][0], result[j][3])
            j += 1
    fenye2()#移库式出库单
    frame7 = tk.Frame(window, height=350, bg="yellow")
    def fenye3():
        sql = 'select id,name,company,location_id from cor'
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
        lb5 = tk.Listbox(frame7, selectmode='extended', height=len(result))
        lb5.pack(side='left', fill='both')
        lb6 = tk.Listbox(frame7, selectmode='extended', height=len(result))
        lb6.pack(side='left', fill='both')
        lb7 = tk.Listbox(frame7, selectmode='extended', height=len(result))
        lb7.pack(side='left', fill='both')
        lb4.insert(0, '出库单编号')
        lb3.insert(0, '尸体编号')
        lb1.insert(0, '尸体姓名')
        lb2.insert(0, '医生编号')
        lb5.insert(0, '医生姓名')
        lb6.insert(0, '时间')
        lb7.insert(0, '货位编号')
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
            lab3 = tk.Label(tc, text="申请人姓名")
            lab3.grid(row=2, column=0)
            lab4 = tk.Label(tc, text="申请类型")
            lab4.grid(row=3, column=0)
            lab5= tk.Label(tc, text="立案申请")
            lab5.grid(row=3, column=1)
            tt1= tk.Text(tc,width=10,height=1)
            tt1.grid(row=0, column=1)
            tt1.insert(tk.INSERT,s_id)
            tt2 = tk.Text(tc, width=10, height=1)
            tt2.grid(row=1, column=1)
            tt2.insert(tk.INSERT, s_name)
            tt3 = tk.Text(tc, width=10, height=1)
            tt3.grid(row=2, column=1)
            tt3.insert(tk.INSERT,'请在此输入')

            def apply():
                p_name = tt3.get(1.0, 1.5)
                sql = 'select name from cor where id=%s' % (s_id)
                # try:
                cursor.execute(sql)
                result = cursor.fetchone()
                if s_name in result:
                    # print('sbnb')
                    sql2 = 'select name from police'
                    cursor.execute(sql2)
                    result2 = cursor.fetchall()
                    if p_name in result2[0]:
                        sql3 = "select max(id) from apply"
                        cursor.execute(sql3)
                        result3 = cursor.fetchall()
                        i = result3[0][0]
                        # print(type(s2), type(i), i, result3)
                        sql4 = 'insert into apply(id,cor_id,cor_name,name,type) values' + ' (%d,%d,"%s","%s","立案申请")' % (
                        i + 1, int(s_id), s_name, p_name)
                        sql5 = 'select cor_id from apply'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        x = 0
                        while x < len(result4):
                            if int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被申请')
                                break
                            x += 1
                            print(result4)
                            print(sql4)
                            try:
                                # 执行sql语句
                                cursor.execute(sql4)
                                # 提交到数据库执行
                                db.commit()
                            except:
                                # 发生错误时回滚
                                print("sql wrong")
                                db.rollback()
                    elif p_name in result2[1]:
                        sql3 = "select max(id) from apply"
                        cursor.execute(sql3)
                        result3 = cursor.fetchall()
                        i = result3[0][0]
                        # print(type(s2), type(i), i, result3)
                        sql4 = 'insert into apply(id,cor_id,cor_name,name,type) values' + ' (%d,%d,"%s","%s","立案申请")' % (
                            i + 1, int(s_id), s_name, p_name)
                        sql5 = 'select cor_id from apply'
                        cursor.execute(sql5)
                        result4 = cursor.fetchall()
                        x = 0
                        while x < len(result4):
                            if int(s_id) in result4[x]:
                                print('yicunzai')
                                tkinter.messagebox.showwarning('警告', '该尸体已被申请')
                                break
                            x += 1
                            print(result4)
                            print(sql4)
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
                        tkinter.messagebox.showwarning('警告', '你不是警察你是谁')
                else:
                    tkinter.messagebox.showwarning('警告', '该尸体不存在或已出库')
            if len(indexs) == 0:
                return
            bt=tk.Button(tc,text='确定',command=apply)
            bt.grid(row=4,column=0)
            bt = tk.Button(tc, text='返回',command=tc.destroy)
            bt.grid(row=4, column=1)
        while j < 48:
            lb3.insert(result[j][0], result[j][0])
            lb1.insert(result[j][0], result[j][1])
            lb2.insert(result[j][0], result[j][2])
            lb4.insert(result[j][0], result[j][3])
            j += 1
        lb3.bind("<<ListboxSelect>>", show_msg)
        while j < len(result):
            lb3.insert(result[j][0], result[j][0])
            lb1.insert(result[j][0], result[j][1])
            lb2.insert(result[j][0], result[j][2])
            lb4.insert(result[j][0], result[j][3])
            # a_j.pack()
            # # self.j.grid(column=0)
            # a_j.insert( '尸体名:%s，家属:%s' % (result[j][0], result[j][1]),chars=100)
            j += 1

    fenye3()#无

    frame3 = tk.Frame(window, height=350, bg="yellow")
    frame3.pack(side=tk.TOP, fill=tk.X)
    def fenye4():

        sql = 'select * from tingshi.in'
        try:
            cursor.execute(sql)
            result = cursor.fetchall()

        except:
            tk.messagebox.showwarning('警告', '请不要乱查询')
        lb3 = tk.Listbox(frame3, selectmode='BROWSE', height=len(result))
        lb3.pack(side='left', fill='both')
        lb1 = tk.Listbox(frame3, selectmode='extended', height=len(result))
        lb1.pack(side='left', fill='both')
        lb2 = tk.Listbox(frame3, selectmode='extended', height=len(result))
        lb2.pack(side='left', fill='both')
        lb4 = tk.Listbox(frame3, selectmode='extended', height=len(result))
        lb4.pack(side='left', fill='both')
        lb5 = tk.Listbox(frame3, selectmode='extended', height=len(result))
        lb5.pack(side='left', fill='both')
        lb6 = tk.Listbox(frame3, selectmode='extended', height=len(result))
        lb6.pack(side='left', fill='both')
        lb7 = tk.Listbox(frame3, selectmode='extended', height=len(result))
        lb7.pack(side='left', fill='both')
        lb4.insert(0, '入库单编号')
        lb3.insert(0, '尸体编号')
        lb1.insert(0, '尸体姓名')
        lb2.insert(0, '医生编号')
        lb5.insert(0, '医生姓名')
        lb6.insert(0, '时间')
        lb7.insert(0, '货位编号')
        j = 0

        def mw(e):
            lb1.yview_scroll(-4 * (e.delta // 120), 'units')
            lb2.yview_scroll(-4 * (e.delta // 120), 'units')
            lb3.yview_scroll(-4 * (e.delta // 120), 'units')
            lb4.yview_scroll(-4 * (e.delta // 120), 'units')
            lb5.yview_scroll(-4 * (e.delta // 120), 'units')
            lb6.yview_scroll(-4 * (e.delta // 120), 'units')
            lb7.yview_scroll(-4 * (e.delta // 120), 'units')

        while j < len(result):

            lb3.insert(result[j][0],result[j][1])
            lb1.insert(result[j][0],result[j][2])
            lb2.insert(result[j][0], result[j][3])
            lb4.insert(result[j][0],result[j][0])
            lb5.insert(result[j][0], result[j][4])
            lb6.insert(result[j][0], result[j][5])
            lb7.insert(result[j][0], result[j][6])

            j += 1
        lb1.bind('<MouseWheel>', mw)
        lb2.bind('<MouseWheel>', mw)
        lb3.bind('<MouseWheel>', mw)
        lb4.bind('<MouseWheel>', mw)
        lb5.bind('<MouseWheel>', mw)
        lb6.bind('<MouseWheel>', mw)
        lb7.bind('<MouseWheel>', mw)
        # lb4.bind('<MouseWheel>', mw)
    fenye4()#入库单


    frame4 = tk.Frame(window, height=350, bg="yellow")
    frame4.pack(side=tk.TOP, fill=tk.X)
    def fenye5():

        sql = 'select * from move'
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)


        except:
            tk.messagebox.showwarning('警告', '请不要乱查询')
        lb3 = tk.Listbox(frame4, selectmode='BROWSE', height=len(result)+1)
        lb3.pack(side='left', fill='both')
        lb1 = tk.Listbox(frame4, selectmode='extended', height=len(result)+1)
        lb1.pack(side='left', fill='both')
        lb2 = tk.Listbox(frame4, selectmode='extended', height=len(result)+1)
        lb2.pack(side='left', fill='both')
        lb4 = tk.Listbox(frame4, selectmode='extended', height=len(result)+1)
        lb4.pack(side='left', fill='both')
        lb5 = tk.Listbox(frame4, selectmode='extended', height=len(result)+1)
        lb5.pack(side='left', fill='both')
        lb6 = tk.Listbox(frame4, selectmode='extended', height=len(result)+1)
        lb6.pack(side='left', fill='both')
        lb5.insert(0, '入库单编号')
        lb6.insert(0, '时间')
        lb4.insert(0, '新货位编号')
        lb3.insert(0, '移库单编号')
        lb1.insert(0, '尸体编号')
        lb2.insert(0, '老货位编号')
        j = 0
        while j < len(result):

            lb3.insert(result[j][0], result[j][0])
            lb1.insert(result[j][0], result[j][1])
            lb2.insert(result[j][0], result[j][2])
            lb4.insert(result[j][0], result[j][3])
            lb5.insert(result[j][0], result[j][4])
            lb6.insert(result[j][0], result[j][5])
            j += 1
    fenye5()#移库单

    # window.attributes("-topmost", True)
    window.mainloop()
# if __name__ == "__main__":
#     tbm = TestBenchMaker()

# initialGUI()