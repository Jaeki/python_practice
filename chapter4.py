def f2(list):
    for n in range(len(list)):
        if list[n]%2 == 1:
            print(list[n])

#f2([1,2,3,4])

def f4(list):
    #print(len(list))
    sum=0
    for i in range(0, len(list)):
        if list[i]%2 == 1:
            sum+=i
    return sum

def f6(list):
    big = list[0]
    for i in range(1, len(list)):
        if big < list[i]:
            big = list[i]
    return big

def f8(a,b,n):
    for i in range(a,b+1):
        if i % n == 0:
            print(i)

#f8(1,10,2)

def f10(num):
    for i in range(num):
        for j in range(0, i+1):
            print('*',end='')
        print()

#def f10_1(num):
#    for i in range(0, num):
#        print('*' * (i+1))

def f12(list):
    neg=False
    for n in range(len(list)):
        if list[n] < 0:
            neg=True
        else:
            neg=False
            break
    print(neg)
#f12([-1,-2,-3])

def f14(list):
    neg=0
    for i in range(0,len(list)):
        if list[i] < 0:
            neg = i;
    print(neg)

def f16(num):
    for i in range(num, 0, -1):
        print('*' * (i))
#f16(5)
def f18(num):
    val=1
    for n in range(num, 0, -1):
        val*=n
    print(val)

#f18(5)

def f20(list):
    for n in range(len(list)):
        for count in range(list[n], -1, -1):
            print(count,end=' ')
        print()

#f20([5,3,6,2])

#2와 3의 배수만 출력
def f22(n):
    for n in range (1, n+1):
        if n%2 == 0 or n%3 == 0:
            print(n)

#f22(10)

def f24(list):
    temp = sorted(list)
    print(temp[len(list)-2])

#f24([1,4,3,2,5])
#f24([3,4])

def f26(list):
    for i in range(0, len(list)):
        max = list[i][0]
        for j in range(0, len(list[i])):
            if list[i][j] > max:
                max = list[i][j]
        print(max)
#f14([1,2,-3])
#f14([1,-2,-3,1,-2,-3])
#f14([-1,1,1,1])
#f10_1(3)
#f26([[1,2,3],[4,5,6],[7,8,9]])
#f26([[1,2,3,4],[1],[34],[2],[3],[56],[67]])
