def f2(n):
    count =1
    for i in range(n):
        for j in range(i+1):
            print(count, end=' ')
            count+=1
        print()
#f2(5)
def f4(n):
    count =1
    for i in range(n):
        for j in range(i+1):
            print(count, end=' ')
            count+=1
        print()
    for i in range(n-1, 0, -1):
        for j in range(i):
            print(count, end=' ')
            count+=1
        print()
#f4(5)

def f6(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i==j:
                print(matrix[i][j])

#f6([[1,0],[0,1]])
#f6([[1,2,3],[4,5,6],[7,8,9]])
def f8(matrix):
    sum=0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum+=matrix[i][j]
    print(sum)

#f8([[1,2,3],[4,5,6]])
#f8([[1],[2],[3],[4]])

def f10(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]%2 == 1:
                print(matrix[i][j],end= ' ')
        print()

#f10([[1,2,3],[4,5,6]])
#f10([[1],[2],[3],[4]])
def f12(matrix1, matrix2):
    #Kang Na Suel
    pass

def f14(rows, cols):
    #Na Jong Sung
    pass
