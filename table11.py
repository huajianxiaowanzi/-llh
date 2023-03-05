from pyhive import hive
import random
conn = hive.Connection(host='192.168.128.140',port=10000,username='root')

import pymysql
con=pymysql.connect(host='rm-bp1a02s4h8x3o8j98to.mysql.rds.aliyuncs.com',password='Zhx20020611',port=3306,
                    user='mysqltest',charset='utf8',database='mysqltest')


#导入pymysql
#
cur=con.cursor()

cursor = conn.cursor()
#select * from data_102 where
cursor.execute("select fund_type,avg(rate) from data_102 where data like '2023%' group by fund_type")
data =[-0.041,-0.04610,-0.0773,0.02459,0.1041855,-0.03486,0.02432]
print(cursor.fetchall()[4])
# for re in cursor.fetchall():
#     data.append(re)
# print(data)

cursor.execute("select fund_name,avg(rate) from data_102 where data like '2023%' group by fund_name")
#cursor.execute("select data,rate,fund_name from data_102 where data=(select data from data_102 where data like '2023%')")
for result in cursor.fetchall():
    if result[0]!='premium':
        print(result)
        data1 = random.choice(data)
        if data1<result[1]:
            s = "'" + result[0] + "'"
            insert_emp_sql = "insert into table_11 (company_name,short_rate) values ("+s+", '推荐购入')"
            cur.execute(insert_emp_sql)
        else:
            s = "'" + result[0] + "'"
            insert_emp_sql = "insert into table_11 (company_name,short_rate) values (" + s + ", '不推荐购入')"
            cur.execute(insert_emp_sql)

con.commit()
cur.close()
con.close()

# ('FOF型', -0.0418168709444841)
# ('QDLL型', -0.04610391154440606)
# ('债券型', -0.07739564752051403)
# ('指数型', 0.02459494721859768)
# ('混合型', 0.10418551765409947)
# ('股票型', -0.03486859011797678)
# ('货币型', 0.02432795060555708)