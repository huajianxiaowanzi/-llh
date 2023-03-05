from pyhive import hive
conn = hive.Connection(host='192.168.128.140',port=10000,username='root')

import pymysql
con=pymysql.connect(host='rm-bp1a02s4h8x3o8j98to.mysql.rds.aliyuncs.com',password='Zhx20020611',port=3306,
                    user='mysqltest',charset='utf8',database='mysqltest')


#导入pymysql
#
cur=con.cursor()

cursor = conn.cursor()
cursor.execute('select dividends,count(distinct fund_name) from data1_csv group by dividends')
for result in cursor.fetchall():
    if result[0]!='dividends':
        print(result)
        insert_emp_sql = "insert into table10 (dividends,count) values (%f,%d)"%(int(result[0]),int(result[1]))
        cur.execute(insert_emp_sql)
con.commit()
cur.close()
con.close()
