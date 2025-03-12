import pymysql

class DataBase:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',user='root',password='M@m@rsh!a1384_',database='university',autocommit=True)
        self.cur = self.conn.cursor()
    def reset_cursor(self):
        self.cur.close()
        self.cur = self.conn.cursor()