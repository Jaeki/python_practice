import random

def selection_sort(list):
    n=len(list)
    for bottom in range(n-1):
        mp=bottom
        for i in range(bottom+1, n):
            if list[i] < list[mp]:
                mp = i
            list[bottom], list[mp] = list[mp], list[bottom]

def insertion_sort(list):
    pass

def bubble_sort(list):
    pass

def merge_sort(list):
    pass

def quick_sort(list):
    pass

data = random.sample(100)
print(data)
