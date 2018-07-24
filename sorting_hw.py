import random

def selection_sort(lst):
    n=len(lst)
    for bottom in range(n-1):
        mp=bottom
        for i in range(bottom+1, n):
            if lst[i] < lst[mp]:
                mp = i
        lst[bottom], lst[mp] = lst[mp], lst[bottom]

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
    index_a =0
    index_b =0
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
data_10 = random.sample(range(100000),10)
data_100 = random.sample(range(100000),100)
data_1000 = random.sample(range(100000),1000)
data_10000 = random.sample(range(100000),10000)
print(data_10)
print(insertion_sort(data_10))
