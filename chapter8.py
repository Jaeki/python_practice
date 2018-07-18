def f2(lst):
    print(*list(filter(lambda x: x%2==1, lst)), sep='\n')
#f2([1,2,3,4,5])

def f6(lst):
    return max(lst)

#print(f6([1,2,3,4]))

def f8(a,b,n):
    print(*filter(lambda x: x%n==0, range(a,b+1)), sep='\n')

def f12(lst):
    return all(map(lambda x: x<0, lst))

def f14(lst):
    return list(filter(lambda x:x[1]<0, enumerate(lst)))[-1][0]
    # -1은 마지막 인덱스
#f8(1,10,2)
#print(f12([-1,-2,-3,4]))
# print(f14([1,-2,-3,1,-2,-3]))
import math
def f18(n):
    return math.factorial(n)

def f20(matrix):
    #print(*list(map(lambda x: x[1][x[0]], enumerate(matrix))), sep='\n')
    print(*map(lambda x: matrix[x][x], range(len(matrix))), sep='\n')



#f20([[1,2,3],[4,5,6],[7,8,9]])

def f22(lst):
    print(*list(map(lambda x: list(range(x, -1, -1)), lst)), sep='\n')

# f22([1,3,5])

def f6b(matrix):
    return sum(list(map(lambda x: sum(x), matrix)))

def f8b(matrix):
    for i in range(0, len(matrix)):
        print(*list(filter(lambda x: x%2==1, matrix[i])), sep=' ')
# print(f6b([[1,0],[0,1]]))

f8b([[1,2,3],[4,5,6]])
