#!/usr/bin/python3

import pymysql
from tkinter import *

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "tingshi")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)
sql = 'select * from cor'
try:
    cursor.execute(sql)
    result = cursor.fetchall()
    j=0
    i=len(result)
    while (j<i):
        print(result[j][3])
        j+=1



except:
    print('wrong')


# 关闭数据库连接
# db.close()
# results = cursor.fetchone()
# print (results[0])
# results=cursor.fetchall()
# print((results[0]))

root = Tk()
text = Text(root,width=50,height=5)
text.pack()
text.insert(INSERT,'原来你是我最想留住的幸运')
text.tag_add('tag1','1.10','1.12')
text.tag_config('tag1',background='yellow',foreground='red')
mainloop()
