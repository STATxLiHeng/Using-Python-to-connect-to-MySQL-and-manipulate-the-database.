import traceback
import pymysql

class MysqlUtil():
    def __init__(self):
        self.host = 'localhost',
        self.user = 'root',
        self.password = 'ki2357968',
        self.db = 'student_system',
        self.charset = 'utf8'
        self.connect()

    def connect(self):
        self.connection=pymysql.connect(
            host='localhost',
            user='root',
            password='ki2357968',
            db='student_system',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )

    def execute(self,sql):
        '''
        執行增刪改
        :param sql:  Sql語法
        :return:  影響記錄條數
        '''
        try:
            with self.connection.cursor() as cursor:
                result = cursor.execute(sql)
            self.connection.commit()
            return result
        except:
            self.traceback()
            self.connection.rollback()


    def find(self,sql,fetch_one=False):
        '''
        查找紀錄
        :param sql: SQL語法
        :param fetch_one:  BOOL True 查找一條, False: 多條
        :return: 結果
        '''
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                if fetch_one:
                    result = cursor.fetchone()
                else:
                    result = cursor.fetchall()
                return result
        except:
            self.traceback()


    def traceback(self):
        with open('log.txt', 'a') as file:
            traceback.print_exc(file=file)
            file.flush()

    def close(self):
        if getattr(self,"connection",0):
            self.connection.close()

    def __del__(self):
        self.close()

if __name__ == "__main__":
    db = MysqlUtil()
    sql = 'select version()'
    result = db.find(sql)
    print(result)

