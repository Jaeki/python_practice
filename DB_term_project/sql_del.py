import pymysql.cursors

# Connect to the database

def send_query(query, values, is_delete=False):
    connection = pymysql.connect(
        host='s.snu.ac.kr',
        user='G4',
        password='G4',
        db='G4',
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

def main():
    s_id = input("삭제할 s_id를 입력해 주세요.:") # 1292003
    grade = input("삭제할 grade를 입력해 주세요.:") # C

    values = []
    values.append(s_id)
    values.append(grade)

    print('Select table...')
    select_tuple(values)
    print('Delete table...')
    delete_tuple(values)
    print('Select table...')
    select_tuple(values)

if __name__=="__main__":
    main()
