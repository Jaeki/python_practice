import pymysql.cursors

PRINT_HYPHEN = "--------------------------------------------------------------------------------"

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
    TableName = 'Performance'
    cHyphen = "--------------------------------------------------------------------------------"
    # cPrintFormat = "id\10t name\20t type\10t price\10t booked"
    cPrintFormat = "{0:3}   {1:30}   {2:15}   {3:10}   {4:6}"

    def __init__(self):
        super().__init__()

    def insert_performance(self):
        name = input("Performance name: ")
        type = input("Performance type: ")
        try:
            price = int(input("Performance price: "))
            #DB의 integer 형 데이터 max 값 확인
            if price > 2147483647:
                raise ValueError('Out of integer range in DB system')
        except:
            print("!! Error : Invalid price value, Please check it again.")
            return
        sql = "INSERT INTO Performance (PName, PType, PPrice) VALUES ('%s', '%s', %s);"  % (name, type, price)
        # print(sql)
        self.ExecuteQuery(sql)

    def remove_performance(self):
        p_id = int(input("Performance ID: "))
        sql = "SELECT PID FROM Performance WHERE PID=%s" % p_id
        result = self.SendQuery(sql)
        # print(result)
        if len(result) > 0:
            sql = "DELETE FROM Performance WHERE PID=%s" % p_id
            self.ExecuteQuery(sql)
            # sql = "DELETE FROM Booking WHERE PID=%s" % p_id
            # self.ExecuteQuery(sql)
        else:
            print("!! Error : Performance ID %d does not exist in Performance database, Please check it again" % p_id)

    def assign_performance(self):
        building_id = int(input("Building ID: "))
        p_id = int(input("Performance ID: "))
        sql = "SELECT PID FROM Assign WHERE PID=%s" % p_id
        result = self.SendQuery(sql)
        if len(result) == 0:
            sql = "INSERT INTO Assign VALUES (%s, %s)" % (p_id, building_id)
            self.ExecuteQuery(sql)
            print("Successfully assign a performance")
        else:
            print("!! Error : Performance ID %d is already assigned, Please check it again" % p_id)

    def print_assigned_performance(self):
        building_id = int(input("Building ID: "))
        sql = "SELECT Performance.PID, PName, PType, PPrice FROM Performance left join Assign using(PID) WHERE Assign.BID=%s" % building_id
        # print(sql)
        result = self.SendQuery(sql)
        if len(result) == 0:
            print("!! Error : Any performance is not assigned to Building ID %d, Please check it again" % building_id)
        else:
            print(Performance.cHyphen)
            print(Performance.cPrintFormat.format("id", "name", "type", "price", "booked"))
            print(Performance.cHyphen)

            for row in result:
                sql = "SELECT count(PID) from Booking Where PID=%s" % row["PID"]
                result = self.SendQuery(sql)
                # print(result[0].get('count(PID)'))
                print(Performance.cPrintFormat.format(row["PID"], row["PName"], row["PType"], row["PPrice"], result[0].get('count(PID)')))

            print(Performance.cHyphen)


    def print_performances(self):
        sql = "select * from Performance"
        result = self.SendQuery(sql)

        print(Performance.cHyphen)
        print(Performance.cPrintFormat.format("id", "name", "type", "price", "booked"))
        print(Performance.cHyphen)

        for row in result:
            sql = "SELECT count(SeatNo) from Booking Where PID=%s" % row["PID"]
            result = self.SendQuery(sql)
            print(Performance.cPrintFormat.format(row["PID"], row["PName"], row["PType"], row["PPrice"], result[0].get('count(SeatNo)')))

        print(Performance.cHyphen)

#--------------------------------------------------------
# konlo 공연장 class
#--------------------------------------------------------
class Building(MysqlDB):

    def __init__(self):
        super().__init__()

    def GetSQLAll(self):
        return ("select * from %s" % Building.TableName)

    # build을 생성함
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

    # buidling을 삭제한다.
    # 삭제 시 BID를 foreign key를 사용하는 것은 on delete cascade설정하여 자동 삭제 된다.
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
        #sql = "select * from Building"
        sql = """
              select B.*, IFNULL(CountTable.AssignCount, 0) as AssignCount
              from Building as B left join
                   (select BID, count(BID) as AssignCount from Assign group by BID) as CountTable
                    on (B.BID = CountTable.BID)
              """
        result = self.SendQuery(sql)

        print(PRINT_HYPHEN)
        PrintFormat = "{0:3}   {1:15}   {2:30}   {3:7}   {4:8}"
        print(PrintFormat.format("id", "name", "location", "captity", "assinged"))
        print(PRINT_HYPHEN)

        for row in result:
            print(PrintFormat.format(row["BID"], row["BName"], row["BLocation"], row["BMax"], row["AssignCount"]))

        print(PRINT_HYPHEN)


    # 해당하는 BID의 capacity를 전달한다.
    # 없는 경우는 None를 return 한다.
    # 반드시 BID가 존재하는지 확인 후에 호출 한다.
    def get_build_capacity(self, BID):
        MaxCapacity = None

        sql = "select BMax from Building where BID=%s" % BID
        result = self.SendQuery(sql)

        for row in result:
            MaxCapacity = row["BMax"]

        return MaxCapacity


