import pymysql

connect = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password ='ki2357968',
    db = 'shop',
    charset = 'utf8'
)

# 獲取游標
with connect.cursor() as cursor:
# cursor = connect.cursor()
# print(cursor)
#SQL
    sql = """
    create table test_py (
    id int auto_increment primary key,
    name varchar(255) not null);
    """
# 執行
    cursor.execute(sql)

    connect.commit()

# 獲取數據
# result=cursor.fetchone()
#print(result)

# 關閉游標
cursor.close()

# 關閉連結
connect.close()