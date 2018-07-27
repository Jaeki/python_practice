#page 117
def f2(items):
    # 조건을 만족하는 것을 찾는것이기 때문에 filter를 사용한다.
    print(*list(filter(lambda x: (x % 2) == 1, items )), sep="\n")

#f2([1,2,3,4])
#f2([1,2,3,4,5])

# konlo
def f4(items):
    # list에서 index를 필요로 할 때는 enumerate를 같이 사용해서 처리 한다.
    return sum(list(map(lambda x: x[0] if x[1] % 2 == 1 else 0, enumerate(items))))

#print(f4([1,2,3,4]))
#print(f4([1,2,3,4,5]))



def f6(items):

    return max(items)

#print(f6([1,2,3,4]))
#print(f6([1,2,3,4,5]))

def f8(a, b, n):
    #print(*list(filter(lambda x : x % n == 0, range(a,b+1))), sep="\n")
    print(*(filter(lambda x: x % n == 0, range(a, b + 1))), sep="\n")
#f8(1,10,2)
#f8(1,10,11)
#f8(1,10,7)

#konlo check 필요 map만으로는 print를 하지 않음.
def f10(n):
    print(*list(map(lambda x : "*" * x, range(1, n+1))), sep="\n")
#f10(2)
#f10(3)


def f12(items):
    resut = all(list(map(lambda x : x < 0 , items)))
    return result

#print(f12([]))
#print(f12([-1, -2, -3, -4, 5]))
#print(f12([1, 2, 3, 4, 5]))
#print(f12([-1, -2, -3]))

def f14(items):
    last_index = 0
    #a = list(map(lambda x , y: last_index = y x < 0 , enumerate(items)))
    # [-1] 은 list의 마지막을 접근하기 위한 것으로
    return list(filter(lambda x : x[1] <0, enumerate(list)))[-1][0]
#f14([1,2,-3])


#konlo range를 이용해서 역으로 화면 출력
# 역시 list를 넣어야만 화면에 출력이 됨
def f16(n):

    list(map(lambda x : print("*" *x), range(n,0,-1)))

#f16(3)
#f16(2)
#szf16(1)


import math
def f18(n):

    return math.factorial(n)

#print(f18(5))

def f20(matrix):
    #list(filter(lambda x:  , ))
    print(*list(map(lambda x : x[1][x[0]], enumerate(matrix))), sep="\n")
    # lambda x : matrix[x][x]
#f20([[1,2,3], [4,5,6], [7,8,9]])

def f22(items):
    print(*(map(lambda x  : list(range(x, -1, -1)), items)), sep="\n")
#f22([1,3,5])

# konlo filter 조건에 맞는 것만 list에서 추출
def f24(n):
    print(*list(filter(lambda x: (x % 2) == 0 or (x %3) == 0, range(1,abs(n) + 1))), sep="\n")

#f24(10)
#f24(1)
#f24(3)

# konlo 
# 조건에 무조건 2개 이상 unique 하다고 했음 그래서 바로 sortedList[1] return 함
def f26(items):
    sortedList = sorted(items, key=None, reverse=True)
    return sortedList[1]

#print(f26([1,4,3,2,5]))
#print(f26([3,2]))
#print(f26([3,4]))

# konlo
# matrix에 row로 input 합니다.
def f28(items):
    print(*list (map(lambda x : max(x), items)), sep="\n")
f28([[1,2,3], [4,5,6], [7,8,9]])
f28([[3,2,1], [0,-1, -2]])
f28([[1,2,3,4], [1],[34], [2], [3], [56], [67]])
