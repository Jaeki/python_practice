#1
def count_matches(lst,value):
    if len( lst ) < 2:
        if len(lst) ==0:
            return 0
        elif lst[0] == value:
            return 1
        else:
            return 0
    return count_matches( [lst[0]], value) +  count_matches(lst[1:], value)

# print(count_matches([0,1,0,4,2,0],0))
# print(count_matches(["a","b","c"],1))
# print(count_matches([],"a"))


#2
def double_each(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst[0]] * 2
    return double_each( [lst[0]] ) +  double_each( lst[1:] )

# nums = [1,2,3]
# print(double_each(nums))
# print(nums)
# print(double_each([]))


#3
def sums_to(items, n):
    if items == [] :
        if n == 0:
            return True
        else:
            return False

    return sums_to(items[1:], n-items[0])

# nums = [1,2,3]
# print(sums_to(nums, 6))
# print(sums_to(nums, 5))
# print(sums_to([], 1))
#4
def is_reverse(str1,str2):
    a = ''
    for i in range(len(str1)):
        a = a + str1[-1]
        str1 = str1[:len(str1)-1]
    if a == str2:
        return True
    else:
        return False

# print(is_reverse("abc","cba"))
# print(is_reverse("abc","abc"))
# print(is_reverse("abc","dcba"))
# print(is_reverse("abc","cb"))
# print(is_reverse("",""))


#5
def sort_repeated(items):

    resultList = []
    setValue = set(items)

    for value in setValue:
        if items.count(value) >= 2:
            resultList.append(value)

    return sorted(resultList)


# print(sort_repeated([1,2,3,2,1]))
# print(sort_repeated([1,2,3,2, 2,4]))
# print(sort_repeated([2]))

#6
# make dic number without get
def make_Dict_number(items):
    result = {}
    for value in items:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result

# make dic number with get
def make_Dict_number_with_get(items):
    result = {}
    for value in items:
        if result.get(value):
            result[value] += 1
        else:
            result[value] = 1
    return result


# result = make_Dict_number([2,5,3,4,6,4,2,4,5])
# print(result)
#
#
# result = make_Dict_number_with_get([2,5,3,4,6,4,2,4,5])
# print(result)

# frequent
def mostFrequent(items):
    result = {}
    for value in items:
        if result.get(value):
            result[value] += 1
        else:
            result[value] = 1


    MaxCount = max(result.values())

    for key, value in result.items():
        if(value == MaxCount):
            return key

# print(mostFrequent([2,5,3,4,6,4,2,4,5]))

#7




def histogram(d):
    a = list(d.values())
    b = {}
    for i in range(len(a)):
        b[a[i]] = 0
        for j in range(len(a)):
            if a[i] == a[j]:
                b[a[i]] = b[a[i]] + 1
    return b

# letters = {1:"a",2:"b",3:"c"}
# print(histogram(letters))
# letters = {1:"a", 2:"b", 3:"c"}
# print(histogram(letters))
# letters[4] = "a"
# letters[5] = "b"
# letters[6] = "a"
# print(histogram(letters))
