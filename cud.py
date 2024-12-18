import pymysql

connect = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password ='ki2357968',
    db = 'shop',
    charset = 'utf8'
)

# data = [('0','1+手機','2999','New one',1,'2020-02-23'),
#         ('0','2+手機','2999','New one',1,'2020-02-24'),
#         ('0','3+手機','2999','New one',1,'2020-02-25')]
# 獲取游標
with connect.cursor() as cursor:
# cursor = connect.cursor()
# print(cursor)
#SQL
    # sql = """
    # insert into goods values(%s,%s,%s,%s,%s,%s)
    # """
    sql = 'update goods set name = "改了喔" where id = 24'
    sql = 'delete from  goods  where id = 24'
# 執行
#     cursor.executemany(sql,data)
    cursor.execute(sql)

    connect.commit()

# 獲取數據
# result=cursor.fetchone()
#print(result)

# 關閉游標
cursor.close()

# 關閉連結
connect.close()