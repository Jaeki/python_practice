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

def double_each(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst[0]] * 2
    return double_each( [lst[0]] ) +  double_each( lst[1:] )

# print(double_each([1,2,3]))
#???
def sums_to(nums, k):
    tmp = nums.pop()
    if len(nums) ==0:
        if k-tmp == 0:
            return True
        else:
            return False
    return sums_to(nums, k-tmp)

print(sums_to([1,2,3], 6))

def sort_repeated(lst):
    count=0
    temp = set()
    for i in range(len(lst)):
        if lst.count(lst[i]) > 1:
            temp.add(lst[i])
    print(temp)


# sort_repeated([1,2,3,2,1])

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
