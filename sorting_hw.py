import random
import time
import copy

def selection_sort(lst):
    n=len(lst)
    for bottom in range(n-1):
        mp=bottom
        for i in range(bottom+1, n):
            if lst[i] < lst[mp]:
                mp = i
        lst[bottom], lst[mp] = lst[mp], lst[bottom]

    return lst

def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j-= 1
    return lst


def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def merge(a, b):
    index_a = 0
    index_b = 0
    c=[]
    while index_a < len(a) and index_b < len(b):
        if a[index_a] <= b[index_b]:
            c.append(a[index_a])
            index_a = index_a +1

        else:
            c.append(b[index_b])
            index_b = index_b +1
    c.extend(a[index_a:])
    c.extend(b[index_b:])
    return c

def merge_sort(lst):

    if len(lst) == 0 or len(lst) ==1:
        return lst[:len(lst)]

    halfway = len(lst) // 2
    lst1 = lst[0:halfway]
    lst2 = lst[halfway:len(lst)]
    newlst1 = merge_sort(lst1)
    newlst2 = merge_sort(lst2)
    newlst = merge(newlst1, newlst2)
    return newlst


def quick_sort(lst):
    if len(lst) > 1:
        pivot_index = len(lst) //2
        smaller_lst = []
        larger_lst = []

        for i, val in enumerate(lst):
            if i != pivot_index:
                if val < lst[pivot_index]:
                    smaller_lst.append(val)
                else:
                    larger_lst.append(val)

        quick_sort(smaller_lst)
        quick_sort(larger_lst)
        lst[:] = smaller_lst + [lst[pivot_index]] + larger_lst

    return lst


# 100 개의 random number 생성
data_100 = random.sample(range(100000),100)
data_1000 = random.sample(range(100000),1000)
data_10000 = random.sample(range(100000),10000)



# start = time.time()
#
#
# print(selection_sort(data_10000))
#
# end = time.time()
# settime = end - start
# print(settime)

test = [selection_sort, bubble_sort, insertion_sort, merge_sort, quick_sort, sorted ]


for i in range(0,6):
    start = time.time()
    a = copy.deepcopy(data_10000)
    print(test[i](a))
    end = time.time()
    settime = end - start
    print(settime)

# 100개
# print(selection_sort(data_100,0))
# print(bubble_sort(data_100,0))
# print(insertion_sort(data_100,0))
# print(merge_sort(data_100))
# print(quick_sort(data_100,0))
# print(sorted(data_100,0))
#
# # 1000 개
# print(selection_sort(data_1000,0))
# print(bubble_sort(data_1000,0))
# print(insertion_sort(data_1000,0))
# print(merge_sort(data_1000,0))
# print(quick_sort(data_1000,0))
# print(sorted(data_1000))
#
# # 10000개
# print(selection_sort(data_10000,0))
# print(bubble_sort(data_10000,0))
# print(insertion_sort(data_10000, 0))
# print(merge_sort(data_10000, 0))
# print(quick_sort(data_10000, 0))
# print(sorted(data_10000))
