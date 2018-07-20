import pymysql.cursors
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



def send_query(query, values, is_delete=False):
    connection = pymysql.connect(
        host='s.snu.ac.kr',
        user='C2',
        password='ghddnwls',
        db='C2',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)
    result = None

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            if is_delete:
                connection.commit()
            else:
                result = cursor.fetchall()
    finally:
        connection.close()
    return result

def delete_tuple(values):
    sql = "DELETE from takes where stu_id=%s and grade=%s;"
    send_query(sql, values, is_delete=True)

def select_tuple(values):
    sql = "SELECT * FROM takes where stu_id=%s and grade=%s;"
    result = send_query(sql, values, is_delete=False)
    print(result)

def find_parents(lst_id):
    # print(lst_id)
    sql = "SELECT * FROM parentship WHERE child = %s;"
    result = send_query(sql, (lst_id,))
    return result

def find_father(lst_id):

    pass

def find_brothers(lst_id):
    pass

def find_children(lst_id):
    pass

def find_cousins(id):
    father_id = find_father(id)
    return find_brother(father_id)


def main():
    # id = input("사람의 ID를 입력해 주세요.:") # 1292003
    # lst = find_cousins(id)
    result = find_parents(580)
    print(result)

if __name__=="__main__":
    main()
