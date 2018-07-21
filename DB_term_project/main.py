import pymysql.cursors


def send_query(query, values, is_delete=False):
    connection = pymysql.connect(
        host='147.46.215.246',
        port=33060,
        # user='jaeki.hong@gmail.com',
        # password='ghddnwls',
        # db='ds2_db10',
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

# --------------------------------------------------------
# MySQL DB Class
# --------------------------------------------------------
class MysqlDB:

    ClassConnection = None
    
    def __init__(self):
        self.connection = MysqlDB.ClassConnection
    
    @classmethod 
    def OpenDB(cls):

        MysqlDB.ClassConnection = pymysql.connect(

            host='147.46.215.246',

            port=33060,

            user='konlona@gmail.com',

            password='dbintro',

            db='ds2_db15',

            charset='utf8',

            cursorclass=pymysql.cursors.DictCursor)

        result = None


    @classmethod
    def CloseDB(cls):
        MysqlDB.ClassConnection.close()

    @classmethod
    def ResetDB(cls):
        sql = """
                DROP TABLE Building;
                DROP TABLE Performance;
                DROP TABLE Audience;
                DROP TABLE Booking;
                DROP TABLE Assign;
                
                
                create table Building(
                    BID int auto_increment primary key,
                    BName varchar(200) not null,
                    BLocation varchar(200) not null,
                    BMax int,
                    check (BMax >= 1)
                );

                create table Performance (
                    PID int auto_increment primary key,
                    PName varchar(200),
                    PType varchar(200),
                    PPrice int,
                    check (PPrice >= 0)
                );

                create table Audience(
                    AID int auto_increment Primary key,
                    AName varchar(200),
                    AGender char(1),
                    AAge int ,
                    check (AGender in ('M', 'F')),
                    check (AAge >=1)
                );

                create table Booking(
                    PID int ,
                    AID int ,
                    SeatNo int,
                    foreign key (PID) references Performance(PID) ON DELETE cascade,
                    foreign key (AID) references Audience(AID) ON DELETE cascade
                );

                create table Assign(
                    PID int,
                    BID int,
                    foreign key (PID) references Performance(PID) on delete cascade,
                    foreign key (BID) references Building(BID) on delete cascade
                ) """
        
        print(sql)
        #with MysqlDB.ClassConnection.cursor() as cursor:
        #    cursor.execute(sql)
        #    MysqlDB.ClassConnection.commit()
            

    def SendQuery(self, sql):

        with self.connection.cursor() as cursor:

            cursor.execute(sql)

            result = cursor.fetchall()
        return result


    # insert, delete, create table, drop

    def ExecuteQuery(self, sql):

        with self.connection.cursor() as cursor:

            cursor.execute(sql)

            self.connection.commit()
            
        
# --------------------------------------------------------
# JK Hong
# --------------------------------------------------------
class Performance(MysqlDB):
    def __init__(self):
        self.sql = "test"
        MysqlDB.__init__(self)

    def insert_performance(self):
        self.name = input("Performance name: ")
        self.type = input("Performance type: ")
        self.price = int(input("Performance price: "))
        self.sql = "INSERT INTO Performance VALUES (NULL, %s, %s, %s);"
        send_query(self.sql, (self.name, self.type, self.price), True)

    def remove_performance(self):
        self.p_id = int(input("Performance ID: "))
        self.sql = "DELETE FROM Performance WHERE PID=%s"
        send_query(self.sql, (self.p_id,))
        self.sql = "DELETE FROM Booking WHERE PID=%s"
        send_query(self.sql, (self.p_id,))
        # error handling is necessary

    def assign_performance(self):
        self.building_id = int(input("Building ID: "))
        self.p_id = int(input("Performance ID: "))
        self.sql = "INSERT INTO Assign VALUES (%s %s)"
        send_query(self.sql, (self.p_id, self.building_id))
        Print("Successfully assign a performance")

    def print_assigned_performance(self):
        self.building_id = int(input("Building ID: "))
        self.sql = "SELECT PID, PName, PType, PPrice FROM Performance, Building WHERE BID=%s"
        send_query(self.sql, (self.building_id,))


#--------------------------------------------------------
# konlo 공연장 class
#--------------------------------------------------------
class Building(MysqlDB):
    TableName = 'Building'
    cHyphen = "--------------------------------------------------------------------------------"
    #cPrintFormat = "id\10t name\20t location\10t captity\10t assinged"
    cPrintFormat = "{0:3}   {1:15}   {2:30}   {3:7}   {4:8}"
    
    def __init__(self):
        self.BID = None
        self.BName = None
        self.BLocation = None
        self.BMax = 0
        super().__init__()
        
    def GetSQLAll(self):
        return ("select * from %s" % Building.TableName)

    def insert_building(self):
        strBuildingName     = input("Building name: ").replace("'", "\\'")
        strBuildingLocation = input("Building location: ").replace("'", "\\'")

        # CapMax는 number가 되도록 한다. 
        CapMax = ''
        while CapMax.isdigit() == False:            
            CapMax = input("Building capacity (number) : ")

        CapMax = int(CapMax)
        sql = ("insert into Building (BName, BLocation, BMax)"
                "values('%.199s', '%.199s', %s)" % (strBuildingName, strBuildingLocation, CapMax))
        self.ExecuteQuery(sql)     

    def remove_building(self):
        BID = ''
        while BID.isdigit() == False:            
            BID = input("input building ID (number) : ")
            
        BID = int(BID)
        # check BID in DB
        # 있는 경우만 삭제함 
        if self.check_BID_building(BID) :               
            sql = ("delete from Building where BID=%s" % BID )
            self.ExecuteQuery(sql)
        # 없는 경우는 에러 메시지 출력 
        else:
            print("!! Error : BID %d does not exist in building database, please check it again" % BID)

    # 해당하는 BID가 있는지 검사한다. 
    def check_BID_building(self, BID):
        sql = (" select BID from Building where BID=%s order by BID" % BID)
        result = self.SendQuery(sql)
        if len(result) > 0:
            return True
        else:
            return False
                        
    def print_building(self):
        sql = "select * from Building"
        result = self.SendQuery(sql)
        
        print(Building.cHyphen)
        print(Building.cPrintFormat.format("id", "name", "location", "captity", "assinged"))
        print(Building.cHyphen)
        
        for row in result:
            print(Building.cPrintFormat.format(row["BID"], row["BName"], row["BLocation"], row["BMax"], "assinged"))
            
        print(Building.cHyphen)
            
# --------------------------------------------------------
# rkdsktmf
# --------------------------------------------------------
class Audience:
    def __init__(self):
        self.sql = "test"

    def print_aud(self):
        self.sql = "select AID, AName, AGender, AAge from Audience"
        result = g_IloveDB.SendQuery(self.sql)
        for i in range(len(result)):
            temp = list(result[i].values())
            print(temp)

    def insert_aud(self):
        a = 1
        while (a > 0):
            AName = input("Audience Name : ")
            break

        while (a > 0):
            Afm = input("Male / Female (M/F) : ")
            if Afm == 'M' or Afm == 'F':
                break
            elif Afm == 'm' or Afm == 'f':
                Afm = Afm.upper()
                break
            else:
                print("입력이 잘못되었습니다. 다시 입력해 주세요.")

        while (a > 0):
            AAge = input("Audience Age : ")
            if int(AAge) > 0:
                break
            else:
                print("입력이 잘못되었습니다. 다시 입력해 주세요.")

        self.sql = ("insert into Audience(AName, AGender, AAge) values ('%s', '%s', %s)"% (AName, Afm, AAge))
        print(self.sql)
        g_IloveDB.ExecuteQuery(self.sql)

    def remove_aud(self):
        a = 1
        self.sql = "select AID from Audience"
        result = g_IloveDB.SendQuery(self.sql)
        for i in range(len(result)):
            temp = list(result[i].values())
            print(temp)

        while (a > 0):
            AID = int(input("Delete ID : "))
            break

        self.sql = ("delete from Audience where AID = %s" % (AID))
        g_IloveDB.ExecuteQuery(self.sql)

    def book_aud(self):

        self.sql = "select AID from Audience"
        dbAID = g_IloveDB.SendQuery(self.sql)
        AIDlist = []
        for i in range(len(dbAID)):
            AIDlist  = AIDlist + list(dbAID[i].values())

        self.sql = "select PID from Performance"
        dbPID = g_IloveDB.SendQuery(self.sql)
        PIDlist = []
        for i in range(len(dbPID)):
            PIDlist  = PIDlist + list(dbPID[i].values())

        print("Audience ID list : ")
        print(AIDlist)
        print("Performance ID list : ")
        print(PIDlist)

        a = 1
        while (a>0):
            AID = input("Audience ID : ")
            for i in range(len(AIDlist)):
                if AIDlist[i] == AID:
                    a = 0
                    break
                else:
                    print("w")

        a = 1
        while (a>0):
            PID = input("Preformance ID : ")
            for i in range(len(PIDlist)):
                if PIDlist[i] == PID:
                    a = 0
                    break


        self.sql = ("select SeatNo from Booking where PID = %s" % (PID))
        dbSeatNo = g_IloveDB.SendQuery(self.sql)
        Seatlist = []
        for i in range(len(result)):
            Seatlist  = Seatlist + list(dbSeatNo[i].values())
        a = 1
        while (a>0):
            SeatNo = list(input("Seat Number : "))

            for i in range(len(SeatNo)):
                for j in range(len(Seatlist)):
                    if Seatlist[j] == SeatNo[i]:
                        print("Seat Number is duplicate. Please check Seat Number.")
                        a = 0
                        break

        self.sql = ("insert into Booking(PID, AID, SeatNo) values ('%s', '%s', %s)" % (PID, AID, SeatNo))
        print(self.sql)
        g_IloveDB.ExecuteQuery(self.sql)

    def print_book(self):
        pass


def menu1():
    pass


# print all performance JK Hong
def menu2():
    pass


def menu3():
    Aud = Audience()
    Aud.print_aud()


def menu4():
    pass


def menu5():
    pass


# insert a new performand JK Hong
def menu6():
    perf = Performance()
    perf.insert_performance()


# remove a performance JK Hong
def menu7():
    perf = Performance()
    perf.remove_performance()


def menu8():
    Aud = Audience()
    Aud.insert_aud()


def menu9():
    Aud = Audience()
    Aud.remove_aud()


# assign a performance to a building JK Hong
def menu10():
    perf = Performance()
    perf.assign_performance()


def menu11():
    Aud = Audience()
    Aud.book_aud()


# print all performances which is assigned to a building JK Hong
def menu12():
    perf = Performance()
    perf.print_assigned_performance()


def menu13():
    Aud = Audience()
    Aud.print_book()


def menu14():
    pass


def menu16():
    pass


def main():
    x = 1

    # building을 위한 객체 생성
    cBuilding = Building()
    while (x > 0):
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
            # menu1()
            # building list 출력함
            cBuilding.print_building()
        elif sel == '2':
            menu2()
        elif sel == '3':
            menu3()
        # 4. insert a new building
        elif sel == '4':
            cBuilding.insert_building()
            menu4()
        # 5. remove a building
        elif sel == '5':
            # menu5()
            cBuilding.remove_building()
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
            #menu16()
            if input("Really want to reset database ? (y/n) : ") == 'y':
                MysqlDB.ResetDB()
        else:
            print("Invalid menu number, Please check the menu number.")


if __name__ == "__main__":
    # class metho를 이용하여 DB Open를 수행한다.
    MysqlDB.OpenDB()
    g_IloveDB = MysqlDB()

    #    g_IloveDB.OpenDB()

    main()

    # Main 함수가 종료되었을 때 DB를 close 한다.
    TestClass = MysqlDB()

#    g_IloveDB.CloseDB()
