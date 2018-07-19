import pymysql.cursors
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

connection = pymysql.connect(
    host='s.snu.ac.kr',
    user='C2',
    password='ghddnwls',
    db='C2',
    charset='utf8',
    cursorclass = pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        #sql = "SELECT * FROM student"
        sql1 = "SELECT stu_id, resident_id FROM student"
        sql2 = "SELECT name, year_emp FROM professor \
                WHERE year_emp > (select year_emp from professor where name = '최성희')"
        sql3 = ("SELECT * "
                " FROM student natural join takes join class"
                " ON takes.class_id = class.class_id"
                " NATURAL JOIN course"
                " where name = %s")
        #cursor.execute(sql1)
        #cursor.execute(sql2)
        cursor.execute(sql3, '김현정')
        result = cursor.fetchall()
finally:
    connection.close()

for row in result:
    print(row["title"] + "\t" + row["grade"])
