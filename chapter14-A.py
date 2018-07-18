#resursive 하게 풀것!
def first_perfect_sqaure(list):
    for i in range(0,len(list)):
        if list[i] >= 0:
            if list[i]**0.5 - int(list[i]**0.5) == 0:
                return print(i)
    return -1

# first_perfect_sqaure([6,8,10,12,9])

def num_perfect_squares(list):
    count=0
    for i in range(0,len(list)):
        if list[i] >= 0:
            if list[i]**0.5 - int(list[i]**0.5) == 0:
                count+=1
    print(count)

# num_perfect_squares([4]*10)
# num_perfect_squares([])
# num_perfect_squares([0])
# num_perfect_squares([0,1])
# num_perfect_squares(list(range(10)))
# num_perfect_squares([3]*10)

def second_largest(lst):
    largest = lst[0]
    second_largest = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > largest:
            second_largest = largest
            largest = lst[i]
        elif lst[i] > second_largest:
            second_largest = lst[i]
    return print(second_largest)

second_largest([3,-2,10,5])
second_largest([-2,1,1,-3,5])
second_largest([1,2,3,3])
second_largest(["alpha","gamma","beta","delta"])
second_largest([3.1,3.1])
second_largest([True,False, False, True])
second_largest([False, False, True])
