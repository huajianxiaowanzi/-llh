from pyhive import hive
conn = hive.Connection(host='192.168.128.140',port=10000,username='root')

import pymysql
con=pymysql.connect(host='rm-bp1a02s4h8x3o8j98to.mysql.rds.aliyuncs.com',password='Zhx20020611',port=3306,
                    user='mysqltest',charset='utf8',database='mysqltest')


#导入pymysql
#
cur=con.cursor()

cursor = conn.cursor()
cursor.execute('select fund_type,fund_name,this_year from data_102 where fund_type="货币型" order by this_year desc limit 10')
for result in cursor.fetchall():

    if result[1]!='this_year':
        print(result)
        # insert_emp_sql = "insert into table11 (fund_type,fund_name,this_year) values "+str(result)
        # cur.execute(insert_emp_sql)
con.commit()
cur.close()
con.close()
