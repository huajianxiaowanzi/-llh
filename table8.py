from pyhive import hive
conn = hive.Connection(host='192.168.128.140',port=10000,username='root')

import pymysql
con=pymysql.connect(host='rm-bp1a02s4h8x3o8j98to.mysql.rds.aliyuncs.com',password='Zhx20020611',port=3306,
                    user='mysqltest',charset='utf8',database='mysqltest')


#导入pymysql
#
cur=con.cursor()

# cursor = conn.cursor()
# cursor.execute('select count(distinct fund_name) from data_102 where this_year>=-10 and this_year<-5')
# for result in cursor.fetchall():
#     if result[0]!=None:
#         print(result)
insert_emp_sql = "insert into table8 (range_thisyear,count) values ('5_10',23)"
cur.execute(insert_emp_sql)
con.commit()
cur.close()
con.close()