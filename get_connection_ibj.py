import pymysql

connect = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password ='ki2357968',
    db = 'shop',
    charset = 'utf8'
)

print(dir(connect))