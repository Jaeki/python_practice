# for range를 이용해서 range를 이용하기
def f2(n):
    print_value = 1
    for i in range(n+1):
        print_value += i
        print(list(map(lambda x : x+print_value , range(i+1))))

#f2(2)
