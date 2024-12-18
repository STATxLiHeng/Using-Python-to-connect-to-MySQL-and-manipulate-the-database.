from mysql_utl import MysqlUtil
import beautifultable

def confirmed():
    check = input("請輸入y: ")
    if check != "y":
        return False
    else:
        return True

def show_menu():
    mes = '''
---------------------------
 學生管理系統 V1.0
    1: 添加學生
    2: 查詢學生
    3: 顯示所有學生
    4: 刪除學生
    5: 修改學生
    6: 總分成績排名
    7: 單科成績排名
    8: 查詢單科成績(最高/低/平均)
    0: 退出系統 
---------------------------
        '''
    print(mes)

def print_table(column_headers=None,rows_value = None):
    table = beautifultable.BeautifulTable()
    table.column_headers = column_headers
    if isinstance(rows_value,list):
        for student in rows_value:
            table.append_row(student.values())
    else:
        table.append_row(rows_value.values())
    print(table)

def get_student_info(student_number):
    sql = f"select {fields} from student  where student_number = {student_number}"
    result = db.find(sql, fetch_one=True)
    return result


def main():
    show_menu()

    while True:
        number = int(input("請輸入功能號碼:"))
        if number == 1:
            student_number = input("請輸入學號: ")
            student_name = input("請輸入姓名: ")
            chinese = input("請輸入語文成績: ")
            math = input("請輸入數學成績: ")
            english = input("請輸入英文成績: ")
            values = (student_number,student_name,chinese,math,english)
            sql = f'insert into student({fields}) values {values}'
            if not confirmed():
                continue
            # print(sql)
            result = db.execute(sql)
            result = "添加成功" if result else "添加失敗"
            print(result)

        elif number == 2:
            student_number = input("請輸入學號: ")
            result=get_student_info(student_number)
            if result:
                # table = beautifultable.BeautifulTable()
                # table.column_headers = fields.split(",")
                # table.append_row(result.values())
                # print(table)
                print_table(fields.split(","),result)
            else:
                print("學號不存在")

        elif number == 3:
            sql = f"select {fields} from student"
            result = db.find(sql,fetch_one=False)
            if result:
                print_table(fields.split(","), result)
            else:
                print("學生不存在")

        elif number == 4: # 刪除
            student_number = input("請輸入學號: ")
            if not get_student_info(student_number):
                print("學號不存在")
                continue
            sql =f"delete from student where student_number = {student_number}"
            if not confirmed():
                continue
            result = db.execute(sql)
            result = "刪除成功" if result else "刪除失敗"
            print(result)

        elif number == 5:
            student_number = input("請輸入學號: ")
            if not get_student_info(student_number):
                print("學號不存在")
                continue
            item = input("更改的科目(chinese/math/english): ")
            value = input("改為幾分")
            sql =f"UPDATE student set {item} = {value} where  student_number = {student_number}"
            if not confirmed():
                continue
            result = db.execute(sql)
            result = "修改成功" if result else "修改失敗"
            print(result)

        elif number == 6:
            total_fields = ",".join((fields ,'chinese+math+english as total'))
            order_by = 'total desc'
            sql = f'select {total_fields} from student order by {order_by}'
            result = db.find(sql)
            if result:
                # table = beautifultable.BeautifulTable()
                # table.column_headers = total_fields.split(",")
                # for student in result:
                #     table.append_row(student.values())
                # print(table)
                print_table(total_fields.split(","), result)
            else:
                print("學生不存在")
        elif number == 7:
            item = input("查詢科目")
            sql = f"select {fields} from student order by {item}"
            result = db.find(sql, fetch_one=False)
            if result:
                # table = beautifultable.BeautifulTable()
                # table.column_headers = fields.split(",")
                # for student in result:
                #     table.append_row(student.values())
                # print(table)
                print_table(fields.split(","), result)
            else:
                print("學生不存在")
        elif number == 8:
            item = input("查詢科目")
            sql = f"select MAX({item}) as Highest, Min({item}) as Lowest, AVG({item}) as Average from student"
            result = db.find(sql, fetch_one=True)
            if result:
                table = beautifultable.BeautifulTable()
                table.column_headers = ["最高分","最低分","平均分"]
                table.append_row(result.values())
                print(table)
            else:
                print("學生不存在")
        elif number == 0:
            print("退出成功")
            break
        else:
            print("輸入無效")


if __name__ == "__main__":
    db = MysqlUtil()
    fields = 'student_number,student_name,chinese,math,english'
    main()