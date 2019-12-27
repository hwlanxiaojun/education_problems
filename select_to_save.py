#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
db= pymysql.connect(host="127.0.0.1",user="root",password="root",db="exam",port=3306)
cur = db.cursor()
f = open('E:/out.txt', mode='a', encoding='utf-8')
sql_select = "SELECT qtext,answer,rightanswer from problems"
cur.execute(sql_select)
result = cur.fetchall()
data_len = len(result)
for i in range(0,data_len):
    f.write(str(i+1)+'. ')
    for j in result[i]:
        f.write(j+'\n')
f.close()