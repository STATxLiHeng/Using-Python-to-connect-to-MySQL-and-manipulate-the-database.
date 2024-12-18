import pymysql

connect = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password ='ki2357968',
    db = 'shop',
    charset = 'utf8',
    cursorclass=pymysql.cursors.DictCursor
)

# 獲取游標
try:
    with connect.cursor() as cursor:
        sql = 'select * from goods'
    # 執行
        cursor.execute(sql)
        result = cursor.fetchall( )
except Exception as e:
    print(e)
finally:
    connect.close()
# 獲取數據

print(result)

for i in result:
    print(f'商品名稱:{i["name"]},價格:{i["price"]}')
