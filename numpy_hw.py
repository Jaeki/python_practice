#8/10(금) 제출
import numpy as np
#(1) Create an array of size 10 filled with 0

arr = np.zeros(10)
print(arr)

#(2) Set fifth value to 1 from above array

arr[4] = 1
print(arr)

#(3) Create an array with values ranging from 10 to 49

arr = np.arange(10,49)
print(arr)

#(4) Create a 5*5 matrix with values ranging from 0 to 24

arr = np.array(range(0,25)).reshape((5,5))
# help(np.reshape)
print(arr)

#(5) Create a 5*5 identity matrix
arr=np.eye(5)
print(arr)

#(6) 5*5 array with random values and find the min and max val
arr = np.random.randint(0,100,25).reshape((5,5))
print(arr)
print(arr.min())
print(arr.max())

#(7) 4*3 mat with 1, 3*2 mat with random num, and multiply
arr1 = np.ones((4,3))
arr2 = np.random.randint(0,100,6).reshape((3,2))
result = np.matmul(arr1, arr2)
print(arr1)
print(arr2)
print(result)

#(8) transpose the above result

t_result = np.transpose(result)
print(t_result)

#(9) create two mat and add and sub
arr1 = np.arange(0,25).reshape((5,5))
arr2 = np.arange(25,50).reshape((5,5))
result_add = arr1+arr2
result_sub = arr2-arr1
print(result_add)
print(result_sub)
