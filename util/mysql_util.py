#!/usr/bin/python3

import pymysql.cursors

# 打开数据库连接
class MySqlUtil:
    def __init__(self):
        self.pmc = pymysql.connect(
                             host='localhost',
                             user='root',
                             password='wang7364',
                             database='test_wangpeng',
                             cursorclass = pymysql.cursors.DictCursor
        )
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cur=self.pmc.cursor()

    def get_sql(self,sql):
        self.cur.execute(sql)
        resuit = self.cur.fetchone()
        self.cur.close()
        return resuit

if __name__ == '__main__':
    mysqlutil =MySqlUtil()
    sql = "select * from student"
    print(mysqlutil.get_sql(sql))





