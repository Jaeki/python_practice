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

def f10(num):
    for i in range(num):
        for j in range(0, i+1):
            print('*',end='')
        print()
def f10_1(num):
    for i in range(0, num):
        print('*' * (i+1))

def f14(list):
    neg=0
    for i in range(0,len(list)):
        if list[i] < 0:
            neg = i;
    print(neg)

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