# --------------------------------------------------------
# konlo : print seat number
# --------------------------------------------------------
class Assign(MysqlDB):
    def __init__(self):
        super().__init__()


    # 좌석을 출력한다. by konlo
    def print_seat_no(self):
        PID = int(input("Performance ID : "))
        sql = " select BMax, Assign.BID, Assign.PID from Building join Assign on (Building.BID = Assign.BID ) where PID = %s" % PID
        result = self.SendQuery(sql)

        #할당된 공연이 있다면 이 중에 Max capacity를 가져온다.
        if len(result) > 0 :
            for row in result :
                MaxCap = int(row["BMax"])

            #Seat 정보를 가져온다.
            sql = "select SeatNo, AID  from Booking where PID = %s " % PID
            SeatResult = self.SendQuery(sql)

            # seat number가 할당되지 않은 것이 있으니
            # 있는 값을 dinctionary 형으로 저장한다.
            SeatInfo = dict()
            for row in SeatResult :
                SeatInfo[int(row["SeatNo"])] = row["AID"]

            print(PRINT_HYPHEN)
            print("{0:40}    {1:20}".format("seat_number", "audience_id"))
            print(PRINT_HYPHEN)

            # 지정된 Capacity 만큼 seat number를 보여주면서
            # 할당된 AID가 있을 경우 출력한다.
            for i in range(1, MaxCap+1):
                # seat_number string
                SeatNumber = str(i)

                # DB에 없는 경우는 "" 처리
                if SeatInfo.get(i) == None:
                    AudenceID = ""
                # 추출된 data가 있는 경우는 SeatInfo에서 추
                else:
                    AudenceID = str(SeatInfo.get(i))

                print("{0:40}    {1:20}".format(SeatNumber, AudenceID))

            print(PRINT_HYPHEN)

        else:
            print(" PID %s is not assigned yet " % PID)




