# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 15:57:27 2022

@author: perry
"""

import db1

# idcard=input('請輸入員工編號:')
# name=input('請輸入員工姓名:')
# sex=input('請輸入員工性別 F、M:')
# tel=input('請輸入員工電話:')
# assume=input('請輸入就職日期 yyyy-mm-dd:')
# sql="insert into emplouee(id,name,sex,tel,assume) values('{}','{}','{}','{}','{}')".format(idcard,name,sex,tel,assume)

# cursor=db1.conn.cursor()
# cursor.execute(sql)
# db1.conn.commit()
# print("查詢員工編號")
# sql="select id from emplouee "

# cursor=db1.conn.cursor()
# cursor.execute(sql)
# db1.conn.commit()

# alldate=cursor.fetchall()
# print("員工工號")
# print("-"*30)
# for row in alldate: 
#       print(row[0])
    
# items=input("請輸入工作項目:")
# info=input("請輸入工作詳述:")
# employeeid=input("請輸入員工編號:")
# sql="insert into works (items,info,employeeid) values('{}','{}','{}')".format(items,info,employeeid)
# cursor=db1.conn.cursor()
# cursor.execute(sql)
# db1.conn.commit()

# tel=input("請輸入修改電話:")
# sex=input("請輸入修改性別:")
# idcard=input("請輸入員工編號:")
# sql="update emplouee set sex='{}', tel='{}' where id='{}' ".format(sex,tel,idcard)
# cursor=db1.conn.cursor()
# cursor.execute(sql)
# db1.conn.commit()

# print("查詢員工編號")
# sql="select id from emplouee "

# cursor=db1.conn.cursor()
# cursor.execute(sql)
# db1.conn.commit()

# alldate=cursor.fetchall()
# print("員工工號")
# print(alldate)
# print("-"*30)
# for row in alldate: 
#     print(row[0])

# idcard=input("請輸入員工編號:")
# sql="select name,sex,tel,assume from emplouee where id='{}'".format(idcard)

# cursor=db1.conn.cursor()
# cursor.execute(sql)
# db1.conn.commit()
# alldate=cursor.fetchall()
# # print(alldate)
# for row in alldate:
#     print("員工姓名:",row[0])
#     print("性別:",row[1])
#     print("電話:",row[2])
#     print("日期:",row[3])
sql="select * from works"
cursor=db1.conn.cursor()
cursor.execute(sql)
db1.conn.commit()
alldate=cursor.fetchall()
print(alldate)

idcard=input('請輸入員工編號:')
sql=" select e.name,w.items,w.info from emplouee e inner join works w  on e.id=w.employeeid  and w.employeeid='{}' ".format(idcard)



#sql="select e.name,w.items,w.info from emplouee e ,works w where e.id=w.employeeid and w.employeeid='{}'".format(idcard)
cursor=db1.conn.cursor()
cursor.execute(sql)
db1.conn.commit()
alldate=cursor.fetchall()
for row in alldate:
    print("員工姓名:",row[0])
    print("工作項目:",row[1])
    print("工作詳述:",row[2])
   

db1.conn.close()