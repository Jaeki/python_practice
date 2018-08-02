#resursive 하게 풀것!
#1 Searching
def first_perfect_square(list):
    for i in range(0,len(list)):
        if list[i] >= 0:
            if list[i]**0.5 - int(list[i]**0.5) == 0:
                return i
    return -1

# print(first_perfect_square(list(range(5))))
# print(first_perfect_square([2,4,6,8,10,12]))
# print(first_perfect_square([6,8,10,12,9]))
# print(first_perfect_square([1,1]))
# print(first_perfect_square([-6, 6, -2, 2, -3, 3]))
# print(first_perfect_square([42]))
# print(first_perfect_square([]))
# print(first_perfect_square([1231241234123123**2]))

#2 Counting
def num_perfect_squares(list):
    count=0
    for i in range(0,len(list)):
        if list[i] >= 0:
            if list[i]**0.5 - int(list[i]**0.5) == 0:
                count+=1
    print(count)


# num_perfect_squares([])
# num_perfect_squares([0])
# num_perfect_squares([0,1])
# num_perfect_squares(list(range(10)))
# num_perfect_squares([3]*10)
# num_perfect_squares([4]*10)
# num_perfect_squares([-4,-2,0,2,4])

#3 Second largest
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

# second_largest([3,-2,10,-1,5])
# second_largest([-2,1,1,-3,5])
# second_largest([1,2,3,3])
# second_largest(["alpha","gamma","beta","delta"])
# second_largest([3.1,3.1])
# second_largest([True,False, False, True])
# second_largest([False, False, True])

# print french for the numbers between lo and hi (inclusive)

def digit(num, pos):
    return (num // 10**(pos-1)) % 10

def num_in_french(num): # assumes 0 <= num <= 100
    ones_list = ["zero", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "treize",
                 "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"]
    tens_list = ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante", "quatre-vingt", "quatre-vingt"]

    # part 2 조건의 값
    part2_list = list(range(0,20)) +[ 100 ]
    # part 4-1
    part4_1_list = list(range(70,80))
    part4_2_list = list(range(80,97))
    part4_3_list = list(range(97,100))
    part5_list = [20,30,40,50,60]
    part6_list = [21,31,41,51,61]

    digit_0 = digit(num, 2)
    digit_1 = digit(num, 1)

    # Part 2: fill in code below for numbers 1, 2, 3, ..., 19 and 100
    if num in part2_list:
        #print(num_in_french(i))
        if num == 100:
            French = "cent"
        else:
            French = ones_list[num]

        print(num,  French)

    # Part 4: case when the numbers are 70, 71, 72, ..., 79 and 90, 91, 92, ..., 99
    elif num in part4_1_list:
        # 60을 뺀 값을 따로 저장한다.
        rest_value = num - 60

        # 71를 위해서 et 생성
        if digit_1 == 1:
            And_ET = " et "
        # 그렇지 않을 경우 '-'
        else:
            And_ET = "-"
        print(num, " ", tens_list[6],  And_ET, ones_list[rest_value] , sep="")

    # part 4-2 : 80, 91, 92, ..., 96
    elif num in part4_2_list:

        rest_value = num - 80
        if( num == 80):
            End_Ones = "s"
        else:
            End_Ones = "-" + ones_list[rest_value]
        print(num, " ", ones_list[4], "-", tens_list[2], End_Ones, sep="")

    # part 4-3 97, 98, 99
    elif num in part4_3_list:
        rest_value = num - 90

        End_Ones = "-" + ones_list[rest_value]

        print(num, " ", ones_list[4], "-", tens_list[2], "-", tens_list[1], End_Ones, sep="")
    # Part 5: otherwise the case when the numbers are 20, 30, 40, 50, 60
    elif num in part5_list:
        print(num,  tens_list[digit_0])
    # Part 6: otherwise the case when the numbers are 21, 31, 41, ...
    elif num in part6_list:
        print(num,  tens_list[digit_0], "et", ones_list[digit_1])
    # 나머지는 tens 와 ones 형태로 출력
    else:
        print(num, " ", tens_list[digit_0], "-", ones_list[digit_1], sep="")

def print_french(start, end):
    numList = range(start, end+1)
    for i in numList:
        num_in_french(i)

#print_french(0,3)
#print_french(0,100)
#print_french(100, 100)
    # Part 1: get the ones and tens digits of num
    # Part 2: fill in code below for numbers 1, 2, 3, ..., 19 and 100
    # Part 4: case when the numbers are 70, 71, 72, ..., 79 and 90, 91, 92, ..., 99
    # Part 5: otherwise the case when the numbers are 20, 30, 40, ...
    # Part 6: otherwise the case when the numbers are 21, 31, 41, ...
    # Part 7: everything else, the most general case for 22, 23, ..., 29, 32,
