def f6_2(n):
    count =1
    for i in range(n):
        for j in range(i+1):
            print(count, end='')
            count+=1
        print()

#f6_2(3)
def f6_6(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i==j:
                print(matrix[i][j])

#f6_6([[1,0],[0,1]])
f6_6([[1,2,3],[4,5,6],[7,8,9]])
