import pymysql.cursors


class MysqlDB:
    def __init__(self):
        self.connection = None
    def OpenDB(self):
        self.connection = pymysql.connect(
            host='147.46.215.246',
            port=33060,
            user='rkdsktmf@naver.com',
            password='dbintro',
            db='ds2_db22',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)
        result = None

    def CloseDB(self):
        self.connection.close()

    def SendQuery(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()

    # insert, delete, create table, drop
    def ExecuteQuery(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            self.connection.commit()

class Performance:
    pass

class Building:
    pass

class Audience(MysqlDB):
    def __init__(self):
        self.sql = "test"
        #self.connection = None
        MysqlDB.__init__(self)
        #super().__init__()

    def print_aud(self):

        self.sql = "select AID, AName, AGender, AAge from Audience"
        print(self.sql)
        result = MysqlDB.SendQuery(self, self.sql)
        #result = self.SendQuery(self.sql)

        return result



    def insert_aud(self):
        pass

    def remove_aud(self):
        pass

    def book_aud(self):
        pass

    def print_book(self):
        pass


def menu1():
    pass

def menu2():
    pass

def menu3():
    Audprint = Audience()
    Audprint.print_aud()
    print(Audprint)

def menu4():
    pass

def menu5():
    pass

def menu6():
    pass

def menu7():
    pass

def menu8():
    Audience.insert_aud()

def menu9():
    Audience.remove_aud()

def menu10():
    pass

def menu11():
    Audience.book_aud()

def menu12():
    pass

def menu13():
    Audience.print_book()

def menu14():
    pass

def menu16():
    pass

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
    g_IloveDB = MysqlDB()
    g_IloveDB.OpenDB()

    main()
    g_IloveDB.CloseDB()
