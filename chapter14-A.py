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

# second_largest([3,-2,10,5])
# second_largest([-2,1,1,-3,5])
# second_largest([1,2,3,3])
# second_largest(["alpha","gamma","beta","delta"])
# second_largest([3.1,3.1])
# second_largest([True,False, False, True])
# second_largest([False, False, True])

# print french for the numbers between lo and hi (inclusive)
def print_french(lo, hi):
    return None

def digit(num, pos):
    return (num // 10**(pos-1)) % 10

def num_in_french(num): # assumes 0 <= num <= 100

    ones_list = ["zero", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "treize",
                 "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"]

    tens_list = ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante", "quatre-vingt", "quatre-vingt"]

    # Part 1: get the ones and tens digits of num
    # Part 2: fill in code below for numbers 1, 2, 3, ..., 19 and 100
    # Part 4: case when the numbers are 70, 71, 72, ..., 79 and 90, 91, 92, ..., 99
    # Part 5: otherwise the case when the numbers are 20, 30, 40, ...
    # Part 6: otherwise the case when the numbers are 21, 31, 41, ...
    # Part 7: everything else, the most general case for 22, 23, ..., 29, 32,
