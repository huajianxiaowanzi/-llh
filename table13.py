from pyhive import hive
conn = hive.Connection(host='192.168.128.140',port=10000,username='root')

import pymysql
con=pymysql.connect(host='rm-bp1a02s4h8x3o8j98to.mysql.rds.aliyuncs.com',password='Zhx20020611',port=3306,
                    user='mysqltest',charset='utf8',database='mysqltest')


#导入pymysql
#
fund_name_list = []
cur=con.cursor()

cursor = conn.cursor()
cursor.execute('select name,avg(femoral_age),count(*),sum(buy) from data_102 where year_come>20 and risk_level="高" group by name ')
for result in cursor.fetchall():
    if result[0]!='fund_name':
        print(result)
        if int(result[1])>5 and int(result[2])>10 and int(result[3])>80000:
            print(1)
            s = "'" + result[0] + "'"
            insert_emp_sql = "insert into table13 (user_temp_name,user_level) values ("+s+", '重点客户')"
            cur.execute(insert_emp_sql)
        elif int(result[1])>3 and int(result[2])>5 and int(result[3])>60000:
            print(2)
            s = "'"+result[0]+"'"
            insert_emp_sql = "insert into table13 (user_temp_name,user_level) values ("+s+", '潜在客户')"
            cur.execute(insert_emp_sql)
        else:
            print(2)
            s = "'" + result[0] + "'"
            insert_emp_sql = "insert into table13 (user_temp_name,user_level) values (" + s + ", '普通客户')"
            cur.execute(insert_emp_sql)
    else:
        pass


con.commit()
cur.close()
con.close()
