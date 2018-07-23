import pymysql.cursors

def menu1():
    with connection.cursor() as cursor:
        sql = ""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

def menu2():
    with connection.cursor() as cursor:
        sql = ""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

def menu3():
    with connection.cursor() as cursor:
        sql = "select AID, AName, AGender, AAge from Audience"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

def menu4():
    with connection.cursor() as cursor:
        sql = ""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

def menu5():
    with connection.cursor() as cursor:
        sql = ""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

def menu6():
    with connection.cursor() as cursor:
        sql = ""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

def menu7():
    with connection.cursor() as cursor:
        sql = ""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

def menu8():
    a=1
    while (a > 0):
        AName = input("Audience Name : ")
        break

    while (a>0):
        Afm = input("Male / Female (M/F) : ")
        if Afm == 'M' or Afm == 'F':
            break
        elif Afm == 'm' or Afm == 'f':
            Afm.upper()
            break
        else:
            print("입력이 잘못되었습니다. 다시 입력해 주세요.")

    while (a > 0):
        AAge = input("Audience Age : ")
        if int(AAge) > 0:
            break
        else:
            print("입력이 잘못되었습니다. 다시 입력해 주세요.")

    with connection.cursor() as cursor:
        sql = "insert into Audience(AName, AGender, AAge) values (%s, %s, %s)"
        cursor.execute(sql, (AName, Afm, int(AAge)))
        connection.commit()


def menu9():
    with connection.cursor() as cursor:
        sql = ""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

def menu10():
    with connection.cursor() as cursor:
        sql = ""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

def menu11():
    with connection.cursor() as cursor:
        sql = ""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

def menu12():
    with connection.cursor() as cursor:
        sql = ""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

def menu13():
    with connection.cursor() as cursor:
        sql = ""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

def menu14():
    with connection.cursor() as cursor:
        sql = ""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

def menu16():
    with connection.cursor() as cursor:
        sql = ""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

def main():
    x = 1
    while (x>0):
        print("1. print all buildings")
        print("2. print all performances")
        print("3. print all audiences")
        print("4. insert a new building")
        print("5. remove a building")
        print("6. insert a new performance")
        print("7. remove a performance")
        print("8. insert a new audience")
        print("9. remove an audience")
        print("10. assign a performance to a building")
        print("11. book a performance")
        print("12. print all performances which assigned at a building")
        print("13. print all audiences who booked for a performance")
        print("14. print ticket booking status of a performance")
        print("15. exit")
        print("16. reset database")

        sel = input("select : ")
        if sel == '1':
            menu1()
        elif sel == '2':
            menu2()
        elif sel == '3':
            menu3()
        elif sel == '4':
            menu4()
        elif sel == '5':
            menu5()
        elif sel == '6':
            menu6()
        elif sel == '7':
            menu7()
        elif sel == '8':
            menu8()
        elif sel == '9':
            menu9()
        elif sel == '10':
            menu10()
        elif sel == '11':
            menu11()
        elif sel == '12':
            menu12()
        elif sel == '13':
            menu13()
        elif sel == '14':
            menu14()
        elif sel == '15':
            break
        elif sel == '16':
            menu16()
        else:
            print("입력이 잘못되었습니다. 다시 입력해주세요.")



if __name__ == "__main__":

    connection = pymysql.connect(
        host='s.snu.ac.kr',
        user='A2',
        password='kns',
        db='A2',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)
    result = None
    try:
        main()
    finally:
        connection.close()