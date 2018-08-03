import copy
import random

L = [1,[4,5,6]]
A = L
S = copy.copy(L)
D = copy.deepcopy(L)
# print(A, L, S, D)

A[1][2] = 100
# print(A, L, S, D)

S[0]=9
# print(A, L, S, D)

D[1]=[100,200,300]
# print(A, L, S, D)

colors = ['red', 'blue', 'green', 'gray', 'black']
result = []
# for i in range(5):
    # result = (random.choice(colors))
# print(result)
def umbrella(p):
    wet=False
    trips=0
    location=0
    umbrellas=[1,1]
    while (not wet):
        if random.random() < p:
            if umbrellas[location] == 0:
                wet=True
            else:
                trips = trips + 1
                umbrellas[location]-=1
                location = 1 - location
                umbrellas[location]+=1
        else:
            trips += 1
            location = 1 - location
    return trips

# for i in range(500):
#     print(umbrella(0.5))


class Performance(object):
    def __init__(self):
        pass
    #register a new performance
    def register(self, id, name, type, price):
        self.id = id
        self.name = name
        self.type = type
        self.price = price
        #insert a record into the performance table
        sql = "insert into Performance(PID, PName, AAge) values (%s, %s, %s)"
        cursor.execute(sql, (AName, Afm, int(AAge)))
        connection.commit()

    def search():
        pass

    def book():
        pass

perf = Performance()

class BaseClass(object):
    def printHam(self):
        print('ham')

class InheritingClass(BaseClass):
    pass

x=InheritingClass()
# x.printHam()

class Ph:
    varr1=333;
    varr2=444;
    def __init__(self):
        self.y=5
        self.z=5

    def printHam(self):
        print("Ham")

# s=Ph()
# s.printHam()
# print(s.y)
# print(s.z)
# s1=Ph()
# s1.varr2 = 666
# print(s1.varr2)
# print(dir(object))

class Person:
    def __init__(self, name):
        self.name = name
        print('this is constructor')

    def Sayhello(self):
        print('Hello, my name is ', self.name )

    def __del__(self):
        print('%s says bye.' % self.name)

# A=Person("Jaeki")
# print(A.name)
# A.Sayhello()
# # del A
# B = copy.copy(A)
# B.Sayhello
#Test commit