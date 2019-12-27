#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pymysql

find_count = 0
data_len = 0
db= pymysql.connect(host="127.0.0.1",user="root",password="root",db="exam",port=3306)
cur = db.cursor()

cookie = '''ga=GA1.3.1525105060.1550119542; gr_user_id=bea89f8f-d77a-43d0-8fa0-92929ded63ab; grwng_uid=d6e5fb33-a12b-445f-9afc-a1f901617fed; 8a762667df5cb9d5_gr_last_sent_cs1=567465; 8a762667df5cb9d5_gr_cs1=567465; MoodleSession=a9f1b4d22dc8059c89ef4354b1f1ea14'''
header = {
'Cookie': cookie}
url = 'http://moodle.zjnu.edu.cn/mod/quiz/review.php?attempt=205164&cmid=22003&showall=1'
wbdata = requests.get(url,headers=header).text
soup = BeautifulSoup(wbdata,features='lxml')
qtext = soup.find_all('div', {"class": "qtext"})
answer = soup.find_all('div', {"class": "answer"})
rightanswer = soup.find_all('div', {"class": "rightanswer"})
for i in range(0,78):
    sql_select = "SELECT rightanswer from problems where qtext = '%s'" % qtext[i].get_text()
    cur.execute(sql_select)
    result = cur.fetchall()
    if result:
        find_count +=1
    else:
        sql_insert = "insert into problems(qtext,answer,rightanswer) values('%s','%s','%s')" % (qtext[i].get_text(), answer[i].get_text(),rightanswer[i].get_text())
        cur.execute(sql_insert)
        db.commit()
db.close()
print("数据库中查询到"+str(find_count)+"条记录")
print("数据库成功插入"+str(78-find_count)+"条记录")




