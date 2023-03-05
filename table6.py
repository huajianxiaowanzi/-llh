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
cursor.execute('select distinct fund_name,data_fund,data_company,count_fund,manage_scale from data_102 ')
for result in cursor.fetchall():
    if result[0]!='fund_name':
        print(result)
        if result[0] not in fund_name_list:
            fund_name_list.append(result[0])
            print(str(result[0]))
            if int(result[1][2:4])<17 and int(result[2][2:4])<12 and int(result[3])>20 and int(result[4])>20:
                print(1)
                s = "'" + result[0] + "'"
                insert_emp_sql = "insert into table6 (company_name,long_rate) values ("+s+", '建议长期持有')"
                cur.execute(insert_emp_sql)
            else:
                print(2)
                print("'"+result[0]+"'")
                s = "'"+result[0]+"'"
                insert_emp_sql = "insert into table6 (company_name,long_rate) values ("+s+", '不建议长期持有')"
                cur.execute(insert_emp_sql)
        else:
            pass


con.commit()
cur.close()
con.close()
