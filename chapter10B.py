# for range를 이용해서 range를 이용하기
def f2(n):
    print_value = 1
    for i in range(n+1):
        print_value += i
        print(list(map(lambda x : x+print_value , range(i+1))))

#f2(2)



def f6(matrix):
    result = []
    for row in matrix:
        result += list(map(lambda x : x , row))
    print(sum(result))

#f6([[1,0], [0,1]])
#f6([[1,2,3], [4,5,6]])
#f6([[1],[2],[3],[4]])

def f8(matrix):
    for row in matrix:
        result = list(filter(lambda x : x % 2 == 1 , row))
        print(*result)

#f8([[1,0], [0,1]])
#f8([[1,2,3], [4,5,6]])
#f8([[1],[2],[3],[4]])

def f10(matrix1, matrix2):
    result_row_len = len(matrix1)
    result_column_len = len(matrix2[0])
    sum_len = len(matrix2)
    resultValue = []

    for i in range(result_row_len):
        rows = []
        for j in range(result_column_len):
            rows.append(0)
        resultValue.append(rows)

    # print("{0} x {1}, {2} ".format(result_row_len,result_column_len, sum_len))

    for i in range(result_row_len):
        for j in range(result_column_len):
            resultValue[i][j] = sum(list(map(lambda x : matrix1[i][x] * matrix2[x][j], range(sum_len))))
    return resultValue


#print(f10([[1,0],[0,1]],[[1,0],[0,1]]))
#print(f10([[1,2,3],[4,5,6]],[[-1,-1],[-1,-1],[-1,-1]]))
#print(f10([[4,3,2,1]],[[1],[2],[3],[4]]))


def f12(rows, cols):
    returnValue = []
    for row in range(rows):
        #adjact_value = []

        result = list(map(lambda x : int(row - 1 >= 0) + int(row + 1 < rows) + int(x - 1 >= 0) + int(x + 1 < cols), range(cols)  ))
        returnValue.append(result)

    return returnValue

#print(f12(3,3))
#print(f12(5,1))
#print(f12(5,0))
#print(f12(0,5))
#print(f12(2,2))