# --------------------------------------------------------
# rkdsktmf
# --------------------------------------------------------
class Audience(MysqlDB):

    hypen = "--------------------------------------------------------------------------------"
    def __init__(self):
        super().__init__()

    def print_aud(self):
        sql = "select AID, AName, AGender, AAge from Audience"
        result = self.SendQuery(sql)

        printformat = "{0:3}   {1:15}   {2:10}    {3:4}"

        print(Audience.hypen)
        print(printformat.format("AID", "AName", "AGender", "AAge"))
        print(Audience.hypen)

        for i in result:
            print(printformat.format(i["AID"], i["AName"], i["AGender"], i["AAge"]))

        print(Audience.hypen)

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

        sql = ("insert into Audience(AName, AGender, AAge) values ('%s', '%s', %s)"% (AName, Afm, AAge))
        self.ExecuteQuery(sql)

    def remove_aud(self):
        a = 1
        sql = "select AID from Audience"
        result = self.SendQuery(sql)

        printformat = "{0:3}"

        print(Audience.hypen)
        print(printformat.format("AID"))
        print(Audience.hypen)

        for i in result:
            print(printformat.format(i["AID"]))

        print(Audience.hypen)

        while (a > 0):
            AID = int(input("Delete ID : "))
            break

        sql = ("delete from Audience where AID = %s" % (AID))
        self.ExecuteQuery(sql)

    def book_aud(self):

        sql = "select AID from Audience"
        dbAID = self.SendQuery(sql)
        AIDlist = []

        for i in range(len(dbAID)):
            AIDlist  = AIDlist + list(dbAID[i].values())

        sql = "select PID from Performance"
        dbPID = self.SendQuery(sql)
        PIDlist = []
        for i in range(len(dbPID)):
            PIDlist  = PIDlist + list(dbPID[i].values())


        print("Audience ID list : ")

        print(Audience.hypen)
        print("{0:3}".format("AID"))
        print(Audience.hypen)

        for i in dbAID:
            print("{0:3}".format(i["AID"]))

        a = 1
        while (a>0):
            AID = int(input("Audience ID : "))
            for i in range(len(AIDlist)):
                if AIDlist[i] == AID:
                    a = 0
                    break
            if a != 0:
                print("Not exist ID. Check the ID")

        print("Performance ID list : ")

        print(Audience.hypen)
        print("{0:3}".format("PID"))
        print(Audience.hypen)

        for i in dbPID:
            print("{0:3}".format(i["PID"]))



        a = 1
        while (a>0):
            PID = int(input("Preformance ID : "))
            for i in range(len(PIDlist)):
                if PIDlist[i] == PID:
                    a = 0
                    break
            if a != 0:
                print("Not exist ID. Check the ID")


        sql = ("select SeatNo from Booking where PID = %s" % (PID))
        dbSeatNo = self.SendQuery(sql)
        Seatlist = []

        for i in range(len(dbSeatNo)):
            Seatlist  = Seatlist + list(dbSeatNo[i].values())

        Seatlist =sorted(Seatlist)

        print(Audience.hypen)
        print("{0:7}".format("SeatNo"))
        print(Audience.hypen)

        for i in range(len(Seatlist)):
            print(Seatlist[i])

        print(Audience.hypen)

        a = 1
        while (a>0):

            SeatNotemp = input("Seat Number : ")
            SeatNo = SeatNotemp.split(",")

            a = 0
            if SeatNo != ['']:
                for i in range(len(SeatNo)):
                    for j in range(len(Seatlist)):
                        if Seatlist[j] == int(SeatNo[i]):
                            print("Seat Number is duplicate. Please check Seat Number.")
                            a = 1
                            break

        for i in range(len(SeatNo)):
            sql = ("insert into Booking(PID, AID, SeatNo) values ('%s', '%s', %s)" % (PID, AID, int(SeatNo[i])))
            self.ExecuteQuery(sql)


        print("Successfully book a performance")

        sql = ("select PPrice from Performance where PID = %s" % (PID))
        dbPrice = self.SendQuery(sql)

        sql = ("select AAge from Audience where AID = %s" % (AID))
        dbAAgeTemp = self.SendQuery(sql)
        dbAAge = []

        for i in range(len(dbAAgeTemp)):
            dbAAge = list(dbAAgeTemp[i].values())

        dbAAge = int(dbAAge[0])

        print(dbAAge)
        if dbAAge < 8:
            print("Total ticket price is Free!!")
        elif dbAAge >= 7 and dbAAge < 13:
            print("Total ticket price is ", dbPrice * len(SeatNo) * 0.5)
        elif dbAAge >= 14 and dbAAge < 19:
            print("Total ticket price is ", dbPrice * len(SeatNo) * 0.8)
        else:
            print("Total ticket price is ", dbPrice * len(SeatNo))

    def print_book(self):
        sql = "select PID from Performance"
        dbPID = self.SendQuery(sql)
        PIDlist = []
        for i in range(len(dbPID)):
            PIDlist  = PIDlist + list(dbPID[i].values())

        print("Performance ID list : ")

        print(Audience.hypen)
        print("{0:3}".format("PID"))
        print(Audience.hypen)

        for i in dbPID:
            print("{0:3}".format(i["PID"]))

        print(Audience.hypen)

        printformat = "{0:3}   {1:15}   {2:10}    {3:4}"

        a = 1
        while (a>0):
            PID = int(input("Preformance ID : "))

            sql = ("SELECT Audience.AID, AName, AGender, AAge FROM Audience WHERE AID IN (SELECT DISTINCT AID FROM Booking, Performance WHERE Booking.PID = Performance.PID and Booking.PID = %s)" % (PID))
            check_book = self.SendQuery(sql)

            if check_book != ():
                a = 0
                print(Audience.hypen)
                print(printformat.format("id", "name", "gender", "age"))
                print(Audience.hypen)

                for i in check_book:
                    print(printformat.format(i["AID"], i["AName"], i["AGender"], i["AAge"]))

                print(Audience.hypen)

                break

            else:
                print("There is no reservation. Please check Performance ID")




def main():
    x = 1

  # building을 위한 객체 생성
    cBuilding = Building()
    cPerformance = Performance()
    cAssign = Assign()
    cAudience = Audience()
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
            cPerformance.print_performances()
        elif sel == '3':
            cAudience.print_aud()
        # 4. insert a new building
        elif sel == '4':
            cBuilding.insert_building()
            # menu4()
        # 5. remove a building
        elif sel == '5':
            # menu5()
            cBuilding.remove_building()
        elif sel == '6':
            cPerformance.insert_performance()
        elif sel == '7':
            cPerformance.remove_performance()
        elif sel == '8':
            cAudience.insert_aud()
        elif sel == '9':
            cAudience.remove_aud()
        elif sel == '10':
            cPerformance.assign_performance()
        elif sel == '11':
            cAudience.book_aud()
        elif sel == '12':
            cPerformance.print_assigned_performance()
        elif sel == '13':
            cAudience.print_book()
        elif sel == '14':
            cAssign.print_seat_no()
            #menu14()
        elif sel == '15':
            print('Bye!')
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
