import random

def selection_sort(lst):
    n=len(lst)
    for bottom in range(n-1):
        mp=bottom
        for i in range(bottom+1, n):
            if lst[i] < lst[mp]:
                mp = i
        lst[bottom], lst[mp] = lst[mp], lst[bottom]

def insertion_sort(list):
    pass

def bubble_sort(list):
    pass

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

def quick_sort(list):
    pass

# 100 개의 random number 생성
data_100 = random.sample(range(100000),100)
data_1000 = random.sample(range(100000),1000)
data_10000 = random.sample(range(100000),10000)
print(data_100)
print(merge_sort(data_100))
